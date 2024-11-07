from datetime import datetime

class AlertSystem:
    def __init__(self):
        pass

    def send_alert(self, name):
        if name == "Unfamiliar":
            print(f"[ALERT] Unfamiliar face detected at {datetime.now()}")
        else:
            print(f"[INFO] Known individual detected: {name} at {datetime.now()}")