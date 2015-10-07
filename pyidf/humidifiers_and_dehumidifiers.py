""" Data objects in group "Humidifiers and Dehumidifiers"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class HumidifierSteamElectric(DataObject):

    """ Corresponds to IDD object `Humidifier:Steam:Electric`
        Electrically heated steam humidifier with fan.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated capacity',
                                       {'name': u'Rated Capacity',
                                        'pyname': u'rated_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'rated power',
                                       {'name': u'Rated Power',
                                        'pyname': u'rated_power',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated fan power',
                                       {'name': u'Rated Fan Power',
                                        'pyname': u'rated_fan_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'standby power',
                                       {'name': u'Standby Power',
                                        'pyname': u'standby_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water storage tank name',
                                       {'name': u'Water Storage Tank Name',
                                        'pyname': u'water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Humidifiers and Dehumidifiers',
               'min-fields': 0,
               'name': u'Humidifier:Steam:Electric',
               'pyname': u'HumidifierSteamElectric',
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

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

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
    def rated_capacity(self):
        """field `Rated Capacity`

        |  Capacity is m3/s of water at 5.05 C
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `rated_capacity` or None if not set

        """
        return self["Rated Capacity"]

    @rated_capacity.setter
    def rated_capacity(self, value=None):
        """Corresponds to IDD field `Rated Capacity`"""
        self["Rated Capacity"] = value

    @property
    def rated_power(self):
        """field `Rated Power`

        |  if autosized the rated power is calculated from the rated capacity
        |  and enthalpy rise of water from 20.0C to 100.0C steam and assumes
        |  electric to thermal energy conversion efficiency of 100.0%
        |  Units: W
        |  IP-Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `rated_power` or None if not set

        """
        return self["Rated Power"]

    @rated_power.setter
    def rated_power(self, value=None):
        """Corresponds to IDD field `Rated Power`"""
        self["Rated Power"] = value

    @property
    def rated_fan_power(self):
        """field `Rated Fan Power`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Rated Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_fan_power` or None if not set

        """
        return self["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=None):
        """Corresponds to IDD field `Rated Fan Power`"""
        self["Rated Fan Power"] = value

    @property
    def standby_power(self):
        """field `Standby Power`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Standby Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `standby_power` or None if not set

        """
        return self["Standby Power"]

    @standby_power.setter
    def standby_power(self, value=None):
        """Corresponds to IDD field `Standby Power`"""
        self["Standby Power"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`"""
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`"""
        self["Air Outlet Node Name"] = value

    @property
    def water_storage_tank_name(self):
        """field `Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_storage_tank_name` or None if not set

        """
        return self["Water Storage Tank Name"]

    @water_storage_tank_name.setter
    def water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Storage Tank Name`"""
        self["Water Storage Tank Name"] = value




class HumidifierSteamGas(DataObject):

    """ Corresponds to IDD object `Humidifier:Steam:Gas`
        Natural gas fired steam humidifier with optional blower fan.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated capacity',
                                       {'name': u'Rated Capacity',
                                        'pyname': u'rated_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'rated gas use rate',
                                       {'name': u'Rated Gas Use Rate',
                                        'pyname': u'rated_gas_use_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'thermal efficiency',
                                       {'name': u'Thermal Efficiency',
                                        'pyname': u'thermal_efficiency',
                                        'default': 0.8,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'thermal efficiency modifier curve name',
                                       {'name': u'Thermal Efficiency Modifier Curve Name',
                                        'pyname': u'thermal_efficiency_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated fan power',
                                       {'name': u'Rated Fan Power',
                                        'pyname': u'rated_fan_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'auxiliary electric power',
                                       {'name': u'Auxiliary Electric Power',
                                        'pyname': u'auxiliary_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water storage tank name',
                                       {'name': u'Water Storage Tank Name',
                                        'pyname': u'water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet water temperature option',
                                       {'name': u'Inlet Water Temperature Option',
                                        'pyname': u'inlet_water_temperature_option',
                                        'default': u'FixedInletWaterTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FixedInletWaterTemperature',
                                                            u'VariableInletWaterTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Humidifiers and Dehumidifiers',
               'min-fields': 0,
               'name': u'Humidifier:Steam:Gas',
               'pyname': u'HumidifierSteamGas',
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

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

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
    def rated_capacity(self):
        """field `Rated Capacity`

        |  Capacity is m3/s of water at 5.05 C
        |  The nominal full capacity water addition rate in m3/s of water at 5.05 C
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `rated_capacity` or None if not set

        """
        return self["Rated Capacity"]

    @rated_capacity.setter
    def rated_capacity(self, value=None):
        """Corresponds to IDD field `Rated Capacity`"""
        self["Rated Capacity"] = value

    @property
    def rated_gas_use_rate(self):
        """field `Rated Gas Use Rate`

        |  if auto-sized, the rated gas use rate is calculated from the rated
        |  capacity and enthalpy rise of water from 20.0C to 100.0C steam and user
        |  input thermal efficiency value specified in the next input field. If this
        |  input field is hard-sized and Inlet Water Temperature Option input field is
        |  selected as FixedInletWaterTemperature, then the thermal efficiency input
        |  field will not be used or else if the Inlet Water Temperature Option input
        |  field is selected as VariableInletWaterTemperature, then the thermal efficiency
        |  input value is overridden by a value calculated from the capacity, rated gas use
        |  rate and design condition.
        |  Units: W
        |  IP-Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Gas Use Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `rated_gas_use_rate` or None if not set

        """
        return self["Rated Gas Use Rate"]

    @rated_gas_use_rate.setter
    def rated_gas_use_rate(self, value=None):
        """Corresponds to IDD field `Rated Gas Use Rate`"""
        self["Rated Gas Use Rate"] = value

    @property
    def thermal_efficiency(self):
        """field `Thermal Efficiency`

        |  Based on the higher heating value of fuel.
        |  If "Rated Gas Use Rate" in the field above is not auto-sized and the Inlet Water
        |  Temperature Option input field is specified as FixedInletWaterTemperature, then the
        |  thermal efficiency specified will not be used in the calculation, or else if the
        |  Inlet Water Temperature Option input field is selected as VariableInletWaterTemperature,
        |  then the thermal efficiency value is overridden by a value calculated from the capacity,
        |  rated gas use rate and design condition.
        |  Units: dimensionless
        |  Default value: 0.8
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Thermal Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_efficiency` or None if not set

        """
        return self["Thermal Efficiency"]

    @thermal_efficiency.setter
    def thermal_efficiency(self, value=0.8):
        """Corresponds to IDD field `Thermal Efficiency`"""
        self["Thermal Efficiency"] = value

    @property
    def thermal_efficiency_modifier_curve_name(self):
        """field `Thermal Efficiency Modifier Curve Name`

        |  Linear, Quadratic and Cubic efficiency curves are solely a function of PLR.
        |  Linear = C1 + C2*PLR
        |  Quadratic = C1 + C2*PLR + C3*PLR^2
        |  Cubic = C1 + C2*PLR + C3*PLR^2 + C4*PLR^3
        |  This is thermal efficiency modifier curve name of gas fired steam humidifier.
        |  This curve is normalized, i.e., curve output value at rated condition is 1.0.

        Args:
            value (str): value for IDD Field `Thermal Efficiency Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_efficiency_modifier_curve_name` or None if not set

        """
        return self["Thermal Efficiency Modifier Curve Name"]

    @thermal_efficiency_modifier_curve_name.setter
    def thermal_efficiency_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Thermal Efficiency Modifier Curve Name`"""
        self["Thermal Efficiency Modifier Curve Name"] = value

    @property
    def rated_fan_power(self):
        """field `Rated Fan Power`

        |  The nominal full capacity electric power input to the blower fan in Watts. If no
        |  blower fan is required to inject the dry steam to the supply air stream, then
        |  this input field is set to zero.
        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Rated Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_fan_power` or None if not set

        """
        return self["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=None):
        """Corresponds to IDD field `Rated Fan Power`"""
        self["Rated Fan Power"] = value

    @property
    def auxiliary_electric_power(self):
        """field `Auxiliary Electric Power`

        |  The auxiliary electric power input in watts. This amount of power will be consumed
        |  whenever the unit is available (as defined by the availability schedule). This
        |  electric power is used for control purpose only.
        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Auxiliary Electric Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `auxiliary_electric_power` or None if not set

        """
        return self["Auxiliary Electric Power"]

    @auxiliary_electric_power.setter
    def auxiliary_electric_power(self, value=None):
        """Corresponds to IDD field `Auxiliary Electric Power`"""
        self["Auxiliary Electric Power"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`"""
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`"""
        self["Air Outlet Node Name"] = value

    @property
    def water_storage_tank_name(self):
        """field `Water Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_storage_tank_name` or None if not set

        """
        return self["Water Storage Tank Name"]

    @water_storage_tank_name.setter
    def water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Storage Tank Name`"""
        self["Water Storage Tank Name"] = value

    @property
    def inlet_water_temperature_option(self):
        """field `Inlet Water Temperature Option`

        |  The inlet water temperature can be fixed at 20C as it is done for electric steam
        |  humidifier or it can be allowed to vary with temperature of the water source.
        |  Currently allowed water sources are main water or water storage tank in water use objects.
        |  if FixedInletWaterTemperature is specified, then a fixed 20C water temperature will be
        |  used, or else if VariableInletWaterTemperature is specified, then inlet water will vary
        |  depending the source water temperature. If this input field is left blank, then fixed
        |  inlet water temperature of 20C will be assumed.
        |  Default value: FixedInletWaterTemperature

        Args:
            value (str): value for IDD Field `Inlet Water Temperature Option`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_water_temperature_option` or None if not set

        """
        return self["Inlet Water Temperature Option"]

    @inlet_water_temperature_option.setter
    def inlet_water_temperature_option(
            self,
            value="FixedInletWaterTemperature"):
        """Corresponds to IDD field `Inlet Water Temperature Option`"""
        self["Inlet Water Temperature Option"] = value




class DehumidifierDesiccantNoFans(DataObject):

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
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'process air inlet node name',
                                       {'name': u'Process Air Inlet Node Name',
                                        'pyname': u'process_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'process air outlet node name',
                                       {'name': u'Process Air Outlet Node Name',
                                        'pyname': u'process_air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'regeneration air inlet node name',
                                       {'name': u'Regeneration Air Inlet Node Name',
                                        'pyname': u'regeneration_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'regeneration fan inlet node name',
                                       {'name': u'Regeneration Fan Inlet Node Name',
                                        'pyname': u'regeneration_fan_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LeavingMaximumHumidityRatioSetpoint',
                                                            u'SystemNodeMaximumHumidityRatioSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'leaving maximum humidity ratio setpoint',
                                       {'name': u'Leaving Maximum Humidity Ratio Setpoint',
                                        'pyname': u'leaving_maximum_humidity_ratio_setpoint',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'nominal process air flow rate',
                                       {'name': u'Nominal Process Air Flow Rate',
                                        'pyname': u'nominal_process_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'nominal process air velocity',
                                       {'name': u'Nominal Process Air Velocity',
                                        'pyname': u'nominal_process_air_velocity',
                                        'minimum>': 0.0,
                                        'maximum': 6.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'rotor power',
                                       {'name': u'Rotor Power',
                                        'pyname': u'rotor_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'regeneration coil object type',
                                       {'name': u'Regeneration Coil Object Type',
                                        'pyname': u'regeneration_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'regeneration coil name',
                                       {'name': u'Regeneration Coil Name',
                                        'pyname': u'regeneration_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration fan object type',
                                       {'name': u'Regeneration Fan Object Type',
                                        'pyname': u'regeneration_fan_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:VariableVolume',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'regeneration fan name',
                                       {'name': u'Regeneration Fan Name',
                                        'pyname': u'regeneration_fan_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'performance model type',
                                       {'name': u'Performance Model Type',
                                        'pyname': u'performance_model_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Default',
                                                            u'UserCurves'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'leaving dry-bulb function of entering dry-bulb and humidity ratio curve name',
                                       {'name': u'Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name',
                                        'pyname': u'leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'leaving dry-bulb function of air velocity curve name',
                                       {'name': u'Leaving Dry-Bulb Function of Air Velocity Curve Name',
                                        'pyname': u'leaving_drybulb_function_of_air_velocity_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'leaving humidity ratio function of entering dry-bulb and humidity ratio curve name',
                                       {'name': u'Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name',
                                        'pyname': u'leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'leaving humidity ratio function of air velocity curve name',
                                       {'name': u'Leaving Humidity Ratio Function of Air Velocity Curve Name',
                                        'pyname': u'leaving_humidity_ratio_function_of_air_velocity_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration energy function of entering dry-bulb and humidity ratio curve name',
                                       {'name': u'Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name',
                                        'pyname': u'regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration energy function of air velocity curve name',
                                       {'name': u'Regeneration Energy Function of Air Velocity Curve Name',
                                        'pyname': u'regeneration_energy_function_of_air_velocity_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration velocity function of entering dry-bulb and humidity ratio curve name',
                                       {'name': u'Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name',
                                        'pyname': u'regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration velocity function of air velocity curve name',
                                       {'name': u'Regeneration Velocity Function of Air Velocity Curve Name',
                                        'pyname': u'regeneration_velocity_function_of_air_velocity_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nominal regeneration temperature',
                                       {'name': u'Nominal Regeneration Temperature',
                                        'pyname': u'nominal_regeneration_temperature',
                                        'maximum': 250.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 40.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'Humidifiers and Dehumidifiers',
               'min-fields': 0,
               'name': u'Dehumidifier:Desiccant:NoFans',
               'pyname': u'DehumidifierDesiccantNoFans',
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

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

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
    def process_air_inlet_node_name(self):
        """field `Process Air Inlet Node Name`

        |  This is the node entering the process side of the desiccant wheel.

        Args:
            value (str): value for IDD Field `Process Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `process_air_inlet_node_name` or None if not set

        """
        return self["Process Air Inlet Node Name"]

    @process_air_inlet_node_name.setter
    def process_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Process Air Inlet Node Name`"""
        self["Process Air Inlet Node Name"] = value

    @property
    def process_air_outlet_node_name(self):
        """field `Process Air Outlet Node Name`

        |  This is the node leaving the process side of the desiccant wheel.

        Args:
            value (str): value for IDD Field `Process Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `process_air_outlet_node_name` or None if not set

        """
        return self["Process Air Outlet Node Name"]

    @process_air_outlet_node_name.setter
    def process_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Process Air Outlet Node Name`"""
        self["Process Air Outlet Node Name"] = value

    @property
    def regeneration_air_inlet_node_name(self):
        """field `Regeneration Air Inlet Node Name`

        |  This is the node entering the regeneration side of the desiccant wheel
        |  after the regeneration coil.

        Args:
            value (str): value for IDD Field `Regeneration Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_inlet_node_name` or None if not set

        """
        return self["Regeneration Air Inlet Node Name"]

    @regeneration_air_inlet_node_name.setter
    def regeneration_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Regeneration Air Inlet Node Name`"""
        self["Regeneration Air Inlet Node Name"] = value

    @property
    def regeneration_fan_inlet_node_name(self):
        """field `Regeneration Fan Inlet Node Name`

        |  Node for air entering the regeneration fan, mass flow is set
        |  by the desiccant dehumidifier module.

        Args:
            value (str): value for IDD Field `Regeneration Fan Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_fan_inlet_node_name` or None if not set

        """
        return self["Regeneration Fan Inlet Node Name"]

    @regeneration_fan_inlet_node_name.setter
    def regeneration_fan_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Regeneration Fan Inlet Node Name`"""
        self["Regeneration Fan Inlet Node Name"] = value

    @property
    def control_type(self):
        """field `Control Type`

        |  Type of setpoint control:
        |  LeavingMaximumHumidityRatioSetpoint means that the unit is controlled
        |  to deliver air at the Leaving Max Humidity Ratio Setpoint (see below),
        |  SystemNodeMaximumHumidityRatioSetpoint means that the leaving humidity
        |  ratio setpoint is the System Node Humidity Ratio Max property
        |  of the Process Air Outlet Node.  A Setpoint
        |  object must be used to control this setpoint.
        |  Both control types use bypass dampers to prevent over drying.

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def leaving_maximum_humidity_ratio_setpoint(self):
        """field `Leaving Maximum Humidity Ratio Setpoint`

        |  Fixed setpoint for maximum process air leaving humidity ratio
        |  Applicable only when Control Type = LeavingMaximumHumidityRatioSetpoint.
        |  Units: kgWater/kgDryAir

        Args:
            value (float): value for IDD Field `Leaving Maximum Humidity Ratio Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `leaving_maximum_humidity_ratio_setpoint` or None if not set

        """
        return self["Leaving Maximum Humidity Ratio Setpoint"]

    @leaving_maximum_humidity_ratio_setpoint.setter
    def leaving_maximum_humidity_ratio_setpoint(self, value=None):
        """Corresponds to IDD field `Leaving Maximum Humidity Ratio
        Setpoint`"""
        self["Leaving Maximum Humidity Ratio Setpoint"] = value

    @property
    def nominal_process_air_flow_rate(self):
        """field `Nominal Process Air Flow Rate`

        |  Process air flow rate at nominal conditions
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Nominal Process Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_process_air_flow_rate` or None if not set

        """
        return self["Nominal Process Air Flow Rate"]

    @nominal_process_air_flow_rate.setter
    def nominal_process_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Nominal Process Air Flow Rate`"""
        self["Nominal Process Air Flow Rate"] = value

    @property
    def nominal_process_air_velocity(self):
        """field `Nominal Process Air Velocity`

        |  Process air velocity at nominal flow
        |  When using Performance Model Type of Default, must be 2.032 to 4.064 m/s (400 to 800 fpm)
        |  Units: m/s
        |  value <= 6.0

        Args:
            value (float): value for IDD Field `Nominal Process Air Velocity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_process_air_velocity` or None if not set

        """
        return self["Nominal Process Air Velocity"]

    @nominal_process_air_velocity.setter
    def nominal_process_air_velocity(self, value=None):
        """Corresponds to IDD field `Nominal Process Air Velocity`"""
        self["Nominal Process Air Velocity"] = value

    @property
    def rotor_power(self):
        """field `Rotor Power`

        |  Power input to wheel rotor motor
        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Rotor Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rotor_power` or None if not set

        """
        return self["Rotor Power"]

    @rotor_power.setter
    def rotor_power(self, value=None):
        """Corresponds to IDD field `Rotor Power`"""
        self["Rotor Power"] = value

    @property
    def regeneration_coil_object_type(self):
        """field `Regeneration Coil Object Type`

        |  heating coil type
        |  works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `Regeneration Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_coil_object_type` or None if not set

        """
        return self["Regeneration Coil Object Type"]

    @regeneration_coil_object_type.setter
    def regeneration_coil_object_type(self, value=None):
        """Corresponds to IDD field `Regeneration Coil Object Type`"""
        self["Regeneration Coil Object Type"] = value

    @property
    def regeneration_coil_name(self):
        """field `Regeneration Coil Name`

        |  Name of heating coil object for regeneration air

        Args:
            value (str): value for IDD Field `Regeneration Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_coil_name` or None if not set

        """
        return self["Regeneration Coil Name"]

    @regeneration_coil_name.setter
    def regeneration_coil_name(self, value=None):
        """Corresponds to IDD field `Regeneration Coil Name`"""
        self["Regeneration Coil Name"] = value

    @property
    def regeneration_fan_object_type(self):
        """field `Regeneration Fan Object Type`

        |  Type of fan object for regeneration air.  When using the Default
        |  Performance Model Type (see below), only Fan:VariableVolume is valid.

        Args:
            value (str): value for IDD Field `Regeneration Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_fan_object_type` or None if not set

        """
        return self["Regeneration Fan Object Type"]

    @regeneration_fan_object_type.setter
    def regeneration_fan_object_type(self, value=None):
        """Corresponds to IDD field `Regeneration Fan Object Type`"""
        self["Regeneration Fan Object Type"] = value

    @property
    def regeneration_fan_name(self):
        """field `Regeneration Fan Name`

        |  Name of fan object for regeneration air

        Args:
            value (str): value for IDD Field `Regeneration Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_fan_name` or None if not set

        """
        return self["Regeneration Fan Name"]

    @regeneration_fan_name.setter
    def regeneration_fan_name(self, value=None):
        """Corresponds to IDD field `Regeneration Fan Name`"""
        self["Regeneration Fan Name"] = value

    @property
    def performance_model_type(self):
        """field `Performance Model Type`

        |  Specifies whether the default performance model or user-specified
        |  curves should be used to model the performance.  The default model
        |  is a generic solid desiccant wheel using performance curves of the form:
        |  curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*vel + C7*vel**2
        |  + C8*edb*ew + C9*edb**2*ew**2 + C10*edb*vel + C11*edb**2*vel**2
        |  + C12*ew*vel + C13*ew**2*vel**2 + C14*ALOG(edb) + C15*ALOG(ew) + C16*ALOG(vel)
        |  edb = process entering dry-bulb temperature [C]
        |  ew  = process entering humidity ratio [kgWater/kgDryAir]
        |  vel = process air velocity [m/s]
        |  If UserCurves are specified, then performance is calculated as follows:
        |  Leaving Dry-Bulb = (Leaving Dry-Bulb fTW Curve) * (Leaving Dry-Bulb fV Curve)
        |  Leaving Humidity Ratio = (Leaving Humidity Ratio fTW Curve) * (Leaving Humidity Ratio fV Curve)
        |  Regen Energy = (Regen Energy fTW Curve) * (Regen Energy fV Curve)
        |  Regen Velocity = (Regen Velocity fTW Curve) * (Regen Velocity fV Curve)

        Args:
            value (str): value for IDD Field `Performance Model Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `performance_model_type` or None if not set

        """
        return self["Performance Model Type"]

    @performance_model_type.setter
    def performance_model_type(self, value=None):
        """Corresponds to IDD field `Performance Model Type`"""
        self["Performance Model Type"] = value

    @property
    def leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self):
        """field `Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        |  Leaving dry-bulb of process air as a function of entering dry-bulb
        |  and entering humidity ratio, biquadratic curve
        |  curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        |  edb = process entering dry-bulb temperature [C]
        |  ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self[
            "Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def leaving_drybulb_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        """
        self[
            "Leaving Dry-Bulb Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def leaving_drybulb_function_of_air_velocity_curve_name(self):
        """field `Leaving Dry-Bulb Function of Air Velocity Curve Name`

        |  Leaving dry-bulb of process air as a function of air velocity,
        |  quadratic curve.
        |  curve = C1 + C2*v + C3*v**2
        |  v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Leaving Dry-Bulb Function of Air Velocity Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `leaving_drybulb_function_of_air_velocity_curve_name` or None if not set
        """
        return self["Leaving Dry-Bulb Function of Air Velocity Curve Name"]

    @leaving_drybulb_function_of_air_velocity_curve_name.setter
    def leaving_drybulb_function_of_air_velocity_curve_name(self, value=None):
        """  Corresponds to IDD field `Leaving Dry-Bulb Function of Air Velocity Curve Name`

        """
        self["Leaving Dry-Bulb Function of Air Velocity Curve Name"] = value

    @property
    def leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self):
        """field `Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        |  Leaving humidity ratio of process air as a function of entering dry-bulb
        |  and entering humidity ratio, biquadratic curve
        |  curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        |  edb = process entering dry-bulb temperature [C]
        |  ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self[
            "Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def leaving_humidity_ratio_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        """
        self[
            "Leaving Humidity Ratio Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def leaving_humidity_ratio_function_of_air_velocity_curve_name(self):
        """field `Leaving Humidity Ratio Function of Air Velocity Curve Name`

        |  Leaving humidity ratio of process air as a function of
        |  process air velocity, quadratic curve.
        |  curve = C1 + C2*v + C3*v**2
        |  v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Leaving Humidity Ratio Function of Air Velocity Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `leaving_humidity_ratio_function_of_air_velocity_curve_name` or None if not set

        """
        return self[
            "Leaving Humidity Ratio Function of Air Velocity Curve Name"]

    @leaving_humidity_ratio_function_of_air_velocity_curve_name.setter
    def leaving_humidity_ratio_function_of_air_velocity_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Leaving Humidity Ratio Function of Air
        Velocity Curve Name`"""
        self[
            "Leaving Humidity Ratio Function of Air Velocity Curve Name"] = value

    @property
    def regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self):
        """field `Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        |  Regeneration energy [J/kg of water removed] as a function of
        |  entering dry-bulb and entering humidity ratio, biquadratic curve
        |  curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        |  edb = process entering dry-bulb temperature [C]
        |  ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self[
            "Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def regeneration_energy_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        """
        self[
            "Regeneration Energy Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def regeneration_energy_function_of_air_velocity_curve_name(self):
        """field `Regeneration Energy Function of Air Velocity Curve Name`

        |  Regeneration energy [J/kg of water removed] as a function of
        |  process air velocity, quadratic curve.
        |  curve = C1 + C2*v + C3*v**2
        |  v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Regeneration Energy Function of Air Velocity Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_energy_function_of_air_velocity_curve_name` or None if not set

        """
        return self["Regeneration Energy Function of Air Velocity Curve Name"]

    @regeneration_energy_function_of_air_velocity_curve_name.setter
    def regeneration_energy_function_of_air_velocity_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Regeneration Energy Function of Air
        Velocity Curve Name`"""
        self["Regeneration Energy Function of Air Velocity Curve Name"] = value

    @property
    def regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self):
        """field `Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        |  Regeneration velocity [m/s] as a function of
        |  entering dry-bulb and entering humidity ratio, biquadratic curve
        |  curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew
        |  edb = process entering dry-bulb temperature [C]
        |  ew  = process entering humidity ratio [kgWater/kgDryAir]

        Args:
            value (str): value for IDD Field `Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name` or None if not set
        """
        return self[
            "Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"]

    @regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name.setter
    def regeneration_velocity_function_of_entering_drybulb_and_humidity_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name`

        """
        self[
            "Regeneration Velocity Function of Entering Dry-Bulb and Humidity Ratio Curve Name"] = value

    @property
    def regeneration_velocity_function_of_air_velocity_curve_name(self):
        """field `Regeneration Velocity Function of Air Velocity Curve Name`

        |  Regeneration velocity [m/s] as a function of
        |  process air velocity, quadratic curve.
        |  curve = C1 + C2*v + C3*v**2
        |  v = process air velocity [m/s]

        Args:
            value (str): value for IDD Field `Regeneration Velocity Function of Air Velocity Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_velocity_function_of_air_velocity_curve_name` or None if not set

        """
        return self[
            "Regeneration Velocity Function of Air Velocity Curve Name"]

    @regeneration_velocity_function_of_air_velocity_curve_name.setter
    def regeneration_velocity_function_of_air_velocity_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Regeneration Velocity Function of Air
        Velocity Curve Name`"""
        self[
            "Regeneration Velocity Function of Air Velocity Curve Name"] = value

    @property
    def nominal_regeneration_temperature(self):
        """field `Nominal Regeneration Temperature`

        |  Nominal regen temperature upon which the regen energy modifier
        |  curve is based.  Not used if Default if chosen for the field Performance Mode Type.
        |  121 C is a commonly used value.
        |  Units: C
        |  value >= 40.0
        |  value <= 250.0

        Args:
            value (float): value for IDD Field `Nominal Regeneration Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_regeneration_temperature` or None if not set

        """
        return self["Nominal Regeneration Temperature"]

    @nominal_regeneration_temperature.setter
    def nominal_regeneration_temperature(self, value=None):
        """Corresponds to IDD field `Nominal Regeneration Temperature`"""
        self["Nominal Regeneration Temperature"] = value




class DehumidifierDesiccantSystem(DataObject):

    """ Corresponds to IDD object `Dehumidifier:Desiccant:System`
        This compound object models a desiccant heat exchanger, an optional
        heater, and associated fans. The process air stream is the air which
        is dehumidified. The regeneration air stream is the air which is
        heated to regenerate the desiccant. The desiccant heat exchanger
        transfers both sensible and latent energy between the process and
        regeneration air streams. The desiccant dehumidifier is typically used
        in an AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC.
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
                                      (u'desiccant heat exchanger object type',
                                       {'name': u'Desiccant Heat Exchanger Object Type',
                                        'pyname': u'desiccant_heat_exchanger_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatExchanger:Desiccant:BalancedFlow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'desiccant heat exchanger name',
                                       {'name': u'Desiccant Heat Exchanger Name',
                                        'pyname': u'desiccant_heat_exchanger_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'regeneration air fan object type',
                                       {'name': u'Regeneration Air Fan Object Type',
                                        'pyname': u'regeneration_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'regeneration air fan name',
                                       {'name': u'Regeneration Air Fan Name',
                                        'pyname': u'regeneration_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration air fan placement',
                                       {'name': u'Regeneration Air Fan Placement',
                                        'pyname': u'regeneration_air_fan_placement',
                                        'default': u'DrawThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'regeneration air heater object type',
                                       {'name': u'Regeneration Air Heater Object Type',
                                        'pyname': u'regeneration_air_heater_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'regeneration air heater name',
                                       {'name': u'Regeneration Air Heater Name',
                                        'pyname': u'regeneration_air_heater_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration inlet air setpoint temperature',
                                       {'name': u'Regeneration Inlet Air Setpoint Temperature',
                                        'pyname': u'regeneration_inlet_air_setpoint_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'companion cooling coil object type',
                                       {'name': u'Companion Cooling Coil Object Type',
                                        'pyname': u'companion_cooling_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                            u'Coil:Cooling:DX:TwoStageWithHumidityControlMode'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'companion cooling coil name',
                                       {'name': u'Companion Cooling Coil Name',
                                        'pyname': u'companion_cooling_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'companion cooling coil upstream of dehumidifier process inlet',
                                       {'name': u'Companion Cooling Coil Upstream of Dehumidifier Process Inlet',
                                        'pyname': u'companion_cooling_coil_upstream_of_dehumidifier_process_inlet',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'companion coil regeneration air heating',
                                       {'name': u'Companion Coil Regeneration Air Heating',
                                        'pyname': u'companion_coil_regeneration_air_heating',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'exhaust fan maximum flow rate',
                                       {'name': u'Exhaust Fan Maximum Flow Rate',
                                        'pyname': u'exhaust_fan_maximum_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'exhaust fan maximum power',
                                       {'name': u'Exhaust Fan Maximum Power',
                                        'pyname': u'exhaust_fan_maximum_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'exhaust fan power curve name',
                                       {'name': u'Exhaust Fan Power Curve Name',
                                        'pyname': u'exhaust_fan_power_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Humidifiers and Dehumidifiers',
               'min-fields': 8,
               'name': u'Dehumidifier:Desiccant:System',
               'pyname': u'DehumidifierDesiccantSystem',
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

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

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
    def desiccant_heat_exchanger_object_type(self):
        """field `Desiccant Heat Exchanger Object Type`

        Args:
            value (str): value for IDD Field `Desiccant Heat Exchanger Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `desiccant_heat_exchanger_object_type` or None if not set

        """
        return self["Desiccant Heat Exchanger Object Type"]

    @desiccant_heat_exchanger_object_type.setter
    def desiccant_heat_exchanger_object_type(self, value=None):
        """Corresponds to IDD field `Desiccant Heat Exchanger Object Type`"""
        self["Desiccant Heat Exchanger Object Type"] = value

    @property
    def desiccant_heat_exchanger_name(self):
        """field `Desiccant Heat Exchanger Name`

        Args:
            value (str): value for IDD Field `Desiccant Heat Exchanger Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `desiccant_heat_exchanger_name` or None if not set

        """
        return self["Desiccant Heat Exchanger Name"]

    @desiccant_heat_exchanger_name.setter
    def desiccant_heat_exchanger_name(self, value=None):
        """Corresponds to IDD field `Desiccant Heat Exchanger Name`"""
        self["Desiccant Heat Exchanger Name"] = value

    @property
    def sensor_node_name(self):
        """field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sensor_node_name` or None if not set

        """
        return self["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """Corresponds to IDD field `Sensor Node Name`"""
        self["Sensor Node Name"] = value

    @property
    def regeneration_air_fan_object_type(self):
        """field `Regeneration Air Fan Object Type`

        Args:
            value (str): value for IDD Field `Regeneration Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_fan_object_type` or None if not set

        """
        return self["Regeneration Air Fan Object Type"]

    @regeneration_air_fan_object_type.setter
    def regeneration_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Regeneration Air Fan Object Type`"""
        self["Regeneration Air Fan Object Type"] = value

    @property
    def regeneration_air_fan_name(self):
        """field `Regeneration Air Fan Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_fan_name` or None if not set

        """
        return self["Regeneration Air Fan Name"]

    @regeneration_air_fan_name.setter
    def regeneration_air_fan_name(self, value=None):
        """Corresponds to IDD field `Regeneration Air Fan Name`"""
        self["Regeneration Air Fan Name"] = value

    @property
    def regeneration_air_fan_placement(self):
        """field `Regeneration Air Fan Placement`

        |  Default value: DrawThrough

        Args:
            value (str): value for IDD Field `Regeneration Air Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_fan_placement` or None if not set

        """
        return self["Regeneration Air Fan Placement"]

    @regeneration_air_fan_placement.setter
    def regeneration_air_fan_placement(self, value="DrawThrough"):
        """Corresponds to IDD field `Regeneration Air Fan Placement`"""
        self["Regeneration Air Fan Placement"] = value

    @property
    def regeneration_air_heater_object_type(self):
        """field `Regeneration Air Heater Object Type`

        |  works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `Regeneration Air Heater Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_heater_object_type` or None if not set

        """
        return self["Regeneration Air Heater Object Type"]

    @regeneration_air_heater_object_type.setter
    def regeneration_air_heater_object_type(self, value=None):
        """Corresponds to IDD field `Regeneration Air Heater Object Type`"""
        self["Regeneration Air Heater Object Type"] = value

    @property
    def regeneration_air_heater_name(self):
        """field `Regeneration Air Heater Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Heater Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_heater_name` or None if not set

        """
        return self["Regeneration Air Heater Name"]

    @regeneration_air_heater_name.setter
    def regeneration_air_heater_name(self, value=None):
        """Corresponds to IDD field `Regeneration Air Heater Name`"""
        self["Regeneration Air Heater Name"] = value

    @property
    def regeneration_inlet_air_setpoint_temperature(self):
        """field `Regeneration Inlet Air Setpoint Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Regeneration Inlet Air Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `regeneration_inlet_air_setpoint_temperature` or None if not set

        """
        return self["Regeneration Inlet Air Setpoint Temperature"]

    @regeneration_inlet_air_setpoint_temperature.setter
    def regeneration_inlet_air_setpoint_temperature(self, value=None):
        """Corresponds to IDD field `Regeneration Inlet Air Setpoint
        Temperature`"""
        self["Regeneration Inlet Air Setpoint Temperature"] = value

    @property
    def companion_cooling_coil_object_type(self):
        """field `Companion Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Companion Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `companion_cooling_coil_object_type` or None if not set

        """
        return self["Companion Cooling Coil Object Type"]

    @companion_cooling_coil_object_type.setter
    def companion_cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Companion Cooling Coil Object Type`"""
        self["Companion Cooling Coil Object Type"] = value

    @property
    def companion_cooling_coil_name(self):
        """field `Companion Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Companion Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `companion_cooling_coil_name` or None if not set

        """
        return self["Companion Cooling Coil Name"]

    @companion_cooling_coil_name.setter
    def companion_cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Companion Cooling Coil Name`"""
        self["Companion Cooling Coil Name"] = value

    @property
    def companion_cooling_coil_upstream_of_dehumidifier_process_inlet(self):
        """field `Companion Cooling Coil Upstream of Dehumidifier Process
        Inlet`

        |  Select Yes if the companion cooling coil is located directly upstream
        |  of the desiccant heat exchanger's process air inlet node.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Companion Cooling Coil Upstream of Dehumidifier Process Inlet`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `companion_cooling_coil_upstream_of_dehumidifier_process_inlet` or None if not set

        """
        return self[
            "Companion Cooling Coil Upstream of Dehumidifier Process Inlet"]

    @companion_cooling_coil_upstream_of_dehumidifier_process_inlet.setter
    def companion_cooling_coil_upstream_of_dehumidifier_process_inlet(
            self,
            value="No"):
        """Corresponds to IDD field `Companion Cooling Coil Upstream of
        Dehumidifier Process Inlet`"""
        self[
            "Companion Cooling Coil Upstream of Dehumidifier Process Inlet"] = value

    @property
    def companion_coil_regeneration_air_heating(self):
        """field `Companion Coil Regeneration Air Heating`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Companion Coil Regeneration Air Heating`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `companion_coil_regeneration_air_heating` or None if not set

        """
        return self["Companion Coil Regeneration Air Heating"]

    @companion_coil_regeneration_air_heating.setter
    def companion_coil_regeneration_air_heating(self, value="No"):
        """Corresponds to IDD field `Companion Coil Regeneration Air
        Heating`"""
        self["Companion Coil Regeneration Air Heating"] = value

    @property
    def exhaust_fan_maximum_flow_rate(self):
        """field `Exhaust Fan Maximum Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Exhaust Fan Maximum Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `exhaust_fan_maximum_flow_rate` or None if not set

        """
        return self["Exhaust Fan Maximum Flow Rate"]

    @exhaust_fan_maximum_flow_rate.setter
    def exhaust_fan_maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Exhaust Fan Maximum Flow Rate`"""
        self["Exhaust Fan Maximum Flow Rate"] = value

    @property
    def exhaust_fan_maximum_power(self):
        """field `Exhaust Fan Maximum Power`

        |  Units: W

        Args:
            value (float): value for IDD Field `Exhaust Fan Maximum Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `exhaust_fan_maximum_power` or None if not set

        """
        return self["Exhaust Fan Maximum Power"]

    @exhaust_fan_maximum_power.setter
    def exhaust_fan_maximum_power(self, value=None):
        """Corresponds to IDD field `Exhaust Fan Maximum Power`"""
        self["Exhaust Fan Maximum Power"] = value

    @property
    def exhaust_fan_power_curve_name(self):
        """field `Exhaust Fan Power Curve Name`

        |  Curve object type must be Curve:Quadratic or Curve:Cubic

        Args:
            value (str): value for IDD Field `Exhaust Fan Power Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_fan_power_curve_name` or None if not set

        """
        return self["Exhaust Fan Power Curve Name"]

    @exhaust_fan_power_curve_name.setter
    def exhaust_fan_power_curve_name(self, value=None):
        """Corresponds to IDD field `Exhaust Fan Power Curve Name`"""
        self["Exhaust Fan Power Curve Name"] = value


