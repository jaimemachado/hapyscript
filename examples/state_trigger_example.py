"""
Example State Trigger Automation

This script demonstrates how to trigger an automation based on state changes.
It monitors a light entity and logs when it changes state.

Usage:
    1. Update the entity_id to match your Home Assistant setup
    2. Copy to config/pyscript/ directory
    3. Reload pyscript

The script will automatically trigger when the monitored entity changes state.
"""

# Replace with your actual entity_id
MONITORED_ENTITY = "light.living_room"

@state_trigger(f"{MONITORED_ENTITY}")
def light_state_changed(var_name=None, value=None, old_value=None):
    """
    Triggered when the monitored light changes state.
    
    Args:
        var_name: The entity_id that changed
        value: The new state value
        old_value: The previous state value
    """
    log.info(f"Light state changed from {old_value} to {value}")
    
    if value == "on" and old_value == "off":
        log.info(f"{MONITORED_ENTITY} was turned on")
    elif value == "off" and old_value == "on":
        log.info(f"{MONITORED_ENTITY} was turned off")
