pythonDI
(python dye)

A rudimentary Dependency injection framework in python.

We load the yaml file which has the dependencies defined and create an instance by specifying the namespace of the
desired object.

if __name__ == '__main__':

    dye.load_di('pydi.yaml')

    s = dye.get_instance('Jubin.Kuriakose.body2')

    s.print()

