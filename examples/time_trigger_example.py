"""
Example Time Trigger Automation

This script demonstrates how to create time-based automations using pyscript.
It runs at a specific time every day.

Usage:
    1. Adjust the time in the decorator to your desired schedule
    2. Copy to config/pyscript/ directory
    3. Reload pyscript

The script will automatically run at the scheduled time(s).
"""

@time_trigger("cron(0 8 * * *)")
def morning_routine():
    """
    Runs every morning at 8:00 AM.
    
    This is an example of a daily morning routine automation.
    Replace with your actual automation logic.
    """
    log.info("Good morning! Running morning routine...")
    
    # Example: Turn on lights
    # service.call("light", "turn_on", entity_id="light.kitchen")
    
    # Example: Send notification
    # service.call("notify", "mobile_app", 
    #              message="Good morning! Time to start your day.",
    #              title="Morning Routine")


@time_trigger("cron(0 22 * * *)")
def evening_routine():
    """
    Runs every evening at 10:00 PM.
    
    This is an example of a nightly routine automation.
    """
    log.info("Good evening! Running evening routine...")
    
    # Example: Turn off lights
    # service.call("light", "turn_off", entity_id="light.living_room")


# Alternative time trigger formats:
# @time_trigger("once(2024-12-31 23:59:59)")  # Run once at specific datetime
# @time_trigger("period(now, 1h)")            # Run every hour
# @time_trigger("cron(*/15 * * * *)")         # Run every 15 minutes
