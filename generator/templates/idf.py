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
from collections import OrderedDict
{%- for file_name in file_names %}
from {{ file_name }} import *
{%- endfor %}


logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())


class IDF(object):
    """ Represents an EnergyPlus IDF input file
    """

    required_objects = [{{required_objects}}]
    unique_objects = [{{unique_objects}}]

    def __init__(self):
        """ Inits IDF with no data dictionary set."""
        self._data = OrderedDict()
        {%- for obj in objs %}
        self._data["{% filter lower %}{{obj.internal_name}}{% endfilter %}"] = []
        {%- endfor %}
        self.comment_headers = []
   
   
    def add(self, dataobject):
        """ Adds a data object to the IDF. If data object is unique, it replaces an
        eventual existing data object

        Args:
            dataobject: the data object
        """
        lower_name = dataobject.internal_name.lower()
        if lower_name in self.unique_objects:
            self._data[lower_name] = [dataobject]
        else:
            self._data[lower_name].append(dataobject)        

    def get(self, name):
        """ Returns a list of all objects

            Args:
                name (str): IDD name of objects (see helper.DataObject)
            Returns: 
                list: list of objects

            Raises:
                ValueError: if no objects are found
        """
        if isinstance(name, str):
            name_lower = name.lower()
            if name_lower not in self._data:
                raise ValueError("{} is not a valid name".format(name))
            else:
                return self._data[name_lower]
        raise ValueError("Objects not found")

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
                for key in self._data:
                    if len(self._data[key]) == 0 and key in self.required_objects:
                        raise ValueError('{} is not valid.'.format(key))
                    if key in self.unique_objects and len(self._data[key]) > 1:
                        raise ValueError('{} is not unique: {}'.format(key,
                                                                       len(self._data[key])))
                    for obj in self._data[key]:
                        obj.check(strict=True)

            for key in self._data:
                if len(self._data[key]) > 0:
                    for dobj in self._data[key]:
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
                                    comment = " Fields {} - {}".format(i + 1, j + 1)
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
                    print "Not matched: ", line
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

                        if current_object not in self._data:
                            logging.error("{} is not a valid data dictionary name".format(current_object))

                        else:
                            data_object = self._create_datadict(current_object)
                            data_object.read(current_vals)
                            self._data[current_object].append(data_object)

                        current_object = None
                        current_vals = []

    {%- for obj in objs %}
    @property
    def {{obj.var_name}}s(self):
        """ Get list of all `{{obj.class_name}}` objects
        """
        return self._data[{% filter lower %}"{{obj.class_name}}"{% endfilter %}]

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
            return self._data[val.lower()]
        elif isinstance(val, int):
            i = 0
            for objs in self._data.values():
                for obj in objs:
                    i += 1
                    if i  == val:
                        return obj
    
    def __len__(self):
        count = 0
        for objs in self._data.values():
            count += len(objs)
        return count

    def __iter__(self):
        for val in self._data.values():
            if len(val) > 0:
                yield val
