from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class EvaporativeCoolerDirectCelDekPad(object):
    """ Corresponds to IDD object `EvaporativeCooler:Direct:CelDekPad`
        Direct evaporative cooler with rigid media evaporative pad and recirculating water
        pump. This model has no controls other than its availability schedule.
    """
    internal_name = "EvaporativeCooler:Direct:CelDekPad"
    field_count = 9
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeCooler:Direct:CelDekPad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Direct Pad Area"] = None
        self._data["Direct Pad Depth"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Control Type"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.direct_pad_area = None
        else:
            self.direct_pad_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.direct_pad_depth = None
        else:
            self.direct_pad_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectCelDekPad.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectCelDekPad.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectCelDekPad.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectCelDekPad.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def direct_pad_area(self):
        """Get direct_pad_area

        Returns:
            float: the value of `direct_pad_area` or None if not set
        """
        return self._data["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value=None):
        """  Corresponds to IDD Field `Direct Pad Area`

        Args:
            value (float): value for IDD Field `Direct Pad Area`
                Units: m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.direct_pad_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerDirectCelDekPad.direct_pad_area`')
        self._data["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """Get direct_pad_depth

        Returns:
            float: the value of `direct_pad_depth` or None if not set
        """
        return self._data["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value=None):
        """  Corresponds to IDD Field `Direct Pad Depth`

        Args:
            value (float): value for IDD Field `Direct Pad Depth`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.direct_pad_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerDirectCelDekPad.direct_pad_depth`')
        self._data["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.recirculating_water_pump_power_consumption`'.format(value))
        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectCelDekPad.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectCelDekPad.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectCelDekPad.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectCelDekPad.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """  Corresponds to IDD Field `Control Type`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectCelDekPad.control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectCelDekPad.control_type`')
        self._data["Control Type"] = value

    @property
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectCelDekPad.water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectCelDekPad.water_supply_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectCelDekPad.water_supply_storage_tank_name`')
        self._data["Water Supply Storage Tank Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field EvaporativeCoolerDirectCelDekPad:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EvaporativeCoolerDirectCelDekPad:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EvaporativeCoolerDirectCelDekPad: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EvaporativeCoolerDirectCelDekPad: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class EvaporativeCoolerIndirectCelDekPad(object):
    """ Corresponds to IDD object `EvaporativeCooler:Indirect:CelDekPad`
        Indirect evaporative cooler with rigid media evaporative pad, recirculating water
        pump, and secondary air fan. This model has no controls other than its availability
        schedule.
    """
    internal_name = "EvaporativeCooler:Indirect:CelDekPad"
    field_count = 14
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeCooler:Indirect:CelDekPad`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Direct Pad Area"] = None
        self._data["Direct Pad Depth"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Secondary Fan Flow Rate"] = None
        self._data["Secondary Fan Total Efficiency"] = None
        self._data["Secondary Fan Delta Pressure"] = None
        self._data["Indirect Heat Exchanger Effectiveness"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Control Type"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.direct_pad_area = None
        else:
            self.direct_pad_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.direct_pad_depth = None
        else:
            self.direct_pad_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_flow_rate = None
        else:
            self.secondary_fan_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_total_efficiency = None
        else:
            self.secondary_fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_delta_pressure = None
        else:
            self.secondary_fan_delta_pressure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.indirect_heat_exchanger_effectiveness = None
        else:
            self.indirect_heat_exchanger_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def direct_pad_area(self):
        """Get direct_pad_area

        Returns:
            float: the value of `direct_pad_area` or None if not set
        """
        return self._data["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value=None):
        """  Corresponds to IDD Field `Direct Pad Area`

        Args:
            value (float): value for IDD Field `Direct Pad Area`
                Units: m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.direct_pad_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.direct_pad_area`')
        self._data["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """Get direct_pad_depth

        Returns:
            float: the value of `direct_pad_depth` or None if not set
        """
        return self._data["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value=None):
        """  Corresponds to IDD Field `Direct Pad Depth`

        Args:
            value (float): value for IDD Field `Direct Pad Depth`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.direct_pad_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.direct_pad_depth`')
        self._data["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.recirculating_water_pump_power_consumption`'.format(value))
        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """Get secondary_fan_flow_rate

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set
        """
        return self._data["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Flow Rate`

        Args:
            value (float): value for IDD Field `Secondary Fan Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_flow_rate`')
        self._data["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """Get secondary_fan_total_efficiency

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set
        """
        return self._data["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Secondary Fan Total Efficiency`
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_total_efficiency`')
        self._data["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """Get secondary_fan_delta_pressure

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set
        """
        return self._data["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Delta Pressure`

        Args:
            value (float): value for IDD Field `Secondary Fan Delta Pressure`
                Units: Pa
                IP-Units: inH2O
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_delta_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.secondary_fan_delta_pressure`')
        self._data["Secondary Fan Delta Pressure"] = value

    @property
    def indirect_heat_exchanger_effectiveness(self):
        """Get indirect_heat_exchanger_effectiveness

        Returns:
            float: the value of `indirect_heat_exchanger_effectiveness` or None if not set
        """
        return self._data["Indirect Heat Exchanger Effectiveness"]

    @indirect_heat_exchanger_effectiveness.setter
    def indirect_heat_exchanger_effectiveness(self, value=None):
        """  Corresponds to IDD Field `Indirect Heat Exchanger Effectiveness`

        Args:
            value (float): value for IDD Field `Indirect Heat Exchanger Effectiveness`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.indirect_heat_exchanger_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.indirect_heat_exchanger_effectiveness`')
        self._data["Indirect Heat Exchanger Effectiveness"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.primary_air_inlet_node_name`')
        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Primary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.primary_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.primary_air_outlet_node_name`')
        self._data["Primary Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """  Corresponds to IDD Field `Control Type`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.control_type`')
        self._data["Control Type"] = value

    @property
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.water_supply_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.water_supply_storage_tank_name`')
        self._data["Water Supply Storage Tank Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectCelDekPad.secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectCelDekPad.secondary_air_inlet_node_name`')
        self._data["Secondary Air Inlet Node Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field EvaporativeCoolerIndirectCelDekPad:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EvaporativeCoolerIndirectCelDekPad:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EvaporativeCoolerIndirectCelDekPad: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EvaporativeCoolerIndirectCelDekPad: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class EvaporativeCoolerIndirectWetCoil(object):
    """ Corresponds to IDD object `EvaporativeCooler:Indirect:WetCoil`
        Indirect evaporative cooler with wetted coil, recirculating water pump, and secondary
        air fan. This model has no controls other than its availability schedule.
    """
    internal_name = "EvaporativeCooler:Indirect:WetCoil"
    field_count = 13
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeCooler:Indirect:WetCoil`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Coil Maximum Efficiency"] = None
        self._data["Coil Flow Ratio"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Secondary Fan Flow Rate"] = None
        self._data["Secondary Fan Total Efficiency"] = None
        self._data["Secondary Fan Delta Pressure"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Control Type"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_maximum_efficiency = None
        else:
            self.coil_maximum_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_flow_ratio = None
        else:
            self.coil_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_flow_rate = None
        else:
            self.secondary_fan_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_total_efficiency = None
        else:
            self.secondary_fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_delta_pressure = None
        else:
            self.secondary_fan_delta_pressure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def coil_maximum_efficiency(self):
        """Get coil_maximum_efficiency

        Returns:
            float: the value of `coil_maximum_efficiency` or None if not set
        """
        return self._data["Coil Maximum Efficiency"]

    @coil_maximum_efficiency.setter
    def coil_maximum_efficiency(self, value=None):
        """  Corresponds to IDD Field `Coil Maximum Efficiency`

        Args:
            value (float): value for IDD Field `Coil Maximum Efficiency`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.coil_maximum_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectWetCoil.coil_maximum_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `EvaporativeCoolerIndirectWetCoil.coil_maximum_efficiency`')
        self._data["Coil Maximum Efficiency"] = value

    @property
    def coil_flow_ratio(self):
        """Get coil_flow_ratio

        Returns:
            float: the value of `coil_flow_ratio` or None if not set
        """
        return self._data["Coil Flow Ratio"]

    @coil_flow_ratio.setter
    def coil_flow_ratio(self, value=None):
        """  Corresponds to IDD Field `Coil Flow Ratio`

        Args:
            value (float): value for IDD Field `Coil Flow Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.coil_flow_ratio`'.format(value))
        self._data["Coil Flow Ratio"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.recirculating_water_pump_power_consumption`'.format(value))
        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """Get secondary_fan_flow_rate

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set
        """
        return self._data["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Flow Rate`

        Args:
            value (float): value for IDD Field `Secondary Fan Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_flow_rate`')
        self._data["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """Get secondary_fan_total_efficiency

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set
        """
        return self._data["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Secondary Fan Total Efficiency`
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_total_efficiency`')
        self._data["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """Get secondary_fan_delta_pressure

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set
        """
        return self._data["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Delta Pressure`

        Args:
            value (float): value for IDD Field `Secondary Fan Delta Pressure`
                Units: Pa
                IP-Units: inH2O
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_delta_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectWetCoil.secondary_fan_delta_pressure`')
        self._data["Secondary Fan Delta Pressure"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.primary_air_inlet_node_name`')
        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Primary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.primary_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.primary_air_outlet_node_name`')
        self._data["Primary Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """  Corresponds to IDD Field `Control Type`
        This field is not currently used and can be left blank

        Args:
            value (str): value for IDD Field `Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.control_type`')
        self._data["Control Type"] = value

    @property
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.water_supply_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.water_supply_storage_tank_name`')
        self._data["Water Supply Storage Tank Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Inlet Node Name`
        Enter the name of an outdoor air node

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectWetCoil.secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectWetCoil.secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectWetCoil.secondary_air_inlet_node_name`')
        self._data["Secondary Air Inlet Node Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field EvaporativeCoolerIndirectWetCoil:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EvaporativeCoolerIndirectWetCoil:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EvaporativeCoolerIndirectWetCoil: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EvaporativeCoolerIndirectWetCoil: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class EvaporativeCoolerIndirectResearchSpecial(object):
    """ Corresponds to IDD object `EvaporativeCooler:Indirect:ResearchSpecial`
        Indirect evaporative cooler with user-specified effectiveness (can represent rigid pad
        or wetted coil), recirculating water pump, and secondary air fan. This model is
        controlled to meet the primary air outlet temperature setpoint.
    """
    internal_name = "EvaporativeCooler:Indirect:ResearchSpecial"
    field_count = 18
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeCooler:Indirect:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Cooler Maximum Effectiveness"] = None
        self._data["Cooler Flow Ratio"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Secondary Fan Flow Rate"] = None
        self._data["Secondary Fan Total Efficiency"] = None
        self._data["Secondary Fan Delta Pressure"] = None
        self._data["Primary Air Inlet Node Name"] = None
        self._data["Primary Air Outlet Node Name"] = None
        self._data["Control Type"] = None
        self._data["Dewpoint Effectiveness Factor"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Relief Air Inlet Node Name"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["Drift Loss Fraction"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooler_maximum_effectiveness = None
        else:
            self.cooler_maximum_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooler_flow_ratio = None
        else:
            self.cooler_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_flow_rate = None
        else:
            self.secondary_fan_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_total_efficiency = None
        else:
            self.secondary_fan_total_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_fan_delta_pressure = None
        else:
            self.secondary_fan_delta_pressure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.primary_air_inlet_node_name = None
        else:
            self.primary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.primary_air_outlet_node_name = None
        else:
            self.primary_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type = None
        else:
            self.control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dewpoint_effectiveness_factor = None
        else:
            self.dewpoint_effectiveness_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.secondary_air_inlet_node_name = None
        else:
            self.secondary_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relief_air_inlet_node_name = None
        else:
            self.relief_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_fraction = None
        else:
            self.drift_loss_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def cooler_maximum_effectiveness(self):
        """Get cooler_maximum_effectiveness

        Returns:
            float: the value of `cooler_maximum_effectiveness` or None if not set
        """
        return self._data["Cooler Maximum Effectiveness"]

    @cooler_maximum_effectiveness.setter
    def cooler_maximum_effectiveness(self, value=None):
        """  Corresponds to IDD Field `Cooler Maximum Effectiveness`

        Args:
            value (float): value for IDD Field `Cooler Maximum Effectiveness`
                value >= 0.0
                value <= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.cooler_maximum_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.cooler_maximum_effectiveness`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.cooler_maximum_effectiveness`')
        self._data["Cooler Maximum Effectiveness"] = value

    @property
    def cooler_flow_ratio(self):
        """Get cooler_flow_ratio

        Returns:
            float: the value of `cooler_flow_ratio` or None if not set
        """
        return self._data["Cooler Flow Ratio"]

    @cooler_flow_ratio.setter
    def cooler_flow_ratio(self, value=None):
        """  Corresponds to IDD Field `Cooler Flow Ratio`

        Args:
            value (float): value for IDD Field `Cooler Flow Ratio`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.cooler_flow_ratio`'.format(value))
        self._data["Cooler Flow Ratio"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.recirculating_water_pump_power_consumption`'.format(value))
        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """Get secondary_fan_flow_rate

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set
        """
        return self._data["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Secondary Fan Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Secondary Fan Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_flow_rate`'.format(value))
                    self._data["Secondary Fan Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_flow_rate`')
        self._data["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """Get secondary_fan_total_efficiency

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set
        """
        return self._data["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Secondary Fan Total Efficiency`
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_total_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_total_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_total_efficiency`')
        self._data["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """Get secondary_fan_delta_pressure

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set
        """
        return self._data["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """  Corresponds to IDD Field `Secondary Fan Delta Pressure`

        Args:
            value (float): value for IDD Field `Secondary Fan Delta Pressure`
                Units: Pa
                IP-Units: inH2O
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_delta_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_fan_delta_pressure`')
        self._data["Secondary Fan Delta Pressure"] = value

    @property
    def primary_air_inlet_node_name(self):
        """Get primary_air_inlet_node_name

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set
        """
        return self._data["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.primary_air_inlet_node_name`')
        self._data["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """Get primary_air_outlet_node_name

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set
        """
        return self._data["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Primary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.primary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.primary_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.primary_air_outlet_node_name`')
        self._data["Primary Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """Get control_type

        Returns:
            str: the value of `control_type` or None if not set
        """
        return self._data["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """  Corresponds to IDD Field `Control Type`

        Args:
            value (str): value for IDD Field `Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.control_type`')
        self._data["Control Type"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """Get dewpoint_effectiveness_factor

        Returns:
            float: the value of `dewpoint_effectiveness_factor` or None if not set
        """
        return self._data["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """  Corresponds to IDD Field `Dewpoint Effectiveness Factor`

        Args:
            value (float): value for IDD Field `Dewpoint Effectiveness Factor`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.dewpoint_effectiveness_factor`'.format(value))
        self._data["Dewpoint Effectiveness Factor"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """Get secondary_air_inlet_node_name

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set
        """
        return self._data["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.secondary_air_inlet_node_name`')
        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.sensor_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.sensor_node_name`')
        self._data["Sensor Node Name"] = value

    @property
    def relief_air_inlet_node_name(self):
        """Get relief_air_inlet_node_name

        Returns:
            str: the value of `relief_air_inlet_node_name` or None if not set
        """
        return self._data["Relief Air Inlet Node Name"]

    @relief_air_inlet_node_name.setter
    def relief_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Relief Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Relief Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.relief_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.relief_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.relief_air_inlet_node_name`')
        self._data["Relief Air Inlet Node Name"] = value

    @property
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.water_supply_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.water_supply_storage_tank_name`')
        self._data["Water Supply Storage Tank Name"] = value

    @property
    def drift_loss_fraction(self):
        """Get drift_loss_fraction

        Returns:
            float: the value of `drift_loss_fraction` or None if not set
        """
        return self._data["Drift Loss Fraction"]

    @drift_loss_fraction.setter
    def drift_loss_fraction(self, value=None):
        """  Corresponds to IDD Field `Drift Loss Fraction`
        Rate of drift loss as a fraction of evaporated water flow rate

        Args:
            value (float): value for IDD Field `Drift Loss Fraction`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.drift_loss_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.drift_loss_fraction`')
        self._data["Drift Loss Fraction"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=None):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the evaporative cooler.
        Blowdown is water intentionally drained from the cooler in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        A typical value is 3.  If left blank then there is no blowdown.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerIndirectResearchSpecial.blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `EvaporativeCoolerIndirectResearchSpecial.blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field EvaporativeCoolerIndirectResearchSpecial:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EvaporativeCoolerIndirectResearchSpecial:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EvaporativeCoolerIndirectResearchSpecial: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EvaporativeCoolerIndirectResearchSpecial: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class EvaporativeCoolerDirectResearchSpecial(object):
    """ Corresponds to IDD object `EvaporativeCooler:Direct:ResearchSpecial`
        Direct evaporative cooler with user-specified effectiveness (can represent rigid pad
        or similar media), and recirculating water pump, and secondary air fan. This model is
        controlled to meet the primary air outlet temperature setpoint.
    """
    internal_name = "EvaporativeCooler:Direct:ResearchSpecial"
    field_count = 10
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EvaporativeCooler:Direct:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Cooler Effectiveness"] = None
        self._data["Recirculating Water Pump Power Consumption"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["Drift Loss Fraction"] = None
        self._data["Blowdown Concentration Ratio"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooler_effectiveness = None
        else:
            self.cooler_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.recirculating_water_pump_power_consumption = None
        else:
            self.recirculating_water_pump_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensor_node_name = None
        else:
            self.sensor_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drift_loss_fraction = None
        else:
            self.drift_loss_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.blowdown_concentration_ratio = None
        else:
            self.blowdown_concentration_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def cooler_effectiveness(self):
        """Get cooler_effectiveness

        Returns:
            float: the value of `cooler_effectiveness` or None if not set
        """
        return self._data["Cooler Effectiveness"]

    @cooler_effectiveness.setter
    def cooler_effectiveness(self, value=None):
        """  Corresponds to IDD Field `Cooler Effectiveness`
        effectiveness with respect to wetbulb depression

        Args:
            value (float): value for IDD Field `Cooler Effectiveness`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.cooler_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.cooler_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.cooler_effectiveness`')
        self._data["Cooler Effectiveness"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """Get recirculating_water_pump_power_consumption

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set
        """
        return self._data["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.recirculating_water_pump_power_consumption`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.recirculating_water_pump_power_consumption`')
        self._data["Recirculating Water Pump Power Consumption"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def sensor_node_name(self):
        """Get sensor_node_name

        Returns:
            str: the value of `sensor_node_name` or None if not set
        """
        return self._data["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """  Corresponds to IDD Field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.sensor_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.sensor_node_name`')
        self._data["Sensor Node Name"] = value

    @property
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.water_supply_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.water_supply_storage_tank_name`')
        self._data["Water Supply Storage Tank Name"] = value

    @property
    def drift_loss_fraction(self):
        """Get drift_loss_fraction

        Returns:
            float: the value of `drift_loss_fraction` or None if not set
        """
        return self._data["Drift Loss Fraction"]

    @drift_loss_fraction.setter
    def drift_loss_fraction(self, value=None):
        """  Corresponds to IDD Field `Drift Loss Fraction`
        Rate of drift loss as a fraction of evaporated water flow rate

        Args:
            value (float): value for IDD Field `Drift Loss Fraction`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.drift_loss_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.drift_loss_fraction`')
        self._data["Drift Loss Fraction"] = value

    @property
    def blowdown_concentration_ratio(self):
        """Get blowdown_concentration_ratio

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self._data["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=None):
        """  Corresponds to IDD Field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the evaporative cooler.
        Blowdown is water intentionally drained from the cooler in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        A typical value is 3. If left blank then there is no blowdown.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                value >= 2.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `EvaporativeCoolerDirectResearchSpecial.blowdown_concentration_ratio`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `EvaporativeCoolerDirectResearchSpecial.blowdown_concentration_ratio`')
        self._data["Blowdown Concentration Ratio"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field EvaporativeCoolerDirectResearchSpecial:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EvaporativeCoolerDirectResearchSpecial:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EvaporativeCoolerDirectResearchSpecial: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EvaporativeCoolerDirectResearchSpecial: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])