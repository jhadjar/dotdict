# dotdict

**Dictionary --> Dot accessible object.**

*Before:*

```python
    >>> dico = {'a': 5, 'b': 7, 'c': {'r': 8, 'd': 6}}
    >>> param = dico['c']['r']
    >>> param
    8
```

*After:*

```python
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
    >>> example2 = DotDict({'a': 5, 'b': 7, 'c': {'r': 8, 'd': 6}})
    >>> example == example2
    True
    >>> for pair in example:
    ...     print pair
    ... 
    ('a', 5)
    ('c', DotDict({'r': 8, 'd': 6}))
    ('b', 7)
```
