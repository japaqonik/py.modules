from events import EventLightStateUpdate

class LightStateStorage:
    def __init__(self):
        self.lighstate = False
    def send_initial_events(self):
        pass
    def handle_received_event(self, event):
        if type(event) == EventLightStateUpdate:
            self.lighstate = event.light_state
    def getlightstate(self):
        return self.lighstate