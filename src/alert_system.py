import os
from datetime import datetime, timedelta

class AlertSystem:
    #Create a Alert log file
    def __init__(self, log_file="alerts.log", cooldown_period=60):
        self.log_file = log_file
        self.cooldown_period = timedelta(seconds=cooldown_period)
        self.last_alert_times = {}  # Store last alert time for each face
        # Ensure log file exists
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as file:
                file.write("Alert Log\n")
                file.write("-" * 40 + "\n")
  
    # Avoid constant alert 
    def send_alert(self, name):
        current_time = datetime.now()
        # Check cooldown to avoid duplicate alerts
        if self._is_in_cooldown(name, current_time):
            return
        # Format the alert message
        alert_type = "[ALERT]" if name == "Unfamiliar" else "[INFO]"
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        message = f"{alert_type} {name} face detected at {formatted_time}"
        # Log to console, file, or external system
        self._print_alert(message)
        self._log_to_file(message)
        # Update last alert time
        self.last_alert_times[name] = current_time
   
    # Cooldown of 60 seconds
    def _is_in_cooldown(self, name, current_time):
        last_alert_time = self.last_alert_times.get(name)
        if last_alert_time and current_time - last_alert_time < self.cooldown_period:
            return True
        return False

    def _print_alert(self, message):
        #Print the alert message to the console.
        print(message)

    def _log_to_file(self, message):
        #Log the alert message to a file.
        with open(self.log_file, "a") as file:
            file.write(message + "\n")
