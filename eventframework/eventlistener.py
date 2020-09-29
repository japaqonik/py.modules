from ..singleton.singletonmeta import SingletonMeta
from ..trace.tracelog import TraceLogger, ABNORMAL, FT_GLOBAL

class EventListener:
    def __init__(self, event_producer = None):
        if event_producer is not None:
            self._event_handlers = {}
            event_producer.register_event_litener(self)

    def register_event_handler(self, event_type, event_handler):
        if not event_type in self._event_handlers:
            TraceLogger().trace(FT_GLOBAL, "Event handler registered for event type: ", event_type)
            self._event_handlers[event_type] = event_handler
        else:
            TraceLogger().trace(ABNORMAL, "Event: ", event_type,
                                " has already registered handler!!!")
        for event_type in self._event_handlers:
            TraceLogger().trace(FT_GLOBAL, "Sending inital events for handler of events type: ", event_type)
            self._event_handlers[event_type].send_initial_events()

    def handle_event(self, event):
        TraceLogger().trace(FT_GLOBAL, "Event received of type: ", type(event))
        if type(event) in self._event_handlers:
            TraceLogger().trace(FT_GLOBAL, "Valid handler found for event of type: ",
                                type(event), ". Rounting event.")
            self._event_handlers[type(event)].handle_received_event(event)
        else:
            TraceLogger().trace(ABNORMAL, "No valid handler found for event of type: ", type(event))

class EventListenerSignleton(EventListener, metaclass=SingletonMeta):
    pass
