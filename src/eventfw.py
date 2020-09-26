from singleton import SingletonMeta


class EventProducer():
    def __init__(self):
        self._event_listeners = []

    def register_event_litener(self, listener):
        self._event_listeners.append(listener)

    def send_event(self, event):
        for listener in self._event_listeners:
            listener.handle_event(event)


class EventProducerSingleton(EventProducer, metaclass=SingletonMeta):
    pass


class EventListener:
    def __init__(self, event_producer):
        self._event_handlers = {}
        event_producer.register_event_litener(self)

    def register_event_handler(self, event_type, event_handler):
        if not event_type in self._event_handlers:
            self._event_handlers[event_type] = event_handler
        else:
            print("Event: ", event_type, " has already registered handler!!!")

    def handle_event(self, event):
        print("Event recieved of type ", type(event))
        if type(event) in self._event_handlers:
            self._event_handlers[type(event)].handler_received_event(event)
        else:
            print("No valid handler found for event of type: ", type(event))
