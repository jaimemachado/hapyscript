# Modules Directory

This directory contains shared code, utilities, and helper functions that can be imported by your pyscripts.

## Purpose

Use the `modules/` directory for:
- Shared utility functions
- Common constants
- Helper classes
- Reusable code across multiple scripts

## Usage

Create Python modules that can be imported by your scripts:

```python
# modules/helpers.py
def format_temperature(temp, unit="C"):
    """Format temperature with unit."""
    return f"{temp}°{unit}"

def is_daytime():
    """Check if it's currently daytime."""
    # Implementation here
    pass
```

Then import in your scripts:

```python
# pyscripts/my_automation.py
from modules.helpers import format_temperature, is_daytime

@service
def temperature_alert():
    temp = state.get("sensor.outdoor_temp")
    formatted = format_temperature(temp)
    log.info(f"Current temperature: {formatted}")
```

## Best Practices

1. **Keep modules focused**: Each module should have a clear purpose
2. **Document functions**: Add docstrings to all functions
3. **Avoid dependencies**: Minimize external dependencies when possible
4. **Test independently**: Test module functions separately from automations
