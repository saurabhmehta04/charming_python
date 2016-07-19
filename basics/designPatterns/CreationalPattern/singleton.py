'''

Singleton pattern
- only one object to be instantiated in the class; global variables in singleton pattern
- acts as cache
- here we are using Borg design pattern (type of singleton pattern)
'''


class Borg:
    _shared_state = dict()

    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


# making a singleton object
x = Singleton(HTTP="Hyper Text Transfer Protocol")

# another singleton object
y = Singleton(SNMP="Simple Network Management Protocol")
print(x)
