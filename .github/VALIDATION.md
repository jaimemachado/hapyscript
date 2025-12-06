# GitHub Actions CI/CD

This repository includes automated validation for pull requests using GitHub Actions.

## Workflow: Validate PyScripts

**File**: `.github/workflows/validate.yml`

### When it runs

- On pull requests to `main` or `master` branches
- On pushes to `main` or `master` branches
- Only when Python files (`**.py`) or the workflow file itself changes

### What it validates

1. **Python Syntax** - Ensures all `.py` files have valid Python syntax
2. **Flake8** - Checks code style and potential errors
3. **Black** - Verifies code formatting consistency
4. **isort** - Checks import statement organization
5. **Pylint** - Additional code quality checks

### Special Considerations

The validation workflow is configured to handle Home Assistant Pyscript specifics:

- **F821 (undefined name)** is ignored because Pyscript provides decorators and globals at runtime:
  - `@service`, `@state_trigger`, `@time_trigger`, `@event_trigger`
  - `log`, `state`, `service`, `task`, etc.

### Using `noqa` Comments

In your pyscripts, you can add `# noqa: F821` comments to suppress warnings about pyscript-provided names:

```python
@service  # noqa: F821 - provided by pyscript
def my_automation():
    log.info("Running")  # noqa: F821 - provided by pyscript
```

### Running Validation Locally

Before submitting a PR, you can run validation locally:

```bash
# Install tools
pip install flake8 black isort pylint

# Check syntax
python -m py_compile examples/*.py pyscripts/*.py

# Run flake8
flake8 . --max-line-length=120 --ignore=E501,W503,F821

# Check formatting
black --check --line-length=120 .

# Auto-format with Black
black --line-length=120 .

# Check import sorting
isort --check-only --profile black --line-length=120 .

# Auto-fix import sorting
isort --profile black --line-length=120 .
```

### Continuous Improvement

The validation checks use `continue-on-error: true` for style checks to avoid blocking PRs on minor style issues. However, it's recommended to address warnings when possible to maintain code quality.

### Customizing the Workflow

To customize the validation workflow:

1. Edit `.github/workflows/validate.yml`
2. Adjust flake8 rules in the `--ignore` flag
3. Change line length in Black and isort (default: 120)
4. Add or remove validation steps as needed
