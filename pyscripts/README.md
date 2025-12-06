# PyScripts Directory

This directory contains individual automation scripts for Home Assistant.

## Adding Scripts

Place your `.py` files in this directory. Each file will be loaded by Pyscript when Home Assistant starts or when you reload Pyscript.

## Structure

- Each script should be self-contained
- Use descriptive filenames (e.g., `living_room_lights.py`, `morning_routine.py`)
- Add docstrings to explain what each script does
- Use decorators to define triggers:
  - `@service` - Create a callable service
  - `@state_trigger` - Trigger on entity state changes
  - `@time_trigger` - Trigger at specific times
  - `@event_trigger` - Trigger on Home Assistant events

## Examples

See the [examples/](../examples/) directory for template scripts you can use as a starting point.

## Best Practices

1. **Keep scripts focused**: One script per automation or related group of automations
2. **Document your code**: Add comments explaining why you're doing something
3. **Use logging**: Use `log.info()`, `log.warning()`, and `log.error()` for debugging
4. **Test thoroughly**: Test scripts before deploying to production
5. **Handle errors**: Use try/except blocks for robust automations
