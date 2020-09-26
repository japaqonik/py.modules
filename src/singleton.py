class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]