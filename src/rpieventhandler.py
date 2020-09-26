from events import EventLightSwitch
from tracelog import TraceLogger, FT_GLOBAL, ERROR

class RaspberryEventHandler:
    def handle_received_event(self, event):
        if type(event) == EventLightSwitch:
            TraceLogger().trace(FT_GLOBAL, "Switching light state to: ", event.new_light_state)
        else:
            TraceLogger().trace(ERROR, "Unknown event received!!!")