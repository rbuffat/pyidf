""" Data objects in group "Non"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class LoadProfilePlant(DataObject):

    """ Corresponds to IDD object `LoadProfile:Plant`
        Used to simulate a scheduled plant loop demand profile.  Load and flow rate are
        specified using schedules. Positive values are heating loads, and negative values are
        cooling loads. The actual load met is dependent on the performance of the supply
        loop components.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'load schedule name',
                                       {'name': u'Load Schedule Name',
                                        'pyname': u'load_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'peak flow rate',
                                       {'name': u'Peak Flow Rate',
                                        'pyname': u'peak_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'flow rate fraction schedule name',
                                       {'name': u'Flow Rate Fraction Schedule Name',
                                        'pyname': u'flow_rate_fraction_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Non',
               'min-fields': 0,
               'name': u'LoadProfile:Plant',
               'pyname': u'LoadProfilePlant',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def inlet_node_name(self):
        """field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value

    @property
    def load_schedule_name(self):
        """field `Load Schedule Name`

        |  Schedule values are load in [W]

        Args:
            value (str): value for IDD Field `Load Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `load_schedule_name` or None if not set

        """
        return self["Load Schedule Name"]

    @load_schedule_name.setter
    def load_schedule_name(self, value=None):
        """Corresponds to IDD field `Load Schedule Name`"""
        self["Load Schedule Name"] = value

    @property
    def peak_flow_rate(self):
        """field `Peak Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Peak Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `peak_flow_rate` or None if not set

        """
        return self["Peak Flow Rate"]

    @peak_flow_rate.setter
    def peak_flow_rate(self, value=None):
        """Corresponds to IDD field `Peak Flow Rate`"""
        self["Peak Flow Rate"] = value

    @property
    def flow_rate_fraction_schedule_name(self):
        """field `Flow Rate Fraction Schedule Name`

        Args:
            value (str): value for IDD Field `Flow Rate Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `flow_rate_fraction_schedule_name` or None if not set

        """
        return self["Flow Rate Fraction Schedule Name"]

    @flow_rate_fraction_schedule_name.setter
    def flow_rate_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Flow Rate Fraction Schedule Name`"""
        self["Flow Rate Fraction Schedule Name"] = value


