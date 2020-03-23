Python Skills:
==============

things to pay attention for logging (speed):
--------------------------------------------


* when displaying debug messages with a >=INFO logging level, check the debugging level before calling 'logging.debug' (e.g. if logging.getLogger().level == logging.DEBUG)

* format the logging messages with "%s" instead of calling the "format" function (e.g. logging.debug("check: [%s]", phrase) )

* in case of multiple checks on the logging level, store that value in a variable to avoid calling the quite expensive "logging.getLogger()" function (e.g. if logger_level == logging.DEBUG )


How to print all properties from  a class:
------------------------------------------

use python `dir`, print all class attribute except python classes like `__str__`, `__dict__`

::

    def props(x):
        return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))


use `vars()` or `__dict__`:

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

::

    >>> vars(a)
    {'c': 2, 'b': 1}
