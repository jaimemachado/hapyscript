# Example Scripts

This directory contains example and template scripts to help you get started with Pyscript for Home Assistant.

## Available Examples

- **hello_world.py** - Basic service creation example
- **state_trigger_example.py** - Automation triggered by entity state changes
- **time_trigger_example.py** - Time-based automation examples

## Using These Examples

1. Review the example that matches your use case
2. Copy the relevant code
3. Customize it for your specific needs
4. Move it to the `pyscripts/` directory
5. Update entity IDs and configuration to match your setup

## Learning Resources

- Read the inline comments in each example
- Check the [Pyscript documentation](https://hacs-pyscript.readthedocs.io/) for more details
- Experiment with the examples in a test environment first

## Template Pattern

All examples follow this pattern:

```python
"""
Script description and documentation
"""

# Configuration constants at the top
ENTITY_ID = "light.example"

# Decorator to define trigger type
@trigger_type
def function_name(args):
    """Function documentation."""
    # Your automation logic
    pass
```

Feel free to use these as templates for your own automations!
