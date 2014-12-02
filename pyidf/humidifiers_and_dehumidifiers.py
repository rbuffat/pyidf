from collections import OrderedDict
import logging
import re

class HumidifierSteamElectric(object):
    """ Corresponds to IDD object `Humidifier:Steam:Electric`
        Electrically heated steam humidifier with fan.
    """
    internal_name = "Humidifier:Steam:Electric"
    field_count = 9
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Humidifier:Steam:Electric`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Rated Capacity"] = None
        self._data["Rated Power"] = None
        self._data["Rated Fan Power"] = None
        self._data["Standby Power"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Water Storage Tank Name"] = None
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
            self.rated_capacity = None
        else:
            self.rated_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_power = None
        else:
            self.rated_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_fan_power = None
        else:
            self.rated_fan_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.standby_power = None
        else:
            self.standby_power = vals[i]
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
            self.water_storage_tank_name = None
        else:
            self.water_storage_tank_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def rated_capacity(self):
        """Get rated_capacity

        Returns:
            float: the value of `rated_capacity` or None if not set
        """
        return self._data["Rated Capacity"]

    @rated_capacity.setter
    def rated_capacity(self, value=None):
        """  Corresponds to IDD Field `Rated Capacity`
        Capacity is m3/s of water at 5.05 C

        Args:
            value (float): value for IDD Field `Rated Capacity`
                Units: m3/s
                IP-Units: gal/min
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
                                 'for field `rated_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_capacity`')
        self._data["Rated Capacity"] = value

    @property
    def rated_power(self):
        """Get rated_power

        Returns:
            float: the value of `rated_power` or None if not set
        """
        return self._data["Rated Power"]

    @rated_power.setter
    def rated_power(self, value=None):
        """  Corresponds to IDD Field `Rated Power`
        if autosized the rated power is calculated from the rated capacity
        and enthalpy rise of water from 20.0C to 100.0C steam and assumes
        electric to thermal energy conversion efficiency of 100.0%

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power`
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
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Rated Power"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logging.warn('Accept value {} as "Autosize" '
                                 'for field `rated_power`'.format(value))
                    self._data["Rated Power"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 'for field `rated_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_power`')
        self._data["Rated Power"] = value

    @property
    def rated_fan_power(self):
        """Get rated_fan_power

        Returns:
            float: the value of `rated_fan_power` or None if not set
        """
        return self._data["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=None):
        """  Corresponds to IDD Field `Rated Fan Power`

        Args:
            value (float): value for IDD Field `Rated Fan Power`
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
                                 'for field `rated_fan_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_fan_power`')
        self._data["Rated Fan Power"] = value

    @property
    def standby_power(self):
        """Get standby_power

        Returns:
            float: the value of `standby_power` or None if not set
        """
        return self._data["Standby Power"]

    @standby_power.setter
    def standby_power(self, value=None):
        """  Corresponds to IDD Field `Standby Power`

        Args:
            value (float): value for IDD Field `Standby Power`
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
                                 'for field `standby_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `standby_power`')
        self._data["Standby Power"] = value

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
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')
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
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def water_storage_tank_name(self):
        """Get water_storage_tank_name

        Returns:
            str: the value of `water_storage_tank_name` or None if not set
        """
        return self._data["Water Storage Tank Name"]

    @water_storage_tank_name.setter
    def water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Storage Tank Name`
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
                                 'for field `water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_storage_tank_name`')
        self._data["Water Storage Tank Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DehumidifierDesiccantNoFans(object):
    """ Corresponds to IDD object `Dehumidifier:Desiccant:NoFans`
        This object models a solid desiccant dehumidifier. The process
        air stream is the air which is dehumidified. The regeneration air
        stream is the air which is heated to regenerate the desiccant.
        This object determines the process air outlet conditions, the
        load on the regeneration heating coil, the electric power consumption
        for the wheel rotor motor, and the regeneration air fan mass flow rate.
        All other heat exchangers are modeled as separate objects connected
        to the inlet and outlet nodes of the dehumidifier. The solid
        desiccant dehumidifier is typically used in an AirLoopHVAC:OutdoorAirSystem,
        but can also be specified in any AirLoopHVAC.
    """
    internal_name = "Dehumidifier:Desiccant:NoFans"
    field_count = 25
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Dehumidifier:Desiccant:NoFans`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Process Air Inlet Node Name"] = None
        self._data["Process Air Outlet Node Name"] = None
        self._data["Regeneration Air Inlet Node Name"] = None
        self._data["Regeneration Fan Inlet Node Name"] = None
        self._data["Control Type"] = None
        self._data["Leaving Maximum Humidity Ratio Setpoint"] = None
        self._data["Nominal Process Air Flow Rate"] = None
        self._data["Nominal Process Air Velocity"] = None
        self._data["Rotor Power"] = None
        self._data["Regeneration Coil Object Type"] = None
        self._data["Regeneration Coil Name"] = None
        self._data["Regeneration Fan Object Type"] = None
        self._data["Regeneration Fan Name"] = None
        self._data["Performance Model Type"] = None
        self._data["Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Leaving Dry-Bulb Function of Air Velocity Curve Name"] = None
        self._data["Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Leaving Humidity Ratio Function of Air Velocity Curve Name"] = None
        self._data["Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Regeneration Energy Function of Air Velocity Curve Name"] = None
        self._data["Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = None
        self._data["Regeneration Velocity Function of Air Velocity Curve Name"] = None
        self._data["Nominal Regeneration Temperature"] = None
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
            self.process_air_inlet_node_name = None
        else:
            self.process_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.process_air_outlet_node_name = None
        else:
            self.process_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_air_inlet_node_name = None
        else:
            self.regeneration_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_fan_inlet_node_name = None
        else:
            self.regeneration_fan_inlet_node_name = vals[i]
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
            self.leaving_maximum_humidity_ratio_setpoint = None
        else:
            self.leaving_maximum_humidity_ratio_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_process_air_flow_rate = None
        else:
            self.nominal_process_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_process_air_velocity = None
        else:
            self.nominal_process_air_velocity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rotor_power = None
        else:
            self.rotor_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_coil_object_type = None
        else:
            self.regeneration_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_coil_name = None
        else:
            self.regeneration_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_fan_object_type = None
        else:
            self.regeneration_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_fan_name = None
        else:
            self.regeneration_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.performance_model_type = None
        else:
            self.performance_model_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.leaving_drybulb_function_of_air_velocity_curve_name = None
        else:
            self.leaving_drybulb_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.leaving_humidity_ratio_function_of_air_velocity_curve_name = None
        else:
            self.leaving_humidity_ratio_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_energy_function_of_air_velocity_curve_name = None
        else:
            self.regeneration_energy_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name = None
        else:
            self.regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_velocity_function_of_air_velocity_curve_name = None
        else:
            self.regeneration_velocity_function_of_air_velocity_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_regeneration_temperature = None
        else:
            self.nominal_regeneration_temperature = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def process_air_inlet_node_name(self):
        """Get process_air_inlet_node_name

        Returns:
            str: the value of `process_air_inlet_node_name` or None if not set
        """
        return self._data["Process Air Inlet Node Name"]

    @process_air_inlet_node_name.setter
    def process_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Process Air Inlet Node Name`
        This is the node entering the process side of the desiccant wheel.

        Args:
            value (str): value for IDD Field `Process Air Inlet Node Name`
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
                                 'for field `process_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `process_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `process_air_inlet_node_name`')
        self._data["Process Air Inlet Node Name"] = value

    @property
    def process_air_outlet_node_name(self):
        """Get process_air_outlet_node_name

        Returns:
            str: the value of `process_air_outlet_node_name` or None if not set
        """
        return self._data["Process Air Outlet Node Name"]

    @process_air_outlet_node_name.setter
    def process_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Process Air Outlet Node Name`
        This is the node leaving the process side of the desiccant wheel.

        Args:
            value (str): value for IDD Field `Process Air Outlet Node Name`
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
                                 'for field `process_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `process_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `process_air_outlet_node_name`')
        self._data["Process Air Outlet Node Name"] = value

    @property
    def regeneration_air_inlet_node_name(self):
        """Get regeneration_air_inlet_node_name

        Returns:
            str: the value of `regeneration_air_inlet_node_name` or None if not set
        """
        return self._data["Regeneration Air Inlet Node Name"]

    @regeneration_air_inlet_node_name.setter
    def regeneration_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Inlet Node Name`
        This is the node entering the regeneration side of the desiccant wheel
        after the regeneration coil.

        Args:
            value (str): value for IDD Field `Regeneration Air Inlet Node Name`
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
                                 'for field `regeneration_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_air_inlet_node_name`')
        self._data["Regeneration Air Inlet Node Name"] = value

    @property
    def regeneration_fan_inlet_node_name(self):
        """Get regeneration_fan_inlet_node_name

        Returns:
            str: the value of `regeneration_fan_inlet_node_name` or None if not set
        """
        return self._data["Regeneration Fan Inlet Node Name"]

    @regeneration_fan_inlet_node_name.setter
    def regeneration_fan_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Fan Inlet Node Name`
        Node for air entering the regeneration fan, mass flow is set
        by the desiccant dehumidifier module.

        Args:
            value (str): value for IDD Field `Regeneration Fan Inlet Node Name`
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
                                 'for field `regeneration_fan_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_fan_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_fan_inlet_node_name`')
        self._data["Regeneration Fan Inlet Node Name"] = value

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
        Type of setpoint control:
        LeavingMaximumHumidityRatioSetpoint means that the unit is controlled
        to deliver air at the Leaving Max Humidity Ratio Setpoint (see below),
        SystemNodeMaximumHumidityRatioSetpoint means that the leaving humidity
        ratio setpoint is the System Node Humidity Ratio Max property
        of the Process Air Outlet Node.  A Setpoint
        object must be used to control this setpoint.
        Both control types use bypass dampers to prevent overdrying.

        Args:
            value (str): value for IDD Field `Control Type`
                Accepted values are:
                      - LeavingMaximumHumidityRatioSetpoint
                      - SystemNodeMaximumHumidityRatioSetpoint
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
                                 'for field `control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_type`')
            vals = {}
            vals["leavingmaximumhumidityratiosetpoint"] = "LeavingMaximumHumidityRatioSetpoint"
            vals["systemnodemaximumhumidityratiosetpoint"] = "SystemNodeMaximumHumidityRatioSetpoint"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `control_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Control Type"] = value

    @property
    def leaving_maximum_humidity_ratio_setpoint(self):
        """Get leaving_maximum_humidity_ratio_setpoint

        Returns:
            float: the value of `leaving_maximum_humidity_ratio_setpoint` or None if not set
        """
        return self._data["Leaving Maximum Humidity Ratio Setpoint"]

    @leaving_maximum_humidity_ratio_setpoint.setter
    def leaving_maximum_humidity_ratio_setpoint(self, value=None):
        """  Corresponds to IDD Field `Leaving Maximum Humidity Ratio Setpoint`
        Fixed setpoint for maximum process air leaving humidity ratio
        Applicable only when Control Type = LeavingMaximumHumidityRatioSetpoint.

        Args:
            value (float): value for IDD Field `Leaving Maximum Humidity Ratio Setpoint`
                Units: kgWater/kgDryAir
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
                                 'for field `leaving_maximum_humidity_ratio_setpoint`'.format(value))
        self._data["Leaving Maximum Humidity Ratio Setpoint"] = value

    @property
    def nominal_process_air_flow_rate(self):
        """Get nominal_process_air_flow_rate

        Returns:
            float: the value of `nominal_process_air_flow_rate` or None if not set
        """
        return self._data["Nominal Process Air Flow Rate"]

    @nominal_process_air_flow_rate.setter
    def nominal_process_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Process Air Flow Rate`
        Process air flow rate at nominal conditions

        Args:
            value (float): value for IDD Field `Nominal Process Air Flow Rate`
                Units: m3/s
                value > 0.0
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
                                 'for field `nominal_process_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_process_air_flow_rate`')
        self._data["Nominal Process Air Flow Rate"] = value

    @property
    def nominal_process_air_velocity(self):
        """Get nominal_process_air_velocity

        Returns:
            float: the value of `nominal_process_air_velocity` or None if not set
        """
        return self._data["Nominal Process Air Velocity"]

    @nominal_process_air_velocity.setter
    def nominal_process_air_velocity(self, value=None):
        """  Corresponds to IDD Field `Nominal Process Air Velocity`
        Process air velocity at nominal flow
        When using Performance Model Type of Default, must be 2.032 to 4.064 m/s (400 to 800 fpm)

        Args:
            value (float): value for IDD Field `Nominal Process Air Velocity`
                Units: m/s
                value > 0.0
                value <= 6.0
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
                                 'for field `nominal_process_air_velocity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nominal_process_air_velocity`')
            if value > 6.0:
                raise ValueError('value need to be smaller 6.0 '
                                 'for field `nominal_process_air_velocity`')
        self._data["Nominal Process Air Velocity"] = value

    @property
    def rotor_power(self):
        """Get rotor_power

        Returns:
            float: the value of `rotor_power` or None if not set
        """
        return self._data["Rotor Power"]

    @rotor_power.setter
    def rotor_power(self, value=None):
        """  Corresponds to IDD Field `Rotor Power`
        Power input to wheel rotor motor

        Args:
            value (float): value for IDD Field `Rotor Power`
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
                                 'for field `rotor_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rotor_power`')
        self._data["Rotor Power"] = value

    @property
    def regeneration_coil_object_type(self):
        """Get regeneration_coil_object_type

        Returns:
            str: the value of `regeneration_coil_object_type` or None if not set
        """
        return self._data["Regeneration Coil Object Type"]

    @regeneration_coil_object_type.setter
    def regeneration_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Regeneration Coil Object Type`
        heating coil type
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `Regeneration Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
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
                                 'for field `regeneration_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_coil_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `regeneration_coil_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `regeneration_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Regeneration Coil Object Type"] = value

    @property
    def regeneration_coil_name(self):
        """Get regeneration_coil_name

        Returns:
            str: the value of `regeneration_coil_name` or None if not set
        """
        return self._data["Regeneration Coil Name"]

    @regeneration_coil_name.setter
    def regeneration_coil_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Coil Name`
        Name of heating coil object for regeneration air

        Args:
            value (str): value for IDD Field `Regeneration Coil Name`
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
                                 'for field `regeneration_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_coil_name`')
        self._data["Regeneration Coil Name"] = value

    @property
    def regeneration_fan_object_type(self):
        """Get regeneration_fan_object_type

        Returns:
            str: the value of `regeneration_fan_object_type` or None if not set
        """
        return self._data["Regeneration Fan Object Type"]

    @regeneration_fan_object_type.setter
    def regeneration_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Regeneration Fan Object Type`
        Type of fan object for regeneration air.  When using the Default
        Performance Model Type (see below), only Fan:VariableVolume is valid.

        Args:
            value (str): value for IDD Field `Regeneration Fan Object Type`
                Accepted values are:
                      - Fan:VariableVolume
                      - Fan:ConstantVolume
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
                                 'for field `regeneration_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_fan_object_type`')
            vals = {}
            vals["fan:variablevolume"] = "Fan:VariableVolume"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `regeneration_fan_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `regeneration_fan_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Regeneration Fan Object Type"] = value

    @property
    def regeneration_fan_name(self):
        """Get regeneration_fan_name

        Returns:
            str: the value of `regeneration_fan_name` or None if not set
        """
        return self._data["Regeneration Fan Name"]

    @regeneration_fan_name.setter
    def regeneration_fan_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Fan Name`
        Name of fan object for regeneration air

        Args:
            value (str): value for IDD Field `Regeneration Fan Name`
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
                                 'for field `regeneration_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_fan_name`')
        self._data["Regeneration Fan Name"] = value

    @property
    def performance_model_type(self):
        """Get performance_model_type

        Returns:
            str: the value of `performance_model_type` or None if not set
        """
        return self._data["Performance Model Type"]

    @performance_model_type.setter
    def performance_model_type(self, value=None):
        """  Corresponds to IDD Field `Performance Model Type`
        Specifies whether the default performance model or user-specified
        curves should be used to model the performance.  The default model
        is a generic solid desiccant wheel using performance curves of the form:
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*vel + C7*vel**2
        + C8*edb*ew + C9*edb**2*ew**2 + C10*edb*vel + C11*edb**2*vel**2
        + C12*ew*vel + C13*ew**2*vel**2 + C14*ALOG(edb) + C15*ALOG(ew) + C16*ALOG(vel)
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]
        vel = process air velocity [m/s]
        If UserCurves are specified, then performance is calculated as follows:
        Leaving Dry-Bulb = (Leaving Dry-Bulb fTW Curve) * (Leaving Dry-Bulb fV Curve)
        Leaving Humidity Ratio = (Leaving Humidity Ratio fTW Curve) * (Leaving Humidity Ratio fV Curve)
        Regen Energy = (Regen Energy fTW Curve) * (Regen Energy fV Curve)
        Regen Velocity = (Regen Velocity fTW Curve) * (Regen Velocity fV Curve)

        Args:
            value (str): value for IDD Field `Performance Model Type`
                Accepted values are:
                      - Default
                      - UserCurves
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
                                 'for field `performance_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_model_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `performance_model_type`')
            vals = {}
            vals["default"] = "Default"
            vals["usercurves"] = "UserCurves"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `performance_model_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `performance_model_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Performance Model Type"] = value

    @property
    def leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
        Leaving dry-bulb of process air as a function of entering dry-bulb
        and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
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
                                 'for field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
        self._data["Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def leaving_drybulb_function_of_air_velocity_curve_name(self):
        """Get leaving_drybulb_function_of_air_velocity_curve_name

        Returns:
            str: the value of `leaving_drybulb_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Leaving Dry-Bulb Function of Air Velocity Curve Name"]

    @leaving_drybulb_function_of_air_velocity_curve_name.setter
    def leaving_drybulb_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `Leaving Dry-Bulb Function of Air Velocity Curve Name`
        Leaving dry-bulb of process air as a function of air velocity,
        quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Leaving Dry-Bulb Function of Air Velocity Curve Name`
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
                                 'for field `leaving_drybulb_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_drybulb_function_of_air_velocity_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `leaving_drybulb_function_of_air_velocity_curve_name`')
        self._data["Leaving Dry-Bulb Function of Air Velocity Curve Name"] = value

    @property
    def leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
        Leaving humidity ratio of process air as a function of entering dry-bulb
        and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
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
                                 'for field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
        self._data["Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def leaving_humidity_ratio_function_of_air_velocity_curve_name(self):
        """Get leaving_humidity_ratio_function_of_air_velocity_curve_name

        Returns:
            str: the value of `leaving_humidity_ratio_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Leaving Humidity Ratio Function of Air Velocity Curve Name"]

    @leaving_humidity_ratio_function_of_air_velocity_curve_name.setter
    def leaving_humidity_ratio_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `Leaving Humidity Ratio Function of Air Velocity Curve Name`
        Leaving humidity ratio of process air as a function of
        process air velocity, quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Leaving Humidity Ratio Function of Air Velocity Curve Name`
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
                                 'for field `leaving_humidity_ratio_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `leaving_humidity_ratio_function_of_air_velocity_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `leaving_humidity_ratio_function_of_air_velocity_curve_name`')
        self._data["Leaving Humidity Ratio Function of Air Velocity Curve Name"] = value

    @property
    def regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
        Regeneration energy [J/kg of water removed] as a function of
        entering dry-bulb and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
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
                                 'for field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
        self._data["Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def regeneration_energy_function_of_air_velocity_curve_name(self):
        """Get regeneration_energy_function_of_air_velocity_curve_name

        Returns:
            str: the value of `regeneration_energy_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Regeneration Energy Function of Air Velocity Curve Name"]

    @regeneration_energy_function_of_air_velocity_curve_name.setter
    def regeneration_energy_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Energy Function of Air Velocity Curve Name`
        Regeneration energy [J/kg of water removed] as a function of
        process air velocity, quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Regeneration Energy Function of Air Velocity Curve Name`
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
                                 'for field `regeneration_energy_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_energy_function_of_air_velocity_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_energy_function_of_air_velocity_curve_name`')
        self._data["Regeneration Energy Function of Air Velocity Curve Name"] = value

    @property
    def regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name(self):
        """Get regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name

        Returns:
            str: the value of `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self._data["Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
        Regeneration velocity [m/s] as a function of
        entering dry-bulb and entering humidity ratio, biquadratic curve
        Table:TwoIndependentVariables object can also be used
        curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        edb = process entering dry-bulb temperature [C]
        ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name`
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
                                 'for field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name`')
        self._data["Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def regeneration_velocity_function_of_air_velocity_curve_name(self):
        """Get regeneration_velocity_function_of_air_velocity_curve_name

        Returns:
            str: the value of `regeneration_velocity_function_of_air_velocity_curve_name` or None if not set
        """
        return self._data["Regeneration Velocity Function of Air Velocity Curve Name"]

    @regeneration_velocity_function_of_air_velocity_curve_name.setter
    def regeneration_velocity_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Velocity Function of Air Velocity Curve Name`
        Regeneration velocity [m/s] as a function of
        process air velocity, quadratic curve.
        Table:OneIndependentVariable object can also be used
        curve = C1 + C2*v + C3*v**2
        v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Regeneration Velocity Function of Air Velocity Curve Name`
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
                                 'for field `regeneration_velocity_function_of_air_velocity_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_velocity_function_of_air_velocity_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_velocity_function_of_air_velocity_curve_name`')
        self._data["Regeneration Velocity Function of Air Velocity Curve Name"] = value

    @property
    def nominal_regeneration_temperature(self):
        """Get nominal_regeneration_temperature

        Returns:
            float: the value of `nominal_regeneration_temperature` or None if not set
        """
        return self._data["Nominal Regeneration Temperature"]

    @nominal_regeneration_temperature.setter
    def nominal_regeneration_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Regeneration Temperature`
        Nominal regen temperature upon which the regen energy modifier
        curve is based.  Not used if Default if chosen for the field Performance Mode Type.
        121 C is a commonly used value.

        Args:
            value (float): value for IDD Field `Nominal Regeneration Temperature`
                Units: C
                value >= 40.0
                value <= 250.0
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
                                 'for field `nominal_regeneration_temperature`'.format(value))
            if value < 40.0:
                raise ValueError('value need to be greater or equal 40.0 '
                                 'for field `nominal_regeneration_temperature`')
            if value > 250.0:
                raise ValueError('value need to be smaller 250.0 '
                                 'for field `nominal_regeneration_temperature`')
        self._data["Nominal Regeneration Temperature"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DehumidifierDesiccantSystem(object):
    """ Corresponds to IDD object `Dehumidifier:Desiccant:System`
        This compound object models a desiccant heat exchanger, an optional
        heater, and associated fans. The process air stream is the air which
        is dehumidified. The regeneration air stream is the air which is
        heated to regenerate the desiccant. The desiccant heat exchanger
        transfers both sensible and latent energy between the process and
        regeneration air streams. The desiccant dehumidifier is typically used
        in an AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC.
    """
    internal_name = "Dehumidifier:Desiccant:System"
    field_count = 18
    required_fields = ["Name", "Desiccant Heat Exchanger Object Type", "Desiccant Heat Exchanger Name", "Sensor Node Name", "Regeneration Air Fan Object Type", "Regeneration Air Fan Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Dehumidifier:Desiccant:System`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Desiccant Heat Exchanger Object Type"] = None
        self._data["Desiccant Heat Exchanger Name"] = None
        self._data["Sensor Node Name"] = None
        self._data["Regeneration Air Fan Object Type"] = None
        self._data["Regeneration Air Fan Name"] = None
        self._data["Regeneration Air Fan Placement"] = None
        self._data["Regeneration Air Heater Object Type"] = None
        self._data["Regeneration Air Heater Name"] = None
        self._data["Regeneration Inlet Air Setpoint Temperature"] = None
        self._data["Companion Cooling Coil Object Type"] = None
        self._data["Companion Cooling Coil Name"] = None
        self._data["Companion Cooling Coil Upstream of Dehumidifier Process Inlet"] = None
        self._data["Companion Coil Regeneration Air Heating"] = None
        self._data["Exhaust Fan Maximum Flow Rate"] = None
        self._data["Exhaust Fan Maximum Power"] = None
        self._data["Exhaust Fan Power Curve Name"] = None
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
            self.desiccant_heat_exchanger_object_type = None
        else:
            self.desiccant_heat_exchanger_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.desiccant_heat_exchanger_name = None
        else:
            self.desiccant_heat_exchanger_name = vals[i]
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
            self.regeneration_air_fan_object_type = None
        else:
            self.regeneration_air_fan_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_air_fan_name = None
        else:
            self.regeneration_air_fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_air_fan_placement = None
        else:
            self.regeneration_air_fan_placement = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_air_heater_object_type = None
        else:
            self.regeneration_air_heater_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_air_heater_name = None
        else:
            self.regeneration_air_heater_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_inlet_air_setpoint_temperature = None
        else:
            self.regeneration_inlet_air_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.companion_cooling_coil_object_type = None
        else:
            self.companion_cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.companion_cooling_coil_name = None
        else:
            self.companion_cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.companion_cooling_coil_upstream_of_dehumidifier_process_inlet = None
        else:
            self.companion_cooling_coil_upstream_of_dehumidifier_process_inlet = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.companion_coil_regeneration_air_heating = None
        else:
            self.companion_coil_regeneration_air_heating = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_fan_maximum_flow_rate = None
        else:
            self.exhaust_fan_maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_fan_maximum_power = None
        else:
            self.exhaust_fan_maximum_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_fan_power_curve_name = None
        else:
            self.exhaust_fan_power_curve_name = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def desiccant_heat_exchanger_object_type(self):
        """Get desiccant_heat_exchanger_object_type

        Returns:
            str: the value of `desiccant_heat_exchanger_object_type` or None if not set
        """
        return self._data["Desiccant Heat Exchanger Object Type"]

    @desiccant_heat_exchanger_object_type.setter
    def desiccant_heat_exchanger_object_type(self, value=None):
        """  Corresponds to IDD Field `Desiccant Heat Exchanger Object Type`

        Args:
            value (str): value for IDD Field `Desiccant Heat Exchanger Object Type`
                Accepted values are:
                      - HeatExchanger:Desiccant:BalancedFlow
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
                                 'for field `desiccant_heat_exchanger_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `desiccant_heat_exchanger_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `desiccant_heat_exchanger_object_type`')
            vals = {}
            vals["heatexchanger:desiccant:balancedflow"] = "HeatExchanger:Desiccant:BalancedFlow"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `desiccant_heat_exchanger_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `desiccant_heat_exchanger_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Desiccant Heat Exchanger Object Type"] = value

    @property
    def desiccant_heat_exchanger_name(self):
        """Get desiccant_heat_exchanger_name

        Returns:
            str: the value of `desiccant_heat_exchanger_name` or None if not set
        """
        return self._data["Desiccant Heat Exchanger Name"]

    @desiccant_heat_exchanger_name.setter
    def desiccant_heat_exchanger_name(self, value=None):
        """  Corresponds to IDD Field `Desiccant Heat Exchanger Name`

        Args:
            value (str): value for IDD Field `Desiccant Heat Exchanger Name`
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
                                 'for field `desiccant_heat_exchanger_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `desiccant_heat_exchanger_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `desiccant_heat_exchanger_name`')
        self._data["Desiccant Heat Exchanger Name"] = value

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
                                 'for field `sensor_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensor_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `sensor_node_name`')
        self._data["Sensor Node Name"] = value

    @property
    def regeneration_air_fan_object_type(self):
        """Get regeneration_air_fan_object_type

        Returns:
            str: the value of `regeneration_air_fan_object_type` or None if not set
        """
        return self._data["Regeneration Air Fan Object Type"]

    @regeneration_air_fan_object_type.setter
    def regeneration_air_fan_object_type(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Fan Object Type`

        Args:
            value (str): value for IDD Field `Regeneration Air Fan Object Type`
                Accepted values are:
                      - Fan:OnOff
                      - Fan:ConstantVolume
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
                                 'for field `regeneration_air_fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_air_fan_object_type`')
            vals = {}
            vals["fan:onoff"] = "Fan:OnOff"
            vals["fan:constantvolume"] = "Fan:ConstantVolume"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `regeneration_air_fan_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `regeneration_air_fan_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Regeneration Air Fan Object Type"] = value

    @property
    def regeneration_air_fan_name(self):
        """Get regeneration_air_fan_name

        Returns:
            str: the value of `regeneration_air_fan_name` or None if not set
        """
        return self._data["Regeneration Air Fan Name"]

    @regeneration_air_fan_name.setter
    def regeneration_air_fan_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Fan Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Fan Name`
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
                                 'for field `regeneration_air_fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_air_fan_name`')
        self._data["Regeneration Air Fan Name"] = value

    @property
    def regeneration_air_fan_placement(self):
        """Get regeneration_air_fan_placement

        Returns:
            str: the value of `regeneration_air_fan_placement` or None if not set
        """
        return self._data["Regeneration Air Fan Placement"]

    @regeneration_air_fan_placement.setter
    def regeneration_air_fan_placement(self, value="DrawThrough"):
        """  Corresponds to IDD Field `Regeneration Air Fan Placement`

        Args:
            value (str): value for IDD Field `Regeneration Air Fan Placement`
                Accepted values are:
                      - BlowThrough
                      - DrawThrough
                Default value: DrawThrough
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
                                 'for field `regeneration_air_fan_placement`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_fan_placement`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_air_fan_placement`')
            vals = {}
            vals["blowthrough"] = "BlowThrough"
            vals["drawthrough"] = "DrawThrough"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `regeneration_air_fan_placement`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `regeneration_air_fan_placement`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Regeneration Air Fan Placement"] = value

    @property
    def regeneration_air_heater_object_type(self):
        """Get regeneration_air_heater_object_type

        Returns:
            str: the value of `regeneration_air_heater_object_type` or None if not set
        """
        return self._data["Regeneration Air Heater Object Type"]

    @regeneration_air_heater_object_type.setter
    def regeneration_air_heater_object_type(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Heater Object Type`
        works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `Regeneration Air Heater Object Type`
                Accepted values are:
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Water
                      - Coil:Heating:Steam
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
                                 'for field `regeneration_air_heater_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_heater_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_air_heater_object_type`')
            vals = {}
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `regeneration_air_heater_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `regeneration_air_heater_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Regeneration Air Heater Object Type"] = value

    @property
    def regeneration_air_heater_name(self):
        """Get regeneration_air_heater_name

        Returns:
            str: the value of `regeneration_air_heater_name` or None if not set
        """
        return self._data["Regeneration Air Heater Name"]

    @regeneration_air_heater_name.setter
    def regeneration_air_heater_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Heater Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Heater Name`
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
                                 'for field `regeneration_air_heater_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `regeneration_air_heater_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `regeneration_air_heater_name`')
        self._data["Regeneration Air Heater Name"] = value

    @property
    def regeneration_inlet_air_setpoint_temperature(self):
        """Get regeneration_inlet_air_setpoint_temperature

        Returns:
            float: the value of `regeneration_inlet_air_setpoint_temperature` or None if not set
        """
        return self._data["Regeneration Inlet Air Setpoint Temperature"]

    @regeneration_inlet_air_setpoint_temperature.setter
    def regeneration_inlet_air_setpoint_temperature(self, value=None):
        """  Corresponds to IDD Field `Regeneration Inlet Air Setpoint Temperature`

        Args:
            value (float): value for IDD Field `Regeneration Inlet Air Setpoint Temperature`
                Units: C
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
                                 'for field `regeneration_inlet_air_setpoint_temperature`'.format(value))
        self._data["Regeneration Inlet Air Setpoint Temperature"] = value

    @property
    def companion_cooling_coil_object_type(self):
        """Get companion_cooling_coil_object_type

        Returns:
            str: the value of `companion_cooling_coil_object_type` or None if not set
        """
        return self._data["Companion Cooling Coil Object Type"]

    @companion_cooling_coil_object_type.setter
    def companion_cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Companion Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Companion Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:DX:SingleSpeed
                      - Coil:Cooling:DX:TwoStageWithHumidityControlMode
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
                                 'for field `companion_cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `companion_cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:dx:singlespeed"] = "Coil:Cooling:DX:SingleSpeed"
            vals["coil:cooling:dx:twostagewithhumiditycontrolmode"] = "Coil:Cooling:DX:TwoStageWithHumidityControlMode"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `companion_cooling_coil_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `companion_cooling_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Companion Cooling Coil Object Type"] = value

    @property
    def companion_cooling_coil_name(self):
        """Get companion_cooling_coil_name

        Returns:
            str: the value of `companion_cooling_coil_name` or None if not set
        """
        return self._data["Companion Cooling Coil Name"]

    @companion_cooling_coil_name.setter
    def companion_cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Companion Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Companion Cooling Coil Name`
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
                                 'for field `companion_cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `companion_cooling_coil_name`')
        self._data["Companion Cooling Coil Name"] = value

    @property
    def companion_cooling_coil_upstream_of_dehumidifier_process_inlet(self):
        """Get companion_cooling_coil_upstream_of_dehumidifier_process_inlet

        Returns:
            str: the value of `companion_cooling_coil_upstream_of_dehumidifier_process_inlet` or None if not set
        """
        return self._data["Companion Cooling Coil Upstream of Dehumidifier Process Inlet"]

    @companion_cooling_coil_upstream_of_dehumidifier_process_inlet.setter
    def companion_cooling_coil_upstream_of_dehumidifier_process_inlet(self, value="No"):
        """  Corresponds to IDD Field `Companion Cooling Coil Upstream of Dehumidifier Process Inlet`
        Select Yes if the companion cooling coil is located directly upstream
        of the desiccant heat exchanger's process air inlet node.

        Args:
            value (str): value for IDD Field `Companion Cooling Coil Upstream of Dehumidifier Process Inlet`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `companion_cooling_coil_upstream_of_dehumidifier_process_inlet`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Companion Cooling Coil Upstream of Dehumidifier Process Inlet"] = value

    @property
    def companion_coil_regeneration_air_heating(self):
        """Get companion_coil_regeneration_air_heating

        Returns:
            str: the value of `companion_coil_regeneration_air_heating` or None if not set
        """
        return self._data["Companion Coil Regeneration Air Heating"]

    @companion_coil_regeneration_air_heating.setter
    def companion_coil_regeneration_air_heating(self, value="No"):
        """  Corresponds to IDD Field `Companion Coil Regeneration Air Heating`

        Args:
            value (str): value for IDD Field `Companion Coil Regeneration Air Heating`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `companion_coil_regeneration_air_heating`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `companion_coil_regeneration_air_heating`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `companion_coil_regeneration_air_heating`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `companion_coil_regeneration_air_heating`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `companion_coil_regeneration_air_heating`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Companion Coil Regeneration Air Heating"] = value

    @property
    def exhaust_fan_maximum_flow_rate(self):
        """Get exhaust_fan_maximum_flow_rate

        Returns:
            float: the value of `exhaust_fan_maximum_flow_rate` or None if not set
        """
        return self._data["Exhaust Fan Maximum Flow Rate"]

    @exhaust_fan_maximum_flow_rate.setter
    def exhaust_fan_maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Exhaust Fan Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Exhaust Fan Maximum Flow Rate`
                Units: m3/s
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
                                 'for field `exhaust_fan_maximum_flow_rate`'.format(value))
        self._data["Exhaust Fan Maximum Flow Rate"] = value

    @property
    def exhaust_fan_maximum_power(self):
        """Get exhaust_fan_maximum_power

        Returns:
            float: the value of `exhaust_fan_maximum_power` or None if not set
        """
        return self._data["Exhaust Fan Maximum Power"]

    @exhaust_fan_maximum_power.setter
    def exhaust_fan_maximum_power(self, value=None):
        """  Corresponds to IDD Field `Exhaust Fan Maximum Power`

        Args:
            value (float): value for IDD Field `Exhaust Fan Maximum Power`
                Units: W
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
                                 'for field `exhaust_fan_maximum_power`'.format(value))
        self._data["Exhaust Fan Maximum Power"] = value

    @property
    def exhaust_fan_power_curve_name(self):
        """Get exhaust_fan_power_curve_name

        Returns:
            str: the value of `exhaust_fan_power_curve_name` or None if not set
        """
        return self._data["Exhaust Fan Power Curve Name"]

    @exhaust_fan_power_curve_name.setter
    def exhaust_fan_power_curve_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Fan Power Curve Name`
        Curve object type must be Curve:Quadratic or Curve:Cubic
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Exhaust Fan Power Curve Name`
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
                                 'for field `exhaust_fan_power_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exhaust_fan_power_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exhaust_fan_power_curve_name`')
        self._data["Exhaust Fan Power Curve Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])