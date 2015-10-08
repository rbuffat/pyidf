""" Data objects in group "Refrigeration"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class RefrigerationCase(DataObject):

    """ Corresponds to IDD object `Refrigeration:Case`
        The Refrigeration Case object works in conjunction with a compressor rack, a
        refrigeration system, or a secondary loop to simulate the performance of a
        refrigerated case system. The object calculates the energy use for lights, fans and
        anti-sweat heaters and accounts for the sensible and latent heat exchange with the
        surrounding environment (termed "case credits") which impacts the temperature
        and humidity in the zone where the case is located.
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
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated ambient temperature',
                                       {'name': u'Rated Ambient Temperature',
                                        'pyname': u'rated_ambient_temperature',
                                        'default': 23.9,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated ambient relative humidity',
                                       {'name': u'Rated Ambient Relative Humidity',
                                        'pyname': u'rated_ambient_relative_humidity',
                                        'default': 55.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 100.0,
                                        'unit': u'percent'}),
                                      (u'rated total cooling capacity per unit length',
                                       {'name': u'Rated Total Cooling Capacity per Unit Length',
                                        'pyname': u'rated_total_cooling_capacity_per_unit_length',
                                        'default': 1900.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'rated latent heat ratio',
                                       {'name': u'Rated Latent Heat Ratio',
                                        'pyname': u'rated_latent_heat_ratio',
                                        'default': 0.3,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'rated runtime fraction',
                                       {'name': u'Rated Runtime Fraction',
                                        'pyname': u'rated_runtime_fraction',
                                        'default': 0.85,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'case length',
                                       {'name': u'Case Length',
                                        'pyname': u'case_length',
                                        'default': 3.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'case operating temperature',
                                       {'name': u'Case Operating Temperature',
                                        'pyname': u'case_operating_temperature',
                                        'default': 1.1,
                                        'maximum<': 20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'latent case credit curve type',
                                       {'name': u'Latent Case Credit Curve Type',
                                        'pyname': u'latent_case_credit_curve_type',
                                        'default': u'CaseTemperatureMethod',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'CaseTemperatureMethod',
                                                            u'RelativeHumidityMethod',
                                                            u'DewpointMethod'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'latent case credit curve name',
                                       {'name': u'Latent Case Credit Curve Name',
                                        'pyname': u'latent_case_credit_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'standard case fan power per unit length',
                                       {'name': u'Standard Case Fan Power per Unit Length',
                                        'pyname': u'standard_case_fan_power_per_unit_length',
                                        'default': 75.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'operating case fan power per unit length',
                                       {'name': u'Operating Case Fan Power per Unit Length',
                                        'pyname': u'operating_case_fan_power_per_unit_length',
                                        'default': 75.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'standard case lighting power per unit length',
                                       {'name': u'Standard Case Lighting Power per Unit Length',
                                        'pyname': u'standard_case_lighting_power_per_unit_length',
                                        'default': 90.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'installed case lighting power per unit length',
                                       {'name': u'Installed Case Lighting Power per Unit Length',
                                        'pyname': u'installed_case_lighting_power_per_unit_length',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'case lighting schedule name',
                                       {'name': u'Case Lighting Schedule Name',
                                        'pyname': u'case_lighting_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fraction of lighting energy to case',
                                       {'name': u'Fraction of Lighting Energy to Case',
                                        'pyname': u'fraction_of_lighting_energy_to_case',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'case anti-sweat heater power per unit length',
                                       {'name': u'Case Anti-Sweat Heater Power per Unit Length',
                                        'pyname': u'case_antisweat_heater_power_per_unit_length',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'minimum anti-sweat heater power per unit length',
                                       {'name': u'Minimum Anti-Sweat Heater Power per Unit Length',
                                        'pyname': u'minimum_antisweat_heater_power_per_unit_length',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'anti-sweat heater control type',
                                       {'name': u'Anti-Sweat Heater Control Type',
                                        'pyname': u'antisweat_heater_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Constant',
                                                            u'Linear',
                                                            u'DewpointMethod',
                                                            u'HeatBalanceMethod'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'humidity at zero anti-sweat heater energy',
                                       {'name': u'Humidity at Zero Anti-Sweat Heater Energy',
                                        'pyname': u'humidity_at_zero_antisweat_heater_energy',
                                        'default': -10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'case height',
                                       {'name': u'Case Height',
                                        'pyname': u'case_height',
                                        'default': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'fraction of anti-sweat heater energy to case',
                                       {'name': u'Fraction of Anti-Sweat Heater Energy to Case',
                                        'pyname': u'fraction_of_antisweat_heater_energy_to_case',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'case defrost power per unit length',
                                       {'name': u'Case Defrost Power per Unit Length',
                                        'pyname': u'case_defrost_power_per_unit_length',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'case defrost type',
                                       {'name': u'Case Defrost Type',
                                        'pyname': u'case_defrost_type',
                                        'default': u'OffCycle',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'OffCycle',
                                                            u'HotGas',
                                                            u'Electric',
                                                            u'HotFluid',
                                                            u'HotGasWithTemperatureTermination',
                                                            u'ElectricWithTemperatureTermination',
                                                            u'HotFluidWithTemperatureTermination'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'case defrost schedule name',
                                       {'name': u'Case Defrost Schedule Name',
                                        'pyname': u'case_defrost_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'case defrost drip-down schedule name',
                                       {'name': u'Case Defrost Drip-Down Schedule Name',
                                        'pyname': u'case_defrost_dripdown_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost energy correction curve type',
                                       {'name': u'Defrost Energy Correction Curve Type',
                                        'pyname': u'defrost_energy_correction_curve_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'CaseTemperatureMethod',
                                                            u'RelativeHumidityMethod',
                                                            u'DewpointMethod'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost energy correction curve name',
                                       {'name': u'Defrost Energy Correction Curve Name',
                                        'pyname': u'defrost_energy_correction_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'under case hvac return air fraction',
                                       {'name': u'Under Case HVAC Return Air Fraction',
                                        'pyname': u'under_case_hvac_return_air_fraction',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'refrigerated case restocking schedule name',
                                       {'name': u'Refrigerated Case Restocking Schedule Name',
                                        'pyname': u'refrigerated_case_restocking_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'case credit fraction schedule name',
                                       {'name': u'Case Credit Fraction Schedule Name',
                                        'pyname': u'case_credit_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design evaporator temperature or brine inlet temperature',
                                       {'name': u'Design Evaporator Temperature or Brine Inlet Temperature',
                                        'pyname': u'design_evaporator_temperature_or_brine_inlet_temperature',
                                        'maximum': 40.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'average refrigerant charge inventory',
                                       {'name': u'Average Refrigerant Charge Inventory',
                                        'pyname': u'average_refrigerant_charge_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 28,
               'name': u'Refrigeration:Case',
               'pyname': u'RefrigerationCase',
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
    def zone_name(self):
        """field `Zone Name`

        |  This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def rated_ambient_temperature(self):
        """field `Rated Ambient Temperature`

        |  Units: C
        |  Default value: 23.9

        Args:
            value (float): value for IDD Field `Rated Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_ambient_temperature` or None if not set

        """
        return self["Rated Ambient Temperature"]

    @rated_ambient_temperature.setter
    def rated_ambient_temperature(self, value=23.9):
        """Corresponds to IDD field `Rated Ambient Temperature`"""
        self["Rated Ambient Temperature"] = value

    @property
    def rated_ambient_relative_humidity(self):
        """field `Rated Ambient Relative Humidity`

        |  Units: percent
        |  Default value: 55.0
        |  value < 100.0

        Args:
            value (float): value for IDD Field `Rated Ambient Relative Humidity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_ambient_relative_humidity` or None if not set

        """
        return self["Rated Ambient Relative Humidity"]

    @rated_ambient_relative_humidity.setter
    def rated_ambient_relative_humidity(self, value=55.0):
        """Corresponds to IDD field `Rated Ambient Relative Humidity`"""
        self["Rated Ambient Relative Humidity"] = value

    @property
    def rated_total_cooling_capacity_per_unit_length(self):
        """field `Rated Total Cooling Capacity per Unit Length`

        |  Units: W/m
        |  Default value: 1900.0

        Args:
            value (float): value for IDD Field `Rated Total Cooling Capacity per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_total_cooling_capacity_per_unit_length` or None if not set

        """
        return self["Rated Total Cooling Capacity per Unit Length"]

    @rated_total_cooling_capacity_per_unit_length.setter
    def rated_total_cooling_capacity_per_unit_length(self, value=1900.0):
        """Corresponds to IDD field `Rated Total Cooling Capacity per Unit
        Length`"""
        self["Rated Total Cooling Capacity per Unit Length"] = value

    @property
    def rated_latent_heat_ratio(self):
        """field `Rated Latent Heat Ratio`

        |  Default value: 0.3
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Rated Latent Heat Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_latent_heat_ratio` or None if not set

        """
        return self["Rated Latent Heat Ratio"]

    @rated_latent_heat_ratio.setter
    def rated_latent_heat_ratio(self, value=0.3):
        """Corresponds to IDD field `Rated Latent Heat Ratio`"""
        self["Rated Latent Heat Ratio"] = value

    @property
    def rated_runtime_fraction(self):
        """field `Rated Runtime Fraction`

        |  Default value: 0.85
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Rated Runtime Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_runtime_fraction` or None if not set

        """
        return self["Rated Runtime Fraction"]

    @rated_runtime_fraction.setter
    def rated_runtime_fraction(self, value=0.85):
        """Corresponds to IDD field `Rated Runtime Fraction`"""
        self["Rated Runtime Fraction"] = value

    @property
    def case_length(self):
        """field `Case Length`

        |  Units: m
        |  Default value: 3.0

        Args:
            value (float): value for IDD Field `Case Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `case_length` or None if not set

        """
        return self["Case Length"]

    @case_length.setter
    def case_length(self, value=3.0):
        """Corresponds to IDD field `Case Length`"""
        self["Case Length"] = value

    @property
    def case_operating_temperature(self):
        """field `Case Operating Temperature`

        |  Units: C
        |  Default value: 1.1
        |  value < 20.0

        Args:
            value (float): value for IDD Field `Case Operating Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `case_operating_temperature` or None if not set

        """
        return self["Case Operating Temperature"]

    @case_operating_temperature.setter
    def case_operating_temperature(self, value=1.1):
        """Corresponds to IDD field `Case Operating Temperature`"""
        self["Case Operating Temperature"] = value

    @property
    def latent_case_credit_curve_type(self):
        """field `Latent Case Credit Curve Type`

        |  Default value: CaseTemperatureMethod

        Args:
            value (str): value for IDD Field `Latent Case Credit Curve Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `latent_case_credit_curve_type` or None if not set

        """
        return self["Latent Case Credit Curve Type"]

    @latent_case_credit_curve_type.setter
    def latent_case_credit_curve_type(self, value="CaseTemperatureMethod"):
        """Corresponds to IDD field `Latent Case Credit Curve Type`"""
        self["Latent Case Credit Curve Type"] = value

    @property
    def latent_case_credit_curve_name(self):
        """field `Latent Case Credit Curve Name`

        Args:
            value (str): value for IDD Field `Latent Case Credit Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `latent_case_credit_curve_name` or None if not set

        """
        return self["Latent Case Credit Curve Name"]

    @latent_case_credit_curve_name.setter
    def latent_case_credit_curve_name(self, value=None):
        """Corresponds to IDD field `Latent Case Credit Curve Name`"""
        self["Latent Case Credit Curve Name"] = value

    @property
    def standard_case_fan_power_per_unit_length(self):
        """field `Standard Case Fan Power per Unit Length`

        |  Units: W/m
        |  Default value: 75.0

        Args:
            value (float): value for IDD Field `Standard Case Fan Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `standard_case_fan_power_per_unit_length` or None if not set

        """
        return self["Standard Case Fan Power per Unit Length"]

    @standard_case_fan_power_per_unit_length.setter
    def standard_case_fan_power_per_unit_length(self, value=75.0):
        """Corresponds to IDD field `Standard Case Fan Power per Unit
        Length`"""
        self["Standard Case Fan Power per Unit Length"] = value

    @property
    def operating_case_fan_power_per_unit_length(self):
        """field `Operating Case Fan Power per Unit Length`

        |  Units: W/m
        |  Default value: 75.0

        Args:
            value (float): value for IDD Field `Operating Case Fan Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `operating_case_fan_power_per_unit_length` or None if not set

        """
        return self["Operating Case Fan Power per Unit Length"]

    @operating_case_fan_power_per_unit_length.setter
    def operating_case_fan_power_per_unit_length(self, value=75.0):
        """Corresponds to IDD field `Operating Case Fan Power per Unit
        Length`"""
        self["Operating Case Fan Power per Unit Length"] = value

    @property
    def standard_case_lighting_power_per_unit_length(self):
        """field `Standard Case Lighting Power per Unit Length`

        |  Units: W/m
        |  Default value: 90.0

        Args:
            value (float): value for IDD Field `Standard Case Lighting Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `standard_case_lighting_power_per_unit_length` or None if not set

        """
        return self["Standard Case Lighting Power per Unit Length"]

    @standard_case_lighting_power_per_unit_length.setter
    def standard_case_lighting_power_per_unit_length(self, value=90.0):
        """Corresponds to IDD field `Standard Case Lighting Power per Unit
        Length`"""
        self["Standard Case Lighting Power per Unit Length"] = value

    @property
    def installed_case_lighting_power_per_unit_length(self):
        """field `Installed Case Lighting Power per Unit Length`

        |  default set equal to Standard Case Lighting Power per Unit Length
        |  Units: W/m

        Args:
            value (float): value for IDD Field `Installed Case Lighting Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `installed_case_lighting_power_per_unit_length` or None if not set

        """
        return self["Installed Case Lighting Power per Unit Length"]

    @installed_case_lighting_power_per_unit_length.setter
    def installed_case_lighting_power_per_unit_length(self, value=None):
        """Corresponds to IDD field `Installed Case Lighting Power per Unit
        Length`"""
        self["Installed Case Lighting Power per Unit Length"] = value

    @property
    def case_lighting_schedule_name(self):
        """field `Case Lighting Schedule Name`

        Args:
            value (str): value for IDD Field `Case Lighting Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `case_lighting_schedule_name` or None if not set

        """
        return self["Case Lighting Schedule Name"]

    @case_lighting_schedule_name.setter
    def case_lighting_schedule_name(self, value=None):
        """Corresponds to IDD field `Case Lighting Schedule Name`"""
        self["Case Lighting Schedule Name"] = value

    @property
    def fraction_of_lighting_energy_to_case(self):
        """field `Fraction of Lighting Energy to Case`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Lighting Energy to Case`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_lighting_energy_to_case` or None if not set

        """
        return self["Fraction of Lighting Energy to Case"]

    @fraction_of_lighting_energy_to_case.setter
    def fraction_of_lighting_energy_to_case(self, value=1.0):
        """Corresponds to IDD field `Fraction of Lighting Energy to Case`"""
        self["Fraction of Lighting Energy to Case"] = value

    @property
    def case_antisweat_heater_power_per_unit_length(self):
        """field `Case Anti-Sweat Heater Power per Unit Length`

        |  Units: W/m

        Args:
            value (float): value for IDD Field `Case Anti-Sweat Heater Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `case_antisweat_heater_power_per_unit_length` or None if not set
        """
        return self["Case Anti-Sweat Heater Power per Unit Length"]

    @case_antisweat_heater_power_per_unit_length.setter
    def case_antisweat_heater_power_per_unit_length(self, value=None):
        """  Corresponds to IDD field `Case Anti-Sweat Heater Power per Unit Length`

        """
        self["Case Anti-Sweat Heater Power per Unit Length"] = value

    @property
    def minimum_antisweat_heater_power_per_unit_length(self):
        """field `Minimum Anti-Sweat Heater Power per Unit Length`

        |  This field is only applicable to the Linear, Dewpoint Method, and
        |  Heat Balance Method anti-sweat heater control types
        |  Units: W/m

        Args:
            value (float): value for IDD Field `Minimum Anti-Sweat Heater Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_antisweat_heater_power_per_unit_length` or None if not set
        """
        return self["Minimum Anti-Sweat Heater Power per Unit Length"]

    @minimum_antisweat_heater_power_per_unit_length.setter
    def minimum_antisweat_heater_power_per_unit_length(self, value=None):
        """  Corresponds to IDD field `Minimum Anti-Sweat Heater Power per Unit Length`

        """
        self["Minimum Anti-Sweat Heater Power per Unit Length"] = value

    @property
    def antisweat_heater_control_type(self):
        """field `Anti-Sweat Heater Control Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Anti-Sweat Heater Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `antisweat_heater_control_type` or None if not set
        """
        return self["Anti-Sweat Heater Control Type"]

    @antisweat_heater_control_type.setter
    def antisweat_heater_control_type(self, value="None"):
        """  Corresponds to IDD field `Anti-Sweat Heater Control Type`

        """
        self["Anti-Sweat Heater Control Type"] = value

    @property
    def humidity_at_zero_antisweat_heater_energy(self):
        """field `Humidity at Zero Anti-Sweat Heater Energy`

        |  This field is only applicable to Linear AS heater control type
        |  Zone relative humidity (%) where anti-sweat heater energy is zero
        |  Units: percent
        |  Default value: -10.0

        Args:
            value (float): value for IDD Field `Humidity at Zero Anti-Sweat Heater Energy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_at_zero_antisweat_heater_energy` or None if not set
        """
        return self["Humidity at Zero Anti-Sweat Heater Energy"]

    @humidity_at_zero_antisweat_heater_energy.setter
    def humidity_at_zero_antisweat_heater_energy(self, value=-10.0):
        """  Corresponds to IDD field `Humidity at Zero Anti-Sweat Heater Energy`

        """
        self["Humidity at Zero Anti-Sweat Heater Energy"] = value

    @property
    def case_height(self):
        """field `Case Height`

        |  This field only applicable to Heat Balance Method AS heater control type
        |  Height must be greater than zero if Heat Balance Method AS heater control is selected
        |  Units: m
        |  Default value: 1.5

        Args:
            value (float): value for IDD Field `Case Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `case_height` or None if not set

        """
        return self["Case Height"]

    @case_height.setter
    def case_height(self, value=1.5):
        """Corresponds to IDD field `Case Height`"""
        self["Case Height"] = value

    @property
    def fraction_of_antisweat_heater_energy_to_case(self):
        """field `Fraction of Anti-Sweat Heater Energy to Case`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Anti-Sweat Heater Energy to Case`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_antisweat_heater_energy_to_case` or None if not set
        """
        return self["Fraction of Anti-Sweat Heater Energy to Case"]

    @fraction_of_antisweat_heater_energy_to_case.setter
    def fraction_of_antisweat_heater_energy_to_case(self, value=1.0):
        """  Corresponds to IDD field `Fraction of Anti-Sweat Heater Energy to Case`

        """
        self["Fraction of Anti-Sweat Heater Energy to Case"] = value

    @property
    def case_defrost_power_per_unit_length(self):
        """field `Case Defrost Power per Unit Length`

        |  Used to evaluate load on case as well as power or heat consumption
        |  Units: W/m

        Args:
            value (float): value for IDD Field `Case Defrost Power per Unit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `case_defrost_power_per_unit_length` or None if not set

        """
        return self["Case Defrost Power per Unit Length"]

    @case_defrost_power_per_unit_length.setter
    def case_defrost_power_per_unit_length(self, value=None):
        """Corresponds to IDD field `Case Defrost Power per Unit Length`"""
        self["Case Defrost Power per Unit Length"] = value

    @property
    def case_defrost_type(self):
        """field `Case Defrost Type`

        |  Default value: OffCycle

        Args:
            value (str): value for IDD Field `Case Defrost Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `case_defrost_type` or None if not set

        """
        return self["Case Defrost Type"]

    @case_defrost_type.setter
    def case_defrost_type(self, value="OffCycle"):
        """Corresponds to IDD field `Case Defrost Type`"""
        self["Case Defrost Type"] = value

    @property
    def case_defrost_schedule_name(self):
        """field `Case Defrost Schedule Name`

        |  A case defrost schedule name is required unless case defrost type = None

        Args:
            value (str): value for IDD Field `Case Defrost Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `case_defrost_schedule_name` or None if not set

        """
        return self["Case Defrost Schedule Name"]

    @case_defrost_schedule_name.setter
    def case_defrost_schedule_name(self, value=None):
        """Corresponds to IDD field `Case Defrost Schedule Name`"""
        self["Case Defrost Schedule Name"] = value

    @property
    def case_defrost_dripdown_schedule_name(self):
        """field `Case Defrost Drip-Down Schedule Name`

        |  If left blank, the defrost schedule will be used
        |  The start time for each defrost period in this drip-down schedule should coincide with
        |  the start time for each defrost period in the case defrost schedule (previous input
        |  field).The length of each defrost drip-down period must be greater than or equal to the
        |  corresponding defrost period specified in the case defrost schedule. This extra time
        |  allows the melted frost to drip from the coil before refrigeration is restarted.

        Args:
            value (str): value for IDD Field `Case Defrost Drip-Down Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `case_defrost_dripdown_schedule_name` or None if not set
        """
        return self["Case Defrost Drip-Down Schedule Name"]

    @case_defrost_dripdown_schedule_name.setter
    def case_defrost_dripdown_schedule_name(self, value=None):
        """  Corresponds to IDD field `Case Defrost Drip-Down Schedule Name`

        """
        self["Case Defrost Drip-Down Schedule Name"] = value

    @property
    def defrost_energy_correction_curve_type(self):
        """field `Defrost Energy Correction Curve Type`

        |  Case Temperature, Relative Humidity, and Dewpoint Method are applicable to case defrost
        |  types with temperature termination only.
        |  Default value: None

        Args:
            value (str): value for IDD Field `Defrost Energy Correction Curve Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_energy_correction_curve_type` or None if not set

        """
        return self["Defrost Energy Correction Curve Type"]

    @defrost_energy_correction_curve_type.setter
    def defrost_energy_correction_curve_type(self, value="None"):
        """Corresponds to IDD field `Defrost Energy Correction Curve Type`"""
        self["Defrost Energy Correction Curve Type"] = value

    @property
    def defrost_energy_correction_curve_name(self):
        """field `Defrost Energy Correction Curve Name`

        |  Defrost Energy Correction Curve Name is applicable to case defrost types
        |  with temperature termination only.

        Args:
            value (str): value for IDD Field `Defrost Energy Correction Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_energy_correction_curve_name` or None if not set

        """
        return self["Defrost Energy Correction Curve Name"]

    @defrost_energy_correction_curve_name.setter
    def defrost_energy_correction_curve_name(self, value=None):
        """Corresponds to IDD field `Defrost Energy Correction Curve Name`"""
        self["Defrost Energy Correction Curve Name"] = value

    @property
    def under_case_hvac_return_air_fraction(self):
        """field `Under Case HVAC Return Air Fraction`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Under Case HVAC Return Air Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `under_case_hvac_return_air_fraction` or None if not set

        """
        return self["Under Case HVAC Return Air Fraction"]

    @under_case_hvac_return_air_fraction.setter
    def under_case_hvac_return_air_fraction(self, value=None):
        """Corresponds to IDD field `Under Case HVAC Return Air Fraction`"""
        self["Under Case HVAC Return Air Fraction"] = value

    @property
    def refrigerated_case_restocking_schedule_name(self):
        """field `Refrigerated Case Restocking Schedule Name`

        |  Schedule values should be in units of Watts per unit case length (W/m)
        |  Leave this field blank if no restocking is to be modeled

        Args:
            value (str): value for IDD Field `Refrigerated Case Restocking Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigerated_case_restocking_schedule_name` or None if not set

        """
        return self["Refrigerated Case Restocking Schedule Name"]

    @refrigerated_case_restocking_schedule_name.setter
    def refrigerated_case_restocking_schedule_name(self, value=None):
        """Corresponds to IDD field `Refrigerated Case Restocking Schedule
        Name`"""
        self["Refrigerated Case Restocking Schedule Name"] = value

    @property
    def case_credit_fraction_schedule_name(self):
        """field `Case Credit Fraction Schedule Name`

        |  Schedule values should be from 0 to 1
        |  Leave this field blank if no case credit fraction is to be applied

        Args:
            value (str): value for IDD Field `Case Credit Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `case_credit_fraction_schedule_name` or None if not set

        """
        return self["Case Credit Fraction Schedule Name"]

    @case_credit_fraction_schedule_name.setter
    def case_credit_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Case Credit Fraction Schedule Name`"""
        self["Case Credit Fraction Schedule Name"] = value

    @property
    def design_evaporator_temperature_or_brine_inlet_temperature(self):
        """field `Design Evaporator Temperature or Brine Inlet Temperature`

        |  Required for detailed refrigeration system, not for compressor rack
        |  For a DX system, enter the saturated temperature for refrigerant pressure leaving case
        |  For a brine-cooled cooled (secondary system) case, enter the brine inlet temperature
        |  Default is 5 C less than case operating temperature
        |  Units: C
        |  value >= -70.0
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Design Evaporator Temperature or Brine Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_evaporator_temperature_or_brine_inlet_temperature` or None if not set

        """
        return self["Design Evaporator Temperature or Brine Inlet Temperature"]

    @design_evaporator_temperature_or_brine_inlet_temperature.setter
    def design_evaporator_temperature_or_brine_inlet_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Design Evaporator Temperature or Brine
        Inlet Temperature`"""
        self[
            "Design Evaporator Temperature or Brine Inlet Temperature"] = value

    @property
    def average_refrigerant_charge_inventory(self):
        """field `Average Refrigerant Charge Inventory`

        |  Units: kg/m

        Args:
            value (float): value for IDD Field `Average Refrigerant Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_refrigerant_charge_inventory` or None if not set

        """
        return self["Average Refrigerant Charge Inventory"]

    @average_refrigerant_charge_inventory.setter
    def average_refrigerant_charge_inventory(self, value=None):
        """Corresponds to IDD field `Average Refrigerant Charge Inventory`"""
        self["Average Refrigerant Charge Inventory"] = value




class RefrigerationCompressorRack(DataObject):

    """ Corresponds to IDD object `Refrigeration:CompressorRack`
        Works in conjunction with the refrigeration case and walk-in objects to simulate the
        performance of a refrigerated case system. This object models the electric
        consumption of the rack compressors and the condenser fans. Heat can be rejected
        either outdoors or to a zone. Compressor rack waste heat can also be reclaimed for
        use by an optional air- or water-heating coil (Coil:Heating:Desuperheater and
        Coil:WaterHeating:Desuperheater).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'heat rejection location',
                                       {'name': u'Heat Rejection Location',
                                        'pyname': u'heat_rejection_location',
                                        'default': u'Outdoors',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Outdoors',
                                                            u'Zone'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design compressor rack cop',
                                       {'name': u'Design Compressor Rack COP',
                                        'pyname': u'design_compressor_rack_cop',
                                        'default': 2.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'compressor rack cop function of temperature curve name',
                                       {'name': u'Compressor Rack COP Function of Temperature Curve Name',
                                        'pyname': u'compressor_rack_cop_function_of_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design condenser fan power',
                                       {'name': u'Design Condenser Fan Power',
                                        'pyname': u'design_condenser_fan_power',
                                        'default': 250.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'condenser fan power function of temperature curve name',
                                       {'name': u'Condenser Fan Power Function of Temperature Curve Name',
                                        'pyname': u'condenser_fan_power_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condenser type',
                                       {'name': u'Condenser Type',
                                        'pyname': u'condenser_type',
                                        'default': u'AirCooled',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'AirCooled',
                                                            u'EvaporativelyCooled',
                                                            u'WaterCooled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water-cooled condenser inlet node name',
                                       {'name': u'Water-Cooled Condenser Inlet Node Name',
                                        'pyname': u'watercooled_condenser_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water-cooled condenser outlet node name',
                                       {'name': u'Water-Cooled Condenser Outlet Node Name',
                                        'pyname': u'watercooled_condenser_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water-cooled loop flow type',
                                       {'name': u'Water-Cooled Loop Flow Type',
                                        'pyname': u'watercooled_loop_flow_type',
                                        'default': u'VariableFlow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'VariableFlow',
                                                            u'ConstantFlow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water-cooled condenser outlet temperature schedule name',
                                       {'name': u'Water-Cooled Condenser Outlet Temperature Schedule Name',
                                        'pyname': u'watercooled_condenser_outlet_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'water-cooled condenser design flow rate',
                                       {'name': u'Water-Cooled Condenser Design Flow Rate',
                                        'pyname': u'watercooled_condenser_design_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'water-cooled condenser maximum flow rate',
                                       {'name': u'Water-Cooled Condenser Maximum Flow Rate',
                                        'pyname': u'watercooled_condenser_maximum_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'water-cooled condenser maximum water outlet temperature',
                                       {'name': u'Water-Cooled Condenser Maximum Water Outlet Temperature',
                                        'pyname': u'watercooled_condenser_maximum_water_outlet_temperature',
                                        'default': 55.0,
                                        'maximum': 60.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 10.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'water-cooled condenser minimum water inlet temperature',
                                       {'name': u'Water-Cooled Condenser Minimum Water Inlet Temperature',
                                        'pyname': u'watercooled_condenser_minimum_water_inlet_temperature',
                                        'default': 10.0,
                                        'maximum': 30.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 10.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'evaporative condenser availability schedule name',
                                       {'name': u'Evaporative Condenser Availability Schedule Name',
                                        'pyname': u'evaporative_condenser_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'evaporative condenser effectiveness',
                                       {'name': u'Evaporative Condenser Effectiveness',
                                        'pyname': u'evaporative_condenser_effectiveness',
                                        'default': 0.9,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'evaporative condenser air flow rate',
                                       {'name': u'Evaporative Condenser Air Flow Rate',
                                        'pyname': u'evaporative_condenser_air_flow_rate',
                                        'default': 'Autocalculate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'basin heater capacity',
                                       {'name': u'Basin Heater Capacity',
                                        'pyname': u'basin_heater_capacity',
                                        'default': 200.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'basin heater setpoint temperature',
                                       {'name': u'Basin Heater Setpoint Temperature',
                                        'pyname': u'basin_heater_setpoint_temperature',
                                        'default': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'design evaporative condenser water pump power',
                                       {'name': u'Design Evaporative Condenser Water Pump Power',
                                        'pyname': u'design_evaporative_condenser_water_pump_power',
                                        'default': 1000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'evaporative water supply tank name',
                                       {'name': u'Evaporative Water Supply Tank Name',
                                        'pyname': u'evaporative_water_supply_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condenser air inlet node name',
                                       {'name': u'Condenser Air Inlet Node Name',
                                        'pyname': u'condenser_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'refrigeration case name or walkin name or caseandwalkinlist name',
                                       {'name': u'Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name',
                                        'pyname': u'refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heat rejection zone name',
                                       {'name': u'Heat Rejection Zone Name',
                                        'pyname': u'heat_rejection_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 25,
               'name': u'Refrigeration:CompressorRack',
               'pyname': u'RefrigerationCompressorRack',
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
    def heat_rejection_location(self):
        """field `Heat Rejection Location`

        |  Default value: Outdoors

        Args:
            value (str): value for IDD Field `Heat Rejection Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_rejection_location` or None if not set

        """
        return self["Heat Rejection Location"]

    @heat_rejection_location.setter
    def heat_rejection_location(self, value="Outdoors"):
        """Corresponds to IDD field `Heat Rejection Location`"""
        self["Heat Rejection Location"] = value

    @property
    def design_compressor_rack_cop(self):
        """field `Design Compressor Rack COP`

        |  It is important that this COP correspond to the lowest saturated suction
        |  temperature needed to serve all refrigeration loads
        |  Units: W/W
        |  Default value: 2.0

        Args:
            value (float): value for IDD Field `Design Compressor Rack COP`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_compressor_rack_cop` or None if not set

        """
        return self["Design Compressor Rack COP"]

    @design_compressor_rack_cop.setter
    def design_compressor_rack_cop(self, value=2.0):
        """Corresponds to IDD field `Design Compressor Rack COP`"""
        self["Design Compressor Rack COP"] = value

    @property
    def compressor_rack_cop_function_of_temperature_curve_name(self):
        """field `Compressor Rack COP Function of Temperature Curve Name`

        |  It is important that this COP curve correspond to the lowest saturated suction
        |  temperature needed to serve all refrigeration loads

        Args:
            value (str): value for IDD Field `Compressor Rack COP Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_rack_cop_function_of_temperature_curve_name` or None if not set

        """
        return self["Compressor Rack COP Function of Temperature Curve Name"]

    @compressor_rack_cop_function_of_temperature_curve_name.setter
    def compressor_rack_cop_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Compressor Rack COP Function of
        Temperature Curve Name`"""
        self["Compressor Rack COP Function of Temperature Curve Name"] = value

    @property
    def design_condenser_fan_power(self):
        """field `Design Condenser Fan Power`

        |  Design power for condenser fan(s).
        |  Units: W
        |  Default value: 250.0

        Args:
            value (float): value for IDD Field `Design Condenser Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_condenser_fan_power` or None if not set

        """
        return self["Design Condenser Fan Power"]

    @design_condenser_fan_power.setter
    def design_condenser_fan_power(self, value=250.0):
        """Corresponds to IDD field `Design Condenser Fan Power`"""
        self["Design Condenser Fan Power"] = value

    @property
    def condenser_fan_power_function_of_temperature_curve_name(self):
        """field `Condenser Fan Power Function of Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Condenser Fan Power Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_fan_power_function_of_temperature_curve_name` or None if not set

        """
        return self["Condenser Fan Power Function of Temperature Curve Name"]

    @condenser_fan_power_function_of_temperature_curve_name.setter
    def condenser_fan_power_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Condenser Fan Power Function of
        Temperature Curve Name`"""
        self["Condenser Fan Power Function of Temperature Curve Name"] = value

    @property
    def condenser_type(self):
        """field `Condenser Type`

        |  Applicable only when Heat Rejection Location is Outdoors.
        |  Default value: AirCooled

        Args:
            value (str): value for IDD Field `Condenser Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_type` or None if not set

        """
        return self["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """Corresponds to IDD field `Condenser Type`"""
        self["Condenser Type"] = value

    @property
    def watercooled_condenser_inlet_node_name(self):
        """field `Water-Cooled Condenser Inlet Node Name`


        Args:
            value (str): value for IDD Field `Water-Cooled Condenser Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `watercooled_condenser_inlet_node_name` or None if not set
        """
        return self["Water-Cooled Condenser Inlet Node Name"]

    @watercooled_condenser_inlet_node_name.setter
    def watercooled_condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD field `Water-Cooled Condenser Inlet Node Name`

        """
        self["Water-Cooled Condenser Inlet Node Name"] = value

    @property
    def watercooled_condenser_outlet_node_name(self):
        """field `Water-Cooled Condenser Outlet Node Name`


        Args:
            value (str): value for IDD Field `Water-Cooled Condenser Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `watercooled_condenser_outlet_node_name` or None if not set
        """
        return self["Water-Cooled Condenser Outlet Node Name"]

    @watercooled_condenser_outlet_node_name.setter
    def watercooled_condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD field `Water-Cooled Condenser Outlet Node Name`

        """
        self["Water-Cooled Condenser Outlet Node Name"] = value

    @property
    def watercooled_loop_flow_type(self):
        """field `Water-Cooled Loop Flow Type`

        |  Applicable only when Condenser Type is WaterCooled.
        |  Default value: VariableFlow

        Args:
            value (str): value for IDD Field `Water-Cooled Loop Flow Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `watercooled_loop_flow_type` or None if not set
        """
        return self["Water-Cooled Loop Flow Type"]

    @watercooled_loop_flow_type.setter
    def watercooled_loop_flow_type(self, value="VariableFlow"):
        """  Corresponds to IDD field `Water-Cooled Loop Flow Type`

        """
        self["Water-Cooled Loop Flow Type"] = value

    @property
    def watercooled_condenser_outlet_temperature_schedule_name(self):
        """field `Water-Cooled Condenser Outlet Temperature Schedule Name`

        |  Applicable only when loop Flow type is VariableFlow.

        Args:
            value (str): value for IDD Field `Water-Cooled Condenser Outlet Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `watercooled_condenser_outlet_temperature_schedule_name` or None if not set
        """
        return self["Water-Cooled Condenser Outlet Temperature Schedule Name"]

    @watercooled_condenser_outlet_temperature_schedule_name.setter
    def watercooled_condenser_outlet_temperature_schedule_name(
            self,
            value=None):
        """  Corresponds to IDD field `Water-Cooled Condenser Outlet Temperature Schedule Name`

        """
        self["Water-Cooled Condenser Outlet Temperature Schedule Name"] = value

    @property
    def watercooled_condenser_design_flow_rate(self):
        """field `Water-Cooled Condenser Design Flow Rate`

        |  Applicable only when loop flow type is ConstantFlow.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watercooled_condenser_design_flow_rate` or None if not set
        """
        return self["Water-Cooled Condenser Design Flow Rate"]

    @watercooled_condenser_design_flow_rate.setter
    def watercooled_condenser_design_flow_rate(self, value=None):
        """  Corresponds to IDD field `Water-Cooled Condenser Design Flow Rate`

        """
        self["Water-Cooled Condenser Design Flow Rate"] = value

    @property
    def watercooled_condenser_maximum_flow_rate(self):
        """field `Water-Cooled Condenser Maximum Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Maximum Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watercooled_condenser_maximum_flow_rate` or None if not set
        """
        return self["Water-Cooled Condenser Maximum Flow Rate"]

    @watercooled_condenser_maximum_flow_rate.setter
    def watercooled_condenser_maximum_flow_rate(self, value=None):
        """  Corresponds to IDD field `Water-Cooled Condenser Maximum Flow Rate`

        """
        self["Water-Cooled Condenser Maximum Flow Rate"] = value

    @property
    def watercooled_condenser_maximum_water_outlet_temperature(self):
        """field `Water-Cooled Condenser Maximum Water Outlet Temperature`

        |  Units: C
        |  Default value: 55.0
        |  value >= 10.0
        |  value <= 60.0

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Maximum Water Outlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watercooled_condenser_maximum_water_outlet_temperature` or None if not set
        """
        return self["Water-Cooled Condenser Maximum Water Outlet Temperature"]

    @watercooled_condenser_maximum_water_outlet_temperature.setter
    def watercooled_condenser_maximum_water_outlet_temperature(
            self,
            value=55.0):
        """  Corresponds to IDD field `Water-Cooled Condenser Maximum Water Outlet Temperature`

        """
        self["Water-Cooled Condenser Maximum Water Outlet Temperature"] = value

    @property
    def watercooled_condenser_minimum_water_inlet_temperature(self):
        """field `Water-Cooled Condenser Minimum Water Inlet Temperature`

        |  Units: C
        |  Default value: 10.0
        |  value >= 10.0
        |  value <= 30.0

        Args:
            value (float): value for IDD Field `Water-Cooled Condenser Minimum Water Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watercooled_condenser_minimum_water_inlet_temperature` or None if not set
        """
        return self["Water-Cooled Condenser Minimum Water Inlet Temperature"]

    @watercooled_condenser_minimum_water_inlet_temperature.setter
    def watercooled_condenser_minimum_water_inlet_temperature(
            self,
            value=10.0):
        """  Corresponds to IDD field `Water-Cooled Condenser Minimum Water Inlet Temperature`

        """
        self["Water-Cooled Condenser Minimum Water Inlet Temperature"] = value

    @property
    def evaporative_condenser_availability_schedule_name(self):
        """field `Evaporative Condenser Availability Schedule Name`

        |  This field is only used for Condenser Type = EvaporativelyCooled.
        |  Schedule values greater than 0 indicate that evaporative cooling of the
        |  condenser is available. This schedule allows the user to define seasonal
        |  shutdown/draining of the water cooling system in cold climate applications.
        |  For periods with schedule values of 0, the condenser operates as AirCooled.

        Args:
            value (str): value for IDD Field `Evaporative Condenser Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `evaporative_condenser_availability_schedule_name` or None if not set

        """
        return self["Evaporative Condenser Availability Schedule Name"]

    @evaporative_condenser_availability_schedule_name.setter
    def evaporative_condenser_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Evaporative Condenser Availability
        Schedule Name`"""
        self["Evaporative Condenser Availability Schedule Name"] = value

    @property
    def evaporative_condenser_effectiveness(self):
        """field `Evaporative Condenser Effectiveness`

        |  Applicable only for Condenser Type = EvaporativlyCooled.
        |  Units: dimensionless
        |  Default value: 0.9
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Evaporative Condenser Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_condenser_effectiveness` or None if not set

        """
        return self["Evaporative Condenser Effectiveness"]

    @evaporative_condenser_effectiveness.setter
    def evaporative_condenser_effectiveness(self, value=0.9):
        """Corresponds to IDD field `Evaporative Condenser Effectiveness`"""
        self["Evaporative Condenser Effectiveness"] = value

    @property
    def evaporative_condenser_air_flow_rate(self):
        """field `Evaporative Condenser Air Flow Rate`

        |  Applicable only for Condenser Type = EvaporativelyCooled.
        |  Used to calculate evaporative condenser water use.
        |  Units: m3/s
        |  Default value: "Autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Evaporative Condenser Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `evaporative_condenser_air_flow_rate` or None if not set

        """
        return self["Evaporative Condenser Air Flow Rate"]

    @evaporative_condenser_air_flow_rate.setter
    def evaporative_condenser_air_flow_rate(self, value="Autocalculate"):
        """Corresponds to IDD field `Evaporative Condenser Air Flow Rate`"""
        self["Evaporative Condenser Air Flow Rate"] = value

    @property
    def basin_heater_capacity(self):
        """field `Basin Heater Capacity`

        |  This field is only used for Condenser Type = EvaporativelyCooled and for periods
        |  when the evaporatively cooled condenser is available (field Evaporative Condenser Availability
        |  Schedule Name). For this situation, the heater heats the basin water when the
        |  outdoor air dry-bulb temperature falls below the setpoint temperature, but
        |  only when the condenser fans are off (i.e., no refrigerated case load).
        |  Units: W/K
        |  Default value: 200.0

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basin_heater_capacity` or None if not set

        """
        return self["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=200.0):
        """Corresponds to IDD field `Basin Heater Capacity`"""
        self["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """field `Basin Heater Setpoint Temperature`

        |  Enter the outdoor dry-bulb temperature at which the basin heater turns on.
        |  Units: C
        |  Default value: 2.0
        |  value >= 2.0

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set

        """
        return self["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """Corresponds to IDD field `Basin Heater Setpoint Temperature`"""
        self["Basin Heater Setpoint Temperature"] = value

    @property
    def design_evaporative_condenser_water_pump_power(self):
        """field `Design Evaporative Condenser Water Pump Power`

        |  Design recirc water pump power for Condenser Type = EvaporativelyCooled.
        |  Applicable only for Condenser Type = EvaporativelyCooled.
        |  Units: W
        |  Default value: 1000.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Evaporative Condenser Water Pump Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `design_evaporative_condenser_water_pump_power` or None if not set

        """
        return self["Design Evaporative Condenser Water Pump Power"]

    @design_evaporative_condenser_water_pump_power.setter
    def design_evaporative_condenser_water_pump_power(self, value=1000.0):
        """Corresponds to IDD field `Design Evaporative Condenser Water Pump
        Power`"""
        self["Design Evaporative Condenser Water Pump Power"] = value

    @property
    def evaporative_water_supply_tank_name(self):
        """field `Evaporative Water Supply Tank Name`

        |  If blank, water supply is from Mains.
        |  Applicable only for Condenser Type = EvaporativelyCooled.

        Args:
            value (str): value for IDD Field `Evaporative Water Supply Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `evaporative_water_supply_tank_name` or None if not set

        """
        return self["Evaporative Water Supply Tank Name"]

    @evaporative_water_supply_tank_name.setter
    def evaporative_water_supply_tank_name(self, value=None):
        """Corresponds to IDD field `Evaporative Water Supply Tank Name`"""
        self["Evaporative Water Supply Tank Name"] = value

    @property
    def condenser_air_inlet_node_name(self):
        """field `Condenser Air Inlet Node Name`

        |  Applicable only when Heat Rejection Location is Outdoors and Condenser Type is
        |  not WaterCooled; otherwise, leave field blank. If field is left blank with
        |  Heat Rejection Location = Outdoors, then the model assumes that the Inlet Air
        |  conditions are the outdoor air conditions for the current timestep
        |  (e.g., no adjustment for height above ground).

        Args:
            value (str): value for IDD Field `Condenser Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_air_inlet_node_name` or None if not set

        """
        return self["Condenser Air Inlet Node Name"]

    @condenser_air_inlet_node_name.setter
    def condenser_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Air Inlet Node Name`"""
        self["Condenser Air Inlet Node Name"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name(self):
        """field `Refrigeration Case Name or WalkIn Name or CaseAndWalkInList
        Name`

        |  Enter the name of a Refrigeration:Case or Refrigeration:Walkin or
        |  Refrigeration:CaseAndWalkinList object.

        Args:
            value (str): value for IDD Field `Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name` or None if not set

        """
        return self[
            "Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name"]

    @refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name.setter
    def refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name(
            self,
            value=None):
        """Corresponds to IDD field `Refrigeration Case Name or WalkIn Name or
        CaseAndWalkInList Name`"""
        self[
            "Refrigeration Case Name or WalkIn Name or CaseAndWalkInList Name"] = value

    @property
    def heat_rejection_zone_name(self):
        """field `Heat Rejection Zone Name`

        |  This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.
        |  Required only if walk-in[s] are connected to this rack
        |  AND the heat rejection location is "Zone"

        Args:
            value (str): value for IDD Field `Heat Rejection Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_rejection_zone_name` or None if not set

        """
        return self["Heat Rejection Zone Name"]

    @heat_rejection_zone_name.setter
    def heat_rejection_zone_name(self, value=None):
        """Corresponds to IDD field `Heat Rejection Zone Name`"""
        self["Heat Rejection Zone Name"] = value




class RefrigerationCaseAndWalkInList(DataObject):

    """ Corresponds to IDD object `Refrigeration:CaseAndWalkInList`
        Provides a list of all the refrigerated cases, walk in coolers, or air chillers
        cooled by a single refrigeration system.  Note that the names of all cases,
        walk-ins ,air chillers, and CaseAndWalkInLists must be unique.  That is, you cannot
        give a list the same name as one of list items. This list may contain a combination
        of case and walk-in names OR a list of air chiller names.  Air chillers
        may not be included in any list that also includes cases or walk-ins.
    """
    _schema = {'extensible-fields': OrderedDict([(u'case or walkin 1 name',
                                                  {'name': u'Case or WalkIn 1 Name',
                                                   'pyname': u'case_or_walkin_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Refrigeration:CaseAndWalkInList',
               'pyname': u'RefrigerationCaseAndWalkInList',
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

    def add_extensible(self,
                       case_or_walkin_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            case_or_walkin_1_name (str): value for IDD Field `Case or WalkIn 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        case_or_walkin_1_name = self.check_value(
            "Case or WalkIn 1 Name",
            case_or_walkin_1_name)
        vals.append(case_or_walkin_1_name)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class RefrigerationCondenserAirCooled(DataObject):

    """ Corresponds to IDD object `Refrigeration:Condenser:AirCooled`
        Air cooled condenser for a refrigeration system (Refrigeration:System).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'rated effective total heat rejection rate curve name',
                                       {'name': u'Rated Effective Total Heat Rejection Rate Curve Name',
                                        'pyname': u'rated_effective_total_heat_rejection_rate_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated subcooling temperature difference',
                                       {'name': u'Rated Subcooling Temperature Difference',
                                        'pyname': u'rated_subcooling_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'condenser fan speed control type',
                                       {'name': u'Condenser Fan Speed Control Type',
                                        'pyname': u'condenser_fan_speed_control_type',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'FixedLinear',
                                                            u'VariableSpeed',
                                                            u'TwoSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'rated fan power',
                                       {'name': u'Rated Fan Power',
                                        'pyname': u'rated_fan_power',
                                        'default': 250.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'minimum fan air flow ratio',
                                       {'name': u'Minimum Fan Air Flow Ratio',
                                        'pyname': u'minimum_fan_air_flow_ratio',
                                        'default': 0.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'air inlet node name or zone name',
                                       {'name': u'Air Inlet Node Name or Zone Name',
                                        'pyname': u'air_inlet_node_name_or_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'condenser refrigerant operating charge inventory',
                                       {'name': u'Condenser Refrigerant Operating Charge Inventory',
                                        'pyname': u'condenser_refrigerant_operating_charge_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate receiver refrigerant inventory',
                                       {'name': u'Condensate Receiver Refrigerant Inventory',
                                        'pyname': u'condensate_receiver_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate piping refrigerant inventory',
                                       {'name': u'Condensate Piping Refrigerant Inventory',
                                        'pyname': u'condensate_piping_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 5,
               'name': u'Refrigeration:Condenser:AirCooled',
               'pyname': u'RefrigerationCondenserAirCooled',
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
    def rated_effective_total_heat_rejection_rate_curve_name(self):
        """field `Rated Effective Total Heat Rejection Rate Curve Name`

        |  Rating as per ARI 460
        |  Be sure the rating corresponds to the correct refrigerant
        |  HeatRejection(W)=C1 +C2(Condensing Temp - Entering Air Temp, deg C)
        |  Will be adjusted for elevation automatically

        Args:
            value (str): value for IDD Field `Rated Effective Total Heat Rejection Rate Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `rated_effective_total_heat_rejection_rate_curve_name` or None if not set

        """
        return self["Rated Effective Total Heat Rejection Rate Curve Name"]

    @rated_effective_total_heat_rejection_rate_curve_name.setter
    def rated_effective_total_heat_rejection_rate_curve_name(self, value=None):
        """Corresponds to IDD field `Rated Effective Total Heat Rejection Rate
        Curve Name`"""
        self["Rated Effective Total Heat Rejection Rate Curve Name"] = value

    @property
    def rated_subcooling_temperature_difference(self):
        """field `Rated Subcooling Temperature Difference`

        |  must correspond to rating given for total heat rejection effect
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Rated Subcooling Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_subcooling_temperature_difference` or None if not set

        """
        return self["Rated Subcooling Temperature Difference"]

    @rated_subcooling_temperature_difference.setter
    def rated_subcooling_temperature_difference(self, value=None):
        """Corresponds to IDD field `Rated Subcooling Temperature
        Difference`"""
        self["Rated Subcooling Temperature Difference"] = value

    @property
    def condenser_fan_speed_control_type(self):
        """field `Condenser Fan Speed Control Type`

        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Condenser Fan Speed Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_fan_speed_control_type` or None if not set

        """
        return self["Condenser Fan Speed Control Type"]

    @condenser_fan_speed_control_type.setter
    def condenser_fan_speed_control_type(self, value="Fixed"):
        """Corresponds to IDD field `Condenser Fan Speed Control Type`"""
        self["Condenser Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """field `Rated Fan Power`

        |  Power for condenser fan(s) corresponding to rated total heat rejection effect.
        |  Units: W
        |  Default value: 250.0

        Args:
            value (float): value for IDD Field `Rated Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_fan_power` or None if not set

        """
        return self["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=250.0):
        """Corresponds to IDD field `Rated Fan Power`"""
        self["Rated Fan Power"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """field `Minimum Fan Air Flow Ratio`

        |  Minimum air flow fraction through condenser fan
        |  Units: dimensionless
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set

        """
        return self["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """Corresponds to IDD field `Minimum Fan Air Flow Ratio`"""
        self["Minimum Fan Air Flow Ratio"] = value

    @property
    def air_inlet_node_name_or_zone_name(self):
        """field `Air Inlet Node Name or Zone Name`

        |  If field is left blank,
        |  then the model assumes that the inlet air
        |  conditions are the outdoor air conditions for the current timestep
        |  (e.g., no adjustment for height above ground).
        |  If the condenser rejects heat to a conditioned zone, enter the zone name here.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name or Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_node_name_or_zone_name` or None if not set

        """
        return self["Air Inlet Node Name or Zone Name"]

    @air_inlet_node_name_or_zone_name.setter
    def air_inlet_node_name_or_zone_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name or Zone Name`"""
        self["Air Inlet Node Name or Zone Name"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """field `Condenser Refrigerant Operating Charge Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set

        """
        return self["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=None):
        """Corresponds to IDD field `Condenser Refrigerant Operating Charge
        Inventory`"""
        self["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """field `Condensate Receiver Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set

        """
        return self["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Receiver Refrigerant
        Inventory`"""
        self["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """field `Condensate Piping Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set

        """
        return self["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Piping Refrigerant
        Inventory`"""
        self["Condensate Piping Refrigerant Inventory"] = value




class RefrigerationCondenserEvaporativeCooled(DataObject):

    """ Corresponds to IDD object `Refrigeration:Condenser:EvaporativeCooled`
        Evaporative-cooled condenser for a refrigeration system (Refrigeration:System).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'rated effective total heat rejection rate',
                                       {'name': u'Rated Effective Total Heat Rejection Rate',
                                        'pyname': u'rated_effective_total_heat_rejection_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated subcooling temperature difference',
                                       {'name': u'Rated Subcooling Temperature Difference',
                                        'pyname': u'rated_subcooling_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'fan speed control type',
                                       {'name': u'Fan Speed Control Type',
                                        'pyname': u'fan_speed_control_type',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'FixedLinear',
                                                            u'VariableSpeed',
                                                            u'TwoSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'rated fan power',
                                       {'name': u'Rated Fan Power',
                                        'pyname': u'rated_fan_power',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'minimum fan air flow ratio',
                                       {'name': u'Minimum Fan Air Flow Ratio',
                                        'pyname': u'minimum_fan_air_flow_ratio',
                                        'default': 0.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'approach temperature constant term',
                                       {'name': u'Approach Temperature Constant Term',
                                        'pyname': u'approach_temperature_constant_term',
                                        'default': 6.63,
                                        'maximum': 20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'approach temperature coefficient 2',
                                       {'name': u'Approach Temperature Coefficient 2',
                                        'pyname': u'approach_temperature_coefficient_2',
                                        'default': 0.468,
                                        'maximum': 20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'approach temperature coefficient 3',
                                       {'name': u'Approach Temperature Coefficient 3',
                                        'pyname': u'approach_temperature_coefficient_3',
                                        'default': 17.93,
                                        'maximum': 30.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'approach temperature coefficient 4',
                                       {'name': u'Approach Temperature Coefficient 4',
                                        'pyname': u'approach_temperature_coefficient_4',
                                        'default': -0.322,
                                        'maximum': 20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -20.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'minimum capacity factor',
                                       {'name': u'Minimum Capacity Factor',
                                        'pyname': u'minimum_capacity_factor',
                                        'default': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'maximum capacity factor',
                                       {'name': u'Maximum Capacity Factor',
                                        'pyname': u'maximum_capacity_factor',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'rated air flow rate',
                                       {'name': u'Rated Air Flow Rate',
                                        'pyname': u'rated_air_flow_rate',
                                        'default': 'autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'basin heater capacity',
                                       {'name': u'Basin Heater Capacity',
                                        'pyname': u'basin_heater_capacity',
                                        'default': 200.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'basin heater setpoint temperature',
                                       {'name': u'Basin Heater Setpoint Temperature',
                                        'pyname': u'basin_heater_setpoint_temperature',
                                        'default': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated water pump power',
                                       {'name': u'Rated Water Pump Power',
                                        'pyname': u'rated_water_pump_power',
                                        'default': 1000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'evaporative water supply tank name',
                                       {'name': u'Evaporative Water Supply Tank Name',
                                        'pyname': u'evaporative_water_supply_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'evaporative condenser availability schedule name',
                                       {'name': u'Evaporative Condenser Availability Schedule Name',
                                        'pyname': u'evaporative_condenser_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'condenser refrigerant operating charge inventory',
                                       {'name': u'Condenser Refrigerant Operating Charge Inventory',
                                        'pyname': u'condenser_refrigerant_operating_charge_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate receiver refrigerant inventory',
                                       {'name': u'Condensate Receiver Refrigerant Inventory',
                                        'pyname': u'condensate_receiver_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate piping refrigerant inventory',
                                       {'name': u'Condensate Piping Refrigerant Inventory',
                                        'pyname': u'condensate_piping_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 10,
               'name': u'Refrigeration:Condenser:EvaporativeCooled',
               'pyname': u'RefrigerationCondenserEvaporativeCooled',
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
    def rated_effective_total_heat_rejection_rate(self):
        """field `Rated Effective Total Heat Rejection Rate`

        |  Rating as per ARI 490
        |  Be sure the rating corresponds to the correct refrigerant
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Effective Total Heat Rejection Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_effective_total_heat_rejection_rate` or None if not set

        """
        return self["Rated Effective Total Heat Rejection Rate"]

    @rated_effective_total_heat_rejection_rate.setter
    def rated_effective_total_heat_rejection_rate(self, value=None):
        """Corresponds to IDD field `Rated Effective Total Heat Rejection
        Rate`"""
        self["Rated Effective Total Heat Rejection Rate"] = value

    @property
    def rated_subcooling_temperature_difference(self):
        """field `Rated Subcooling Temperature Difference`

        |  must correspond to rating given for total heat rejection effect
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Rated Subcooling Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_subcooling_temperature_difference` or None if not set

        """
        return self["Rated Subcooling Temperature Difference"]

    @rated_subcooling_temperature_difference.setter
    def rated_subcooling_temperature_difference(self, value=None):
        """Corresponds to IDD field `Rated Subcooling Temperature
        Difference`"""
        self["Rated Subcooling Temperature Difference"] = value

    @property
    def fan_speed_control_type(self):
        """field `Fan Speed Control Type`

        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Fan Speed Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_speed_control_type` or None if not set

        """
        return self["Fan Speed Control Type"]

    @fan_speed_control_type.setter
    def fan_speed_control_type(self, value="Fixed"):
        """Corresponds to IDD field `Fan Speed Control Type`"""
        self["Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """field `Rated Fan Power`

        |  Power for condenser fan(s) corresponding to rated total heat rejection effect.
        |  Units: W

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
    def minimum_fan_air_flow_ratio(self):
        """field `Minimum Fan Air Flow Ratio`

        |  Minimum air flow fraction through condenser fan
        |  Units: dimensionless
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set

        """
        return self["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """Corresponds to IDD field `Minimum Fan Air Flow Ratio`"""
        self["Minimum Fan Air Flow Ratio"] = value

    @property
    def approach_temperature_constant_term(self):
        """field `Approach Temperature Constant Term`

        |  A1 in delta T = A1 + A2(hrcf) + A3/(hrcf) + A4(Twb)
        |  Units: C
        |  Default value: 6.63
        |  value <= 20.0

        Args:
            value (float): value for IDD Field `Approach Temperature Constant Term`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `approach_temperature_constant_term` or None if not set

        """
        return self["Approach Temperature Constant Term"]

    @approach_temperature_constant_term.setter
    def approach_temperature_constant_term(self, value=6.63):
        """Corresponds to IDD field `Approach Temperature Constant Term`"""
        self["Approach Temperature Constant Term"] = value

    @property
    def approach_temperature_coefficient_2(self):
        """field `Approach Temperature Coefficient 2`

        |  A2 in delta T = A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)
        |  Units: C
        |  Default value: 0.468
        |  value <= 20.0

        Args:
            value (float): value for IDD Field `Approach Temperature Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `approach_temperature_coefficient_2` or None if not set

        """
        return self["Approach Temperature Coefficient 2"]

    @approach_temperature_coefficient_2.setter
    def approach_temperature_coefficient_2(self, value=0.468):
        """Corresponds to IDD field `Approach Temperature Coefficient 2`"""
        self["Approach Temperature Coefficient 2"] = value

    @property
    def approach_temperature_coefficient_3(self):
        """field `Approach Temperature Coefficient 3`

        |  A3 in delta T = A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)
        |  Units: C
        |  Default value: 17.93
        |  value <= 30.0

        Args:
            value (float): value for IDD Field `Approach Temperature Coefficient 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `approach_temperature_coefficient_3` or None if not set

        """
        return self["Approach Temperature Coefficient 3"]

    @approach_temperature_coefficient_3.setter
    def approach_temperature_coefficient_3(self, value=17.93):
        """Corresponds to IDD field `Approach Temperature Coefficient 3`"""
        self["Approach Temperature Coefficient 3"] = value

    @property
    def approach_temperature_coefficient_4(self):
        """field `Approach Temperature Coefficient 4`

        |  A4 in deltaT=A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)
        |  Units: dimensionless
        |  Default value: -0.322
        |  value >= -20.0
        |  value <= 20.0

        Args:
            value (float): value for IDD Field `Approach Temperature Coefficient 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `approach_temperature_coefficient_4` or None if not set

        """
        return self["Approach Temperature Coefficient 4"]

    @approach_temperature_coefficient_4.setter
    def approach_temperature_coefficient_4(self, value=-0.322):
        """Corresponds to IDD field `Approach Temperature Coefficient 4`"""
        self["Approach Temperature Coefficient 4"] = value

    @property
    def minimum_capacity_factor(self):
        """field `Minimum Capacity Factor`

        |  taken from manufacturer's Heat Rejection Capacity Factor Table
        |  Units: dimensionless
        |  Default value: 0.5

        Args:
            value (float): value for IDD Field `Minimum Capacity Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_capacity_factor` or None if not set

        """
        return self["Minimum Capacity Factor"]

    @minimum_capacity_factor.setter
    def minimum_capacity_factor(self, value=0.5):
        """Corresponds to IDD field `Minimum Capacity Factor`"""
        self["Minimum Capacity Factor"] = value

    @property
    def maximum_capacity_factor(self):
        """field `Maximum Capacity Factor`

        |  taken from manufacturer's Heat Rejection Capacity Factor Table
        |  Units: dimensionless
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Maximum Capacity Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_capacity_factor` or None if not set

        """
        return self["Maximum Capacity Factor"]

    @maximum_capacity_factor.setter
    def maximum_capacity_factor(self, value=5.0):
        """Corresponds to IDD field `Maximum Capacity Factor`"""
        self["Maximum Capacity Factor"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  If field is left blank,
        |  then the model assumes that the inlet air
        |  conditions are the outdoor air conditions for the current timestep
        |  (e.g., no adjustment for height above ground).

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
    def rated_air_flow_rate(self):
        """field `Rated Air Flow Rate`

        |  Used to calculate evaporative condenser water use and fan energy use.
        |  Units: m3/s
        |  Default value: "autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Rated Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `rated_air_flow_rate` or None if not set

        """
        return self["Rated Air Flow Rate"]

    @rated_air_flow_rate.setter
    def rated_air_flow_rate(self, value="autocalculate"):
        """Corresponds to IDD field `Rated Air Flow Rate`"""
        self["Rated Air Flow Rate"] = value

    @property
    def basin_heater_capacity(self):
        """field `Basin Heater Capacity`

        |  This field is only used for periods
        |  when the evap condenser is available (field Evaporative Condenser Availability
        |  Schedule). For this situation, the heater heats the basin water when the
        |  outdoor air dry-bulb temperature falls below the set point temperature, but
        |  only when the condenser fans are off (i.e., no refrigerated case load).
        |  Units: W/K
        |  Default value: 200.0

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basin_heater_capacity` or None if not set

        """
        return self["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=200.0):
        """Corresponds to IDD field `Basin Heater Capacity`"""
        self["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """field `Basin Heater Setpoint Temperature`

        |  Enter the outdoor dry-bulb temperature at which the basin heater turns on.
        |  Units: C
        |  Default value: 2.0
        |  value >= 2.0

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set

        """
        return self["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """Corresponds to IDD field `Basin Heater Setpoint Temperature`"""
        self["Basin Heater Setpoint Temperature"] = value

    @property
    def rated_water_pump_power(self):
        """field `Rated Water Pump Power`

        |  Design recirculating water pump power.
        |  Units: W
        |  Default value: 1000.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Rated Water Pump Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `rated_water_pump_power` or None if not set

        """
        return self["Rated Water Pump Power"]

    @rated_water_pump_power.setter
    def rated_water_pump_power(self, value=1000.0):
        """Corresponds to IDD field `Rated Water Pump Power`"""
        self["Rated Water Pump Power"] = value

    @property
    def evaporative_water_supply_tank_name(self):
        """field `Evaporative Water Supply Tank Name`

        |  If blank, water supply is from Mains.

        Args:
            value (str): value for IDD Field `Evaporative Water Supply Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `evaporative_water_supply_tank_name` or None if not set

        """
        return self["Evaporative Water Supply Tank Name"]

    @evaporative_water_supply_tank_name.setter
    def evaporative_water_supply_tank_name(self, value=None):
        """Corresponds to IDD field `Evaporative Water Supply Tank Name`"""
        self["Evaporative Water Supply Tank Name"] = value

    @property
    def evaporative_condenser_availability_schedule_name(self):
        """field `Evaporative Condenser Availability Schedule Name`

        |  Schedule values greater than 0 indicate that evaporative cooling of the
        |  condenser is available. This schedule allows the user to define seasonal
        |  shutdown/draining of the water cooling system in cold climate applications.
        |  For periods with schedule values of 0, the condenser operates as Air Cooled.

        Args:
            value (str): value for IDD Field `Evaporative Condenser Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `evaporative_condenser_availability_schedule_name` or None if not set

        """
        return self["Evaporative Condenser Availability Schedule Name"]

    @evaporative_condenser_availability_schedule_name.setter
    def evaporative_condenser_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Evaporative Condenser Availability
        Schedule Name`"""
        self["Evaporative Condenser Availability Schedule Name"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """field `Condenser Refrigerant Operating Charge Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set

        """
        return self["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=None):
        """Corresponds to IDD field `Condenser Refrigerant Operating Charge
        Inventory`"""
        self["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """field `Condensate Receiver Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set

        """
        return self["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Receiver Refrigerant
        Inventory`"""
        self["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """field `Condensate Piping Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set

        """
        return self["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Piping Refrigerant
        Inventory`"""
        self["Condensate Piping Refrigerant Inventory"] = value




class RefrigerationCondenserWaterCooled(DataObject):

    """ Corresponds to IDD object `Refrigeration:Condenser:WaterCooled`
        Water cooled condenser for a refrigeration system (Refrigeration:System).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'rated effective total heat rejection rate',
                                       {'name': u'Rated Effective Total Heat Rejection Rate',
                                        'pyname': u'rated_effective_total_heat_rejection_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated condensing temperature',
                                       {'name': u'Rated Condensing Temperature',
                                        'pyname': u'rated_condensing_temperature',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated subcooling temperature difference',
                                       {'name': u'Rated Subcooling Temperature Difference',
                                        'pyname': u'rated_subcooling_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'rated water inlet temperature',
                                       {'name': u'Rated Water Inlet Temperature',
                                        'pyname': u'rated_water_inlet_temperature',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'water inlet node name',
                                       {'name': u'Water Inlet Node Name',
                                        'pyname': u'water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water outlet node name',
                                       {'name': u'Water Outlet Node Name',
                                        'pyname': u'water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water-cooled loop flow type',
                                       {'name': u'Water-Cooled Loop Flow Type',
                                        'pyname': u'watercooled_loop_flow_type',
                                        'default': u'VariableFlow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'VariableFlow',
                                                            u'ConstantFlow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water outlet temperature schedule name',
                                       {'name': u'Water Outlet Temperature Schedule Name',
                                        'pyname': u'water_outlet_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'water design flow rate',
                                       {'name': u'Water Design Flow Rate',
                                        'pyname': u'water_design_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'water maximum flow rate',
                                       {'name': u'Water Maximum Flow Rate',
                                        'pyname': u'water_maximum_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'water maximum water outlet temperature',
                                       {'name': u'Water Maximum Water Outlet Temperature',
                                        'pyname': u'water_maximum_water_outlet_temperature',
                                        'default': 55.0,
                                        'maximum': 60.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 10.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'water minimum water inlet temperature',
                                       {'name': u'Water Minimum Water Inlet Temperature',
                                        'pyname': u'water_minimum_water_inlet_temperature',
                                        'default': 10.0,
                                        'maximum': 30.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 10.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'condenser refrigerant operating charge inventory',
                                       {'name': u'Condenser Refrigerant Operating Charge Inventory',
                                        'pyname': u'condenser_refrigerant_operating_charge_inventory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate receiver refrigerant inventory',
                                       {'name': u'Condensate Receiver Refrigerant Inventory',
                                        'pyname': u'condensate_receiver_refrigerant_inventory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate piping refrigerant inventory',
                                       {'name': u'Condensate Piping Refrigerant Inventory',
                                        'pyname': u'condensate_piping_refrigerant_inventory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Refrigeration:Condenser:WaterCooled',
               'pyname': u'RefrigerationCondenserWaterCooled',
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
    def rated_effective_total_heat_rejection_rate(self):
        """field `Rated Effective Total Heat Rejection Rate`

        |  Rating as per ARI 450
        |  Be sure the rating corresponds to the correct refrigerant
        |  not used in calculations, only for identification and output
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Effective Total Heat Rejection Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_effective_total_heat_rejection_rate` or None if not set

        """
        return self["Rated Effective Total Heat Rejection Rate"]

    @rated_effective_total_heat_rejection_rate.setter
    def rated_effective_total_heat_rejection_rate(self, value=None):
        """Corresponds to IDD field `Rated Effective Total Heat Rejection
        Rate`"""
        self["Rated Effective Total Heat Rejection Rate"] = value

    @property
    def rated_condensing_temperature(self):
        """field `Rated Condensing Temperature`

        |  must correspond to rating given for total heat rejection effect
        |  Units: C

        Args:
            value (float): value for IDD Field `Rated Condensing Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_condensing_temperature` or None if not set

        """
        return self["Rated Condensing Temperature"]

    @rated_condensing_temperature.setter
    def rated_condensing_temperature(self, value=None):
        """Corresponds to IDD field `Rated Condensing Temperature`"""
        self["Rated Condensing Temperature"] = value

    @property
    def rated_subcooling_temperature_difference(self):
        """field `Rated Subcooling Temperature Difference`

        |  must correspond to rating given for total heat rejection effect
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Rated Subcooling Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_subcooling_temperature_difference` or None if not set

        """
        return self["Rated Subcooling Temperature Difference"]

    @rated_subcooling_temperature_difference.setter
    def rated_subcooling_temperature_difference(self, value=None):
        """Corresponds to IDD field `Rated Subcooling Temperature
        Difference`"""
        self["Rated Subcooling Temperature Difference"] = value

    @property
    def rated_water_inlet_temperature(self):
        """field `Rated Water Inlet Temperature`

        |  must correspond to rating given for total heat rejection effect
        |  Units: C

        Args:
            value (float): value for IDD Field `Rated Water Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_water_inlet_temperature` or None if not set

        """
        return self["Rated Water Inlet Temperature"]

    @rated_water_inlet_temperature.setter
    def rated_water_inlet_temperature(self, value=None):
        """Corresponds to IDD field `Rated Water Inlet Temperature`"""
        self["Rated Water Inlet Temperature"] = value

    @property
    def water_inlet_node_name(self):
        """field `Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_inlet_node_name` or None if not set

        """
        return self["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Water Inlet Node Name`"""
        self["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """field `Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_outlet_node_name` or None if not set

        """
        return self["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Water Outlet Node Name`"""
        self["Water Outlet Node Name"] = value

    @property
    def watercooled_loop_flow_type(self):
        """field `Water-Cooled Loop Flow Type`

        |  Default value: VariableFlow

        Args:
            value (str): value for IDD Field `Water-Cooled Loop Flow Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `watercooled_loop_flow_type` or None if not set
        """
        return self["Water-Cooled Loop Flow Type"]

    @watercooled_loop_flow_type.setter
    def watercooled_loop_flow_type(self, value="VariableFlow"):
        """  Corresponds to IDD field `Water-Cooled Loop Flow Type`

        """
        self["Water-Cooled Loop Flow Type"] = value

    @property
    def water_outlet_temperature_schedule_name(self):
        """field `Water Outlet Temperature Schedule Name`

        |  Applicable only when loop flow type is Variable Flow.

        Args:
            value (str): value for IDD Field `Water Outlet Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_outlet_temperature_schedule_name` or None if not set

        """
        return self["Water Outlet Temperature Schedule Name"]

    @water_outlet_temperature_schedule_name.setter
    def water_outlet_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Water Outlet Temperature Schedule Name`"""
        self["Water Outlet Temperature Schedule Name"] = value

    @property
    def water_design_flow_rate(self):
        """field `Water Design Flow Rate`

        |  note required units must be converted from L/s as specified in ARI 450-2007
        |  Applicable only when loop flow type is Constant Flow.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Water Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_design_flow_rate` or None if not set

        """
        return self["Water Design Flow Rate"]

    @water_design_flow_rate.setter
    def water_design_flow_rate(self, value=None):
        """Corresponds to IDD field `Water Design Flow Rate`"""
        self["Water Design Flow Rate"] = value

    @property
    def water_maximum_flow_rate(self):
        """field `Water Maximum Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Water Maximum Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_maximum_flow_rate` or None if not set

        """
        return self["Water Maximum Flow Rate"]

    @water_maximum_flow_rate.setter
    def water_maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Water Maximum Flow Rate`"""
        self["Water Maximum Flow Rate"] = value

    @property
    def water_maximum_water_outlet_temperature(self):
        """field `Water Maximum Water Outlet Temperature`

        |  Units: C
        |  Default value: 55.0
        |  value >= 10.0
        |  value <= 60.0

        Args:
            value (float): value for IDD Field `Water Maximum Water Outlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_maximum_water_outlet_temperature` or None if not set

        """
        return self["Water Maximum Water Outlet Temperature"]

    @water_maximum_water_outlet_temperature.setter
    def water_maximum_water_outlet_temperature(self, value=55.0):
        """Corresponds to IDD field `Water Maximum Water Outlet Temperature`"""
        self["Water Maximum Water Outlet Temperature"] = value

    @property
    def water_minimum_water_inlet_temperature(self):
        """field `Water Minimum Water Inlet Temperature`

        |  related to the minimum allowed refrigeration system condensing temperature
        |  Units: C
        |  Default value: 10.0
        |  value >= 10.0
        |  value <= 30.0

        Args:
            value (float): value for IDD Field `Water Minimum Water Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_minimum_water_inlet_temperature` or None if not set

        """
        return self["Water Minimum Water Inlet Temperature"]

    @water_minimum_water_inlet_temperature.setter
    def water_minimum_water_inlet_temperature(self, value=10.0):
        """Corresponds to IDD field `Water Minimum Water Inlet Temperature`"""
        self["Water Minimum Water Inlet Temperature"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """field `Condenser Refrigerant Operating Charge Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set

        """
        return self["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=None):
        """Corresponds to IDD field `Condenser Refrigerant Operating Charge
        Inventory`"""
        self["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """field `Condensate Receiver Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set

        """
        return self["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Receiver Refrigerant
        Inventory`"""
        self["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """field `Condensate Piping Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set

        """
        return self["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Piping Refrigerant
        Inventory`"""
        self["Condensate Piping Refrigerant Inventory"] = value




class RefrigerationCondenserCascade(DataObject):

    """ Corresponds to IDD object `Refrigeration:Condenser:Cascade`
        Cascade condenser for a refrigeration system (Refrigeration:System). The cascade
        condenser is unlike the other condenser options because it rejects heat to another,
        higher-temperature, refrigeration system. That is, the cascade condenser acts as a
        heat rejection object for one system, but acts as a refrigeration load for another
        system.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'rated condensing temperature',
                                       {'name': u'Rated Condensing Temperature',
                                        'pyname': u'rated_condensing_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated approach temperature difference',
                                       {'name': u'Rated Approach Temperature Difference',
                                        'pyname': u'rated_approach_temperature_difference',
                                        'default': 3.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'rated effective total heat rejection rate',
                                       {'name': u'Rated Effective Total Heat Rejection Rate',
                                        'pyname': u'rated_effective_total_heat_rejection_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'condensing temperature control type',
                                       {'name': u'Condensing Temperature Control Type',
                                        'pyname': u'condensing_temperature_control_type',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'Float'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'condenser refrigerant operating charge inventory',
                                       {'name': u'Condenser Refrigerant Operating Charge Inventory',
                                        'pyname': u'condenser_refrigerant_operating_charge_inventory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate receiver refrigerant inventory',
                                       {'name': u'Condensate Receiver Refrigerant Inventory',
                                        'pyname': u'condensate_receiver_refrigerant_inventory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'condensate piping refrigerant inventory',
                                       {'name': u'Condensate Piping Refrigerant Inventory',
                                        'pyname': u'condensate_piping_refrigerant_inventory',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Refrigeration:Condenser:Cascade',
               'pyname': u'RefrigerationCondenserCascade',
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
    def rated_condensing_temperature(self):
        """field `Rated Condensing Temperature`

        |  This is the condensing temperature for the lower temperature secondary loop
        |  Units: C

        Args:
            value (float): value for IDD Field `Rated Condensing Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_condensing_temperature` or None if not set

        """
        return self["Rated Condensing Temperature"]

    @rated_condensing_temperature.setter
    def rated_condensing_temperature(self, value=None):
        """Corresponds to IDD field `Rated Condensing Temperature`"""
        self["Rated Condensing Temperature"] = value

    @property
    def rated_approach_temperature_difference(self):
        """field `Rated Approach Temperature Difference`

        |  This is the difference between the condensing and evaporating temperatures
        |  Units: deltaC
        |  Default value: 3.0

        Args:
            value (float): value for IDD Field `Rated Approach Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_approach_temperature_difference` or None if not set

        """
        return self["Rated Approach Temperature Difference"]

    @rated_approach_temperature_difference.setter
    def rated_approach_temperature_difference(self, value=3.0):
        """Corresponds to IDD field `Rated Approach Temperature Difference`"""
        self["Rated Approach Temperature Difference"] = value

    @property
    def rated_effective_total_heat_rejection_rate(self):
        """field `Rated Effective Total Heat Rejection Rate`

        |  used for identification and rough system size error checking
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Effective Total Heat Rejection Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_effective_total_heat_rejection_rate` or None if not set

        """
        return self["Rated Effective Total Heat Rejection Rate"]

    @rated_effective_total_heat_rejection_rate.setter
    def rated_effective_total_heat_rejection_rate(self, value=None):
        """Corresponds to IDD field `Rated Effective Total Heat Rejection
        Rate`"""
        self["Rated Effective Total Heat Rejection Rate"] = value

    @property
    def condensing_temperature_control_type(self):
        """field `Condensing Temperature Control Type`

        |  Fixed keeps condensing temperature constant
        |  Float sets the condensing temperature according to
        |  the other loads on the higher temperature system
        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Condensing Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condensing_temperature_control_type` or None if not set

        """
        return self["Condensing Temperature Control Type"]

    @condensing_temperature_control_type.setter
    def condensing_temperature_control_type(self, value="Fixed"):
        """Corresponds to IDD field `Condensing Temperature Control Type`"""
        self["Condensing Temperature Control Type"] = value

    @property
    def condenser_refrigerant_operating_charge_inventory(self):
        """field `Condenser Refrigerant Operating Charge Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condenser Refrigerant Operating Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condenser_refrigerant_operating_charge_inventory` or None if not set

        """
        return self["Condenser Refrigerant Operating Charge Inventory"]

    @condenser_refrigerant_operating_charge_inventory.setter
    def condenser_refrigerant_operating_charge_inventory(self, value=None):
        """Corresponds to IDD field `Condenser Refrigerant Operating Charge
        Inventory`"""
        self["Condenser Refrigerant Operating Charge Inventory"] = value

    @property
    def condensate_receiver_refrigerant_inventory(self):
        """field `Condensate Receiver Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Receiver Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_receiver_refrigerant_inventory` or None if not set

        """
        return self["Condensate Receiver Refrigerant Inventory"]

    @condensate_receiver_refrigerant_inventory.setter
    def condensate_receiver_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Receiver Refrigerant
        Inventory`"""
        self["Condensate Receiver Refrigerant Inventory"] = value

    @property
    def condensate_piping_refrigerant_inventory(self):
        """field `Condensate Piping Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Condensate Piping Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensate_piping_refrigerant_inventory` or None if not set

        """
        return self["Condensate Piping Refrigerant Inventory"]

    @condensate_piping_refrigerant_inventory.setter
    def condensate_piping_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Condensate Piping Refrigerant
        Inventory`"""
        self["Condensate Piping Refrigerant Inventory"] = value




class RefrigerationGasCoolerAirCooled(DataObject):

    """ Corresponds to IDD object `Refrigeration:GasCooler:AirCooled`
        The transcritical refrigeration system requires a single gas cooler to reject the
        system heat.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'rated total heat rejection rate curve name',
                                       {'name': u'Rated Total Heat Rejection Rate Curve Name',
                                        'pyname': u'rated_total_heat_rejection_rate_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gas cooler fan speed control type',
                                       {'name': u'Gas Cooler Fan Speed Control Type',
                                        'pyname': u'gas_cooler_fan_speed_control_type',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'FixedLinear',
                                                            u'VariableSpeed',
                                                            u'TwoSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'rated fan power',
                                       {'name': u'Rated Fan Power',
                                        'pyname': u'rated_fan_power',
                                        'default': 5000.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'minimum fan air flow ratio',
                                       {'name': u'Minimum Fan Air Flow Ratio',
                                        'pyname': u'minimum_fan_air_flow_ratio',
                                        'default': 0.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'transition temperature',
                                       {'name': u'Transition Temperature',
                                        'pyname': u'transition_temperature',
                                        'default': 27.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'transcritical approach temperature',
                                       {'name': u'Transcritical Approach Temperature',
                                        'pyname': u'transcritical_approach_temperature',
                                        'default': 3.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'subcritical temperature difference',
                                       {'name': u'Subcritical Temperature Difference',
                                        'pyname': u'subcritical_temperature_difference',
                                        'default': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'minimum condensing temperature',
                                       {'name': u'Minimum Condensing Temperature',
                                        'pyname': u'minimum_condensing_temperature',
                                        'default': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'gas cooler refrigerant operating charge inventory',
                                       {'name': u'Gas Cooler Refrigerant Operating Charge Inventory',
                                        'pyname': u'gas_cooler_refrigerant_operating_charge_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'gas cooler receiver refrigerant inventory',
                                       {'name': u'Gas Cooler Receiver Refrigerant Inventory',
                                        'pyname': u'gas_cooler_receiver_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'gas cooler outlet piping refrigerant inventory',
                                       {'name': u'Gas Cooler Outlet Piping Refrigerant Inventory',
                                        'pyname': u'gas_cooler_outlet_piping_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Refrigeration:GasCooler:AirCooled',
               'pyname': u'RefrigerationGasCoolerAirCooled',
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
    def rated_total_heat_rejection_rate_curve_name(self):
        """field `Rated Total Heat Rejection Rate Curve Name`

        |  Be sure the rating corresponds to the correct refrigerant (R744)
        |  HeatRejection(W)=C1 +C2(Gas Cooler Outlet Temp - Entering Air Temp, deg C)
        |  Will be adjusted for elevation automatically

        Args:
            value (str): value for IDD Field `Rated Total Heat Rejection Rate Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `rated_total_heat_rejection_rate_curve_name` or None if not set

        """
        return self["Rated Total Heat Rejection Rate Curve Name"]

    @rated_total_heat_rejection_rate_curve_name.setter
    def rated_total_heat_rejection_rate_curve_name(self, value=None):
        """Corresponds to IDD field `Rated Total Heat Rejection Rate Curve
        Name`"""
        self["Rated Total Heat Rejection Rate Curve Name"] = value

    @property
    def gas_cooler_fan_speed_control_type(self):
        """field `Gas Cooler Fan Speed Control Type`

        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Gas Cooler Fan Speed Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `gas_cooler_fan_speed_control_type` or None if not set

        """
        return self["Gas Cooler Fan Speed Control Type"]

    @gas_cooler_fan_speed_control_type.setter
    def gas_cooler_fan_speed_control_type(self, value="Fixed"):
        """Corresponds to IDD field `Gas Cooler Fan Speed Control Type`"""
        self["Gas Cooler Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """field `Rated Fan Power`

        |  Power for gas cooler fan(s) corresponding to rated total heat rejection effect.
        |  Units: W
        |  Default value: 5000.0

        Args:
            value (float): value for IDD Field `Rated Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_fan_power` or None if not set

        """
        return self["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=5000.0):
        """Corresponds to IDD field `Rated Fan Power`"""
        self["Rated Fan Power"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """field `Minimum Fan Air Flow Ratio`

        |  Minimum air flow fraction through gas cooler fan
        |  Units: dimensionless
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set

        """
        return self["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """Corresponds to IDD field `Minimum Fan Air Flow Ratio`"""
        self["Minimum Fan Air Flow Ratio"] = value

    @property
    def transition_temperature(self):
        """field `Transition Temperature`

        |  Temperature at which system transitions between subcritical and transcritical operation.
        |  Units: C
        |  Default value: 27.0

        Args:
            value (float): value for IDD Field `Transition Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `transition_temperature` or None if not set

        """
        return self["Transition Temperature"]

    @transition_temperature.setter
    def transition_temperature(self, value=27.0):
        """Corresponds to IDD field `Transition Temperature`"""
        self["Transition Temperature"] = value

    @property
    def transcritical_approach_temperature(self):
        """field `Transcritical Approach Temperature`

        |  Temperature difference between the CO2 exiting the gas cooler and the air entering the
        |  gas cooler during transcritical operation.
        |  Units: deltaC
        |  Default value: 3.0

        Args:
            value (float): value for IDD Field `Transcritical Approach Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `transcritical_approach_temperature` or None if not set

        """
        return self["Transcritical Approach Temperature"]

    @transcritical_approach_temperature.setter
    def transcritical_approach_temperature(self, value=3.0):
        """Corresponds to IDD field `Transcritical Approach Temperature`"""
        self["Transcritical Approach Temperature"] = value

    @property
    def subcritical_temperature_difference(self):
        """field `Subcritical Temperature Difference`

        |  Temperature difference between the saturated condensing temperature and the air
        |  temperature during subcritical operation.
        |  Units: deltaC
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Subcritical Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `subcritical_temperature_difference` or None if not set

        """
        return self["Subcritical Temperature Difference"]

    @subcritical_temperature_difference.setter
    def subcritical_temperature_difference(self, value=10.0):
        """Corresponds to IDD field `Subcritical Temperature Difference`"""
        self["Subcritical Temperature Difference"] = value

    @property
    def minimum_condensing_temperature(self):
        """field `Minimum Condensing Temperature`

        |  Minimum saturated condensing temperature during subcritical operation.
        |  Units: C
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Minimum Condensing Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_condensing_temperature` or None if not set

        """
        return self["Minimum Condensing Temperature"]

    @minimum_condensing_temperature.setter
    def minimum_condensing_temperature(self, value=10.0):
        """Corresponds to IDD field `Minimum Condensing Temperature`"""
        self["Minimum Condensing Temperature"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  If field is left blank,
        |  then the model assumes that the inlet air
        |  conditions are the outdoor air conditions for the current timestep
        |  (e.g., no adjustment for height above ground).

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
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def gas_cooler_refrigerant_operating_charge_inventory(self):
        """field `Gas Cooler Refrigerant Operating Charge Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Gas Cooler Refrigerant Operating Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_cooler_refrigerant_operating_charge_inventory` or None if not set

        """
        return self["Gas Cooler Refrigerant Operating Charge Inventory"]

    @gas_cooler_refrigerant_operating_charge_inventory.setter
    def gas_cooler_refrigerant_operating_charge_inventory(self, value=None):
        """Corresponds to IDD field `Gas Cooler Refrigerant Operating Charge
        Inventory`"""
        self["Gas Cooler Refrigerant Operating Charge Inventory"] = value

    @property
    def gas_cooler_receiver_refrigerant_inventory(self):
        """field `Gas Cooler Receiver Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Gas Cooler Receiver Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_cooler_receiver_refrigerant_inventory` or None if not set

        """
        return self["Gas Cooler Receiver Refrigerant Inventory"]

    @gas_cooler_receiver_refrigerant_inventory.setter
    def gas_cooler_receiver_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Gas Cooler Receiver Refrigerant
        Inventory`"""
        self["Gas Cooler Receiver Refrigerant Inventory"] = value

    @property
    def gas_cooler_outlet_piping_refrigerant_inventory(self):
        """field `Gas Cooler Outlet Piping Refrigerant Inventory`

        |  optional input
        |  Units: kg

        Args:
            value (float): value for IDD Field `Gas Cooler Outlet Piping Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gas_cooler_outlet_piping_refrigerant_inventory` or None if not set

        """
        return self["Gas Cooler Outlet Piping Refrigerant Inventory"]

    @gas_cooler_outlet_piping_refrigerant_inventory.setter
    def gas_cooler_outlet_piping_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Gas Cooler Outlet Piping Refrigerant
        Inventory`"""
        self["Gas Cooler Outlet Piping Refrigerant Inventory"] = value




class RefrigerationTransferLoadList(DataObject):

    """ Corresponds to IDD object `Refrigeration:TransferLoadList`
        A refrigeration system may provide cooling to other, secondary, systems through
        either a secondary loop or a cascade condenser. If multiple transfer loads are served
        by a single primary system, use this list to group them together for reference by the
        primary system (see the field "Refrigeration Transfer Load or TransferLoad List Name"
        in the Refrigeration:System object).
    """
    _schema = {'extensible-fields': OrderedDict([(u'cascade condenser name or secondary system 1 name',
                                                  {'name': u'Cascade Condenser Name or Secondary System 1 Name',
                                                   'pyname': u'cascade_condenser_name_or_secondary_system_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Refrigeration:TransferLoadList',
               'pyname': u'RefrigerationTransferLoadList',
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

    def add_extensible(self,
                       cascade_condenser_name_or_secondary_system_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            cascade_condenser_name_or_secondary_system_1_name (str): value for IDD Field `Cascade Condenser Name or Secondary System 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        cascade_condenser_name_or_secondary_system_1_name = self.check_value(
            "Cascade Condenser Name or Secondary System 1 Name",
            cascade_condenser_name_or_secondary_system_1_name)
        vals.append(cascade_condenser_name_or_secondary_system_1_name)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class RefrigerationSubcooler(DataObject):

    """ Corresponds to IDD object `Refrigeration:Subcooler`
        Two types of subcoolers are modeled by the detailed refrigeration system.  The
        liquid suction heat exchanger uses cool suction gas to subcool the hot condensate
        after it leaves the condenser and before it reaches the thermal expansion valve.
        A mechanical subcooler is used to transfer cooling capacity from one refrigeration
        system to another.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'subcooler type',
                                       {'name': u'Subcooler Type',
                                        'pyname': u'subcooler_type',
                                        'default': u'LiquidSuction',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Mechanical',
                                                            u'LiquidSuction'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'liquid suction design subcooling temperature difference',
                                       {'name': u'Liquid Suction Design Subcooling Temperature Difference',
                                        'pyname': u'liquid_suction_design_subcooling_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'design liquid inlet temperature',
                                       {'name': u'Design Liquid Inlet Temperature',
                                        'pyname': u'design_liquid_inlet_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'design vapor inlet temperature',
                                       {'name': u'Design Vapor Inlet Temperature',
                                        'pyname': u'design_vapor_inlet_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'capacity-providing system',
                                       {'name': u'Capacity-Providing System',
                                        'pyname': u'capacityproviding_system',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outlet control temperature',
                                       {'name': u'Outlet Control Temperature',
                                        'pyname': u'outlet_control_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 5,
               'name': u'Refrigeration:Subcooler',
               'pyname': u'RefrigerationSubcooler',
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
    def subcooler_type(self):
        """field `Subcooler Type`

        |  plan to add ambient subcoolers at future time
        |  Default value: LiquidSuction

        Args:
            value (str): value for IDD Field `Subcooler Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `subcooler_type` or None if not set

        """
        return self["Subcooler Type"]

    @subcooler_type.setter
    def subcooler_type(self, value="LiquidSuction"):
        """Corresponds to IDD field `Subcooler Type`"""
        self["Subcooler Type"] = value

    @property
    def liquid_suction_design_subcooling_temperature_difference(self):
        """field `Liquid Suction Design Subcooling Temperature Difference`

        |  Applicable only and required for liquid suction heat exchangers
        |  design liquid suction subcooling
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Liquid Suction Design Subcooling Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `liquid_suction_design_subcooling_temperature_difference` or None if not set

        """
        return self["Liquid Suction Design Subcooling Temperature Difference"]

    @liquid_suction_design_subcooling_temperature_difference.setter
    def liquid_suction_design_subcooling_temperature_difference(
            self,
            value=None):
        """Corresponds to IDD field `Liquid Suction Design Subcooling
        Temperature Difference`"""
        self["Liquid Suction Design Subcooling Temperature Difference"] = value

    @property
    def design_liquid_inlet_temperature(self):
        """field `Design Liquid Inlet Temperature`

        |  design inlet temperature on liquid side
        |  Applicable only and required for liquid suction heat exchangers (LSHX)
        |  Units: C

        Args:
            value (float): value for IDD Field `Design Liquid Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_liquid_inlet_temperature` or None if not set

        """
        return self["Design Liquid Inlet Temperature"]

    @design_liquid_inlet_temperature.setter
    def design_liquid_inlet_temperature(self, value=None):
        """Corresponds to IDD field `Design Liquid Inlet Temperature`"""
        self["Design Liquid Inlet Temperature"] = value

    @property
    def design_vapor_inlet_temperature(self):
        """field `Design Vapor Inlet Temperature`

        |  design inlet temperature on vapor side
        |  Applicable only and required for liquid suction heat exchangers (LSHX)
        |  Design vapor inlet temperature must be less than or equal to
        |  the Liquid inlet design temp
        |  Units: C

        Args:
            value (float): value for IDD Field `Design Vapor Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_vapor_inlet_temperature` or None if not set

        """
        return self["Design Vapor Inlet Temperature"]

    @design_vapor_inlet_temperature.setter
    def design_vapor_inlet_temperature(self, value=None):
        """Corresponds to IDD field `Design Vapor Inlet Temperature`"""
        self["Design Vapor Inlet Temperature"] = value

    @property
    def capacityproviding_system(self):
        """field `Capacity-Providing System`

        |  Name of the Detailed Refrigeration System providing cooling capacity
        |  Applicable only and required for mechanical subcoolers

        Args:
            value (str): value for IDD Field `Capacity-Providing System`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `capacityproviding_system` or None if not set
        """
        return self["Capacity-Providing System"]

    @capacityproviding_system.setter
    def capacityproviding_system(self, value=None):
        """  Corresponds to IDD field `Capacity-Providing System`

        """
        self["Capacity-Providing System"] = value

    @property
    def outlet_control_temperature(self):
        """field `Outlet Control Temperature`

        |  Control Temperature Out for subcooled liquid
        |  Applicable only and required for mechanical subcoolers
        |  Units: C

        Args:
            value (float): value for IDD Field `Outlet Control Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outlet_control_temperature` or None if not set

        """
        return self["Outlet Control Temperature"]

    @outlet_control_temperature.setter
    def outlet_control_temperature(self, value=None):
        """Corresponds to IDD field `Outlet Control Temperature`"""
        self["Outlet Control Temperature"] = value




class RefrigerationCompressor(DataObject):

    """ Corresponds to IDD object `Refrigeration:Compressor`
        Refrigeration system compressor. Data is available for many compressors
        in the RefrigerationCompressor.idf dataset
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'refrigeration compressor power curve name',
                                       {'name': u'Refrigeration Compressor Power Curve Name',
                                        'pyname': u'refrigeration_compressor_power_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'refrigeration compressor capacity curve name',
                                       {'name': u'Refrigeration Compressor Capacity Curve Name',
                                        'pyname': u'refrigeration_compressor_capacity_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated superheat',
                                       {'name': u'Rated Superheat',
                                        'pyname': u'rated_superheat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'rated return gas temperature',
                                       {'name': u'Rated Return Gas Temperature',
                                        'pyname': u'rated_return_gas_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated liquid temperature',
                                       {'name': u'Rated Liquid Temperature',
                                        'pyname': u'rated_liquid_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated subcooling',
                                       {'name': u'Rated Subcooling',
                                        'pyname': u'rated_subcooling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'mode of operation',
                                       {'name': u'Mode of Operation',
                                        'pyname': u'mode_of_operation',
                                        'default': u'Subcritical',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Subcritical',
                                                            u'Transcritical'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'transcritical compressor power curve name',
                                       {'name': u'Transcritical Compressor Power Curve Name',
                                        'pyname': u'transcritical_compressor_power_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'transcritical compressor capacity curve name',
                                       {'name': u'Transcritical Compressor Capacity Curve Name',
                                        'pyname': u'transcritical_compressor_capacity_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 6,
               'name': u'Refrigeration:Compressor',
               'pyname': u'RefrigerationCompressor',
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
    def refrigeration_compressor_power_curve_name(self):
        """field `Refrigeration Compressor Power Curve Name`

        |  the input order for the Curve:Bicubic does not
        |  match the ARI 540-2004 Eq. 1 coefficient order
        |  N1 is ARI_C1, N2 is ARI_C2, N3 is ARI_C4, N4 is ARI_C3,
        |  N5 is ARI_C6, N6 is ARI_C5, N7 is ARI_C7, N8 is ARI_C10,
        |  N9 is ARI_C8, N10 is ARI_C9,
        |  N11 is Minimum Suction dewpoint temperature,
        |  N12 is Maximum Suction dewpoint temperature,
        |  N13 is Minimum Discharge dewpoint temperature,
        |  N14 is Maximum Discharge dewpoint temperature

        Args:
            value (str): value for IDD Field `Refrigeration Compressor Power Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_compressor_power_curve_name` or None if not set

        """
        return self["Refrigeration Compressor Power Curve Name"]

    @refrigeration_compressor_power_curve_name.setter
    def refrigeration_compressor_power_curve_name(self, value=None):
        """Corresponds to IDD field `Refrigeration Compressor Power Curve
        Name`"""
        self["Refrigeration Compressor Power Curve Name"] = value

    @property
    def refrigeration_compressor_capacity_curve_name(self):
        """field `Refrigeration Compressor Capacity Curve Name`

        |  the input order for the Curve:Bicubic does not
        |  match the ARI 540-2004 Eq. 1 coefficient order
        |  N1 is ARI_C1, N2 is ARI_C2, N3 is ARI_C4, N4 is ARI_C3,
        |  N5 is ARI_C6, N6 is ARI_C5, N7 is ARI_C7, N8 is ARI_C10,
        |  N9 is ARI_C8, N10 is ARI_C9,
        |  N11 is Minimum Suction dewpoint temperature,
        |  N12 is Maximum Suction dewpoint temperature,
        |  N13 is Minimum Discharge dewpoint temperature,
        |  N14 is Maximum Discharge dewpoint temperature

        Args:
            value (str): value for IDD Field `Refrigeration Compressor Capacity Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_compressor_capacity_curve_name` or None if not set

        """
        return self["Refrigeration Compressor Capacity Curve Name"]

    @refrigeration_compressor_capacity_curve_name.setter
    def refrigeration_compressor_capacity_curve_name(self, value=None):
        """Corresponds to IDD field `Refrigeration Compressor Capacity Curve
        Name`"""
        self["Refrigeration Compressor Capacity Curve Name"] = value

    @property
    def rated_superheat(self):
        """field `Rated Superheat`

        |  Use this input field OR the next, not both
        |  This is used if the compressor rating is based upon
        |  degrees of superheat
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Rated Superheat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_superheat` or None if not set

        """
        return self["Rated Superheat"]

    @rated_superheat.setter
    def rated_superheat(self, value=None):
        """Corresponds to IDD field `Rated Superheat`"""
        self["Rated Superheat"] = value

    @property
    def rated_return_gas_temperature(self):
        """field `Rated Return Gas Temperature`

        |  Use this input field OR the previous, not both
        |  This is used if the compressor rating is based upon
        |  rated return gas temperature (Rated Suction Temperature)
        |  Units: C

        Args:
            value (float): value for IDD Field `Rated Return Gas Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_return_gas_temperature` or None if not set

        """
        return self["Rated Return Gas Temperature"]

    @rated_return_gas_temperature.setter
    def rated_return_gas_temperature(self, value=None):
        """Corresponds to IDD field `Rated Return Gas Temperature`"""
        self["Rated Return Gas Temperature"] = value

    @property
    def rated_liquid_temperature(self):
        """field `Rated Liquid Temperature`

        |  Use this input field OR the next, not both
        |  This is used if the compressor rating is based upon
        |  rated liquid temperature at the expansion valve
        |  Units: C

        Args:
            value (float): value for IDD Field `Rated Liquid Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_liquid_temperature` or None if not set

        """
        return self["Rated Liquid Temperature"]

    @rated_liquid_temperature.setter
    def rated_liquid_temperature(self, value=None):
        """Corresponds to IDD field `Rated Liquid Temperature`"""
        self["Rated Liquid Temperature"] = value

    @property
    def rated_subcooling(self):
        """field `Rated Subcooling`

        |  Use this input field OR the previous, not both
        |  This is used if the compressor rating is based upon
        |  degrees of subcooling
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Rated Subcooling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_subcooling` or None if not set

        """
        return self["Rated Subcooling"]

    @rated_subcooling.setter
    def rated_subcooling(self, value=None):
        """Corresponds to IDD field `Rated Subcooling`"""
        self["Rated Subcooling"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def mode_of_operation(self):
        """field `Mode of Operation`

        |  Default value: Subcritical

        Args:
            value (str): value for IDD Field `Mode of Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mode_of_operation` or None if not set

        """
        return self["Mode of Operation"]

    @mode_of_operation.setter
    def mode_of_operation(self, value="Subcritical"):
        """Corresponds to IDD field `Mode of Operation`"""
        self["Mode of Operation"] = value

    @property
    def transcritical_compressor_power_curve_name(self):
        """field `Transcritical Compressor Power Curve Name`

        Args:
            value (str): value for IDD Field `Transcritical Compressor Power Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `transcritical_compressor_power_curve_name` or None if not set

        """
        return self["Transcritical Compressor Power Curve Name"]

    @transcritical_compressor_power_curve_name.setter
    def transcritical_compressor_power_curve_name(self, value=None):
        """Corresponds to IDD field `Transcritical Compressor Power Curve
        Name`"""
        self["Transcritical Compressor Power Curve Name"] = value

    @property
    def transcritical_compressor_capacity_curve_name(self):
        """field `Transcritical Compressor Capacity Curve Name`

        Args:
            value (str): value for IDD Field `Transcritical Compressor Capacity Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `transcritical_compressor_capacity_curve_name` or None if not set

        """
        return self["Transcritical Compressor Capacity Curve Name"]

    @transcritical_compressor_capacity_curve_name.setter
    def transcritical_compressor_capacity_curve_name(self, value=None):
        """Corresponds to IDD field `Transcritical Compressor Capacity Curve
        Name`"""
        self["Transcritical Compressor Capacity Curve Name"] = value




class RefrigerationCompressorList(DataObject):

    """ Corresponds to IDD object `Refrigeration:CompressorList`
        List of all the compressors included within a single refrigeration system
        (Refrigeration:System). Each list must contain at least one compressor.
        The order in which the individual compressors are listed here will be the
        order in which the compressors are dispatched to meet the system load.
        IMPORTANT: List compressor names in the order in which the compressors will be loaded
        Data is available for many compressors in the RefrigerationCompressor.idf dataset
    """
    _schema = {'extensible-fields': OrderedDict([(u'refrigeration compressor 1 name',
                                                  {'name': u'Refrigeration Compressor 1 Name',
                                                   'pyname': u'refrigeration_compressor_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 2,
               'name': u'Refrigeration:CompressorList',
               'pyname': u'RefrigerationCompressorList',
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

    def add_extensible(self,
                       refrigeration_compressor_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            refrigeration_compressor_1_name (str): value for IDD Field `Refrigeration Compressor 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        refrigeration_compressor_1_name = self.check_value(
            "Refrigeration Compressor 1 Name",
            refrigeration_compressor_1_name)
        vals.append(refrigeration_compressor_1_name)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class RefrigerationSystem(DataObject):

    """ Corresponds to IDD object `Refrigeration:System`
        Simulates the performance of a supermarket refrigeration system when used along with
        other objects to define the refrigeration load(s), the compressor(s), and the
        condenser.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'refrigerated case or walkin or caseandwalkinlist name',
                                       {'name': u'Refrigerated Case or Walkin or CaseAndWalkInList Name',
                                        'pyname': u'refrigerated_case_or_walkin_or_caseandwalkinlist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'refrigeration transfer load or transferload list name',
                                       {'name': u'Refrigeration Transfer Load or TransferLoad List Name',
                                        'pyname': u'refrigeration_transfer_load_or_transferload_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'refrigeration condenser name',
                                       {'name': u'Refrigeration Condenser Name',
                                        'pyname': u'refrigeration_condenser_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor or compressorlist name',
                                       {'name': u'Compressor or CompressorList Name',
                                        'pyname': u'compressor_or_compressorlist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum condensing temperature',
                                       {'name': u'Minimum Condensing Temperature',
                                        'pyname': u'minimum_condensing_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'refrigeration system working fluid type',
                                       {'name': u'Refrigeration System Working Fluid Type',
                                        'pyname': u'refrigeration_system_working_fluid_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'suction temperature control type',
                                       {'name': u'Suction Temperature Control Type',
                                        'pyname': u'suction_temperature_control_type',
                                        'default': u'ConstantSuctionTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'FloatSuctionTemperature',
                                                            u'ConstantSuctionTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mechanical subcooler name',
                                       {'name': u'Mechanical Subcooler Name',
                                        'pyname': u'mechanical_subcooler_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'liquid suction heat exchanger subcooler name',
                                       {'name': u'Liquid Suction Heat Exchanger Subcooler Name',
                                        'pyname': u'liquid_suction_heat_exchanger_subcooler_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sum ua suction piping',
                                       {'name': u'Sum UA Suction Piping',
                                        'pyname': u'sum_ua_suction_piping',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'suction piping zone name',
                                       {'name': u'Suction Piping Zone Name',
                                        'pyname': u'suction_piping_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'number of compressor stages',
                                       {'name': u'Number of Compressor Stages',
                                        'pyname': u'number_of_compressor_stages',
                                        'default': 1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [1,
                                                            2],
                                        'autocalculatable': False,
                                        'type': 'integer'}),
                                      (u'intercooler type',
                                       {'name': u'Intercooler Type',
                                        'pyname': u'intercooler_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Flash Intercooler',
                                                            u'Shell-and-Coil Intercooler'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'shell-and-coil intercooler effectiveness',
                                       {'name': u'Shell-and-Coil Intercooler Effectiveness',
                                        'pyname': u'shellandcoil_intercooler_effectiveness',
                                        'default': 0.8,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'high-stage compressor or compressorlist name',
                                       {'name': u'High-Stage Compressor or CompressorList Name',
                                        'pyname': u'highstage_compressor_or_compressorlist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 7,
               'name': u'Refrigeration:System',
               'pyname': u'RefrigerationSystem',
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
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(self):
        """field `Refrigerated Case or Walkin or CaseAndWalkInList Name`

        |  Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        |  If there is more than one refrigerated case or walk-in served by this system,
        |  enter the name of a Refrigeration:CaseAndWalkInList object.
        |  Only cases and walkins served directly by the system should be included in this list.
        |  Any cases served indirectly via a secondary chiller should NOT be included in this list

        Args:
            value (str): value for IDD Field `Refrigerated Case or Walkin or CaseAndWalkInList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set

        """
        return self["Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(
            self,
            value=None):
        """Corresponds to IDD field `Refrigerated Case or Walkin or
        CaseAndWalkInList Name`"""
        self["Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def refrigeration_transfer_load_or_transferload_list_name(self):
        """field `Refrigeration Transfer Load or TransferLoad List Name`

        |  Enter the name of a Refrigeration:SecondarySystem object OR
        |  a Refrigeration:Condenser:Cascade object OR,
        |  a Refrigeration:TransferLoadList object.
        |  A transfer load is identified as one which moves the load from one system to another.
        |  So if you have more than one such load (including cascade condensers and secondary
        |  loops) served by the same system, use a TransferLoadList object.

        Args:
            value (str): value for IDD Field `Refrigeration Transfer Load or TransferLoad List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_transfer_load_or_transferload_list_name` or None if not set

        """
        return self["Refrigeration Transfer Load or TransferLoad List Name"]

    @refrigeration_transfer_load_or_transferload_list_name.setter
    def refrigeration_transfer_load_or_transferload_list_name(
            self,
            value=None):
        """Corresponds to IDD field `Refrigeration Transfer Load or
        TransferLoad List Name`"""
        self["Refrigeration Transfer Load or TransferLoad List Name"] = value

    @property
    def refrigeration_condenser_name(self):
        """field `Refrigeration Condenser Name`

        Args:
            value (str): value for IDD Field `Refrigeration Condenser Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_condenser_name` or None if not set

        """
        return self["Refrigeration Condenser Name"]

    @refrigeration_condenser_name.setter
    def refrigeration_condenser_name(self, value=None):
        """Corresponds to IDD field `Refrigeration Condenser Name`"""
        self["Refrigeration Condenser Name"] = value

    @property
    def compressor_or_compressorlist_name(self):
        """field `Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `Compressor or CompressorList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_or_compressorlist_name` or None if not set

        """
        return self["Compressor or CompressorList Name"]

    @compressor_or_compressorlist_name.setter
    def compressor_or_compressorlist_name(self, value=None):
        """Corresponds to IDD field `Compressor or CompressorList Name`"""
        self["Compressor or CompressorList Name"] = value

    @property
    def minimum_condensing_temperature(self):
        """field `Minimum Condensing Temperature`

        |  related to the proper operation of the thermal expansion
        |  valves and compressors
        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Condensing Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_condensing_temperature` or None if not set

        """
        return self["Minimum Condensing Temperature"]

    @minimum_condensing_temperature.setter
    def minimum_condensing_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Condensing Temperature`"""
        self["Minimum Condensing Temperature"] = value

    @property
    def refrigeration_system_working_fluid_type(self):
        """field `Refrigeration System Working Fluid Type`

        |  Fluid property data for the refrigerant must be entered.
        |  The fluid property data, including the objects:
        |  FluidProperties:Name, FluidProperties:Temperatures,
        |  FluidProperties:Saturated and FluidProperties:Superheated
        |  can be copied from the FluidPropertiesRefData.idf dataset

        Args:
            value (str): value for IDD Field `Refrigeration System Working Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_system_working_fluid_type` or None if not set

        """
        return self["Refrigeration System Working Fluid Type"]

    @refrigeration_system_working_fluid_type.setter
    def refrigeration_system_working_fluid_type(self, value=None):
        """Corresponds to IDD field `Refrigeration System Working Fluid
        Type`"""
        self["Refrigeration System Working Fluid Type"] = value

    @property
    def suction_temperature_control_type(self):
        """field `Suction Temperature Control Type`

        |  Default value: ConstantSuctionTemperature

        Args:
            value (str): value for IDD Field `Suction Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `suction_temperature_control_type` or None if not set

        """
        return self["Suction Temperature Control Type"]

    @suction_temperature_control_type.setter
    def suction_temperature_control_type(
            self,
            value="ConstantSuctionTemperature"):
        """Corresponds to IDD field `Suction Temperature Control Type`"""
        self["Suction Temperature Control Type"] = value

    @property
    def mechanical_subcooler_name(self):
        """field `Mechanical Subcooler Name`

        |  Optional Field
        |  Recipient of refrigeration capacity, that is receives cool liquid
        |  from another refrigeration system to help meet aggregate case loads

        Args:
            value (str): value for IDD Field `Mechanical Subcooler Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mechanical_subcooler_name` or None if not set

        """
        return self["Mechanical Subcooler Name"]

    @mechanical_subcooler_name.setter
    def mechanical_subcooler_name(self, value=None):
        """Corresponds to IDD field `Mechanical Subcooler Name`"""
        self["Mechanical Subcooler Name"] = value

    @property
    def liquid_suction_heat_exchanger_subcooler_name(self):
        """field `Liquid Suction Heat Exchanger Subcooler Name`

        |  Optional Field
        |  Liquid Suction Heat Exchanger Name, or leave blank

        Args:
            value (str): value for IDD Field `Liquid Suction Heat Exchanger Subcooler Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `liquid_suction_heat_exchanger_subcooler_name` or None if not set

        """
        return self["Liquid Suction Heat Exchanger Subcooler Name"]

    @liquid_suction_heat_exchanger_subcooler_name.setter
    def liquid_suction_heat_exchanger_subcooler_name(self, value=None):
        """Corresponds to IDD field `Liquid Suction Heat Exchanger Subcooler
        Name`"""
        self["Liquid Suction Heat Exchanger Subcooler Name"] = value

    @property
    def sum_ua_suction_piping(self):
        """field `Sum UA Suction Piping`

        |  Use only if you want to include suction piping heat gain in refrigeration load
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Sum UA Suction Piping`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sum_ua_suction_piping` or None if not set

        """
        return self["Sum UA Suction Piping"]

    @sum_ua_suction_piping.setter
    def sum_ua_suction_piping(self, value=None):
        """Corresponds to IDD field `Sum UA Suction Piping`"""
        self["Sum UA Suction Piping"] = value

    @property
    def suction_piping_zone_name(self):
        """field `Suction Piping Zone Name`

        |  This will be used to determine the temperature used for distribution piping heat gain
        |  and the pipe heat gains  as cooling credit for the zone.
        |  Required only if Sum UA Distribution Piping >0.0

        Args:
            value (str): value for IDD Field `Suction Piping Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `suction_piping_zone_name` or None if not set

        """
        return self["Suction Piping Zone Name"]

    @suction_piping_zone_name.setter
    def suction_piping_zone_name(self, value=None):
        """Corresponds to IDD field `Suction Piping Zone Name`"""
        self["Suction Piping Zone Name"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def number_of_compressor_stages(self):
        """field `Number of Compressor Stages`

        |  Default value: 1

        Args:
            value (int): value for IDD Field `Number of Compressor Stages`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_compressor_stages` or None if not set

        """
        return self["Number of Compressor Stages"]

    @number_of_compressor_stages.setter
    def number_of_compressor_stages(self, value=1):
        """Corresponds to IDD field `Number of Compressor Stages`"""
        self["Number of Compressor Stages"] = value

    @property
    def intercooler_type(self):
        """field `Intercooler Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Intercooler Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `intercooler_type` or None if not set

        """
        return self["Intercooler Type"]

    @intercooler_type.setter
    def intercooler_type(self, value="None"):
        """Corresponds to IDD field `Intercooler Type`"""
        self["Intercooler Type"] = value

    @property
    def shellandcoil_intercooler_effectiveness(self):
        """field `Shell-and-Coil Intercooler Effectiveness`

        |  Default value: 0.8

        Args:
            value (float): value for IDD Field `Shell-and-Coil Intercooler Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shellandcoil_intercooler_effectiveness` or None if not set
        """
        return self["Shell-and-Coil Intercooler Effectiveness"]

    @shellandcoil_intercooler_effectiveness.setter
    def shellandcoil_intercooler_effectiveness(self, value=0.8):
        """  Corresponds to IDD field `Shell-and-Coil Intercooler Effectiveness`

        """
        self["Shell-and-Coil Intercooler Effectiveness"] = value

    @property
    def highstage_compressor_or_compressorlist_name(self):
        """field `High-Stage Compressor or CompressorList Name`


        Args:
            value (str): value for IDD Field `High-Stage Compressor or CompressorList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `highstage_compressor_or_compressorlist_name` or None if not set
        """
        return self["High-Stage Compressor or CompressorList Name"]

    @highstage_compressor_or_compressorlist_name.setter
    def highstage_compressor_or_compressorlist_name(self, value=None):
        """  Corresponds to IDD field `High-Stage Compressor or CompressorList Name`

        """
        self["High-Stage Compressor or CompressorList Name"] = value




class RefrigerationTranscriticalSystem(DataObject):

    """ Corresponds to IDD object `Refrigeration:TranscriticalSystem`
        Detailed transcritical carbon dioxide (CO2) booster refrigeration systems used in
        supermarkets.  The object allows for modeling either a single stage system with
        medium-temperature loads or a two stage system with both medium- and low-temperature
        loads.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'system type',
                                       {'name': u'System Type',
                                        'pyname': u'system_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'SingleStage',
                                                            u'TwoStage'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'medium temperature refrigerated case or walkin or caseandwalkinlist name',
                                       {'name': u'Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name',
                                        'pyname': u'medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'low temperature refrigerated case or walkin or caseandwalkinlist name',
                                       {'name': u'Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name',
                                        'pyname': u'low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'refrigeration gas cooler name',
                                       {'name': u'Refrigeration Gas Cooler Name',
                                        'pyname': u'refrigeration_gas_cooler_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'high pressure compressor or compressorlist name',
                                       {'name': u'High Pressure Compressor or CompressorList Name',
                                        'pyname': u'high_pressure_compressor_or_compressorlist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'low pressure compressor or compressorlist name',
                                       {'name': u'Low Pressure Compressor or CompressorList Name',
                                        'pyname': u'low_pressure_compressor_or_compressorlist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'receiver pressure',
                                       {'name': u'Receiver Pressure',
                                        'pyname': u'receiver_pressure',
                                        'default': 4000000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'subcooler effectiveness',
                                       {'name': u'Subcooler Effectiveness',
                                        'pyname': u'subcooler_effectiveness',
                                        'default': 0.4,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'refrigeration system working fluid type',
                                       {'name': u'Refrigeration System Working Fluid Type',
                                        'pyname': u'refrigeration_system_working_fluid_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sum ua suction piping for medium temperature loads',
                                       {'name': u'Sum UA Suction Piping for Medium Temperature Loads',
                                        'pyname': u'sum_ua_suction_piping_for_medium_temperature_loads',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'medium temperature suction piping zone name',
                                       {'name': u'Medium Temperature Suction Piping Zone Name',
                                        'pyname': u'medium_temperature_suction_piping_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sum ua suction piping for low temperature loads',
                                       {'name': u'Sum UA Suction Piping for Low Temperature Loads',
                                        'pyname': u'sum_ua_suction_piping_for_low_temperature_loads',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'low temperature suction piping zone name',
                                       {'name': u'Low Temperature Suction Piping Zone Name',
                                        'pyname': u'low_temperature_suction_piping_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Refrigeration:TranscriticalSystem',
               'pyname': u'RefrigerationTranscriticalSystem',
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
    def system_type(self):
        """field `System Type`

        Args:
            value (str): value for IDD Field `System Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `system_type` or None if not set

        """
        return self["System Type"]

    @system_type.setter
    def system_type(self, value=None):
        """Corresponds to IDD field `System Type`"""
        self["System Type"] = value

    @property
    def medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(
            self):
        """field `Medium Temperature Refrigerated Case or Walkin or
        CaseAndWalkInList Name`

        |  Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        |  If there is more than one refrigerated case or walk-in served by this system,
        |  enter the name of a Refrigeration:CaseAndWalkInList object.
        |  Only medium temperature cases and walk-ins served directly by the system should
        |  be included in this list.

        Args:
            value (str): value for IDD Field `Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set

        """
        return self[
            "Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(
            self,
            value=None):
        """Corresponds to IDD field `Medium Temperature Refrigerated Case or
        Walkin or CaseAndWalkInList Name`"""
        self[
            "Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(
            self):
        """field `Low Temperature Refrigerated Case or Walkin or
        CaseAndWalkInList Name`

        |  Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        |  If there is more than one refrigerated case or walk-in served by this system,
        |  enter the name of a Refrigeration:CaseAndWalkInList object.
        |  Only low temperature cases and walkins served directly by the system should be
        |  included in this list.

        Args:
            value (str): value for IDD Field `Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set

        """
        return self[
            "Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name(
            self,
            value=None):
        """Corresponds to IDD field `Low Temperature Refrigerated Case or
        Walkin or CaseAndWalkInList Name`"""
        self[
            "Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def refrigeration_gas_cooler_name(self):
        """field `Refrigeration Gas Cooler Name`

        Args:
            value (str): value for IDD Field `Refrigeration Gas Cooler Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_gas_cooler_name` or None if not set

        """
        return self["Refrigeration Gas Cooler Name"]

    @refrigeration_gas_cooler_name.setter
    def refrigeration_gas_cooler_name(self, value=None):
        """Corresponds to IDD field `Refrigeration Gas Cooler Name`"""
        self["Refrigeration Gas Cooler Name"] = value

    @property
    def high_pressure_compressor_or_compressorlist_name(self):
        """field `High Pressure Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `High Pressure Compressor or CompressorList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `high_pressure_compressor_or_compressorlist_name` or None if not set

        """
        return self["High Pressure Compressor or CompressorList Name"]

    @high_pressure_compressor_or_compressorlist_name.setter
    def high_pressure_compressor_or_compressorlist_name(self, value=None):
        """Corresponds to IDD field `High Pressure Compressor or CompressorList
        Name`"""
        self["High Pressure Compressor or CompressorList Name"] = value

    @property
    def low_pressure_compressor_or_compressorlist_name(self):
        """field `Low Pressure Compressor or CompressorList Name`

        Args:
            value (str): value for IDD Field `Low Pressure Compressor or CompressorList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `low_pressure_compressor_or_compressorlist_name` or None if not set

        """
        return self["Low Pressure Compressor or CompressorList Name"]

    @low_pressure_compressor_or_compressorlist_name.setter
    def low_pressure_compressor_or_compressorlist_name(self, value=None):
        """Corresponds to IDD field `Low Pressure Compressor or CompressorList
        Name`"""
        self["Low Pressure Compressor or CompressorList Name"] = value

    @property
    def receiver_pressure(self):
        """field `Receiver Pressure`

        |  Units: Pa
        |  Default value: 4000000.0

        Args:
            value (float): value for IDD Field `Receiver Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `receiver_pressure` or None if not set

        """
        return self["Receiver Pressure"]

    @receiver_pressure.setter
    def receiver_pressure(self, value=4000000.0):
        """Corresponds to IDD field `Receiver Pressure`"""
        self["Receiver Pressure"] = value

    @property
    def subcooler_effectiveness(self):
        """field `Subcooler Effectiveness`

        |  Default value: 0.4

        Args:
            value (float): value for IDD Field `Subcooler Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `subcooler_effectiveness` or None if not set

        """
        return self["Subcooler Effectiveness"]

    @subcooler_effectiveness.setter
    def subcooler_effectiveness(self, value=0.4):
        """Corresponds to IDD field `Subcooler Effectiveness`"""
        self["Subcooler Effectiveness"] = value

    @property
    def refrigeration_system_working_fluid_type(self):
        """field `Refrigeration System Working Fluid Type`

        |  Fluid property data for the refrigerant must be entered.
        |  The fluid property data, including the objects:
        |  FluidProperties:Name, FluidProperties:Temperatures,
        |  FluidProperties:Saturated and FluidProperties:Superheated
        |  can be copied from the FluidPropertiesRefData.idf dataset

        Args:
            value (str): value for IDD Field `Refrigeration System Working Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigeration_system_working_fluid_type` or None if not set

        """
        return self["Refrigeration System Working Fluid Type"]

    @refrigeration_system_working_fluid_type.setter
    def refrigeration_system_working_fluid_type(self, value=None):
        """Corresponds to IDD field `Refrigeration System Working Fluid
        Type`"""
        self["Refrigeration System Working Fluid Type"] = value

    @property
    def sum_ua_suction_piping_for_medium_temperature_loads(self):
        """field `Sum UA Suction Piping for Medium Temperature Loads`

        |  Use only if you want to include suction piping heat gain in refrigeration load
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Sum UA Suction Piping for Medium Temperature Loads`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sum_ua_suction_piping_for_medium_temperature_loads` or None if not set

        """
        return self["Sum UA Suction Piping for Medium Temperature Loads"]

    @sum_ua_suction_piping_for_medium_temperature_loads.setter
    def sum_ua_suction_piping_for_medium_temperature_loads(self, value=None):
        """Corresponds to IDD field `Sum UA Suction Piping for Medium
        Temperature Loads`"""
        self["Sum UA Suction Piping for Medium Temperature Loads"] = value

    @property
    def medium_temperature_suction_piping_zone_name(self):
        """field `Medium Temperature Suction Piping Zone Name`

        |  This will be used to determine the temperature used for distribution piping heat
        |  gain and the pipe heat gains as cooling credit for the zone.
        |  Required only if Sum UA Distribution Piping for Medium Temperature Loads > 0.0

        Args:
            value (str): value for IDD Field `Medium Temperature Suction Piping Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `medium_temperature_suction_piping_zone_name` or None if not set

        """
        return self["Medium Temperature Suction Piping Zone Name"]

    @medium_temperature_suction_piping_zone_name.setter
    def medium_temperature_suction_piping_zone_name(self, value=None):
        """Corresponds to IDD field `Medium Temperature Suction Piping Zone
        Name`"""
        self["Medium Temperature Suction Piping Zone Name"] = value

    @property
    def sum_ua_suction_piping_for_low_temperature_loads(self):
        """field `Sum UA Suction Piping for Low Temperature Loads`

        |  Use only if you want to include suction piping heat gain in refrigeration load
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Sum UA Suction Piping for Low Temperature Loads`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sum_ua_suction_piping_for_low_temperature_loads` or None if not set

        """
        return self["Sum UA Suction Piping for Low Temperature Loads"]

    @sum_ua_suction_piping_for_low_temperature_loads.setter
    def sum_ua_suction_piping_for_low_temperature_loads(self, value=None):
        """Corresponds to IDD field `Sum UA Suction Piping for Low Temperature
        Loads`"""
        self["Sum UA Suction Piping for Low Temperature Loads"] = value

    @property
    def low_temperature_suction_piping_zone_name(self):
        """field `Low Temperature Suction Piping Zone Name`

        |  This will be used to determine the temperature used for distribution piping heat
        |  gain and the pipe heat gains as cooling credit for the zone.
        |  Required only if Sum UA Distribution Piping for Low Temperature Loads > 0.0

        Args:
            value (str): value for IDD Field `Low Temperature Suction Piping Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `low_temperature_suction_piping_zone_name` or None if not set

        """
        return self["Low Temperature Suction Piping Zone Name"]

    @low_temperature_suction_piping_zone_name.setter
    def low_temperature_suction_piping_zone_name(self, value=None):
        """Corresponds to IDD field `Low Temperature Suction Piping Zone
        Name`"""
        self["Low Temperature Suction Piping Zone Name"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class RefrigerationSecondarySystem(DataObject):

    """ Corresponds to IDD object `Refrigeration:SecondarySystem`
        Works in conjunction with refrigerated cases and walkins to simulate the performance
        of a secondary loop supermarket refrigeration system. Heat from the refrigeration
        loads served by the secondary loop is absorbed by a primary refrigeration system
        (Refrigeration:System). The SecondarySystem object simulates a heat exchanger that
        is an evaporator, or refrigeration load, on the primary refrigeration system.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'refrigerated case or walkin or caseandwalkinlist name',
                                       {'name': u'Refrigerated Case or Walkin or CaseAndWalkInList Name',
                                        'pyname': u'refrigerated_case_or_walkin_or_caseandwalkinlist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'circulating fluid type',
                                       {'name': u'Circulating Fluid Type',
                                        'pyname': u'circulating_fluid_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'FluidAlwaysLiquid',
                                                            u'FluidPhaseChange'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'circulating fluid name',
                                       {'name': u'Circulating Fluid Name',
                                        'pyname': u'circulating_fluid_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'evaporator capacity',
                                       {'name': u'Evaporator Capacity',
                                        'pyname': u'evaporator_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'evaporator flow rate for secondary fluid',
                                       {'name': u'Evaporator Flow Rate for Secondary Fluid',
                                        'pyname': u'evaporator_flow_rate_for_secondary_fluid',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'M3/s'}),
                                      (u'evaporator evaporating temperature',
                                       {'name': u'Evaporator Evaporating Temperature',
                                        'pyname': u'evaporator_evaporating_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'evaporator approach temperature difference',
                                       {'name': u'Evaporator Approach Temperature Difference',
                                        'pyname': u'evaporator_approach_temperature_difference',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'evaporator range temperature difference',
                                       {'name': u'Evaporator Range Temperature Difference',
                                        'pyname': u'evaporator_range_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'number of pumps in loop',
                                       {'name': u'Number of Pumps in Loop',
                                        'pyname': u'number_of_pumps_in_loop',
                                        'default': 1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'total pump flow rate',
                                       {'name': u'Total Pump Flow Rate',
                                        'pyname': u'total_pump_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'M3/s'}),
                                      (u'total pump power',
                                       {'name': u'Total Pump Power',
                                        'pyname': u'total_pump_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'total pump head',
                                       {'name': u'Total Pump Head',
                                        'pyname': u'total_pump_head',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'phasechange circulating rate',
                                       {'name': u'PhaseChange Circulating Rate',
                                        'pyname': u'phasechange_circulating_rate',
                                        'default': 2.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'pump drive type',
                                       {'name': u'Pump Drive Type',
                                        'pyname': u'pump_drive_type',
                                        'default': u'Constant',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Variable'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'variable speed pump cubic curve name',
                                       {'name': u'Variable Speed Pump Cubic Curve Name',
                                        'pyname': u'variable_speed_pump_cubic_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pump motor heat to fluid',
                                       {'name': u'Pump Motor Heat to Fluid',
                                        'pyname': u'pump_motor_heat_to_fluid',
                                        'default': 0.85,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.5,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'sum ua distribution piping',
                                       {'name': u'Sum UA Distribution Piping',
                                        'pyname': u'sum_ua_distribution_piping',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'distribution piping zone name',
                                       {'name': u'Distribution Piping Zone Name',
                                        'pyname': u'distribution_piping_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'sum ua receiver/separator shell',
                                       {'name': u'Sum UA Receiver/Separator Shell',
                                        'pyname': u'sum_ua_receiver_or_separator_shell',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'receiver/separator zone name',
                                       {'name': u'Receiver/Separator Zone Name',
                                        'pyname': u'receiver_or_separator_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'evaporator refrigerant inventory',
                                       {'name': u'Evaporator Refrigerant Inventory',
                                        'pyname': u'evaporator_refrigerant_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 14,
               'name': u'Refrigeration:SecondarySystem',
               'pyname': u'RefrigerationSecondarySystem',
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
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(self):
        """field `Refrigerated Case or Walkin or CaseAndWalkInList Name`

        |  Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.
        |  If there is more than one refrigerated case or walk-in served by this secondary system,
        |  enter the name of a Refrigeration:CaseAndWalkInList object.

        Args:
            value (str): value for IDD Field `Refrigerated Case or Walkin or CaseAndWalkInList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigerated_case_or_walkin_or_caseandwalkinlist_name` or None if not set

        """
        return self["Refrigerated Case or Walkin or CaseAndWalkInList Name"]

    @refrigerated_case_or_walkin_or_caseandwalkinlist_name.setter
    def refrigerated_case_or_walkin_or_caseandwalkinlist_name(
            self,
            value=None):
        """Corresponds to IDD field `Refrigerated Case or Walkin or
        CaseAndWalkInList Name`"""
        self["Refrigerated Case or Walkin or CaseAndWalkInList Name"] = value

    @property
    def circulating_fluid_type(self):
        """field `Circulating Fluid Type`

        |  If "FluidAlwaysLiquid" is selected, the fluid properties
        |  must be input using the objects: FluidProperties:Name,
        |  FluidProperties:GlycolConcentration, and, if user defined fluid type,
        |  FluidProperties:Temperatures and FluidProperties:Concentration.
        |  Many sets of fluid properties can be found in GlycolPropertiesRefData.idf.
        |  If "FluidPhaseChange" is selected, the refrigerant properties
        |  must be input using the objects: (if user defined fluid type): FluidProperties:Name,
        |  FluidProperties:Temperatures, FluidProperties:Saturated, and
        |  FluidProperties:Superheated.
        |  Many sets of refrigerant data can be found in FluidPropertiesRefData.idf.

        Args:
            value (str): value for IDD Field `Circulating Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `circulating_fluid_type` or None if not set

        """
        return self["Circulating Fluid Type"]

    @circulating_fluid_type.setter
    def circulating_fluid_type(self, value=None):
        """Corresponds to IDD field `Circulating Fluid Type`"""
        self["Circulating Fluid Type"] = value

    @property
    def circulating_fluid_name(self):
        """field `Circulating Fluid Name`

        |  This must correspond to a name in the FluidProperties:Name object.

        Args:
            value (str): value for IDD Field `Circulating Fluid Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `circulating_fluid_name` or None if not set

        """
        return self["Circulating Fluid Name"]

    @circulating_fluid_name.setter
    def circulating_fluid_name(self, value=None):
        """Corresponds to IDD field `Circulating Fluid Name`"""
        self["Circulating Fluid Name"] = value

    @property
    def evaporator_capacity(self):
        """field `Evaporator Capacity`

        |  For "FluidAlwaysLiquid", at least one of the two, Evaporator Capacity OR
        |  Evaporator Flow Rate for Secondary Fluid, is required.
        |  For "FluidPhaseChange", the default capacity is the sum of the rated capacities of the
        |  Cases and Walk-ins served by the secondary loop.
        |  Units: W

        Args:
            value (float): value for IDD Field `Evaporator Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporator_capacity` or None if not set

        """
        return self["Evaporator Capacity"]

    @evaporator_capacity.setter
    def evaporator_capacity(self, value=None):
        """Corresponds to IDD field `Evaporator Capacity`"""
        self["Evaporator Capacity"] = value

    @property
    def evaporator_flow_rate_for_secondary_fluid(self):
        """field `Evaporator Flow Rate for Secondary Fluid`

        |  For "FluidAlwaysLiquid", at least one of the two, Evaporator Capacity OR
        |  Evaporator Flow Rate for Secondary Fluid, is required.
        |  For "FluidPhaseChange" loops, this input is not used. (see PhaseChange Circulating
        |  Rate)
        |  Units: M3/s

        Args:
            value (float): value for IDD Field `Evaporator Flow Rate for Secondary Fluid`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporator_flow_rate_for_secondary_fluid` or None if not set

        """
        return self["Evaporator Flow Rate for Secondary Fluid"]

    @evaporator_flow_rate_for_secondary_fluid.setter
    def evaporator_flow_rate_for_secondary_fluid(self, value=None):
        """Corresponds to IDD field `Evaporator Flow Rate for Secondary
        Fluid`"""
        self["Evaporator Flow Rate for Secondary Fluid"] = value

    @property
    def evaporator_evaporating_temperature(self):
        """field `Evaporator Evaporating Temperature`

        |  This is the evaporating temperature in the heat exchanger
        |  used to chill or condense the secondary loop circulating fluid.
        |  It is NOT the temperature in any cases or walk-ins served by the
        |  secondary loop.
        |  Units: C

        Args:
            value (float): value for IDD Field `Evaporator Evaporating Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporator_evaporating_temperature` or None if not set

        """
        return self["Evaporator Evaporating Temperature"]

    @evaporator_evaporating_temperature.setter
    def evaporator_evaporating_temperature(self, value=None):
        """Corresponds to IDD field `Evaporator Evaporating Temperature`"""
        self["Evaporator Evaporating Temperature"] = value

    @property
    def evaporator_approach_temperature_difference(self):
        """field `Evaporator Approach Temperature Difference`

        |  For "FluidAlwaysLiquid", this is the rated difference between the temperature of the
        |  circulating fluid leaving the heat exchanger
        |  and the heat exchanger's rated evaporating temperature.
        |  For "FluidPhaseChange", this is the difference between the temperature of the
        |  evaporating and condensing temperatures in the heat exchanger.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Evaporator Approach Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporator_approach_temperature_difference` or None if not set

        """
        return self["Evaporator Approach Temperature Difference"]

    @evaporator_approach_temperature_difference.setter
    def evaporator_approach_temperature_difference(self, value=None):
        """Corresponds to IDD field `Evaporator Approach Temperature
        Difference`"""
        self["Evaporator Approach Temperature Difference"] = value

    @property
    def evaporator_range_temperature_difference(self):
        """field `Evaporator Range Temperature Difference`

        |  For "FluidAlwaysLiquid", this is the rated difference between the temperature of the
        |  circulating fluid entering the heat exchanger and the temperature of the
        |  circulating fluid leaving the heat exchanger, and is Required.
        |  For "FluidPhaseChange", this input is not used.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Evaporator Range Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporator_range_temperature_difference` or None if not set

        """
        return self["Evaporator Range Temperature Difference"]

    @evaporator_range_temperature_difference.setter
    def evaporator_range_temperature_difference(self, value=None):
        """Corresponds to IDD field `Evaporator Range Temperature
        Difference`"""
        self["Evaporator Range Temperature Difference"] = value

    @property
    def number_of_pumps_in_loop(self):
        """field `Number of Pumps in Loop`

        |  Default value: 1

        Args:
            value (int): value for IDD Field `Number of Pumps in Loop`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_pumps_in_loop` or None if not set

        """
        return self["Number of Pumps in Loop"]

    @number_of_pumps_in_loop.setter
    def number_of_pumps_in_loop(self, value=1):
        """Corresponds to IDD field `Number of Pumps in Loop`"""
        self["Number of Pumps in Loop"] = value

    @property
    def total_pump_flow_rate(self):
        """field `Total Pump Flow Rate`

        |  For "FluidAlwaysLiquid",if not input, Evaporator Flow Rate for Secondary Fluid
        |  will be used.
        |  For "FluidPhaseChange", if not input, this will be calculated using the
        |  PhaseChange Circulating Rate.
        |  Units: M3/s

        Args:
            value (float): value for IDD Field `Total Pump Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `total_pump_flow_rate` or None if not set

        """
        return self["Total Pump Flow Rate"]

    @total_pump_flow_rate.setter
    def total_pump_flow_rate(self, value=None):
        """Corresponds to IDD field `Total Pump Flow Rate`"""
        self["Total Pump Flow Rate"] = value

    @property
    def total_pump_power(self):
        """field `Total Pump Power`

        |  Either the Total Pump Power or the Total Pump Head is required.
        |  Units: W

        Args:
            value (float): value for IDD Field `Total Pump Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `total_pump_power` or None if not set

        """
        return self["Total Pump Power"]

    @total_pump_power.setter
    def total_pump_power(self, value=None):
        """Corresponds to IDD field `Total Pump Power`"""
        self["Total Pump Power"] = value

    @property
    def total_pump_head(self):
        """field `Total Pump Head`

        |  Either the Total Pump Power or the Total Pump Head is required.
        |  Units: Pa

        Args:
            value (float): value for IDD Field `Total Pump Head`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `total_pump_head` or None if not set

        """
        return self["Total Pump Head"]

    @total_pump_head.setter
    def total_pump_head(self, value=None):
        """Corresponds to IDD field `Total Pump Head`"""
        self["Total Pump Head"] = value

    @property
    def phasechange_circulating_rate(self):
        """field `PhaseChange Circulating Rate`

        |  This is the total mass flow at the pump divided by the gaseous mass flow
        |  leaving the refrigeration load.
        |  Units: dimensionless
        |  Default value: 2.5
        |  value >= 1.0

        Args:
            value (float): value for IDD Field `PhaseChange Circulating Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `phasechange_circulating_rate` or None if not set

        """
        return self["PhaseChange Circulating Rate"]

    @phasechange_circulating_rate.setter
    def phasechange_circulating_rate(self, value=2.5):
        """Corresponds to IDD field `PhaseChange Circulating Rate`"""
        self["PhaseChange Circulating Rate"] = value

    @property
    def pump_drive_type(self):
        """field `Pump Drive Type`

        |  Default value: Constant

        Args:
            value (str): value for IDD Field `Pump Drive Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pump_drive_type` or None if not set

        """
        return self["Pump Drive Type"]

    @pump_drive_type.setter
    def pump_drive_type(self, value="Constant"):
        """Corresponds to IDD field `Pump Drive Type`"""
        self["Pump Drive Type"] = value

    @property
    def variable_speed_pump_cubic_curve_name(self):
        """field `Variable Speed Pump Cubic Curve Name`

        |  Variable Speed Pump Curve Name is applicable to variable speed pumps
        |  only.

        Args:
            value (str): value for IDD Field `Variable Speed Pump Cubic Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `variable_speed_pump_cubic_curve_name` or None if not set

        """
        return self["Variable Speed Pump Cubic Curve Name"]

    @variable_speed_pump_cubic_curve_name.setter
    def variable_speed_pump_cubic_curve_name(self, value=None):
        """Corresponds to IDD field `Variable Speed Pump Cubic Curve Name`"""
        self["Variable Speed Pump Cubic Curve Name"] = value

    @property
    def pump_motor_heat_to_fluid(self):
        """field `Pump Motor Heat to Fluid`

        |  This is the portion of the pump motor heat added to secondary circulating fluid
        |  and is equal to the motor efficiency for non-hermetic motor.
        |  Enter 1.0 for a semi-hermetic motor.
        |  Units: dimensionless
        |  Default value: 0.85
        |  value >= 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Pump Motor Heat to Fluid`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pump_motor_heat_to_fluid` or None if not set

        """
        return self["Pump Motor Heat to Fluid"]

    @pump_motor_heat_to_fluid.setter
    def pump_motor_heat_to_fluid(self, value=0.85):
        """Corresponds to IDD field `Pump Motor Heat to Fluid`"""
        self["Pump Motor Heat to Fluid"] = value

    @property
    def sum_ua_distribution_piping(self):
        """field `Sum UA Distribution Piping`

        |  Use only if you want to include distribution piping heat gain in refrigeration load.
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Sum UA Distribution Piping`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sum_ua_distribution_piping` or None if not set

        """
        return self["Sum UA Distribution Piping"]

    @sum_ua_distribution_piping.setter
    def sum_ua_distribution_piping(self, value=None):
        """Corresponds to IDD field `Sum UA Distribution Piping`"""
        self["Sum UA Distribution Piping"] = value

    @property
    def distribution_piping_zone_name(self):
        """field `Distribution Piping Zone Name`

        |  This will be used to determine the temperature used for distribution piping heat gain.
        |  The pipe heat gains are also counted as cooling credit for the zone.
        |  Required only if Sum UA Distribution Piping >0.0

        Args:
            value (str): value for IDD Field `Distribution Piping Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `distribution_piping_zone_name` or None if not set

        """
        return self["Distribution Piping Zone Name"]

    @distribution_piping_zone_name.setter
    def distribution_piping_zone_name(self, value=None):
        """Corresponds to IDD field `Distribution Piping Zone Name`"""
        self["Distribution Piping Zone Name"] = value

    @property
    def sum_ua_receiver_or_separator_shell(self):
        """field `Sum UA Receiver/Separator Shell`

        |  Use only if you want to include Receiver/Separator Shell heat gain in refrigeration load.
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Sum UA Receiver/Separator Shell`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sum_ua_receiver_or_separator_shell` or None if not set

        """
        return self["Sum UA Receiver/Separator Shell"]

    @sum_ua_receiver_or_separator_shell.setter
    def sum_ua_receiver_or_separator_shell(self, value=None):
        """Corresponds to IDD field `Sum UA Receiver/Separator Shell`"""
        self["Sum UA Receiver/Separator Shell"] = value

    @property
    def receiver_or_separator_zone_name(self):
        """field `Receiver/Separator Zone Name`

        |  This will be used to determine the temperature used for Receiver/Separator Shell heat gain.
        |  The shell heat gains are also counted as cooling credit for the zone.
        |  Required only if Sum UA Receiver/Separator Shell >0.0

        Args:
            value (str): value for IDD Field `Receiver/Separator Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `receiver_or_separator_zone_name` or None if not set

        """
        return self["Receiver/Separator Zone Name"]

    @receiver_or_separator_zone_name.setter
    def receiver_or_separator_zone_name(self, value=None):
        """Corresponds to IDD field `Receiver/Separator Zone Name`"""
        self["Receiver/Separator Zone Name"] = value

    @property
    def evaporator_refrigerant_inventory(self):
        """field `Evaporator Refrigerant Inventory`

        |  This value refers to the refrigerant circulating within the primary system providing
        |  cooling to the chiller for the secondary loop, not to the fluid circulating
        |  within the secondary loop itself.
        |  Units: kg

        Args:
            value (float): value for IDD Field `Evaporator Refrigerant Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporator_refrigerant_inventory` or None if not set

        """
        return self["Evaporator Refrigerant Inventory"]

    @evaporator_refrigerant_inventory.setter
    def evaporator_refrigerant_inventory(self, value=None):
        """Corresponds to IDD field `Evaporator Refrigerant Inventory`"""
        self["Evaporator Refrigerant Inventory"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class RefrigerationWalkIn(DataObject):

    """ Corresponds to IDD object `Refrigeration:WalkIn`
        Works in conjunction with a compressor rack, a refrigeration system, or a
        refrigeration secondary system to simulate the performance of a walk-in cooler.
        The walk-in cooler model uses information at rated conditions along with input
        descriptions for heat transfer surfaces facing multiple zones to determine
        performance.
    """
    _schema = {'extensible-fields': OrderedDict([(u'zone 1 name',
                                                  {'name': u'Zone 1 Name',
                                                   'pyname': u'zone_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'total insulated surface area facing zone 1',
                                                  {'name': u'Total Insulated Surface Area Facing Zone 1',
                                                   'pyname': u'total_insulated_surface_area_facing_zone_1',
                                                   'minimum>': 0.0,
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm2'}),
                                                 (u'insulated surface u-value facing zone 1',
                                                  {'name': u'Insulated Surface U-Value Facing Zone 1',
                                                   'pyname': u'insulated_surface_uvalue_facing_zone_1',
                                                   'default': 0.3154,
                                                   'minimum>': 0.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'W/m2-K'}),
                                                 (u'area of glass reach in doors facing zone 1',
                                                  {'name': u'Area of Glass Reach In Doors Facing Zone 1',
                                                   'pyname': u'area_of_glass_reach_in_doors_facing_zone_1',
                                                   'default': 0.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm2'}),
                                                 (u'height of glass reach in doors facing zone 1',
                                                  {'name': u'Height of Glass Reach In Doors Facing Zone 1',
                                                   'pyname': u'height_of_glass_reach_in_doors_facing_zone_1',
                                                   'default': 1.5,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm'}),
                                                 (u'glass reach in door u value facing zone 1',
                                                  {'name': u'Glass Reach In Door U Value Facing Zone 1',
                                                   'pyname': u'glass_reach_in_door_u_value_facing_zone_1',
                                                   'default': 1.136,
                                                   'minimum>': 0.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'W/m2-K'}),
                                                 (u'glass reach in door opening schedule name facing zone 1',
                                                  {'name': u'Glass Reach In Door Opening Schedule Name Facing Zone 1',
                                                   'pyname': u'glass_reach_in_door_opening_schedule_name_facing_zone_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'area of stocking doors facing zone 1',
                                                  {'name': u'Area of Stocking Doors Facing Zone 1',
                                                   'pyname': u'area_of_stocking_doors_facing_zone_1',
                                                   'default': 0.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm2'}),
                                                 (u'height of stocking doors facing zone 1',
                                                  {'name': u'Height of Stocking Doors Facing Zone 1',
                                                   'pyname': u'height_of_stocking_doors_facing_zone_1',
                                                   'default': 3.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm'}),
                                                 (u'stocking door u value facing zone 1',
                                                  {'name': u'Stocking Door U Value Facing Zone 1',
                                                   'pyname': u'stocking_door_u_value_facing_zone_1',
                                                   'default': 0.3785,
                                                   'minimum>': 0.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'W/m2-K'}),
                                                 (u'stocking door opening schedule name facing zone 1',
                                                  {'name': u'Stocking Door Opening Schedule Name Facing Zone 1',
                                                   'pyname': u'stocking_door_opening_schedule_name_facing_zone_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'stocking door opening protection type facing zone 1',
                                                  {'name': u'Stocking Door Opening Protection Type Facing Zone 1',
                                                   'pyname': u'stocking_door_opening_protection_type_facing_zone_1',
                                                   'default': u'AirCurtain',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'accepted-values': [u'None',
                                                                       u'AirCurtain',
                                                                       u'StripCurtain'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'})]),
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
                                      (u'rated coil cooling capacity',
                                       {'name': u'Rated Coil Cooling Capacity',
                                        'pyname': u'rated_coil_cooling_capacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'operating temperature',
                                       {'name': u'Operating Temperature',
                                        'pyname': u'operating_temperature',
                                        'maximum<': 20.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated cooling source temperature',
                                       {'name': u'Rated Cooling Source Temperature',
                                        'pyname': u'rated_cooling_source_temperature',
                                        'maximum': 40.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated total heating power',
                                       {'name': u'Rated Total Heating Power',
                                        'pyname': u'rated_total_heating_power',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating power schedule name',
                                       {'name': u'Heating Power Schedule Name',
                                        'pyname': u'heating_power_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated cooling coil fan power',
                                       {'name': u'Rated Cooling Coil Fan Power',
                                        'pyname': u'rated_cooling_coil_fan_power',
                                        'default': 375.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated circulation fan power',
                                       {'name': u'Rated Circulation Fan Power',
                                        'pyname': u'rated_circulation_fan_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated total lighting power',
                                       {'name': u'Rated Total Lighting Power',
                                        'pyname': u'rated_total_lighting_power',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'lighting schedule name',
                                       {'name': u'Lighting Schedule Name',
                                        'pyname': u'lighting_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost type',
                                       {'name': u'Defrost Type',
                                        'pyname': u'defrost_type',
                                        'default': u'Electric',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'HotFluid',
                                                            u'Electric',
                                                            u'None',
                                                            u'OffCycle'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost control type',
                                       {'name': u'Defrost Control Type',
                                        'pyname': u'defrost_control_type',
                                        'default': u'TimeSchedule',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'TimeSchedule',
                                                            u'TemperatureTermination'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost schedule name',
                                       {'name': u'Defrost Schedule Name',
                                        'pyname': u'defrost_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost drip-down schedule name',
                                       {'name': u'Defrost Drip-Down Schedule Name',
                                        'pyname': u'defrost_dripdown_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost power',
                                       {'name': u'Defrost Power',
                                        'pyname': u'defrost_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'temperature termination defrost fraction to ice',
                                       {'name': u'Temperature Termination Defrost Fraction to Ice',
                                        'pyname': u'temperature_termination_defrost_fraction_to_ice',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'restocking schedule name',
                                       {'name': u'Restocking Schedule Name',
                                        'pyname': u'restocking_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'average refrigerant charge inventory',
                                       {'name': u'Average Refrigerant Charge Inventory',
                                        'pyname': u'average_refrigerant_charge_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'}),
                                      (u'insulated floor surface area',
                                       {'name': u'Insulated Floor Surface Area',
                                        'pyname': u'insulated_floor_surface_area',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'insulated floor u-value',
                                       {'name': u'Insulated Floor U-Value',
                                        'pyname': u'insulated_floor_uvalue',
                                        'default': 0.3154,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 28,
               'name': u'Refrigeration:WalkIn',
               'pyname': u'RefrigerationWalkIn',
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
    def rated_coil_cooling_capacity(self):
        """field `Rated Coil Cooling Capacity`

        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Coil Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_coil_cooling_capacity` or None if not set

        """
        return self["Rated Coil Cooling Capacity"]

    @rated_coil_cooling_capacity.setter
    def rated_coil_cooling_capacity(self, value=None):
        """Corresponds to IDD field `Rated Coil Cooling Capacity`"""
        self["Rated Coil Cooling Capacity"] = value

    @property
    def operating_temperature(self):
        """field `Operating Temperature`

        |  Units: C
        |  value < 20.0

        Args:
            value (float): value for IDD Field `Operating Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `operating_temperature` or None if not set

        """
        return self["Operating Temperature"]

    @operating_temperature.setter
    def operating_temperature(self, value=None):
        """Corresponds to IDD field `Operating Temperature`"""
        self["Operating Temperature"] = value

    @property
    def rated_cooling_source_temperature(self):
        """field `Rated Cooling Source Temperature`

        |  If DXEvaporator, use evaporating temperature (saturated suction temperature)
        |  If BrineCoil, use Brine entering temperature
        |  used to set minimum suction pressure for DX systems and
        |  minimum brine temp for secondary systems
        |  Units: C
        |  value >= -70.0
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Rated Cooling Source Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_cooling_source_temperature` or None if not set

        """
        return self["Rated Cooling Source Temperature"]

    @rated_cooling_source_temperature.setter
    def rated_cooling_source_temperature(self, value=None):
        """Corresponds to IDD field `Rated Cooling Source Temperature`"""
        self["Rated Cooling Source Temperature"] = value

    @property
    def rated_total_heating_power(self):
        """field `Rated Total Heating Power`

        |  Include total for all anti-sweat, door, drip-pan, and floor heater power
        |  Do not include defrost heater power
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Total Heating Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_total_heating_power` or None if not set

        """
        return self["Rated Total Heating Power"]

    @rated_total_heating_power.setter
    def rated_total_heating_power(self, value=None):
        """Corresponds to IDD field `Rated Total Heating Power`"""
        self["Rated Total Heating Power"] = value

    @property
    def heating_power_schedule_name(self):
        """field `Heating Power Schedule Name`

        |  Values will be used to multiply the total heating power
        |  Values in the schedule should be between 0.0 and 1.0
        |  For example, this could be used if display door antisweat heaters
        |  are turned off at night
        |  Defaults to always on if schedule name left blank.

        Args:
            value (str): value for IDD Field `Heating Power Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_power_schedule_name` or None if not set

        """
        return self["Heating Power Schedule Name"]

    @heating_power_schedule_name.setter
    def heating_power_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Power Schedule Name`"""
        self["Heating Power Schedule Name"] = value

    @property
    def rated_cooling_coil_fan_power(self):
        """field `Rated Cooling Coil Fan Power`

        |  Units: W
        |  Default value: 375.0

        Args:
            value (float): value for IDD Field `Rated Cooling Coil Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_cooling_coil_fan_power` or None if not set

        """
        return self["Rated Cooling Coil Fan Power"]

    @rated_cooling_coil_fan_power.setter
    def rated_cooling_coil_fan_power(self, value=375.0):
        """Corresponds to IDD field `Rated Cooling Coil Fan Power`"""
        self["Rated Cooling Coil Fan Power"] = value

    @property
    def rated_circulation_fan_power(self):
        """field `Rated Circulation Fan Power`

        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Circulation Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_circulation_fan_power` or None if not set

        """
        return self["Rated Circulation Fan Power"]

    @rated_circulation_fan_power.setter
    def rated_circulation_fan_power(self, value=None):
        """Corresponds to IDD field `Rated Circulation Fan Power`"""
        self["Rated Circulation Fan Power"] = value

    @property
    def rated_total_lighting_power(self):
        """field `Rated Total Lighting Power`

        |  Enter the total (display + task) installed lighting power.
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Total Lighting Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_total_lighting_power` or None if not set

        """
        return self["Rated Total Lighting Power"]

    @rated_total_lighting_power.setter
    def rated_total_lighting_power(self, value=None):
        """Corresponds to IDD field `Rated Total Lighting Power`"""
        self["Rated Total Lighting Power"] = value

    @property
    def lighting_schedule_name(self):
        """field `Lighting Schedule Name`

        |  The schedule should contain values between 0 and 1
        |  Defaults to always on if schedule name left blank.

        Args:
            value (str): value for IDD Field `Lighting Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `lighting_schedule_name` or None if not set

        """
        return self["Lighting Schedule Name"]

    @lighting_schedule_name.setter
    def lighting_schedule_name(self, value=None):
        """Corresponds to IDD field `Lighting Schedule Name`"""
        self["Lighting Schedule Name"] = value

    @property
    def defrost_type(self):
        """field `Defrost Type`

        |  HotFluid includes either hot gas defrost for a DX system or
        |  Hot Brine defrost if this walk in is cooled by brine from a secondary chiller
        |  Default value: Electric

        Args:
            value (str): value for IDD Field `Defrost Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_type` or None if not set

        """
        return self["Defrost Type"]

    @defrost_type.setter
    def defrost_type(self, value="Electric"):
        """Corresponds to IDD field `Defrost Type`"""
        self["Defrost Type"] = value

    @property
    def defrost_control_type(self):
        """field `Defrost Control Type`

        |  Default value: TimeSchedule

        Args:
            value (str): value for IDD Field `Defrost Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_control_type` or None if not set

        """
        return self["Defrost Control Type"]

    @defrost_control_type.setter
    def defrost_control_type(self, value="TimeSchedule"):
        """Corresponds to IDD field `Defrost Control Type`"""
        self["Defrost Control Type"] = value

    @property
    def defrost_schedule_name(self):
        """field `Defrost Schedule Name`

        |  The schedule values should be 0 (off) or 1 (on)

        Args:
            value (str): value for IDD Field `Defrost Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_schedule_name` or None if not set

        """
        return self["Defrost Schedule Name"]

    @defrost_schedule_name.setter
    def defrost_schedule_name(self, value=None):
        """Corresponds to IDD field `Defrost Schedule Name`"""
        self["Defrost Schedule Name"] = value

    @property
    def defrost_dripdown_schedule_name(self):
        """field `Defrost Drip-Down Schedule Name`

        |  The schedule values should be 0 (off) or 1 (on)
        |  The start time for each defrost period in this drip-down schedule should coincide with
        |  the start time for each defrost period in the defrost schedule (previous input
        |  field).The length of each defrost drip-down period must be greater than or equal to the
        |  corresponding defrost period specified in the defrost schedule. This extra time
        |  allows the melted frost to drip from the coil before refrigeration is restarted.

        Args:
            value (str): value for IDD Field `Defrost Drip-Down Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_dripdown_schedule_name` or None if not set
        """
        return self["Defrost Drip-Down Schedule Name"]

    @defrost_dripdown_schedule_name.setter
    def defrost_dripdown_schedule_name(self, value=None):
        """  Corresponds to IDD field `Defrost Drip-Down Schedule Name`

        """
        self["Defrost Drip-Down Schedule Name"] = value

    @property
    def defrost_power(self):
        """field `Defrost Power`

        |  needed for all defrost types except none and offcycle
        |  Units: W

        Args:
            value (float): value for IDD Field `Defrost Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `defrost_power` or None if not set

        """
        return self["Defrost Power"]

    @defrost_power.setter
    def defrost_power(self, value=None):
        """Corresponds to IDD field `Defrost Power`"""
        self["Defrost Power"] = value

    @property
    def temperature_termination_defrost_fraction_to_ice(self):
        """field `Temperature Termination Defrost Fraction to Ice`

        |  This is the portion of the defrost energy that is available to melt frost
        |  Needed only for defrost control type TemperatureTermination
        |  defaults to 0.7 for electric defrost and to 0.3 for hot fluid defrost
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Temperature Termination Defrost Fraction to Ice`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_termination_defrost_fraction_to_ice` or None if not set

        """
        return self["Temperature Termination Defrost Fraction to Ice"]

    @temperature_termination_defrost_fraction_to_ice.setter
    def temperature_termination_defrost_fraction_to_ice(self, value=None):
        """Corresponds to IDD field `Temperature Termination Defrost Fraction
        to Ice`"""
        self["Temperature Termination Defrost Fraction to Ice"] = value

    @property
    def restocking_schedule_name(self):
        """field `Restocking Schedule Name`

        |  Schedule values should be in units of Watts
        |  Leave this field blank if no restocking is to be modeled

        Args:
            value (str): value for IDD Field `Restocking Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `restocking_schedule_name` or None if not set

        """
        return self["Restocking Schedule Name"]

    @restocking_schedule_name.setter
    def restocking_schedule_name(self, value=None):
        """Corresponds to IDD field `Restocking Schedule Name`"""
        self["Restocking Schedule Name"] = value

    @property
    def average_refrigerant_charge_inventory(self):
        """field `Average Refrigerant Charge Inventory`

        |  This value is only used if the Cooling Source Type is DXEvaporator
        |  Units: kg

        Args:
            value (float): value for IDD Field `Average Refrigerant Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_refrigerant_charge_inventory` or None if not set

        """
        return self["Average Refrigerant Charge Inventory"]

    @average_refrigerant_charge_inventory.setter
    def average_refrigerant_charge_inventory(self, value=None):
        """Corresponds to IDD field `Average Refrigerant Charge Inventory`"""
        self["Average Refrigerant Charge Inventory"] = value

    @property
    def insulated_floor_surface_area(self):
        """field `Insulated Floor Surface Area`

        |  floor area of walk-in cooler
        |  Units: m2

        Args:
            value (float): value for IDD Field `Insulated Floor Surface Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `insulated_floor_surface_area` or None if not set

        """
        return self["Insulated Floor Surface Area"]

    @insulated_floor_surface_area.setter
    def insulated_floor_surface_area(self, value=None):
        """Corresponds to IDD field `Insulated Floor Surface Area`"""
        self["Insulated Floor Surface Area"] = value

    @property
    def insulated_floor_uvalue(self):
        """field `Insulated Floor U-Value`

        |  The default value corresponds to R18 [ft2-F-hr/Btu]
        |  To convert other IP R-values to U, divide 5.678 by the R-value
        |  Some examples:
        |  R15 is U 0.3785 W/m2-K
        |  R5 is U 1.136 W/m2-K
        |  Units: W/m2-K
        |  Default value: 0.3154

        Args:
            value (float): value for IDD Field `Insulated Floor U-Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `insulated_floor_uvalue` or None if not set
        """
        return self["Insulated Floor U-Value"]

    @insulated_floor_uvalue.setter
    def insulated_floor_uvalue(self, value=0.3154):
        """  Corresponds to IDD field `Insulated Floor U-Value`

        """
        self["Insulated Floor U-Value"] = value

    def add_extensible(
        self,
        zone_1_name=None,
        total_insulated_surface_area_facing_zone_1=None,
        insulated_surface_uvalue_facing_zone_1=0.3154,
        area_of_glass_reach_in_doors_facing_zone_1=None,
        height_of_glass_reach_in_doors_facing_zone_1=1.5,
        glass_reach_in_door_u_value_facing_zone_1=1.136,
        glass_reach_in_door_opening_schedule_name_facing_zone_1=None,
        area_of_stocking_doors_facing_zone_1=None,
        height_of_stocking_doors_facing_zone_1=3.0,
        stocking_door_u_value_facing_zone_1=0.3785,
        stocking_door_opening_schedule_name_facing_zone_1=None,
        stocking_door_opening_protection_type_facing_zone_1="AirCurtain",
    ):
        """Add values for extensible fields.

        Args:

            zone_1_name (str): value for IDD Field `Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            total_insulated_surface_area_facing_zone_1 (float): value for IDD Field `Total Insulated Surface Area Facing Zone 1`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            insulated_surface_uvalue_facing_zone_1 (float): value for IDD Field `Insulated Surface U-Value Facing Zone 1`
                Units: W/m2-K
                Default value: 0.3154
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            area_of_glass_reach_in_doors_facing_zone_1 (float): value for IDD Field `Area of Glass Reach In Doors Facing Zone 1`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            height_of_glass_reach_in_doors_facing_zone_1 (float): value for IDD Field `Height of Glass Reach In Doors Facing Zone 1`
                Units: m
                Default value: 1.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            glass_reach_in_door_u_value_facing_zone_1 (float): value for IDD Field `Glass Reach In Door U Value Facing Zone 1`
                Units: W/m2-K
                Default value: 1.136
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            glass_reach_in_door_opening_schedule_name_facing_zone_1 (str): value for IDD Field `Glass Reach In Door Opening Schedule Name Facing Zone 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            area_of_stocking_doors_facing_zone_1 (float): value for IDD Field `Area of Stocking Doors Facing Zone 1`
                Units: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            height_of_stocking_doors_facing_zone_1 (float): value for IDD Field `Height of Stocking Doors Facing Zone 1`
                Units: m
                Default value: 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            stocking_door_u_value_facing_zone_1 (float): value for IDD Field `Stocking Door U Value Facing Zone 1`
                Units: W/m2-K
                Default value: 0.3785
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            stocking_door_opening_schedule_name_facing_zone_1 (str): value for IDD Field `Stocking Door Opening Schedule Name Facing Zone 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            stocking_door_opening_protection_type_facing_zone_1 (str): value for IDD Field `Stocking Door Opening Protection Type Facing Zone 1`
                Default value: AirCurtain
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        zone_1_name = self.check_value("Zone 1 Name", zone_1_name)
        vals.append(zone_1_name)
        total_insulated_surface_area_facing_zone_1 = self.check_value(
            "Total Insulated Surface Area Facing Zone 1",
            total_insulated_surface_area_facing_zone_1)
        vals.append(total_insulated_surface_area_facing_zone_1)
        insulated_surface_uvalue_facing_zone_1 = self.check_value(
            "Insulated Surface U-Value Facing Zone 1",
            insulated_surface_uvalue_facing_zone_1)
        vals.append(insulated_surface_uvalue_facing_zone_1)
        area_of_glass_reach_in_doors_facing_zone_1 = self.check_value(
            "Area of Glass Reach In Doors Facing Zone 1",
            area_of_glass_reach_in_doors_facing_zone_1)
        vals.append(area_of_glass_reach_in_doors_facing_zone_1)
        height_of_glass_reach_in_doors_facing_zone_1 = self.check_value(
            "Height of Glass Reach In Doors Facing Zone 1",
            height_of_glass_reach_in_doors_facing_zone_1)
        vals.append(height_of_glass_reach_in_doors_facing_zone_1)
        glass_reach_in_door_u_value_facing_zone_1 = self.check_value(
            "Glass Reach In Door U Value Facing Zone 1",
            glass_reach_in_door_u_value_facing_zone_1)
        vals.append(glass_reach_in_door_u_value_facing_zone_1)
        glass_reach_in_door_opening_schedule_name_facing_zone_1 = self.check_value(
            "Glass Reach In Door Opening Schedule Name Facing Zone 1",
            glass_reach_in_door_opening_schedule_name_facing_zone_1)
        vals.append(glass_reach_in_door_opening_schedule_name_facing_zone_1)
        area_of_stocking_doors_facing_zone_1 = self.check_value(
            "Area of Stocking Doors Facing Zone 1",
            area_of_stocking_doors_facing_zone_1)
        vals.append(area_of_stocking_doors_facing_zone_1)
        height_of_stocking_doors_facing_zone_1 = self.check_value(
            "Height of Stocking Doors Facing Zone 1",
            height_of_stocking_doors_facing_zone_1)
        vals.append(height_of_stocking_doors_facing_zone_1)
        stocking_door_u_value_facing_zone_1 = self.check_value(
            "Stocking Door U Value Facing Zone 1",
            stocking_door_u_value_facing_zone_1)
        vals.append(stocking_door_u_value_facing_zone_1)
        stocking_door_opening_schedule_name_facing_zone_1 = self.check_value(
            "Stocking Door Opening Schedule Name Facing Zone 1",
            stocking_door_opening_schedule_name_facing_zone_1)
        vals.append(stocking_door_opening_schedule_name_facing_zone_1)
        stocking_door_opening_protection_type_facing_zone_1 = self.check_value(
            "Stocking Door Opening Protection Type Facing Zone 1",
            stocking_door_opening_protection_type_facing_zone_1)
        vals.append(stocking_door_opening_protection_type_facing_zone_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class RefrigerationAirChiller(DataObject):

    """ Corresponds to IDD object `Refrigeration:AirChiller`
        Works in conjunction with a refrigeration chiller set, compressor rack, a
        refrigeration system, or a refrigeration secondary system to simulate the performance
        of an air chiller, similar to one found in a refrigerated warehouse. Energy use for
        fans and heaters is modeled based on inputs for nominal power, schedules, and control
        type. The air chiller model accounts for the sensible and latent heat exchange
        with the surrounding environment.
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
                                      (u'capacity rating type',
                                       {'name': u'Capacity Rating Type',
                                        'pyname': u'capacity_rating_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'UnitLoadFactorSensibleOnly',
                                                            u'CapacityTotalSpecificConditions',
                                                            u'EuropeanSC1Standard',
                                                            u'EuropeanSC1NominalWet',
                                                            u'EuropeanSC2Standard',
                                                            u'EuropeanSC2NominalWet',
                                                            u'EuropeanSC3Standard',
                                                            u'FixedLinear',
                                                            u'EuropeanSC3NominalWet',
                                                            u'EuropeanSC4Standard',
                                                            u'EuropeanSC4NominalWet',
                                                            u'EuropeanSC5Standard',
                                                            u'EuropeanSC5NominalWet'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'rated unit load factor',
                                       {'name': u'Rated Unit Load Factor',
                                        'pyname': u'rated_unit_load_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'rated capacity',
                                       {'name': u'Rated Capacity',
                                        'pyname': u'rated_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated relative humidity',
                                       {'name': u'Rated Relative Humidity',
                                        'pyname': u'rated_relative_humidity',
                                        'default': 85.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'rated cooling source temperature',
                                       {'name': u'Rated Cooling Source Temperature',
                                        'pyname': u'rated_cooling_source_temperature',
                                        'maximum': 40.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated temperature difference dt1',
                                       {'name': u'Rated Temperature Difference DT1',
                                        'pyname': u'rated_temperature_difference_dt1',
                                        'maximum': 20.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum temperature difference between inlet air and evaporating temperature',
                                       {'name': u'Maximum Temperature Difference Between Inlet Air and Evaporating Temperature',
                                        'pyname': u'maximum_temperature_difference_between_inlet_air_and_evaporating_temperature',
                                        'maximum': 25.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'coil material correction factor',
                                       {'name': u'Coil Material Correction Factor',
                                        'pyname': u'coil_material_correction_factor',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'refrigerant correction factor',
                                       {'name': u'Refrigerant Correction Factor',
                                        'pyname': u'refrigerant_correction_factor',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'capacity correction curve type',
                                       {'name': u'Capacity Correction Curve Type',
                                        'pyname': u'capacity_correction_curve_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LinearSHR60',
                                                            u'QuadraticSHR',
                                                            u'European',
                                                            u'TabularRHxDT1xTRoom'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'capacity correction curve name',
                                       {'name': u'Capacity Correction Curve Name',
                                        'pyname': u'capacity_correction_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'shr60 correction factor',
                                       {'name': u'SHR60 Correction Factor',
                                        'pyname': u'shr60_correction_factor',
                                        'default': 1.48,
                                        'maximum': 1.67,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'rated total heating power',
                                       {'name': u'Rated Total Heating Power',
                                        'pyname': u'rated_total_heating_power',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating power schedule name',
                                       {'name': u'Heating Power Schedule Name',
                                        'pyname': u'heating_power_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan speed control type',
                                       {'name': u'Fan Speed Control Type',
                                        'pyname': u'fan_speed_control_type',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'FixedLinear',
                                                            u'VariableSpeed',
                                                            u'TwoSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'rated fan power',
                                       {'name': u'Rated Fan Power',
                                        'pyname': u'rated_fan_power',
                                        'default': 375.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated air flow',
                                       {'name': u'Rated Air Flow',
                                        'pyname': u'rated_air_flow',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum fan air flow ratio',
                                       {'name': u'Minimum Fan Air Flow Ratio',
                                        'pyname': u'minimum_fan_air_flow_ratio',
                                        'default': 0.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'defrost type',
                                       {'name': u'Defrost Type',
                                        'pyname': u'defrost_type',
                                        'default': u'Electric',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'HotFluid',
                                                            u'Electric',
                                                            u'None',
                                                            u'OffCycle'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost control type',
                                       {'name': u'Defrost Control Type',
                                        'pyname': u'defrost_control_type',
                                        'default': u'TimeSchedule',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'TimeSchedule',
                                                            u'TemperatureTermination'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost schedule name',
                                       {'name': u'Defrost Schedule Name',
                                        'pyname': u'defrost_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost drip-down schedule name',
                                       {'name': u'Defrost Drip-Down Schedule Name',
                                        'pyname': u'defrost_dripdown_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost power',
                                       {'name': u'Defrost Power',
                                        'pyname': u'defrost_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'temperature termination defrost fraction to ice',
                                       {'name': u'Temperature Termination Defrost Fraction to Ice',
                                        'pyname': u'temperature_termination_defrost_fraction_to_ice',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'vertical location',
                                       {'name': u'Vertical Location',
                                        'pyname': u'vertical_location',
                                        'default': u'Middle',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Ceiling',
                                                            u'Middle',
                                                            u'Floor'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'average refrigerant charge inventory',
                                       {'name': u'Average Refrigerant Charge Inventory',
                                        'pyname': u'average_refrigerant_charge_inventory',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 23,
               'name': u'Refrigeration:AirChiller',
               'pyname': u'RefrigerationAirChiller',
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
    def capacity_rating_type(self):
        """field `Capacity Rating Type`

        |  In each case, select the rating option that corresponds to the expected service conditions.
        |  For example, U.S. manufacturers quote a separate Unit Load Factor for wet or frosted coils.
        |  If the evaporating temperature is less than 0C, input the frosted coil value.
        |  Within the European convention, select SC1, 2, 3, 4, or 5 depending upon the expected evaporating temperature.

        Args:
            value (str): value for IDD Field `Capacity Rating Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `capacity_rating_type` or None if not set

        """
        return self["Capacity Rating Type"]

    @capacity_rating_type.setter
    def capacity_rating_type(self, value=None):
        """Corresponds to IDD field `Capacity Rating Type`"""
        self["Capacity Rating Type"] = value

    @property
    def rated_unit_load_factor(self):
        """field `Rated Unit Load Factor`

        |  The sensible cooling capacity in watts (W/C) at rated conditions.
        |  The value entered for this field must be greater than zero, with no default value.
        |  This value is only used if the Capacity Rating Type is UnitLoadFactorSensibleOnly.
        |  The value given must be based upon the difference between the chiller inlet and
        |  outlet air temperatures, not on the difference between the zone mean temperature
        |  and the outlet air temperature
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Rated Unit Load Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_unit_load_factor` or None if not set

        """
        return self["Rated Unit Load Factor"]

    @rated_unit_load_factor.setter
    def rated_unit_load_factor(self, value=None):
        """Corresponds to IDD field `Rated Unit Load Factor`"""
        self["Rated Unit Load Factor"] = value

    @property
    def rated_capacity(self):
        """field `Rated Capacity`

        |  This value is only used if the Capacity Rating Type is NOT UnitLoadFactorSensibleOnly.
        |  For CapacityTotalSpecificConditions, this capacity includes both sensible and latent
        |  at the conditions given in the next two fields.
        |  Note that the European Standard ratings are sensible only and
        |  the European Nominal ratings include latent capacity as well.
        |  The value given here must correspond to the capacity rating type given previously
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_capacity` or None if not set

        """
        return self["Rated Capacity"]

    @rated_capacity.setter
    def rated_capacity(self, value=None):
        """Corresponds to IDD field `Rated Capacity`"""
        self["Rated Capacity"] = value

    @property
    def rated_relative_humidity(self):
        """field `Rated Relative Humidity`

        |  This field is ONLY used if the Capacity Rating Type is CapacityTotalSpecificConditions and
        |  represents the relative humidity at rated conditions. The default is 85.
        |  Units: percent
        |  Default value: 85.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Rated Relative Humidity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_relative_humidity` or None if not set

        """
        return self["Rated Relative Humidity"]

    @rated_relative_humidity.setter
    def rated_relative_humidity(self, value=85.0):
        """Corresponds to IDD field `Rated Relative Humidity`"""
        self["Rated Relative Humidity"] = value

    @property
    def rated_cooling_source_temperature(self):
        """field `Rated Cooling Source Temperature`

        |  If DXEvaporator, use evaporating temperature (saturated suction temperature)
        |  If BrineCoil, use Brine entering temperature
        |  used to set minimum suction pressure for DX systems and
        |  minimum brine temp for secondary systems
        |  Units: C
        |  value >= -70.0
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Rated Cooling Source Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_cooling_source_temperature` or None if not set

        """
        return self["Rated Cooling Source Temperature"]

    @rated_cooling_source_temperature.setter
    def rated_cooling_source_temperature(self, value=None):
        """Corresponds to IDD field `Rated Cooling Source Temperature`"""
        self["Rated Cooling Source Temperature"] = value

    @property
    def rated_temperature_difference_dt1(self):
        """field `Rated Temperature Difference DT1`

        |  The rated difference between the air entering the refrigeration chiller and the
        |  cooling source temperature in degC.
        |  Units: deltaC
        |  value <= 20.0

        Args:
            value (float): value for IDD Field `Rated Temperature Difference DT1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_temperature_difference_dt1` or None if not set

        """
        return self["Rated Temperature Difference DT1"]

    @rated_temperature_difference_dt1.setter
    def rated_temperature_difference_dt1(self, value=None):
        """Corresponds to IDD field `Rated Temperature Difference DT1`"""
        self["Rated Temperature Difference DT1"] = value

    @property
    def maximum_temperature_difference_between_inlet_air_and_evaporating_temperature(
            self):
        """field `Maximum Temperature Difference Between Inlet Air and
        Evaporating Temperature`

        |  The maximum difference between the air entering the refrigeration chiller and the
        |  cooling source temperature in degC used to limit capacity during pull-down.
        |  defaults to 1.3 times the Rated Temperature Difference DT1
        |  Units: deltaC
        |  value <= 25.0

        Args:
            value (float): value for IDD Field `Maximum Temperature Difference Between Inlet Air and Evaporating Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_temperature_difference_between_inlet_air_and_evaporating_temperature` or None if not set

        """
        return self[
            "Maximum Temperature Difference Between Inlet Air and Evaporating Temperature"]

    @maximum_temperature_difference_between_inlet_air_and_evaporating_temperature.setter
    def maximum_temperature_difference_between_inlet_air_and_evaporating_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Temperature Difference Between
        Inlet Air and Evaporating Temperature`"""
        self[
            "Maximum Temperature Difference Between Inlet Air and Evaporating Temperature"] = value

    @property
    def coil_material_correction_factor(self):
        """field `Coil Material Correction Factor`

        |  This is the manufacturer's correction factor for coil material corresponding to rating
        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Coil Material Correction Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coil_material_correction_factor` or None if not set

        """
        return self["Coil Material Correction Factor"]

    @coil_material_correction_factor.setter
    def coil_material_correction_factor(self, value=1.0):
        """Corresponds to IDD field `Coil Material Correction Factor`"""
        self["Coil Material Correction Factor"] = value

    @property
    def refrigerant_correction_factor(self):
        """field `Refrigerant Correction Factor`

        |  This is the manufacturer's correction factor for refrigerant corresponding to rating
        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Refrigerant Correction Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `refrigerant_correction_factor` or None if not set

        """
        return self["Refrigerant Correction Factor"]

    @refrigerant_correction_factor.setter
    def refrigerant_correction_factor(self, value=1.0):
        """Corresponds to IDD field `Refrigerant Correction Factor`"""
        self["Refrigerant Correction Factor"] = value

    @property
    def capacity_correction_curve_type(self):
        """field `Capacity Correction Curve Type`

        |  In each case, select the correction curve type that corresponds to the rating type.
        |  default LinearSHR60 unless Capacity Rating Type = CapacityTotalSpecificConditions

        Args:
            value (str): value for IDD Field `Capacity Correction Curve Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `capacity_correction_curve_type` or None if not set

        """
        return self["Capacity Correction Curve Type"]

    @capacity_correction_curve_type.setter
    def capacity_correction_curve_type(self, value=None):
        """Corresponds to IDD field `Capacity Correction Curve Type`"""
        self["Capacity Correction Curve Type"] = value

    @property
    def capacity_correction_curve_name(self):
        """field `Capacity Correction Curve Name`

        |  Can also be the name of a "Table:OneIndependentVariable" or a "Table:MultiVariableLookup"
        |  Should be blank for LinearSHR60 correction curve type

        Args:
            value (str): value for IDD Field `Capacity Correction Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `capacity_correction_curve_name` or None if not set

        """
        return self["Capacity Correction Curve Name"]

    @capacity_correction_curve_name.setter
    def capacity_correction_curve_name(self, value=None):
        """Corresponds to IDD field `Capacity Correction Curve Name`"""
        self["Capacity Correction Curve Name"] = value

    @property
    def shr60_correction_factor(self):
        """field `SHR60 Correction Factor`

        |  only used when the capacity correction curve type is LinearSHR60
        |  Units: dimensionless
        |  Default value: 1.48
        |  value <= 1.67

        Args:
            value (float): value for IDD Field `SHR60 Correction Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shr60_correction_factor` or None if not set

        """
        return self["SHR60 Correction Factor"]

    @shr60_correction_factor.setter
    def shr60_correction_factor(self, value=1.48):
        """Corresponds to IDD field `SHR60 Correction Factor`"""
        self["SHR60 Correction Factor"] = value

    @property
    def rated_total_heating_power(self):
        """field `Rated Total Heating Power`

        |  Include total for all heater power
        |  Do not include defrost heater power
        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Total Heating Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_total_heating_power` or None if not set

        """
        return self["Rated Total Heating Power"]

    @rated_total_heating_power.setter
    def rated_total_heating_power(self, value=None):
        """Corresponds to IDD field `Rated Total Heating Power`"""
        self["Rated Total Heating Power"] = value

    @property
    def heating_power_schedule_name(self):
        """field `Heating Power Schedule Name`

        |  Values will be used to multiply the total heating power
        |  Values in the schedule should be between 0.0 and 1.0
        |  Defaults to always on if schedule name left blank.

        Args:
            value (str): value for IDD Field `Heating Power Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_power_schedule_name` or None if not set

        """
        return self["Heating Power Schedule Name"]

    @heating_power_schedule_name.setter
    def heating_power_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Power Schedule Name`"""
        self["Heating Power Schedule Name"] = value

    @property
    def fan_speed_control_type(self):
        """field `Fan Speed Control Type`

        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Fan Speed Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_speed_control_type` or None if not set

        """
        return self["Fan Speed Control Type"]

    @fan_speed_control_type.setter
    def fan_speed_control_type(self, value="Fixed"):
        """Corresponds to IDD field `Fan Speed Control Type`"""
        self["Fan Speed Control Type"] = value

    @property
    def rated_fan_power(self):
        """field `Rated Fan Power`

        |  Units: W
        |  Default value: 375.0

        Args:
            value (float): value for IDD Field `Rated Fan Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_fan_power` or None if not set

        """
        return self["Rated Fan Power"]

    @rated_fan_power.setter
    def rated_fan_power(self, value=375.0):
        """Corresponds to IDD field `Rated Fan Power`"""
        self["Rated Fan Power"] = value

    @property
    def rated_air_flow(self):
        """field `Rated Air Flow`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Rated Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_air_flow` or None if not set

        """
        return self["Rated Air Flow"]

    @rated_air_flow.setter
    def rated_air_flow(self, value=None):
        """Corresponds to IDD field `Rated Air Flow`"""
        self["Rated Air Flow"] = value

    @property
    def minimum_fan_air_flow_ratio(self):
        """field `Minimum Fan Air Flow Ratio`

        |  Minimum air flow fraction through fan
        |  Units: dimensionless
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Minimum Fan Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_fan_air_flow_ratio` or None if not set

        """
        return self["Minimum Fan Air Flow Ratio"]

    @minimum_fan_air_flow_ratio.setter
    def minimum_fan_air_flow_ratio(self, value=0.2):
        """Corresponds to IDD field `Minimum Fan Air Flow Ratio`"""
        self["Minimum Fan Air Flow Ratio"] = value

    @property
    def defrost_type(self):
        """field `Defrost Type`

        |  HotFluid includes either hot gas defrost for a DX system or
        |  Hot Brine defrost if this walk in is cooled by brine from a secondary chiller
        |  Default value: Electric

        Args:
            value (str): value for IDD Field `Defrost Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_type` or None if not set

        """
        return self["Defrost Type"]

    @defrost_type.setter
    def defrost_type(self, value="Electric"):
        """Corresponds to IDD field `Defrost Type`"""
        self["Defrost Type"] = value

    @property
    def defrost_control_type(self):
        """field `Defrost Control Type`

        |  Default value: TimeSchedule

        Args:
            value (str): value for IDD Field `Defrost Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_control_type` or None if not set

        """
        return self["Defrost Control Type"]

    @defrost_control_type.setter
    def defrost_control_type(self, value="TimeSchedule"):
        """Corresponds to IDD field `Defrost Control Type`"""
        self["Defrost Control Type"] = value

    @property
    def defrost_schedule_name(self):
        """field `Defrost Schedule Name`

        |  The schedule values should be 0 (off) or 1 (on)

        Args:
            value (str): value for IDD Field `Defrost Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_schedule_name` or None if not set

        """
        return self["Defrost Schedule Name"]

    @defrost_schedule_name.setter
    def defrost_schedule_name(self, value=None):
        """Corresponds to IDD field `Defrost Schedule Name`"""
        self["Defrost Schedule Name"] = value

    @property
    def defrost_dripdown_schedule_name(self):
        """field `Defrost Drip-Down Schedule Name`

        |  The schedule values should be 0 (off) or 1 (on)
        |  The start time for each defrost period in this drip-down schedule should coincide with
        |  the start time for each defrost period in the defrost schedule (previous input
        |  field).The length of each defrost drip-down period must be greater than or equal to the
        |  corresponding defrost period specified in the defrost schedule. This extra time
        |  allows the melted frost to drip from the coil before refrigeration is restarted.

        Args:
            value (str): value for IDD Field `Defrost Drip-Down Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_dripdown_schedule_name` or None if not set
        """
        return self["Defrost Drip-Down Schedule Name"]

    @defrost_dripdown_schedule_name.setter
    def defrost_dripdown_schedule_name(self, value=None):
        """  Corresponds to IDD field `Defrost Drip-Down Schedule Name`

        """
        self["Defrost Drip-Down Schedule Name"] = value

    @property
    def defrost_power(self):
        """field `Defrost Power`

        |  needed for all defrost types except none and offcycle
        |  Units: W

        Args:
            value (float): value for IDD Field `Defrost Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `defrost_power` or None if not set

        """
        return self["Defrost Power"]

    @defrost_power.setter
    def defrost_power(self, value=None):
        """Corresponds to IDD field `Defrost Power`"""
        self["Defrost Power"] = value

    @property
    def temperature_termination_defrost_fraction_to_ice(self):
        """field `Temperature Termination Defrost Fraction to Ice`

        |  This is the portion of the defrost energy that is available to melt frost
        |  Needed only for defrost control type TemperatureTermination
        |  defaults to 0.7 for electric defrost and to 0.3 for hot fluid defrost
        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Temperature Termination Defrost Fraction to Ice`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_termination_defrost_fraction_to_ice` or None if not set

        """
        return self["Temperature Termination Defrost Fraction to Ice"]

    @temperature_termination_defrost_fraction_to_ice.setter
    def temperature_termination_defrost_fraction_to_ice(self, value=None):
        """Corresponds to IDD field `Temperature Termination Defrost Fraction
        to Ice`"""
        self["Temperature Termination Defrost Fraction to Ice"] = value

    @property
    def vertical_location(self):
        """field `Vertical Location`

        |  Default value: Middle

        Args:
            value (str): value for IDD Field `Vertical Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `vertical_location` or None if not set

        """
        return self["Vertical Location"]

    @vertical_location.setter
    def vertical_location(self, value="Middle"):
        """Corresponds to IDD field `Vertical Location`"""
        self["Vertical Location"] = value

    @property
    def average_refrigerant_charge_inventory(self):
        """field `Average Refrigerant Charge Inventory`

        |  This value is only used if the Cooling Source Type is DXEvaporator
        |  Units: kg

        Args:
            value (float): value for IDD Field `Average Refrigerant Charge Inventory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_refrigerant_charge_inventory` or None if not set

        """
        return self["Average Refrigerant Charge Inventory"]

    @average_refrigerant_charge_inventory.setter
    def average_refrigerant_charge_inventory(self, value=None):
        """Corresponds to IDD field `Average Refrigerant Charge Inventory`"""
        self["Average Refrigerant Charge Inventory"] = value




class ZoneHvacRefrigerationChillerSet(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:RefrigerationChillerSet`
        Works in conjunction with one or multiple air chillers, compressor racks,
        refrigeration systems, or refrigeration secondary system objects to simulate the
        performance of a group of air chillers cooling a single zone. The chiller set
        model passes information about the zone conditions to determine the performance of
        individual chiller coils within the set, thus providing the sensible and latent heat
        exchange with the zone environment.
    """
    _schema = {'extensible-fields': OrderedDict([(u'air chiller  name',
                                                  {'name': u'Air Chiller  Name',
                                                   'pyname': u'air_chiller_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
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
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
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
                                        'type': u'node'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 6,
               'name': u'ZoneHVAC:RefrigerationChillerSet',
               'pyname': u'ZoneHvacRefrigerationChillerSet',
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
    def zone_name(self):
        """field `Zone Name`

        |  This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  Not used - reserved for future use
        |  Name of the zone exhaust node (see Node) from which the refrigeration chiller
        |  draws its indoor air.
        |  This should be one of the zone exhaust nodes for the zone cooled by the chiller set.

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

        |  Not used - reserved for future use
        |  The name of the node where the chiller coil sends its outlet air,
        |  which must be one of the inlet air nodes for the zone which is being cooled.

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

    def add_extensible(self,
                       air_chiller_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            air_chiller_name (str): value for IDD Field `Air Chiller  Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        air_chiller_name = self.check_value(
            "Air Chiller  Name",
            air_chiller_name)
        vals.append(air_chiller_name)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class MatrixTwoDimension(DataObject):

    """ Corresponds to IDD object `Matrix:TwoDimension`
        matrix data in row-major order
        list each row keeping the columns in order
        number of values must equal N1 x N2
    """
    _schema = {'extensible-fields': OrderedDict([(u'value',
                                                  {'name': u'Value',
                                                   'pyname': u'value',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'number of rows',
                                       {'name': u'Number of Rows',
                                        'pyname': u'number_of_rows',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of columns',
                                       {'name': u'Number of Columns',
                                        'pyname': u'number_of_columns',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Refrigeration',
               'min-fields': 0,
               'name': u'Matrix:TwoDimension',
               'pyname': u'MatrixTwoDimension',
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
    def number_of_rows(self):
        """field `Number of Rows`

        Args:
            value (int): value for IDD Field `Number of Rows`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_rows` or None if not set

        """
        return self["Number of Rows"]

    @number_of_rows.setter
    def number_of_rows(self, value=None):
        """Corresponds to IDD field `Number of Rows`"""
        self["Number of Rows"] = value

    @property
    def number_of_columns(self):
        """field `Number of Columns`

        Args:
            value (int): value for IDD Field `Number of Columns`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_columns` or None if not set

        """
        return self["Number of Columns"]

    @number_of_columns.setter
    def number_of_columns(self, value=None):
        """Corresponds to IDD field `Number of Columns`"""
        self["Number of Columns"] = value

    def add_extensible(self,
                       value=None,
                       ):
        """Add values for extensible fields.

        Args:

            value (float): value for IDD Field `Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        value = self.check_value("Value", value)
        vals.append(value)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)


