
messages = {
    'name_squatting': ('"{name}" is a reserved attribute name. '
                       'The original dictionary is stored there.'),
}


class DotDict(object):
    """Recursively turn a dictionary into a dot accessible object.

    Before::

        >>> param = example['key1']['key2']['key3']

    After::

        >>> example = DotDict({'a': 5, 'b': 7, 'c': {'r': 8, 'd': 6}})
        >>>> example
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
        self._original_dict = origin
        for key, value in origin.items():
            if key == '_original_dict':
                msg = messages['name_squatting']
                raise ValueError(msg.format(name='_original_dict'))
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
            if key != "_original_dict":
                yield key, value

    def __len__(self):
        return len(self._original_dict)

    def __eq__(self, other):
        try:
            return self._original_dict == other._original_dict
        except AttributeError:
            return False

    def __repr__(self):
        r = "{self.__class__.__name__}({self._original_dict})"
        return r.format(self=self)
