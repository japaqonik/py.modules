from ..eventframework.events import EventLightSwitch, EventLightStateUpdate
from ..trace.tracelog import TraceLogger, FT_GLOBAL, ERROR
from ..eventframework.eventproducer import EventProducerSingleton

class RaspberryEventHandler:
    def __init__(self):
        self.lightstate = False
    def send_initial_events(self):
        EventProducerSingleton().send_event(EventLightStateUpdate(self.lightstate))
    def handle_received_event(self, event):
        if type(event) == EventLightSwitch:
            if event.new_light_state != self.lightstate:
                TraceLogger().trace(FT_GLOBAL, "Switching light state to: ", event.new_light_state)
                self.lightstate = event.new_light_state
                EventProducerSingleton().send_event(EventLightStateUpdate(event.new_light_state))
        else:
            TraceLogger().trace(ERROR, "Unknown event received!!!")