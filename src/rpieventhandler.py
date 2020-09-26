from events import EventLightSwitch

class RaspberryEventHandler:
    def handler_received_event(self, event):
        if type(event) == EventLightSwitch:
            print("Switching light state to: ", event.new_light_state)
        else:
            print("Unknown event recieved")