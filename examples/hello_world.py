"""
Example Hello World Pyscript

This is a simple example script that demonstrates the basic structure of a pyscript.
It creates a service that can be called from Home Assistant to log a hello message.

Usage:
    Call the service from Home Assistant:
    - Service: pyscript.hello_world
    - Service Data: { "name": "World" }

Author: Home Assistant User
"""

@service
def hello_world(name="World"):
    """
    Say hello to someone.
    
    Args:
        name: The name to greet (default: "World")
    """
    log.info(f"Hello, {name}!")
    
    # You can also use Home Assistant services
    # service.call("notify", "persistent_notification", 
    #              message=f"Hello, {name}!",
    #              title="Greeting from Pyscript")
