'''
Created on Oct 30, 2014

@author: rene
'''
from _collections import defaultdict
import logging
import re
import unicodedata

from helper import DataObject, DataField
from helper import normalize_field_name
class IDDParser():

    object_attributes = []

    field_attributes = []

    def _is_new_group(self, line):
        return re.search(r"^\s*\\group", line) is not None

    def _is_new_field(self, line):
        if self._is_new_group(line):
            return False
        return re.search(r"^\s*[AN]\d+\s*[,;]", line) is not None

    def _is_attribute(self, line):
        if self._is_new_group(line):
            return False
        return re.search(r"^\s*\\", line) is not None

    def _is_new_object(self, line):
        if self._is_new_group(line):
            return False
        if self._is_new_field(line) or self._is_attribute(line):
            return False
        return re.search(r"^\s*(.*)[,;]", line) is not None

    def _parse_object_name(self, line):

        match_obj_name = re.search(r"^\s*(.*)[,;]", line)
        assert match_obj_name is not None

        internal_name = match_obj_name.group(1)
        return internal_name

    def _parse_group_name(self, line):
        match_group_name = re.search(r"^\s*\\group\w*([a-zA-Z0-9 ]*[a-zA-Z0-9])", line)
        assert match_group_name is not None
        return match_group_name.group(1)

    def _parse_field_name(self, line):
        # print "NewField:\t", line
        match_field_name = re.search(r"\\field\s(.*)$", line)
        match_field_type = re.search(r"^\s*([AN])", line)

        if match_field_name is None or match_field_type is None:
#             print "Did not match field name: ", line, match_field_name, match_field_type
            return None

        ftype = match_field_type.group(1)
        internal_name = match_field_name.group(1).strip()
        return ftype, internal_name

    def _parse_attribute(self, line):

        attribute_name = None
        attribute_value = None

        match_attribute_name = re.match(r"\s*\\([^\s]+)", line)
        if match_attribute_name is not None:
            attribute_name = match_attribute_name.group(1).strip()

            no_value_attributes = ["required-field",
                                   "unique-object",
                                   "required-object"]

            if attribute_name in no_value_attributes:
                return attribute_name, True

            match_value = re.search(r"\s*\\[^\s]+\s?(.*)", line)
            if match_value is not None:
                attribute_value = match_value.group(1).strip()

        return attribute_name, attribute_value

    def __init__(self):
        self.current_object = None
        self.current_field = None
        self.current_group = "energyplus"
        self.objects = []

    def parse(self, path):

        with open(path, mode='r') as f:
            for line in f:
                if line[0] == '!':
                    continue
                line = line.strip()
                line = unicode(line, errors='ignore')

#                 print self._is_new_group(line), "\t", self._is_new_object(line), "\t", self._is_new_field(line), "\t", self._is_attribute(line), "\t", line
                assert self._is_new_group(line) + self._is_new_object(line) + self._is_new_field(line) + self._is_attribute(line) <= 1

                if self._is_new_group(line):
                    self.current_group = normalize_field_name(self._parse_group_name(line))
                elif self._is_new_object(line):

                    if self.current_object is not None and self.current_field is not None:
                        self.current_object.fields.append(self.current_field)

                    if self.current_object is not None:
                        self.objects.append(self.current_object)

                    internal_name = self._parse_object_name(line)
                    self.current_object = DataObject(internal_name, file_name=self.current_group)
                    self.current_field = None

                elif self._is_new_field(line):

                    if (self.current_object is not None and
                            self.current_field is not None):
                        self.current_object.fields.append(self.current_field)

                    try:
                        ftype, internal_name = self._parse_field_name(line)
                        self.current_field = DataField(internal_name, ftype, self.current_object)
                    except Exception as e:
                        self.current_object.ignored = True
#                         print self.current_object.internal_name, line

                elif self._is_attribute(line):

                    multiple_value_attributes = ["key",
                                                 "note",
                                                 "memo"]

                    name, value = self._parse_attribute(line)

                    # Check if object attribute
                    if (self.current_object is not None and
                            self.current_field is None):
                        if name in multiple_value_attributes:
                            if name not in self.current_object.attributes:
                                self.current_object.attributes[name] = []
                            self.current_object.attributes[name].append(value)
                        else:
                            self.current_object.attributes[name] = value

                    # => field attribute
                    else:
                        if name in multiple_value_attributes:
                            if name not in self.current_field.attributes:
                                self.current_field.attributes[name] = []
                            self.current_field.attributes[name].append(value)
                        else:
                            self.current_field.attributes[name] = value
                else:
                    pass
#                     if len(line) > 0:
#                         logging.warn(u"did not parse line: {}".format(line))

        if self.current_field is not None:
            self.current_object.fields.append(self.current_field)

        if self.current_object is not None:
            self.objects.append(self.current_object)

        good_objs = []
        for obj in self.objects:
            if not obj.ignored:
                fields = defaultdict(list)
                for field in obj.fields:

                    if field.internal_name in fields:
                        fields[field.internal_name].append(field)
                        logging.warn("duplicated field name: {}->{}".format(field.dataobject.internal_name,
                                                                            field.internal_name))
                        new_name = "{} v{}".format(field.internal_name,
                                                   str(len(fields[field.internal_name])))
                        field.set_internal_name(new_name)

                    fields[field.internal_name].append(field)
                    field.conv_vals()
                good_objs.append(obj)
            else:
                logging.warn("ignore object: {}".format(obj.internal_name))

        return good_objs

if __name__ == '__main__':
    parser = IDDParser()
    objects = parser.parse("V8-2-0-Energy+.idd")
