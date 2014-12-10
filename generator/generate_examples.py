'''
Created on Dec 9, 2014

@author: rene
'''
import autopep8
from jinja2 import Environment, PackageLoader
from pyidf.idf import IDF
import six
env = Environment(loader=PackageLoader('generator', 'templates'))

file_name = r"../examples/Exercise1A_properties.py"
file_name_named = r"../examples/Exercise1A_named.py"

if __name__ == "__main__":
    idf = IDF(
        r"/usr/local/EnergyPlus-8-2-0/ExampleFiles/BasicsFiles/Exercise1A.idf")
    objs = []
    imports = set()
    for obj in idf:
        ob = {}
        ob['class'] = obj.__class__.__name__
        ob['dd_name'] = obj.schema['name']
        ob['module'] = obj.__module__

        imports.add((obj.__module__, obj.__class__.__name__))
        ob['fields'] = []
        ob['dd-fields'] = []
        ob['extensible-fields'] = []
        for item in obj.items():
            if not isinstance(item[0], tuple):
                val = item[1]
                if isinstance(val, six.string_types):
                    val = '"{}"'.format(val)
                ob['fields'].append((obj.field(item[0])['pyname'], val))
                ob['dd-fields'].append((item[0], val))

        if len(obj.schema['extensible-fields']) > 0:
            for ext in obj.extensibles:
                paras = []
                for val in ext:
                    if isinstance(val, six.string_types):
                        val = '"{}"'.format(val)
                    paras.append(str(val))
                ob['extensible-fields'].append(", ".join(paras))
        objs.append(ob)

    template = env.get_template('example.py')
    context = {}
    context["objs"] = objs
    context["imports"] = imports

    source = template.render(context)
    source = autopep8.fix_code(
        source, options=autopep8.parse_args(['--aggressive',
                                             '--aggressive',
                                             '--aggressive',
                                             '']))
    with open(file_name, 'w') as f:
        f.write(source)

    template_named = env.get_template('example_named.py')
    source_named = template_named.render(context)
    source_named = autopep8.fix_code(
        source_named, options=autopep8.parse_args(['--aggressive',
                                             '--aggressive',
                                             '--aggressive',
                                             '']))
    with open(file_name_named, 'w') as f:
        f.write(source_named)
