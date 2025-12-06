# Apps Directory

This directory is for more complex, multi-file applications that require additional structure.

## When to Use Apps

Use the `apps/` directory when:
- Your automation requires multiple Python files
- You need to organize related functionality into modules
- You're building a complex application with multiple components

## Structure

Each app should have its own subdirectory:

```
apps/
├── my_app/
│   ├── __init__.py
│   ├── main.py
│   └── helpers.py
└── another_app/
    ├── __init__.py
    └── automation.py
```

## Example

```python
# apps/my_app/__init__.py
from .main import setup

# apps/my_app/main.py
@service
def my_complex_service():
    """A more complex service."""
    # Your logic here
    pass
```

## Loading Apps

Apps are automatically loaded by Pyscript when placed in the appropriate directory structure in your Home Assistant configuration.
