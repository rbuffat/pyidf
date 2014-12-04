from collections import OrderedDict
import logging
import re
from helper import DataObject

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())



class LeadInput(DataObject):

    """ Corresponds to IDD object `Lead Input`
    """
    schema = {
        'min-fields': 0,
        'name': u'Lead Input',
        'pyname': u'LeadInput',
        'format': None,
        'fields': OrderedDict(),
        'extensible-fields': OrderedDict(),
        'unique-object': False,
        'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `Lead Input`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True


class SimulationData(DataObject):

    """ Corresponds to IDD object `Simulation Data`
    """
    schema = {
        'min-fields': 0,
        'name': u'Simulation Data',
        'pyname': u'SimulationData',
        'format': None,
        'fields': OrderedDict(),
        'extensible-fields': OrderedDict(),
        'unique-object': False,
        'required-object': False}

    def __init__(self):
        """ Init data dictionary object for IDD  `Simulation Data`
        """
        self._data = OrderedDict()
        for key in self.schema['fields']:
            self._data[key] = None
        self._data["extensibles"] = []
        self.strict = True
