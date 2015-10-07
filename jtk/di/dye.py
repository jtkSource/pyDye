__author__ = 'jubin'

import yaml
import importlib

di_map = None

def __loadclass(full_class_name):
    module_name, class_name = str(full_class_name).rsplit(".", 1)
    clazz = getattr(importlib.import_module(module_name), class_name)
    return clazz

def __resolve_ref(kwargs):

    for key in kwargs:

        if isinstance(kwargs[key], str):

            if kwargs[key].startswith('ref:'):

                ref = kwargs[key].split(':')

                kwargs[key] = get_instance(ref[1])

    return kwargs

def load_di(yaml_path):

    global di_map

    with open(yaml_path) as f:

        di_map = yaml.load(f)


def get_instance(namespace):

    global di_map

    if di_map is None:

        raise Exception('DI yaml file not specified')

    path = di_map[namespace]['class']

    clazz = __loadclass(path)

    if 'class_attr' in di_map[namespace]:

        kwargs = __resolve_ref(di_map[namespace]['class_attr'])

        for key in kwargs:

            setattr(clazz, key, kwargs[key])

    if 'const_args' in di_map[namespace]:

        kwargs = __resolve_ref(di_map[namespace]['const_args'])

        ins = clazz(**kwargs)

    else:

        ins = clazz()

    if 'inst_attr' in di_map[namespace]:

        kwargs = __resolve_ref(di_map[namespace]['inst_attr'])

        for key in kwargs:

            setattr(ins, key, kwargs[key])

    return ins
