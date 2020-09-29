from ..singleton.singletonmeta import SingletonMeta
from ..trace.tracelog import TraceLogger, FT_GLOBAL

class EventProducer:
    def __init__(self):
        self._event_listeners = []

    def register_event_litener(self, listener):
        self._event_listeners.append(listener)

    def send_event(self, event):
        for listener in self._event_listeners:
            TraceLogger().trace(FT_GLOBAL, "Sending event of type: ", type(event))
            listener.handle_event(event)


class EventProducerSingleton(EventProducer, metaclass=SingletonMeta):
    pass
