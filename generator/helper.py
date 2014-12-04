'''
Created on Oct 30, 2014

@author: rene
'''
from collections import OrderedDict
import logging
import re
import string
def normalize_field_name(internal_name):

    name = internal_name.strip()
    name = name.replace('/', ' or ').replace('&', ' and ')
    name = name.replace('.', ' ').replace(',', ' ')
    name = name.lower()
    name = name.replace(' ', '_')
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    name = re.sub(r'_+', '_', name)
    if re.search(r"^[0-9]", name) is not None:
        name = "a_" + name
    return name


def normalize_object_name(internal_name):
    name = internal_name.replace('/', ' or ').replace('&', ' and ').strip()
    name = re.sub(r'[^a-zA-Z0-9_]', ' ', name)
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', name)
    name = string.capwords(name)
    name = name.replace(' ', '')
    return name


def normalize_object_var_name(internal_name):
    name = internal_name.strip().replace('/', ' or ').replace('&', ' and ').lower()
    name = name.replace(' ', '_')
    name = re.sub(r'[^a-zA-Z0-9_]', '', name)
    return name


def object_filename(internal_name):
    splits = internal_name.split(":")
    name = normalize_field_name(splits[0])
    return name


class DataObject:

    def __init__(self, internal_name=None, file_name=""):
        self.internal_name = internal_name
        self.class_name = normalize_object_name(internal_name)
        self.var_name = normalize_object_var_name(internal_name)
        self.file_name = file_name
        self.fields = []
        self.extensible_fields = []
        self.attributes = {}
        self.ignored = False

    def make_extensibles(self):
        if "extensible" in self.attributes:
            count = self.attributes["extensible"]

            for i, field in enumerate(self.fields):
                if "begin-extensible" in field.attributes:
                    self.extensible_fields = self.fields[i:i + count]
                    self.fields = self.fields[0:i]

# { 
#               'name' : "TemperingValve",
#               'field_count' : 6,
#               'format' : None,
#               'min-fields' : 0,
#               'fields:' : OrderedDict([
#                                        ('field_name', { 'required' : True,
#                                                         'type' : 'int',
#                                                         'accepted_values' : set(1,2,3,4) }),
#                                        ])}

    def create_schema(self):
        schema = {}
        schema['name'] = self.internal_name
        schema['pyname'] = self.class_name
        if format in self.attributes:
            schema['format'] = self.attributes['format'].lower()
        else:
            schema['format'] = None

        if "min-fields" in self.attributes:
            schema['min-fields'] = int(self.attributes['min-fields'])
        else:
            schema['min-fields'] = 0
        if 'required-object' in self.attributes:
            schema['required-object'] = True
        else:
            schema['required-object'] = False
        if 'unique-object' in self.attributes:
            schema['unique-object'] = True
        else:
            schema['unique-object'] = False

        schema['fields'] = OrderedDict()
        for field in self.fields:
            field_dict = {}
            field_dict['type'] = field.attributes["type"]
            field_dict['name'] = field.internal_name
            field_dict['pyname'] = field.field_name

            if 'required-field' in field.attributes:
                field_dict['required-field'] = True
            else:
                field_dict['required-field'] = False

            if 'key' in field.attributes["type"]:
                field_dict['accepted-values'] = field.attributes['key']

            if 'units' in field.attributes:
                field_dict['unit'] = field.attributes['units']

            if 'minimum' in field.attributes:
                field_dict['minimum'] = field.attributes['minimum']

            if 'minimum>' in field.attributes:
                field_dict['minimum>'] = field.attributes['minimum>']

            if 'maximum' in field.attributes:
                field_dict['maximum'] = field.attributes['maximum']

            if 'maximum<' in field.attributes:
                field_dict['maximum<'] = field.attributes['maximum<']

            if 'default' in field.attributes:
                val = field.attributes['default']
                if isinstance(val, str):
                    if val[0] == '"' and val[-1] == '"':
                        val = val[1:-1]
                field_dict['default'] = val

            if 'autocalculatable' in field.attributes:
                field_dict['autocalculatable'] = True
            else:
                field_dict['autocalculatable'] = False

            if 'autosizable' in field.attributes:
                field_dict['autosizable'] = True
            else:
                field_dict['autosizable'] = False

            schema['fields'][field.internal_name.lower()] = field_dict

        schema['extensible-fields'] = OrderedDict()
        for field in self.extensible_fields:
            field_dict = {}
            field_dict['type'] = field.attributes["type"]
            field_dict['name'] = field.internal_name
            field_dict['pyname'] = field.field_name

            if 'required-field' in field.attributes:
                field_dict['required-field'] = True
            else:
                field_dict['required-field'] = False

            if 'key' in field.attributes["type"]:
                field_dict['accepted-values'] = field.attributes['key']

            if 'units' in field.attributes:
                field_dict['unit'] = field.attributes['units']

            if 'minimum' in field.attributes:
                field_dict['minimum'] = field.attributes['minimum']

            if 'minimum>' in field.attributes:
                field_dict['minimum>'] = field.attributes['minimum>']

            if 'maximum' in field.attributes:
                field_dict['maximum'] = field.attributes['maximum']

            if 'maximum<' in field.attributes:
                field_dict['maximum<'] = field.attributes['maximum<']

            if 'default' in field.attributes:
                val = field.attributes['default']
                if isinstance(val, str):
                    if val[0] == '"' and val[-1] == '"':
                        val = val[1:-1]
                field_dict['default'] = val

            if 'autocalculatable' in field.attributes:
                field_dict['autocalculatable'] = True
            else:
                field_dict['autocalculatable'] = False

            if 'autosizable' in field.attributes:
                field_dict['autosizable'] = True
            else:
                field_dict['autosizable'] = False

            schema['extensible-fields'][field.internal_name.lower()] = field_dict

        self.schema = schema


class DataField(object):

    def __init__(self, internal_name, ftype, fid, dataobject):

        self.attributes = {}
        self.set_internal_name(internal_name)
        self.is_list = False
        self.ftype = ftype
        self.fid = fid
        self.dataobject = dataobject

    def set_internal_name(self, internal_name):
        self.internal_name = internal_name
        self.field_name = normalize_field_name(internal_name)

    def value2py(self, value, ftype):
        if ftype == 'alpha':
            return value
        if ftype == 'integer':
            return int(value)
        if ftype == 'real':
            return float(value)
        return value

    def pytype(self, ftype):
        if ftype == 'alpha':
            return "str"
        if ftype == 'integer':
            return "int"
        if ftype == 'real':
            return "float"
        return "str"

    def add_attribute(self, attribute_name, value):
        self.attributes[attribute_name] = value

    def conv_vals(self):

        # Sanity check
        if "type" in self.attributes:
            if (self.attributes["type"] == "alpha") and self.ftype == "N":
                logging.warn("alpha type is declared as number: {}->{} / {}".format(self.dataobject.internal_name,
                                                                               self.internal_name,
                                                                            self.attributes["type"]))

            if (self.attributes["type"] == "real" or self.attributes[
                    "type"] == "integer") and self.ftype == "A":
                logging.warn("number type as alpha: {}->{} {}".format(self.dataobject.internal_name,
                                                                   self.internal_name,
                                                                   self.attributes["type"]))

        # Update type if not other specified
        if "type" not in self.attributes:
            if self.ftype == "A":
                self.attributes["type"] = "alpha"
            elif self.ftype == "N":
#                 logging.warn("number field without definition of int / real: {}->{}".format(self.dataobject.internal_name,
#                                                                    self.internal_name))
                self.attributes["type"] = "real"

        if self.attributes["type"] == "choice":
            if self.ftype == "A":
                self.attributes["type"] = "alpha"
            elif self.ftype == "N":
                self.attributes["type"] = "int"

        self.attributes["pytype"] = self.pytype(self.attributes["type"])

        if not self.attributes["type"] == "alpha":
        # Convert some values to python representation
            for attribute_name in list(self.attributes):
                if attribute_name in ["default",
                                      "minimum",
                                      "minimum>",
                                      "maximum",
                                      "maximum<",
                                      "missing"]:
                    value = self.attributes[attribute_name]
                    try:
                        self.attributes[attribute_name] = self.value2py(value,
                                                                        self.attributes["type"])
                    except Exception:
                        self.attributes[attribute_name] = '"{}"'.format(value)
#                     logging.warn("cast to py value failed for {} {} {}: {}->{}".format(attribute_name,
#                                                                                        value,
#                                                                                        self.attributes["type"],
#                                                                                        self.dataobject.internal_name,
#                                                                                        self.internal_name))

            self.attributes["pytype"] = self.pytype(self.attributes["type"])

        # unitsBasedOnField
        if "unitsBasedOnField" in self.attributes:
            fv = self.attributes["unitsBasedOnField"]

            for field in self.dataobject.fields:
                if field.fid == fv:
                    self.attributes["unitsBasedOnField"] = field.field_name
            if self.attributes["unitsBasedOnField"] == fv:
                logging.warn("did not found units based on field field for {}->{}".format(self.dataobject.internal_name,
                                                                   self.internal_name))
