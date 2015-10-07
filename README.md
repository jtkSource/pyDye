=====================
pyDye (python dye)
=====================

A rudimentary Dependency injection framework in python.

The dependencies are defined in a yaml file as mentioned below. Th objects are created by referring to the namespace defined in yaml for the desired object.

Main modules are:

- `jtk.di.dye`


Sample Code::

    dye.load_di('pydi.yaml')

    s = dye.get_instance('jubin.body')

    s.print()

- `main.py`


Objects created can also reference other objects.

Config file
===========
- `pydi.yaml`

Comes in this format::

    namespace1:
      class: class_name
      class_attr:
        attr: value
      const_args:
        attr: value
        attr: 'ref:namespace2'
      inst_attr:
        attr: value
        attr: value

    namespace2:
      class: class_name
      const_args:
        attr: value

PyPI URL_.

.. _URL: https://pypi.python.org/pypi/pyDye/
	
