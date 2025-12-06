# HaPyScript 🏠🐍

A repository for storing [Pyscript](https://github.com/custom-components/pyscript) scripts for my Home Assistant instance.

## What is Pyscript?

Pyscript is a powerful Home Assistant integration that allows you to write Python scripts to automate your smart home. It provides a full Python environment with access to Home Assistant's state, services, and events.

## Repository Structure

```
hapyscript/
├── pyscripts/          # Individual automation scripts
├── apps/               # More complex multi-file applications
├── modules/            # Shared code and utilities
└── examples/           # Example scripts and templates
```

## Installation

1. Make sure you have the [Pyscript integration](https://hacs-pyscript.readthedocs.io/) installed in Home Assistant through HACS
2. Clone or copy the scripts from this repository to your Home Assistant configuration directory:
   ```
   config/pyscript/
   ```
3. Restart Home Assistant or reload Pyscript from Developer Tools → YAML

## Usage

### Adding a New Script

1. Create a new `.py` file in the `pyscripts/` directory
2. Copy the script to your Home Assistant `config/pyscript/` directory
3. Reload Pyscript or restart Home Assistant
4. The script will be automatically loaded and available

### Script Structure

A basic pyscript looks like this:

```python
@service
def my_automation():
    """My custom automation service."""
    log.info("Running my automation")
    # Your automation logic here
```

## Available Scripts

See the [pyscripts/](pyscripts/) directory for all available scripts. Each script includes documentation at the top of the file explaining its purpose and usage.

## Requirements

- Home Assistant (tested on version 2023.x and above)
- [Pyscript integration](https://github.com/custom-components/pyscript) installed via HACS

## Documentation

- [Pyscript Official Documentation](https://hacs-pyscript.readthedocs.io/)
- [Home Assistant Documentation](https://www.home-assistant.io/docs/)
- [Pyscript Tutorial](https://hacs-pyscript.readthedocs.io/en/latest/tutorial.html)

## Contributing

This is a personal repository for my Home Assistant setup, but feel free to:
- Use any scripts that might be helpful for your setup
- Open issues if you find bugs
- Suggest improvements

## License

This repository is provided as-is for personal use. Feel free to use and modify the scripts for your own Home Assistant instance.

## Useful Tips

- Test your scripts in the Pyscript Jupyter kernel before deploying
- Use `log.info()`, `log.warning()`, and `log.error()` for debugging
- Check the Home Assistant logs for pyscript errors: `config/home-assistant.log`
- Reload scripts without restarting: Developer Tools → YAML → Pyscript

## Resources

- [Pyscript GitHub](https://github.com/custom-components/pyscript)
- [Home Assistant Community Forum - Pyscript](https://community.home-assistant.io/c/third-party/pyscript/)