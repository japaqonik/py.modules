class EventLightSwitch:
    def __init__(self, new_light_state):
        self.new_light_state = new_light_state

class EventLightStateUpdate:
    def __init__(self, light_state):
        self.light_state = light_state
