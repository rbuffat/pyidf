import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.{{ obj.file_name }} import {{ obj.class_name }}

log = logging.getLogger(__name__)

class Test{{ obj.class_name }}(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_{{ obj.var_name }}(self):

        pyidf.validation_level = ValidationLevel.error

        obj = {{ obj.class_name }}()
        {%- for field in obj.fields %}
        # {{ field.attributes.type}}
        var_{{field.field_name}} = {% if (field.attributes.type == "real" or field.attributes.type == "integer")  %}{{default[field.field_name]}}{% else %}"{{default[field.field_name]}}"{% endif %}
        obj.{{field.field_name}} = var_{{field.field_name}}
        {%- endfor %}

        {%- if obj.extensible_fields|count > 0 %}
        paras = []
        {%- for field in obj.extensible_fields %}
        var_{{field.field_name}} = {% if (field.attributes.type == "real" or field.attributes.type == "integer")  %}{{default[field.field_name]}}{% else %}"{{default[field.field_name]}}"{% endif %}
        paras.append(var_{{field.field_name}})
        {%- endfor %}
        obj.add_extensible(*paras)
        {% endif %}

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        {%- for field in obj.fields %}
            {%- if field.attributes.pytype == "str" %}
        self.assertEqual(idf2.{{obj.var_name}}s[0].{{field.field_name}}, var_{{field.field_name}})
            {%- elif field.attributes.pytype == "int" %}
        self.assertEqual(idf2.{{obj.var_name}}s[0].{{field.field_name}}, var_{{field.field_name}})
            {%- elif field.attributes.pytype == "float" %}
        self.assertAlmostEqual(idf2.{{obj.var_name}}s[0].{{field.field_name}}, var_{{field.field_name}})
            {%- endif %}
        {%- endfor %}
        {%- for field in obj.extensible_fields %}
        index = obj.extensible_field_index("{{ field.internal_name }}")
            {%- if field.attributes.pytype == "str" %}
        self.assertEqual(idf2.{{obj.var_name}}s[0].extensibles[0][index], var_{{field.field_name}})
            {%- elif field.attributes.pytype == "int" %}
        self.assertEqual(idf2.{{obj.var_name}}s[0].extensibles[0][index], var_{{field.field_name}})
            {%- elif field.attributes.pytype == "float" %}
        self.assertAlmostEqual(idf2.{{obj.var_name}}s[0].extensibles[0][index], var_{{field.field_name}})
            {%- endif %}
        {%- endfor %}