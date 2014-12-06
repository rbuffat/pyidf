""" Data objects in group "energyplus"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class LeadInput(DataObject):

    """Corresponds to IDD object `Lead Input`"""
    schema = {
        'min-fields': 0,
        'name': u'Lead Input',
        'pyname': u'LeadInput',
        'format': None,
        'fields': OrderedDict(),
        'extensible-fields': OrderedDict(),
        'unique-object': False,
        'required-object': False,
        'group': 'energyplus'}




class SimulationData(DataObject):

    """Corresponds to IDD object `Simulation Data`"""
    schema = {
        'min-fields': 0,
        'name': u'Simulation Data',
        'pyname': u'SimulationData',
        'format': None,
        'fields': OrderedDict(),
        'extensible-fields': OrderedDict(),
        'unique-object': False,
        'required-object': False,
        'group': 'energyplus'}


