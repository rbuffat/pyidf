""" Data objects in group "Exterior Equipment"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ExteriorLights(DataObject):

    """ Corresponds to IDD object `Exterior:Lights`
        only used for Meter type reporting, does not affect building loads
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'schedule name',
                                      {'name': u'Schedule Name',
                                       'pyname': u'schedule_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'design level',
                                      {'name': u'Design Level',
                                       'pyname': u'design_level',
                                       'required-field': True,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'W'}),
                                     (u'control option',
                                      {'name': u'Control Option',
                                       'pyname': u'control_option',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'ScheduleNameOnly',
                                                           u'AstronomicalClock'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'format': None,
              'group': u'Exterior Equipment',
              'min-fields': 0,
              'name': u'Exterior:Lights',
              'pyname': u'ExteriorLights',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def schedule_name(self):
        """Get schedule_name.

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`

        units in schedule should be fraction applied to capacity of the exterior lights equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Schedule Name"] = value

    @property
    def design_level(self):
        """Get design_level.

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`

        Args:
            value (float): value for IDD Field `Design Level`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Design Level"] = value

    @property
    def control_option(self):
        """Get control_option.

        Returns:
            str: the value of `control_option` or None if not set

        """
        return self["Control Option"]

    @control_option.setter
    def control_option(self, value=None):
        """Corresponds to IDD field `Control Option` Astronomical Clock option
        overrides schedule to turn lights off when sun is up.

        Args:
            value (str): value for IDD Field `Control Option`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Control Option"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value




class ExteriorFuelEquipment(DataObject):

    """ Corresponds to IDD object `Exterior:FuelEquipment`
        only used for Meter type reporting, does not affect building loads
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'fuel use type',
                                      {'name': u'Fuel Use Type',
                                       'pyname': u'fuel_use_type',
                                       'required-field': True,
                                       'autosizable': False,
                                       'accepted-values': [u'Electricity',
                                                           u'NaturalGas',
                                                           u'PropaneGas',
                                                           u'FuelOil#1',
                                                           u'FuelOil#2',
                                                           u'Diesel',
                                                           u'Gasoline',
                                                           u'Coal',
                                                           u'OtherFuel1',
                                                           u'OtherFuel2',
                                                           u'Steam',
                                                           u'DistrictHeating',
                                                           u'DistrictCooling'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'schedule name',
                                      {'name': u'Schedule Name',
                                       'pyname': u'schedule_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'design level',
                                      {'name': u'Design Level',
                                       'pyname': u'design_level',
                                       'required-field': True,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'W'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'format': None,
              'group': u'Exterior Equipment',
              'min-fields': 0,
              'name': u'Exterior:FuelEquipment',
              'pyname': u'ExteriorFuelEquipment',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def fuel_use_type(self):
        """Get fuel_use_type.

        Returns:
            str: the value of `fuel_use_type` or None if not set

        """
        return self["Fuel Use Type"]

    @fuel_use_type.setter
    def fuel_use_type(self, value=None):
        """Corresponds to IDD field `Fuel Use Type`

        Args:
            value (str): value for IDD Field `Fuel Use Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fuel Use Type"] = value

    @property
    def schedule_name(self):
        """Get schedule_name.

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`

        units in schedule should be fraction applied to capacity of the exterior fuel equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Schedule Name"] = value

    @property
    def design_level(self):
        """Get design_level.

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`

        Args:
            value (float): value for IDD Field `Design Level`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Design Level"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value




class ExteriorWaterEquipment(DataObject):

    """ Corresponds to IDD object `Exterior:WaterEquipment`
        only used for Meter type reporting, does not affect building loads
    """
    schema = {'extensible-fields': OrderedDict(),
              'fields': OrderedDict([(u'name',
                                      {'name': u'Name',
                                       'pyname': u'name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'}),
                                     (u'fuel use type',
                                      {'name': u'Fuel Use Type',
                                       'pyname': u'fuel_use_type',
                                       'default': u'Water',
                                       'required-field': False,
                                       'autosizable': False,
                                       'accepted-values': [u'Water'],
                                       'autocalculatable': False,
                                       'type': 'alpha'}),
                                     (u'schedule name',
                                      {'name': u'Schedule Name',
                                       'pyname': u'schedule_name',
                                       'required-field': True,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'object-list'}),
                                     (u'design level',
                                      {'name': u'Design Level',
                                       'pyname': u'design_level',
                                       'required-field': True,
                                       'autosizable': False,
                                       'minimum': 0.0,
                                       'autocalculatable': False,
                                       'type': u'real',
                                       'unit': u'm3/s'}),
                                     (u'end-use subcategory',
                                      {'name': u'End-Use Subcategory',
                                       'pyname': u'enduse_subcategory',
                                       'default': u'General',
                                       'required-field': False,
                                       'autosizable': False,
                                       'autocalculatable': False,
                                       'type': u'alpha'})]),
              'format': None,
              'group': u'Exterior Equipment',
              'min-fields': 0,
              'name': u'Exterior:WaterEquipment',
              'pyname': u'ExteriorWaterEquipment',
              'required-object': False,
              'unique-object': False}

    @property
    def name(self):
        """Get name.

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Name"] = value

    @property
    def fuel_use_type(self):
        """Get fuel_use_type.

        Returns:
            str: the value of `fuel_use_type` or None if not set

        """
        return self["Fuel Use Type"]

    @fuel_use_type.setter
    def fuel_use_type(self, value="Water"):
        """Corresponds to IDD field `Fuel Use Type`

        Args:
            value (str): value for IDD Field `Fuel Use Type`
                Default value: Water
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Fuel Use Type"] = value

    @property
    def schedule_name(self):
        """Get schedule_name.

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`

        units in Schedule should be fraction applied to capacity of the exterior water equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Schedule Name"] = value

    @property
    def design_level(self):
        """Get design_level.

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`

        Args:
            value (float): value for IDD Field `Design Level`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value

        """
        self["Design Level"] = value

    @property
    def enduse_subcategory(self):
        """Get enduse_subcategory.

        Returns:
            str: the value of `enduse_subcategory` or None if not set

        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        self["End-Use Subcategory"] = value


