Python Skills:
==============

How to print all properties from  a class:
------------------------------------------

use python `dir`, print all class attribute except python classes like `__str__`, `__dict__`

examples:
^^^^^^^^^

::

    def props(x):
        return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


use `vars()` or `__dict__`:

examples:
^^^^^^^^^

::

    >>> class A(object):
    ...   def __init__(self):
    ...     self.b = 1
    ...     self.c = 2
    ...   def do_nothing(self):
    ...     pass
    ...
    >>> a = A()
    >>> a.__dict__
    {'c': 2, 'b': 1}

or using the vars() function which calls `__dict__`:

examples:
^^^^^^^^^

::

    >>> vars(a)
    {'c': 2, 'b': 1}
