""" Data objects in group "energyplus"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class LeadInput(DataObject):

    """Corresponds to IDD object `Lead Input`"""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': 'energyplus',
               'min-fields': 0,
               'name': u'Lead Input',
               'pyname': u'LeadInput',
               'required-object': False,
               'unique-object': False}




class SimulationData(DataObject):

    """Corresponds to IDD object `Simulation Data`"""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': 'energyplus',
               'min-fields': 0,
               'name': u'Simulation Data',
               'pyname': u'SimulationData',
               'required-object': False,
               'unique-object': False}


