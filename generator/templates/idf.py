#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on a modified Energy+.idd specification file.

Do not expect (yet) that it actually works!

Generation date: {{ generation_date}}

"""
import six
import re
import logging
import pyidf
import datetime
from collections import OrderedDict
{%- for file_name in file_names %}
from pyidf.{{ file_name }} import *
{%- endfor %}


logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())


class IDF(object):
    """ Represents an EnergyPlus IDF input file
    """

    required_objects = [{{required_objects}}]
    unique_objects = [{{unique_objects}}]

    def __init__(self, path=None):
        """ Inits IDF object"""
        self._data = OrderedDict()
        self.comment_headers = []

        if path is not None:
            self.read(path)


    def add(self, dataobject):
        """ Adds a data object to the IDF. If data object is unique, it replaces an
        eventual existing data object

        Args:
            dataobject: the data object
        """
        group = dataobject.schema['group']
        if group not in self._data:
            self._data[group] = OrderedDict()

        lower_name = dataobject.schema['name'].lower()
        if lower_name not in self._data[group]:
            self._data[group][lower_name] = []
        if lower_name in self.unique_objects:
            self._data[group][lower_name] = [dataobject]
        else:
            self._data[group][lower_name].append(dataobject)


    def save(self, path, check=True):
        """ Save data to path

            Args:
                path (str): path where data should be save

            Raises:
                ValueError: if required objects are not present or 
                    unique objects are not unique
        """
        with open(path, 'w') as f:
            if check:
                for group in self._data:
                    for key in self._data[group]:
                        if len(self._data[group][key]) == 0 and key in self.required_objects:
                            raise ValueError('{} is not valid.'.format(key))
                        if key in self.unique_objects and len(self._data[group][key]) > 1:
                            raise ValueError('{} is not unique: {}'.format(key,
                                                                           len(self._data[group][key])))
                        for obj in self._data[group][key]:
                            obj.check(strict=True)

            f.write("!- Generated with pyidf version {}, "
                    "generation date: {}\n".format(pyidf.__version__, str(datetime.datetime.now())))
            f.write("!- Validation level: {}\n".format(pyidf.validation_level))

            if len(self.comment_headers) > 0:
                f.write("\n!- Previous comments:\n\n")
                for comment in self.comment_headers:
                    f.write("{}\n".format(comment))

            for group in self._data:
                f.write("\n!-   ===========  ALL OBJECTS OF GROUP: {}  ===========\n".format(group))
                for key in self._data[group]:
                    if len(self._data[group][key]) > 0:
                        for dobj in self._data[group][key]:
                            if dobj.schema['format'] == "singleline":
                                vals = [dobj.schema['name']]
                                vals += [v[1] for v in dobj.export()]
                                f.write("\n  {};\n".format(",".join(vals)))
                            elif dobj.schema['format'] == "vertices":
                                f.write("\n  {},\n".format(dobj.schema['name']))
                                vals = dobj.export()
                                cval = len(vals)
                                i = 0
                                while i < cval:

                                    if ((i + 2) < cval and "x" in vals[i][0].lower() and 
                                        "y" in vals[i + 1][0].lower() and "z" in vals[i + 2][0].lower()):
                                        val = ",".join([vals[i][1], vals[i + 1][1], vals[i + 2][1]])
                                        comment = ",".join([vals[i][0], vals[i + 1][0], vals[i + 2][0]])
                                        i += 3
                                    else: 
                                        val = vals[i][1]
                                        comment = vals[i][0]
                                        i += 1

                                    sep = ','
                                    if i >= cval:
                                        sep = ';'
                                    blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                    f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                       sep=sep,
                                                                                       blanks=blanks,
                                                                                       comment=comment))
                            elif dobj.schema['format'] == "compactschedule":
                                f.write("\n  {},\n".format(dobj.schema['name']))
                                vals = dobj.export()
                                cval = len(vals)
                                i = 0
                                while i < cval:

                                    if "until" in vals[i][1].lower():
                                        j = i + 1
                                        while j < cval:
                                            jval = vals[j][1].lower()
                                            if "for" in jval or "until" in jval:
                                                break
                                            j += 1
                                        val = ",".join([vals[i][1]] + [vals[t][1] for t in range(i + 1, j) ])
                                        comment = "Fields {} - {}".format(i + 1, j + 1)
                                        i += (j - i)
                                    else: 
                                        val = vals[i][1]
                                        comment = vals[i][0]
                                        i += 1

                                    sep = ','
                                    if i >= cval:
                                        sep = ';'
                                    blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                    f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                       sep=sep,
                                                                                       blanks=blanks,
                                                                                       comment=comment))
                            elif dobj.schema['format'] == "fluidproperty":

                                f.write("\n  {},\n".format(dobj.schema['name']))
                                vals = dobj.export()
                                cval = len(vals)
                                i = 0
                                while i < cval:
    
                                    is_fluidprops = True
                                    for j in range(min(7, cval - i)):

                                        # Test the next values
                                        fluidprops_match = re.search(r"([0-9]|value|property)", vals[i + j][0])
                                        if fluidprops_match is None:
                                            is_fluidprops = False
                                            break

                                    if  is_fluidprops:                                    
                                        val = ",".join([vals[i + j][1] for j in range(min(7, cval - i))])
                                        comment = ""
                                        i += min(7, cval - i)
                                    else:
                                        val = vals[i][1]
                                        comment = vals[i][0]
                                        i += 1

                                    sep = ','
                                    if i >= cval:
                                        sep = ';'
                                    blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                    f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                       sep=sep,
                                                                                       blanks=blanks,
                                                                                       comment=comment))
                            elif dobj.schema['format'] == "spectral":
                                f.write("\n  {},\n".format(dobj.schema['name']))
                                vals = dobj.export()
                                cval = len(vals)
                                i = 0
                                while i < cval:

                                    start = i
                                    end = min(i + 4, cval)

                                    if False not in ["name" not in jval[0].lower() for jval in vals[start:end]]:
                                        val = ",".join([vals[j][1] for j in range(start, end) ])
                                        i += (end - start)
                                        comment = ""
                                    else: 
                                        val = vals[i][1]
                                        comment = vals[i][0]
                                        i += 1

                                    sep = ','
                                    if i >= cval:
                                        sep = ';'
                                    blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                    f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                       sep=sep,
                                                                                       blanks=blanks,
                                                                                       comment=comment))

                            else:
                                f.write("\n  {},\n".format(dobj.schema['name']))
                                vals = dobj.export()
                                cval = len(vals)
                                for i, val in enumerate(vals):

                                    sep = ','
                                    if i == (cval - 1):
                                        sep = ';'
                                    blanks = ' ' * max(30 - 4 - len(val[1]) - 2, 2)
                                    comment = val[0]

                                    f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val[1],
                                                                                       sep=sep,
                                                                                       blanks=blanks,
                                                                                       comment=comment))

    def read(self, path):
        """Read IDF data from path

           Args:
               path (str): path to read data from
        """
        with open(path, "r") as f:
            current_object = None
            current_vals = []

            # First lines are header comments
            header = True

            for line in f:

                line = line.strip()
                if re.search(r"^\s*!", line) is not None:
                    if header:
                        self.comment_headers.append(line)
                    continue
                if len(line) == 0:
                    continue

                header = False

                line_comments = line.split("!")
                line_match = re.search(r"\s*([\S ]*[,;])\s*", line_comments[0])
                if line_match is None:
                    logger.warn("Not matched: {}".format(line))
                    continue
                else:
                    line = line_match.group(1)

                splits = line.split(";")

                for i, split in enumerate(splits):

                    split = split.strip()
                    if len(split) > 0 and split[-1] == ',':
                        split = split[:-1]

                    splitvals = split.split(",")
                    
                    if i > 1 and len(split) == 0:
                        continue

                    for j, val in enumerate(splitvals):

                        val = val.strip()

                        if j == len(splitvals) and len(val) == 0:
                            continue

                        if val == '' and current_object is None:
                            continue

                        if current_object is None:
                            current_object = val.lower()
                        else:
                            current_vals.append(val)

                    if len(splits) > 1 and current_object is not None:

                        data_object = self._create_datadict(current_object)
                        data_object.read(current_vals)
                        self.add(data_object)

                        current_object = None
                        current_vals = []

    {%- for obj in objs %}
    @property
    def {{obj.var_name}}s(self):
        """ Get list of all `{{obj.class_name}}` objects

        Raises:
            ValueError: if no objects of type `{{obj.class_name}}` are present
        """
        return self._data["{{obj.group}}"][{% filter lower %}"{{obj.internal_name}}"{% endfilter %}]

    {%- endfor %}

    @classmethod
    def _create_datadict(cls, internal_name):
        """ Creates an object depending on `internal_name`

            Args:
                internal_name (str): IDD name

            Raises:
                ValueError: if `internal_name` cannot be matched to a data dictionary object
        """
        {%- for obj in objs %}
        if internal_name.lower() == "{% filter lower %}{{ obj.internal_name }}"{% endfilter %}:
            return {{ obj.class_name }}()
        {%- endfor %}
        raise ValueError("No DataDictionary known for {}".format(internal_name))

    def __getitem__(self, val):
        if isinstance(val, six.string_types):
            group = self._create_datadict(val).schema['group']
            if group not in self._data:
                self._data[group] = OrderedDict()
    
            lower_name = val.lower()
            if lower_name not in self._data[group]:
                self._data[group][lower_name] = []

            return self._data[group][lower_name]

        elif isinstance(val, int):
            i = 0
            for group in self._data:
                for key in self._data[group]:
                    for obj in self._data[group][key]:
                        if i == val:
                            return obj
                        i += 1
        else:
            raise TypeError("Wrong type {} for IDF".format(type(val)))
    
    def __len__(self):
        count = 0
        for group in self._data:
            for key in self._data[group]:
                count += len(self._data[group][key])
        return count

    def __iter__(self):
        for group in self._data:
            for key in self._data[group]:
                for obj in self._data[group][key]:
                    yield obj

    def __contains__(self, key):
        key_lower = key.lower()
        for group in self._data:
            if key_lower in self._data[group]:
                if len(self._data[group][key_lower]) > 0:
                    return True
                break
        return False
        

    def keys(self):
        keys = []
        for group in self._data:
            for key in self._data[group]:
                if len(self._data[group][key]) > 0:
                    keys.append(key)
        return keys