'''
Created on Nov 29, 2014

@author: rene
'''
from datetime import date
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('generator', 'templates'))


def generate_class(obj):
    template = env.get_template('class.py')

    required_fields = []
    for field in obj.fields:
        if "required-field" in field.attributes:
            required_fields.append('"{}"'.format(field.internal_name))

    context = {}
    context["obj"] = obj
    context["required_fields"] = ", ".join(required_fields)

    return template.render(context)


def generate_idf(objs):
    source_files = set()
    required_objects = set()
    unique_objects = set()
    for obj in objs:
        source_files.add(obj.file_name)
        if "required-object" in obj.attributes:
            required_objects.add('"{}"'.format(obj.internal_name))
            
        if "unique-object" in obj.attributes:
            unique_objects.add('"{}"'.format(obj.internal_name))

    template = env.get_template('idf.py')
    context = {}
    context["generation_date"] = date.today()
    context["objs"] = objs
    context["file_names"] = list(source_files)
    context["required_objects"] = ", ".join(required_objects)
    context["unique_objects"] = ", ".join(unique_objects)
    return template.render(context)

if __name__ == '__main__':
    pass