'''
Created on Nov 29, 2014

@author: rene
'''
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('generator', 'templates'))


def generate_class(obj):
    template = env.get_template('class.py')

    context = {}
    context["obj"] = obj
    return template.render(context)

if __name__ == '__main__':
    pass