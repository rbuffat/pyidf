""" Data objects in group "Zone HVAC Forced Air Units"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ZoneHvacIdealLoadsAirSystem(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:IdealLoadsAirSystem`
        Ideal system used to calculate loads without modeling a full HVAC system. All that is
        required for the ideal system are zone controls, zone equipment configurations, and
        the ideal loads system component. This component can be thought of as an ideal unit
        that mixes zone air with the specified amount of outdoor air and then adds or removes
        heat and moisture at 100% efficiency in order to meet the specified controls. Energy
        use is reported as DistrictHeating and DistrictCooling.
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
                                      (u'zone supply air node name',
                                       {'name': u'Zone Supply Air Node Name',
                                        'pyname': u'zone_supply_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone exhaust air node name',
                                       {'name': u'Zone Exhaust Air Node Name',
                                        'pyname': u'zone_exhaust_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum heating supply air temperature',
                                       {'name': u'Maximum Heating Supply Air Temperature',
                                        'pyname': u'maximum_heating_supply_air_temperature',
                                        'default': 50.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'maximum<': 100.0,
                                        'unit': u'C'}),
                                      (u'minimum cooling supply air temperature',
                                       {'name': u'Minimum Cooling Supply Air Temperature',
                                        'pyname': u'minimum_cooling_supply_air_temperature',
                                        'default': 13.0,
                                        'minimum>': -100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'maximum<': 50.0,
                                        'unit': u'C'}),
                                      (u'maximum heating supply air humidity ratio',
                                       {'name': u'Maximum Heating Supply Air Humidity Ratio',
                                        'pyname': u'maximum_heating_supply_air_humidity_ratio',
                                        'default': 0.0156,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'minimum cooling supply air humidity ratio',
                                       {'name': u'Minimum Cooling Supply Air Humidity Ratio',
                                        'pyname': u'minimum_cooling_supply_air_humidity_ratio',
                                        'default': 0.0077,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'heating limit',
                                       {'name': u'Heating Limit',
                                        'pyname': u'heating_limit',
                                        'default': u'NoLimit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NoLimit',
                                                            u'LimitFlowRate',
                                                            u'LimitCapacity',
                                                            u'LimitFlowRateAndCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum heating air flow rate',
                                       {'name': u'Maximum Heating Air Flow Rate',
                                        'pyname': u'maximum_heating_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum sensible heating capacity',
                                       {'name': u'Maximum Sensible Heating Capacity',
                                        'pyname': u'maximum_sensible_heating_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'cooling limit',
                                       {'name': u'Cooling Limit',
                                        'pyname': u'cooling_limit',
                                        'default': u'NoLimit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NoLimit',
                                                            u'LimitFlowRate',
                                                            u'LimitCapacity',
                                                            u'LimitFlowRateAndCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum cooling air flow rate',
                                       {'name': u'Maximum Cooling Air Flow Rate',
                                        'pyname': u'maximum_cooling_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum total cooling capacity',
                                       {'name': u'Maximum Total Cooling Capacity',
                                        'pyname': u'maximum_total_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'heating availability schedule name',
                                       {'name': u'Heating Availability Schedule Name',
                                        'pyname': u'heating_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling availability schedule name',
                                       {'name': u'Cooling Availability Schedule Name',
                                        'pyname': u'cooling_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'ConstantSensibleHeatRatio',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ConstantSensibleHeatRatio',
                                                            u'Humidistat',
                                                            u'None',
                                                            u'ConstantSupplyHumidityRatio'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling sensible heat ratio',
                                       {'name': u'Cooling Sensible Heat Ratio',
                                        'pyname': u'cooling_sensible_heat_ratio',
                                        'default': 0.7,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'humidification control type',
                                       {'name': u'Humidification Control Type',
                                        'pyname': u'humidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Humidistat',
                                                            u'ConstantSupplyHumidityRatio'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design specification outdoor air object name',
                                       {'name': u'Design Specification Outdoor Air Object Name',
                                        'pyname': u'design_specification_outdoor_air_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outdoor air inlet node name',
                                       {'name': u'Outdoor Air Inlet Node Name',
                                        'pyname': u'outdoor_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'demand controlled ventilation type',
                                       {'name': u'Demand Controlled Ventilation Type',
                                        'pyname': u'demand_controlled_ventilation_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'OccupancySchedule',
                                                            u'CO2Setpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air economizer type',
                                       {'name': u'Outdoor Air Economizer Type',
                                        'pyname': u'outdoor_air_economizer_type',
                                        'default': u'NoEconomizer',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NoEconomizer',
                                                            u'DifferentialDryBulb',
                                                            u'DifferentialEnthalpy'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heat recovery type',
                                       {'name': u'Heat Recovery Type',
                                        'pyname': u'heat_recovery_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Sensible',
                                                            u'Enthalpy'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'sensible heat recovery effectiveness',
                                       {'name': u'Sensible Heat Recovery Effectiveness',
                                        'pyname': u'sensible_heat_recovery_effectiveness',
                                        'default': 0.7,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'latent heat recovery effectiveness',
                                       {'name': u'Latent Heat Recovery Effectiveness',
                                        'pyname': u'latent_heat_recovery_effectiveness',
                                        'default': 0.65,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 26,
               'name': u'ZoneHVAC:IdealLoadsAirSystem',
               'pyname': u'ZoneHvacIdealLoadsAirSystem',
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
    def zone_supply_air_node_name(self):
        """field `Zone Supply Air Node Name`

        |  Must match a zone air inlet node name.

        Args:
            value (str): value for IDD Field `Zone Supply Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_supply_air_node_name` or None if not set

        """
        return self["Zone Supply Air Node Name"]

    @zone_supply_air_node_name.setter
    def zone_supply_air_node_name(self, value=None):
        """Corresponds to IDD field `Zone Supply Air Node Name`"""
        self["Zone Supply Air Node Name"] = value

    @property
    def zone_exhaust_air_node_name(self):
        """field `Zone Exhaust Air Node Name`

        |  Should match a zone air exhaust node name.
        |  This field is optional, but is required if this
        |  this object is used with other forced air equipment.

        Args:
            value (str): value for IDD Field `Zone Exhaust Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_exhaust_air_node_name` or None if not set

        """
        return self["Zone Exhaust Air Node Name"]

    @zone_exhaust_air_node_name.setter
    def zone_exhaust_air_node_name(self, value=None):
        """Corresponds to IDD field `Zone Exhaust Air Node Name`"""
        self["Zone Exhaust Air Node Name"] = value

    @property
    def maximum_heating_supply_air_temperature(self):
        """field `Maximum Heating Supply Air Temperature`

        |  Units: C
        |  Default value: 50.0
        |  value < 100.0

        Args:
            value (float): value for IDD Field `Maximum Heating Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_heating_supply_air_temperature` or None if not set

        """
        return self["Maximum Heating Supply Air Temperature"]

    @maximum_heating_supply_air_temperature.setter
    def maximum_heating_supply_air_temperature(self, value=50.0):
        """Corresponds to IDD field `Maximum Heating Supply Air Temperature`"""
        self["Maximum Heating Supply Air Temperature"] = value

    @property
    def minimum_cooling_supply_air_temperature(self):
        """field `Minimum Cooling Supply Air Temperature`

        |  Units: C
        |  Default value: 13.0
        |  value > -100.0
        |  value < 50.0

        Args:
            value (float): value for IDD Field `Minimum Cooling Supply Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_cooling_supply_air_temperature` or None if not set

        """
        return self["Minimum Cooling Supply Air Temperature"]

    @minimum_cooling_supply_air_temperature.setter
    def minimum_cooling_supply_air_temperature(self, value=13.0):
        """Corresponds to IDD field `Minimum Cooling Supply Air Temperature`"""
        self["Minimum Cooling Supply Air Temperature"] = value

    @property
    def maximum_heating_supply_air_humidity_ratio(self):
        """field `Maximum Heating Supply Air Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.0156

        Args:
            value (float): value for IDD Field `Maximum Heating Supply Air Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_heating_supply_air_humidity_ratio` or None if not set

        """
        return self["Maximum Heating Supply Air Humidity Ratio"]

    @maximum_heating_supply_air_humidity_ratio.setter
    def maximum_heating_supply_air_humidity_ratio(self, value=0.0156):
        """Corresponds to IDD field `Maximum Heating Supply Air Humidity
        Ratio`"""
        self["Maximum Heating Supply Air Humidity Ratio"] = value

    @property
    def minimum_cooling_supply_air_humidity_ratio(self):
        """field `Minimum Cooling Supply Air Humidity Ratio`

        |  Units: kgWater/kgDryAir
        |  Default value: 0.0077

        Args:
            value (float): value for IDD Field `Minimum Cooling Supply Air Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_cooling_supply_air_humidity_ratio` or None if not set

        """
        return self["Minimum Cooling Supply Air Humidity Ratio"]

    @minimum_cooling_supply_air_humidity_ratio.setter
    def minimum_cooling_supply_air_humidity_ratio(self, value=0.0077):
        """Corresponds to IDD field `Minimum Cooling Supply Air Humidity
        Ratio`"""
        self["Minimum Cooling Supply Air Humidity Ratio"] = value

    @property
    def heating_limit(self):
        """field `Heating Limit`

        |  Default value: NoLimit

        Args:
            value (str): value for IDD Field `Heating Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_limit` or None if not set

        """
        return self["Heating Limit"]

    @heating_limit.setter
    def heating_limit(self, value="NoLimit"):
        """Corresponds to IDD field `Heating Limit`"""
        self["Heating Limit"] = value

    @property
    def maximum_heating_air_flow_rate(self):
        """field `Maximum Heating Air Flow Rate`

        |  This field is ignored if Heating Limit = NoLimit
        |  If this field is blank, there is no limit.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Heating Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_heating_air_flow_rate` or None if not set

        """
        return self["Maximum Heating Air Flow Rate"]

    @maximum_heating_air_flow_rate.setter
    def maximum_heating_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Heating Air Flow Rate`"""
        self["Maximum Heating Air Flow Rate"] = value

    @property
    def maximum_sensible_heating_capacity(self):
        """field `Maximum Sensible Heating Capacity`

        |  This field is ignored if Heating Limit = NoLimit
        |  If this field is blank, there is no limit.
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Sensible Heating Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_sensible_heating_capacity` or None if not set

        """
        return self["Maximum Sensible Heating Capacity"]

    @maximum_sensible_heating_capacity.setter
    def maximum_sensible_heating_capacity(self, value=None):
        """Corresponds to IDD field `Maximum Sensible Heating Capacity`"""
        self["Maximum Sensible Heating Capacity"] = value

    @property
    def cooling_limit(self):
        """field `Cooling Limit`

        |  Default value: NoLimit

        Args:
            value (str): value for IDD Field `Cooling Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_limit` or None if not set

        """
        return self["Cooling Limit"]

    @cooling_limit.setter
    def cooling_limit(self, value="NoLimit"):
        """Corresponds to IDD field `Cooling Limit`"""
        self["Cooling Limit"] = value

    @property
    def maximum_cooling_air_flow_rate(self):
        """field `Maximum Cooling Air Flow Rate`

        |  This field is ignored if Cooling Limit = NoLimit
        |  This field is required if Outdoor Air Economizer Type is anything other than NoEconomizer.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cooling Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_cooling_air_flow_rate` or None if not set

        """
        return self["Maximum Cooling Air Flow Rate"]

    @maximum_cooling_air_flow_rate.setter
    def maximum_cooling_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Cooling Air Flow Rate`"""
        self["Maximum Cooling Air Flow Rate"] = value

    @property
    def maximum_total_cooling_capacity(self):
        """field `Maximum Total Cooling Capacity`

        |  This field is ignored if Cooling Limit = NoLimit
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Total Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_total_cooling_capacity` or None if not set

        """
        return self["Maximum Total Cooling Capacity"]

    @maximum_total_cooling_capacity.setter
    def maximum_total_cooling_capacity(self, value=None):
        """Corresponds to IDD field `Maximum Total Cooling Capacity`"""
        self["Maximum Total Cooling Capacity"] = value

    @property
    def heating_availability_schedule_name(self):
        """field `Heating Availability Schedule Name`

        |  If blank, heating is always available.

        Args:
            value (str): value for IDD Field `Heating Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_availability_schedule_name` or None if not set

        """
        return self["Heating Availability Schedule Name"]

    @heating_availability_schedule_name.setter
    def heating_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Availability Schedule Name`"""
        self["Heating Availability Schedule Name"] = value

    @property
    def cooling_availability_schedule_name(self):
        """field `Cooling Availability Schedule Name`

        |  If blank, cooling is always available.

        Args:
            value (str): value for IDD Field `Cooling Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_availability_schedule_name` or None if not set

        """
        return self["Cooling Availability Schedule Name"]

    @cooling_availability_schedule_name.setter
    def cooling_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Availability Schedule Name`"""
        self["Cooling Availability Schedule Name"] = value

    @property
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`

        |  ConstantSensibleHeatRatio means that the ideal loads system
        |  will be controlled to meet the sensible cooling load, and the
        |  latent cooling rate will be computed using a constant
        |  sensible heat ratio (SHR)
        |  Humidistat means that there is a ZoneControl:Humidistat for this
        |  zone and the ideal loads system will attempt to satisfy the humidistat.
        |  None means that there is no dehumidification.
        |  ConstantSupplyHumidityRatio means that during cooling the supply air
        |  will always be at the Minimum Cooling Supply Humidity Ratio.
        |  Default value: ConstantSensibleHeatRatio

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set

        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="ConstantSensibleHeatRatio"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value

    @property
    def cooling_sensible_heat_ratio(self):
        """field `Cooling Sensible Heat Ratio`

        |  This field is applicable only when Dehumidification Control Type is ConstantSensibleHeatRatio
        |  Units: dimensionless
        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Cooling Sensible Heat Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_sensible_heat_ratio` or None if not set

        """
        return self["Cooling Sensible Heat Ratio"]

    @cooling_sensible_heat_ratio.setter
    def cooling_sensible_heat_ratio(self, value=0.7):
        """Corresponds to IDD field `Cooling Sensible Heat Ratio`"""
        self["Cooling Sensible Heat Ratio"] = value

    @property
    def humidification_control_type(self):
        """field `Humidification Control Type`

        |  None means that there is no humidification.
        |  Humidistat means that there is a ZoneControl:Humidistat for this
        |  zone and the ideal loads system will attempt to satisfy the humidistat.
        |  ConstantSupplyHumidityRatio means that during heating the supply air
        |  will always be at the Maximum Heating Supply Humidity Ratio.
        |  Default value: None

        Args:
            value (str): value for IDD Field `Humidification Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `humidification_control_type` or None if not set

        """
        return self["Humidification Control Type"]

    @humidification_control_type.setter
    def humidification_control_type(self, value="None"):
        """Corresponds to IDD field `Humidification Control Type`"""
        self["Humidification Control Type"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """field `Design Specification Outdoor Air Object Name`

        |  When the name of a DesignSpecification:OutdoorAir object is entered, the minimum
        |  outdoor air flow rate will be computed using these specifications. The outdoor air
        |  flow rate will also be affected by the next two fields.
        |  If this field is blank, there will be no outdoor air and the remaining fields will
        |  be ignored.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set

        """
        return self["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification Outdoor Air Object
        Name`"""
        self["Design Specification Outdoor Air Object Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """field `Outdoor Air Inlet Node Name`

        |  This field is required if the system provides outdoor air
        |  Enter the name of an outdoor air node. This node name is also specified in
        |  an OutdoorAir:Node or OutdoorAir:NodeList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set

        """
        return self["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Inlet Node Name`"""
        self["Outdoor Air Inlet Node Name"] = value

    @property
    def demand_controlled_ventilation_type(self):
        """field `Demand Controlled Ventilation Type`

        |  This field controls how the minimum outdoor air flow rate is calculated.
        |  None means that design occupancy will be used to compute the minimum outdoor air flow rate
        |  OccupancySchedule means that current occupancy level will be used.
        |  CO2Setpoint means that the design occupancy will be used to compute the minimum outdoor air flow
        |  rate and the outdoor air flow rate may be increased if necessary to maintain the indoor air carbon
        |  dioxide setpoint defined in a ZoneControl:ContaminantController object.
        |  Default value: None

        Args:
            value (str): value for IDD Field `Demand Controlled Ventilation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_controlled_ventilation_type` or None if not set

        """
        return self["Demand Controlled Ventilation Type"]

    @demand_controlled_ventilation_type.setter
    def demand_controlled_ventilation_type(self, value="None"):
        """Corresponds to IDD field `Demand Controlled Ventilation Type`"""
        self["Demand Controlled Ventilation Type"] = value

    @property
    def outdoor_air_economizer_type(self):
        """field `Outdoor Air Economizer Type`

        |  DifferentialDryBulb and DifferentialEnthalpy will increase the outdoor air flow rate
        |  when there is a cooling load and the outdoor air temperature or enthalpy
        |  is below the zone exhaust air temperature or enthalpy.
        |  Default value: NoEconomizer

        Args:
            value (str): value for IDD Field `Outdoor Air Economizer Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_economizer_type` or None if not set

        """
        return self["Outdoor Air Economizer Type"]

    @outdoor_air_economizer_type.setter
    def outdoor_air_economizer_type(self, value="NoEconomizer"):
        """Corresponds to IDD field `Outdoor Air Economizer Type`"""
        self["Outdoor Air Economizer Type"] = value

    @property
    def heat_recovery_type(self):
        """field `Heat Recovery Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Heat Recovery Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_type` or None if not set

        """
        return self["Heat Recovery Type"]

    @heat_recovery_type.setter
    def heat_recovery_type(self, value="None"):
        """Corresponds to IDD field `Heat Recovery Type`"""
        self["Heat Recovery Type"] = value

    @property
    def sensible_heat_recovery_effectiveness(self):
        """field `Sensible Heat Recovery Effectiveness`

        |  Units: dimensionless
        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Sensible Heat Recovery Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sensible_heat_recovery_effectiveness` or None if not set

        """
        return self["Sensible Heat Recovery Effectiveness"]

    @sensible_heat_recovery_effectiveness.setter
    def sensible_heat_recovery_effectiveness(self, value=0.7):
        """Corresponds to IDD field `Sensible Heat Recovery Effectiveness`"""
        self["Sensible Heat Recovery Effectiveness"] = value

    @property
    def latent_heat_recovery_effectiveness(self):
        """field `Latent Heat Recovery Effectiveness`

        |  Applicable only if Heat Recovery Type is Enthalpy.
        |  Units: dimensionless
        |  Default value: 0.65
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Latent Heat Recovery Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `latent_heat_recovery_effectiveness` or None if not set

        """
        return self["Latent Heat Recovery Effectiveness"]

    @latent_heat_recovery_effectiveness.setter
    def latent_heat_recovery_effectiveness(self, value=0.65):
        """Corresponds to IDD field `Latent Heat Recovery Effectiveness`"""
        self["Latent Heat Recovery Effectiveness"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacFourPipeFanCoil(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:FourPipeFanCoil`
        Four pipe fan coil system. Forced-convection hydronic heating-cooling unit with
        supply fan, hot water heating coil, chilled water cooling coil, and fixed-position
        outdoor air mixer.
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
                                      (u'capacity control method',
                                       {'name': u'Capacity Control Method',
                                        'pyname': u'capacity_control_method',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ConstantFanVariableFlow',
                                                            u'CyclingFan',
                                                            u'VariableFanVariableFlow',
                                                            u'VariableFanConstantFlow',
                                                            u'MultiSpeedFan'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum supply air flow rate',
                                       {'name': u'Maximum Supply Air Flow Rate',
                                        'pyname': u'maximum_supply_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'low speed supply air flow ratio',
                                       {'name': u'Low Speed Supply Air Flow Ratio',
                                        'pyname': u'low_speed_supply_air_flow_ratio',
                                        'default': 0.33,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'medium speed supply air flow ratio',
                                       {'name': u'Medium Speed Supply Air Flow Ratio',
                                        'pyname': u'medium_speed_supply_air_flow_ratio',
                                        'default': 0.66,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum outdoor air flow rate',
                                       {'name': u'Maximum Outdoor Air Flow Rate',
                                        'pyname': u'maximum_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air schedule name',
                                       {'name': u'Outdoor Air Schedule Name',
                                        'pyname': u'outdoor_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air mixer object type',
                                       {'name': u'Outdoor Air Mixer Object Type',
                                        'pyname': u'outdoor_air_mixer_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAir:Mixer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air mixer name',
                                       {'name': u'Outdoor Air Mixer Name',
                                        'pyname': u'outdoor_air_mixer_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume',
                                                            u'Fan:VariableVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatExchangerAssisted'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum cold water flow rate',
                                       {'name': u'Maximum Cold Water Flow Rate',
                                        'pyname': u'maximum_cold_water_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum cold water flow rate',
                                       {'name': u'Minimum Cold Water Flow Rate',
                                        'pyname': u'minimum_cold_water_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling convergence tolerance',
                                       {'name': u'Cooling Convergence Tolerance',
                                        'pyname': u'cooling_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water flow rate',
                                       {'name': u'Maximum Hot Water Flow Rate',
                                        'pyname': u'maximum_hot_water_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water flow rate',
                                       {'name': u'Minimum Hot Water Flow Rate',
                                        'pyname': u'minimum_hot_water_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'heating convergence tolerance',
                                       {'name': u'Heating Convergence Tolerance',
                                        'pyname': u'heating_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 24,
               'name': u'ZoneHVAC:FourPipeFanCoil',
               'pyname': u'ZoneHvacFourPipeFanCoil',
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
    def capacity_control_method(self):
        """field `Capacity Control Method`

        Args:
            value (str): value for IDD Field `Capacity Control Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `capacity_control_method` or None if not set

        """
        return self["Capacity Control Method"]

    @capacity_control_method.setter
    def capacity_control_method(self, value=None):
        """Corresponds to IDD field `Capacity Control Method`"""
        self["Capacity Control Method"] = value

    @property
    def maximum_supply_air_flow_rate(self):
        """field `Maximum Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_supply_air_flow_rate` or None if not set

        """
        return self["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Supply Air Flow Rate`"""
        self["Maximum Supply Air Flow Rate"] = value

    @property
    def low_speed_supply_air_flow_ratio(self):
        """field `Low Speed Supply Air Flow Ratio`

        |  Default value: 0.33

        Args:
            value (float): value for IDD Field `Low Speed Supply Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `low_speed_supply_air_flow_ratio` or None if not set

        """
        return self["Low Speed Supply Air Flow Ratio"]

    @low_speed_supply_air_flow_ratio.setter
    def low_speed_supply_air_flow_ratio(self, value=0.33):
        """Corresponds to IDD field `Low Speed Supply Air Flow Ratio`"""
        self["Low Speed Supply Air Flow Ratio"] = value

    @property
    def medium_speed_supply_air_flow_ratio(self):
        """field `Medium Speed Supply Air Flow Ratio`

        |  Medium Speed Supply Air Flow Ratio should be greater
        |  than Low Speed Supply Air Flow Ratio
        |  Default value: 0.66

        Args:
            value (float): value for IDD Field `Medium Speed Supply Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `medium_speed_supply_air_flow_ratio` or None if not set

        """
        return self["Medium Speed Supply Air Flow Ratio"]

    @medium_speed_supply_air_flow_ratio.setter
    def medium_speed_supply_air_flow_ratio(self, value=0.66):
        """Corresponds to IDD field `Medium Speed Supply Air Flow Ratio`"""
        self["Medium Speed Supply Air Flow Ratio"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """field `Maximum Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_outdoor_air_flow_rate` or None if not set

        """
        return self["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Air Flow Rate`"""
        self["Maximum Outdoor Air Flow Rate"] = value

    @property
    def outdoor_air_schedule_name(self):
        """field `Outdoor Air Schedule Name`

        |  Value of schedule multiplies maximum outdoor air flow rate

        Args:
            value (str): value for IDD Field `Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_schedule_name` or None if not set

        """
        return self["Outdoor Air Schedule Name"]

    @outdoor_air_schedule_name.setter
    def outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Schedule Name`"""
        self["Outdoor Air Schedule Name"] = value

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
    def outdoor_air_mixer_object_type(self):
        """field `Outdoor Air Mixer Object Type`

        |  currently only one type OutdoorAir:Mixer object is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set

        """
        return self["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Object Type`"""
        self["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """field `Outdoor Air Mixer Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set

        """
        return self["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Name`"""
        self["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Fan type must be according to capacity control method (see I/O)
        |  For ConstantFanVariableFlow a Fan:OnOff or Fan:ConstantVolume is valid.
        |  For CyclingFan, a Fan:OnOff is valid.
        |  For VariableFanVariableFlow or VariableFanConstantFlow a Fan:VariableVolume is valid.
        |  The fan's inlet node should be the same as the outdoor air mixer's mixed air node.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_name` or None if not set

        """
        return self["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Name`"""
        self["Cooling Coil Name"] = value

    @property
    def maximum_cold_water_flow_rate(self):
        """field `Maximum Cold Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cold Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_cold_water_flow_rate` or None if not set

        """
        return self["Maximum Cold Water Flow Rate"]

    @maximum_cold_water_flow_rate.setter
    def maximum_cold_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Cold Water Flow Rate`"""
        self["Maximum Cold Water Flow Rate"] = value

    @property
    def minimum_cold_water_flow_rate(self):
        """field `Minimum Cold Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Cold Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_cold_water_flow_rate` or None if not set

        """
        return self["Minimum Cold Water Flow Rate"]

    @minimum_cold_water_flow_rate.setter
    def minimum_cold_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Cold Water Flow Rate`"""
        self["Minimum Cold Water Flow Rate"] = value

    @property
    def cooling_convergence_tolerance(self):
        """field `Cooling Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set

        """
        return self["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Cooling Convergence Tolerance`"""
        self["Cooling Convergence Tolerance"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def maximum_hot_water_flow_rate(self):
        """field `Maximum Hot Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_flow_rate` or None if not set

        """
        return self["Maximum Hot Water Flow Rate"]

    @maximum_hot_water_flow_rate.setter
    def maximum_hot_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water Flow Rate`"""
        self["Maximum Hot Water Flow Rate"] = value

    @property
    def minimum_hot_water_flow_rate(self):
        """field `Minimum Hot Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_flow_rate` or None if not set

        """
        return self["Minimum Hot Water Flow Rate"]

    @minimum_hot_water_flow_rate.setter
    def minimum_hot_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water Flow Rate`"""
        self["Minimum Hot Water Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """field `Heating Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set

        """
        return self["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence Tolerance`"""
        self["Heating Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        |  cycling fan operation (fan cycles with cooling coil). Schedule values greater
        |  than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        |  The fan operating mode defaults to cycling fan operation if this field is left blank.
        |  This input field is currently used with MultiStageFan capacity control method

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value




class ZoneHvacWindowAirConditioner(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:WindowAirConditioner`
        Window air conditioner. Forced-convection cooling-only unit with supply fan, direct
        expansion (DX) cooling coil, and fixed-position outdoor air mixer.
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
                                      (u'maximum supply air flow rate',
                                       {'name': u'Maximum Supply Air Flow Rate',
                                        'pyname': u'maximum_supply_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum outdoor air flow rate',
                                       {'name': u'Maximum Outdoor Air Flow Rate',
                                        'pyname': u'maximum_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air mixer object type',
                                       {'name': u'Outdoor Air Mixer Object Type',
                                        'pyname': u'outdoor_air_mixer_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAir:Mixer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air mixer name',
                                       {'name': u'Outdoor Air Mixer Name',
                                        'pyname': u'outdoor_air_mixer_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                            u'CoilSystem:Cooling:DX:HeatExchangerAssisted'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dx cooling coil name',
                                       {'name': u'DX Cooling Coil Name',
                                        'pyname': u'dx_cooling_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling convergence tolerance',
                                       {'name': u'Cooling Convergence Tolerance',
                                        'pyname': u'cooling_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 15,
               'name': u'ZoneHVAC:WindowAirConditioner',
               'pyname': u'ZoneHvacWindowAirConditioner',
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
    def maximum_supply_air_flow_rate(self):
        """field `Maximum Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_supply_air_flow_rate` or None if not set

        """
        return self["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Supply Air Flow Rate`"""
        self["Maximum Supply Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """field `Maximum Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_outdoor_air_flow_rate` or None if not set

        """
        return self["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Air Flow Rate`"""
        self["Maximum Outdoor Air Flow Rate"] = value

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
    def outdoor_air_mixer_object_type(self):
        """field `Outdoor Air Mixer Object Type`

        |  currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set

        """
        return self["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Object Type`"""
        self["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """field `Outdoor Air Mixer Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set

        """
        return self["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Name`"""
        self["Outdoor Air Mixer Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Fan:ConstantVolume only works when continuous fan operation is used the entire
        |  simulation (all supply air fan operating mode schedule values are greater than 0).
        |  If any fan operating mode schedule values are 0 a Fan:OnOff object must be used.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        |  Fan type Fan:ConstantVolume is used with continuous fan
        |  and fan type Fan:OnOff is used with cycling Fan.

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def dx_cooling_coil_name(self):
        """field `DX Cooling Coil Name`

        Args:
            value (str): value for IDD Field `DX Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dx_cooling_coil_name` or None if not set

        """
        return self["DX Cooling Coil Name"]

    @dx_cooling_coil_name.setter
    def dx_cooling_coil_name(self, value=None):
        """Corresponds to IDD field `DX Cooling Coil Name`"""
        self["DX Cooling Coil Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        |  cycling fan operation (fan cycles with cooling coil). Schedule values greater
        |  than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        |  The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value=None):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def cooling_convergence_tolerance(self):
        """field `Cooling Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set

        """
        return self["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Cooling Convergence Tolerance`"""
        self["Cooling Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacPackagedTerminalAirConditioner(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:PackagedTerminalAirConditioner`
        Packaged terminal air conditioner (PTAC).  Forced-convection heating-cooling unit
        with supply fan, direct expansion (DX) cooling coil, heating coil (gas, electric, hot
        water, or steam) and fixed-position outdoor air mixer.
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
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air mixer object type',
                                       {'name': u'Outdoor Air Mixer Object Type',
                                        'pyname': u'outdoor_air_mixer_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAir:Mixer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air mixer name',
                                       {'name': u'Outdoor Air Mixer Name',
                                        'pyname': u'outdoor_air_mixer_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling supply air flow rate',
                                       {'name': u'Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating supply air flow rate',
                                       {'name': u'Heating Supply Air Flow Rate',
                                        'pyname': u'heating_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load supply air flow rate',
                                       {'name': u'No Load Supply Air Flow Rate',
                                        'pyname': u'no_load_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling outdoor air flow rate',
                                       {'name': u'Cooling Outdoor Air Flow Rate',
                                        'pyname': u'cooling_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating outdoor air flow rate',
                                       {'name': u'Heating Outdoor Air Flow Rate',
                                        'pyname': u'heating_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load outdoor air flow rate',
                                       {'name': u'No Load Outdoor Air Flow Rate',
                                        'pyname': u'no_load_outdoor_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                            u'Coil:Cooling:DX:VariableSpeed',
                                                            u'CoilSystem:Cooling:DX:HeatExchangerAssisted'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'default': u'DrawThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 18,
               'name': u'ZoneHVAC:PackagedTerminalAirConditioner',
               'pyname': u'ZoneHvacPackagedTerminalAirConditioner',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Unique name for this packaged terminal air conditioner object.

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
        |  Schedule values of 0 denote the unit is off.

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
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  Air inlet node for the PTAC must be a zone air exhaust Node.

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

        |  Air outlet node for the PTAC must be a zone air inlet node.

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
    def outdoor_air_mixer_object_type(self):
        """field `Outdoor Air Mixer Object Type`

        |  currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set

        """
        return self["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Object Type`"""
        self["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """field `Outdoor Air Mixer Name`

        |  Needs to match the name of the PTAC outdoor air mixer object.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set

        """
        return self["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Name`"""
        self["Outdoor Air Mixer Name"] = value

    @property
    def cooling_supply_air_flow_rate(self):
        """field `Cooling Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Supply Air Flow Rate"]

    @cooling_supply_air_flow_rate.setter
    def cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate`"""
        self["Cooling Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate(self):
        """field `Heating Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Supply Air Flow Rate"]

    @heating_supply_air_flow_rate.setter
    def heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate`"""
        self["Heating Supply Air Flow Rate"] = value

    @property
    def no_load_supply_air_flow_rate(self):
        """field `No Load Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Only used when supply air fan operating mode schedule values specify continuous fan
        |  (schedule values greater than 0 specify continuous fan operation).
        |  This air flow rate is used when no heating or cooling is required and the cooling or
        |  heating coil is off. If this field is left blank or zero, the supply air flow rate
        |  from the previous on cycle (either cooling or heating) is used.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_supply_air_flow_rate` or None if not set

        """
        return self["No Load Supply Air Flow Rate"]

    @no_load_supply_air_flow_rate.setter
    def no_load_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Supply Air Flow Rate`"""
        self["No Load Supply Air Flow Rate"] = value

    @property
    def cooling_outdoor_air_flow_rate(self):
        """field `Cooling Outdoor Air Flow Rate`

        |  Must be less than or equal to supply air flow rate during cooling operation.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_outdoor_air_flow_rate` or None if not set

        """
        return self["Cooling Outdoor Air Flow Rate"]

    @cooling_outdoor_air_flow_rate.setter
    def cooling_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Outdoor Air Flow Rate`"""
        self["Cooling Outdoor Air Flow Rate"] = value

    @property
    def heating_outdoor_air_flow_rate(self):
        """field `Heating Outdoor Air Flow Rate`

        |  Must be less than or equal to supply air flow rate during heating operation.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_outdoor_air_flow_rate` or None if not set

        """
        return self["Heating Outdoor Air Flow Rate"]

    @heating_outdoor_air_flow_rate.setter
    def heating_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Outdoor Air Flow Rate`"""
        self["Heating Outdoor Air Flow Rate"] = value

    @property
    def no_load_outdoor_air_flow_rate(self):
        """field `No Load Outdoor Air Flow Rate`

        |  Only used when supply air fan operating mode schedule values specify continuous fan
        |  (schedule values greater than 0 specify continuous fan operation).
        |  This air flow rate is used when no heating or cooling is required and the cooling or
        |  heating coil is off. If this field is left blank or zero, the outdoor air flow rate
        |  from the previous on cycle (either cooling or heating) is used.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_outdoor_air_flow_rate` or None if not set

        """
        return self["No Load Outdoor Air Flow Rate"]

    @no_load_outdoor_air_flow_rate.setter
    def no_load_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Outdoor Air Flow Rate`"""
        self["No Load Outdoor Air Flow Rate"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Fan:ConstantVolume only works when continuous fan operation is used the entire
        |  simulation (all supply air fan operating mode schedule values are greater than 0).
        |  If any fan operating mode schedule values are 0 a Fan:OnOff object must be used.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        |  Needs to match in the fan object.

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        |  Select the type of heating coil.

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        |  Needs to match in the heating coil object.

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        |  Select the type of Cooling Coil.
        |  Only works with Coil:Cooling:DX:SingleSpeed or
        |  CoilSystem:Cooling:DX:HeatExchangerAssisted or
        |  Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """field `Cooling Coil Name`

        |  Needs to match a DX cooling coil object.

        Args:
            value (str): value for IDD Field `Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_name` or None if not set

        """
        return self["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Name`"""
        self["Cooling Coil Name"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        |  Select fan placement as either blow through or draw through.
        |  Default value: DrawThrough

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote
        |  cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater
        |  than 0 denote constant fan operation (fan runs continually regardless of coil operation).

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacPackagedTerminalHeatPump(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:PackagedTerminalHeatPump`
        Packaged terminal heat pump (PTHP). Forced-convection heating-cooling unit with
        supply fan, direct expansion (DX) cooling coil, DX heating coil (air-to-air heat
        pump), supplemental heating coil (gas, electric, hot water, or steam), and
        fixed-position outdoor air mixer.
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
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air mixer object type',
                                       {'name': u'Outdoor Air Mixer Object Type',
                                        'pyname': u'outdoor_air_mixer_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAir:Mixer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air mixer name',
                                       {'name': u'Outdoor Air Mixer Name',
                                        'pyname': u'outdoor_air_mixer_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling supply air flow rate',
                                       {'name': u'Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating supply air flow rate',
                                       {'name': u'Heating Supply Air Flow Rate',
                                        'pyname': u'heating_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load supply air flow rate',
                                       {'name': u'No Load Supply Air Flow Rate',
                                        'pyname': u'no_load_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling outdoor air flow rate',
                                       {'name': u'Cooling Outdoor Air Flow Rate',
                                        'pyname': u'cooling_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating outdoor air flow rate',
                                       {'name': u'Heating Outdoor Air Flow Rate',
                                        'pyname': u'heating_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load outdoor air flow rate',
                                       {'name': u'No Load Outdoor Air Flow Rate',
                                        'pyname': u'no_load_outdoor_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:DX:SingleSpeed',
                                                            u'Coil:Heating:DX:VariableSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating convergence tolerance',
                                       {'name': u'Heating Convergence Tolerance',
                                        'pyname': u'heating_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'minimum outdoor dry-bulb temperature for compressor operation',
                                       {'name': u'Minimum Outdoor Dry-Bulb Temperature for Compressor Operation',
                                        'pyname': u'minimum_outdoor_drybulb_temperature_for_compressor_operation',
                                        'default': -8.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -20.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                            u'Coil:Cooling:DX:VariableSpeed',
                                                            u'CoilSystem:Cooling:DX:HeatExchangerAssisted'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling convergence tolerance',
                                       {'name': u'Cooling Convergence Tolerance',
                                        'pyname': u'cooling_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'supplemental heating coil object type',
                                       {'name': u'Supplemental Heating Coil Object Type',
                                        'pyname': u'supplemental_heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supplemental heating coil name',
                                       {'name': u'Supplemental Heating Coil Name',
                                        'pyname': u'supplemental_heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature from supplemental heater',
                                       {'name': u'Maximum Supply Air Temperature from Supplemental Heater',
                                        'pyname': u'maximum_supply_air_temperature_from_supplemental_heater',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor dry-bulb temperature for supplemental heater operation',
                                       {'name': u'Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation',
                                        'default': 21.0,
                                        'maximum': 21.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'default': u'DrawThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 27,
               'name': u'ZoneHVAC:PackagedTerminalHeatPump',
               'pyname': u'ZoneHvacPackagedTerminalHeatPump',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Unique name for this packaged terminal heat pump object.

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
        |  Schedule values of 0 denote the unit is off.

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
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  Air inlet node for the PTHP must be a zone air exhaust node.

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

        |  Air outlet node for the PTHP must be a zone air inlet node.

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
    def outdoor_air_mixer_object_type(self):
        """field `Outdoor Air Mixer Object Type`

        |  currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set

        """
        return self["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Object Type`"""
        self["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """field `Outdoor Air Mixer Name`

        |  Needs to match name of outdoor air mixer object.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set

        """
        return self["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Name`"""
        self["Outdoor Air Mixer Name"] = value

    @property
    def cooling_supply_air_flow_rate(self):
        """field `Cooling Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Supply Air Flow Rate"]

    @cooling_supply_air_flow_rate.setter
    def cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate`"""
        self["Cooling Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate(self):
        """field `Heating Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Supply Air Flow Rate"]

    @heating_supply_air_flow_rate.setter
    def heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate`"""
        self["Heating Supply Air Flow Rate"] = value

    @property
    def no_load_supply_air_flow_rate(self):
        """field `No Load Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Only used when heat pump fan operating mode is continuous. This air flow rate
        |  is used when no heating or cooling is required and the DX coil compressor is off.
        |  If this field is left blank or zero, the supply air flow rate from the previous on cycle
        |  (either cooling or heating) is used.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_supply_air_flow_rate` or None if not set

        """
        return self["No Load Supply Air Flow Rate"]

    @no_load_supply_air_flow_rate.setter
    def no_load_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Supply Air Flow Rate`"""
        self["No Load Supply Air Flow Rate"] = value

    @property
    def cooling_outdoor_air_flow_rate(self):
        """field `Cooling Outdoor Air Flow Rate`

        |  Must be less than or equal to supply air flow rate during cooling operation.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_outdoor_air_flow_rate` or None if not set

        """
        return self["Cooling Outdoor Air Flow Rate"]

    @cooling_outdoor_air_flow_rate.setter
    def cooling_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Outdoor Air Flow Rate`"""
        self["Cooling Outdoor Air Flow Rate"] = value

    @property
    def heating_outdoor_air_flow_rate(self):
        """field `Heating Outdoor Air Flow Rate`

        |  Must be less than or equal to supply air flow rate during heating operation.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_outdoor_air_flow_rate` or None if not set

        """
        return self["Heating Outdoor Air Flow Rate"]

    @heating_outdoor_air_flow_rate.setter
    def heating_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Outdoor Air Flow Rate`"""
        self["Heating Outdoor Air Flow Rate"] = value

    @property
    def no_load_outdoor_air_flow_rate(self):
        """field `No Load Outdoor Air Flow Rate`

        |  Only used when heat pump Fan operating mode is continuous. This air flow rate
        |  is used when no heating or cooling is required and the DX coil compressor is off.
        |  If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        |  (either cooling or heating) is used.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_outdoor_air_flow_rate` or None if not set

        """
        return self["No Load Outdoor Air Flow Rate"]

    @no_load_outdoor_air_flow_rate.setter
    def no_load_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Outdoor Air Flow Rate`"""
        self["No Load Outdoor Air Flow Rate"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Fan:ConstantVolume only works with fan operating mode is continuous.

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        |  Needs to match a fan object.

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        |  Only works with Coil:Heating:DX:SingleSpeed or
        |  Coil:Heating:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        |  Needs to match in the DX Heating Coil object.

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def heating_convergence_tolerance(self):
        """field `Heating Convergence Tolerance`

        |  Defines Heating convergence tolerance as a fraction of Heating load to be met.
        |  Units: dimensionless
        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set

        """
        return self["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence Tolerance`"""
        self["Heating Convergence Tolerance"] = value

    @property
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self):
        """field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`

        |  Needs to match the corresponding minimum outdoor temperature defined
        |  in the DX Heating Coil object.
        |  Units: C
        |  Default value: -8.0
        |  value >= -20.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_drybulb_temperature_for_compressor_operation` or None if not set
        """
        return self[
            "Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"]

    @minimum_outdoor_drybulb_temperature_for_compressor_operation.setter
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(
            self,
            value=-
            8.0):
        """  Corresponds to IDD field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`

        """
        self[
            "Minimum Outdoor Dry-Bulb Temperature for Compressor Operation"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        |  Only works with Coil:Cooling:DX:SingleSpeed or
        |  CoilSystem:Cooling:DX:HeatExchangerAssisted or
        |  Coil:Cooling:DX:VariableSpeed.

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """field `Cooling Coil Name`

        |  Needs to match in the DX Cooling Coil object.

        Args:
            value (str): value for IDD Field `Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_name` or None if not set

        """
        return self["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Name`"""
        self["Cooling Coil Name"] = value

    @property
    def cooling_convergence_tolerance(self):
        """field `Cooling Convergence Tolerance`

        |  Defines Cooling convergence tolerance as a fraction of the Cooling load to be met.
        |  Units: dimensionless
        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set

        """
        return self["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Cooling Convergence Tolerance`"""
        self["Cooling Convergence Tolerance"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """field `Supplemental Heating Coil Object Type`

        |  works with gas, electric, hot water and steam heating coil.

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set

        """
        return self["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Supplemental Heating Coil Object Type`"""
        self["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """field `Supplemental Heating Coil Name`

        |  Needs to match in the supplemental heating coil object.

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set

        """
        return self["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """Corresponds to IDD field `Supplemental Heating Coil Name`"""
        self["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """field `Maximum Supply Air Temperature from Supplemental Heater`

        |  Supply air temperature from the supplemental heater will not exceed this value.
        |  Units: C

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set

        """
        return self["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Supply Air Temperature from
        Supplemental Heater`"""
        self["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(
            self):
        """field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        |  Supplemental heater will not operate when outdoor temperature exceeds this value.
        |  Units: C
        |  Default value: 21.0
        |  value <= 21.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self[
            "Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(
            self,
            value=21.0):
        """  Corresponds to IDD field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        """
        self[
            "Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        |  Select fan placement as either blow through or draw through.
        |  Default value: DrawThrough

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        |  cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater
        |  than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        |  The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacWaterToAirHeatPump(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:WaterToAirHeatPump`
        Water-to-air heat pump. Forced-convection heating-cooling unit with supply fan,
        water-to-air cooling and heating coils, supplemental heating coil (gas, electric, hot
        water, or steam), and fixed-position outdoor air mixer.
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
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air mixer object type',
                                       {'name': u'Outdoor Air Mixer Object Type',
                                        'pyname': u'outdoor_air_mixer_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAir:Mixer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air mixer name',
                                       {'name': u'Outdoor Air Mixer Name',
                                        'pyname': u'outdoor_air_mixer_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling supply air flow rate',
                                       {'name': u'Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating supply air flow rate',
                                       {'name': u'Heating Supply Air Flow Rate',
                                        'pyname': u'heating_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load supply air flow rate',
                                       {'name': u'No Load Supply Air Flow Rate',
                                        'pyname': u'no_load_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling outdoor air flow rate',
                                       {'name': u'Cooling Outdoor Air Flow Rate',
                                        'pyname': u'cooling_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating outdoor air flow rate',
                                       {'name': u'Heating Outdoor Air Flow Rate',
                                        'pyname': u'heating_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load outdoor air flow rate',
                                       {'name': u'No Load Outdoor Air Flow Rate',
                                        'pyname': u'no_load_outdoor_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:WaterToAirHeatPump:EquationFit',
                                                            u'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:WaterToAirHeatPump:EquationFit',
                                                            u'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum cycling rate',
                                       {'name': u'Maximum Cycling Rate',
                                        'pyname': u'maximum_cycling_rate',
                                        'default': 2.5,
                                        'maximum': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'cycles/hr'}),
                                      (u'heat pump time constant',
                                       {'name': u'Heat Pump Time Constant',
                                        'pyname': u'heat_pump_time_constant',
                                        'default': 60.0,
                                        'maximum': 500.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u's'}),
                                      (u'fraction of on-cycle power use',
                                       {'name': u'Fraction of On-Cycle Power Use',
                                        'pyname': u'fraction_of_oncycle_power_use',
                                        'default': 0.01,
                                        'maximum': 0.05,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'heat pump fan delay time',
                                       {'name': u'Heat Pump Fan Delay Time',
                                        'pyname': u'heat_pump_fan_delay_time',
                                        'default': 60.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u's'}),
                                      (u'supplemental heating coil object type',
                                       {'name': u'Supplemental Heating Coil Object Type',
                                        'pyname': u'supplemental_heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supplemental heating coil name',
                                       {'name': u'Supplemental Heating Coil Name',
                                        'pyname': u'supplemental_heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature from supplemental heater',
                                       {'name': u'Maximum Supply Air Temperature from Supplemental Heater',
                                        'pyname': u'maximum_supply_air_temperature_from_supplemental_heater',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor dry-bulb temperature for supplemental heater operation',
                                       {'name': u'Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation',
                                        'default': 21.0,
                                        'maximum': 21.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'outdoor dry-bulb temperature sensor node name',
                                       {'name': u'Outdoor Dry-Bulb Temperature Sensor Node Name',
                                        'pyname': u'outdoor_drybulb_temperature_sensor_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'default': u'BlowThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heat pump coil water flow mode',
                                       {'name': u'Heat Pump Coil Water Flow Mode',
                                        'pyname': u'heat_pump_coil_water_flow_mode',
                                        'default': u'Cycling',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Cycling',
                                                            u'ConstantOnDemand'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 25,
               'name': u'ZoneHVAC:WaterToAirHeatPump',
               'pyname': u'ZoneHvacWaterToAirHeatPump',
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
    def outdoor_air_mixer_object_type(self):
        """field `Outdoor Air Mixer Object Type`

        |  currently only one OutdoorAir:Mixer object type is available.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_object_type` or None if not set

        """
        return self["Outdoor Air Mixer Object Type"]

    @outdoor_air_mixer_object_type.setter
    def outdoor_air_mixer_object_type(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Object Type`"""
        self["Outdoor Air Mixer Object Type"] = value

    @property
    def outdoor_air_mixer_name(self):
        """field `Outdoor Air Mixer Name`

        |  This optional field specifies the name of the outdoor air mixer object.
        |  When used, this name needs to match name of outdoor air mixer object.

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_name` or None if not set

        """
        return self["Outdoor Air Mixer Name"]

    @outdoor_air_mixer_name.setter
    def outdoor_air_mixer_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Name`"""
        self["Outdoor Air Mixer Name"] = value

    @property
    def cooling_supply_air_flow_rate(self):
        """field `Cooling Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Supply Air Flow Rate"]

    @cooling_supply_air_flow_rate.setter
    def cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate`"""
        self["Cooling Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate(self):
        """field `Heating Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Supply Air Flow Rate"]

    @heating_supply_air_flow_rate.setter
    def heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate`"""
        self["Heating Supply Air Flow Rate"] = value

    @property
    def no_load_supply_air_flow_rate(self):
        """field `No Load Supply Air Flow Rate`

        |  Must be less than or equal to fan size.
        |  Only used when heat pump fan operating mode is continuous. This air flow rate
        |  is used when no heating or cooling is required and the DX coil compressor is off.
        |  If this field is left blank or zero, the supply air flow rate from the previous on cycle
        |  (either cooling or heating) is used.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_supply_air_flow_rate` or None if not set

        """
        return self["No Load Supply Air Flow Rate"]

    @no_load_supply_air_flow_rate.setter
    def no_load_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Supply Air Flow Rate`"""
        self["No Load Supply Air Flow Rate"] = value

    @property
    def cooling_outdoor_air_flow_rate(self):
        """field `Cooling Outdoor Air Flow Rate`

        |  Must be less than or equal to supply air flow rate during cooling operation.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_outdoor_air_flow_rate` or None if not set

        """
        return self["Cooling Outdoor Air Flow Rate"]

    @cooling_outdoor_air_flow_rate.setter
    def cooling_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Outdoor Air Flow Rate`"""
        self["Cooling Outdoor Air Flow Rate"] = value

    @property
    def heating_outdoor_air_flow_rate(self):
        """field `Heating Outdoor Air Flow Rate`

        |  Must be less than or equal to supply air flow rate during heating operation.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_outdoor_air_flow_rate` or None if not set

        """
        return self["Heating Outdoor Air Flow Rate"]

    @heating_outdoor_air_flow_rate.setter
    def heating_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Outdoor Air Flow Rate`"""
        self["Heating Outdoor Air Flow Rate"] = value

    @property
    def no_load_outdoor_air_flow_rate(self):
        """field `No Load Outdoor Air Flow Rate`

        |  Only used when heat pump Fan operating mode is continuous. This air flow rate
        |  is used when no heating or cooling is required and the DX coil compressor is off.
        |  If this field is left blank or zero, the outdoor air flow rate from the previous on cycle
        |  (either cooling or heating) is used.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_outdoor_air_flow_rate` or None if not set

        """
        return self["No Load Outdoor Air Flow Rate"]

    @no_load_outdoor_air_flow_rate.setter
    def no_load_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Outdoor Air Flow Rate`"""
        self["No Load Outdoor Air Flow Rate"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Only works with On/Off Fan

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        |  Needs to match Fan:OnOff object

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        |  Needs to match in the water-to-air heat pump heating coil object

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """field `Cooling Coil Name`

        |  Needs to match in the water-to-air heat pump cooling coil object

        Args:
            value (str): value for IDD Field `Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_name` or None if not set

        """
        return self["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Name`"""
        self["Cooling Coil Name"] = value

    @property
    def maximum_cycling_rate(self):
        """field `Maximum Cycling Rate`

        |  The maximum on-off cycling rate for the compressor
        |  Suggested value is 2.5 for a typical heat pump
        |  Units: cycles/hr
        |  Default value: 2.5
        |  value <= 5.0

        Args:
            value (float): value for IDD Field `Maximum Cycling Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_cycling_rate` or None if not set

        """
        return self["Maximum Cycling Rate"]

    @maximum_cycling_rate.setter
    def maximum_cycling_rate(self, value=2.5):
        """Corresponds to IDD field `Maximum Cycling Rate`"""
        self["Maximum Cycling Rate"] = value

    @property
    def heat_pump_time_constant(self):
        """field `Heat Pump Time Constant`

        |  Time constant for the cooling coil's capacity to reach steady state after startup
        |  Suggested value is 60 for a typical heat pump
        |  Units: s
        |  Default value: 60.0
        |  value <= 500.0

        Args:
            value (float): value for IDD Field `Heat Pump Time Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_pump_time_constant` or None if not set

        """
        return self["Heat Pump Time Constant"]

    @heat_pump_time_constant.setter
    def heat_pump_time_constant(self, value=60.0):
        """Corresponds to IDD field `Heat Pump Time Constant`"""
        self["Heat Pump Time Constant"] = value

    @property
    def fraction_of_oncycle_power_use(self):
        """field `Fraction of On-Cycle Power Use`

        |  The fraction of on-cycle power use to adjust the part load fraction based on
        |  the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        |  Suggested value is 0.01 for a typical heat pump
        |  Default value: 0.01
        |  value <= 0.05

        Args:
            value (float): value for IDD Field `Fraction of On-Cycle Power Use`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_oncycle_power_use` or None if not set
        """
        return self["Fraction of On-Cycle Power Use"]

    @fraction_of_oncycle_power_use.setter
    def fraction_of_oncycle_power_use(self, value=0.01):
        """  Corresponds to IDD field `Fraction of On-Cycle Power Use`

        """
        self["Fraction of On-Cycle Power Use"] = value

    @property
    def heat_pump_fan_delay_time(self):
        """field `Heat Pump Fan Delay Time`

        |  Programmed time delay for heat pump fan to shut off after compressor cycle off.
        |  Only required when fan operating mode is cycling
        |  Enter 0 when fan operating mode is continuous
        |  Units: s
        |  Default value: 60.0

        Args:
            value (float): value for IDD Field `Heat Pump Fan Delay Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_pump_fan_delay_time` or None if not set

        """
        return self["Heat Pump Fan Delay Time"]

    @heat_pump_fan_delay_time.setter
    def heat_pump_fan_delay_time(self, value=60.0):
        """Corresponds to IDD field `Heat Pump Fan Delay Time`"""
        self["Heat Pump Fan Delay Time"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """field `Supplemental Heating Coil Object Type`

        |  works with gas, electric, hot water and steam heating coils

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supplemental_heating_coil_object_type` or None if not set

        """
        return self["Supplemental Heating Coil Object Type"]

    @supplemental_heating_coil_object_type.setter
    def supplemental_heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Supplemental Heating Coil Object Type`"""
        self["Supplemental Heating Coil Object Type"] = value

    @property
    def supplemental_heating_coil_name(self):
        """field `Supplemental Heating Coil Name`

        |  Needs to match in the supplemental heating coil object

        Args:
            value (str): value for IDD Field `Supplemental Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supplemental_heating_coil_name` or None if not set

        """
        return self["Supplemental Heating Coil Name"]

    @supplemental_heating_coil_name.setter
    def supplemental_heating_coil_name(self, value=None):
        """Corresponds to IDD field `Supplemental Heating Coil Name`"""
        self["Supplemental Heating Coil Name"] = value

    @property
    def maximum_supply_air_temperature_from_supplemental_heater(self):
        """field `Maximum Supply Air Temperature from Supplemental Heater`

        |  Units: C

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set

        """
        return self["Maximum Supply Air Temperature from Supplemental Heater"]

    @maximum_supply_air_temperature_from_supplemental_heater.setter
    def maximum_supply_air_temperature_from_supplemental_heater(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Supply Air Temperature from
        Supplemental Heater`"""
        self["Maximum Supply Air Temperature from Supplemental Heater"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(
            self):
        """field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        |  Units: C
        |  Default value: 21.0
        |  value <= 21.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation` or None if not set
        """
        return self[
            "Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"]

    @maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation.setter
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(
            self,
            value=21.0):
        """  Corresponds to IDD field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`

        """
        self[
            "Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation"] = value

    @property
    def outdoor_drybulb_temperature_sensor_node_name(self):
        """field `Outdoor Dry-Bulb Temperature Sensor Node Name`


        Args:
            value (str): value for IDD Field `Outdoor Dry-Bulb Temperature Sensor Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_drybulb_temperature_sensor_node_name` or None if not set
        """
        return self["Outdoor Dry-Bulb Temperature Sensor Node Name"]

    @outdoor_drybulb_temperature_sensor_node_name.setter
    def outdoor_drybulb_temperature_sensor_node_name(self, value=None):
        """  Corresponds to IDD field `Outdoor Dry-Bulb Temperature Sensor Node Name`

        """
        self["Outdoor Dry-Bulb Temperature Sensor Node Name"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        |  Default value: BlowThrough

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="BlowThrough"):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule values of 0 denote
        |  cycling fan operation (fan cycles with cooling or heating coil). Schedule values greater
        |  than 0 denote constant fan operation (fan runs continually regardless of coil operation).
        |  The fan operating mode defaults to cycling fan operation if this field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def heat_pump_coil_water_flow_mode(self):
        """field `Heat Pump Coil Water Flow Mode`

        |  used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit
        |  Constant results in 100% water flow regardless of compressor PLR
        |  Cycling results in water flow that matches compressor PLR
        |  ConstantOnDemand results in 100% water flow whenever the coil is on, but is 0% whenever the coil has no load
        |  Default value: Cycling

        Args:
            value (str): value for IDD Field `Heat Pump Coil Water Flow Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_pump_coil_water_flow_mode` or None if not set

        """
        return self["Heat Pump Coil Water Flow Mode"]

    @heat_pump_coil_water_flow_mode.setter
    def heat_pump_coil_water_flow_mode(self, value="Cycling"):
        """Corresponds to IDD field `Heat Pump Coil Water Flow Mode`"""
        self["Heat Pump Coil Water Flow Mode"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacDehumidifierDx(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:Dehumidifier:DX`
        This object calculates the performance of zone (room) air dehumidifiers.
        Meant to model conventional direct expansion (DX) cooling-based room air
        dehumidifiers (reject 100% of condenser heat to the zone air), but this
        object might be able to be used to model other room air dehumidifier types.
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
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'rated water removal',
                                       {'name': u'Rated Water Removal',
                                        'pyname': u'rated_water_removal',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'L/day'}),
                                      (u'rated energy factor',
                                       {'name': u'Rated Energy Factor',
                                        'pyname': u'rated_energy_factor',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'L/kWh'}),
                                      (u'rated air flow rate',
                                       {'name': u'Rated Air Flow Rate',
                                        'pyname': u'rated_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'water removal curve name',
                                       {'name': u'Water Removal Curve Name',
                                        'pyname': u'water_removal_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'energy factor curve name',
                                       {'name': u'Energy Factor Curve Name',
                                        'pyname': u'energy_factor_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'part load fraction correlation curve name',
                                       {'name': u'Part Load Fraction Correlation Curve Name',
                                        'pyname': u'part_load_fraction_correlation_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum dry-bulb temperature for dehumidifier operation',
                                       {'name': u'Minimum Dry-Bulb Temperature for Dehumidifier Operation',
                                        'pyname': u'minimum_drybulb_temperature_for_dehumidifier_operation',
                                        'default': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum dry-bulb temperature for dehumidifier operation',
                                       {'name': u'Maximum Dry-Bulb Temperature for Dehumidifier Operation',
                                        'pyname': u'maximum_drybulb_temperature_for_dehumidifier_operation',
                                        'default': 35.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'off-cycle parasitic electric load',
                                       {'name': u'Off-Cycle Parasitic Electric Load',
                                        'pyname': u'offcycle_parasitic_electric_load',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'condensate collection water storage tank name',
                                       {'name': u'Condensate Collection Water Storage Tank Name',
                                        'pyname': u'condensate_collection_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 13,
               'name': u'ZoneHVAC:Dehumidifier:DX',
               'pyname': u'ZoneHvacDehumidifierDx',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Unique name for this direct expansion (DX) zone dehumidifier object.

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
        |  Schedule values of 0 denote the unit is off.
        |  Schedule values >0.0 (usually 1.0) indicate that the dehumidifier is available to operate.

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
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  Air inlet node for the dehumidifier must be a zone air exhaust node.

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

        |  Air outlet node for the dehumidifier must be a zone air inlet node.

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
    def rated_water_removal(self):
        """field `Rated Water Removal`

        |  Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.
        |  Units: L/day

        Args:
            value (float): value for IDD Field `Rated Water Removal`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_water_removal` or None if not set

        """
        return self["Rated Water Removal"]

    @rated_water_removal.setter
    def rated_water_removal(self, value=None):
        """Corresponds to IDD field `Rated Water Removal`"""
        self["Rated Water Removal"] = value

    @property
    def rated_energy_factor(self):
        """field `Rated Energy Factor`

        |  Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.
        |  Units: L/kWh

        Args:
            value (float): value for IDD Field `Rated Energy Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_energy_factor` or None if not set

        """
        return self["Rated Energy Factor"]

    @rated_energy_factor.setter
    def rated_energy_factor(self, value=None):
        """Corresponds to IDD field `Rated Energy Factor`"""
        self["Rated Energy Factor"] = value

    @property
    def rated_air_flow_rate(self):
        """field `Rated Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Rated Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_air_flow_rate` or None if not set

        """
        return self["Rated Air Flow Rate"]

    @rated_air_flow_rate.setter
    def rated_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Rated Air Flow Rate`"""
        self["Rated Air Flow Rate"] = value

    @property
    def water_removal_curve_name(self):
        """field `Water Removal Curve Name`

        |  Name of a curve that describes the water removal rate (normalized to rated conditions)
        |  as a function of the dry-bulb temperature and relative humidity of the air
        |  entering the dehumidifier.
        |  Curve output = (actual water removal/rated water removal) = a + b*T + c*T**2 + d*RH +
        |  e*RH**2 + f*T*RH
        |  T = inlet air dry-bulb temperature (C)
        |  RH = inlet air RH (%)

        Args:
            value (str): value for IDD Field `Water Removal Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_removal_curve_name` or None if not set

        """
        return self["Water Removal Curve Name"]

    @water_removal_curve_name.setter
    def water_removal_curve_name(self, value=None):
        """Corresponds to IDD field `Water Removal Curve Name`"""
        self["Water Removal Curve Name"] = value

    @property
    def energy_factor_curve_name(self):
        """field `Energy Factor Curve Name`

        |  Name of a curve that describes the energy factor (normalized to rated conditions)
        |  as a function of the dry-bulb temperature and relative humidity of the air
        |  entering the dehumidifier.
        |  Curve output = (actual energy factor/rated energy factor) = a + b*T + c*T**2 + d*RH +
        |  e*RH**2 + f*T*RH
        |  T = inlet air dry-bulb temperature (C)
        |  RH = inlet air RH (%)

        Args:
            value (str): value for IDD Field `Energy Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `energy_factor_curve_name` or None if not set

        """
        return self["Energy Factor Curve Name"]

    @energy_factor_curve_name.setter
    def energy_factor_curve_name(self, value=None):
        """Corresponds to IDD field `Energy Factor Curve Name`"""
        self["Energy Factor Curve Name"] = value

    @property
    def part_load_fraction_correlation_curve_name(self):
        """field `Part Load Fraction Correlation Curve Name`

        |  Name of a curve that describes the part load fraction (PLF) of the system as
        |  a function of the part load ratio. Used to calculate dehumidifier run time fraction
        |  and electric power.
        |  quadratic curve = a + b*PLR + c*PLR**2
        |  cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3
        |  PLR = part load ratio (dehumidification load/steady state water removal capacity)

        Args:
            value (str): value for IDD Field `Part Load Fraction Correlation Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `part_load_fraction_correlation_curve_name` or None if not set

        """
        return self["Part Load Fraction Correlation Curve Name"]

    @part_load_fraction_correlation_curve_name.setter
    def part_load_fraction_correlation_curve_name(self, value=None):
        """Corresponds to IDD field `Part Load Fraction Correlation Curve
        Name`"""
        self["Part Load Fraction Correlation Curve Name"] = value

    @property
    def minimum_drybulb_temperature_for_dehumidifier_operation(self):
        """field `Minimum Dry-Bulb Temperature for Dehumidifier Operation`

        |  Dehumidifier shut off if inlet air (zone) temperature is below this value.
        |  This value must be less than the Maximum Dry-Bulb Temperature for Dehumidifier Operation.
        |  Units: C
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Minimum Dry-Bulb Temperature for Dehumidifier Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_drybulb_temperature_for_dehumidifier_operation` or None if not set
        """
        return self["Minimum Dry-Bulb Temperature for Dehumidifier Operation"]

    @minimum_drybulb_temperature_for_dehumidifier_operation.setter
    def minimum_drybulb_temperature_for_dehumidifier_operation(
            self,
            value=10.0):
        """  Corresponds to IDD field `Minimum Dry-Bulb Temperature for Dehumidifier Operation`

        """
        self["Minimum Dry-Bulb Temperature for Dehumidifier Operation"] = value

    @property
    def maximum_drybulb_temperature_for_dehumidifier_operation(self):
        """field `Maximum Dry-Bulb Temperature for Dehumidifier Operation`

        |  Dehumidifier shut off if inlet air (zone) temperature is above this value.
        |  This value must be greater than the Minimum Dry-Bulb Temperature for Dehumidifier Operation.
        |  Units: C
        |  Default value: 35.0

        Args:
            value (float): value for IDD Field `Maximum Dry-Bulb Temperature for Dehumidifier Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_drybulb_temperature_for_dehumidifier_operation` or None if not set
        """
        return self["Maximum Dry-Bulb Temperature for Dehumidifier Operation"]

    @maximum_drybulb_temperature_for_dehumidifier_operation.setter
    def maximum_drybulb_temperature_for_dehumidifier_operation(
            self,
            value=35.0):
        """  Corresponds to IDD field `Maximum Dry-Bulb Temperature for Dehumidifier Operation`

        """
        self["Maximum Dry-Bulb Temperature for Dehumidifier Operation"] = value

    @property
    def offcycle_parasitic_electric_load(self):
        """field `Off-Cycle Parasitic Electric Load`

        |  Parasitic electric power consumed when the dehumidifier is available to operate, but
        |  does not operate (i.e., no high humidity load to be met).
        |  Off cycle parasitic power is 0 when the availability schedule is 0.
        |  This electric load is considered as a heat gain to the zone air.
        |  Units: W

        Args:
            value (float): value for IDD Field `Off-Cycle Parasitic Electric Load`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `offcycle_parasitic_electric_load` or None if not set
        """
        return self["Off-Cycle Parasitic Electric Load"]

    @offcycle_parasitic_electric_load.setter
    def offcycle_parasitic_electric_load(self, value=None):
        """  Corresponds to IDD field `Off-Cycle Parasitic Electric Load`

        """
        self["Off-Cycle Parasitic Electric Load"] = value

    @property
    def condensate_collection_water_storage_tank_name(self):
        """field `Condensate Collection Water Storage Tank Name`

        |  Name of storage tank used to collect water removed by the dehumidifier.

        Args:
            value (str): value for IDD Field `Condensate Collection Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condensate_collection_water_storage_tank_name` or None if not set

        """
        return self["Condensate Collection Water Storage Tank Name"]

    @condensate_collection_water_storage_tank_name.setter
    def condensate_collection_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Condensate Collection Water Storage Tank
        Name`"""
        self["Condensate Collection Water Storage Tank Name"] = value




class ZoneHvacEnergyRecoveryVentilator(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:EnergyRecoveryVentilator`
        This compound component models a stand-alone energy recovery ventilator (ERV)
        that conditions outdoor ventilation air and supplies that air directly to a zone.
        The ERV unit is modeled as a collection of components: air-to-air heat exchanger,
        supply air fan, exhaust air fan and an optional controller to avoid overheating
        of the supply air (economizer or free cooling operation).
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
                                      (u'heat exchanger name',
                                       {'name': u'Heat Exchanger Name',
                                        'pyname': u'heat_exchanger_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air flow rate',
                                       {'name': u'Supply Air Flow Rate',
                                        'pyname': u'supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'exhaust air flow rate',
                                       {'name': u'Exhaust Air Flow Rate',
                                        'pyname': u'exhaust_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'exhaust air fan name',
                                       {'name': u'Exhaust Air Fan Name',
                                        'pyname': u'exhaust_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'controller name',
                                       {'name': u'Controller Name',
                                        'pyname': u'controller_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ventilation rate per unit floor area',
                                       {'name': u'Ventilation Rate per Unit Floor Area',
                                        'pyname': u'ventilation_rate_per_unit_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'ventilation rate per occupant',
                                       {'name': u'Ventilation Rate per Occupant',
                                        'pyname': u'ventilation_rate_per_occupant',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-person'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 7,
               'name': u'ZoneHVAC:EnergyRecoveryVentilator',
               'pyname': u'ZoneHvacEnergyRecoveryVentilator',
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
    def heat_exchanger_name(self):
        """field `Heat Exchanger Name`

        |  Heat exchanger type must be HeatExchanger:AirToAir:SensibleAndLatent

        Args:
            value (str): value for IDD Field `Heat Exchanger Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_exchanger_name` or None if not set

        """
        return self["Heat Exchanger Name"]

    @heat_exchanger_name.setter
    def heat_exchanger_name(self, value=None):
        """Corresponds to IDD field `Heat Exchanger Name`"""
        self["Heat Exchanger Name"] = value

    @property
    def supply_air_flow_rate(self):
        """field `Supply Air Flow Rate`

        |  This flow rate must match the supply fan's air flow rate.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `supply_air_flow_rate` or None if not set

        """
        return self["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate`"""
        self["Supply Air Flow Rate"] = value

    @property
    def exhaust_air_flow_rate(self):
        """field `Exhaust Air Flow Rate`

        |  This flow rate must match the supply fan air flow rate.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Exhaust Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `exhaust_air_flow_rate` or None if not set

        """
        return self["Exhaust Air Flow Rate"]

    @exhaust_air_flow_rate.setter
    def exhaust_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Exhaust Air Flow Rate`"""
        self["Exhaust Air Flow Rate"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        |  Fan type must be Fan:OnOff

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def exhaust_air_fan_name(self):
        """field `Exhaust Air Fan Name`

        |  Fan type must be Fan:OnOff

        Args:
            value (str): value for IDD Field `Exhaust Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_fan_name` or None if not set

        """
        return self["Exhaust Air Fan Name"]

    @exhaust_air_fan_name.setter
    def exhaust_air_fan_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Fan Name`"""
        self["Exhaust Air Fan Name"] = value

    @property
    def controller_name(self):
        """field `Controller Name`

        |  Enter the name of a ZoneHVAC:EnergyRecoveryVentilator:Controller object.

        Args:
            value (str): value for IDD Field `Controller Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_name` or None if not set

        """
        return self["Controller Name"]

    @controller_name.setter
    def controller_name(self, value=None):
        """Corresponds to IDD field `Controller Name`"""
        self["Controller Name"] = value

    @property
    def ventilation_rate_per_unit_floor_area(self):
        """field `Ventilation Rate per Unit Floor Area`

        |  0.000508 m3/s-m2 corresponds to 0.1 ft3/min-ft2
        |  Used only when supply and exhaust air flow rates are autosized.
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Ventilation Rate per Unit Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ventilation_rate_per_unit_floor_area` or None if not set

        """
        return self["Ventilation Rate per Unit Floor Area"]

    @ventilation_rate_per_unit_floor_area.setter
    def ventilation_rate_per_unit_floor_area(self, value=None):
        """Corresponds to IDD field `Ventilation Rate per Unit Floor Area`"""
        self["Ventilation Rate per Unit Floor Area"] = value

    @property
    def ventilation_rate_per_occupant(self):
        """field `Ventilation Rate per Occupant`

        |  0.00236 m3/s-person corresponds to 5 ft3/min-person
        |  Used only when supply and exhaust air flow rates are autosized.
        |  Units: m3/s-person

        Args:
            value (float): value for IDD Field `Ventilation Rate per Occupant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ventilation_rate_per_occupant` or None if not set

        """
        return self["Ventilation Rate per Occupant"]

    @ventilation_rate_per_occupant.setter
    def ventilation_rate_per_occupant(self, value=None):
        """Corresponds to IDD field `Ventilation Rate per Occupant`"""
        self["Ventilation Rate per Occupant"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value




class ZoneHvacEnergyRecoveryVentilatorController(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:EnergyRecoveryVentilator:Controller`
        This controller is used exclusively by the ZoneHVAC:EnergyRecoveryVentilator object
        to allow economizer (free cooling) operation when possible.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'temperature high limit',
                                       {'name': u'Temperature High Limit',
                                        'pyname': u'temperature_high_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'temperature low limit',
                                       {'name': u'Temperature Low Limit',
                                        'pyname': u'temperature_low_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'enthalpy high limit',
                                       {'name': u'Enthalpy High Limit',
                                        'pyname': u'enthalpy_high_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'dewpoint temperature limit',
                                       {'name': u'Dewpoint Temperature Limit',
                                        'pyname': u'dewpoint_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'electronic enthalpy limit curve name',
                                       {'name': u'Electronic Enthalpy Limit Curve Name',
                                        'pyname': u'electronic_enthalpy_limit_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'exhaust air temperature limit',
                                       {'name': u'Exhaust Air Temperature Limit',
                                        'pyname': u'exhaust_air_temperature_limit',
                                        'default': u'NoExhaustAirTemperatureLimit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ExhaustAirTemperatureLimit',
                                                            u'NoExhaustAirTemperatureLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'exhaust air enthalpy limit',
                                       {'name': u'Exhaust Air Enthalpy Limit',
                                        'pyname': u'exhaust_air_enthalpy_limit',
                                        'default': u'NoExhaustAirEnthalpyLimit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ExhaustAirEnthalpyLimit',
                                                            u'NoExhaustAirEnthalpyLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'time of day economizer flow control schedule name',
                                       {'name': u'Time of Day Economizer Flow Control Schedule Name',
                                        'pyname': u'time_of_day_economizer_flow_control_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'high humidity control flag',
                                       {'name': u'High Humidity Control Flag',
                                        'pyname': u'high_humidity_control_flag',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'humidistat control zone name',
                                       {'name': u'Humidistat Control Zone Name',
                                        'pyname': u'humidistat_control_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'high humidity outdoor air flow ratio',
                                       {'name': u'High Humidity Outdoor Air Flow Ratio',
                                        'pyname': u'high_humidity_outdoor_air_flow_ratio',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'control high indoor humidity based on outdoor humidity ratio',
                                       {'name': u'Control High Indoor Humidity Based on Outdoor Humidity Ratio',
                                        'pyname': u'control_high_indoor_humidity_based_on_outdoor_humidity_ratio',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 3,
               'name': u'ZoneHVAC:EnergyRecoveryVentilator:Controller',
               'pyname': u'ZoneHvacEnergyRecoveryVentilatorController',
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
    def temperature_high_limit(self):
        """field `Temperature High Limit`

        |  Enter the maximum outdoor dry-bulb temperature limit for economizer operation.
        |  No input or blank input means this limit is not operative
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature High Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_high_limit` or None if not set

        """
        return self["Temperature High Limit"]

    @temperature_high_limit.setter
    def temperature_high_limit(self, value=None):
        """Corresponds to IDD field `Temperature High Limit`"""
        self["Temperature High Limit"] = value

    @property
    def temperature_low_limit(self):
        """field `Temperature Low Limit`

        |  Enter the minimum outdoor dry-bulb temperature limit for economizer operation.
        |  No input or blank input means this limit is not operative
        |  Units: C

        Args:
            value (float): value for IDD Field `Temperature Low Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_low_limit` or None if not set

        """
        return self["Temperature Low Limit"]

    @temperature_low_limit.setter
    def temperature_low_limit(self, value=None):
        """Corresponds to IDD field `Temperature Low Limit`"""
        self["Temperature Low Limit"] = value

    @property
    def enthalpy_high_limit(self):
        """field `Enthalpy High Limit`

        |  Enter the maximum outdoor enthalpy limit for economizer operation.
        |  No input or blank input means this limit is not operative
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy High Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_high_limit` or None if not set

        """
        return self["Enthalpy High Limit"]

    @enthalpy_high_limit.setter
    def enthalpy_high_limit(self, value=None):
        """Corresponds to IDD field `Enthalpy High Limit`"""
        self["Enthalpy High Limit"] = value

    @property
    def dewpoint_temperature_limit(self):
        """field `Dewpoint Temperature Limit`

        |  Enter the maximum outdoor dew point temperature limit for economizer operation.
        |  No input or blank input means this limit is not operative
        |  Units: C

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_limit` or None if not set

        """
        return self["Dewpoint Temperature Limit"]

    @dewpoint_temperature_limit.setter
    def dewpoint_temperature_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Limit`"""
        self["Dewpoint Temperature Limit"] = value

    @property
    def electronic_enthalpy_limit_curve_name(self):
        """field `Electronic Enthalpy Limit Curve Name`

        |  Enter the name of a quadratic or cubic curve which defines the maximum outdoor
        |  humidity ratio (function of outdoor dry-bulb temperature) for economizer operation.
        |  No input or blank input means this limit is not operative

        Args:
            value (str): value for IDD Field `Electronic Enthalpy Limit Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `electronic_enthalpy_limit_curve_name` or None if not set

        """
        return self["Electronic Enthalpy Limit Curve Name"]

    @electronic_enthalpy_limit_curve_name.setter
    def electronic_enthalpy_limit_curve_name(self, value=None):
        """Corresponds to IDD field `Electronic Enthalpy Limit Curve Name`"""
        self["Electronic Enthalpy Limit Curve Name"] = value

    @property
    def exhaust_air_temperature_limit(self):
        """field `Exhaust Air Temperature Limit`

        |  Default value: NoExhaustAirTemperatureLimit

        Args:
            value (str): value for IDD Field `Exhaust Air Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_temperature_limit` or None if not set

        """
        return self["Exhaust Air Temperature Limit"]

    @exhaust_air_temperature_limit.setter
    def exhaust_air_temperature_limit(
            self,
            value="NoExhaustAirTemperatureLimit"):
        """Corresponds to IDD field `Exhaust Air Temperature Limit`"""
        self["Exhaust Air Temperature Limit"] = value

    @property
    def exhaust_air_enthalpy_limit(self):
        """field `Exhaust Air Enthalpy Limit`

        |  Default value: NoExhaustAirEnthalpyLimit

        Args:
            value (str): value for IDD Field `Exhaust Air Enthalpy Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_enthalpy_limit` or None if not set

        """
        return self["Exhaust Air Enthalpy Limit"]

    @exhaust_air_enthalpy_limit.setter
    def exhaust_air_enthalpy_limit(self, value="NoExhaustAirEnthalpyLimit"):
        """Corresponds to IDD field `Exhaust Air Enthalpy Limit`"""
        self["Exhaust Air Enthalpy Limit"] = value

    @property
    def time_of_day_economizer_flow_control_schedule_name(self):
        """field `Time of Day Economizer Flow Control Schedule Name`

        |  Schedule values greater than 0 indicate economizer operation is active. This
        |  schedule may be used with or without the High Humidity Control option.
        |  When used together, high humidity control has priority over economizer control.

        Args:
            value (str): value for IDD Field `Time of Day Economizer Flow Control Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `time_of_day_economizer_flow_control_schedule_name` or None if not set

        """
        return self["Time of Day Economizer Flow Control Schedule Name"]

    @time_of_day_economizer_flow_control_schedule_name.setter
    def time_of_day_economizer_flow_control_schedule_name(self, value=None):
        """Corresponds to IDD field `Time of Day Economizer Flow Control
        Schedule Name`"""
        self["Time of Day Economizer Flow Control Schedule Name"] = value

    @property
    def high_humidity_control_flag(self):
        """field `High Humidity Control Flag`

        |  Select Yes to modify air flow rates based on a zone humidistat.
        |  Select No to disable this feature.
        |  Default value: No

        Args:
            value (str): value for IDD Field `High Humidity Control Flag`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `high_humidity_control_flag` or None if not set

        """
        return self["High Humidity Control Flag"]

    @high_humidity_control_flag.setter
    def high_humidity_control_flag(self, value="No"):
        """Corresponds to IDD field `High Humidity Control Flag`"""
        self["High Humidity Control Flag"] = value

    @property
    def humidistat_control_zone_name(self):
        """field `Humidistat Control Zone Name`

        |  Enter the name of the zone where the humidistat is located.

        Args:
            value (str): value for IDD Field `Humidistat Control Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `humidistat_control_zone_name` or None if not set

        """
        return self["Humidistat Control Zone Name"]

    @humidistat_control_zone_name.setter
    def humidistat_control_zone_name(self, value=None):
        """Corresponds to IDD field `Humidistat Control Zone Name`"""
        self["Humidistat Control Zone Name"] = value

    @property
    def high_humidity_outdoor_air_flow_ratio(self):
        """field `High Humidity Outdoor Air Flow Ratio`

        |  Enter the ratio of supply (outdoor) air to the maximum supply air flow rate when modified
        |  air flow rates are active based on high indoor humidity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `High Humidity Outdoor Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `high_humidity_outdoor_air_flow_ratio` or None if not set

        """
        return self["High Humidity Outdoor Air Flow Ratio"]

    @high_humidity_outdoor_air_flow_ratio.setter
    def high_humidity_outdoor_air_flow_ratio(self, value=1.0):
        """Corresponds to IDD field `High Humidity Outdoor Air Flow Ratio`"""
        self["High Humidity Outdoor Air Flow Ratio"] = value

    @property
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(self):
        """field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`

        |  If NO is selected, the air flow rate is modified any time indoor relative
        |  humidity is above humidistat setpoint. If YES is selected, outdoor air flow
        |  rate is modified any time indoor relative humidity is above the humidistat
        |  setpoint AND the outdoor humidity ratio is less than the indoor humidity ratio.
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Control High Indoor Humidity Based on Outdoor Humidity Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_high_indoor_humidity_based_on_outdoor_humidity_ratio` or None if not set

        """
        return self[
            "Control High Indoor Humidity Based on Outdoor Humidity Ratio"]

    @control_high_indoor_humidity_based_on_outdoor_humidity_ratio.setter
    def control_high_indoor_humidity_based_on_outdoor_humidity_ratio(
            self,
            value="Yes"):
        """Corresponds to IDD field `Control High Indoor Humidity Based on
        Outdoor Humidity Ratio`"""
        self[
            "Control High Indoor Humidity Based on Outdoor Humidity Ratio"] = value




class ZoneHvacUnitVentilator(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:UnitVentilator`
        Unit ventilator. Forced-convection ventilation unit with supply fan (constant-volume
        or variable-volume), optional chilled water cooling coil, optional heating coil
        (gas, electric, hot water, or steam) and controllable outdoor air mixer.
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
                                      (u'maximum supply air flow rate',
                                       {'name': u'Maximum Supply Air Flow Rate',
                                        'pyname': u'maximum_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air control type',
                                       {'name': u'Outdoor Air Control Type',
                                        'pyname': u'outdoor_air_control_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'FixedAmount',
                                                            u'VariablePercent',
                                                            u'FixedTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum outdoor air flow rate',
                                       {'name': u'Minimum Outdoor Air Flow Rate',
                                        'pyname': u'minimum_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum outdoor air schedule name',
                                       {'name': u'Minimum Outdoor Air Schedule Name',
                                        'pyname': u'minimum_outdoor_air_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum outdoor air flow rate',
                                       {'name': u'Maximum Outdoor Air Flow Rate',
                                        'pyname': u'maximum_outdoor_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum outdoor air fraction or temperature schedule name',
                                       {'name': u'Maximum Outdoor Air Fraction or Temperature Schedule Name',
                                        'pyname': u'maximum_outdoor_air_fraction_or_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air node name',
                                       {'name': u'Outdoor Air Node Name',
                                        'pyname': u'outdoor_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'exhaust air node name',
                                       {'name': u'Exhaust Air Node Name',
                                        'pyname': u'exhaust_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'mixed air node name',
                                       {'name': u'Mixed Air Node Name',
                                        'pyname': u'mixed_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume',
                                                            u'Fan:VariableVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'coil option',
                                       {'name': u'Coil Option',
                                        'pyname': u'coil_option',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Heating',
                                                            u'Cooling',
                                                            u'HeatingAndCooling'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating convergence tolerance',
                                       {'name': u'Heating Convergence Tolerance',
                                        'pyname': u'heating_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatExchangerAssisted'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling convergence tolerance',
                                       {'name': u'Cooling Convergence Tolerance',
                                        'pyname': u'cooling_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 16,
               'name': u'ZoneHVAC:UnitVentilator',
               'pyname': u'ZoneHvacUnitVentilator',
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
    def maximum_supply_air_flow_rate(self):
        """field `Maximum Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_supply_air_flow_rate` or None if not set

        """
        return self["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Supply Air Flow Rate`"""
        self["Maximum Supply Air Flow Rate"] = value

    @property
    def outdoor_air_control_type(self):
        """field `Outdoor Air Control Type`

        Args:
            value (str): value for IDD Field `Outdoor Air Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_control_type` or None if not set

        """
        return self["Outdoor Air Control Type"]

    @outdoor_air_control_type.setter
    def outdoor_air_control_type(self, value=None):
        """Corresponds to IDD field `Outdoor Air Control Type`"""
        self["Outdoor Air Control Type"] = value

    @property
    def minimum_outdoor_air_flow_rate(self):
        """field `Minimum Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `minimum_outdoor_air_flow_rate` or None if not set

        """
        return self["Minimum Outdoor Air Flow Rate"]

    @minimum_outdoor_air_flow_rate.setter
    def minimum_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Air Flow Rate`"""
        self["Minimum Outdoor Air Flow Rate"] = value

    @property
    def minimum_outdoor_air_schedule_name(self):
        """field `Minimum Outdoor Air Schedule Name`

        |  schedule values multiply the minimum outdoor air flow rate

        Args:
            value (str): value for IDD Field `Minimum Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_air_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Air Schedule Name"]

    @minimum_outdoor_air_schedule_name.setter
    def minimum_outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Air Schedule Name`"""
        self["Minimum Outdoor Air Schedule Name"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """field `Maximum Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_outdoor_air_flow_rate` or None if not set

        """
        return self["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Air Flow Rate`"""
        self["Maximum Outdoor Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_fraction_or_temperature_schedule_name(self):
        """field `Maximum Outdoor Air Fraction or Temperature Schedule Name`

        |  that this depends on the control type as to whether it is a fraction or temperature

        Args:
            value (str): value for IDD Field `Maximum Outdoor Air Fraction or Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_outdoor_air_fraction_or_temperature_schedule_name` or None if not set

        """
        return self[
            "Maximum Outdoor Air Fraction or Temperature Schedule Name"]

    @maximum_outdoor_air_fraction_or_temperature_schedule_name.setter
    def maximum_outdoor_air_fraction_or_temperature_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Outdoor Air Fraction or
        Temperature Schedule Name`"""
        self[
            "Maximum Outdoor Air Fraction or Temperature Schedule Name"] = value

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
    def outdoor_air_node_name(self):
        """field `Outdoor Air Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set

        """
        return self["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Node Name`"""
        self["Outdoor Air Node Name"] = value

    @property
    def exhaust_air_node_name(self):
        """field `Exhaust Air Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_node_name` or None if not set

        """
        return self["Exhaust Air Node Name"]

    @exhaust_air_node_name.setter
    def exhaust_air_node_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Node Name`"""
        self["Exhaust Air Node Name"] = value

    @property
    def mixed_air_node_name(self):
        """field `Mixed Air Node Name`

        |  inlet to coils

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_air_node_name` or None if not set

        """
        return self["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """Corresponds to IDD field `Mixed Air Node Name`"""
        self["Mixed Air Node Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Allowable fan types are Fan:ConstantVolume, Fan:OnOff and
        |  Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def coil_option(self):
        """field `Coil Option`

        Args:
            value (str): value for IDD Field `Coil Option`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `coil_option` or None if not set

        """
        return self["Coil Option"]

    @coil_option.setter
    def coil_option(self, value=None):
        """Corresponds to IDD field `Coil Option`"""
        self["Coil Option"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule
        |  name values of 0 denote cycling fan operation (fan cycles with
        |  cooling/heating coil). Schedule values greater than 0 denote
        |  constant fan operation (fan runs continually regardless of coil
        |  operation). The fan operating mode defaults to cycling fan operation
        |  if this input field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def heating_convergence_tolerance(self):
        """field `Heating Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set

        """
        return self["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence Tolerance`"""
        self["Heating Convergence Tolerance"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_name` or None if not set

        """
        return self["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Name`"""
        self["Cooling Coil Name"] = value

    @property
    def cooling_convergence_tolerance(self):
        """field `Cooling Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set

        """
        return self["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Cooling Convergence Tolerance`"""
        self["Cooling Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacUnitHeater(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:UnitHeater`
        Unit heater. Forced-convection heating-only unit with supply fan, heating coil
        (gas, electric, hot water, or steam) and fixed-position outdoor air mixer.
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
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume',
                                                            u'Fan:VariableVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air flow rate',
                                       {'name': u'Maximum Supply Air Flow Rate',
                                        'pyname': u'maximum_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan operation during no heating',
                                       {'name': u'Supply Air Fan Operation During No Heating',
                                        'pyname': u'supply_air_fan_operation_during_no_heating',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'heating convergence tolerance',
                                       {'name': u'Heating Convergence Tolerance',
                                        'pyname': u'heating_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 11,
               'name': u'ZoneHVAC:UnitHeater',
               'pyname': u'ZoneHvacUnitHeater',
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
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Allowable fan types are Fan:ConstantVolume, Fan:OnOff and
        |  Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def maximum_supply_air_flow_rate(self):
        """field `Maximum Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_supply_air_flow_rate` or None if not set

        """
        return self["Maximum Supply Air Flow Rate"]

    @maximum_supply_air_flow_rate.setter
    def maximum_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Supply Air Flow Rate`"""
        self["Maximum Supply Air Flow Rate"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        |  Enter the name of a schedule that controls fan operation. Schedule
        |  name values of 0 denote cycling fan operation (fan cycles with the
        |  heating coil). Schedule values greater than 0 denote constant fan
        |  operation (fan runs continually regardless of coil operation).
        |  The fan operating mode defaults to cycling fan operation if this
        |  input field is left blank.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def supply_air_fan_operation_during_no_heating(self):
        """field `Supply Air Fan Operation During No Heating`

        |  This choice field allows the user to define how the unit heater will operate
        |  under "no heating load" or cooling conditions. If the "No" is selected, then
        |  the fan will not run unless there is a heating load. If the fan does not run,
        |  this effectively shuts the unit heater system off when there is no heating load.
        |  If the "Yes" is selected, the unit heater is available and has a ConstantVolume
        |  fan, or has an OnOff fan with "Supply Air Fan Operating Mode Schedule" value
        |  greater than zero, then the fan will always run regardless of the zone load.

        Args:
            value (str): value for IDD Field `Supply Air Fan Operation During No Heating`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operation_during_no_heating` or None if not set

        """
        return self["Supply Air Fan Operation During No Heating"]

    @supply_air_fan_operation_during_no_heating.setter
    def supply_air_fan_operation_during_no_heating(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operation During No
        Heating`"""
        self["Supply Air Fan Operation During No Heating"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when heating coil is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when heating coil is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """field `Heating Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set

        """
        return self["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence Tolerance`"""
        self["Heating Convergence Tolerance"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacEvaporativeCoolerUnit(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:EvaporativeCoolerUnit`
        Zone evaporative cooler. Forced-convection cooling-only unit with supply fan,
        100% outdoor air supply.  Optional relief exhaust node
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
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outdoor air inlet node name',
                                       {'name': u'Outdoor Air Inlet Node Name',
                                        'pyname': u'outdoor_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cooler outlet node name',
                                       {'name': u'Cooler Outlet Node Name',
                                        'pyname': u'cooler_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone relief air node name',
                                       {'name': u'Zone Relief Air Node Name',
                                        'pyname': u'zone_relief_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:ConstantVolume',
                                                            u'Fan:OnOff',
                                                            u'Fan:VariableVolume',
                                                            u'Fan:ComponentModel'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan name',
                                       {'name': u'Supply Air Fan Name',
                                        'pyname': u'supply_air_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design supply air flow rate',
                                       {'name': u'Design Supply Air Flow Rate',
                                        'pyname': u'design_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooler unit control method',
                                       {'name': u'Cooler Unit Control Method',
                                        'pyname': u'cooler_unit_control_method',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneTemperatureDeadbandOnOffCycling',
                                                            u'ZoneCoolingLoadOnOffCycling',
                                                            u'ZoneCoolingLoadVariableSpeedFan'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'throttling range temperature difference',
                                       {'name': u'Throttling Range Temperature Difference',
                                        'pyname': u'throttling_range_temperature_difference',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'cooling load control threshold heat transfer rate',
                                       {'name': u'Cooling Load Control Threshold Heat Transfer Rate',
                                        'pyname': u'cooling_load_control_threshold_heat_transfer_rate',
                                        'default': 100.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'first evaporative cooler object type',
                                       {'name': u'First Evaporative Cooler Object Type',
                                        'pyname': u'first_evaporative_cooler_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'EvaporativeCooler:Direct:CelDekPad',
                                                            u'EvaporativeCooler:Direct:ResearchSpecial',
                                                            u'EvaporativeCooler:Indirect:CelDekPad',
                                                            u'EvaporativeCooler:Indirect:WetCoil',
                                                            u'EvaporativeCooler:Indirect:ResearchSpecial'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'first evaporative cooler object name',
                                       {'name': u'First Evaporative Cooler Object Name',
                                        'pyname': u'first_evaporative_cooler_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'second evaporative cooler object type',
                                       {'name': u'Second Evaporative Cooler Object Type',
                                        'pyname': u'second_evaporative_cooler_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'EvaporativeCooler:Direct:CelDekPad',
                                                            u'EvaporativeCooler:Direct:ResearchSpecial',
                                                            u'EvaporativeCooler:Indirect:CelDekPad',
                                                            u'EvaporativeCooler:Indirect:WetCoil',
                                                            u'EvaporativeCooler:Indirect:ResearchSpecial'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'second evaporative cooler name',
                                       {'name': u'Second Evaporative Cooler Name',
                                        'pyname': u'second_evaporative_cooler_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 15,
               'name': u'ZoneHVAC:EvaporativeCoolerUnit',
               'pyname': u'ZoneHvacEvaporativeCoolerUnit',
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
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def outdoor_air_inlet_node_name(self):
        """field `Outdoor Air Inlet Node Name`

        |  this is an outdoor air node

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set

        """
        return self["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Inlet Node Name`"""
        self["Outdoor Air Inlet Node Name"] = value

    @property
    def cooler_outlet_node_name(self):
        """field `Cooler Outlet Node Name`

        |  this is a zone inlet node

        Args:
            value (str): value for IDD Field `Cooler Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooler_outlet_node_name` or None if not set

        """
        return self["Cooler Outlet Node Name"]

    @cooler_outlet_node_name.setter
    def cooler_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Cooler Outlet Node Name`"""
        self["Cooler Outlet Node Name"] = value

    @property
    def zone_relief_air_node_name(self):
        """field `Zone Relief Air Node Name`

        |  this is a zone exhaust node, optional if flow is being balanced elsewhere

        Args:
            value (str): value for IDD Field `Zone Relief Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_relief_air_node_name` or None if not set

        """
        return self["Zone Relief Air Node Name"]

    @zone_relief_air_node_name.setter
    def zone_relief_air_node_name(self, value=None):
        """Corresponds to IDD field `Zone Relief Air Node Name`"""
        self["Zone Relief Air Node Name"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_name(self):
        """field `Supply Air Fan Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_name` or None if not set

        """
        return self["Supply Air Fan Name"]

    @supply_air_fan_name.setter
    def supply_air_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Name`"""
        self["Supply Air Fan Name"] = value

    @property
    def design_supply_air_flow_rate(self):
        """field `Design Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Design Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_supply_air_flow_rate` or None if not set

        """
        return self["Design Supply Air Flow Rate"]

    @design_supply_air_flow_rate.setter
    def design_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate`"""
        self["Design Supply Air Flow Rate"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value=None):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def cooler_unit_control_method(self):
        """field `Cooler Unit Control Method`

        Args:
            value (str): value for IDD Field `Cooler Unit Control Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooler_unit_control_method` or None if not set

        """
        return self["Cooler Unit Control Method"]

    @cooler_unit_control_method.setter
    def cooler_unit_control_method(self, value=None):
        """Corresponds to IDD field `Cooler Unit Control Method`"""
        self["Cooler Unit Control Method"] = value

    @property
    def throttling_range_temperature_difference(self):
        """field `Throttling Range Temperature Difference`

        |  used for ZoneTemperatureDeadbandOnOffCycling hystersis range for thermostatic control
        |  Units: deltaC
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Throttling Range Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `throttling_range_temperature_difference` or None if not set

        """
        return self["Throttling Range Temperature Difference"]

    @throttling_range_temperature_difference.setter
    def throttling_range_temperature_difference(self, value=1.0):
        """Corresponds to IDD field `Throttling Range Temperature
        Difference`"""
        self["Throttling Range Temperature Difference"] = value

    @property
    def cooling_load_control_threshold_heat_transfer_rate(self):
        """field `Cooling Load Control Threshold Heat Transfer Rate`

        |  Sign convention is that positive values indicate a cooling load
        |  Units: W
        |  Default value: 100.0

        Args:
            value (float): value for IDD Field `Cooling Load Control Threshold Heat Transfer Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_load_control_threshold_heat_transfer_rate` or None if not set

        """
        return self["Cooling Load Control Threshold Heat Transfer Rate"]

    @cooling_load_control_threshold_heat_transfer_rate.setter
    def cooling_load_control_threshold_heat_transfer_rate(self, value=100.0):
        """Corresponds to IDD field `Cooling Load Control Threshold Heat
        Transfer Rate`"""
        self["Cooling Load Control Threshold Heat Transfer Rate"] = value

    @property
    def first_evaporative_cooler_object_type(self):
        """field `First Evaporative Cooler Object Type`

        Args:
            value (str): value for IDD Field `First Evaporative Cooler Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `first_evaporative_cooler_object_type` or None if not set

        """
        return self["First Evaporative Cooler Object Type"]

    @first_evaporative_cooler_object_type.setter
    def first_evaporative_cooler_object_type(self, value=None):
        """Corresponds to IDD field `First Evaporative Cooler Object Type`"""
        self["First Evaporative Cooler Object Type"] = value

    @property
    def first_evaporative_cooler_object_name(self):
        """field `First Evaporative Cooler Object Name`

        Args:
            value (str): value for IDD Field `First Evaporative Cooler Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `first_evaporative_cooler_object_name` or None if not set

        """
        return self["First Evaporative Cooler Object Name"]

    @first_evaporative_cooler_object_name.setter
    def first_evaporative_cooler_object_name(self, value=None):
        """Corresponds to IDD field `First Evaporative Cooler Object Name`"""
        self["First Evaporative Cooler Object Name"] = value

    @property
    def second_evaporative_cooler_object_type(self):
        """field `Second Evaporative Cooler Object Type`

        |  optional, used for direct/indirect configurations
        |  second cooler must be immediately downstream of first cooler, if present

        Args:
            value (str): value for IDD Field `Second Evaporative Cooler Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `second_evaporative_cooler_object_type` or None if not set

        """
        return self["Second Evaporative Cooler Object Type"]

    @second_evaporative_cooler_object_type.setter
    def second_evaporative_cooler_object_type(self, value=None):
        """Corresponds to IDD field `Second Evaporative Cooler Object Type`"""
        self["Second Evaporative Cooler Object Type"] = value

    @property
    def second_evaporative_cooler_name(self):
        """field `Second Evaporative Cooler Name`

        |  optional, used for direct/indirect configurations

        Args:
            value (str): value for IDD Field `Second Evaporative Cooler Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `second_evaporative_cooler_name` or None if not set

        """
        return self["Second Evaporative Cooler Name"]

    @second_evaporative_cooler_name.setter
    def second_evaporative_cooler_name(self, value=None):
        """Corresponds to IDD field `Second Evaporative Cooler Name`"""
        self["Second Evaporative Cooler Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value




class ZoneHvacOutdoorAirUnit(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:OutdoorAirUnit`
        The zone outdoor air unit models a single-zone dedicated outdoor air system (DOAS).
        Forced-convection 100% outdoor air unit with supply fan and optional equipment
        including exhaust fan, heating coil, cooling coil, and heat recovery.
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
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outdoor air flow rate',
                                       {'name': u'Outdoor Air Flow Rate',
                                        'pyname': u'outdoor_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air schedule name',
                                       {'name': u'Outdoor Air Schedule Name',
                                        'pyname': u'outdoor_air_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply fan name',
                                       {'name': u'Supply Fan Name',
                                        'pyname': u'supply_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply fan placement',
                                       {'name': u'Supply Fan Placement',
                                        'pyname': u'supply_fan_placement',
                                        'default': u'DrawThrough',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'exhaust fan name',
                                       {'name': u'Exhaust Fan Name',
                                        'pyname': u'exhaust_fan_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'exhaust air flow rate',
                                       {'name': u'Exhaust Air Flow Rate',
                                        'pyname': u'exhaust_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'exhaust air schedule name',
                                       {'name': u'Exhaust Air Schedule Name',
                                        'pyname': u'exhaust_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'unit control type',
                                       {'name': u'Unit Control Type',
                                        'pyname': u'unit_control_type',
                                        'default': u'NeutralControl',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'NeutralControl',
                                                            u'TemperatureControl'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'high air control temperature schedule name',
                                       {'name': u'High Air Control Temperature Schedule Name',
                                        'pyname': u'high_air_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'low air control temperature schedule name',
                                       {'name': u'Low Air Control Temperature Schedule Name',
                                        'pyname': u'low_air_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outdoor air node name',
                                       {'name': u'Outdoor Air Node Name',
                                        'pyname': u'outdoor_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'airoutlet node name',
                                       {'name': u'AirOutlet Node Name',
                                        'pyname': u'airoutlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'airinlet node name',
                                       {'name': u'AirInlet Node Name',
                                        'pyname': u'airinlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply fanoutlet node name',
                                       {'name': u'Supply FanOutlet Node Name',
                                        'pyname': u'supply_fanoutlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air unit list name',
                                       {'name': u'Outdoor Air Unit List Name',
                                        'pyname': u'outdoor_air_unit_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 18,
               'name': u'ZoneHVAC:OutdoorAirUnit',
               'pyname': u'ZoneHvacOutdoorAirUnit',
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

        |  (name of zone system is serving)

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
    def outdoor_air_flow_rate(self):
        """field `Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `outdoor_air_flow_rate` or None if not set

        """
        return self["Outdoor Air Flow Rate"]

    @outdoor_air_flow_rate.setter
    def outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow Rate`"""
        self["Outdoor Air Flow Rate"] = value

    @property
    def outdoor_air_schedule_name(self):
        """field `Outdoor Air Schedule Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_schedule_name` or None if not set

        """
        return self["Outdoor Air Schedule Name"]

    @outdoor_air_schedule_name.setter
    def outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Schedule Name`"""
        self["Outdoor Air Schedule Name"] = value

    @property
    def supply_fan_name(self):
        """field `Supply Fan Name`

        |  Allowable fan types are Fan:ConstantVolume and
        |  Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Supply Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_name` or None if not set

        """
        return self["Supply Fan Name"]

    @supply_fan_name.setter
    def supply_fan_name(self, value=None):
        """Corresponds to IDD field `Supply Fan Name`"""
        self["Supply Fan Name"] = value

    @property
    def supply_fan_placement(self):
        """field `Supply Fan Placement`

        |  Default value: DrawThrough

        Args:
            value (str): value for IDD Field `Supply Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_placement` or None if not set

        """
        return self["Supply Fan Placement"]

    @supply_fan_placement.setter
    def supply_fan_placement(self, value="DrawThrough"):
        """Corresponds to IDD field `Supply Fan Placement`"""
        self["Supply Fan Placement"] = value

    @property
    def exhaust_fan_name(self):
        """field `Exhaust Fan Name`

        |  Allowable fan types are Fan:ConstantVolume and
        |  Fan:VariableVolume

        Args:
            value (str): value for IDD Field `Exhaust Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_fan_name` or None if not set

        """
        return self["Exhaust Fan Name"]

    @exhaust_fan_name.setter
    def exhaust_fan_name(self, value=None):
        """Corresponds to IDD field `Exhaust Fan Name`"""
        self["Exhaust Fan Name"] = value

    @property
    def exhaust_air_flow_rate(self):
        """field `Exhaust Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Exhaust Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `exhaust_air_flow_rate` or None if not set

        """
        return self["Exhaust Air Flow Rate"]

    @exhaust_air_flow_rate.setter
    def exhaust_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Exhaust Air Flow Rate`"""
        self["Exhaust Air Flow Rate"] = value

    @property
    def exhaust_air_schedule_name(self):
        """field `Exhaust Air Schedule Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_schedule_name` or None if not set

        """
        return self["Exhaust Air Schedule Name"]

    @exhaust_air_schedule_name.setter
    def exhaust_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Schedule Name`"""
        self["Exhaust Air Schedule Name"] = value

    @property
    def unit_control_type(self):
        """field `Unit Control Type`

        |  Default value: NeutralControl

        Args:
            value (str): value for IDD Field `Unit Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unit_control_type` or None if not set

        """
        return self["Unit Control Type"]

    @unit_control_type.setter
    def unit_control_type(self, value="NeutralControl"):
        """Corresponds to IDD field `Unit Control Type`"""
        self["Unit Control Type"] = value

    @property
    def high_air_control_temperature_schedule_name(self):
        """field `High Air Control Temperature Schedule Name`

        |  Air and control temperatures for cooling. If outdoor air temperature
        |  is above the high air control temperature, then the zone inlet air temperature
        |  is set to the high air control temperature. If the outdoor air is between high and low
        |  air control temperature, then there is no cooling/heating requirements.

        Args:
            value (str): value for IDD Field `High Air Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `high_air_control_temperature_schedule_name` or None if not set

        """
        return self["High Air Control Temperature Schedule Name"]

    @high_air_control_temperature_schedule_name.setter
    def high_air_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `High Air Control Temperature Schedule
        Name`"""
        self["High Air Control Temperature Schedule Name"] = value

    @property
    def low_air_control_temperature_schedule_name(self):
        """field `Low Air Control Temperature Schedule Name`

        |  Air and control temperatures for Heating. If outdoor air temperature
        |  is below the low air control temperature, then the zone inlet air temperature
        |  is set to the low air control temperature. If the outdoor air is between high and low
        |  air control temperature, then there is no cooling/heating requirements.

        Args:
            value (str): value for IDD Field `Low Air Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `low_air_control_temperature_schedule_name` or None if not set

        """
        return self["Low Air Control Temperature Schedule Name"]

    @low_air_control_temperature_schedule_name.setter
    def low_air_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Low Air Control Temperature Schedule
        Name`"""
        self["Low Air Control Temperature Schedule Name"] = value

    @property
    def outdoor_air_node_name(self):
        """field `Outdoor Air Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set

        """
        return self["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Node Name`"""
        self["Outdoor Air Node Name"] = value

    @property
    def airoutlet_node_name(self):
        """field `AirOutlet Node Name`

        Args:
            value (str): value for IDD Field `AirOutlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `airoutlet_node_name` or None if not set

        """
        return self["AirOutlet Node Name"]

    @airoutlet_node_name.setter
    def airoutlet_node_name(self, value=None):
        """Corresponds to IDD field `AirOutlet Node Name`"""
        self["AirOutlet Node Name"] = value

    @property
    def airinlet_node_name(self):
        """field `AirInlet Node Name`

        |  air leaves zone

        Args:
            value (str): value for IDD Field `AirInlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `airinlet_node_name` or None if not set

        """
        return self["AirInlet Node Name"]

    @airinlet_node_name.setter
    def airinlet_node_name(self, value=None):
        """Corresponds to IDD field `AirInlet Node Name`"""
        self["AirInlet Node Name"] = value

    @property
    def supply_fanoutlet_node_name(self):
        """field `Supply FanOutlet Node Name`

        Args:
            value (str): value for IDD Field `Supply FanOutlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fanoutlet_node_name` or None if not set

        """
        return self["Supply FanOutlet Node Name"]

    @supply_fanoutlet_node_name.setter
    def supply_fanoutlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply FanOutlet Node Name`"""
        self["Supply FanOutlet Node Name"] = value

    @property
    def outdoor_air_unit_list_name(self):
        """field `Outdoor Air Unit List Name`

        |  Enter the name of an ZoneHVAC:OutdoorAirUnit:EquipmentList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Unit List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_unit_list_name` or None if not set

        """
        return self["Outdoor Air Unit List Name"]

    @outdoor_air_unit_list_name.setter
    def outdoor_air_unit_list_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Unit List Name`"""
        self["Outdoor Air Unit List Name"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value




class ZoneHvacOutdoorAirUnitEquipmentList(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:OutdoorAirUnit:EquipmentList`
        Equipment list for components in a ZoneHVAC:OutdoorAirUnit. Components are simulated
        sequentially in the order given in the equipment list.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'component 1 object type',
                                       {'name': u'Component 1 Object Type',
                                        'pyname': u'component_1_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 1 name',
                                       {'name': u'Component 1 Name',
                                        'pyname': u'component_1_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 2 object type',
                                       {'name': u'Component 2 Object Type',
                                        'pyname': u'component_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 2 name',
                                       {'name': u'Component 2 Name',
                                        'pyname': u'component_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 3 object type',
                                       {'name': u'Component 3 Object Type',
                                        'pyname': u'component_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 3 name',
                                       {'name': u'Component 3 Name',
                                        'pyname': u'component_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 4 object type',
                                       {'name': u'Component 4 Object Type',
                                        'pyname': u'component_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 4 name',
                                       {'name': u'Component 4 Name',
                                        'pyname': u'component_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 5 object type',
                                       {'name': u'Component 5 Object Type',
                                        'pyname': u'component_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 5 name',
                                       {'name': u'Component 5 Name',
                                        'pyname': u'component_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 6 object type',
                                       {'name': u'Component 6 Object Type',
                                        'pyname': u'component_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 6 name',
                                       {'name': u'Component 6 Name',
                                        'pyname': u'component_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 7 object type',
                                       {'name': u'Component 7 Object Type',
                                        'pyname': u'component_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 7 name',
                                       {'name': u'Component 7 Name',
                                        'pyname': u'component_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 8 object type',
                                       {'name': u'Component 8 Object Type',
                                        'pyname': u'component_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry',
                                                            u'CoilSystem:Cooling:Water:HeatexchangerAssisted',
                                                            u'CoilSystem:Cooling:DX',
                                                            u'CoilSystem:Heating:DX',
                                                            u'HeatExchanger:AirToAir:FlatPlate',
                                                            u'HeatExchanger:AirToAir:SensibleAndLatent',
                                                            u'Dehumidifier:Desiccant:NoFans'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 8 name',
                                       {'name': u'Component 8 Name',
                                        'pyname': u'component_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 0,
               'name': u'ZoneHVAC:OutdoorAirUnit:EquipmentList',
               'pyname': u'ZoneHvacOutdoorAirUnitEquipmentList',
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
    def component_1_object_type(self):
        """field `Component 1 Object Type`

        Args:
            value (str): value for IDD Field `Component 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_object_type` or None if not set

        """
        return self["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """Corresponds to IDD field `Component 1 Object Type`"""
        self["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """field `Component 1 Name`

        Args:
            value (str): value for IDD Field `Component 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_name` or None if not set

        """
        return self["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """Corresponds to IDD field `Component 1 Name`"""
        self["Component 1 Name"] = value

    @property
    def component_2_object_type(self):
        """field `Component 2 Object Type`

        Args:
            value (str): value for IDD Field `Component 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_object_type` or None if not set

        """
        return self["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """Corresponds to IDD field `Component 2 Object Type`"""
        self["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """field `Component 2 Name`

        Args:
            value (str): value for IDD Field `Component 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_name` or None if not set

        """
        return self["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """Corresponds to IDD field `Component 2 Name`"""
        self["Component 2 Name"] = value

    @property
    def component_3_object_type(self):
        """field `Component 3 Object Type`

        Args:
            value (str): value for IDD Field `Component 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_object_type` or None if not set

        """
        return self["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """Corresponds to IDD field `Component 3 Object Type`"""
        self["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """field `Component 3 Name`

        Args:
            value (str): value for IDD Field `Component 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_name` or None if not set

        """
        return self["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """Corresponds to IDD field `Component 3 Name`"""
        self["Component 3 Name"] = value

    @property
    def component_4_object_type(self):
        """field `Component 4 Object Type`

        Args:
            value (str): value for IDD Field `Component 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_object_type` or None if not set

        """
        return self["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """Corresponds to IDD field `Component 4 Object Type`"""
        self["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """field `Component 4 Name`

        Args:
            value (str): value for IDD Field `Component 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_name` or None if not set

        """
        return self["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """Corresponds to IDD field `Component 4 Name`"""
        self["Component 4 Name"] = value

    @property
    def component_5_object_type(self):
        """field `Component 5 Object Type`

        Args:
            value (str): value for IDD Field `Component 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_object_type` or None if not set

        """
        return self["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """Corresponds to IDD field `Component 5 Object Type`"""
        self["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """field `Component 5 Name`

        Args:
            value (str): value for IDD Field `Component 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_name` or None if not set

        """
        return self["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """Corresponds to IDD field `Component 5 Name`"""
        self["Component 5 Name"] = value

    @property
    def component_6_object_type(self):
        """field `Component 6 Object Type`

        Args:
            value (str): value for IDD Field `Component 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_object_type` or None if not set

        """
        return self["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """Corresponds to IDD field `Component 6 Object Type`"""
        self["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """field `Component 6 Name`

        Args:
            value (str): value for IDD Field `Component 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_name` or None if not set

        """
        return self["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """Corresponds to IDD field `Component 6 Name`"""
        self["Component 6 Name"] = value

    @property
    def component_7_object_type(self):
        """field `Component 7 Object Type`

        Args:
            value (str): value for IDD Field `Component 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_object_type` or None if not set

        """
        return self["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """Corresponds to IDD field `Component 7 Object Type`"""
        self["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """field `Component 7 Name`

        Args:
            value (str): value for IDD Field `Component 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_name` or None if not set

        """
        return self["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """Corresponds to IDD field `Component 7 Name`"""
        self["Component 7 Name"] = value

    @property
    def component_8_object_type(self):
        """field `Component 8 Object Type`

        Args:
            value (str): value for IDD Field `Component 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_object_type` or None if not set

        """
        return self["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """Corresponds to IDD field `Component 8 Object Type`"""
        self["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """field `Component 8 Name`

        Args:
            value (str): value for IDD Field `Component 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_name` or None if not set

        """
        return self["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """Corresponds to IDD field `Component 8 Name`"""
        self["Component 8 Name"] = value




class ZoneHvacTerminalUnitVariableRefrigerantFlow(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:TerminalUnit:VariableRefrigerantFlow`
        Zone terminal unit with variable refrigerant flow (VRF) DX cooling and heating coils
        (air-to-air heat pump). The VRF terminal units are served by an
        AirConditioner:VariableRefrigerantFlow system.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'zone terminal unit name',
                                       {'name': u'Zone Terminal Unit Name',
                                        'pyname': u'zone_terminal_unit_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'terminal unit availability schedule',
                                       {'name': u'Terminal Unit Availability Schedule',
                                        'pyname': u'terminal_unit_availability_schedule',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'terminal unit air inlet node name',
                                       {'name': u'Terminal Unit Air Inlet Node Name',
                                        'pyname': u'terminal_unit_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'terminal unit air outlet node name',
                                       {'name': u'Terminal Unit Air Outlet Node Name',
                                        'pyname': u'terminal_unit_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cooling supply air flow rate',
                                       {'name': u'Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no cooling supply air flow rate',
                                       {'name': u'No Cooling Supply Air Flow Rate',
                                        'pyname': u'no_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating supply air flow rate',
                                       {'name': u'Heating Supply Air Flow Rate',
                                        'pyname': u'heating_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no heating supply air flow rate',
                                       {'name': u'No Heating Supply Air Flow Rate',
                                        'pyname': u'no_heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling outdoor air flow rate',
                                       {'name': u'Cooling Outdoor Air Flow Rate',
                                        'pyname': u'cooling_outdoor_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating outdoor air flow rate',
                                       {'name': u'Heating Outdoor Air Flow Rate',
                                        'pyname': u'heating_outdoor_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load outdoor air flow rate',
                                       {'name': u'No Load Outdoor Air Flow Rate',
                                        'pyname': u'no_load_outdoor_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air fan placement',
                                       {'name': u'Supply Air Fan Placement',
                                        'pyname': u'supply_air_fan_placement',
                                        'default': u'BlowThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan object type',
                                       {'name': u'Supply Air Fan Object Type',
                                        'pyname': u'supply_air_fan_object_type',
                                        'default': u'Fan:ConstantVolume',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume',
                                                            u'Fan:VariableVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air fan object name',
                                       {'name': u'Supply Air Fan Object Name',
                                        'pyname': u'supply_air_fan_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outside air mixer object type',
                                       {'name': u'Outside Air Mixer Object Type',
                                        'pyname': u'outside_air_mixer_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'OutdoorAir:Mixer'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outside air mixer object name',
                                       {'name': u'Outside Air Mixer Object Name',
                                        'pyname': u'outside_air_mixer_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:VariableRefrigerantFlow',
                                                            u'Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil object name',
                                       {'name': u'Cooling Coil Object Name',
                                        'pyname': u'cooling_coil_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:DX:VariableRefrigerantFlow',
                                                            u'Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil object name',
                                       {'name': u'Heating Coil Object Name',
                                        'pyname': u'heating_coil_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone terminal unit on parasitic electric energy use',
                                       {'name': u'Zone Terminal Unit On Parasitic Electric Energy Use',
                                        'pyname': u'zone_terminal_unit_on_parasitic_electric_energy_use',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'zone terminal unit off parasitic electric energy use',
                                       {'name': u'Zone Terminal Unit Off Parasitic Electric Energy Use',
                                        'pyname': u'zone_terminal_unit_off_parasitic_electric_energy_use',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated heating capacity sizing ratio',
                                       {'name': u'Rated Heating Capacity Sizing Ratio',
                                        'pyname': u'rated_heating_capacity_sizing_ratio',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification zonehvac sizing object name',
                                       {'name': u'Design Specification ZoneHVAC Sizing Object Name',
                                        'pyname': u'design_specification_zonehvac_sizing_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Forced Air Units',
               'min-fields': 19,
               'name': u'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
               'pyname': u'ZoneHvacTerminalUnitVariableRefrigerantFlow',
               'required-object': False,
               'unique-object': False}

    @property
    def zone_terminal_unit_name(self):
        """field `Zone Terminal Unit Name`

        Args:
            value (str): value for IDD Field `Zone Terminal Unit Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_terminal_unit_name` or None if not set

        """
        return self["Zone Terminal Unit Name"]

    @zone_terminal_unit_name.setter
    def zone_terminal_unit_name(self, value=None):
        """Corresponds to IDD field `Zone Terminal Unit Name`"""
        self["Zone Terminal Unit Name"] = value

    @property
    def terminal_unit_availability_schedule(self):
        """field `Terminal Unit Availability Schedule`

        |  The unit is available the entire simulation if this field is left blank
        |  Schedule values of 0 denote the unit is off.

        Args:
            value (str): value for IDD Field `Terminal Unit Availability Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_availability_schedule` or None if not set

        """
        return self["Terminal Unit Availability Schedule"]

    @terminal_unit_availability_schedule.setter
    def terminal_unit_availability_schedule(self, value=None):
        """Corresponds to IDD field `Terminal Unit Availability Schedule`"""
        self["Terminal Unit Availability Schedule"] = value

    @property
    def terminal_unit_air_inlet_node_name(self):
        """field `Terminal Unit Air Inlet Node Name`

        |  the inlet node to the terminal unit

        Args:
            value (str): value for IDD Field `Terminal Unit Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_air_inlet_node_name` or None if not set

        """
        return self["Terminal Unit Air Inlet Node Name"]

    @terminal_unit_air_inlet_node_name.setter
    def terminal_unit_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Air Inlet Node Name`"""
        self["Terminal Unit Air Inlet Node Name"] = value

    @property
    def terminal_unit_air_outlet_node_name(self):
        """field `Terminal Unit Air Outlet Node Name`

        |  the outlet node of the terminal unit

        Args:
            value (str): value for IDD Field `Terminal Unit Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_air_outlet_node_name` or None if not set

        """
        return self["Terminal Unit Air Outlet Node Name"]

    @terminal_unit_air_outlet_node_name.setter
    def terminal_unit_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Air Outlet Node Name`"""
        self["Terminal Unit Air Outlet Node Name"] = value

    @property
    def cooling_supply_air_flow_rate(self):
        """field `Cooling Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Supply Air Flow Rate"]

    @cooling_supply_air_flow_rate.setter
    def cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate`"""
        self["Cooling Supply Air Flow Rate"] = value

    @property
    def no_cooling_supply_air_flow_rate(self):
        """field `No Cooling Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_cooling_supply_air_flow_rate` or None if not set

        """
        return self["No Cooling Supply Air Flow Rate"]

    @no_cooling_supply_air_flow_rate.setter
    def no_cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Cooling Supply Air Flow Rate`"""
        self["No Cooling Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate(self):
        """field `Heating Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Supply Air Flow Rate"]

    @heating_supply_air_flow_rate.setter
    def heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate`"""
        self["Heating Supply Air Flow Rate"] = value

    @property
    def no_heating_supply_air_flow_rate(self):
        """field `No Heating Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_heating_supply_air_flow_rate` or None if not set

        """
        return self["No Heating Supply Air Flow Rate"]

    @no_heating_supply_air_flow_rate.setter
    def no_heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Heating Supply Air Flow Rate`"""
        self["No Heating Supply Air Flow Rate"] = value

    @property
    def cooling_outdoor_air_flow_rate(self):
        """field `Cooling Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_outdoor_air_flow_rate` or None if not set

        """
        return self["Cooling Outdoor Air Flow Rate"]

    @cooling_outdoor_air_flow_rate.setter
    def cooling_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Outdoor Air Flow Rate`"""
        self["Cooling Outdoor Air Flow Rate"] = value

    @property
    def heating_outdoor_air_flow_rate(self):
        """field `Heating Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_outdoor_air_flow_rate` or None if not set

        """
        return self["Heating Outdoor Air Flow Rate"]

    @heating_outdoor_air_flow_rate.setter
    def heating_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Outdoor Air Flow Rate`"""
        self["Heating Outdoor Air Flow Rate"] = value

    @property
    def no_load_outdoor_air_flow_rate(self):
        """field `No Load Outdoor Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_outdoor_air_flow_rate` or None if not set

        """
        return self["No Load Outdoor Air Flow Rate"]

    @no_load_outdoor_air_flow_rate.setter
    def no_load_outdoor_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Outdoor Air Flow Rate`"""
        self["No Load Outdoor Air Flow Rate"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Operating Mode Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_operating_mode_schedule_name` or None if not set

        """
        return self["Supply Air Fan Operating Mode Schedule Name"]

    @supply_air_fan_operating_mode_schedule_name.setter
    def supply_air_fan_operating_mode_schedule_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Operating Mode Schedule
        Name`"""
        self["Supply Air Fan Operating Mode Schedule Name"] = value

    @property
    def supply_air_fan_placement(self):
        """field `Supply Air Fan Placement`

        |  Select fan placement as either blow through or draw through.
        |  Default value: BlowThrough

        Args:
            value (str): value for IDD Field `Supply Air Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_placement` or None if not set

        """
        return self["Supply Air Fan Placement"]

    @supply_air_fan_placement.setter
    def supply_air_fan_placement(self, value="BlowThrough"):
        """Corresponds to IDD field `Supply Air Fan Placement`"""
        self["Supply Air Fan Placement"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`

        |  Supply Air Fan Object Type must be
        |  Fan:OnOff or Fan:ConstantVolume
        |  if AirConditioner:VariableRefrigerantFlow
        |  is used to model VRF outdoor unit
        |  Supply Air Fan Object Type must be Fan:VariableVolume if
        |  AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl
        |  is used to model VRF outdoor unit
        |  Default value: Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_type` or None if not set

        """
        return self["Supply Air Fan Object Type"]

    @supply_air_fan_object_type.setter
    def supply_air_fan_object_type(self, value="Fan:ConstantVolume"):
        """Corresponds to IDD field `Supply Air Fan Object Type`"""
        self["Supply Air Fan Object Type"] = value

    @property
    def supply_air_fan_object_name(self):
        """field `Supply Air Fan Object Name`

        Args:
            value (str): value for IDD Field `Supply Air Fan Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_object_name` or None if not set

        """
        return self["Supply Air Fan Object Name"]

    @supply_air_fan_object_name.setter
    def supply_air_fan_object_name(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Object Name`"""
        self["Supply Air Fan Object Name"] = value

    @property
    def outside_air_mixer_object_type(self):
        """field `Outside Air Mixer Object Type`

        |  If this field is blank, and outside air mixer is not used.

        Args:
            value (str): value for IDD Field `Outside Air Mixer Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_air_mixer_object_type` or None if not set

        """
        return self["Outside Air Mixer Object Type"]

    @outside_air_mixer_object_type.setter
    def outside_air_mixer_object_type(self, value=None):
        """Corresponds to IDD field `Outside Air Mixer Object Type`"""
        self["Outside Air Mixer Object Type"] = value

    @property
    def outside_air_mixer_object_name(self):
        """field `Outside Air Mixer Object Name`

        |  If this field is blank, and outside air mixer is not used.

        Args:
            value (str): value for IDD Field `Outside Air Mixer Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outside_air_mixer_object_name` or None if not set

        """
        return self["Outside Air Mixer Object Name"]

    @outside_air_mixer_object_name.setter
    def outside_air_mixer_object_name(self, value=None):
        """Corresponds to IDD field `Outside Air Mixer Object Name`"""
        self["Outside Air Mixer Object Name"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        |  Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow
        |  if AirConditioner:VariableRefrigerantFlow is used
        |  to model VRF outdoor unit
        |  Cooling Coil Type must be
        |  Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl
        |  if AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl
        |  is used to model VRF outdoor unit
        |  This field may be left blank if heating-only mode is used

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_object_name(self):
        """field `Cooling Coil Object Name`

        |  Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow
        |  This field may be left blank if heating-only mode is used

        Args:
            value (str): value for IDD Field `Cooling Coil Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_name` or None if not set

        """
        return self["Cooling Coil Object Name"]

    @cooling_coil_object_name.setter
    def cooling_coil_object_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Name`"""
        self["Cooling Coil Object Name"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        |  Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow
        |  if AirConditioner:VariableRefrigerantFlow is used
        |  to model VRF outdoor unit
        |  Heating Coil Type must be
        |  Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl
        |  if AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl
        |  is used to model VRF outdoor unit
        |  This field may be left blank if cooling-only mode is used

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_object_name(self):
        """field `Heating Coil Object Name`

        |  Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow
        |  This field may be left blank if cooling-only mode is used

        Args:
            value (str): value for IDD Field `Heating Coil Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_name` or None if not set

        """
        return self["Heating Coil Object Name"]

    @heating_coil_object_name.setter
    def heating_coil_object_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Name`"""
        self["Heating Coil Object Name"] = value

    @property
    def zone_terminal_unit_on_parasitic_electric_energy_use(self):
        """field `Zone Terminal Unit On Parasitic Electric Energy Use`

        |  Units: W

        Args:
            value (float): value for IDD Field `Zone Terminal Unit On Parasitic Electric Energy Use`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_terminal_unit_on_parasitic_electric_energy_use` or None if not set

        """
        return self["Zone Terminal Unit On Parasitic Electric Energy Use"]

    @zone_terminal_unit_on_parasitic_electric_energy_use.setter
    def zone_terminal_unit_on_parasitic_electric_energy_use(self, value=None):
        """Corresponds to IDD field `Zone Terminal Unit On Parasitic Electric
        Energy Use`"""
        self["Zone Terminal Unit On Parasitic Electric Energy Use"] = value

    @property
    def zone_terminal_unit_off_parasitic_electric_energy_use(self):
        """field `Zone Terminal Unit Off Parasitic Electric Energy Use`

        |  Units: W

        Args:
            value (float): value for IDD Field `Zone Terminal Unit Off Parasitic Electric Energy Use`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_terminal_unit_off_parasitic_electric_energy_use` or None if not set

        """
        return self["Zone Terminal Unit Off Parasitic Electric Energy Use"]

    @zone_terminal_unit_off_parasitic_electric_energy_use.setter
    def zone_terminal_unit_off_parasitic_electric_energy_use(self, value=None):
        """Corresponds to IDD field `Zone Terminal Unit Off Parasitic Electric
        Energy Use`"""
        self["Zone Terminal Unit Off Parasitic Electric Energy Use"] = value

    @property
    def rated_heating_capacity_sizing_ratio(self):
        """field `Rated Heating Capacity Sizing Ratio`

        |  If this terminal unit's heating coil is autosized, the heating capacity is sized
        |  to be equal to the cooling capacity multiplied by this sizing ratio.
        |  This input applies to the terminal unit heating coil and overrides the sizing
        |  ratio entered in the AirConditioner:VariableRefrigerantFlow object.
        |  Units: W/W
        |  Default value: 1.0
        |  value >= 1.0

        Args:
            value (float): value for IDD Field `Rated Heating Capacity Sizing Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_heating_capacity_sizing_ratio` or None if not set

        """
        return self["Rated Heating Capacity Sizing Ratio"]

    @rated_heating_capacity_sizing_ratio.setter
    def rated_heating_capacity_sizing_ratio(self, value=1.0):
        """Corresponds to IDD field `Rated Heating Capacity Sizing Ratio`"""
        self["Rated Heating Capacity Sizing Ratio"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """field `Design Specification ZoneHVAC Sizing Object Name`

        |  Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set

        """
        return self["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification ZoneHVAC Sizing
        Object Name`"""
        self["Design Specification ZoneHVAC Sizing Object Name"] = value


