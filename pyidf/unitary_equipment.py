""" Data objects in group "Unitary Equipment"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class AirLoopHvacUnitarySystem(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitarySystem`
        AirloopHVAC:UnitarySystem is a generic HVAC system type that allows any
        configuration of coils and/or fan. This object is a replacement of other
        AirloopHVAC objects. This object can be used in outdoor air systems,
        outdoor air units, air loops, and as zone equipment if desired.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'default': u'Load',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Load',
                                                            u'SetPoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Multimode',
                                                            u'CoolReheat'],
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
                                      (u'supply fan object type',
                                       {'name': u'Supply Fan Object Type',
                                        'pyname': u'supply_fan_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume',
                                                            u'Fan:VariableVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply fan name',
                                       {'name': u'Supply Fan Name',
                                        'pyname': u'supply_fan_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
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
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:DX:SingleSpeed',
                                                            u'Coil:Heating:DX:MultiSpeed',
                                                            u'Coil:Heating:DX:VariableSpeed',
                                                            u'Coil:Heating:WaterToAirHeatPump:ParameterEstimation',
                                                            u'Coil:Heating:WaterToAirHeatPump:EquationFit',
                                                            u'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Gas:MultiStage',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Electric:MultiStage',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam',
                                                            u'Coil:Heating:Desuperheater'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dx heating coil sizing ratio',
                                       {'name': u'DX Heating Coil Sizing Ratio',
                                        'pyname': u'dx_heating_coil_sizing_ratio',
                                        'default': 1.0,
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
                                        'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                            u'Coil:Cooling:DX:TwoSpeed',
                                                            u'Coil:Cooling:DX:MultiSpeed',
                                                            u'Coil:Cooling:DX:VariableSpeed',
                                                            u'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
                                                            u'CoilSystem:Cooling:DX:HeatExchangerAssisted',
                                                            u'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation',
                                                            u'Coil:Cooling:WaterToAirHeatPump:EquationFit',
                                                            u'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
                                                            u'Coil:Cooling:Water',
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
                                      (u'use doas dx cooling coil',
                                       {'name': u'Use DOAS DX Cooling Coil',
                                        'pyname': u'use_doas_dx_cooling_coil',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'doas dx cooling coil leaving minimum air temperature',
                                       {'name': u'DOAS DX Cooling Coil Leaving Minimum Air Temperature',
                                        'pyname': u'doas_dx_cooling_coil_leaving_minimum_air_temperature',
                                        'default': 2.0,
                                        'maximum': 7.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'latent load control',
                                       {'name': u'Latent Load Control',
                                        'pyname': u'latent_load_control',
                                        'default': u'SensibleOnlyLoadControl',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SensibleOnlyLoadControl',
                                                            u'LatentOnlyLoadControl',
                                                            u'LatentWithSensibleLoadControl',
                                                            u'LatentOrSensibleLoadControl'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supplemental heating coil object type',
                                       {'name': u'Supplemental Heating Coil Object Type',
                                        'pyname': u'supplemental_heating_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Desuperheater',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supplemental heating coil name',
                                       {'name': u'Supplemental Heating Coil Name',
                                        'pyname': u'supplemental_heating_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air flow rate method during cooling operation',
                                       {'name': u'Supply Air Flow Rate Method During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_method_during_cooling_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'SupplyAirFlowRate',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedCoolingValue',
                                                            u'FlowPerCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air flow rate during cooling operation',
                                       {'name': u'Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_during_cooling_operation',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate per floor area during cooling operation',
                                       {'name': u'Supply Air Flow Rate Per Floor Area During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_per_floor_area_during_cooling_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of autosized design cooling supply air flow rate',
                                       {'name': u'Fraction of Autosized Design Cooling Supply Air Flow Rate',
                                        'pyname': u'fraction_of_autosized_design_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'design supply air flow rate per unit of capacity during cooling operation',
                                       {'name': u'Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation',
                                        'pyname': u'design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'supply air flow rate method during heating operation',
                                       {'name': u'Supply air Flow Rate Method During Heating Operation',
                                        'pyname': u'supply_air_flow_rate_method_during_heating_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'SupplyAirFlowRate',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedHeatingValue',
                                                            u'FlowPerHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air flow rate during heating operation',
                                       {'name': u'Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'supply_air_flow_rate_during_heating_operation',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate per floor area during heating operation',
                                       {'name': u'Supply Air Flow Rate Per Floor Area during Heating Operation',
                                        'pyname': u'supply_air_flow_rate_per_floor_area_during_heating_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of autosized design heating supply air flow rate',
                                       {'name': u'Fraction of Autosized Design Heating Supply Air Flow Rate',
                                        'pyname': u'fraction_of_autosized_design_heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'design supply air flow rate per unit of capacity during heating operation',
                                       {'name': u'Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation',
                                        'pyname': u'design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'supply air flow rate method when no cooling or heating is required',
                                       {'name': u'Supply Air Flow Rate Method When No Cooling or Heating is Required',
                                        'pyname': u'supply_air_flow_rate_method_when_no_cooling_or_heating_is_required',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'SupplyAirFlowRate',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedCoolingValue',
                                                            u'FractionOfAutosizedHeatingValue',
                                                            u'FlowPerCoolingCapacity',
                                                            u'FlowPerHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air flow rate when no cooling or heating is required',
                                       {'name': u'Supply Air Flow Rate When No Cooling or Heating is Required',
                                        'pyname': u'supply_air_flow_rate_when_no_cooling_or_heating_is_required',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate per floor area when no cooling or heating is required',
                                       {'name': u'Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required',
                                        'pyname': u'supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      ('fraction of autosized design cooling supply air flow rate v3',
                                       {'name': 'Fraction of Autosized Design Cooling Supply Air Flow Rate v3',
                                        'pyname': 'fraction_of_autosized_design_cooling_supply_air_flow_rate_v3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      ('fraction of autosized design heating supply air flow rate v3',
                                       {'name': 'Fraction of Autosized Design Heating Supply Air Flow Rate v3',
                                        'pyname': 'fraction_of_autosized_design_heating_supply_air_flow_rate_v3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      ('design supply air flow rate per unit of capacity during cooling operation v3',
                                       {'name': 'Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v3',
                                        'pyname': 'design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      ('design supply air flow rate per unit of capacity during heating operation v3',
                                       {'name': 'Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v3',
                                        'pyname': 'design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 80.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor dry-bulb temperature for supplemental heater operation',
                                       {'name': u'Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation',
                                        'default': 21.0,
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
                                        'type': u'real'}),
                                      (u'heat pump fan delay time',
                                       {'name': u'Heat Pump Fan Delay Time',
                                        'pyname': u'heat_pump_fan_delay_time',
                                        'default': 60.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u's'}),
                                      (u'ancilliary on-cycle electric power',
                                       {'name': u'Ancilliary On-Cycle Electric Power',
                                        'pyname': u'ancilliary_oncycle_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'ancilliary off-cycle electric power',
                                       {'name': u'Ancilliary Off-Cycle Electric Power',
                                        'pyname': u'ancilliary_offcycle_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'design heat recovery water flow rate',
                                       {'name': u'Design Heat Recovery Water Flow Rate',
                                        'pyname': u'design_heat_recovery_water_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum temperature for heat recovery',
                                       {'name': u'Maximum Temperature for Heat Recovery',
                                        'pyname': u'maximum_temperature_for_heat_recovery',
                                        'default': 80.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'heat recovery water inlet node name',
                                       {'name': u'Heat Recovery Water Inlet Node Name',
                                        'pyname': u'heat_recovery_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heat recovery water outlet node name',
                                       {'name': u'Heat Recovery Water Outlet Node Name',
                                        'pyname': u'heat_recovery_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'design specification multispeed heat pump object type',
                                       {'name': u'Design Specification Multispeed Heat Pump Object Type',
                                        'pyname': u'design_specification_multispeed_heat_pump_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'UnitarySystemPerformance:HeatPump:Multispeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design specification multispeed heat pump object name',
                                       {'name': u'Design Specification Multispeed Heat Pump Object Name',
                                        'pyname': u'design_specification_multispeed_heat_pump_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 14,
               'name': u'AirLoopHVAC:UnitarySystem',
               'pyname': u'AirLoopHvacUnitarySystem',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name` Unique name for the Unitary System.

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
    def control_type(self):
        """field `Control Type` Load control requires a Controlling Zone name.
        SetPoint control requires set points at coil outlet node.

        Args:
            value (str): value for IDD Field `Control Type`
                Default value: Load

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value="Load"):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`
        Used only for Load based control
        Zone name where thermostat is located. Required when Control Type = Load.

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set
        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`
        None = meet sensible load only
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available. A schedule value
        greater than zero (usually 1 is used) indicates that the unit is
        available to operate as needed. A value less than or equal to zero
        (usually zero is used) denotes that the unit must be off.

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
        """field `Air Inlet Node Name` Enter the node name used as the inlet
        air node for the unitary system.

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
        """field `Air Outlet Node Name` Enter the node name used as the outlet
        air node for the unitary system.

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
    def supply_fan_object_type(self):
        """field `Supply Fan Object Type`
        Enter the type of supply air fan if included in the unitary system.
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply
        air fan operating mode schedule values greater than 0).
        Specify a Fan:OnOff object when the Supply Air Fan Operating Mode Schedule Name
        input field above is left blank.
        Specifiy a Fan:VariableVolume when modeling VAV systems which used setpoint based control
        if the fan is included in the unitary system object.
        The variable or constant volume fan may be specified on the branch instead of contained
        within the unitary system object (i.e., this field may be blank for certain configurations).

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Fan Object Type`"""
        self["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """field `Supply Fan Name` Enter the name of the supply air fan if
        included in the unitary system.

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
    def fan_placement(self):
        """field `Fan Placement` Enter the type of supply air fan if included
        in the unitary system.

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
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation). Provide a schedule
        with non-zero values when high humidity control is specified.
        Leaving this schedule name blank will default to constant fan mode for the
        entire simulation period.
        This field is not used when set point based control is used where a set point
        controls the coil (i.e., model assumes constant fan mode operation).

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
        """field `Heating Coil Object Type` Enter the type of heating coil if
        included in the unitary system.

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
        """field `Heating Coil Name` Enter the name of the heating coil if
        included in the unitary system.

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
    def dx_heating_coil_sizing_ratio(self):
        """field `DX Heating Coil Sizing Ratio` Used to adjust heat pump
        heating capacity with respect to DX cooling capacity used only for heat
        pump configurations (i.e., a cooling and DX heating coil is used).

        Args:
            value (float): value for IDD Field `DX Heating Coil Sizing Ratio`
                Default value: 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dx_heating_coil_sizing_ratio` or None if not set

        """
        return self["DX Heating Coil Sizing Ratio"]

    @dx_heating_coil_sizing_ratio.setter
    def dx_heating_coil_sizing_ratio(self, value=1.0):
        """Corresponds to IDD field `DX Heating Coil Sizing Ratio`"""
        self["DX Heating Coil Sizing Ratio"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type` Enter the type of cooling coil if
        included in the unitary system.

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
        """field `Cooling Coil Name` Enter the name of the cooling coil if
        included in the unitary system.

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
    def use_doas_dx_cooling_coil(self):
        """field `Use DOAS DX Cooling Coil` If Yes, the DX cooling coil runs as
        100% DOAS DX coil. If No, the DX cooling coil runs as a regular DX
        coil. If left blank the default is regular dx coil.

        Args:
            value (str): value for IDD Field `Use DOAS DX Cooling Coil`
                Default value: No

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_doas_dx_cooling_coil` or None if not set

        """
        return self["Use DOAS DX Cooling Coil"]

    @use_doas_dx_cooling_coil.setter
    def use_doas_dx_cooling_coil(self, value="No"):
        """Corresponds to IDD field `Use DOAS DX Cooling Coil`"""
        self["Use DOAS DX Cooling Coil"] = value

    @property
    def doas_dx_cooling_coil_leaving_minimum_air_temperature(self):
        """field `DOAS DX Cooling Coil Leaving Minimum Air Temperature` DX
        cooling coil leaving minimum air temperature defines the minimum DOAS
        DX cooling coil leaving air temperature that should be maintained to
        avoid frost formation. This input field is optional and only used along
        with the input field above.

        Args:
            value (float): value for IDD Field `DOAS DX Cooling Coil Leaving Minimum Air Temperature`
                Units: C
                Default value: 2.0
                value <= 7.2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `doas_dx_cooling_coil_leaving_minimum_air_temperature` or None if not set

        """
        return self["DOAS DX Cooling Coil Leaving Minimum Air Temperature"]

    @doas_dx_cooling_coil_leaving_minimum_air_temperature.setter
    def doas_dx_cooling_coil_leaving_minimum_air_temperature(self, value=2.0):
        """Corresponds to IDD field `DOAS DX Cooling Coil Leaving Minimum Air
        Temperature`"""
        self["DOAS DX Cooling Coil Leaving Minimum Air Temperature"] = value

    @property
    def latent_load_control(self):
        """field `Latent Load Control` SensibleOnlyLoadControl is selected when
        thermostat control is used. LatentOnlyLoadControl is selected when
        humidistat control is used. LatentWithSensibleLoadControl is selected
        when thermostat control is used and dehumidification is required only
        when a sensible load exists. LatentOrSensibleLoadControl is selected
        when thermostat control is used and dehumidification is required any
        time the humidistat set point is exceeded.

        Args:
            value (str): value for IDD Field `Latent Load Control`
                Default value: SensibleOnlyLoadControl

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `latent_load_control` or None if not set

        """
        return self["Latent Load Control"]

    @latent_load_control.setter
    def latent_load_control(self, value="SensibleOnlyLoadControl"):
        """Corresponds to IDD field `Latent Load Control`"""
        self["Latent Load Control"] = value

    @property
    def supplemental_heating_coil_object_type(self):
        """field `Supplemental Heating Coil Object Type` Enter the type of
        supplemental heating coil if included in the unitary system. Only
        required if dehumidification control type is "CoolReheat".

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
        """field `Supplemental Heating Coil Name` Enter the name of the
        supplemental heating coil if included in the unitary system. Only
        required if dehumidification control type is "CoolReheat".

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
    def supply_air_flow_rate_method_during_cooling_operation(self):
        """field `Supply Air Flow Rate Method During Cooling Operation` Enter
        the method used to determine the cooling supply air volume flow rate.
        None is used when a cooling coil is not included in the unitary system
        or this field may be blank. SupplyAirFlowRate is selected when the
        magnitude of the supply air volume is used. FlowPerFloorArea is
        selected when the supply air volume flow rate is based on total floor
        area served by the unitary system. FractionOfAutosizedCoolingValue is
        selected when the supply air volume is a fraction of the value
        determined by the simulation. FlowPerCoolingCapacity is selected when
        the supply air volume is a fraction of the cooling capacity as
        determined by the simulation.

        Args:
            value (str): value for IDD Field `Supply Air Flow Rate Method During Cooling Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_flow_rate_method_during_cooling_operation` or None if not set

        """
        return self["Supply Air Flow Rate Method During Cooling Operation"]

    @supply_air_flow_rate_method_during_cooling_operation.setter
    def supply_air_flow_rate_method_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Method During Cooling
        Operation`"""
        self["Supply Air Flow Rate Method During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """field `Supply Air Flow Rate During Cooling Operation` Enter the
        magnitude of the supply air volume flow rate during cooling operation.
        Required field when Supply air Flow Rate Method During Cooling
        Operation is SupplyAirFlowRate. This field may be blank if a cooling
        coil is not included in the unitary system.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Cooling
        Operation`"""
        self["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self):
        """field `Supply Air Flow Rate Per Floor Area During Cooling Operation`
        Enter the supply air volume flow rate per total floor area fraction.
        Required field when Supply air Flow Rate Method During Cooling
        Operation is FlowPerFloorArea. This field may be blank if a cooling
        coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area During Cooling Operation`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_cooling_operation` or None if not set

        """
        return self[
            "Supply Air Flow Rate Per Floor Area During Cooling Operation"]

    @supply_air_flow_rate_per_floor_area_during_cooling_operation.setter
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Per Floor Area During
        Cooling Operation`"""
        self[
            "Supply Air Flow Rate Per Floor Area During Cooling Operation"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self):
        """field `Fraction of Autosized Design Cooling Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the cooling
        supply air flow rate. Required field when Supply air Flow Rate Method
        During Cooling Operation is FractionOfAutosizedCoolingValue. This field
        may be blank if a cooling coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate` or None if not set

        """
        return self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Cooling
        Supply Air Flow Rate`"""
        self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation(
            self):
        """field `Design Supply Air Flow Rate Per Unit of Capacity During
        Cooling Operation` Enter the supply air volume flow rate as a fraction
        of the cooling capacity. Required field when Supply air Flow Rate
        Method During Cooling Operation is FlowPerCoolingCapacity. This field
        may be blank if a cooling coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation` or None if not set

        """
        return self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate Per Unit of
        Capacity During Cooling Operation`"""
        self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_method_during_heating_operation(self):
        """field `Supply air Flow Rate Method During Heating Operation` Enter
        the method used to determine the heating supply air volume flow rate.
        None is used when a heating coil is not included in the unitary system
        or this field may be blank. SupplyAirFlowRate is selected when the
        magnitude of the supply air volume is used. FlowPerFloorArea is
        selected when the supply air volume flow rate is based on total floor
        area served by the unitary system. FractionOfAutosizedHeatingValue is
        selected when the supply air volume is a fraction of the value
        determined by the simulation. FlowPerHeatingCapacity is selected when
        the supply air volume is a fraction of the heating capacity as
        determined by the simulation.

        Args:
            value (str): value for IDD Field `Supply air Flow Rate Method During Heating Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_flow_rate_method_during_heating_operation` or None if not set

        """
        return self["Supply air Flow Rate Method During Heating Operation"]

    @supply_air_flow_rate_method_during_heating_operation.setter
    def supply_air_flow_rate_method_during_heating_operation(self, value=None):
        """Corresponds to IDD field `Supply air Flow Rate Method During Heating
        Operation`"""
        self["Supply air Flow Rate Method During Heating Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """field `Supply Air Flow Rate During Heating Operation` Enter the
        magnitude of the supply air volume flow rate during heating operation.
        Required field when Supply air Flow Rate Method During Heating
        Operation is SupplyAirFlowRate. This field may be blank if a heating
        coil is not included in the unitary system.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Heating
        Operation`"""
        self["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self):
        """field `Supply Air Flow Rate Per Floor Area during Heating Operation`
        Enter the supply air volume flow rate per total floor area fraction.
        Required field when Supply air Flow Rate Method During Heating
        Operation is FlowPerFloorArea. This field may be blank if a heating
        coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area during Heating Operation`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_heating_operation` or None if not set

        """
        return self[
            "Supply Air Flow Rate Per Floor Area during Heating Operation"]

    @supply_air_flow_rate_per_floor_area_during_heating_operation.setter
    def supply_air_flow_rate_per_floor_area_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Per Floor Area during
        Heating Operation`"""
        self[
            "Supply Air Flow Rate Per Floor Area during Heating Operation"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self):
        """field `Fraction of Autosized Design Heating Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the heating
        supply air flow rate. Required field when Supply air Flow Rate Method
        During Heating Operation is FractionOfAutosizedHeatingValue. This field
        may be blank if a heating coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate` or None if not set

        """
        return self[
            "Fraction of Autosized Design Heating Supply Air Flow Rate"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Heating
        Supply Air Flow Rate`"""
        self[
            "Fraction of Autosized Design Heating Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation(
            self):
        """field `Design Supply Air Flow Rate Per Unit of Capacity During
        Heating Operation` Enter the supply air volume flow rate as a fraction
        of the heating capacity. Required field when Supply air Flow Rate
        Method During Heating Operation is FlowPerHeatingCapacity. This field
        may be blank if a heating coil is not included in the unitary system.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation` or None if not set

        """
        return self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate Per Unit of
        Capacity During Heating Operation`"""
        self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation"] = value

    @property
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(
            self):
        """field `Supply Air Flow Rate Method When No Cooling or Heating is
        Required` Enter the method used to determine the supply air volume flow
        rate when no cooling or heating is required. None is used when a
        heating coil is not included in the unitary system or this field may be
        blank. SupplyAirFlowRate is selected when the magnitude of the supply
        air volume is used. FlowPerFloorArea is selected when the supply air
        volume flow rate is based on total floor area served by the unitary
        system. FractionOfAutosizedCoolingValue is selected when the supply air
        volume is a fraction of the cooling value determined by the simulation.
        FractionOfAutosizedHeatingValue is selected when the supply air volume
        is a fraction of the heating value determined by the simulation.
        FlowPerCoolingCapacity is selected when the supply air volume is a
        fraction of the cooling capacity as determined by the simulation.
        FlowPerHeatingCapacity is selected when the supply air volume is a
        fraction of the heating capacity as determined by the simulation.

        Args:
            value (str): value for IDD Field `Supply Air Flow Rate Method When No Cooling or Heating is Required`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required` or None if not set

        """
        return self[
            "Supply Air Flow Rate Method When No Cooling or Heating is Required"]

    @supply_air_flow_rate_method_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Method When No
        Cooling or Heating is Required`"""
        self[
            "Supply Air Flow Rate Method When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(self):
        """field `Supply Air Flow Rate When No Cooling or Heating is Required`
        Enter the magnitude of the supply air volume flow rate during when no
        cooling or heating is required. Required field when Supply air Flow
        Rate Method When No Cooling or Heating is Required is
        SupplyAirFlowRate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Required`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_required` or None if not set

        """
        return self[
            "Supply Air Flow Rate When No Cooling or Heating is Required"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate When No Cooling or
        Heating is Required`"""
        self[
            "Supply Air Flow Rate When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required(
            self):
        """field `Supply Air Flow Rate Per Floor Area When No Cooling or
        Heating is Required` Enter the supply air volume flow rate per total
        floor area fraction. Required field when Supply air Flow Rate Method
        When No Cooling or Heating is Required is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required` or None if not set

        """
        return self[
            "Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required"]

    @supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_per_floor_area_when_no_cooling_or_heating_is_required(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Per Floor Area When
        No Cooling or Heating is Required`"""
        self[
            "Supply Air Flow Rate Per Floor Area When No Cooling or Heating is Required"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v3(self):
        """field `Fraction of Autosized Design Cooling Supply Air Flow Rate v3`
        Enter the supply air volume flow rate as a fraction of the cooling
        supply air flow rate. Required field when Supply air Flow Rate Method
        When No Cooling or Heating is Required is
        FractionOfAutosizedCoolingValue.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3` or None if not set

        """
        return self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate v3"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate_v3.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v3(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Cooling
        Supply Air Flow Rate v3`"""
        self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate v3"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate_v3(self):
        """field `Fraction of Autosized Design Heating Supply Air Flow Rate v3`
        Enter the supply air volume flow rate as a fraction of the heating
        supply air flow rate. Required field when Supply air Flow Rate Method
        When No Cooling or Heating is Required is
        FractionOfAutosizedHeatingValue.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Heating Supply Air Flow Rate v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate_v3` or None if not set

        """
        return self[
            "Fraction of Autosized Design Heating Supply Air Flow Rate v3"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate_v3.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate_v3(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Heating
        Supply Air Flow Rate v3`"""
        self[
            "Fraction of Autosized Design Heating Supply Air Flow Rate v3"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3(
            self):
        """field `Design Supply Air Flow Rate Per Unit of Capacity During
        Cooling Operation v3` Enter the supply air volume flow rate as a
        fraction of the cooling capacity. Required field when Supply air Flow
        Rate Method During Heating Operation is FlowPerCoolingCapacity.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v3`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3` or None if not set

        """
        return self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v3"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation_v3(
            self,
            value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate Per Unit of
        Capacity During Cooling Operation v3`"""
        self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Cooling Operation v3"] = value

    @property
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3(
            self):
        """field `Design Supply Air Flow Rate Per Unit of Capacity During
        Heating Operation v3` Enter the supply air volume flow rate as a
        fraction of the heating capacity. Required field when Supply air Flow
        Rate Method During Heating Operation is FlowPerHeatingCapacity.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v3`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3` or None if not set

        """
        return self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v3"]

    @design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3.setter
    def design_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation_v3(
            self,
            value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate Per Unit of
        Capacity During Heating Operation v3`"""
        self[
            "Design Supply Air Flow Rate Per Unit of Capacity During Heating Operation v3"] = value

    @property
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature` Enter the maximum supply air
        temperature leaving the heating coil.

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 80.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation(
            self):
        """field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
        Enter the maximum outdoor dry-bulb temperature for supplemental heater operation.

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
                Units: C
                Default value: 21.0

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
        If this field is blank, outdoor temperature from the weather file is used.
        If this field is not blank, the node name specified determines the outdoor temperature used
        for controlling supplemental heater operation.

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
    def maximum_cycling_rate(self):
        """field `Maximum Cycling Rate`
        Used only for water source heat pump.
        The maximum on-off cycling rate for the compressor.
        Suggested value is 2.5 for a typical heat pump.

        Args:
            value (float): value for IDD Field `Maximum Cycling Rate`
                Units: cycles/hr
                Default value: 2.5
                value <= 5.0

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
        """field `Heat Pump Time Constant` Used only for water source heat
        pump. Time constant for the cooling coil's capacity to reach steady
        state after startup. Suggested value is 60 for a typical heat pump.

        Args:
            value (float): value for IDD Field `Heat Pump Time Constant`
                Units: s
                Default value: 60.0
                value <= 500.0

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
        Used only for water source heat pump.
        The fraction of on-cycle power use to adjust the part load fraction based on
        the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        Suggested value is 0.01 for a typical heat pump.

        Args:
            value (float): value for IDD Field `Fraction of On-Cycle Power Use`
                Default value: 0.01
                value <= 0.05

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
        """field `Heat Pump Fan Delay Time` Used only for water source heat
        pump. Programmed time delay for heat pump fan to shut off after
        compressor cycle off. Only required when fan operating mode is cycling.
        Enter 0 when fan operating mode is continuous.

        Args:
            value (float): value for IDD Field `Heat Pump Fan Delay Time`
                Units: s
                Default value: 60.0

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
    def ancilliary_oncycle_electric_power(self):
        """field `Ancilliary On-Cycle Electric Power`
        Enter the value of ancilliary electric power for controls or other devices consumed during the on cycle.

        Args:
            value (float): value for IDD Field `Ancilliary On-Cycle Electric Power`
                Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ancilliary_oncycle_electric_power` or None if not set
        """
        return self["Ancilliary On-Cycle Electric Power"]

    @ancilliary_oncycle_electric_power.setter
    def ancilliary_oncycle_electric_power(self, value=None):
        """  Corresponds to IDD field `Ancilliary On-Cycle Electric Power`

        """
        self["Ancilliary On-Cycle Electric Power"] = value

    @property
    def ancilliary_offcycle_electric_power(self):
        """field `Ancilliary Off-Cycle Electric Power`
        Enter the value of ancilliary electric power for controls or other devices consumed during the off cycle.

        Args:
            value (float): value for IDD Field `Ancilliary Off-Cycle Electric Power`
                Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ancilliary_offcycle_electric_power` or None if not set
        """
        return self["Ancilliary Off-Cycle Electric Power"]

    @ancilliary_offcycle_electric_power.setter
    def ancilliary_offcycle_electric_power(self, value=None):
        """  Corresponds to IDD field `Ancilliary Off-Cycle Electric Power`

        """
        self["Ancilliary Off-Cycle Electric Power"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """field `Design Heat Recovery Water Flow Rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.
        Used for heat recovery to an EnergyPlus plant loop.

        Args:
            value (float): value for IDD Field `Design Heat Recovery Water Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Heat Recovery Water Flow Rate`"""
        self["Design Heat Recovery Water Flow Rate"] = value

    @property
    def maximum_temperature_for_heat_recovery(self):
        """field `Maximum Temperature for Heat Recovery` Enter the maximum heat
        recovery inlet temperature allowed for heat recovery.

        Args:
            value (float): value for IDD Field `Maximum Temperature for Heat Recovery`
                Units: C
                Default value: 80.0
                value <= 100.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_temperature_for_heat_recovery` or None if not set

        """
        return self["Maximum Temperature for Heat Recovery"]

    @maximum_temperature_for_heat_recovery.setter
    def maximum_temperature_for_heat_recovery(self, value=80.0):
        """Corresponds to IDD field `Maximum Temperature for Heat Recovery`"""
        self["Maximum Temperature for Heat Recovery"] = value

    @property
    def heat_recovery_water_inlet_node_name(self):
        """field `Heat Recovery Water Inlet Node Name` Enter the name of the
        heat recovery water inlet node if plant water loop connections are
        present.

        Args:
            value (str): value for IDD Field `Heat Recovery Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_water_inlet_node_name` or None if not set

        """
        return self["Heat Recovery Water Inlet Node Name"]

    @heat_recovery_water_inlet_node_name.setter
    def heat_recovery_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Water Inlet Node Name`"""
        self["Heat Recovery Water Inlet Node Name"] = value

    @property
    def heat_recovery_water_outlet_node_name(self):
        """field `Heat Recovery Water Outlet Node Name` Enter the name of the
        heat recovery water outlet node if plant water loop connections are
        present.

        Args:
            value (str): value for IDD Field `Heat Recovery Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_water_outlet_node_name` or None if not set

        """
        return self["Heat Recovery Water Outlet Node Name"]

    @heat_recovery_water_outlet_node_name.setter
    def heat_recovery_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Water Outlet Node Name`"""
        self["Heat Recovery Water Outlet Node Name"] = value

    @property
    def design_specification_multispeed_heat_pump_object_type(self):
        """field `Design Specification Multispeed Heat Pump Object Type` Enter
        the type of performance specification object used to describe the
        multispeed coil.

        Args:
            value (str): value for IDD Field `Design Specification Multispeed Heat Pump Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_multispeed_heat_pump_object_type` or None if not set

        """
        return self["Design Specification Multispeed Heat Pump Object Type"]

    @design_specification_multispeed_heat_pump_object_type.setter
    def design_specification_multispeed_heat_pump_object_type(
            self,
            value=None):
        """Corresponds to IDD field `Design Specification Multispeed Heat Pump
        Object Type`"""
        self["Design Specification Multispeed Heat Pump Object Type"] = value

    @property
    def design_specification_multispeed_heat_pump_object_name(self):
        """field `Design Specification Multispeed Heat Pump Object Name` Enter
        the name of the performance specification object used to describe the
        multispeed coil.

        Args:
            value (str): value for IDD Field `Design Specification Multispeed Heat Pump Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_multispeed_heat_pump_object_name` or None if not set

        """
        return self["Design Specification Multispeed Heat Pump Object Name"]

    @design_specification_multispeed_heat_pump_object_name.setter
    def design_specification_multispeed_heat_pump_object_name(
            self,
            value=None):
        """Corresponds to IDD field `Design Specification Multispeed Heat Pump
        Object Name`"""
        self["Design Specification Multispeed Heat Pump Object Name"] = value




class UnitarySystemPerformanceHeatPumpMultispeed(DataObject):

    """ Corresponds to IDD object `UnitarySystemPerformance:HeatPump:Multispeed`
        The UnitarySystemPerformance object is used to specify the air flow ratio at each
        operating speed. This object is primarily used for multispeed coils to allow operation
        at alternate flow rates different from those specified in the coil object.
    """
    _schema = {'extensible-fields': OrderedDict([(u'speed 1 supply air flow ratio during heating operation',
                                                  {'name': u'Speed 1 Supply Air Flow Ratio During Heating Operation',
                                                   'pyname': u'speed_1_supply_air_flow_ratio_during_heating_operation',
                                                   'minimum>': 0.0,
                                                   'required-field': True,
                                                   'autosizable': True,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm3/s'}),
                                                 (u'speed 1 supply air flow ratio during cooling operation',
                                                  {'name': u'Speed 1 Supply Air Flow Ratio During Cooling Operation',
                                                   'pyname': u'speed_1_supply_air_flow_ratio_during_cooling_operation',
                                                   'minimum>': 0.0,
                                                   'required-field': True,
                                                   'autosizable': True,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm3/s'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'number of speeds for heating',
                                       {'name': u'Number of Speeds for Heating',
                                        'pyname': u'number_of_speeds_for_heating',
                                        'maximum': 10,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of speeds for cooling',
                                       {'name': u'Number of Speeds for Cooling',
                                        'pyname': u'number_of_speeds_for_cooling',
                                        'maximum': 10,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 0,
               'name': u'UnitarySystemPerformance:HeatPump:Multispeed',
               'pyname': u'UnitarySystemPerformanceHeatPumpMultispeed',
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
    def number_of_speeds_for_heating(self):
        """field `Number of Speeds for Heating` Used only for Multi speed coils
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `Number of Speeds for Heating`
                value <= 10

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_speeds_for_heating` or None if not set

        """
        return self["Number of Speeds for Heating"]

    @number_of_speeds_for_heating.setter
    def number_of_speeds_for_heating(self, value=None):
        """Corresponds to IDD field `Number of Speeds for Heating`"""
        self["Number of Speeds for Heating"] = value

    @property
    def number_of_speeds_for_cooling(self):
        """field `Number of Speeds for Cooling` Used only for Multi speed coils
        Enter the number of the following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `Number of Speeds for Cooling`
                value <= 10

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_speeds_for_cooling` or None if not set

        """
        return self["Number of Speeds for Cooling"]

    @number_of_speeds_for_cooling.setter
    def number_of_speeds_for_cooling(self, value=None):
        """Corresponds to IDD field `Number of Speeds for Cooling`"""
        self["Number of Speeds for Cooling"] = value

    def add_extensible(
        self,
        speed_1_supply_air_flow_ratio_during_heating_operation=None,
        speed_1_supply_air_flow_ratio_during_cooling_operation=None,
    ):
        """Add values for extensible fields.

        Args:

            speed_1_supply_air_flow_ratio_during_heating_operation (float or "Autosize"): value for IDD Field `Speed 1 Supply Air Flow Ratio During Heating Operation`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            speed_1_supply_air_flow_ratio_during_cooling_operation (float or "Autosize"): value for IDD Field `Speed 1 Supply Air Flow Ratio During Cooling Operation`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        speed_1_supply_air_flow_ratio_during_heating_operation = self.check_value(
            "Speed 1 Supply Air Flow Ratio During Heating Operation",
            speed_1_supply_air_flow_ratio_during_heating_operation)
        vals.append(speed_1_supply_air_flow_ratio_during_heating_operation)
        speed_1_supply_air_flow_ratio_during_cooling_operation = self.check_value(
            "Speed 1 Supply Air Flow Ratio During Cooling Operation",
            speed_1_supply_air_flow_ratio_during_cooling_operation)
        vals.append(speed_1_supply_air_flow_ratio_during_cooling_operation)
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




class AirLoopHvacUnitaryFurnaceHeatOnly(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:Unitary:Furnace:HeatOnly`
        Unitary system, heating-only with constant volume supply fan (continuous or cycling)
        and heating coil (gas, electric, hot water, or steam). Identical to
        AirLoopHVAC:UnitaryHeatOnly.
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
                                      (u'furnace air inlet node name',
                                       {'name': u'Furnace Air Inlet Node Name',
                                        'pyname': u'furnace_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'furnace air outlet node name',
                                       {'name': u'Furnace Air Outlet Node Name',
                                        'pyname': u'furnace_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 80.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'supply air flow rate',
                                       {'name': u'Supply Air Flow Rate',
                                        'pyname': u'supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply fan object type',
                                       {'name': u'Supply Fan Object Type',
                                        'pyname': u'supply_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply fan name',
                                       {'name': u'Supply Fan Name',
                                        'pyname': u'supply_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
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
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 13,
               'name': u'AirLoopHVAC:Unitary:Furnace:HeatOnly',
               'pyname': u'AirLoopHvacUnitaryFurnaceHeatOnly',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def furnace_air_inlet_node_name(self):
        """field `Furnace Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Furnace Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `furnace_air_inlet_node_name` or None if not set

        """
        return self["Furnace Air Inlet Node Name"]

    @furnace_air_inlet_node_name.setter
    def furnace_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Furnace Air Inlet Node Name`"""
        self["Furnace Air Inlet Node Name"] = value

    @property
    def furnace_air_outlet_node_name(self):
        """field `Furnace Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Furnace Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `furnace_air_outlet_node_name` or None if not set

        """
        return self["Furnace Air Outlet Node Name"]

    @furnace_air_outlet_node_name.setter
    def furnace_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Furnace Air Outlet Node Name`"""
        self["Furnace Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name` A fan operating
        mode schedule value of 0 indicates cycling fan mode (supply air fan
        cycles on and off in tandem with the heating coil). Any other schedule
        value indicates continuous fan mode (supply air fan operates
        continuously regardless of heating coil operation). Leaving this
        schedule name blank will default to cycling fan mode for the entire
        simulation period.

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
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 80.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate(self):
        """field `Supply Air Flow Rate`
        This value should be > 0 and <= than the fan air flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate`"""
        self["Supply Air Flow Rate"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """field `Supply Fan Object Type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan
        operating mode schedule values are greater than 0).

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Fan Object Type`"""
        self["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """field `Supply Fan Name`

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
    def fan_placement(self):
        """field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Default value: BlowThrough

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
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type` works with gas, electric, hot water
        and steam heating coils.

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




class AirLoopHvacUnitaryFurnaceHeatCool(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:Unitary:Furnace:HeatCool`
        Unitary system, heating and cooling with constant volume supply fan (continuous or
        cycling), direct expansion (DX) cooling coil, heating coil (gas, electric,
        hot water, or steam), and optional reheat coil for dehumidification control.
        Identical to AirLoopHVAC:UnitaryHeatCool.
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
                                      (u'furnace air inlet node name',
                                       {'name': u'Furnace Air Inlet Node Name',
                                        'pyname': u'furnace_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'furnace air outlet node name',
                                       {'name': u'Furnace Air Outlet Node Name',
                                        'pyname': u'furnace_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 80.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'supply air flow rate during cooling operation',
                                       {'name': u'Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate during heating operation',
                                       {'name': u'Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate when no cooling or heating is needed',
                                       {'name': u'Supply Air Flow Rate When No Cooling or Heating is Needed',
                                        'pyname': u'supply_air_flow_rate_when_no_cooling_or_heating_is_needed',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply fan object type',
                                       {'name': u'Supply Fan Object Type',
                                        'pyname': u'supply_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply fan name',
                                       {'name': u'Supply Fan Name',
                                        'pyname': u'supply_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
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
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Multimode',
                                                            u'CoolReheat'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Desuperheater',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 17,
               'name': u'AirLoopHVAC:Unitary:Furnace:HeatCool',
               'pyname': u'AirLoopHvacUnitaryFurnaceHeatCool',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available. A schedule value
        greater than zero (usually 1 is used) indicates that the unit is
        available to operate as needed. A value less than or equal to zero
        (usually zero is used) denotes that the unit must be off.

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
    def furnace_air_inlet_node_name(self):
        """field `Furnace Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Furnace Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `furnace_air_inlet_node_name` or None if not set

        """
        return self["Furnace Air Inlet Node Name"]

    @furnace_air_inlet_node_name.setter
    def furnace_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Furnace Air Inlet Node Name`"""
        self["Furnace Air Inlet Node Name"] = value

    @property
    def furnace_air_outlet_node_name(self):
        """field `Furnace Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Furnace Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `furnace_air_outlet_node_name` or None if not set

        """
        return self["Furnace Air Outlet Node Name"]

    @furnace_air_outlet_node_name.setter
    def furnace_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Furnace Air Outlet Node Name`"""
        self["Furnace Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation). Provide a schedule
        with non-zero values when high humidity control is specified.
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

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
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 80.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """field `Supply Air Flow Rate During Cooling Operation` Must be less
        than or equal to the fan's maximum flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Cooling
        Operation`"""
        self["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """field `Supply Air Flow Rate During Heating Operation` Must be less
        than or equal to the fan's maximum flow fate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Heating
        Operation`"""
        self["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Must be less than or equal to the fan's maximum flow rate. Only used
        when fan operating mode is continuous (disregarded for cycling fan
        mode). This air flow rate is used when no heating or cooling is
        required (i.e., the DX coil compressor and heating coil are off). If
        this field is left blank or zero, the supply air flow rate from the
        previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set

        """
        return self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate When No Cooling or
        Heating is Needed`"""
        self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """field `Supply Fan Object Type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply
        air fan operating mode schedule values not equal to 0).

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Fan Object Type`"""
        self["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """field `Supply Fan Name`

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
    def fan_placement(self):
        """field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Default value: BlowThrough

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
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type` works with gas, electric, hot water
        and steam heating coils.

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
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type` Only works with DX cooling coil
        types.

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
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`
        None = meet sensible load only
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value

    @property
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type` Only required if dehumidification
        control type is "CoolReheat" works with gas, electric, hot water and
        steam heating coils.

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name` Only required if dehumidification control
        type is "CoolReheat".

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value




class AirLoopHvacUnitaryHeatOnly(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatOnly`
        Unitary system, heating-only with constant volume supply fan (continuous or cycling)
        and heating coil (gas, electric, hot water, or steam). Identical to
        AirLoopHVAC:Unitary:Furnace:HeatOnly.
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
                                      (u'unitary system air inlet node name',
                                       {'name': u'Unitary System Air Inlet Node Name',
                                        'pyname': u'unitary_system_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'unitary system air outlet node name',
                                       {'name': u'Unitary System Air Outlet Node Name',
                                        'pyname': u'unitary_system_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 80.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'supply air flow rate',
                                       {'name': u'Supply Air Flow Rate',
                                        'pyname': u'supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply fan object type',
                                       {'name': u'Supply Fan Object Type',
                                        'pyname': u'supply_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply fan name',
                                       {'name': u'Supply Fan Name',
                                        'pyname': u'supply_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
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
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 13,
               'name': u'AirLoopHVAC:UnitaryHeatOnly',
               'pyname': u'AirLoopHvacUnitaryHeatOnly',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def unitary_system_air_inlet_node_name(self):
        """field `Unitary System Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Unitary System Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unitary_system_air_inlet_node_name` or None if not set

        """
        return self["Unitary System Air Inlet Node Name"]

    @unitary_system_air_inlet_node_name.setter
    def unitary_system_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Unitary System Air Inlet Node Name`"""
        self["Unitary System Air Inlet Node Name"] = value

    @property
    def unitary_system_air_outlet_node_name(self):
        """field `Unitary System Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Unitary System Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unitary_system_air_outlet_node_name` or None if not set

        """
        return self["Unitary System Air Outlet Node Name"]

    @unitary_system_air_outlet_node_name.setter
    def unitary_system_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Unitary System Air Outlet Node Name`"""
        self["Unitary System Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name` A fan operating
        mode schedule value of 0 indicates cycling fan mode (supply air fan
        cycles on and off in tandem with the heating coil). Any other schedule
        value indicates continuous fan mode (supply air fan operates
        continuously regardless of heating coil operation). Leaving this
        schedule name blank will default to cycling fan mode for the entire
        simulation period.

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
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 80.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate(self):
        """field `Supply Air Flow Rate`
        This value should be > 0 and <= than the fan air flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate`"""
        self["Supply Air Flow Rate"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """field `Supply Fan Object Type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan
        operating mode schedule values are greater than 0).

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Fan Object Type`"""
        self["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """field `Supply Fan Name`

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
    def fan_placement(self):
        """field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Default value: BlowThrough

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
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type` works with gas, electric, hot water
        and steam heating coils.

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




class AirLoopHvacUnitaryHeatCool(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatCool`
        Unitary system, heating and cooling with constant volume supply fan (continuous or
        cycling), direct expansion (DX) cooling coil, heating coil (gas, electric,
        hot water, or steam), and optional reheat coil for dehumidification control.
        Identical to AirLoopHVAC:Unitary:Furnace:HeatCool.
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
                                      (u'unitary system air inlet node name',
                                       {'name': u'Unitary System Air Inlet Node Name',
                                        'pyname': u'unitary_system_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'unitary system air outlet node name',
                                       {'name': u'Unitary System Air Outlet Node Name',
                                        'pyname': u'unitary_system_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air fan operating mode schedule name',
                                       {'name': u'Supply Air Fan Operating Mode Schedule Name',
                                        'pyname': u'supply_air_fan_operating_mode_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature',
                                       {'name': u'Maximum Supply Air Temperature',
                                        'pyname': u'maximum_supply_air_temperature',
                                        'default': 80.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'supply air flow rate during cooling operation',
                                       {'name': u'Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate during heating operation',
                                       {'name': u'Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate when no cooling or heating is needed',
                                       {'name': u'Supply Air Flow Rate When No Cooling or Heating is Needed',
                                        'pyname': u'supply_air_flow_rate_when_no_cooling_or_heating_is_needed',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply fan object type',
                                       {'name': u'Supply Fan Object Type',
                                        'pyname': u'supply_fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff',
                                                            u'Fan:ConstantVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply fan name',
                                       {'name': u'Supply Fan Name',
                                        'pyname': u'supply_fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
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
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Multimode',
                                                            u'CoolReheat'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Desuperheater',
                                                            u'Coil:Heating:Water',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 17,
               'name': u'AirLoopHVAC:UnitaryHeatCool',
               'pyname': u'AirLoopHvacUnitaryHeatCool',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def unitary_system_air_inlet_node_name(self):
        """field `Unitary System Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Unitary System Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unitary_system_air_inlet_node_name` or None if not set

        """
        return self["Unitary System Air Inlet Node Name"]

    @unitary_system_air_inlet_node_name.setter
    def unitary_system_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Unitary System Air Inlet Node Name`"""
        self["Unitary System Air Inlet Node Name"] = value

    @property
    def unitary_system_air_outlet_node_name(self):
        """field `Unitary System Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Unitary System Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unitary_system_air_outlet_node_name` or None if not set

        """
        return self["Unitary System Air Outlet Node Name"]

    @unitary_system_air_outlet_node_name.setter
    def unitary_system_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Unitary System Air Outlet Node Name`"""
        self["Unitary System Air Outlet Node Name"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`
        A fan operating mode schedule value of 0 indicates cycling fan mode (supply air
        fan cycles on and off in tandem with the cooling or heating coil).
        Any other schedule value indicates continuous fan mode (supply air fan operates
        continuously regardless of cooling or heating coil operation). Provide a schedule
        with non-zero values when high humidity control is specified.
        Leaving this schedule name blank will default to cycling fan mode for the
        entire simulation period.

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
    def maximum_supply_air_temperature(self):
        """field `Maximum Supply Air Temperature`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature`
                Units: C
                Default value: 80.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature` or None if not set

        """
        return self["Maximum Supply Air Temperature"]

    @maximum_supply_air_temperature.setter
    def maximum_supply_air_temperature(self, value=80.0):
        """Corresponds to IDD field `Maximum Supply Air Temperature`"""
        self["Maximum Supply Air Temperature"] = value

    @property
    def supply_air_flow_rate_during_cooling_operation(self):
        """field `Supply Air Flow Rate During Cooling Operation` Must be less
        than or equal to the fan's maximum flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Cooling
        Operation`"""
        self["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """field `Supply Air Flow Rate During Heating Operation` Must be less
        than or equal to the fan's maximum flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Heating
        Operation`"""
        self["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Must be less than or equal to the fan's maximum flow rate. Only used
        when fan operating mode is continuous (disregarded for cycling fan
        mode). This air flow rate is used when no heating or cooling is
        required (i.e., the DX coil compressor and heating coil are off). If
        this field is left blank or zero, the supply air flow rate from the
        previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set

        """
        return self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate When No Cooling or
        Heating is Needed`"""
        self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_fan_object_type(self):
        """field `Supply Fan Object Type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply
        air fan operating mode schedule values not equal to 0).

        Args:
            value (str): value for IDD Field `Supply Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_fan_object_type` or None if not set
        """
        return self["Supply Fan Object Type"]

    @supply_fan_object_type.setter
    def supply_fan_object_type(self, value=None):
        """Corresponds to IDD field `Supply Fan Object Type`"""
        self["Supply Fan Object Type"] = value

    @property
    def supply_fan_name(self):
        """field `Supply Fan Name`

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
    def fan_placement(self):
        """field `Fan Placement`

        Args:
            value (str): value for IDD Field `Fan Placement`
                Default value: BlowThrough

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
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type` works with gas, electric, hot water
        and steam heating coils.

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
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`
        Only works with DX cooling coil types or
        Coil:Cooling:DX:VariableSpeed.

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
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`
        None = meet sensible load only
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted Cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value

    @property
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type` Only required if dehumidification
        control type is "CoolReheat" works with gas, electric, desuperheating,
        hot water and steam heating coils.

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name` Only required if dehumidification control
        type is "CoolReheat".

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value




class AirLoopHvacUnitaryHeatPumpAirToAir(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatPump:AirToAir`
        Unitary heat pump system, heating and cooling, single-speed with supply fan, direct
        expansion (DX) cooling coil, DX heating coil (air-to-air heat pump), and supplemental
        heating coil (gas, electric, hot water, or steam).
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
                                      (u'supply air flow rate during cooling operation',
                                       {'name': u'Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate during heating operation',
                                       {'name': u'Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate when no cooling or heating is needed',
                                       {'name': u'Supply Air Flow Rate When No Cooling or Heating is Needed',
                                        'pyname': u'supply_air_flow_rate_when_no_cooling_or_heating_is_needed',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
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
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Multimode',
                                                            u'CoolReheat'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 19,
               'name': u'AirLoopHVAC:UnitaryHeatPump:AirToAir',
               'pyname': u'AirLoopHvacUnitaryHeatPumpAirToAir',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available. A schedule value
        greater than zero (usually 1 is used) indicates that the unit is
        available to operate as needed. A value less than or equal to zero
        (usually zero is used) denotes that the unit must be off.

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
    def supply_air_flow_rate_during_cooling_operation(self):
        """field `Supply Air Flow Rate During Cooling Operation` Must be less
        than or equal to the fan's maximum flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Cooling Operation"]

    @supply_air_flow_rate_during_cooling_operation.setter
    def supply_air_flow_rate_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Cooling
        Operation`"""
        self["Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def supply_air_flow_rate_during_heating_operation(self):
        """field `Supply Air Flow Rate During Heating Operation` Must be less
        than or equal to the fan's maximum flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Supply Air Flow Rate During Heating Operation"]

    @supply_air_flow_rate_during_heating_operation.setter
    def supply_air_flow_rate_during_heating_operation(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate During Heating
        Operation`"""
        self["Supply Air Flow Rate During Heating Operation"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Must be less than or equal to the fans maximum flow rate. Only used
        when fan operating mode is continuous (disregarded for cycling fan
        mode). This air flow rate is used when no heating or cooling is
        required (i.e., the DX coil compressor and supplemental heating coil
        are off). If this field is left blank or zero, the supply air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set

        """
        return self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate When No Cooling or
        Heating is Needed`"""
        self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type`
        Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan
        operating mode schedule values are greater than 0 or the fan operating mode
        schedule name field is left blank).

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
        """field `Supply Air Fan Name` Needs to match in the fan object.

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
        Only works with Coil:Heating:DX:SingleSpeed or
        Coil:Heating:DX:VariableSpeed

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
        """field `Heating Coil Name` Needs to match in the DX heating coil
        object.

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
        Only works with Coil:Cooling:DX:SingleSpeed or
        CoilSystem:Cooling:DX:HeatExchangerAssisted or
        Coil:Cooling:DX:VariableSpeed

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
        """field `Cooling Coil Name` Needs to match in the DX cooling coil
        object.

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
    def supplemental_heating_coil_object_type(self):
        """field `Supplemental Heating Coil Object Type` works with gas,
        electric, hot water and steam heating coils.

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
        """field `Supplemental Heating Coil Name` Needs to match in the
        supplemental heating coil object.

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

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set

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

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
                Units: C
                Default value: 21.0
                value <= 21.0

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

        Args:
            value (str): value for IDD Field `Fan Placement`
                Default value: BlowThrough

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
        """field `Supply Air Fan Operating Mode Schedule Name` A fan operating
        mode schedule value of 0 indicates cycling fan mode (supply air fan
        cycles on and off in tandem with the cooling or heating coil). Any
        other schedule value indicates continuous fan mode (supply air fan
        operates continuously regardless of cooling or heating coil operation).
        Leaving this schedule name blank will default to cycling fan mode for
        the entire simulation period.

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
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`
        None = meet sensible load only
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load.  Valid only with
        cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted.
        This control mode allows the heat exchanger to be turned
        on and off based on the zone dehumidification requirements.
        A ZoneControl:Humidistat object is also required.
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid with all
        cooling coil types. When a heat exchanger assisted Cooling
        coil is used, the heat exchanger is locked on at all times.
        A ZoneControl:Humidistat object is also required.

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value




class AirLoopHvacUnitaryHeatPumpWaterToAir(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatPump:WaterToAir`
        Unitary heat pump system, heating and cooling, single-speed with constant volume
        supply fan (continuous or cycling), direct expansion (DX) cooling coil, DX heating
        coil (water-to-air heat pump), and supplemental heating coil (gas, electric,
        hot water, or steam).
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
                                      (u'supply air flow rate',
                                       {'name': u'Supply Air Flow Rate',
                                        'pyname': u'supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
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
                                        'accepted-values': [u'Coil:Heating:WaterToAirHeatPump:ParameterEstimation',
                                                            u'Coil:Heating:WaterToAirHeatPump:EquationFit',
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
                                      (u'heating convergence',
                                       {'name': u'Heating Convergence',
                                        'pyname': u'heating_convergence',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation',
                                                            u'Coil:Cooling:WaterToAirHeatPump:EquationFit',
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
                                      (u'cooling convergence',
                                       {'name': u'Cooling Convergence',
                                        'pyname': u'cooling_convergence',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
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
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'CoolReheat'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 25,
               'name': u'AirLoopHVAC:UnitaryHeatPump:WaterToAir',
               'pyname': u'AirLoopHvacUnitaryHeatPumpWaterToAir',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def supply_air_flow_rate(self):
        """field `Supply Air Flow Rate`
        This value should be > 0 and <= than the fan air flow rate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate` or None if not set
        """
        return self["Supply Air Flow Rate"]

    @supply_air_flow_rate.setter
    def supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Supply Air Flow Rate`"""
        self["Supply Air Flow Rate"] = value

    @property
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type` Only works with On/Off Fan.

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
        Needs to match Fan:OnOff object

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
        Needs to match in the water-to-air heatpump heating coil object

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
    def heating_convergence(self):
        """field `Heating Convergence`

        Args:
            value (float): value for IDD Field `Heating Convergence`
                Default value: 0.001

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence` or None if not set

        """
        return self["Heating Convergence"]

    @heating_convergence.setter
    def heating_convergence(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence`"""
        self["Heating Convergence"] = value

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
        Needs to match in the water-to-air heatpump cooling coil object

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
    def cooling_convergence(self):
        """field `Cooling Convergence`

        Args:
            value (float): value for IDD Field `Cooling Convergence`
                Default value: 0.001

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_convergence` or None if not set

        """
        return self["Cooling Convergence"]

    @cooling_convergence.setter
    def cooling_convergence(self, value=0.001):
        """Corresponds to IDD field `Cooling Convergence`"""
        self["Cooling Convergence"] = value

    @property
    def maximum_cycling_rate(self):
        """field `Maximum Cycling Rate`
        The maximum on-off cycling rate for the compressor
        Suggested value is 2.5 for a typical heat pump

        Args:
            value (float): value for IDD Field `Maximum Cycling Rate`
                Units: cycles/hr
                Default value: 2.5
                value <= 5.0

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
        """field `Heat Pump Time Constant` Time constant for the cooling coil's
        capacity to reach steady state after startup Suggested value is 60 for
        a typical heat pump.

        Args:
            value (float): value for IDD Field `Heat Pump Time Constant`
                Units: s
                Default value: 60.0
                value <= 500.0

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
        The fraction of on-cycle power use to adjust the part load fraction based on
        the off-cycle power consumption due to crankcase heaters, controls, fans, and etc.
        Suggested value is 0.01 for a typical heat pump

        Args:
            value (float): value for IDD Field `Fraction of On-Cycle Power Use`
                Default value: 0.01
                value <= 0.05

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
        """field `Heat Pump Fan Delay Time` Programmed time delay for heat pump
        fan to shut off after compressor cycle off. Only required when fan
        operating mode is cycling Enter 0 when fan operating mode is
        continuous.

        Args:
            value (float): value for IDD Field `Heat Pump Fan Delay Time`
                Units: s
                Default value: 60.0

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
        """field `Supplemental Heating Coil Object Type` works with gas,
        electric, hot water and steam heating coils.

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
        """field `Supplemental Heating Coil Name` Needs to match in the
        supplemental heating coil object.

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

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set

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

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
                Units: C
                Default value: 21.0
                value <= 21.0

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

        Args:
            value (str): value for IDD Field `Fan Placement`
                Default value: BlowThrough

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
        """field `Supply Air Fan Operating Mode Schedule Name` Enter the name
        of a schedule that controls fan operation. Schedule values of 0 denote
        cycling fan operation (fan cycles with cooling or heating coil).
        Schedule values greater than 0 denote constant fan operation (fan runs
        continually regardless of coil operation). The fan operating mode
        defaults to cycling fan operation if this field is left blank.

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
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`
        None = meet sensible load only
        CoolReheat = cool beyond the dry bulb setpoint.
        as required to meet the humidity setpoint.  Valid only with
        Coil:Cooling:WaterToAirHeatPump:EquationFit or
        Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value

    @property
    def heat_pump_coil_water_flow_mode(self):
        """field `Heat Pump Coil Water Flow Mode`
        used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit
        Constant results in 100% water flow regardless of compressor PLR
        Cycling results in water flow that matches compressor PLR
        ConstantOnDemand results in 100% water flow whenever the coil is on, but is 0% whenever the coil has no load

        Args:
            value (str): value for IDD Field `Heat Pump Coil Water Flow Mode`
                Default value: Cycling

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




class AirLoopHvacUnitaryHeatCoolVavchangeoverBypass(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass`
        Unitary system, heating and cooling with constant volume supply fan (continuous or
        cycling), direct expansion (DX) cooling coil, heating coil (gas, electric,
        hot water, steam, or DX air-to-air heat pump) and bypass damper for variable volume
        flow to terminal units. Used with AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat
        or AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat.
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
                                      (u'system air flow rate during cooling operation',
                                       {'name': u'System Air Flow Rate During Cooling Operation',
                                        'pyname': u'system_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'system air flow rate during heating operation',
                                       {'name': u'System Air Flow Rate During Heating Operation',
                                        'pyname': u'system_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'system air flow rate when no cooling or heating is needed',
                                       {'name': u'System Air Flow Rate When No Cooling or Heating is Needed',
                                        'pyname': u'system_air_flow_rate_when_no_cooling_or_heating_is_needed',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air flow rate during cooling operation',
                                       {'name': u'Outdoor Air Flow Rate During Cooling Operation',
                                        'pyname': u'outdoor_air_flow_rate_during_cooling_operation',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air flow rate during heating operation',
                                       {'name': u'Outdoor Air Flow Rate During Heating Operation',
                                        'pyname': u'outdoor_air_flow_rate_during_heating_operation',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air flow rate when no cooling or heating is needed',
                                       {'name': u'Outdoor Air Flow Rate When No Cooling or Heating is Needed',
                                        'pyname': u'outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air flow rate multiplier schedule name',
                                       {'name': u'Outdoor Air Flow Rate Multiplier Schedule Name',
                                        'pyname': u'outdoor_air_flow_rate_multiplier_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'bypass duct mixer node name',
                                       {'name': u'Bypass Duct Mixer Node Name',
                                        'pyname': u'bypass_duct_mixer_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'bypass duct splitter node name',
                                       {'name': u'Bypass Duct Splitter Node Name',
                                        'pyname': u'bypass_duct_splitter_node_name',
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
                                      (u'supply air fan placement',
                                       {'name': u'Supply Air Fan Placement',
                                        'pyname': u'supply_air_fan_placement',
                                        'required-field': True,
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
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:SingleSpeed',
                                                            u'CoilSystem:Cooling:DX:HeatExchangerAssisted',
                                                            u'Coil:Cooling:DX:TwoStageWithHumidityControlMode'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
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
                                                            u'Coil:Heating:Gas',
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
                                      (u'priority control mode',
                                       {'name': u'Priority Control Mode',
                                        'pyname': u'priority_control_mode',
                                        'default': u'ZonePriority',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'CoolingPriority',
                                                            u'HeatingPriority',
                                                            u'ZonePriority'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum outlet air temperature during cooling operation',
                                       {'name': u'Minimum Outlet Air Temperature During Cooling Operation',
                                        'pyname': u'minimum_outlet_air_temperature_during_cooling_operation',
                                        'default': 8.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outlet air temperature during heating operation',
                                       {'name': u'Maximum Outlet Air Temperature During Heating Operation',
                                        'pyname': u'maximum_outlet_air_temperature_during_heating_operation',
                                        'default': 50.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Multimode',
                                                            u'CoolReheat'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 23,
               'name': u'AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass',
               'pyname': u'AirLoopHvacUnitaryHeatCoolVavchangeoverBypass',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name` Enter a unique name for this unitary system.

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
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.
        Enter the availability schedule name. Schedule values of zero denote system
        is Off. Non-zero schedule values denote system is available to operate.

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
    def system_air_flow_rate_during_cooling_operation(self):
        """field `System Air Flow Rate During Cooling Operation` Enter the
        system air flow rate during cooling operation or specify autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `System Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `system_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["System Air Flow Rate During Cooling Operation"]

    @system_air_flow_rate_during_cooling_operation.setter
    def system_air_flow_rate_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `System Air Flow Rate During Cooling
        Operation`"""
        self["System Air Flow Rate During Cooling Operation"] = value

    @property
    def system_air_flow_rate_during_heating_operation(self):
        """field `System Air Flow Rate During Heating Operation` Enter the
        system air flow rate during heating operation or specify autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `System Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `system_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["System Air Flow Rate During Heating Operation"]

    @system_air_flow_rate_during_heating_operation.setter
    def system_air_flow_rate_during_heating_operation(self, value=None):
        """Corresponds to IDD field `System Air Flow Rate During Heating
        Operation`"""
        self["System Air Flow Rate During Heating Operation"] = value

    @property
    def system_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """field `System Air Flow Rate When No Cooling or Heating is Needed`
        Only used when the supply air fan operating mode is continuous (see
        field Supply air fan operating mode schedule name). This system air
        flow rate is used when no heating or cooling is required and the coils
        are off. If this field is left blank or zero, the system air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `System Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `system_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set

        """
        return self[
            "System Air Flow Rate When No Cooling or Heating is Needed"]

    @system_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def system_air_flow_rate_when_no_cooling_or_heating_is_needed(
            self,
            value=None):
        """Corresponds to IDD field `System Air Flow Rate When No Cooling or
        Heating is Needed`"""
        self[
            "System Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_during_cooling_operation(self):
        """field `Outdoor Air Flow Rate During Cooling Operation` Enter the
        outdoor air flow rate during cooling operation or specify autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Outdoor Air Flow Rate During Cooling Operation"]

    @outdoor_air_flow_rate_during_cooling_operation.setter
    def outdoor_air_flow_rate_during_cooling_operation(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow Rate During Cooling
        Operation`"""
        self["Outdoor Air Flow Rate During Cooling Operation"] = value

    @property
    def outdoor_air_flow_rate_during_heating_operation(self):
        """field `Outdoor Air Flow Rate During Heating Operation` Enter the
        outdoor air flow rate during heating operation or specify autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Outdoor Air Flow Rate During Heating Operation"]

    @outdoor_air_flow_rate_during_heating_operation.setter
    def outdoor_air_flow_rate_during_heating_operation(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow Rate During Heating
        Operation`"""
        self["Outdoor Air Flow Rate During Heating Operation"] = value

    @property
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
        Only used when the supply air fan operating mode is continuous (see
        field Supply air fan operating mode schedule name). This outdoor air
        flow rate is used when no heating or cooling is required and the coils
        are off. If this field is left blank or zero, the outdoor air flow rate
        from the previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Outdoor Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set

        """
        return self[
            "Outdoor Air Flow Rate When No Cooling or Heating is Needed"]

    @outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def outdoor_air_flow_rate_when_no_cooling_or_heating_is_needed(
            self,
            value=None):
        """Corresponds to IDD field `Outdoor Air Flow Rate When No Cooling or
        Heating is Needed`"""
        self[
            "Outdoor Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def outdoor_air_flow_rate_multiplier_schedule_name(self):
        """field `Outdoor Air Flow Rate Multiplier Schedule Name`
        Enter the name of a schedule that contains multipliers for the outdoor air
        flow rates. Schedule values must be from 0 to 1.
        If field is left blank, model assumes multiplier is 1 for the entire simulation period.

        Args:
            value (str): value for IDD Field `Outdoor Air Flow Rate Multiplier Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_flow_rate_multiplier_schedule_name` or None if not set
        """
        return self["Outdoor Air Flow Rate Multiplier Schedule Name"]

    @outdoor_air_flow_rate_multiplier_schedule_name.setter
    def outdoor_air_flow_rate_multiplier_schedule_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow Rate Multiplier Schedule
        Name`"""
        self["Outdoor Air Flow Rate Multiplier Schedule Name"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name` Enter the name of the unitary system's
        air inlet node.

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
    def bypass_duct_mixer_node_name(self):
        """field `Bypass Duct Mixer Node Name` Enter the name of the bypass
        duct mixer node. This name should be the name of the return air node
        for the outdoor air mixer associated with this system. This node name
        must be different from the air inlet node name.

        Args:
            value (str): value for IDD Field `Bypass Duct Mixer Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `bypass_duct_mixer_node_name` or None if not set

        """
        return self["Bypass Duct Mixer Node Name"]

    @bypass_duct_mixer_node_name.setter
    def bypass_duct_mixer_node_name(self, value=None):
        """Corresponds to IDD field `Bypass Duct Mixer Node Name`"""
        self["Bypass Duct Mixer Node Name"] = value

    @property
    def bypass_duct_splitter_node_name(self):
        """field `Bypass Duct Splitter Node Name` Enter the name of the bypass
        duct splitter node. This splitter air node is the outlet node of the
        last component in this unitary system. For blow through fan placement,
        the splitter air node is the outlet node of the heating coil. For draw
        through fan placement, the splitter node is the outlet node of the
        supply air fan.

        Args:
            value (str): value for IDD Field `Bypass Duct Splitter Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `bypass_duct_splitter_node_name` or None if not set

        """
        return self["Bypass Duct Splitter Node Name"]

    @bypass_duct_splitter_node_name.setter
    def bypass_duct_splitter_node_name(self, value=None):
        """Corresponds to IDD field `Bypass Duct Splitter Node Name`"""
        self["Bypass Duct Splitter Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name` Enter the name of the unitary system's
        air outlet node.

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
        currently only one type OutdoorAir:Mixer object is available.

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
        """field `Outdoor Air Mixer Name` Enter the name of the outdoor air
        mixer used with this unitary system.

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
        """field `Supply Air Fan Object Type` Specify the type of supply air
        fan used in this unitary system.

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
        """field `Supply Air Fan Name` Enter the name of the supply air fan
        used in this unitary system.

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
    def supply_air_fan_placement(self):
        """field `Supply Air Fan Placement` Specify supply air fan placement as
        either blow through or draw through. BlowThrough means the supply air
        fan is located before the cooling coil. DrawThrough means the supply
        air fan is located after the heating coil.

        Args:
            value (str): value for IDD Field `Supply Air Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_placement` or None if not set

        """
        return self["Supply Air Fan Placement"]

    @supply_air_fan_placement.setter
    def supply_air_fan_placement(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Placement`"""
        self["Supply Air Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule to control the supply air fan. Schedule Name values of zero
        mean that the supply air fan will cycle off if there is no cooling or heating load
        in any of the zones being served by this system. Non-zero schedule values mean
        that the supply air fan will operate continuously even if there is no cooling or
        heating load in any of the zones being served. If this field is left blank,
        the supply air fan will operate continuously for the entire simulation period.

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
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type` Specify the type of cooling coil
        used in this unitary system.

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
        """field `Cooling Coil Name` Enter the name of the cooling coil used in
        this unitary system.

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
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type` works with DX, gas, electric, hot
        water and steam heating coils Specify the type of heating coil used in
        this unitary system.

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
        """field `Heating Coil Name` Enter the name of the heating coil used in
        this unitary system.

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
    def priority_control_mode(self):
        """field `Priority Control Mode`
        CoolingPriority = system provides cooling if any zone requires cooling.
        HeatingPriority = system provides heating if any zone requires heating.
        ZonePriority = system controlled based on the total number of zones
        requiring cooling or heating (highest number of zones
        in cooling or heating determines the system's operating mode).

        Args:
            value (str): value for IDD Field `Priority Control Mode`
                Default value: ZonePriority

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `priority_control_mode` or None if not set
        """
        return self["Priority Control Mode"]

    @priority_control_mode.setter
    def priority_control_mode(self, value="ZonePriority"):
        """Corresponds to IDD field `Priority Control Mode`"""
        self["Priority Control Mode"] = value

    @property
    def minimum_outlet_air_temperature_during_cooling_operation(self):
        """field `Minimum Outlet Air Temperature During Cooling Operation`
        Specify the minimum outlet air temperature allowed for this unitary
        system during cooling operation. This value should be less than the
        maximum outlet air temperature during heating operation.

        Args:
            value (float): value for IDD Field `Minimum Outlet Air Temperature During Cooling Operation`
                Units: C
                Default value: 8.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outlet_air_temperature_during_cooling_operation` or None if not set

        """
        return self["Minimum Outlet Air Temperature During Cooling Operation"]

    @minimum_outlet_air_temperature_during_cooling_operation.setter
    def minimum_outlet_air_temperature_during_cooling_operation(
            self,
            value=8.0):
        """Corresponds to IDD field `Minimum Outlet Air Temperature During
        Cooling Operation`"""
        self["Minimum Outlet Air Temperature During Cooling Operation"] = value

    @property
    def maximum_outlet_air_temperature_during_heating_operation(self):
        """field `Maximum Outlet Air Temperature During Heating Operation`
        Specify the maximum outlet air temperature allowed for this unitary
        system during heating operation. This value should be greater than the
        minimum outlet air temperature during cooling operation.

        Args:
            value (float): value for IDD Field `Maximum Outlet Air Temperature During Heating Operation`
                Units: C
                Default value: 50.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outlet_air_temperature_during_heating_operation` or None if not set

        """
        return self["Maximum Outlet Air Temperature During Heating Operation"]

    @maximum_outlet_air_temperature_during_heating_operation.setter
    def maximum_outlet_air_temperature_during_heating_operation(
            self,
            value=50.0):
        """Corresponds to IDD field `Maximum Outlet Air Temperature During
        Heating Operation`"""
        self["Maximum Outlet Air Temperature During Heating Operation"] = value

    @property
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`
        None = meet sensible load only.
        Multimode = activate enhanced dehumidification mode
        as needed and meet sensible load.  Valid only with
        Coil:Cooling:DX:TwoStageWithHumidityControlMode.
        CoolReheat = cool beyond the Dry-Bulb temperature setpoint
        as required to meet the humidity setpoint.  Valid only with
        Coil:Cooling:DX:TwoStageWithHumidityControlMode.
        For all dehumidification controls, the max humidity setpoint
        on this unitary system's air outlet node is used.
        This must be set using ZoneControl:Humidistat and
        SetpointManager:SingleZone:Humidity:Maximum,
        SetpointManager:MultiZone:Humidity:Maximum or
        SetpointManager:MultiZone:MaximumHumidity:Average objects.

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="None"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value




class AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed`
        Unitary system, heating and cooling, multi-speed with constant volume supply fan
        (continuous or cycling), direct expansion (DX) cooling coil, heating coil
        (DX air-to-air heat pump, gas, electric, hot water, or steam), and supplemental
        heating coil (gas, electric, hot water, or steam).
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
                                      (u'controlling zone or thermostat location',
                                       {'name': u'Controlling Zone or Thermostat Location',
                                        'pyname': u'controlling_zone_or_thermostat_location',
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
                                      (u'supply air fan placement',
                                       {'name': u'Supply Air Fan Placement',
                                        'pyname': u'supply_air_fan_placement',
                                        'required-field': True,
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
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:DX:MultiSpeed',
                                                            u'Coil:Heating:Electric:MultiStage',
                                                            u'Coil:Heating:Gas:MultiStage',
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
                                      (u'minimum outdoor dry-bulb temperature for compressor operation',
                                       {'name': u'Minimum Outdoor Dry-Bulb Temperature for Compressor Operation',
                                        'pyname': u'minimum_outdoor_drybulb_temperature_for_compressor_operation',
                                        'default': -8.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:DX:MultiSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supplemental heating coil object type',
                                       {'name': u'Supplemental Heating Coil Object Type',
                                        'pyname': u'supplemental_heating_coil_object_type',
                                        'required-field': False,
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
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum supply air temperature from supplemental heater',
                                       {'name': u'Maximum Supply Air Temperature from Supplemental Heater',
                                        'pyname': u'maximum_supply_air_temperature_from_supplemental_heater',
                                        'required-field': False,
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
                                      (u'auxiliary on-cycle electric power',
                                       {'name': u'Auxiliary On-Cycle Electric Power',
                                        'pyname': u'auxiliary_oncycle_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'auxiliary off-cycle electric power',
                                       {'name': u'Auxiliary Off-Cycle Electric Power',
                                        'pyname': u'auxiliary_offcycle_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'design heat recovery water flow rate',
                                       {'name': u'Design Heat Recovery Water Flow Rate',
                                        'pyname': u'design_heat_recovery_water_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum temperature for heat recovery',
                                       {'name': u'Maximum Temperature for Heat Recovery',
                                        'pyname': u'maximum_temperature_for_heat_recovery',
                                        'default': 80.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'heat recovery water inlet node name',
                                       {'name': u'Heat Recovery Water Inlet Node Name',
                                        'pyname': u'heat_recovery_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heat recovery water outlet node name',
                                       {'name': u'Heat Recovery Water Outlet Node Name',
                                        'pyname': u'heat_recovery_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air flow rate when no cooling or heating is needed',
                                       {'name': u'Supply Air Flow Rate When No Cooling or Heating is Needed',
                                        'pyname': u'supply_air_flow_rate_when_no_cooling_or_heating_is_needed',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'number of speeds for heating',
                                       {'name': u'Number of Speeds for Heating',
                                        'pyname': u'number_of_speeds_for_heating',
                                        'maximum': 4,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of speeds for cooling',
                                       {'name': u'Number of Speeds for Cooling',
                                        'pyname': u'number_of_speeds_for_cooling',
                                        'maximum': 4,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 2,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'speed 1 supply air flow rate during heating operation',
                                       {'name': u'Speed 1 Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'speed_1_supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 2 supply air flow rate during heating operation',
                                       {'name': u'Speed 2 Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'speed_2_supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 3 supply air flow rate during heating operation',
                                       {'name': u'Speed 3 Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'speed_3_supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 4 supply air flow rate during heating operation',
                                       {'name': u'Speed 4 Supply Air Flow Rate During Heating Operation',
                                        'pyname': u'speed_4_supply_air_flow_rate_during_heating_operation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 1 supply air flow rate during cooling operation',
                                       {'name': u'Speed 1 Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'speed_1_supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 2 supply air flow rate during cooling operation',
                                       {'name': u'Speed 2 Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'speed_2_supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 3 supply air flow rate during cooling operation',
                                       {'name': u'Speed 3 Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'speed_3_supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'speed 4 supply air flow rate during cooling operation',
                                       {'name': u'Speed 4 Supply Air Flow Rate During Cooling Operation',
                                        'pyname': u'speed_4_supply_air_flow_rate_during_cooling_operation',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Unitary Equipment',
               'min-fields': 31,
               'name': u'AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed',
               'pyname': u'AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def controlling_zone_or_thermostat_location(self):
        """field `Controlling Zone or Thermostat Location`

        Args:
            value (str): value for IDD Field `Controlling Zone or Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlling_zone_or_thermostat_location` or None if not set

        """
        return self["Controlling Zone or Thermostat Location"]

    @controlling_zone_or_thermostat_location.setter
    def controlling_zone_or_thermostat_location(self, value=None):
        """Corresponds to IDD field `Controlling Zone or Thermostat
        Location`"""
        self["Controlling Zone or Thermostat Location"] = value

    @property
    def supply_air_fan_object_type(self):
        """field `Supply Air Fan Object Type` Select the type of supply air fan
        used in this unitary system.

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
        """field `Supply Air Fan Name` Enter the name of the supply air fan
        used in this unitary system.

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
    def supply_air_fan_placement(self):
        """field `Supply Air Fan Placement` Select supply air fan placement as
        either BlowThrough or DrawThrough. BlowThrough means the supply air fan
        is located before the cooling coil. DrawThrough means the supply air
        fan is located after the heating coil but before the optional
        supplemental heating coil.

        Args:
            value (str): value for IDD Field `Supply Air Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_fan_placement` or None if not set

        """
        return self["Supply Air Fan Placement"]

    @supply_air_fan_placement.setter
    def supply_air_fan_placement(self, value=None):
        """Corresponds to IDD field `Supply Air Fan Placement`"""
        self["Supply Air Fan Placement"] = value

    @property
    def supply_air_fan_operating_mode_schedule_name(self):
        """field `Supply Air Fan Operating Mode Schedule Name`
        Enter the name of a schedule to control the supply air fan. Schedule values of zero
        mean that the supply air fan will cycle off if there is no cooling or heating load
        in the control zone. Non-zero schedule values mean that the supply air fan
        will operate continuously even if there is no cooling or heating load
        in the control zone. If this field is left blank, the supply air fan will
        operate continuously for the entire simulation period.

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
        """field `Heating Coil Object Type` Multi Speed DX, Electric, Gas, and
        Single speed Water and Steam coils.

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
    def minimum_outdoor_drybulb_temperature_for_compressor_operation(self):
        """field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`
        Needs to match the corresponding minimum outdoor temperature defined
        in the DX heating coil object.

        Args:
            value (float): value for IDD Field `Minimum Outdoor Dry-Bulb Temperature for Compressor Operation`
                Units: C
                Default value: -8.0

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
        Only works with Coil:Cooling:DX:MultiSpeed

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
        """field `Cooling Coil Name` Needs to match in the DX Cooling Coil
        object.

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
    def supplemental_heating_coil_object_type(self):
        """field `Supplemental Heating Coil Object Type` works with gas,
        electric, hot water and steam heating coils.

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
        """field `Supplemental Heating Coil Name` Needs to match in the
        supplemental heating coil object.

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

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Supply Air Temperature from Supplemental Heater`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_supply_air_temperature_from_supplemental_heater` or None if not set

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

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Supplemental Heater Operation`
                Units: C
                Default value: 21.0
                value <= 21.0

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
    def auxiliary_oncycle_electric_power(self):
        """field `Auxiliary On-Cycle Electric Power`

        Args:
            value (float): value for IDD Field `Auxiliary On-Cycle Electric Power`
                Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `auxiliary_oncycle_electric_power` or None if not set
        """
        return self["Auxiliary On-Cycle Electric Power"]

    @auxiliary_oncycle_electric_power.setter
    def auxiliary_oncycle_electric_power(self, value=None):
        """  Corresponds to IDD field `Auxiliary On-Cycle Electric Power`

        """
        self["Auxiliary On-Cycle Electric Power"] = value

    @property
    def auxiliary_offcycle_electric_power(self):
        """field `Auxiliary Off-Cycle Electric Power`

        Args:
            value (float): value for IDD Field `Auxiliary Off-Cycle Electric Power`
                Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `auxiliary_offcycle_electric_power` or None if not set
        """
        return self["Auxiliary Off-Cycle Electric Power"]

    @auxiliary_offcycle_electric_power.setter
    def auxiliary_offcycle_electric_power(self, value=None):
        """  Corresponds to IDD field `Auxiliary Off-Cycle Electric Power`

        """
        self["Auxiliary Off-Cycle Electric Power"] = value

    @property
    def design_heat_recovery_water_flow_rate(self):
        """field `Design Heat Recovery Water Flow Rate`
        If non-zero, then the heat recovery inlet and outlet node names must be entered.
        Used for heat recovery to an EnergyPlus plant loop.

        Args:
            value (float): value for IDD Field `Design Heat Recovery Water Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_heat_recovery_water_flow_rate` or None if not set
        """
        return self["Design Heat Recovery Water Flow Rate"]

    @design_heat_recovery_water_flow_rate.setter
    def design_heat_recovery_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Heat Recovery Water Flow Rate`"""
        self["Design Heat Recovery Water Flow Rate"] = value

    @property
    def maximum_temperature_for_heat_recovery(self):
        """field `Maximum Temperature for Heat Recovery`

        Args:
            value (float): value for IDD Field `Maximum Temperature for Heat Recovery`
                Units: C
                Default value: 80.0
                value <= 100.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_temperature_for_heat_recovery` or None if not set

        """
        return self["Maximum Temperature for Heat Recovery"]

    @maximum_temperature_for_heat_recovery.setter
    def maximum_temperature_for_heat_recovery(self, value=80.0):
        """Corresponds to IDD field `Maximum Temperature for Heat Recovery`"""
        self["Maximum Temperature for Heat Recovery"] = value

    @property
    def heat_recovery_water_inlet_node_name(self):
        """field `Heat Recovery Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Heat Recovery Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_water_inlet_node_name` or None if not set

        """
        return self["Heat Recovery Water Inlet Node Name"]

    @heat_recovery_water_inlet_node_name.setter
    def heat_recovery_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Water Inlet Node Name`"""
        self["Heat Recovery Water Inlet Node Name"] = value

    @property
    def heat_recovery_water_outlet_node_name(self):
        """field `Heat Recovery Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Heat Recovery Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_water_outlet_node_name` or None if not set

        """
        return self["Heat Recovery Water Outlet Node Name"]

    @heat_recovery_water_outlet_node_name.setter
    def heat_recovery_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Water Outlet Node Name`"""
        self["Heat Recovery Water Outlet Node Name"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(self):
        """field `Supply Air Flow Rate When No Cooling or Heating is Needed`
        Only used when the supply air fan operating mode is continuous (see
        field Supply Air Fan Operating Mode Schedule Name). This air flow rate
        is used when no heating or cooling is required and the coils are off.
        If this field is left blank or zero, the supply air flow rate from the
        previous on cycle (either cooling or heating) is used.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Needed`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_needed` or None if not set

        """
        return self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_needed.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_needed(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate When No Cooling or
        Heating is Needed`"""
        self[
            "Supply Air Flow Rate When No Cooling or Heating is Needed"] = value

    @property
    def number_of_speeds_for_heating(self):
        """field `Number of Speeds for Heating`
        Enter the number of the following sets of data for air flow rates.
        If Heating Coil Object Type is Coil:Heating:Water or Coil:Heating:Steam,
        this field should be 1.

        Args:
            value (int): value for IDD Field `Number of Speeds for Heating`
                value >= 1
                value <= 4

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_speeds_for_heating` or None if not set
        """
        return self["Number of Speeds for Heating"]

    @number_of_speeds_for_heating.setter
    def number_of_speeds_for_heating(self, value=None):
        """Corresponds to IDD field `Number of Speeds for Heating`"""
        self["Number of Speeds for Heating"] = value

    @property
    def number_of_speeds_for_cooling(self):
        """field `Number of Speeds for Cooling` Enter the number of the
        following sets of data for air flow rates.

        Args:
            value (int): value for IDD Field `Number of Speeds for Cooling`
                value >= 2
                value <= 4

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_speeds_for_cooling` or None if not set

        """
        return self["Number of Speeds for Cooling"]

    @number_of_speeds_for_cooling.setter
    def number_of_speeds_for_cooling(self, value=None):
        """Corresponds to IDD field `Number of Speeds for Cooling`"""
        self["Number of Speeds for Cooling"] = value

    @property
    def speed_1_supply_air_flow_rate_during_heating_operation(self):
        """field `Speed 1 Supply Air Flow Rate During Heating Operation` Enter
        the operating supply air flow rate during heating operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 1 Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_1_supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Speed 1 Supply Air Flow Rate During Heating Operation"]

    @speed_1_supply_air_flow_rate_during_heating_operation.setter
    def speed_1_supply_air_flow_rate_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 1 Supply Air Flow Rate During
        Heating Operation`"""
        self["Speed 1 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_2_supply_air_flow_rate_during_heating_operation(self):
        """field `Speed 2 Supply Air Flow Rate During Heating Operation` Enter
        the operating supply air flow rate during heating operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 2 Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_2_supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Speed 2 Supply Air Flow Rate During Heating Operation"]

    @speed_2_supply_air_flow_rate_during_heating_operation.setter
    def speed_2_supply_air_flow_rate_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 2 Supply Air Flow Rate During
        Heating Operation`"""
        self["Speed 2 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_3_supply_air_flow_rate_during_heating_operation(self):
        """field `Speed 3 Supply Air Flow Rate During Heating Operation` Enter
        the operating supply air flow rate during heating operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 3 Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_3_supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Speed 3 Supply Air Flow Rate During Heating Operation"]

    @speed_3_supply_air_flow_rate_during_heating_operation.setter
    def speed_3_supply_air_flow_rate_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 3 Supply Air Flow Rate During
        Heating Operation`"""
        self["Speed 3 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_4_supply_air_flow_rate_during_heating_operation(self):
        """field `Speed 4 Supply Air Flow Rate During Heating Operation` Enter
        the operating supply air flow rate during heating operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 4 Supply Air Flow Rate During Heating Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_4_supply_air_flow_rate_during_heating_operation` or None if not set

        """
        return self["Speed 4 Supply Air Flow Rate During Heating Operation"]

    @speed_4_supply_air_flow_rate_during_heating_operation.setter
    def speed_4_supply_air_flow_rate_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 4 Supply Air Flow Rate During
        Heating Operation`"""
        self["Speed 4 Supply Air Flow Rate During Heating Operation"] = value

    @property
    def speed_1_supply_air_flow_rate_during_cooling_operation(self):
        """field `Speed 1 Supply Air Flow Rate During Cooling Operation` Enter
        the operating supply air flow rate during cooling operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 1 Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_1_supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Speed 1 Supply Air Flow Rate During Cooling Operation"]

    @speed_1_supply_air_flow_rate_during_cooling_operation.setter
    def speed_1_supply_air_flow_rate_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 1 Supply Air Flow Rate During
        Cooling Operation`"""
        self["Speed 1 Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def speed_2_supply_air_flow_rate_during_cooling_operation(self):
        """field `Speed 2 Supply Air Flow Rate During Cooling Operation` Enter
        the operating supply air flow rate during cooling operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 2 Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_2_supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Speed 2 Supply Air Flow Rate During Cooling Operation"]

    @speed_2_supply_air_flow_rate_during_cooling_operation.setter
    def speed_2_supply_air_flow_rate_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 2 Supply Air Flow Rate During
        Cooling Operation`"""
        self["Speed 2 Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def speed_3_supply_air_flow_rate_during_cooling_operation(self):
        """field `Speed 3 Supply Air Flow Rate During Cooling Operation` Enter
        the operating supply air flow rate during cooling operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 3 Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_3_supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Speed 3 Supply Air Flow Rate During Cooling Operation"]

    @speed_3_supply_air_flow_rate_during_cooling_operation.setter
    def speed_3_supply_air_flow_rate_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 3 Supply Air Flow Rate During
        Cooling Operation`"""
        self["Speed 3 Supply Air Flow Rate During Cooling Operation"] = value

    @property
    def speed_4_supply_air_flow_rate_during_cooling_operation(self):
        """field `Speed 4 Supply Air Flow Rate During Cooling Operation` Enter
        the operating supply air flow rate during cooling operation or specify
        autosize.

        Args:
            value (float or "Autosize"): value for IDD Field `Speed 4 Supply Air Flow Rate During Cooling Operation`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `speed_4_supply_air_flow_rate_during_cooling_operation` or None if not set

        """
        return self["Speed 4 Supply Air Flow Rate During Cooling Operation"]

    @speed_4_supply_air_flow_rate_during_cooling_operation.setter
    def speed_4_supply_air_flow_rate_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Speed 4 Supply Air Flow Rate During
        Cooling Operation`"""
        self["Speed 4 Supply Air Flow Rate During Cooling Operation"] = value


