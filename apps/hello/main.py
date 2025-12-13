from stubs.pyscript_builtins import service

import debugpy, sys, os
log.info("DEBUGPY: python=%s pid=%s cwd=%s", sys.executable, os.getpid(), os.getcwd())
log.info("DEBUGPY: connected=%s", debugpy.is_client_connected())


@service()
def hello():
    """A more complex service."""
    debugpy.breakpoint()
    print("Hello service executed.")
    log.error("Hello service executed.")
    # Your logic here
    pass