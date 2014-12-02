from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class HeatExchangerAirToAirFlatPlate(object):
    """ Corresponds to IDD object `HeatExchanger:AirToAir:FlatPlate`
        Flat plate air-to-air heat exchanger, typically used for exhaust or relief air heat
        recovery.
    """
    internal_name = "HeatExchanger:AirToAir:FlatPlate"
    field_count = 15
    required_fields = ["Name", "Nominal Supply Air Flow Rate", "Nominal Supply Air Inlet Temperature", "Nominal Supply Air Outlet Temperature", "Nominal Secondary Air Flow Rate", "Nominal Secondary Air Inlet Temperature", "Supply Air Inlet Node Name", "Supply Air Outlet Node Name", "Secondary Air Inlet Node Name", "Secondary Air Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 15
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatExchanger:AirToAir:FlatPlate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Flow Arrangement Type"] = None
        self._data["Economizer Lockout"] = None
        self._data["Ratio of Supply to Secondary hA Values"] = None
        self._data["Nominal Supply Air Flow Rate"] = None
        self._data["Nominal Supply Air Inlet Temperature"] = None
        self._data["Nominal Supply Air Outlet Temperature"] = None
        self._data["Nominal Secondary Air Flow Rate"] = None
        self._data["Nominal Secondary Air Inlet Temperature"] = None
        self._data["Nominal Electric Power"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Supply Air Outlet Node Name"] = None
        self._data["Secondary Air Inlet Node Name"] = None
        self._data["Secondary Air Outlet Node Name"] = None
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
            self.flow_arrangement_type = None
        else:
            self.flow_arrangement_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_lockout = None
        else:
            self.economizer_lockout = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_supply_to_secondary_ha_values = None
        else:
            self.ratio_of_supply_to_secondary_ha_values = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_supply_air_flow_rate = None
        else:
            self.nominal_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_supply_air_inlet_temperature = None
        else:
            self.nominal_supply_air_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_supply_air_outlet_temperature = None
        else:
            self.nominal_supply_air_outlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_secondary_air_flow_rate = None
        else:
            self.nominal_secondary_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_secondary_air_inlet_temperature = None
        else:
            self.nominal_secondary_air_inlet_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_electric_power = None
        else:
            self.nominal_electric_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_outlet_node_name = None
        else:
            self.supply_air_outlet_node_name = vals[i]
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
            self.secondary_air_outlet_node_name = None
        else:
            self.secondary_air_outlet_node_name = vals[i]
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.name`')
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def flow_arrangement_type(self):
        """Get flow_arrangement_type

        Returns:
            str: the value of `flow_arrangement_type` or None if not set
        """
        return self._data["Flow Arrangement Type"]

    @flow_arrangement_type.setter
    def flow_arrangement_type(self, value=None):
        """  Corresponds to IDD Field `Flow Arrangement Type`

        Args:
            value (str): value for IDD Field `Flow Arrangement Type`
                Accepted values are:
                      - CounterFlow
                      - ParallelFlow
                      - CrossFlowBothUnmixed
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.flow_arrangement_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.flow_arrangement_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.flow_arrangement_type`')
            vals = {}
            vals["counterflow"] = "CounterFlow"
            vals["parallelflow"] = "ParallelFlow"
            vals["crossflowbothunmixed"] = "CrossFlowBothUnmixed"
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
                                     'field `HeatExchangerAirToAirFlatPlate.flow_arrangement_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerAirToAirFlatPlate.flow_arrangement_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Flow Arrangement Type"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self._data["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """  Corresponds to IDD Field `Economizer Lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `Economizer Lockout`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.economizer_lockout`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.economizer_lockout`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.economizer_lockout`')
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
                                     'field `HeatExchangerAirToAirFlatPlate.economizer_lockout`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerAirToAirFlatPlate.economizer_lockout`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Economizer Lockout"] = value

    @property
    def ratio_of_supply_to_secondary_ha_values(self):
        """Get ratio_of_supply_to_secondary_ha_values

        Returns:
            float: the value of `ratio_of_supply_to_secondary_ha_values` or None if not set
        """
        return self._data["Ratio of Supply to Secondary hA Values"]

    @ratio_of_supply_to_secondary_ha_values.setter
    def ratio_of_supply_to_secondary_ha_values(self, value=None):
        """  Corresponds to IDD Field `Ratio of Supply to Secondary hA Values`
        Ratio of h*A for supply side to h*A for exhaust side

        Args:
            value (float): value for IDD Field `Ratio of Supply to Secondary hA Values`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.ratio_of_supply_to_secondary_ha_values`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirFlatPlate.ratio_of_supply_to_secondary_ha_values`')
        self._data["Ratio of Supply to Secondary hA Values"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """Get nominal_supply_air_flow_rate

        Returns:
            float: the value of `nominal_supply_air_flow_rate` or None if not set
        """
        return self._data["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Flow Rate`

        Args:
            value (float): value for IDD Field `Nominal Supply Air Flow Rate`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.nominal_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerAirToAirFlatPlate.nominal_supply_air_flow_rate`')
        self._data["Nominal Supply Air Flow Rate"] = value

    @property
    def nominal_supply_air_inlet_temperature(self):
        """Get nominal_supply_air_inlet_temperature

        Returns:
            float: the value of `nominal_supply_air_inlet_temperature` or None if not set
        """
        return self._data["Nominal Supply Air Inlet Temperature"]

    @nominal_supply_air_inlet_temperature.setter
    def nominal_supply_air_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Inlet Temperature`

        Args:
            value (float): value for IDD Field `Nominal Supply Air Inlet Temperature`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.nominal_supply_air_inlet_temperature`'.format(value))
        self._data["Nominal Supply Air Inlet Temperature"] = value

    @property
    def nominal_supply_air_outlet_temperature(self):
        """Get nominal_supply_air_outlet_temperature

        Returns:
            float: the value of `nominal_supply_air_outlet_temperature` or None if not set
        """
        return self._data["Nominal Supply Air Outlet Temperature"]

    @nominal_supply_air_outlet_temperature.setter
    def nominal_supply_air_outlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Outlet Temperature`

        Args:
            value (float): value for IDD Field `Nominal Supply Air Outlet Temperature`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.nominal_supply_air_outlet_temperature`'.format(value))
        self._data["Nominal Supply Air Outlet Temperature"] = value

    @property
    def nominal_secondary_air_flow_rate(self):
        """Get nominal_secondary_air_flow_rate

        Returns:
            float: the value of `nominal_secondary_air_flow_rate` or None if not set
        """
        return self._data["Nominal Secondary Air Flow Rate"]

    @nominal_secondary_air_flow_rate.setter
    def nominal_secondary_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Secondary Air Flow Rate`

        Args:
            value (float): value for IDD Field `Nominal Secondary Air Flow Rate`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.nominal_secondary_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerAirToAirFlatPlate.nominal_secondary_air_flow_rate`')
        self._data["Nominal Secondary Air Flow Rate"] = value

    @property
    def nominal_secondary_air_inlet_temperature(self):
        """Get nominal_secondary_air_inlet_temperature

        Returns:
            float: the value of `nominal_secondary_air_inlet_temperature` or None if not set
        """
        return self._data["Nominal Secondary Air Inlet Temperature"]

    @nominal_secondary_air_inlet_temperature.setter
    def nominal_secondary_air_inlet_temperature(self, value=None):
        """  Corresponds to IDD Field `Nominal Secondary Air Inlet Temperature`

        Args:
            value (float): value for IDD Field `Nominal Secondary Air Inlet Temperature`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.nominal_secondary_air_inlet_temperature`'.format(value))
        self._data["Nominal Secondary Air Inlet Temperature"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self._data["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """  Corresponds to IDD Field `Nominal Electric Power`

        Args:
            value (float): value for IDD Field `Nominal Electric Power`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.nominal_electric_power`'.format(value))
        self._data["Nominal Electric Power"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.supply_air_inlet_node_name`')
        self._data["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self._data["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.supply_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.supply_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.supply_air_outlet_node_name`')
        self._data["Supply Air Outlet Node Name"] = value

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
                                 ' for field `HeatExchangerAirToAirFlatPlate.secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.secondary_air_inlet_node_name`')
        self._data["Secondary Air Inlet Node Name"] = value

    @property
    def secondary_air_outlet_node_name(self):
        """Get secondary_air_outlet_node_name

        Returns:
            str: the value of `secondary_air_outlet_node_name` or None if not set
        """
        return self._data["Secondary Air Outlet Node Name"]

    @secondary_air_outlet_node_name.setter
    def secondary_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Secondary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Outlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirFlatPlate.secondary_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirFlatPlate.secondary_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirFlatPlate.secondary_air_outlet_node_name`')
        self._data["Secondary Air Outlet Node Name"] = value

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
                    raise ValueError("Required field HeatExchangerAirToAirFlatPlate:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field HeatExchangerAirToAirFlatPlate:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for HeatExchangerAirToAirFlatPlate: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for HeatExchangerAirToAirFlatPlate: {} / {}".format(out_fields,
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

class HeatExchangerAirToAirSensibleAndLatent(object):
    """ Corresponds to IDD object `HeatExchanger:AirToAir:SensibleAndLatent`
        This object models an air-to-air heat exchanger using effectiveness relationships.
        The heat exchanger can transfer sensible energy, latent energy, or both between the
        supply (primary) and exhaust (secondary) air streams.
    """
    internal_name = "HeatExchanger:AirToAir:SensibleAndLatent"
    field_count = 23
    required_fields = ["Name", "Nominal Supply Air Flow Rate", "Supply Air Inlet Node Name", "Supply Air Outlet Node Name", "Exhaust Air Inlet Node Name", "Exhaust Air Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 19
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatExchanger:AirToAir:SensibleAndLatent`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Nominal Supply Air Flow Rate"] = None
        self._data["Sensible Effectiveness at 100% Heating Air Flow"] = None
        self._data["Latent Effectiveness at 100% Heating Air Flow"] = None
        self._data["Sensible Effectiveness at 75% Heating Air Flow"] = None
        self._data["Latent Effectiveness at 75% Heating Air Flow"] = None
        self._data["Sensible Effectiveness at 100% Cooling Air Flow"] = None
        self._data["Latent Effectiveness at 100% Cooling Air Flow"] = None
        self._data["Sensible Effectiveness at 75% Cooling Air Flow"] = None
        self._data["Latent Effectiveness at 75% Cooling Air Flow"] = None
        self._data["Supply Air Inlet Node Name"] = None
        self._data["Supply Air Outlet Node Name"] = None
        self._data["Exhaust Air Inlet Node Name"] = None
        self._data["Exhaust Air Outlet Node Name"] = None
        self._data["Nominal Electric Power"] = None
        self._data["Supply Air Outlet Temperature Control"] = None
        self._data["Heat Exchanger Type"] = None
        self._data["Frost Control Type"] = None
        self._data["Threshold Temperature"] = None
        self._data["Initial Defrost Time Fraction"] = None
        self._data["Rate of Defrost Time Fraction Increase"] = None
        self._data["Economizer Lockout"] = None
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
            self.nominal_supply_air_flow_rate = None
        else:
            self.nominal_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_100_heating_air_flow = None
        else:
            self.sensible_effectiveness_at_100_heating_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_100_heating_air_flow = None
        else:
            self.latent_effectiveness_at_100_heating_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_75_heating_air_flow = None
        else:
            self.sensible_effectiveness_at_75_heating_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_75_heating_air_flow = None
        else:
            self.latent_effectiveness_at_75_heating_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_100_cooling_air_flow = None
        else:
            self.sensible_effectiveness_at_100_cooling_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_100_cooling_air_flow = None
        else:
            self.latent_effectiveness_at_100_cooling_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensible_effectiveness_at_75_cooling_air_flow = None
        else:
            self.sensible_effectiveness_at_75_cooling_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_effectiveness_at_75_cooling_air_flow = None
        else:
            self.latent_effectiveness_at_75_cooling_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_inlet_node_name = None
        else:
            self.supply_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_outlet_node_name = None
        else:
            self.supply_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_inlet_node_name = None
        else:
            self.exhaust_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_outlet_node_name = None
        else:
            self.exhaust_air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_electric_power = None
        else:
            self.nominal_electric_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_outlet_temperature_control = None
        else:
            self.supply_air_outlet_temperature_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_exchanger_type = None
        else:
            self.heat_exchanger_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frost_control_type = None
        else:
            self.frost_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.threshold_temperature = None
        else:
            self.threshold_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_defrost_time_fraction = None
        else:
            self.initial_defrost_time_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rate_of_defrost_time_fraction_increase = None
        else:
            self.rate_of_defrost_time_fraction_increase = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_lockout = None
        else:
            self.economizer_lockout = vals[i]
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.name`')
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """Get nominal_supply_air_flow_rate

        Returns:
            float: the value of `nominal_supply_air_flow_rate` or None if not set
        """
        return self._data["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Supply Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Nominal Supply Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.nominal_supply_air_flow_rate`'.format(value))
                    self._data["Nominal Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.nominal_supply_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.nominal_supply_air_flow_rate`')
        self._data["Nominal Supply Air Flow Rate"] = value

    @property
    def sensible_effectiveness_at_100_heating_air_flow(self):
        """Get sensible_effectiveness_at_100_heating_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_100_heating_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 100% Heating Air Flow"]

    @sensible_effectiveness_at_100_heating_air_flow.setter
    def sensible_effectiveness_at_100_heating_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Sensible Effectiveness at 100% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 100% Heating Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_100_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_100_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_100_heating_air_flow`')
        self._data["Sensible Effectiveness at 100% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_100_heating_air_flow(self):
        """Get latent_effectiveness_at_100_heating_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_100_heating_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 100% Heating Air Flow"]

    @latent_effectiveness_at_100_heating_air_flow.setter
    def latent_effectiveness_at_100_heating_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Latent Effectiveness at 100% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 100% Heating Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_100_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_100_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_100_heating_air_flow`')
        self._data["Latent Effectiveness at 100% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_heating_air_flow(self):
        """Get sensible_effectiveness_at_75_heating_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_75_heating_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 75% Heating Air Flow"]

    @sensible_effectiveness_at_75_heating_air_flow.setter
    def sensible_effectiveness_at_75_heating_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Sensible Effectiveness at 75% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 75% Heating Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_75_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_75_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_75_heating_air_flow`')
        self._data["Sensible Effectiveness at 75% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_75_heating_air_flow(self):
        """Get latent_effectiveness_at_75_heating_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_75_heating_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 75% Heating Air Flow"]

    @latent_effectiveness_at_75_heating_air_flow.setter
    def latent_effectiveness_at_75_heating_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Latent Effectiveness at 75% Heating Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 75% Heating Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_75_heating_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_75_heating_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_75_heating_air_flow`')
        self._data["Latent Effectiveness at 75% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_100_cooling_air_flow(self):
        """Get sensible_effectiveness_at_100_cooling_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_100_cooling_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 100% Cooling Air Flow"]

    @sensible_effectiveness_at_100_cooling_air_flow.setter
    def sensible_effectiveness_at_100_cooling_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Sensible Effectiveness at 100% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 100% Cooling Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_100_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_100_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_100_cooling_air_flow`')
        self._data["Sensible Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_100_cooling_air_flow(self):
        """Get latent_effectiveness_at_100_cooling_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_100_cooling_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 100% Cooling Air Flow"]

    @latent_effectiveness_at_100_cooling_air_flow.setter
    def latent_effectiveness_at_100_cooling_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Latent Effectiveness at 100% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 100% Cooling Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_100_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_100_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_100_cooling_air_flow`')
        self._data["Latent Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_cooling_air_flow(self):
        """Get sensible_effectiveness_at_75_cooling_air_flow

        Returns:
            float: the value of `sensible_effectiveness_at_75_cooling_air_flow` or None if not set
        """
        return self._data["Sensible Effectiveness at 75% Cooling Air Flow"]

    @sensible_effectiveness_at_75_cooling_air_flow.setter
    def sensible_effectiveness_at_75_cooling_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Sensible Effectiveness at 75% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 75% Cooling Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_75_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_75_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.sensible_effectiveness_at_75_cooling_air_flow`')
        self._data["Sensible Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_75_cooling_air_flow(self):
        """Get latent_effectiveness_at_75_cooling_air_flow

        Returns:
            float: the value of `latent_effectiveness_at_75_cooling_air_flow` or None if not set
        """
        return self._data["Latent Effectiveness at 75% Cooling Air Flow"]

    @latent_effectiveness_at_75_cooling_air_flow.setter
    def latent_effectiveness_at_75_cooling_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Latent Effectiveness at 75% Cooling Air Flow`

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 75% Cooling Air Flow`
                Units: dimensionless
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_75_cooling_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_75_cooling_air_flow`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.latent_effectiveness_at_75_cooling_air_flow`')
        self._data["Latent Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def supply_air_inlet_node_name(self):
        """Get supply_air_inlet_node_name

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_inlet_node_name`')
        self._data["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """Get supply_air_outlet_node_name

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set
        """
        return self._data["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_node_name`')
        self._data["Supply Air Outlet Node Name"] = value

    @property
    def exhaust_air_inlet_node_name(self):
        """Get exhaust_air_inlet_node_name

        Returns:
            str: the value of `exhaust_air_inlet_node_name` or None if not set
        """
        return self._data["Exhaust Air Inlet Node Name"]

    @exhaust_air_inlet_node_name.setter
    def exhaust_air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Inlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.exhaust_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.exhaust_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.exhaust_air_inlet_node_name`')
        self._data["Exhaust Air Inlet Node Name"] = value

    @property
    def exhaust_air_outlet_node_name(self):
        """Get exhaust_air_outlet_node_name

        Returns:
            str: the value of `exhaust_air_outlet_node_name` or None if not set
        """
        return self._data["Exhaust Air Outlet Node Name"]

    @exhaust_air_outlet_node_name.setter
    def exhaust_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Outlet Node Name`
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.exhaust_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.exhaust_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.exhaust_air_outlet_node_name`')
        self._data["Exhaust Air Outlet Node Name"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self._data["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=0.0):
        """  Corresponds to IDD Field `Nominal Electric Power`

        Args:
            value (float): value for IDD Field `Nominal Electric Power`
                Units: W
                IP-Units: W
                Default value: 0.0
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.nominal_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.nominal_electric_power`')
        self._data["Nominal Electric Power"] = value

    @property
    def supply_air_outlet_temperature_control(self):
        """Get supply_air_outlet_temperature_control

        Returns:
            str: the value of `supply_air_outlet_temperature_control` or None if not set
        """
        return self._data["Supply Air Outlet Temperature Control"]

    @supply_air_outlet_temperature_control.setter
    def supply_air_outlet_temperature_control(self, value="No"):
        """  Corresponds to IDD Field `Supply Air Outlet Temperature Control`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Temperature Control`
                Accepted values are:
                      - No
                      - Yes
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_temperature_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_temperature_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_temperature_control`')
            vals = {}
            vals["no"] = "No"
            vals["yes"] = "Yes"
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
                                     'field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_temperature_control`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerAirToAirSensibleAndLatent.supply_air_outlet_temperature_control`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Supply Air Outlet Temperature Control"] = value

    @property
    def heat_exchanger_type(self):
        """Get heat_exchanger_type

        Returns:
            str: the value of `heat_exchanger_type` or None if not set
        """
        return self._data["Heat Exchanger Type"]

    @heat_exchanger_type.setter
    def heat_exchanger_type(self, value="Plate"):
        """  Corresponds to IDD Field `Heat Exchanger Type`

        Args:
            value (str): value for IDD Field `Heat Exchanger Type`
                Accepted values are:
                      - Plate
                      - Rotary
                Default value: Plate
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.heat_exchanger_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.heat_exchanger_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.heat_exchanger_type`')
            vals = {}
            vals["plate"] = "Plate"
            vals["rotary"] = "Rotary"
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
                                     'field `HeatExchangerAirToAirSensibleAndLatent.heat_exchanger_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerAirToAirSensibleAndLatent.heat_exchanger_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heat Exchanger Type"] = value

    @property
    def frost_control_type(self):
        """Get frost_control_type

        Returns:
            str: the value of `frost_control_type` or None if not set
        """
        return self._data["Frost Control Type"]

    @frost_control_type.setter
    def frost_control_type(self, value="None"):
        """  Corresponds to IDD Field `Frost Control Type`

        Args:
            value (str): value for IDD Field `Frost Control Type`
                Accepted values are:
                      - None
                      - ExhaustAirRecirculation
                      - ExhaustOnly
                      - MinimumExhaustTemperature
                Default value: None
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.frost_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.frost_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.frost_control_type`')
            vals = {}
            vals["none"] = "None"
            vals["exhaustairrecirculation"] = "ExhaustAirRecirculation"
            vals["exhaustonly"] = "ExhaustOnly"
            vals["minimumexhausttemperature"] = "MinimumExhaustTemperature"
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
                                     'field `HeatExchangerAirToAirSensibleAndLatent.frost_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerAirToAirSensibleAndLatent.frost_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Frost Control Type"] = value

    @property
    def threshold_temperature(self):
        """Get threshold_temperature

        Returns:
            float: the value of `threshold_temperature` or None if not set
        """
        return self._data["Threshold Temperature"]

    @threshold_temperature.setter
    def threshold_temperature(self, value=1.7):
        """  Corresponds to IDD Field `Threshold Temperature`
        Supply (outdoor) air inlet temp threshold for exhaust air recirculation and
        exhaust only frost control types. Exhaust air outlet threshold Temperature for
        minimum exhaust temperature frost control type.

        Args:
            value (float): value for IDD Field `Threshold Temperature`
                Units: C
                Default value: 1.7
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.threshold_temperature`'.format(value))
        self._data["Threshold Temperature"] = value

    @property
    def initial_defrost_time_fraction(self):
        """Get initial_defrost_time_fraction

        Returns:
            float: the value of `initial_defrost_time_fraction` or None if not set
        """
        return self._data["Initial Defrost Time Fraction"]

    @initial_defrost_time_fraction.setter
    def initial_defrost_time_fraction(self, value=0.083):
        """  Corresponds to IDD Field `Initial Defrost Time Fraction`
        Fraction of the time when frost control will be invoked at the threshold temperature.
        This field only used for exhaust air recirc and exhaust-only frost control types.

        Args:
            value (float): value for IDD Field `Initial Defrost Time Fraction`
                Units: dimensionless
                Default value: 0.083
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.initial_defrost_time_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.initial_defrost_time_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.initial_defrost_time_fraction`')
        self._data["Initial Defrost Time Fraction"] = value

    @property
    def rate_of_defrost_time_fraction_increase(self):
        """Get rate_of_defrost_time_fraction_increase

        Returns:
            float: the value of `rate_of_defrost_time_fraction_increase` or None if not set
        """
        return self._data["Rate of Defrost Time Fraction Increase"]

    @rate_of_defrost_time_fraction_increase.setter
    def rate_of_defrost_time_fraction_increase(self, value=0.012):
        """  Corresponds to IDD Field `Rate of Defrost Time Fraction Increase`
        Rate of increase in defrost time fraction as actual temp falls below threshold temperature.
        This field only used for exhaust air recirc and exhaust-only frost control types.

        Args:
            value (float): value for IDD Field `Rate of Defrost Time Fraction Increase`
                Units: 1/K
                Default value: 0.012
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.rate_of_defrost_time_fraction_increase`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.rate_of_defrost_time_fraction_increase`')
        self._data["Rate of Defrost Time Fraction Increase"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self._data["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """  Corresponds to IDD Field `Economizer Lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `Economizer Lockout`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 ' for field `HeatExchangerAirToAirSensibleAndLatent.economizer_lockout`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.economizer_lockout`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerAirToAirSensibleAndLatent.economizer_lockout`')
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
                                     'field `HeatExchangerAirToAirSensibleAndLatent.economizer_lockout`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerAirToAirSensibleAndLatent.economizer_lockout`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Economizer Lockout"] = value

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
                    raise ValueError("Required field HeatExchangerAirToAirSensibleAndLatent:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field HeatExchangerAirToAirSensibleAndLatent:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for HeatExchangerAirToAirSensibleAndLatent: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for HeatExchangerAirToAirSensibleAndLatent: {} / {}".format(out_fields,
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

class HeatExchangerDesiccantBalancedFlow(object):
    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow`
        This object models a balanced desiccant heat exchanger.
        The heat exchanger transfers both sensible and latent energy between the
        process and regeneration air streams. The air flow rate and face velocity
        are assumed to be the same on both the process and regeneration sides of the
        heat exchanger.
    """
    internal_name = "HeatExchanger:Desiccant:BalancedFlow"
    field_count = 9
    required_fields = ["Name", "Regeneration Air Inlet Node Name", "Regeneration Air Outlet Node Name", "Process Air Inlet Node Name", "Process Air Outlet Node Name", "Heat Exchanger Performance Name"]
    extensible_fields = 0
    format = None
    min_fields = 8
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatExchanger:Desiccant:BalancedFlow`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Regeneration Air Inlet Node Name"] = None
        self._data["Regeneration Air Outlet Node Name"] = None
        self._data["Process Air Inlet Node Name"] = None
        self._data["Process Air Outlet Node Name"] = None
        self._data["Heat Exchanger Performance Object Type"] = None
        self._data["Heat Exchanger Performance Name"] = None
        self._data["Economizer Lockout"] = None
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
            self.regeneration_air_inlet_node_name = None
        else:
            self.regeneration_air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.regeneration_air_outlet_node_name = None
        else:
            self.regeneration_air_outlet_node_name = vals[i]
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
            self.heat_exchanger_performance_object_type = None
        else:
            self.heat_exchanger_performance_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_exchanger_performance_name = None
        else:
            self.heat_exchanger_performance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.economizer_lockout = None
        else:
            self.economizer_lockout = vals[i]
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.name`')
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.regeneration_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.regeneration_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.regeneration_air_inlet_node_name`')
        self._data["Regeneration Air Inlet Node Name"] = value

    @property
    def regeneration_air_outlet_node_name(self):
        """Get regeneration_air_outlet_node_name

        Returns:
            str: the value of `regeneration_air_outlet_node_name` or None if not set
        """
        return self._data["Regeneration Air Outlet Node Name"]

    @regeneration_air_outlet_node_name.setter
    def regeneration_air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Regeneration Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Outlet Node Name`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.regeneration_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.regeneration_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.regeneration_air_outlet_node_name`')
        self._data["Regeneration Air Outlet Node Name"] = value

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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.process_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.process_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.process_air_inlet_node_name`')
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.process_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.process_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.process_air_outlet_node_name`')
        self._data["Process Air Outlet Node Name"] = value

    @property
    def heat_exchanger_performance_object_type(self):
        """Get heat_exchanger_performance_object_type

        Returns:
            str: the value of `heat_exchanger_performance_object_type` or None if not set
        """
        return self._data["Heat Exchanger Performance Object Type"]

    @heat_exchanger_performance_object_type.setter
    def heat_exchanger_performance_object_type(self, value="HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"):
        """  Corresponds to IDD Field `Heat Exchanger Performance Object Type`

        Args:
            value (str): value for IDD Field `Heat Exchanger Performance Object Type`
                Accepted values are:
                      - HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1
                Default value: HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_object_type`')
            vals = {}
            vals["heatexchanger:desiccant:balancedflow:performancedatatype1"] = "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"
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
                                     'field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heat Exchanger Performance Object Type"] = value

    @property
    def heat_exchanger_performance_name(self):
        """Get heat_exchanger_performance_name

        Returns:
            str: the value of `heat_exchanger_performance_name` or None if not set
        """
        return self._data["Heat Exchanger Performance Name"]

    @heat_exchanger_performance_name.setter
    def heat_exchanger_performance_name(self, value=None):
        """  Corresponds to IDD Field `Heat Exchanger Performance Name`

        Args:
            value (str): value for IDD Field `Heat Exchanger Performance Name`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.heat_exchanger_performance_name`')
        self._data["Heat Exchanger Performance Name"] = value

    @property
    def economizer_lockout(self):
        """Get economizer_lockout

        Returns:
            str: the value of `economizer_lockout` or None if not set
        """
        return self._data["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="No"):
        """  Corresponds to IDD Field `Economizer Lockout`
        Yes means that the heat exchanger will be locked out (off)
        when the economizer is operating or high humidity control is active

        Args:
            value (str): value for IDD Field `Economizer Lockout`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlow.economizer_lockout`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlow.economizer_lockout`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlow.economizer_lockout`')
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
                                     'field `HeatExchangerDesiccantBalancedFlow.economizer_lockout`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatExchangerDesiccantBalancedFlow.economizer_lockout`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Economizer Lockout"] = value

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
                    raise ValueError("Required field HeatExchangerDesiccantBalancedFlow:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field HeatExchangerDesiccantBalancedFlow:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for HeatExchangerDesiccantBalancedFlow: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for HeatExchangerDesiccantBalancedFlow: {} / {}".format(out_fields,
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

class HeatExchangerDesiccantBalancedFlowPerformanceDataType1(object):
    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1`
        RTO = B1 + B2*RWI + B3*RTI + B4*(RWI/RTI) + B5*PWI + B6*PTI + B7*(PWI/PTI)
        + B8*RFV
        RWO = C1 + C2*RWI + C3*RTI + C4*(RWI/RTI) + C5*PWI + C6*PTI + C7*(PWI/PTI)
        + C8*RFV
        where,
        RTO = Dry-bulb temperature of the regeneration outlet air (C)
        RWO = Humidity ratio of the regeneration outlet air (kgWater/kgDryAir)
        RWI = Humidity ratio of the regeneration inlet air (kgWater/kgDryAir)
        RTI = Dry-bulb temperature of the regeneration inlet air (C)
        PWI = Humidity ratio of the process inlet air (kgWater/kgDryAir)
        PTI = Dry-bulb temperature of the process inlet air (C)
        RFV = Regeneration Face Velocity (m/s)
    """
    internal_name = "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"
    field_count = 52
    required_fields = ["Name", "Nominal Air Face Velocity", "Temperature Equation Coefficient 1", "Temperature Equation Coefficient 2", "Temperature Equation Coefficient 3", "Temperature Equation Coefficient 4", "Temperature Equation Coefficient 5", "Temperature Equation Coefficient 6", "Temperature Equation Coefficient 7", "Temperature Equation Coefficient 8", "Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation", "Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation", "Minimum Regeneration Inlet Air Temperature for Temperature Equation", "Maximum Regeneration Inlet Air Temperature for Temperature Equation", "Minimum Process Inlet Air Humidity Ratio for Temperature Equation", "Maximum Process Inlet Air Humidity Ratio for Temperature Equation", "Minimum Process Inlet Air Temperature for Temperature Equation", "Maximum Process Inlet Air Temperature for Temperature Equation", "Minimum Regeneration Air Velocity for Temperature Equation", "Maximum Regeneration Air Velocity for Temperature Equation", "Minimum Regeneration Outlet Air Temperature for Temperature Equation", "Maximum Regeneration Outlet Air Temperature for Temperature Equation", "Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation", "Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation", "Minimum Process Inlet Air Relative Humidity for Temperature Equation", "Maximum Process Inlet Air Relative Humidity for Temperature Equation", "Humidity Ratio Equation Coefficient 1", "Humidity Ratio Equation Coefficient 2", "Humidity Ratio Equation Coefficient 3", "Humidity Ratio Equation Coefficient 4", "Humidity Ratio Equation Coefficient 5", "Humidity Ratio Equation Coefficient 6", "Humidity Ratio Equation Coefficient 7", "Humidity Ratio Equation Coefficient 8", "Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation", "Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation", "Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation", "Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation", "Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation", "Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation", "Minimum Process Inlet Air Temperature for Humidity Ratio Equation", "Maximum Process Inlet Air Temperature for Humidity Ratio Equation", "Minimum Regeneration Air Velocity for Humidity Ratio Equation", "Maximum Regeneration Air Velocity for Humidity Ratio Equation", "Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation", "Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation", "Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation", "Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation", "Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation", "Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]
    extensible_fields = 0
    format = None
    min_fields = 52
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Nominal Air Flow Rate"] = None
        self._data["Nominal Air Face Velocity"] = None
        self._data["Nominal Electric Power"] = None
        self._data["Temperature Equation Coefficient 1"] = None
        self._data["Temperature Equation Coefficient 2"] = None
        self._data["Temperature Equation Coefficient 3"] = None
        self._data["Temperature Equation Coefficient 4"] = None
        self._data["Temperature Equation Coefficient 5"] = None
        self._data["Temperature Equation Coefficient 6"] = None
        self._data["Temperature Equation Coefficient 7"] = None
        self._data["Temperature Equation Coefficient 8"] = None
        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Minimum Regeneration Inlet Air Temperature for Temperature Equation"] = None
        self._data["Maximum Regeneration Inlet Air Temperature for Temperature Equation"] = None
        self._data["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"] = None
        self._data["Minimum Process Inlet Air Temperature for Temperature Equation"] = None
        self._data["Maximum Process Inlet Air Temperature for Temperature Equation"] = None
        self._data["Minimum Regeneration Air Velocity for Temperature Equation"] = None
        self._data["Maximum Regeneration Air Velocity for Temperature Equation"] = None
        self._data["Minimum Regeneration Outlet Air Temperature for Temperature Equation"] = None
        self._data["Maximum Regeneration Outlet Air Temperature for Temperature Equation"] = None
        self._data["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Minimum Process Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Maximum Process Inlet Air Relative Humidity for Temperature Equation"] = None
        self._data["Humidity Ratio Equation Coefficient 1"] = None
        self._data["Humidity Ratio Equation Coefficient 2"] = None
        self._data["Humidity Ratio Equation Coefficient 3"] = None
        self._data["Humidity Ratio Equation Coefficient 4"] = None
        self._data["Humidity Ratio Equation Coefficient 5"] = None
        self._data["Humidity Ratio Equation Coefficient 6"] = None
        self._data["Humidity Ratio Equation Coefficient 7"] = None
        self._data["Humidity Ratio Equation Coefficient 8"] = None
        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Air Velocity for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Air Velocity for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = None
        self._data["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
        self._data["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
        self._data["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
        self._data["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = None
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
            self.nominal_air_flow_rate = None
        else:
            self.nominal_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_air_face_velocity = None
        else:
            self.nominal_air_face_velocity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_electric_power = None
        else:
            self.nominal_electric_power = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_1 = None
        else:
            self.temperature_equation_coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_2 = None
        else:
            self.temperature_equation_coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_3 = None
        else:
            self.temperature_equation_coefficient_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_4 = None
        else:
            self.temperature_equation_coefficient_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_5 = None
        else:
            self.temperature_equation_coefficient_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_6 = None
        else:
            self.temperature_equation_coefficient_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_7 = None
        else:
            self.temperature_equation_coefficient_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_equation_coefficient_8 = None
        else:
            self.temperature_equation_coefficient_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_temperature_for_temperature_equation = None
        else:
            self.minimum_regeneration_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_temperature_for_temperature_equation = None
        else:
            self.maximum_regeneration_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.minimum_process_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_humidity_ratio_for_temperature_equation = None
        else:
            self.maximum_process_inlet_air_humidity_ratio_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_temperature_for_temperature_equation = None
        else:
            self.minimum_process_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_temperature_for_temperature_equation = None
        else:
            self.maximum_process_inlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_air_velocity_for_temperature_equation = None
        else:
            self.minimum_regeneration_air_velocity_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_air_velocity_for_temperature_equation = None
        else:
            self.maximum_regeneration_air_velocity_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_outlet_air_temperature_for_temperature_equation = None
        else:
            self.minimum_regeneration_outlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_outlet_air_temperature_for_temperature_equation = None
        else:
            self.maximum_regeneration_outlet_air_temperature_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.minimum_process_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_relative_humidity_for_temperature_equation = None
        else:
            self.maximum_process_inlet_air_relative_humidity_for_temperature_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_1 = None
        else:
            self.humidity_ratio_equation_coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_2 = None
        else:
            self.humidity_ratio_equation_coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_3 = None
        else:
            self.humidity_ratio_equation_coefficient_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_4 = None
        else:
            self.humidity_ratio_equation_coefficient_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_5 = None
        else:
            self.humidity_ratio_equation_coefficient_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_6 = None
        else:
            self.humidity_ratio_equation_coefficient_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_7 = None
        else:
            self.humidity_ratio_equation_coefficient_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_ratio_equation_coefficient_8 = None
        else:
            self.humidity_ratio_equation_coefficient_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.minimum_process_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_temperature_for_humidity_ratio_equation = None
        else:
            self.maximum_process_inlet_air_temperature_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_air_velocity_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_air_velocity_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_air_velocity_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_air_velocity_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = None
        else:
            self.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation = vals[i]
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.name`')
        self._data["Name"] = value

    @property
    def nominal_air_flow_rate(self):
        """Get nominal_air_flow_rate

        Returns:
            float: the value of `nominal_air_flow_rate` or None if not set
        """
        return self._data["Nominal Air Flow Rate"]

    @nominal_air_flow_rate.setter
    def nominal_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Nominal Air Flow Rate`
        Air flow rate at nominal conditions (assumed to be the same for both sides
        of the heat exchanger).

        Args:
            value (float): value for IDD Field `Nominal Air Flow Rate`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_air_flow_rate`')
        self._data["Nominal Air Flow Rate"] = value

    @property
    def nominal_air_face_velocity(self):
        """Get nominal_air_face_velocity

        Returns:
            float: the value of `nominal_air_face_velocity` or None if not set
        """
        return self._data["Nominal Air Face Velocity"]

    @nominal_air_face_velocity.setter
    def nominal_air_face_velocity(self, value=None):
        """  Corresponds to IDD Field `Nominal Air Face Velocity`

        Args:
            value (float): value for IDD Field `Nominal Air Face Velocity`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_air_face_velocity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_air_face_velocity`')
            if value > 6.0:
                raise ValueError('value need to be smaller 6.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_air_face_velocity`')
        self._data["Nominal Air Face Velocity"] = value

    @property
    def nominal_electric_power(self):
        """Get nominal_electric_power

        Returns:
            float: the value of `nominal_electric_power` or None if not set
        """
        return self._data["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=0.0):
        """  Corresponds to IDD Field `Nominal Electric Power`
        Parasitic electric power (e.g., desiccant wheel motor)

        Args:
            value (float): value for IDD Field `Nominal Electric Power`
                Units: W
                IP-Units: W
                Default value: 0.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_electric_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.nominal_electric_power`')
        self._data["Nominal Electric Power"] = value

    @property
    def temperature_equation_coefficient_1(self):
        """Get temperature_equation_coefficient_1

        Returns:
            float: the value of `temperature_equation_coefficient_1` or None if not set
        """
        return self._data["Temperature Equation Coefficient 1"]

    @temperature_equation_coefficient_1.setter
    def temperature_equation_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 1`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 1`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_1`'.format(value))
        self._data["Temperature Equation Coefficient 1"] = value

    @property
    def temperature_equation_coefficient_2(self):
        """Get temperature_equation_coefficient_2

        Returns:
            float: the value of `temperature_equation_coefficient_2` or None if not set
        """
        return self._data["Temperature Equation Coefficient 2"]

    @temperature_equation_coefficient_2.setter
    def temperature_equation_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 2`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 2`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_2`'.format(value))
        self._data["Temperature Equation Coefficient 2"] = value

    @property
    def temperature_equation_coefficient_3(self):
        """Get temperature_equation_coefficient_3

        Returns:
            float: the value of `temperature_equation_coefficient_3` or None if not set
        """
        return self._data["Temperature Equation Coefficient 3"]

    @temperature_equation_coefficient_3.setter
    def temperature_equation_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 3`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 3`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_3`'.format(value))
        self._data["Temperature Equation Coefficient 3"] = value

    @property
    def temperature_equation_coefficient_4(self):
        """Get temperature_equation_coefficient_4

        Returns:
            float: the value of `temperature_equation_coefficient_4` or None if not set
        """
        return self._data["Temperature Equation Coefficient 4"]

    @temperature_equation_coefficient_4.setter
    def temperature_equation_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 4`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 4`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_4`'.format(value))
        self._data["Temperature Equation Coefficient 4"] = value

    @property
    def temperature_equation_coefficient_5(self):
        """Get temperature_equation_coefficient_5

        Returns:
            float: the value of `temperature_equation_coefficient_5` or None if not set
        """
        return self._data["Temperature Equation Coefficient 5"]

    @temperature_equation_coefficient_5.setter
    def temperature_equation_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 5`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 5`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_5`'.format(value))
        self._data["Temperature Equation Coefficient 5"] = value

    @property
    def temperature_equation_coefficient_6(self):
        """Get temperature_equation_coefficient_6

        Returns:
            float: the value of `temperature_equation_coefficient_6` or None if not set
        """
        return self._data["Temperature Equation Coefficient 6"]

    @temperature_equation_coefficient_6.setter
    def temperature_equation_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 6`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 6`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_6`'.format(value))
        self._data["Temperature Equation Coefficient 6"] = value

    @property
    def temperature_equation_coefficient_7(self):
        """Get temperature_equation_coefficient_7

        Returns:
            float: the value of `temperature_equation_coefficient_7` or None if not set
        """
        return self._data["Temperature Equation Coefficient 7"]

    @temperature_equation_coefficient_7.setter
    def temperature_equation_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 7`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 7`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_7`'.format(value))
        self._data["Temperature Equation Coefficient 7"] = value

    @property
    def temperature_equation_coefficient_8(self):
        """Get temperature_equation_coefficient_8

        Returns:
            float: the value of `temperature_equation_coefficient_8` or None if not set
        """
        return self._data["Temperature Equation Coefficient 8"]

    @temperature_equation_coefficient_8.setter
    def temperature_equation_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `Temperature Equation Coefficient 8`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 8`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.temperature_equation_coefficient_8`'.format(value))
        self._data["Temperature Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')
        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation`')
        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Temperature for Temperature Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_temperature_for_temperature_equation`'.format(value))
        self._data["Minimum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Temperature for Temperature Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_temperature_for_temperature_equation`'.format(value))
        self._data["Maximum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get minimum_process_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_humidity_ratio_for_temperature_equation`')
        self._data["Minimum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(self):
        """Get maximum_process_inlet_air_humidity_ratio_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Humidity Ratio for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Humidity Ratio for Temperature Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_humidity_ratio_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_humidity_ratio_for_temperature_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_humidity_ratio_for_temperature_equation`')
        self._data["Maximum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_temperature_equation(self):
        """Get minimum_process_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Temperature for Temperature Equation"]

    @minimum_process_inlet_air_temperature_for_temperature_equation.setter
    def minimum_process_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Temperature for Temperature Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_temperature_for_temperature_equation`'.format(value))
        self._data["Minimum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_temperature_equation(self):
        """Get maximum_process_inlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Temperature for Temperature Equation"]

    @maximum_process_inlet_air_temperature_for_temperature_equation.setter
    def maximum_process_inlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Temperature for Temperature Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_temperature_for_temperature_equation`'.format(value))
        self._data["Maximum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_temperature_equation(self):
        """Get minimum_regeneration_air_velocity_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Air Velocity for Temperature Equation"]

    @minimum_regeneration_air_velocity_for_temperature_equation.setter
    def minimum_regeneration_air_velocity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Air Velocity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Air Velocity for Temperature Equation`
                Units: m/s
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_air_velocity_for_temperature_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_air_velocity_for_temperature_equation`')
        self._data["Minimum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_temperature_equation(self):
        """Get maximum_regeneration_air_velocity_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Air Velocity for Temperature Equation"]

    @maximum_regeneration_air_velocity_for_temperature_equation.setter
    def maximum_regeneration_air_velocity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Air Velocity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Air Velocity for Temperature Equation`
                Units: m/s
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_air_velocity_for_temperature_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_air_velocity_for_temperature_equation`')
        self._data["Maximum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(self):
        """Get minimum_regeneration_outlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Outlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Outlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Outlet Air Temperature for Temperature Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_outlet_air_temperature_for_temperature_equation`'.format(value))
        self._data["Minimum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(self):
        """Get maximum_regeneration_outlet_air_temperature_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Outlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Outlet Air Temperature for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Outlet Air Temperature for Temperature Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_outlet_air_temperature_for_temperature_equation`'.format(value))
        self._data["Maximum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')
        self._data["Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation`')
        self._data["Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get minimum_process_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_relative_humidity_for_temperature_equation`')
        self._data["Minimum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(self):
        """Get maximum_process_inlet_air_relative_humidity_for_temperature_equation

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Relative Humidity for Temperature Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Relative Humidity for Temperature Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_relative_humidity_for_temperature_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_relative_humidity_for_temperature_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_relative_humidity_for_temperature_equation`')
        self._data["Maximum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def humidity_ratio_equation_coefficient_1(self):
        """Get humidity_ratio_equation_coefficient_1

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_1` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 1"]

    @humidity_ratio_equation_coefficient_1.setter
    def humidity_ratio_equation_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 1`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 1`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_1`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 1"] = value

    @property
    def humidity_ratio_equation_coefficient_2(self):
        """Get humidity_ratio_equation_coefficient_2

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_2` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 2"]

    @humidity_ratio_equation_coefficient_2.setter
    def humidity_ratio_equation_coefficient_2(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 2`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 2`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_2`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 2"] = value

    @property
    def humidity_ratio_equation_coefficient_3(self):
        """Get humidity_ratio_equation_coefficient_3

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_3` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 3"]

    @humidity_ratio_equation_coefficient_3.setter
    def humidity_ratio_equation_coefficient_3(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 3`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 3`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_3`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 3"] = value

    @property
    def humidity_ratio_equation_coefficient_4(self):
        """Get humidity_ratio_equation_coefficient_4

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_4` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 4"]

    @humidity_ratio_equation_coefficient_4.setter
    def humidity_ratio_equation_coefficient_4(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 4`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 4`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_4`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 4"] = value

    @property
    def humidity_ratio_equation_coefficient_5(self):
        """Get humidity_ratio_equation_coefficient_5

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_5` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 5"]

    @humidity_ratio_equation_coefficient_5.setter
    def humidity_ratio_equation_coefficient_5(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 5`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 5`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_5`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 5"] = value

    @property
    def humidity_ratio_equation_coefficient_6(self):
        """Get humidity_ratio_equation_coefficient_6

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_6` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 6"]

    @humidity_ratio_equation_coefficient_6.setter
    def humidity_ratio_equation_coefficient_6(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 6`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 6`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_6`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 6"] = value

    @property
    def humidity_ratio_equation_coefficient_7(self):
        """Get humidity_ratio_equation_coefficient_7

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_7` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 7"]

    @humidity_ratio_equation_coefficient_7.setter
    def humidity_ratio_equation_coefficient_7(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 7`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 7`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_7`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 7"] = value

    @property
    def humidity_ratio_equation_coefficient_8(self):
        """Get humidity_ratio_equation_coefficient_8

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_8` or None if not set
        """
        return self._data["Humidity Ratio Equation Coefficient 8"]

    @humidity_ratio_equation_coefficient_8.setter
    def humidity_ratio_equation_coefficient_8(self, value=None):
        """  Corresponds to IDD Field `Humidity Ratio Equation Coefficient 8`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 8`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.humidity_ratio_equation_coefficient_8`'.format(value))
        self._data["Humidity Ratio Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
        self._data["Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
        self._data["Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))
        self._data["Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))
        self._data["Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
        self._data["Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation`')
        self._data["Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Temperature for Humidity Ratio Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))
        self._data["Minimum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_temperature_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Temperature for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Temperature for Humidity Ratio Equation`
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_temperature_for_humidity_ratio_equation`'.format(value))
        self._data["Maximum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_air_velocity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Air Velocity for Humidity Ratio Equation"]

    @minimum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Air Velocity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Air Velocity for Humidity Ratio Equation`
                Units: m/s
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_air_velocity_for_humidity_ratio_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_air_velocity_for_humidity_ratio_equation`')
        self._data["Minimum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_air_velocity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Air Velocity for Humidity Ratio Equation"]

    @maximum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Air Velocity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Air Velocity for Humidity Ratio Equation`
                Units: m/s
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_air_velocity_for_humidity_ratio_equation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_air_velocity_for_humidity_ratio_equation`')
        self._data["Maximum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')
        self._data["Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`
                Units: kgWater/kgDryAir
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation`')
        self._data["Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')
        self._data["Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation`')
        self._data["Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')
        self._data["Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self):
        """Get maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set
        """
        return self._data["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(self, value=None):
        """  Corresponds to IDD Field `Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation`

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation`
                Units: percent
                value >= 0.0
                value <= 100.0
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
                                 ' for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `HeatExchangerDesiccantBalancedFlowPerformanceDataType1.maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation`')
        self._data["Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

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
                    raise ValueError("Required field HeatExchangerDesiccantBalancedFlowPerformanceDataType1:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field HeatExchangerDesiccantBalancedFlowPerformanceDataType1:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for HeatExchangerDesiccantBalancedFlowPerformanceDataType1: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for HeatExchangerDesiccantBalancedFlowPerformanceDataType1: {} / {}".format(out_fields,
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