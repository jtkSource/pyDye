=====================
pythonDI (python dye)
=====================

A rudimentary Dependency injection framework in python.

We load the yaml file which has the dependencies defined and create an instance by specifying the namespace of the
desired object.

Main modules are: *Italics*, **bold**
- `jtk.py.di.dye`


Sample Code::

    dye.load_di('pydi.yaml')

    s = dye.get_instance('Jubin.Kuriakose.body2')

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

