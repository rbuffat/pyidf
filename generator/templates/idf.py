#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on a modified Energy+.idd specification file.

Do not expect (yet) that it actually works!

Generation date: {{ generation_date}}

"""
import re
from collections import OrderedDict
{%- for file_name in file_names %}
from {{ file_name }} import *
{%- endfor %}


class IDF(object):
    """ Represens an EnergyPlus IDF input file
    """
    
    required_objects = [{{required_objects}}]

    def __init__(self):
        """ Inits IDF with no data dictionary set."""
        self._data = OrderedDict()
        {%- for obj in objs %}
        self._data["{{obj.internal_name}}"] = None
        {%- endfor %}
   
   
    def set(self, data):
        self._data[data.internal_name] = data        
   

    def save(self, path, check=True):
        """ Save data to path
        
            Args:
                path (str): path where data should be saved
        """
        with open(path, 'w') as f:
            if check:
                for key in self._data:
                    if self._data[key] is None and key in self.required_objects:
                        raise ValueError('{} is not valid.'.format(key))
            for key in self._data:
                if self._data[key] is not None:
                    f.write(self._data[key].export() + "\n")

    @classmethod
    def _create_datadict(cls, internal_name):
        """ Creates an object depending on `internal_name`
        
            Args:
                internal_name (str): IDD name
                
            Raises:
                ValueError: if `internal_name` cannot be matched to a data dictionary object
        """
        {%- for obj in objs %}
        if internal_name == "{{ obj.internal_name }}":
            return {{ obj.class_name }}()
        {%- endfor %}
        raise ValueError("No DataDictionary known for {}".format(internal_name))

    def read(self, path):
        """Read IDF data from path
        
           Args:
               path (str): path to read data from
        """
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                match_obj_name = re.search(r"^([A-Z][A-Z/ \d]+),", line)
                if match_obj_name is not None:
                    internal_name = match_obj_name.group(1)
                    if internal_name in self._data:
                        self._data[internal_name] = self._create_datadict(internal_name)
                        data_line = line[len(internal_name) + 1:]
                        vals = data_line.strip().split(',')
                        self._data[internal_name].read(vals)
