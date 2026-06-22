"""Button-driven light brightness stepper for Home Assistant pyscript.

Register a button and a list of lights, then each button press increases
brightness by 25% (configurable). When the next step reaches 100%,
all lights in the group are turned off.
"""

from stubs.pyscript_builtins import event_trigger, service, state
from stubs.pyscript_generated import light


class BrightnessStepper:
    """Cycles a group of lights through brightness levels on button presses."""

    def __init__(self, button_entity: str, light_entities: list[str], step_pct: int = 25):
        self.button_entity = button_entity
        self.light_entities = light_entities
        self.step_pct = max(1, min(int(step_pct), 100))

    def _current_brightness_pct(self) -> int:
        """Estimate current brightness from configured lights (0-100)."""
        current = 0
        for entity_id in self.light_entities:
            try:
                light_state = state.get(entity_id)
                attrs = state.getattr(entity_id) or {}
            except Exception:
                continue

            if light_state != "on":
                continue

            brightness = attrs.get("brightness")
            if brightness is None:
                # Some lights expose only on/off. Treat on as full brightness.
                current = max(current, 100)
                continue

            pct = int(round((float(brightness) / 255.0) * 100.0))
            current = max(current, max(0, min(pct, 100)))

        return current

    def handle_press(self) -> None:
        """Apply one brightness step, turning lights off at 100%."""
        if not self.light_entities:
            log.warning("brightness_stepper: no lights configured for %s", self.button_entity)
            return

        next_pct = self._current_brightness_pct() + self.step_pct

        if next_pct >= 100:
            for entity_id in self.light_entities:
                light.turn_off(entity_id=entity_id)
            log.info(
                "brightness_stepper: %s reached 100%%, turning off %s",
                self.button_entity,
                ", ".join(self.light_entities),
            )
            return

        for entity_id in self.light_entities:
            light.turn_on(entity_id=entity_id, brightness_pct=next_pct)

        log.info(
            "brightness_stepper: %s -> set %s to %s%%",
            self.button_entity,
            ", ".join(self.light_entities),
            next_pct,
        )


STEPPERS: dict[str, BrightnessStepper] = {}


def _parse_lights(lights: str) -> list[str]:
    return [entity.strip() for entity in lights.split(",") if entity.strip()]


def _extract_state_value(state_obj):
    """Handle both dict-like and object-like state payloads from events."""
    if state_obj is None:
        return None

    if isinstance(state_obj, dict):
        return state_obj.get("state")

    return getattr(state_obj, "state", None)


@service()
def brightness_stepper_register(button_entity: str, lights: str, step_pct: int = 25):
    """Register/update a button brightness stepper.

    Args:
        button_entity: Button entity id to listen to (for example input_button.room_dimmer).
        lights: Comma-separated light entities (for example "light.a, light.b").
        step_pct: Increment step in percent (defaults to 25).
    """
    light_entities = _parse_lights(lights)
    if not light_entities:
        raise ValueError("lights must include at least one light entity")

    STEPPERS[button_entity] = BrightnessStepper(button_entity, light_entities, step_pct=step_pct)
    log.info(
        "brightness_stepper: registered %s with lights [%s], step=%s%%",
        button_entity,
        ", ".join(light_entities),
        step_pct,
    )


@service()
def brightness_stepper_unregister(button_entity: str):
    """Unregister a previously configured brightness stepper."""
    if STEPPERS.pop(button_entity, None) is None:
        log.warning("brightness_stepper: no stepper registered for %s", button_entity)
        return

    log.info("brightness_stepper: unregistered %s", button_entity)


@service()
def brightness_stepper_press(button_entity: str):
    """Manually run one step for a registered button (useful for testing)."""
    stepper = STEPPERS.get(button_entity)
    if not stepper:
        raise ValueError(f"no stepper registered for {button_entity}")

    stepper.handle_press()


@event_trigger("state_changed")
def _brightness_stepper_button_listener(
    entity_id=None,
    old_state=None,
    new_state=None,
    **kwargs,
):
    """React to state changes for registered button entities."""
    stepper = STEPPERS.get(entity_id)
    if not stepper:
        return

    old_value = _extract_state_value(old_state)
    new_value = _extract_state_value(new_state)

    # Ignore attribute-only updates where the button state value did not change.
    if old_value == new_value:
        return

    stepper.handle_press()
