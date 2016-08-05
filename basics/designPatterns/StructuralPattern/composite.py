'''

Composite design pattern => component, child and composite class

'''


class Component(object):
    ''' Abstract class'''

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Composite():  # Inherits from the abstract class, Component
    ''' Concrete class and maintains the tree recursive structure '''

    def __init__(self):
        Component.__init__(self, *args, )
