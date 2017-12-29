
messages = {
    'name_squatting': ('"{name}" is a reserved attribute name. '
                       'The original dictionary is stored there.'),
}


class DotDict(object):
    """Recursively turn a dictionary into a dot accessible object.

    Before::

        >>> dico = {'a': 5, 'b': 7, 'c': {'r': 8, 'd': 6}}
        >>> param = dico['c']['r']
        >>> param
        8

    After::

        >>> example = DotDict({'a': 5, 'b': 7, 'c': {'r': 8, 'd': 6}})
        >>> example
        DotDict({'a': 5, 'b': 7, 'c': {'r': 8, 'd': 6}})
        >>> example.a
        5
        >>> example.b
        7
        >>> example.c
        DotDict({'r': 8, 'd': 6})
        >>> example.c.r
        8
        >>> len(example)
        3
        >>> example2 = DotDict({'d': 6, 'r': 8})
        >>> example == example2
        True
    """

    def __init__(self, origin):
        self._origin = origin
        for key, value in origin.items():
            if key == '_origin':
                msg = messages['name_squatting']
                raise ValueError(msg.format(name='_origin'))
            if isinstance(value, dict):
                setattr(self, key, self.__class__(value))
            else:
                setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __iter__(self):
        for key, value in self.__dict__.items():
            if key != "_origin":
                yield key, value

    def __len__(self):
        return len(self._origin)

    def __eq__(self, other):
        try:
            return self._origin == other._origin
        except AttributeError:
            return False

    def __repr__(self):
        return "{self.__class__.__name__}({self._origin})".format(self=self)
