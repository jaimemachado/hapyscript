from stubs.pyscript_builtins import service


@service()
def hello():
    """A more complex service."""
    print("Hello service executed.")
    log.error("Hello service executed.")
    # Your logic here
    pass