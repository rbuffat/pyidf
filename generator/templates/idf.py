#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on a modified Energy+.idd specification file.

Do not expect (yet) that it actually works!

Generation date: {{ generation_date}}

"""
import re
import logging
from collections import OrderedDict
{%- for file_name in file_names %}
from {{ file_name }} import *
{%- endfor %}


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class IDF(object):
    """ Represens an EnergyPlus IDF input file
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
   
   
    def set(self, data):
        self._data[data.internal_name].append(data)        
   

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
                        if dobj.format == "singleline":
                            vals = [dobj.internal_name]
                            vals += [v[1] for v in dobj.export()]
                            f.write("\n  {};\n".format(",".join(vals)))
                        elif dobj.format == "vertices":
                            f.write("\n  {},\n".format(dobj.internal_name))
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
                        elif dobj.format == "compactschedule":
                            f.write("\n  {},\n".format(dobj.internal_name))
                            vals = dobj.export()
                            cval = len(vals)
                            i = 0
                            while i < cval:

                                if ((i + 1) < cval and "until" in vals[i][0].lower()):
                                    val = ",".join([vals[i][1], vals[i + 1][1]])
                                    comment = ",".join([vals[i][0], vals[i + 1][0]])
                                    i += 2
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
                            f.write("\n  {},\n".format(dobj.internal_name))
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
#                             raise ValueError("{} is not a valid data dictionary name".format(current_object))
                        else:
                            data_object = self._create_datadict(current_object)
                            data_object.read(current_vals)
                            self._data[current_object].append(data_object)
                        
                        current_object = None
                        current_vals = []
                        
