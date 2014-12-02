from collections import OrderedDict
import logging
import re

class WaterUseEquipment(object):
    """ Corresponds to IDD object `WaterUse:Equipment`
        A generalized object for simulating all water end uses. Hot and cold water uses are
        included, as well as controlled mixing of hot and cold water at the tap. The
        WaterUse:Equipment object can be used stand-alone, or coupled into a plant loop using
        the WaterUse:Connections object (see below). The WaterUse:Connections object allows
        water uses to be linked to WaterUse:Storage objects to store and draw reclaimed water.
        The object can also simulate drainwater heat recovery.
    """
    internal_name = "WaterUse:Equipment"
    field_count = 10
    required_fields = ["Name", "Peak Flow Rate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterUse:Equipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["End-Use Subcategory"] = None
        self._data["Peak Flow Rate"] = None
        self._data["Flow Rate Fraction Schedule Name"] = None
        self._data["Target Temperature Schedule Name"] = None
        self._data["Hot Water Supply Temperature Schedule Name"] = None
        self._data["Cold Water Supply Temperature Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Sensible Fraction Schedule Name"] = None
        self._data["Latent Fraction Schedule Name"] = None
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
            self.enduse_subcategory = None
        else:
            self.enduse_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.peak_flow_rate = None
        else:
            self.peak_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_rate_fraction_schedule_name = None
        else:
            self.flow_rate_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.target_temperature_schedule_name = None
        else:
            self.target_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_supply_temperature_schedule_name = None
        else:
            self.hot_water_supply_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_water_supply_temperature_schedule_name = None
        else:
            self.cold_water_supply_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sensible_fraction_schedule_name = None
        else:
            self.sensible_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.latent_fraction_schedule_name = None
        else:
            self.latent_fraction_schedule_name = vals[i]
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
    def enduse_subcategory(self):
        """Get enduse_subcategory

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self._data["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD Field `End-Use Subcategory`

        Args:
            value (str): value for IDD Field `End-Use Subcategory`
                Default value: General
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
                                 'for field `enduse_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `enduse_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `enduse_subcategory`')
        self._data["End-Use Subcategory"] = value

    @property
    def peak_flow_rate(self):
        """Get peak_flow_rate

        Returns:
            float: the value of `peak_flow_rate` or None if not set
        """
        return self._data["Peak Flow Rate"]

    @peak_flow_rate.setter
    def peak_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Peak Flow Rate`

        Args:
            value (float): value for IDD Field `Peak Flow Rate`
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
                                 'for field `peak_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `peak_flow_rate`')
        self._data["Peak Flow Rate"] = value

    @property
    def flow_rate_fraction_schedule_name(self):
        """Get flow_rate_fraction_schedule_name

        Returns:
            str: the value of `flow_rate_fraction_schedule_name` or None if not set
        """
        return self._data["Flow Rate Fraction Schedule Name"]

    @flow_rate_fraction_schedule_name.setter
    def flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Flow Rate Fraction Schedule Name`
        Defaults to 1.0 at all times

        Args:
            value (str): value for IDD Field `Flow Rate Fraction Schedule Name`
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
                                 'for field `flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_rate_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `flow_rate_fraction_schedule_name`')
        self._data["Flow Rate Fraction Schedule Name"] = value

    @property
    def target_temperature_schedule_name(self):
        """Get target_temperature_schedule_name

        Returns:
            str: the value of `target_temperature_schedule_name` or None if not set
        """
        return self._data["Target Temperature Schedule Name"]

    @target_temperature_schedule_name.setter
    def target_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Target Temperature Schedule Name`
        Defaults to hot water supply temperature

        Args:
            value (str): value for IDD Field `Target Temperature Schedule Name`
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
                                 'for field `target_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `target_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `target_temperature_schedule_name`')
        self._data["Target Temperature Schedule Name"] = value

    @property
    def hot_water_supply_temperature_schedule_name(self):
        """Get hot_water_supply_temperature_schedule_name

        Returns:
            str: the value of `hot_water_supply_temperature_schedule_name` or None if not set
        """
        return self._data["Hot Water Supply Temperature Schedule Name"]

    @hot_water_supply_temperature_schedule_name.setter
    def hot_water_supply_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water Supply Temperature Schedule Name`
        Defaults to cold water supply temperature

        Args:
            value (str): value for IDD Field `Hot Water Supply Temperature Schedule Name`
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
                                 'for field `hot_water_supply_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_supply_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_supply_temperature_schedule_name`')
        self._data["Hot Water Supply Temperature Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """Get cold_water_supply_temperature_schedule_name

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set
        """
        return self._data["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cold Water Supply Temperature Schedule Name`
        Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `Cold Water Supply Temperature Schedule Name`
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
                                 'for field `cold_water_supply_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_water_supply_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_water_supply_temperature_schedule_name`')
        self._data["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def sensible_fraction_schedule_name(self):
        """Get sensible_fraction_schedule_name

        Returns:
            str: the value of `sensible_fraction_schedule_name` or None if not set
        """
        return self._data["Sensible Fraction Schedule Name"]

    @sensible_fraction_schedule_name.setter
    def sensible_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Sensible Fraction Schedule Name`
        Defaults to 0.0 at all times

        Args:
            value (str): value for IDD Field `Sensible Fraction Schedule Name`
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
                                 'for field `sensible_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sensible_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `sensible_fraction_schedule_name`')
        self._data["Sensible Fraction Schedule Name"] = value

    @property
    def latent_fraction_schedule_name(self):
        """Get latent_fraction_schedule_name

        Returns:
            str: the value of `latent_fraction_schedule_name` or None if not set
        """
        return self._data["Latent Fraction Schedule Name"]

    @latent_fraction_schedule_name.setter
    def latent_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Latent Fraction Schedule Name`
        Defaults to 0.0 at all times

        Args:
            value (str): value for IDD Field `Latent Fraction Schedule Name`
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
                                 'for field `latent_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `latent_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `latent_fraction_schedule_name`')
        self._data["Latent Fraction Schedule Name"] = value

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

class WaterUseConnections(object):
    """ Corresponds to IDD object `WaterUse:Connections`
        A subsystem that groups together multiple WaterUse:Equipment components.
        As its name suggests, the object provides connections that are shared by these
        components, including: 1. Inlet node and outlet node connections to a plant loop
        2. Connections to WaterUse:Storage objects to store and draw reclaimed water
        3. Internal connections to simulate drainwater heat recovery.
    """
    internal_name = "WaterUse:Connections"
    field_count = 20
    required_fields = ["Name", "Water Use Equipment 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterUse:Connections`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Reclamation Water Storage Tank Name"] = None
        self._data["Hot Water Supply Temperature Schedule Name"] = None
        self._data["Cold Water Supply Temperature Schedule Name"] = None
        self._data["Drain Water Heat Exchanger Type"] = None
        self._data["Drain Water Heat Exchanger Destination"] = None
        self._data["Drain Water Heat Exchanger U-Factor Times Area"] = None
        self._data["Water Use Equipment 1 Name"] = None
        self._data["Water Use Equipment 2 Name"] = None
        self._data["Water Use Equipment 3 Name"] = None
        self._data["Water Use Equipment 4 Name"] = None
        self._data["Water Use Equipment 5 Name"] = None
        self._data["Water Use Equipment 6 Name"] = None
        self._data["Water Use Equipment 7 Name"] = None
        self._data["Water Use Equipment 8 Name"] = None
        self._data["Water Use Equipment 9 Name"] = None
        self._data["Water Use Equipment 10 Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reclamation_water_storage_tank_name = None
        else:
            self.reclamation_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_supply_temperature_schedule_name = None
        else:
            self.hot_water_supply_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_water_supply_temperature_schedule_name = None
        else:
            self.cold_water_supply_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drain_water_heat_exchanger_type = None
        else:
            self.drain_water_heat_exchanger_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drain_water_heat_exchanger_destination = None
        else:
            self.drain_water_heat_exchanger_destination = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drain_water_heat_exchanger_ufactor_times_area = None
        else:
            self.drain_water_heat_exchanger_ufactor_times_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_1_name = None
        else:
            self.water_use_equipment_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_2_name = None
        else:
            self.water_use_equipment_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_3_name = None
        else:
            self.water_use_equipment_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_4_name = None
        else:
            self.water_use_equipment_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_5_name = None
        else:
            self.water_use_equipment_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_6_name = None
        else:
            self.water_use_equipment_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_7_name = None
        else:
            self.water_use_equipment_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_8_name = None
        else:
            self.water_use_equipment_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_9_name = None
        else:
            self.water_use_equipment_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_use_equipment_10_name = None
        else:
            self.water_use_equipment_10_name = vals[i]
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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inlet_node_name`')
        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Supply Water Storage Tank Name`
        If blank, or tank is empty, defaults to fresh water from the mains

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`
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
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')
        self._data["Supply Water Storage Tank Name"] = value

    @property
    def reclamation_water_storage_tank_name(self):
        """Get reclamation_water_storage_tank_name

        Returns:
            str: the value of `reclamation_water_storage_tank_name` or None if not set
        """
        return self._data["Reclamation Water Storage Tank Name"]

    @reclamation_water_storage_tank_name.setter
    def reclamation_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Reclamation Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Reclamation Water Storage Tank Name`
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
                                 'for field `reclamation_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reclamation_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reclamation_water_storage_tank_name`')
        self._data["Reclamation Water Storage Tank Name"] = value

    @property
    def hot_water_supply_temperature_schedule_name(self):
        """Get hot_water_supply_temperature_schedule_name

        Returns:
            str: the value of `hot_water_supply_temperature_schedule_name` or None if not set
        """
        return self._data["Hot Water Supply Temperature Schedule Name"]

    @hot_water_supply_temperature_schedule_name.setter
    def hot_water_supply_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water Supply Temperature Schedule Name`
        Defaults to cold water supply temperature

        Args:
            value (str): value for IDD Field `Hot Water Supply Temperature Schedule Name`
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
                                 'for field `hot_water_supply_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_supply_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_supply_temperature_schedule_name`')
        self._data["Hot Water Supply Temperature Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """Get cold_water_supply_temperature_schedule_name

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set
        """
        return self._data["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cold Water Supply Temperature Schedule Name`
        Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `Cold Water Supply Temperature Schedule Name`
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
                                 'for field `cold_water_supply_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_water_supply_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_water_supply_temperature_schedule_name`')
        self._data["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def drain_water_heat_exchanger_type(self):
        """Get drain_water_heat_exchanger_type

        Returns:
            str: the value of `drain_water_heat_exchanger_type` or None if not set
        """
        return self._data["Drain Water Heat Exchanger Type"]

    @drain_water_heat_exchanger_type.setter
    def drain_water_heat_exchanger_type(self, value="None"):
        """  Corresponds to IDD Field `Drain Water Heat Exchanger Type`

        Args:
            value (str): value for IDD Field `Drain Water Heat Exchanger Type`
                Accepted values are:
                      - None
                      - Ideal
                      - CounterFlow
                      - CrossFlow
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
                                 'for field `drain_water_heat_exchanger_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drain_water_heat_exchanger_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `drain_water_heat_exchanger_type`')
            vals = {}
            vals["none"] = "None"
            vals["ideal"] = "Ideal"
            vals["counterflow"] = "CounterFlow"
            vals["crossflow"] = "CrossFlow"
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
                                     'field `drain_water_heat_exchanger_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `drain_water_heat_exchanger_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Drain Water Heat Exchanger Type"] = value

    @property
    def drain_water_heat_exchanger_destination(self):
        """Get drain_water_heat_exchanger_destination

        Returns:
            str: the value of `drain_water_heat_exchanger_destination` or None if not set
        """
        return self._data["Drain Water Heat Exchanger Destination"]

    @drain_water_heat_exchanger_destination.setter
    def drain_water_heat_exchanger_destination(self, value="Plant"):
        """  Corresponds to IDD Field `Drain Water Heat Exchanger Destination`

        Args:
            value (str): value for IDD Field `Drain Water Heat Exchanger Destination`
                Accepted values are:
                      - Plant
                      - Equipment
                      - PlantAndEquipment
                Default value: Plant
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
                                 'for field `drain_water_heat_exchanger_destination`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drain_water_heat_exchanger_destination`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `drain_water_heat_exchanger_destination`')
            vals = {}
            vals["plant"] = "Plant"
            vals["equipment"] = "Equipment"
            vals["plantandequipment"] = "PlantAndEquipment"
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
                                     'field `drain_water_heat_exchanger_destination`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `drain_water_heat_exchanger_destination`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Drain Water Heat Exchanger Destination"] = value

    @property
    def drain_water_heat_exchanger_ufactor_times_area(self):
        """Get drain_water_heat_exchanger_ufactor_times_area

        Returns:
            float: the value of `drain_water_heat_exchanger_ufactor_times_area` or None if not set
        """
        return self._data["Drain Water Heat Exchanger U-Factor Times Area"]

    @drain_water_heat_exchanger_ufactor_times_area.setter
    def drain_water_heat_exchanger_ufactor_times_area(self, value=None):
        """  Corresponds to IDD Field `Drain Water Heat Exchanger U-Factor Times Area`

        Args:
            value (float): value for IDD Field `Drain Water Heat Exchanger U-Factor Times Area`
                Units: W/K
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
                                 'for field `drain_water_heat_exchanger_ufactor_times_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `drain_water_heat_exchanger_ufactor_times_area`')
        self._data["Drain Water Heat Exchanger U-Factor Times Area"] = value

    @property
    def water_use_equipment_1_name(self):
        """Get water_use_equipment_1_name

        Returns:
            str: the value of `water_use_equipment_1_name` or None if not set
        """
        return self._data["Water Use Equipment 1 Name"]

    @water_use_equipment_1_name.setter
    def water_use_equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 1 Name`
        Enter the name of a WaterUse:Equipment object.

        Args:
            value (str): value for IDD Field `Water Use Equipment 1 Name`
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
                                 'for field `water_use_equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_1_name`')
        self._data["Water Use Equipment 1 Name"] = value

    @property
    def water_use_equipment_2_name(self):
        """Get water_use_equipment_2_name

        Returns:
            str: the value of `water_use_equipment_2_name` or None if not set
        """
        return self._data["Water Use Equipment 2 Name"]

    @water_use_equipment_2_name.setter
    def water_use_equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 2 Name`
        Enter the name of a WaterUse:Equipment object.

        Args:
            value (str): value for IDD Field `Water Use Equipment 2 Name`
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
                                 'for field `water_use_equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_2_name`')
        self._data["Water Use Equipment 2 Name"] = value

    @property
    def water_use_equipment_3_name(self):
        """Get water_use_equipment_3_name

        Returns:
            str: the value of `water_use_equipment_3_name` or None if not set
        """
        return self._data["Water Use Equipment 3 Name"]

    @water_use_equipment_3_name.setter
    def water_use_equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 3 Name`
        Enter the name of a WaterUse:Equipment object.

        Args:
            value (str): value for IDD Field `Water Use Equipment 3 Name`
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
                                 'for field `water_use_equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_3_name`')
        self._data["Water Use Equipment 3 Name"] = value

    @property
    def water_use_equipment_4_name(self):
        """Get water_use_equipment_4_name

        Returns:
            str: the value of `water_use_equipment_4_name` or None if not set
        """
        return self._data["Water Use Equipment 4 Name"]

    @water_use_equipment_4_name.setter
    def water_use_equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 4 Name`
        Enter the name of a WaterUse:Equipment object.

        Args:
            value (str): value for IDD Field `Water Use Equipment 4 Name`
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
                                 'for field `water_use_equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_4_name`')
        self._data["Water Use Equipment 4 Name"] = value

    @property
    def water_use_equipment_5_name(self):
        """Get water_use_equipment_5_name

        Returns:
            str: the value of `water_use_equipment_5_name` or None if not set
        """
        return self._data["Water Use Equipment 5 Name"]

    @water_use_equipment_5_name.setter
    def water_use_equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 5 Name`
        Enter the name of a WaterUse:Equipment object.

        Args:
            value (str): value for IDD Field `Water Use Equipment 5 Name`
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
                                 'for field `water_use_equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_5_name`')
        self._data["Water Use Equipment 5 Name"] = value

    @property
    def water_use_equipment_6_name(self):
        """Get water_use_equipment_6_name

        Returns:
            str: the value of `water_use_equipment_6_name` or None if not set
        """
        return self._data["Water Use Equipment 6 Name"]

    @water_use_equipment_6_name.setter
    def water_use_equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Water Use Equipment 6 Name`
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
                                 'for field `water_use_equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_6_name`')
        self._data["Water Use Equipment 6 Name"] = value

    @property
    def water_use_equipment_7_name(self):
        """Get water_use_equipment_7_name

        Returns:
            str: the value of `water_use_equipment_7_name` or None if not set
        """
        return self._data["Water Use Equipment 7 Name"]

    @water_use_equipment_7_name.setter
    def water_use_equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Water Use Equipment 7 Name`
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
                                 'for field `water_use_equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_7_name`')
        self._data["Water Use Equipment 7 Name"] = value

    @property
    def water_use_equipment_8_name(self):
        """Get water_use_equipment_8_name

        Returns:
            str: the value of `water_use_equipment_8_name` or None if not set
        """
        return self._data["Water Use Equipment 8 Name"]

    @water_use_equipment_8_name.setter
    def water_use_equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Water Use Equipment 8 Name`
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
                                 'for field `water_use_equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_8_name`')
        self._data["Water Use Equipment 8 Name"] = value

    @property
    def water_use_equipment_9_name(self):
        """Get water_use_equipment_9_name

        Returns:
            str: the value of `water_use_equipment_9_name` or None if not set
        """
        return self._data["Water Use Equipment 9 Name"]

    @water_use_equipment_9_name.setter
    def water_use_equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Water Use Equipment 9 Name`
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
                                 'for field `water_use_equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_9_name`')
        self._data["Water Use Equipment 9 Name"] = value

    @property
    def water_use_equipment_10_name(self):
        """Get water_use_equipment_10_name

        Returns:
            str: the value of `water_use_equipment_10_name` or None if not set
        """
        return self._data["Water Use Equipment 10 Name"]

    @water_use_equipment_10_name.setter
    def water_use_equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `Water Use Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Water Use Equipment 10 Name`
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
                                 'for field `water_use_equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_use_equipment_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_use_equipment_10_name`')
        self._data["Water Use Equipment 10 Name"] = value

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

class WaterUseStorage(object):
    """ Corresponds to IDD object `WaterUse:Storage`
        A water storage tank. If the building model is to include any on-site
        water collection, wells, or storing and reuse of graywater, then a WaterUse:Storage
        object is needed. Each WaterUse:Storage can serve as a central node and make
        connections to numerous sources of supply or numerous components with demand. If a
        maximum capacity is not specified, the tank is assumed to have unlimited capacity.
    """
    internal_name = "WaterUse:Storage"
    field_count = 20
    required_fields = ["Name", "Water Temperature Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterUse:Storage`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Water Quality Subcategory"] = None
        self._data["Maximum Capacity"] = None
        self._data["Initial Volume"] = None
        self._data["Design In Flow Rate"] = None
        self._data["Design Out Flow Rate"] = None
        self._data["Overflow Destination"] = None
        self._data["Type of Supply Controlled by Float Valve"] = None
        self._data["Float Valve On Capacity"] = None
        self._data["Float Valve Off Capacity"] = None
        self._data["Backup Mains Capacity"] = None
        self._data["Other Tank Name"] = None
        self._data["Water Thermal Mode"] = None
        self._data["Water Temperature Schedule Name"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Tank Surface Area"] = None
        self._data["Tank U Value"] = None
        self._data["Tank Outside Surface Material Name"] = None
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
            self.water_quality_subcategory = None
        else:
            self.water_quality_subcategory = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_capacity = None
        else:
            self.maximum_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_volume = None
        else:
            self.initial_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_in_flow_rate = None
        else:
            self.design_in_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_out_flow_rate = None
        else:
            self.design_out_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overflow_destination = None
        else:
            self.overflow_destination = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type_of_supply_controlled_by_float_valve = None
        else:
            self.type_of_supply_controlled_by_float_valve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.float_valve_on_capacity = None
        else:
            self.float_valve_on_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.float_valve_off_capacity = None
        else:
            self.float_valve_off_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.backup_mains_capacity = None
        else:
            self.backup_mains_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.other_tank_name = None
        else:
            self.other_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_thermal_mode = None
        else:
            self.water_thermal_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_temperature_schedule_name = None
        else:
            self.water_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_surface_area = None
        else:
            self.tank_surface_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_u_value = None
        else:
            self.tank_u_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tank_outside_surface_material_name = None
        else:
            self.tank_outside_surface_material_name = vals[i]
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
    def water_quality_subcategory(self):
        """Get water_quality_subcategory

        Returns:
            str: the value of `water_quality_subcategory` or None if not set
        """
        return self._data["Water Quality Subcategory"]

    @water_quality_subcategory.setter
    def water_quality_subcategory(self, value=None):
        """  Corresponds to IDD Field `Water Quality Subcategory`

        Args:
            value (str): value for IDD Field `Water Quality Subcategory`
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
                                 'for field `water_quality_subcategory`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_quality_subcategory`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_quality_subcategory`')
        self._data["Water Quality Subcategory"] = value

    @property
    def maximum_capacity(self):
        """Get maximum_capacity

        Returns:
            float: the value of `maximum_capacity` or None if not set
        """
        return self._data["Maximum Capacity"]

    @maximum_capacity.setter
    def maximum_capacity(self, value=None):
        """  Corresponds to IDD Field `Maximum Capacity`
        Defaults to unlimited capacity.

        Args:
            value (float): value for IDD Field `Maximum Capacity`
                Units: m3
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
                                 'for field `maximum_capacity`'.format(value))
        self._data["Maximum Capacity"] = value

    @property
    def initial_volume(self):
        """Get initial_volume

        Returns:
            float: the value of `initial_volume` or None if not set
        """
        return self._data["Initial Volume"]

    @initial_volume.setter
    def initial_volume(self, value=None):
        """  Corresponds to IDD Field `Initial Volume`

        Args:
            value (float): value for IDD Field `Initial Volume`
                Units: m3
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
                                 'for field `initial_volume`'.format(value))
        self._data["Initial Volume"] = value

    @property
    def design_in_flow_rate(self):
        """Get design_in_flow_rate

        Returns:
            float: the value of `design_in_flow_rate` or None if not set
        """
        return self._data["Design In Flow Rate"]

    @design_in_flow_rate.setter
    def design_in_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design In Flow Rate`
        Defaults to unlimited flow.

        Args:
            value (float): value for IDD Field `Design In Flow Rate`
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
                                 'for field `design_in_flow_rate`'.format(value))
        self._data["Design In Flow Rate"] = value

    @property
    def design_out_flow_rate(self):
        """Get design_out_flow_rate

        Returns:
            float: the value of `design_out_flow_rate` or None if not set
        """
        return self._data["Design Out Flow Rate"]

    @design_out_flow_rate.setter
    def design_out_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Out Flow Rate`
        Defaults to unlimited flow.

        Args:
            value (float): value for IDD Field `Design Out Flow Rate`
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
                                 'for field `design_out_flow_rate`'.format(value))
        self._data["Design Out Flow Rate"] = value

    @property
    def overflow_destination(self):
        """Get overflow_destination

        Returns:
            str: the value of `overflow_destination` or None if not set
        """
        return self._data["Overflow Destination"]

    @overflow_destination.setter
    def overflow_destination(self, value=None):
        """  Corresponds to IDD Field `Overflow Destination`
        If blank, overflow is discarded

        Args:
            value (str): value for IDD Field `Overflow Destination`
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
                                 'for field `overflow_destination`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `overflow_destination`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `overflow_destination`')
        self._data["Overflow Destination"] = value

    @property
    def type_of_supply_controlled_by_float_valve(self):
        """Get type_of_supply_controlled_by_float_valve

        Returns:
            str: the value of `type_of_supply_controlled_by_float_valve` or None if not set
        """
        return self._data["Type of Supply Controlled by Float Valve"]

    @type_of_supply_controlled_by_float_valve.setter
    def type_of_supply_controlled_by_float_valve(self, value=None):
        """  Corresponds to IDD Field `Type of Supply Controlled by Float Valve`

        Args:
            value (str): value for IDD Field `Type of Supply Controlled by Float Valve`
                Accepted values are:
                      - None
                      - Mains
                      - GroundwaterWell
                      - OtherTank
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
                                 'for field `type_of_supply_controlled_by_float_valve`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_supply_controlled_by_float_valve`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `type_of_supply_controlled_by_float_valve`')
            vals = {}
            vals["none"] = "None"
            vals["mains"] = "Mains"
            vals["groundwaterwell"] = "GroundwaterWell"
            vals["othertank"] = "OtherTank"
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
                                     'field `type_of_supply_controlled_by_float_valve`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `type_of_supply_controlled_by_float_valve`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Type of Supply Controlled by Float Valve"] = value

    @property
    def float_valve_on_capacity(self):
        """Get float_valve_on_capacity

        Returns:
            float: the value of `float_valve_on_capacity` or None if not set
        """
        return self._data["Float Valve On Capacity"]

    @float_valve_on_capacity.setter
    def float_valve_on_capacity(self, value=None):
        """  Corresponds to IDD Field `Float Valve On Capacity`
        Lower range of target storage level e.g. float valve kicks on

        Args:
            value (float): value for IDD Field `Float Valve On Capacity`
                Units: m3
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
                                 'for field `float_valve_on_capacity`'.format(value))
        self._data["Float Valve On Capacity"] = value

    @property
    def float_valve_off_capacity(self):
        """Get float_valve_off_capacity

        Returns:
            float: the value of `float_valve_off_capacity` or None if not set
        """
        return self._data["Float Valve Off Capacity"]

    @float_valve_off_capacity.setter
    def float_valve_off_capacity(self, value=None):
        """  Corresponds to IDD Field `Float Valve Off Capacity`
        Upper range of target storage level e.g. float valve kicks off

        Args:
            value (float): value for IDD Field `Float Valve Off Capacity`
                Units: m3
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
                                 'for field `float_valve_off_capacity`'.format(value))
        self._data["Float Valve Off Capacity"] = value

    @property
    def backup_mains_capacity(self):
        """Get backup_mains_capacity

        Returns:
            float: the value of `backup_mains_capacity` or None if not set
        """
        return self._data["Backup Mains Capacity"]

    @backup_mains_capacity.setter
    def backup_mains_capacity(self, value=None):
        """  Corresponds to IDD Field `Backup Mains Capacity`
        Lower range of secondary target storage level
        used to keep tanks at a minimum level using
        mains water if well can't keep up

        Args:
            value (float): value for IDD Field `Backup Mains Capacity`
                Units: m3
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
                                 'for field `backup_mains_capacity`'.format(value))
        self._data["Backup Mains Capacity"] = value

    @property
    def other_tank_name(self):
        """Get other_tank_name

        Returns:
            str: the value of `other_tank_name` or None if not set
        """
        return self._data["Other Tank Name"]

    @other_tank_name.setter
    def other_tank_name(self, value=None):
        """  Corresponds to IDD Field `Other Tank Name`

        Args:
            value (str): value for IDD Field `Other Tank Name`
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
                                 'for field `other_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `other_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `other_tank_name`')
        self._data["Other Tank Name"] = value

    @property
    def water_thermal_mode(self):
        """Get water_thermal_mode

        Returns:
            str: the value of `water_thermal_mode` or None if not set
        """
        return self._data["Water Thermal Mode"]

    @water_thermal_mode.setter
    def water_thermal_mode(self, value=None):
        """  Corresponds to IDD Field `Water Thermal Mode`

        Args:
            value (str): value for IDD Field `Water Thermal Mode`
                Accepted values are:
                      - ScheduledTemperature
                      - ThermalModel
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
                                 'for field `water_thermal_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_thermal_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_thermal_mode`')
            vals = {}
            vals["scheduledtemperature"] = "ScheduledTemperature"
            vals["thermalmodel"] = "ThermalModel"
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
                                     'field `water_thermal_mode`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `water_thermal_mode`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Water Thermal Mode"] = value

    @property
    def water_temperature_schedule_name(self):
        """Get water_temperature_schedule_name

        Returns:
            str: the value of `water_temperature_schedule_name` or None if not set
        """
        return self._data["Water Temperature Schedule Name"]

    @water_temperature_schedule_name.setter
    def water_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Water Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Water Temperature Schedule Name`
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
                                 'for field `water_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_temperature_schedule_name`')
        self._data["Water Temperature Schedule Name"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `Ambient Temperature Indicator`

        Args:
            value (str): value for IDD Field `Ambient Temperature Indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
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
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_indicator`')
            vals = {}
            vals["schedule"] = "Schedule"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
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
                                     'field `ambient_temperature_indicator`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `ambient_temperature_indicator`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`
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
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ambient_temperature_schedule_name`')
        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def tank_surface_area(self):
        """Get tank_surface_area

        Returns:
            float: the value of `tank_surface_area` or None if not set
        """
        return self._data["Tank Surface Area"]

    @tank_surface_area.setter
    def tank_surface_area(self, value=None):
        """  Corresponds to IDD Field `Tank Surface Area`

        Args:
            value (float): value for IDD Field `Tank Surface Area`
                Units: m2
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
                                 'for field `tank_surface_area`'.format(value))
        self._data["Tank Surface Area"] = value

    @property
    def tank_u_value(self):
        """Get tank_u_value

        Returns:
            float: the value of `tank_u_value` or None if not set
        """
        return self._data["Tank U Value"]

    @tank_u_value.setter
    def tank_u_value(self, value=None):
        """  Corresponds to IDD Field `Tank U Value`

        Args:
            value (float): value for IDD Field `Tank U Value`
                Units: W/m2-K
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
                                 'for field `tank_u_value`'.format(value))
        self._data["Tank U Value"] = value

    @property
    def tank_outside_surface_material_name(self):
        """Get tank_outside_surface_material_name

        Returns:
            str: the value of `tank_outside_surface_material_name` or None if not set
        """
        return self._data["Tank Outside Surface Material Name"]

    @tank_outside_surface_material_name.setter
    def tank_outside_surface_material_name(self, value=None):
        """  Corresponds to IDD Field `Tank Outside Surface Material Name`

        Args:
            value (str): value for IDD Field `Tank Outside Surface Material Name`
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
                                 'for field `tank_outside_surface_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_outside_surface_material_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `tank_outside_surface_material_name`')
        self._data["Tank Outside Surface Material Name"] = value

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

class WaterUseWell(object):
    """ Corresponds to IDD object `WaterUse:Well`
        Simulates on-site water supply from a well. Well water is pumped out of the ground
        into a WaterUse:Storage. The operation of the ground water well is controlled by the
        associated WaterUse:Storage which is assumed to be operated as a vented cistern with
        no pressure tank.
    """
    internal_name = "WaterUse:Well"
    field_count = 12
    required_fields = ["Name", "Storage Tank Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterUse:Well`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Storage Tank Name"] = None
        self._data["Pump Depth"] = None
        self._data["Pump Rated Flow Rate"] = None
        self._data["Pump Rated Head"] = None
        self._data["Pump Rated Power Consumption"] = None
        self._data["Pump Efficiency"] = None
        self._data["Well Recovery Rate"] = None
        self._data["Nominal Well Storage Volume"] = None
        self._data["Water Table Depth Mode"] = None
        self._data["Water Table Depth"] = None
        self._data["Water Table Depth Schedule Name"] = None
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
            self.storage_tank_name = None
        else:
            self.storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_depth = None
        else:
            self.pump_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_rated_flow_rate = None
        else:
            self.pump_rated_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_rated_head = None
        else:
            self.pump_rated_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_rated_power_consumption = None
        else:
            self.pump_rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_efficiency = None
        else:
            self.pump_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.well_recovery_rate = None
        else:
            self.well_recovery_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nominal_well_storage_volume = None
        else:
            self.nominal_well_storage_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_table_depth_mode = None
        else:
            self.water_table_depth_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_table_depth = None
        else:
            self.water_table_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_table_depth_schedule_name = None
        else:
            self.water_table_depth_schedule_name = vals[i]
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
    def storage_tank_name(self):
        """Get storage_tank_name

        Returns:
            str: the value of `storage_tank_name` or None if not set
        """
        return self._data["Storage Tank Name"]

    @storage_tank_name.setter
    def storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Storage Tank Name`

        Args:
            value (str): value for IDD Field `Storage Tank Name`
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
                                 'for field `storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `storage_tank_name`')
        self._data["Storage Tank Name"] = value

    @property
    def pump_depth(self):
        """Get pump_depth

        Returns:
            float: the value of `pump_depth` or None if not set
        """
        return self._data["Pump Depth"]

    @pump_depth.setter
    def pump_depth(self, value=None):
        """  Corresponds to IDD Field `Pump Depth`

        Args:
            value (float): value for IDD Field `Pump Depth`
                Units: m
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
                                 'for field `pump_depth`'.format(value))
        self._data["Pump Depth"] = value

    @property
    def pump_rated_flow_rate(self):
        """Get pump_rated_flow_rate

        Returns:
            float: the value of `pump_rated_flow_rate` or None if not set
        """
        return self._data["Pump Rated Flow Rate"]

    @pump_rated_flow_rate.setter
    def pump_rated_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Pump Rated Flow Rate`

        Args:
            value (float): value for IDD Field `Pump Rated Flow Rate`
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
                                 'for field `pump_rated_flow_rate`'.format(value))
        self._data["Pump Rated Flow Rate"] = value

    @property
    def pump_rated_head(self):
        """Get pump_rated_head

        Returns:
            float: the value of `pump_rated_head` or None if not set
        """
        return self._data["Pump Rated Head"]

    @pump_rated_head.setter
    def pump_rated_head(self, value=None):
        """  Corresponds to IDD Field `Pump Rated Head`

        Args:
            value (float): value for IDD Field `Pump Rated Head`
                Units: Pa
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
                                 'for field `pump_rated_head`'.format(value))
        self._data["Pump Rated Head"] = value

    @property
    def pump_rated_power_consumption(self):
        """Get pump_rated_power_consumption

        Returns:
            float: the value of `pump_rated_power_consumption` or None if not set
        """
        return self._data["Pump Rated Power Consumption"]

    @pump_rated_power_consumption.setter
    def pump_rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Pump Rated Power Consumption`

        Args:
            value (float): value for IDD Field `Pump Rated Power Consumption`
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
                                 'for field `pump_rated_power_consumption`'.format(value))
        self._data["Pump Rated Power Consumption"] = value

    @property
    def pump_efficiency(self):
        """Get pump_efficiency

        Returns:
            float: the value of `pump_efficiency` or None if not set
        """
        return self._data["Pump Efficiency"]

    @pump_efficiency.setter
    def pump_efficiency(self, value=None):
        """  Corresponds to IDD Field `Pump Efficiency`

        Args:
            value (float): value for IDD Field `Pump Efficiency`
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
                                 'for field `pump_efficiency`'.format(value))
        self._data["Pump Efficiency"] = value

    @property
    def well_recovery_rate(self):
        """Get well_recovery_rate

        Returns:
            float: the value of `well_recovery_rate` or None if not set
        """
        return self._data["Well Recovery Rate"]

    @well_recovery_rate.setter
    def well_recovery_rate(self, value=None):
        """  Corresponds to IDD Field `Well Recovery Rate`

        Args:
            value (float): value for IDD Field `Well Recovery Rate`
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
                                 'for field `well_recovery_rate`'.format(value))
        self._data["Well Recovery Rate"] = value

    @property
    def nominal_well_storage_volume(self):
        """Get nominal_well_storage_volume

        Returns:
            float: the value of `nominal_well_storage_volume` or None if not set
        """
        return self._data["Nominal Well Storage Volume"]

    @nominal_well_storage_volume.setter
    def nominal_well_storage_volume(self, value=None):
        """  Corresponds to IDD Field `Nominal Well Storage Volume`

        Args:
            value (float): value for IDD Field `Nominal Well Storage Volume`
                Units: m3
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
                                 'for field `nominal_well_storage_volume`'.format(value))
        self._data["Nominal Well Storage Volume"] = value

    @property
    def water_table_depth_mode(self):
        """Get water_table_depth_mode

        Returns:
            str: the value of `water_table_depth_mode` or None if not set
        """
        return self._data["Water Table Depth Mode"]

    @water_table_depth_mode.setter
    def water_table_depth_mode(self, value=None):
        """  Corresponds to IDD Field `Water Table Depth Mode`

        Args:
            value (str): value for IDD Field `Water Table Depth Mode`
                Accepted values are:
                      - Constant
                      - Scheduled
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
                                 'for field `water_table_depth_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_table_depth_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_table_depth_mode`')
            vals = {}
            vals["constant"] = "Constant"
            vals["scheduled"] = "Scheduled"
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
                                     'field `water_table_depth_mode`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `water_table_depth_mode`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Water Table Depth Mode"] = value

    @property
    def water_table_depth(self):
        """Get water_table_depth

        Returns:
            float: the value of `water_table_depth` or None if not set
        """
        return self._data["Water Table Depth"]

    @water_table_depth.setter
    def water_table_depth(self, value=None):
        """  Corresponds to IDD Field `Water Table Depth`

        Args:
            value (float): value for IDD Field `Water Table Depth`
                Units: m
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
                                 'for field `water_table_depth`'.format(value))
        self._data["Water Table Depth"] = value

    @property
    def water_table_depth_schedule_name(self):
        """Get water_table_depth_schedule_name

        Returns:
            str: the value of `water_table_depth_schedule_name` or None if not set
        """
        return self._data["Water Table Depth Schedule Name"]

    @water_table_depth_schedule_name.setter
    def water_table_depth_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Water Table Depth Schedule Name`

        Args:
            value (str): value for IDD Field `Water Table Depth Schedule Name`
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
                                 'for field `water_table_depth_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_table_depth_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `water_table_depth_schedule_name`')
        self._data["Water Table Depth Schedule Name"] = value

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

class WaterUseRainCollector(object):
    """ Corresponds to IDD object `WaterUse:RainCollector`
        Used for harvesting rainwater falling on building surfaces. The rainwater is sent to a
        WaterUse:Storage object. In order to use this object it is necessary to also include
        a Site:Precipitation object to describe the rates of rainfall.
    """
    internal_name = "WaterUse:RainCollector"
    field_count = 16
    required_fields = ["Name", "Storage Tank Name", "Collection Surface 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `WaterUse:RainCollector`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Storage Tank Name"] = None
        self._data["Loss Factor Mode"] = None
        self._data["Collection Loss Factor"] = None
        self._data["Collection Loss Factor Schedule Name"] = None
        self._data["Maximum Collection Rate"] = None
        self._data["Collection Surface 1 Name"] = None
        self._data["Collection Surface 2 Name"] = None
        self._data["Collection Surface 3 Name"] = None
        self._data["Collection Surface 4 Name"] = None
        self._data["Collection Surface 5 Name"] = None
        self._data["Collection Surface 6 Name"] = None
        self._data["Collection Surface 7 Name"] = None
        self._data["Collection Surface 8 Name"] = None
        self._data["Collection Surface 9 Name"] = None
        self._data["Collection Surface 10 Name"] = None
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
            self.storage_tank_name = None
        else:
            self.storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loss_factor_mode = None
        else:
            self.loss_factor_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_loss_factor = None
        else:
            self.collection_loss_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_loss_factor_schedule_name = None
        else:
            self.collection_loss_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_collection_rate = None
        else:
            self.maximum_collection_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_1_name = None
        else:
            self.collection_surface_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_2_name = None
        else:
            self.collection_surface_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_3_name = None
        else:
            self.collection_surface_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_4_name = None
        else:
            self.collection_surface_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_5_name = None
        else:
            self.collection_surface_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_6_name = None
        else:
            self.collection_surface_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_7_name = None
        else:
            self.collection_surface_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_8_name = None
        else:
            self.collection_surface_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_9_name = None
        else:
            self.collection_surface_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collection_surface_10_name = None
        else:
            self.collection_surface_10_name = vals[i]
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
    def storage_tank_name(self):
        """Get storage_tank_name

        Returns:
            str: the value of `storage_tank_name` or None if not set
        """
        return self._data["Storage Tank Name"]

    @storage_tank_name.setter
    def storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `Storage Tank Name`

        Args:
            value (str): value for IDD Field `Storage Tank Name`
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
                                 'for field `storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `storage_tank_name`')
        self._data["Storage Tank Name"] = value

    @property
    def loss_factor_mode(self):
        """Get loss_factor_mode

        Returns:
            str: the value of `loss_factor_mode` or None if not set
        """
        return self._data["Loss Factor Mode"]

    @loss_factor_mode.setter
    def loss_factor_mode(self, value=None):
        """  Corresponds to IDD Field `Loss Factor Mode`

        Args:
            value (str): value for IDD Field `Loss Factor Mode`
                Accepted values are:
                      - Constant
                      - Scheduled
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
                                 'for field `loss_factor_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loss_factor_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loss_factor_mode`')
            vals = {}
            vals["constant"] = "Constant"
            vals["scheduled"] = "Scheduled"
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
                                     'field `loss_factor_mode`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `loss_factor_mode`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Loss Factor Mode"] = value

    @property
    def collection_loss_factor(self):
        """Get collection_loss_factor

        Returns:
            float: the value of `collection_loss_factor` or None if not set
        """
        return self._data["Collection Loss Factor"]

    @collection_loss_factor.setter
    def collection_loss_factor(self, value=None):
        """  Corresponds to IDD Field `Collection Loss Factor`
        this is the portion of rain
        that is lost in the process of collecting it
        the rain collected is one minus this factor

        Args:
            value (float): value for IDD Field `Collection Loss Factor`
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
                                 'for field `collection_loss_factor`'.format(value))
        self._data["Collection Loss Factor"] = value

    @property
    def collection_loss_factor_schedule_name(self):
        """Get collection_loss_factor_schedule_name

        Returns:
            str: the value of `collection_loss_factor_schedule_name` or None if not set
        """
        return self._data["Collection Loss Factor Schedule Name"]

    @collection_loss_factor_schedule_name.setter
    def collection_loss_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Collection Loss Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Collection Loss Factor Schedule Name`
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
                                 'for field `collection_loss_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_loss_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_loss_factor_schedule_name`')
        self._data["Collection Loss Factor Schedule Name"] = value

    @property
    def maximum_collection_rate(self):
        """Get maximum_collection_rate

        Returns:
            float: the value of `maximum_collection_rate` or None if not set
        """
        return self._data["Maximum Collection Rate"]

    @maximum_collection_rate.setter
    def maximum_collection_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Collection Rate`
        Defaults to unlimited flow.

        Args:
            value (float): value for IDD Field `Maximum Collection Rate`
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
                                 'for field `maximum_collection_rate`'.format(value))
        self._data["Maximum Collection Rate"] = value

    @property
    def collection_surface_1_name(self):
        """Get collection_surface_1_name

        Returns:
            str: the value of `collection_surface_1_name` or None if not set
        """
        return self._data["Collection Surface 1 Name"]

    @collection_surface_1_name.setter
    def collection_surface_1_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 1 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 1 Name`
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
                                 'for field `collection_surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_1_name`')
        self._data["Collection Surface 1 Name"] = value

    @property
    def collection_surface_2_name(self):
        """Get collection_surface_2_name

        Returns:
            str: the value of `collection_surface_2_name` or None if not set
        """
        return self._data["Collection Surface 2 Name"]

    @collection_surface_2_name.setter
    def collection_surface_2_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 2 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 2 Name`
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
                                 'for field `collection_surface_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_2_name`')
        self._data["Collection Surface 2 Name"] = value

    @property
    def collection_surface_3_name(self):
        """Get collection_surface_3_name

        Returns:
            str: the value of `collection_surface_3_name` or None if not set
        """
        return self._data["Collection Surface 3 Name"]

    @collection_surface_3_name.setter
    def collection_surface_3_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 3 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 3 Name`
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
                                 'for field `collection_surface_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_3_name`')
        self._data["Collection Surface 3 Name"] = value

    @property
    def collection_surface_4_name(self):
        """Get collection_surface_4_name

        Returns:
            str: the value of `collection_surface_4_name` or None if not set
        """
        return self._data["Collection Surface 4 Name"]

    @collection_surface_4_name.setter
    def collection_surface_4_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 4 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 4 Name`
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
                                 'for field `collection_surface_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_4_name`')
        self._data["Collection Surface 4 Name"] = value

    @property
    def collection_surface_5_name(self):
        """Get collection_surface_5_name

        Returns:
            str: the value of `collection_surface_5_name` or None if not set
        """
        return self._data["Collection Surface 5 Name"]

    @collection_surface_5_name.setter
    def collection_surface_5_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 5 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 5 Name`
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
                                 'for field `collection_surface_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_5_name`')
        self._data["Collection Surface 5 Name"] = value

    @property
    def collection_surface_6_name(self):
        """Get collection_surface_6_name

        Returns:
            str: the value of `collection_surface_6_name` or None if not set
        """
        return self._data["Collection Surface 6 Name"]

    @collection_surface_6_name.setter
    def collection_surface_6_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 6 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 6 Name`
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
                                 'for field `collection_surface_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_6_name`')
        self._data["Collection Surface 6 Name"] = value

    @property
    def collection_surface_7_name(self):
        """Get collection_surface_7_name

        Returns:
            str: the value of `collection_surface_7_name` or None if not set
        """
        return self._data["Collection Surface 7 Name"]

    @collection_surface_7_name.setter
    def collection_surface_7_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 7 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 7 Name`
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
                                 'for field `collection_surface_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_7_name`')
        self._data["Collection Surface 7 Name"] = value

    @property
    def collection_surface_8_name(self):
        """Get collection_surface_8_name

        Returns:
            str: the value of `collection_surface_8_name` or None if not set
        """
        return self._data["Collection Surface 8 Name"]

    @collection_surface_8_name.setter
    def collection_surface_8_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 8 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 8 Name`
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
                                 'for field `collection_surface_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_8_name`')
        self._data["Collection Surface 8 Name"] = value

    @property
    def collection_surface_9_name(self):
        """Get collection_surface_9_name

        Returns:
            str: the value of `collection_surface_9_name` or None if not set
        """
        return self._data["Collection Surface 9 Name"]

    @collection_surface_9_name.setter
    def collection_surface_9_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 9 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 9 Name`
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
                                 'for field `collection_surface_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_9_name`')
        self._data["Collection Surface 9 Name"] = value

    @property
    def collection_surface_10_name(self):
        """Get collection_surface_10_name

        Returns:
            str: the value of `collection_surface_10_name` or None if not set
        """
        return self._data["Collection Surface 10 Name"]

    @collection_surface_10_name.setter
    def collection_surface_10_name(self, value=None):
        """  Corresponds to IDD Field `Collection Surface 10 Name`

        Args:
            value (str): value for IDD Field `Collection Surface 10 Name`
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
                                 'for field `collection_surface_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_surface_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `collection_surface_10_name`')
        self._data["Collection Surface 10 Name"] = value

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