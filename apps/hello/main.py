from stubs.pyscript_builtins import service

import debugpy, sys, os
log.info("DEBUGPY: python=%s pid=%s file=%s cwd=%s", sys.executable, os.getpid(), __file__, os.getcwd())
log.info("DEBUGPY: connected=%s", debugpy.is_client_connected())


@service()
def hello():
    """A more complex service."""
    print("Hello service executed.")
    log.error("Hello service executed.")
    # Your logic here
    pass