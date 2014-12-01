'''
Created on Oct 30, 2014

@author: rene
'''
import string
import re
import logging


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
        self.attributes = {}
        self.ignored = False


class DataField(object):

    def __init__(self, internal_name, ftype, dataobject):

        self.attributes = {}
        self.set_internal_name(internal_name)
        self.is_list = False
        self.ftype = ftype
        self.dataobject = dataobject

    def set_internal_name(self, internal_name):
        self.internal_name = internal_name
        self.field_name = normalize_field_name(internal_name)

    def value2py(self, value, ftype):
        if ftype == 'alpha':
            return str(value)
        if ftype == 'integer':
            return str(int(value))
        if ftype == 'real':
            return str(float(value))
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
                logging.warn("number field without definition of int / real: {}->{}".format(self.dataobject.internal_name,
                                                                   self.internal_name))
                self.attributes["type"] = "real"

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
