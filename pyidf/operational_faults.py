""" Data objects in group "Operational Faults"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class FaultModelTemperatureSensorOffsetOutdoorAir(DataObject):

    """ Corresponds to IDD object `FaultModel:TemperatureSensorOffset:OutdoorAir`
        This object describes outdoor air temperature sensor offset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller object type',
                                       {'name': u'Controller Object Type',
                                        'pyname': u'controller_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller object name',
                                       {'name': u'Controller Object Name',
                                        'pyname': u'controller_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'temperature sensor offset',
                                       {'name': u'Temperature Sensor Offset',
                                        'pyname': u'temperature_sensor_offset',
                                        'default': 0.0,
                                        'minimum>': -10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 10.0,
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:TemperatureSensorOffset:OutdoorAir',
               'pyname': u'FaultModelTemperatureSensorOffsetOutdoorAir',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_type` or None if not set

        """
        return self["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """Corresponds to IDD field `Controller Object Type`"""
        self["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_name` or None if not set

        """
        return self["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """Corresponds to IDD field `Controller Object Name`"""
        self["Controller Object Name"] = value

    @property
    def temperature_sensor_offset(self):
        """field `Temperature Sensor Offset`

        Args:
            value (float): value for IDD Field `Temperature Sensor Offset`
                Units: deltaC
                value > -10.0
                value < 10.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_sensor_offset` or None if not set

        """
        return self["Temperature Sensor Offset"]

    @temperature_sensor_offset.setter
    def temperature_sensor_offset(self, value=None):
        """Corresponds to IDD field `Temperature Sensor Offset`"""
        self["Temperature Sensor Offset"] = value




class FaultModelHumiditySensorOffsetOutdoorAir(DataObject):

    """ Corresponds to IDD object `FaultModel:HumiditySensorOffset:OutdoorAir`
        This object describes outdoor air humidity sensor offset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller object type',
                                       {'name': u'Controller Object Type',
                                        'pyname': u'controller_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller object name',
                                       {'name': u'Controller Object Name',
                                        'pyname': u'controller_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'humidity sensor offset',
                                       {'name': u'Humidity Sensor Offset',
                                        'pyname': u'humidity_sensor_offset',
                                        'default': 0.0,
                                        'minimum>': -0.02,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 0.02,
                                        'unit': u'kgWater/kgDryAir'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:HumiditySensorOffset:OutdoorAir',
               'pyname': u'FaultModelHumiditySensorOffsetOutdoorAir',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_type` or None if not set

        """
        return self["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """Corresponds to IDD field `Controller Object Type`"""
        self["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_name` or None if not set

        """
        return self["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """Corresponds to IDD field `Controller Object Name`"""
        self["Controller Object Name"] = value

    @property
    def humidity_sensor_offset(self):
        """field `Humidity Sensor Offset`

        Args:
            value (float): value for IDD Field `Humidity Sensor Offset`
                Units: kgWater/kgDryAir
                value > -0.02
                value < 0.02

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_sensor_offset` or None if not set

        """
        return self["Humidity Sensor Offset"]

    @humidity_sensor_offset.setter
    def humidity_sensor_offset(self, value=None):
        """Corresponds to IDD field `Humidity Sensor Offset`"""
        self["Humidity Sensor Offset"] = value




class FaultModelEnthalpySensorOffsetOutdoorAir(DataObject):

    """ Corresponds to IDD object `FaultModel:EnthalpySensorOffset:OutdoorAir`
        This object describes outdoor air enthalpy sensor offset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller object type',
                                       {'name': u'Controller Object Type',
                                        'pyname': u'controller_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller object name',
                                       {'name': u'Controller Object Name',
                                        'pyname': u'controller_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'enthalpy sensor offset',
                                       {'name': u'Enthalpy Sensor Offset',
                                        'pyname': u'enthalpy_sensor_offset',
                                        'default': 0.0,
                                        'minimum>': -20000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 20000.0,
                                        'unit': u'J/kg'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:EnthalpySensorOffset:OutdoorAir',
               'pyname': u'FaultModelEnthalpySensorOffsetOutdoorAir',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_type` or None if not set

        """
        return self["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """Corresponds to IDD field `Controller Object Type`"""
        self["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_name` or None if not set

        """
        return self["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """Corresponds to IDD field `Controller Object Name`"""
        self["Controller Object Name"] = value

    @property
    def enthalpy_sensor_offset(self):
        """field `Enthalpy Sensor Offset`

        Args:
            value (float): value for IDD Field `Enthalpy Sensor Offset`
                Units: J/kg
                value > -20000.0
                value < 20000.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_sensor_offset` or None if not set

        """
        return self["Enthalpy Sensor Offset"]

    @enthalpy_sensor_offset.setter
    def enthalpy_sensor_offset(self, value=None):
        """Corresponds to IDD field `Enthalpy Sensor Offset`"""
        self["Enthalpy Sensor Offset"] = value




class FaultModelPressureSensorOffsetOutdoorAir(DataObject):

    """ Corresponds to IDD object `FaultModel:PressureSensorOffset:OutdoorAir`
        This object describes outdoor air pressure sensor offset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller object type',
                                       {'name': u'Controller Object Type',
                                        'pyname': u'controller_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller object name',
                                       {'name': u'Controller Object Name',
                                        'pyname': u'controller_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pressure sensor offset',
                                       {'name': u'Pressure Sensor Offset',
                                        'pyname': u'pressure_sensor_offset',
                                        'default': 0.0,
                                        'minimum>': -10000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 10000.0,
                                        'unit': u'Pa'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:PressureSensorOffset:OutdoorAir',
               'pyname': u'FaultModelPressureSensorOffsetOutdoorAir',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_type` or None if not set

        """
        return self["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """Corresponds to IDD field `Controller Object Type`"""
        self["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_name` or None if not set

        """
        return self["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """Corresponds to IDD field `Controller Object Name`"""
        self["Controller Object Name"] = value

    @property
    def pressure_sensor_offset(self):
        """field `Pressure Sensor Offset`

        Args:
            value (float): value for IDD Field `Pressure Sensor Offset`
                Units: Pa
                value > -10000.0
                value < 10000.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pressure_sensor_offset` or None if not set

        """
        return self["Pressure Sensor Offset"]

    @pressure_sensor_offset.setter
    def pressure_sensor_offset(self, value=None):
        """Corresponds to IDD field `Pressure Sensor Offset`"""
        self["Pressure Sensor Offset"] = value




class FaultModelTemperatureSensorOffsetReturnAir(DataObject):

    """ Corresponds to IDD object `FaultModel:TemperatureSensorOffset:ReturnAir`
        This object describes return air temperature sensor offset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller object type',
                                       {'name': u'Controller Object Type',
                                        'pyname': u'controller_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller object name',
                                       {'name': u'Controller Object Name',
                                        'pyname': u'controller_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'temperature sensor offset',
                                       {'name': u'Temperature Sensor Offset',
                                        'pyname': u'temperature_sensor_offset',
                                        'default': 0.0,
                                        'minimum>': -10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 10.0,
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:TemperatureSensorOffset:ReturnAir',
               'pyname': u'FaultModelTemperatureSensorOffsetReturnAir',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_type` or None if not set

        """
        return self["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """Corresponds to IDD field `Controller Object Type`"""
        self["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_name` or None if not set

        """
        return self["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """Corresponds to IDD field `Controller Object Name`"""
        self["Controller Object Name"] = value

    @property
    def temperature_sensor_offset(self):
        """field `Temperature Sensor Offset`

        Args:
            value (float): value for IDD Field `Temperature Sensor Offset`
                Units: deltaC
                value > -10.0
                value < 10.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_sensor_offset` or None if not set

        """
        return self["Temperature Sensor Offset"]

    @temperature_sensor_offset.setter
    def temperature_sensor_offset(self, value=None):
        """Corresponds to IDD field `Temperature Sensor Offset`"""
        self["Temperature Sensor Offset"] = value




class FaultModelEnthalpySensorOffsetReturnAir(DataObject):

    """ Corresponds to IDD object `FaultModel:EnthalpySensorOffset:ReturnAir`
        This object describes return air enthalpy sensor offset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller object type',
                                       {'name': u'Controller Object Type',
                                        'pyname': u'controller_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Controller:OutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controller object name',
                                       {'name': u'Controller Object Name',
                                        'pyname': u'controller_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'enthalpy sensor offset',
                                       {'name': u'Enthalpy Sensor Offset',
                                        'pyname': u'enthalpy_sensor_offset',
                                        'default': 0.0,
                                        'minimum>': -20000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 20000.0,
                                        'unit': u'J/kg'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:EnthalpySensorOffset:ReturnAir',
               'pyname': u'FaultModelEnthalpySensorOffsetReturnAir',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def controller_object_type(self):
        """field `Controller Object Type`

        Args:
            value (str): value for IDD Field `Controller Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_type` or None if not set

        """
        return self["Controller Object Type"]

    @controller_object_type.setter
    def controller_object_type(self, value=None):
        """Corresponds to IDD field `Controller Object Type`"""
        self["Controller Object Type"] = value

    @property
    def controller_object_name(self):
        """field `Controller Object Name`

        Args:
            value (str): value for IDD Field `Controller Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_object_name` or None if not set

        """
        return self["Controller Object Name"]

    @controller_object_name.setter
    def controller_object_name(self, value=None):
        """Corresponds to IDD field `Controller Object Name`"""
        self["Controller Object Name"] = value

    @property
    def enthalpy_sensor_offset(self):
        """field `Enthalpy Sensor Offset`

        Args:
            value (float): value for IDD Field `Enthalpy Sensor Offset`
                Units: J/kg
                value > -20000.0
                value < 20000.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_sensor_offset` or None if not set

        """
        return self["Enthalpy Sensor Offset"]

    @enthalpy_sensor_offset.setter
    def enthalpy_sensor_offset(self, value=None):
        """Corresponds to IDD field `Enthalpy Sensor Offset`"""
        self["Enthalpy Sensor Offset"] = value




class FaultModelFoulingCoil(DataObject):

    """ Corresponds to IDD object `FaultModel:Fouling:Coil`
        This object describes fouling water heating or cooling coils
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coil name',
                                       {'name': u'Coil Name',
                                        'pyname': u'coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'severity schedule name',
                                       {'name': u'Severity Schedule Name',
                                        'pyname': u'severity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fouling input method',
                                       {'name': u'Fouling Input Method',
                                        'pyname': u'fouling_input_method',
                                        'default': u'FouledUARated',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FouledUARated',
                                                            u'FoulingFactor'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'uafouled',
                                       {'name': u'UAFouled',
                                        'pyname': u'uafouled',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'water side fouling factor',
                                       {'name': u'Water Side Fouling Factor',
                                        'pyname': u'water_side_fouling_factor',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2-K/W'}),
                                      (u'air side fouling factor',
                                       {'name': u'Air Side Fouling Factor',
                                        'pyname': u'air_side_fouling_factor',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2-K/W'}),
                                      (u'outside coil surface area',
                                       {'name': u'Outside Coil Surface Area',
                                        'pyname': u'outside_coil_surface_area',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'inside to outside coil surface area ratio',
                                       {'name': u'Inside to Outside Coil Surface Area Ratio',
                                        'pyname': u'inside_to_outside_coil_surface_area_ratio',
                                        'default': 0.07,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Operational Faults',
               'min-fields': 0,
               'name': u'FaultModel:Fouling:Coil',
               'pyname': u'FaultModelFoulingCoil',
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
    def coil_name(self):
        """field `Coil Name`

        Args:
            value (str): value for IDD Field `Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `coil_name` or None if not set

        """
        return self["Coil Name"]

    @coil_name.setter
    def coil_name(self, value=None):
        """Corresponds to IDD field `Coil Name`"""
        self["Coil Name"] = value

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def severity_schedule_name(self):
        """field `Severity Schedule Name`

        Args:
            value (str): value for IDD Field `Severity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `severity_schedule_name` or None if not set

        """
        return self["Severity Schedule Name"]

    @severity_schedule_name.setter
    def severity_schedule_name(self, value=None):
        """Corresponds to IDD field `Severity Schedule Name`"""
        self["Severity Schedule Name"] = value

    @property
    def fouling_input_method(self):
        """field `Fouling Input Method`

        Args:
            value (str): value for IDD Field `Fouling Input Method`
                Default value: FouledUARated

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fouling_input_method` or None if not set

        """
        return self["Fouling Input Method"]

    @fouling_input_method.setter
    def fouling_input_method(self, value="FouledUARated"):
        """Corresponds to IDD field `Fouling Input Method`"""
        self["Fouling Input Method"] = value

    @property
    def uafouled(self):
        """field `UAFouled`
        Fouling coil UA value under rating conditions
        For Fouling Input Method: FouledUARated

        Args:
            value (float): value for IDD Field `UAFouled`
                Units: W/K

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `uafouled` or None if not set
        """
        return self["UAFouled"]

    @uafouled.setter
    def uafouled(self, value=None):
        """Corresponds to IDD field `UAFouled`"""
        self["UAFouled"] = value

    @property
    def water_side_fouling_factor(self):
        """field `Water Side Fouling Factor`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Water Side Fouling Factor`
                Units: m2-K/W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_side_fouling_factor` or None if not set
        """
        return self["Water Side Fouling Factor"]

    @water_side_fouling_factor.setter
    def water_side_fouling_factor(self, value=None):
        """Corresponds to IDD field `Water Side Fouling Factor`"""
        self["Water Side Fouling Factor"] = value

    @property
    def air_side_fouling_factor(self):
        """field `Air Side Fouling Factor`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Air Side Fouling Factor`
                Units: m2-K/W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_side_fouling_factor` or None if not set
        """
        return self["Air Side Fouling Factor"]

    @air_side_fouling_factor.setter
    def air_side_fouling_factor(self, value=None):
        """Corresponds to IDD field `Air Side Fouling Factor`"""
        self["Air Side Fouling Factor"] = value

    @property
    def outside_coil_surface_area(self):
        """field `Outside Coil Surface Area`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Outside Coil Surface Area`
                Units: m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outside_coil_surface_area` or None if not set
        """
        return self["Outside Coil Surface Area"]

    @outside_coil_surface_area.setter
    def outside_coil_surface_area(self, value=None):
        """Corresponds to IDD field `Outside Coil Surface Area`"""
        self["Outside Coil Surface Area"] = value

    @property
    def inside_to_outside_coil_surface_area_ratio(self):
        """field `Inside to Outside Coil Surface Area Ratio`
        For Fouling Input Method: FoulingFactor

        Args:
            value (float): value for IDD Field `Inside to Outside Coil Surface Area Ratio`
                Units: dimensionless
                Default value: 0.07

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `inside_to_outside_coil_surface_area_ratio` or None if not set
        """
        return self["Inside to Outside Coil Surface Area Ratio"]

    @inside_to_outside_coil_surface_area_ratio.setter
    def inside_to_outside_coil_surface_area_ratio(self, value=0.07):
        """Corresponds to IDD field `Inside to Outside Coil Surface Area
        Ratio`"""
        self["Inside to Outside Coil Surface Area Ratio"] = value


