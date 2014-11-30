#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on a modified Energy+.idd specification file.

Do not expect (yet) that it actually works!

Generation date: 2014-11-30

"""
import re
from collections import OrderedDict
from internal_gains import *
from water_heaters_and_thermal_storage import *
from variable_refrigerant_flow_equipment import *
from condenser_equipment_and_heat_exchangers import *
from exterior_equipment import *
from energy_management_system import *
from schedules import *
from location_and_climate import *
from unitary_equipment import *
from zone_hvac_radiative import *
from external_interface import *
from performance_tables import *
from natural_ventilation_and_duct_leakage import *
from simulation_parameters import *
from performance_curves import *
from compliance_objects import *
from refrigeration import *
from advanced_construction import *
from daylighting import *
from node import *
from plant import *
from zone_hvac_forced_air_units import *
from zone_hvac_air_loop_terminal_units import *
from surface_construction_elements import *
from zone_hvac_equipment_connections import *
from setpoint_managers import *
from hvac_design_objects import *
from zone_airflow import *
from room_air_models import *
from user_defined_hvac_and_plant_component_models import *
from thermal_zones_and_surfaces import *
from system_availability_managers import *
from detailed_ground_heat_transfer import *
from air_distribution import *
from controllers import *
from energyplus import *


class IDF(object):
    """ Represens an EnergyPlus IDF input file
    """
    
    required_objects = []

    def __init__(self):
        """ Inits IDF with no data dictionary set."""
        self._data = OrderedDict()
        self._data["Lead Input"] = None
        self._data["Simulation Data"] = None
        self._data["Version"] = None
        self._data["SimulationControl"] = None
        self._data["Building"] = None
        self._data["ShadowCalculation"] = None
        self._data["SurfaceConvectionAlgorithm:Inside"] = None
        self._data["SurfaceConvectionAlgorithm:Outside"] = None
        self._data["HeatBalanceAlgorithm"] = None
        self._data["HeatBalanceSettings:ConductionFiniteDifference"] = None
        self._data["ZoneAirHeatBalanceAlgorithm"] = None
        self._data["ZoneAirContaminantBalance"] = None
        self._data["ZoneAirMassFlowConservation"] = None
        self._data["ZoneCapacitanceMultiplier:ResearchSpecial"] = None
        self._data["Timestep"] = None
        self._data["ConvergenceLimits"] = None
        self._data["ProgramControl"] = None
        self._data["Compliance:Building"] = None
        self._data["Site:Location"] = None
        self._data["SizingPeriod:DesignDay"] = None
        self._data["SizingPeriod:WeatherFileDays"] = None
        self._data["SizingPeriod:WeatherFileConditionType"] = None
        self._data["RunPeriod"] = None
        self._data["RunPeriod:CustomRange"] = None
        self._data["RunPeriodControl:SpecialDays"] = None
        self._data["RunPeriodControl:DaylightSavingTime"] = None
        self._data["WeatherProperty:SkyTemperature"] = None
        self._data["Site:WeatherStation"] = None
        self._data["Site:HeightVariation"] = None
        self._data["Site:GroundTemperature:BuildingSurface"] = None
        self._data["Site:GroundTemperature:FCfactorMethod"] = None
        self._data["Site:GroundTemperature:Shallow"] = None
        self._data["Site:GroundTemperature:Deep"] = None
        self._data["Site:GroundDomain"] = None
        self._data["Site:GroundReflectance"] = None
        self._data["Site:GroundReflectance:SnowModifier"] = None
        self._data["Site:WaterMainsTemperature"] = None
        self._data["Site:Precipitation"] = None
        self._data["RoofIrrigation"] = None
        self._data["Site:SolarAndVisibleSpectrum"] = None
        self._data["Site:SpectrumData"] = None
        self._data["ScheduleTypeLimits"] = None
        self._data["Schedule:Day:Hourly"] = None
        self._data["Schedule:Day:Interval"] = None
        self._data["Schedule:Week:Daily"] = None
        self._data["Schedule:Week:Compact"] = None
        self._data["Schedule:Constant"] = None
        self._data["Schedule:File"] = None
        self._data["Material"] = None
        self._data["Material:NoMass"] = None
        self._data["Material:InfraredTransparent"] = None
        self._data["Material:AirGap"] = None
        self._data["Material:RoofVegetation"] = None
        self._data["WindowMaterial:SimpleGlazingSystem"] = None
        self._data["WindowMaterial:Glazing"] = None
        self._data["WindowMaterial:GlazingGroup:Thermochromic"] = None
        self._data["WindowMaterial:Glazing:RefractionExtinctionMethod"] = None
        self._data["WindowMaterial:Gas"] = None
        self._data["WindowGap:SupportPillar"] = None
        self._data["WindowGap:DeflectionState"] = None
        self._data["WindowMaterial:GasMixture"] = None
        self._data["WindowMaterial:Gap"] = None
        self._data["WindowMaterial:Shade"] = None
        self._data["WindowMaterial:ComplexShade"] = None
        self._data["WindowMaterial:Blind"] = None
        self._data["WindowMaterial:Screen"] = None
        self._data["WindowMaterial:Shade:EquivalentLayer"] = None
        self._data["WindowMaterial:Drape:EquivalentLayer"] = None
        self._data["WindowMaterial:Blind:EquivalentLayer"] = None
        self._data["WindowMaterial:Screen:EquivalentLayer"] = None
        self._data["WindowMaterial:Glazing:EquivalentLayer"] = None
        self._data["Construction:WindowEquivalentLayer"] = None
        self._data["WindowMaterial:Gap:EquivalentLayer"] = None
        self._data["MaterialProperty:MoisturePenetrationDepth:Settings"] = None
        self._data["MaterialProperty:PhaseChange"] = None
        self._data["MaterialProperty:VariableThermalConductivity"] = None
        self._data["MaterialProperty:HeatAndMoistureTransfer:Settings"] = None
        self._data["MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm"] = None
        self._data["MaterialProperty:HeatAndMoistureTransfer:Suction"] = None
        self._data["MaterialProperty:HeatAndMoistureTransfer:Redistribution"] = None
        self._data["MaterialProperty:HeatAndMoistureTransfer:Diffusion"] = None
        self._data["MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity"] = None
        self._data["Construction"] = None
        self._data["Construction:CfactorUndergroundWall"] = None
        self._data["Construction:FfactorGroundFloor"] = None
        self._data["Construction:InternalSource"] = None
        self._data["WindowThermalModel:Params"] = None
        self._data["Construction:ComplexFenestrationState"] = None
        self._data["Construction:WindowDataFile"] = None
        self._data["GlobalGeometryRules"] = None
        self._data["GeometryTransform"] = None
        self._data["Zone"] = None
        self._data["ZoneGroup"] = None
        self._data["BuildingSurface:Detailed"] = None
        self._data["Wall:Detailed"] = None
        self._data["RoofCeiling:Detailed"] = None
        self._data["Floor:Detailed"] = None
        self._data["Wall:Exterior"] = None
        self._data["Wall:Adiabatic"] = None
        self._data["Wall:Underground"] = None
        self._data["Wall:Interzone"] = None
        self._data["Roof"] = None
        self._data["Ceiling:Adiabatic"] = None
        self._data["Ceiling:Interzone"] = None
        self._data["Floor:GroundContact"] = None
        self._data["Floor:Adiabatic"] = None
        self._data["Floor:Interzone"] = None
        self._data["FenestrationSurface:Detailed"] = None
        self._data["Window"] = None
        self._data["Door"] = None
        self._data["GlazedDoor"] = None
        self._data["Window:Interzone"] = None
        self._data["Door:Interzone"] = None
        self._data["GlazedDoor:Interzone"] = None
        self._data["WindowProperty:ShadingControl"] = None
        self._data["WindowProperty:FrameAndDivider"] = None
        self._data["WindowProperty:AirflowControl"] = None
        self._data["WindowProperty:StormWindow"] = None
        self._data["InternalMass"] = None
        self._data["Shading:Site"] = None
        self._data["Shading:Building"] = None
        self._data["Shading:Site:Detailed"] = None
        self._data["Shading:Building:Detailed"] = None
        self._data["Shading:Overhang"] = None
        self._data["Shading:Overhang:Projection"] = None
        self._data["Shading:Fin"] = None
        self._data["Shading:Fin:Projection"] = None
        self._data["Shading:Zone:Detailed"] = None
        self._data["ShadingProperty:Reflectance"] = None
        self._data["SurfaceProperty:HeatTransferAlgorithm"] = None
        self._data["SurfaceProperty:HeatTransferAlgorithm:MultipleSurface"] = None
        self._data["SurfaceProperty:HeatTransferAlgorithm:SurfaceList"] = None
        self._data["SurfaceProperty:HeatTransferAlgorithm:Construction"] = None
        self._data["SurfaceControl:MovableInsulation"] = None
        self._data["SurfaceProperty:OtherSideCoefficients"] = None
        self._data["SurfaceProperty:OtherSideConditionsModel"] = None
        self._data["SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections"] = None
        self._data["SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections"] = None
        self._data["SurfaceConvectionAlgorithm:Inside:UserCurve"] = None
        self._data["SurfaceConvectionAlgorithm:Outside:UserCurve"] = None
        self._data["SurfaceProperty:ConvectionCoefficients"] = None
        self._data["SurfaceProperty:ConvectionCoefficients:MultipleSurface"] = None
        self._data["SurfaceProperties:VaporCoefficients"] = None
        self._data["SurfaceProperty:ExteriorNaturalVentedCavity"] = None
        self._data["SurfaceProperty:SolarIncidentInside"] = None
        self._data["ComplexFenestrationProperty:SolarAbsorbedLayers"] = None
        self._data["ZoneProperty:UserViewFactors:bySurfaceName"] = None
        self._data["GroundHeatTransfer:Control"] = None
        self._data["GroundHeatTransfer:Slab:Materials"] = None
        self._data["GroundHeatTransfer:Slab:MatlProps"] = None
        self._data["GroundHeatTransfer:Slab:BoundConds"] = None
        self._data["GroundHeatTransfer:Slab:BldgProps"] = None
        self._data["GroundHeatTransfer:Slab:Insulation"] = None
        self._data["GroundHeatTransfer:Slab:EquivalentSlab"] = None
        self._data["GroundHeatTransfer:Slab:AutoGrid"] = None
        self._data["GroundHeatTransfer:Slab:ManualGrid"] = None
        self._data["GroundHeatTransfer:Basement:SimParameters"] = None
        self._data["GroundHeatTransfer:Basement:MatlProps"] = None
        self._data["GroundHeatTransfer:Basement:Insulation"] = None
        self._data["GroundHeatTransfer:Basement:SurfaceProps"] = None
        self._data["GroundHeatTransfer:Basement:BldgData"] = None
        self._data["GroundHeatTransfer:Basement:Interior"] = None
        self._data["GroundHeatTransfer:Basement:ComBldg"] = None
        self._data["GroundHeatTransfer:Basement:EquivSlab"] = None
        self._data["GroundHeatTransfer:Basement:EquivAutoGrid"] = None
        self._data["GroundHeatTransfer:Basement:AutoGrid"] = None
        self._data["GroundHeatTransfer:Basement:ManualGrid"] = None
        self._data["RoomAirModelType"] = None
        self._data["RoomAir:TemperaturePattern:UserDefined"] = None
        self._data["RoomAir:TemperaturePattern:ConstantGradient"] = None
        self._data["RoomAir:TemperaturePattern:TwoGradient"] = None
        self._data["RoomAir:TemperaturePattern:NondimensionalHeight"] = None
        self._data["RoomAir:TemperaturePattern:SurfaceMapping"] = None
        self._data["RoomAir:Node"] = None
        self._data["RoomAirSettings:OneNodeDisplacementVentilation"] = None
        self._data["RoomAirSettings:ThreeNodeDisplacementVentilation"] = None
        self._data["RoomAirSettings:CrossVentilation"] = None
        self._data["RoomAirSettings:UnderFloorAirDistributionInterior"] = None
        self._data["RoomAirSettings:UnderFloorAirDistributionExterior"] = None
        self._data["People"] = None
        self._data["ComfortViewFactorAngles"] = None
        self._data["Lights"] = None
        self._data["ElectricEquipment"] = None
        self._data["GasEquipment"] = None
        self._data["HotWaterEquipment"] = None
        self._data["SteamEquipment"] = None
        self._data["OtherEquipment"] = None
        self._data["ZoneBaseboard:OutdoorTemperatureControlled"] = None
        self._data["ZoneContaminantSourceAndSink:CarbonDioxide"] = None
        self._data["ZoneContaminantSourceAndSink:Generic:Constant"] = None
        self._data["SurfaceContaminantSourceAndSink:Generic:PressureDriven"] = None
        self._data["ZoneContaminantSourceAndSink:Generic:CutoffModel"] = None
        self._data["ZoneContaminantSourceAndSink:Generic:DecaySource"] = None
        self._data["SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"] = None
        self._data["SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"] = None
        self._data["ZoneContaminantSourceAndSink:Generic:DepositionRateSink"] = None
        self._data["Daylighting:Controls"] = None
        self._data["Daylighting:DELight:Controls"] = None
        self._data["Daylighting:DELight:ReferencePoint"] = None
        self._data["Daylighting:DELight:ComplexFenestration"] = None
        self._data["DaylightingDevice:Tubular"] = None
        self._data["DaylightingDevice:Shelf"] = None
        self._data["DaylightingDevice:LightWell"] = None
        self._data["Output:DaylightFactors"] = None
        self._data["Output:IlluminanceMap"] = None
        self._data["OutputControl:IlluminanceMap:Style"] = None
        self._data["ZoneInfiltration:DesignFlowRate"] = None
        self._data["ZoneInfiltration:EffectiveLeakageArea"] = None
        self._data["ZoneInfiltration:FlowCoefficient"] = None
        self._data["ZoneVentilation:DesignFlowRate"] = None
        self._data["ZoneVentilation:WindandStackOpenArea"] = None
        self._data["ZoneAirBalance:OutdoorAir"] = None
        self._data["ZoneMixing"] = None
        self._data["ZoneCrossMixing"] = None
        self._data["ZoneRefrigerationDoorMixing"] = None
        self._data["ZoneEarthtube"] = None
        self._data["ZoneCoolTower:Shower"] = None
        self._data["ZoneThermalChimney"] = None
        self._data["AirflowNetwork:SimulationControl"] = None
        self._data["AirflowNetwork:MultiZone:Zone"] = None
        self._data["AirflowNetwork:MultiZone:Surface"] = None
        self._data["AirflowNetwork:MultiZone:ReferenceCrackConditions"] = None
        self._data["AirflowNetwork:MultiZone:Surface:Crack"] = None
        self._data["AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea"] = None
        self._data["AirflowNetwork:MultiZone:Component:DetailedOpening"] = None
        self._data["AirflowNetwork:MultiZone:Component:SimpleOpening"] = None
        self._data["AirflowNetwork:MultiZone:Component:HorizontalOpening"] = None
        self._data["AirflowNetwork:MultiZone:Component:ZoneExhaustFan"] = None
        self._data["AirflowNetwork:MultiZone:ExternalNode"] = None
        self._data["AirflowNetwork:MultiZone:WindPressureCoefficientArray"] = None
        self._data["AirflowNetwork:MultiZone:WindPressureCoefficientValues"] = None
        self._data["AirflowNetwork:Distribution:Node"] = None
        self._data["AirflowNetwork:Distribution:Component:Leak"] = None
        self._data["AirflowNetwork:Distribution:Component:LeakageRatio"] = None
        self._data["AirflowNetwork:Distribution:Component:Duct"] = None
        self._data["AirflowNetwork:Distribution:Component:Fan"] = None
        self._data["AirflowNetwork:Distribution:Component:Coil"] = None
        self._data["AirflowNetwork:Distribution:Component:HeatExchanger"] = None
        self._data["AirflowNetwork:Distribution:Component:TerminalUnit"] = None
        self._data["AirflowNetwork:Distribution:Component:ConstantPressureDrop"] = None
        self._data["AirflowNetwork:Distribution:Linkage"] = None
        self._data["Exterior:Lights"] = None
        self._data["Exterior:FuelEquipment"] = None
        self._data["Exterior:WaterEquipment"] = None
        self._data["HVACTemplate:Thermostat"] = None
        self._data["HVACTemplate:Zone:IdealLoadsAirSystem"] = None
        self._data["HVACTemplate:Zone:BaseboardHeat"] = None
        self._data["HVACTemplate:Zone:FanCoil"] = None
        self._data["HVACTemplate:Zone:PTAC"] = None
        self._data["HVACTemplate:Zone:PTHP"] = None
        self._data["HVACTemplate:Zone:WaterToAirHeatPump"] = None
        self._data["HVACTemplate:Zone:VRF"] = None
        self._data["HVACTemplate:Zone:Unitary"] = None
        self._data["HVACTemplate:Zone:VAV"] = None
        self._data["HVACTemplate:Zone:VAV:FanPowered"] = None
        self._data["HVACTemplate:Zone:VAV:HeatAndCool"] = None
        self._data["HVACTemplate:Zone:ConstantVolume"] = None
        self._data["HVACTemplate:Zone:DualDuct"] = None
        self._data["HVACTemplate:System:VRF"] = None
        self._data["HVACTemplate:System:Unitary"] = None
        self._data["HVACTemplate:System:UnitaryHeatPump:AirToAir"] = None
        self._data["HVACTemplate:System:UnitarySystem"] = None
        self._data["HVACTemplate:System:VAV"] = None
        self._data["HVACTemplate:System:PackagedVAV"] = None
        self._data["HVACTemplate:System:ConstantVolume"] = None
        self._data["HVACTemplate:System:DualDuct"] = None
        self._data["HVACTemplate:System:DedicatedOutdoorAir"] = None
        self._data["HVACTemplate:Plant:ChilledWaterLoop"] = None
        self._data["HVACTemplate:Plant:Chiller"] = None
        self._data["HVACTemplate:Plant:Chiller:ObjectReference"] = None
        self._data["HVACTemplate:Plant:Tower"] = None
        self._data["HVACTemplate:Plant:Tower:ObjectReference"] = None
        self._data["HVACTemplate:Plant:HotWaterLoop"] = None
        self._data["HVACTemplate:Plant:Boiler"] = None
        self._data["HVACTemplate:Plant:Boiler:ObjectReference"] = None
        self._data["HVACTemplate:Plant:MixedWaterLoop"] = None
        self._data["DesignSpecification:OutdoorAir"] = None
        self._data["DesignSpecification:ZoneAirDistribution"] = None
        self._data["Sizing:Parameters"] = None
        self._data["Sizing:Zone"] = None
        self._data["DesignSpecification:ZoneHVAC:Sizing"] = None
        self._data["Sizing:System"] = None
        self._data["Sizing:Plant"] = None
        self._data["OutputControl:Sizing:Style"] = None
        self._data["ZoneControl:Humidistat"] = None
        self._data["ZoneControl:Thermostat"] = None
        self._data["ZoneControl:Thermostat:OperativeTemperature"] = None
        self._data["ZoneControl:Thermostat:ThermalComfort"] = None
        self._data["ZoneControl:Thermostat:TemperatureAndHumidity"] = None
        self._data["ThermostatSetpoint:SingleHeating"] = None
        self._data["ThermostatSetpoint:SingleCooling"] = None
        self._data["ThermostatSetpoint:SingleHeatingOrCooling"] = None
        self._data["ThermostatSetpoint:DualSetpoint"] = None
        self._data["ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"] = None
        self._data["ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"] = None
        self._data["ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"] = None
        self._data["ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"] = None
        self._data["ZoneControl:Thermostat:StagedDualSetpoint"] = None
        self._data["ZoneControl:ContaminantController"] = None
        self._data["ZoneHVAC:IdealLoadsAirSystem"] = None
        self._data["ZoneHVAC:FourPipeFanCoil"] = None
        self._data["ZoneHVAC:WindowAirConditioner"] = None
        self._data["ZoneHVAC:PackagedTerminalAirConditioner"] = None
        self._data["ZoneHVAC:PackagedTerminalHeatPump"] = None
        self._data["ZoneHVAC:WaterToAirHeatPump"] = None
        self._data["ZoneHVAC:Dehumidifier:DX"] = None
        self._data["ZoneHVAC:EnergyRecoveryVentilator"] = None
        self._data["ZoneHVAC:EnergyRecoveryVentilator:Controller"] = None
        self._data["ZoneHVAC:UnitVentilator"] = None
        self._data["ZoneHVAC:UnitHeater"] = None
        self._data["ZoneHVAC:EvaporativeCoolerUnit"] = None
        self._data["ZoneHVAC:OutdoorAirUnit"] = None
        self._data["ZoneHVAC:OutdoorAirUnit:EquipmentList"] = None
        self._data["ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"] = None
        self._data["ZoneHVAC:Baseboard:RadiantConvective:Water"] = None
        self._data["ZoneHVAC:Baseboard:RadiantConvective:Steam"] = None
        self._data["ZoneHVAC:Baseboard:RadiantConvective:Electric"] = None
        self._data["ZoneHVAC:Baseboard:Convective:Water"] = None
        self._data["ZoneHVAC:Baseboard:Convective:Electric"] = None
        self._data["ZoneHVAC:LowTemperatureRadiant:VariableFlow"] = None
        self._data["ZoneHVAC:LowTemperatureRadiant:ConstantFlow"] = None
        self._data["ZoneHVAC:LowTemperatureRadiant:Electric"] = None
        self._data["ZoneHVAC:LowTemperatureRadiant:SurfaceGroup"] = None
        self._data["ZoneHVAC:HighTemperatureRadiant"] = None
        self._data["ZoneHVAC:VentilatedSlab"] = None
        self._data["ZoneHVAC:VentilatedSlab:SlabGroup"] = None
        self._data["AirTerminal:SingleDuct:Uncontrolled"] = None
        self._data["AirTerminal:SingleDuct:ConstantVolume:Reheat"] = None
        self._data["AirTerminal:SingleDuct:VAV:NoReheat"] = None
        self._data["AirTerminal:SingleDuct:VAV:Reheat"] = None
        self._data["AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan"] = None
        self._data["AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"] = None
        self._data["AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"] = None
        self._data["AirTerminal:SingleDuct:SeriesPIU:Reheat"] = None
        self._data["AirTerminal:SingleDuct:ParallelPIU:Reheat"] = None
        self._data["AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"] = None
        self._data["AirTerminal:SingleDuct:ConstantVolume:CooledBeam"] = None
        self._data["AirTerminal:SingleDuct:InletSideMixer"] = None
        self._data["AirTerminal:SingleDuct:SupplySideMixer"] = None
        self._data["AirTerminal:DualDuct:ConstantVolume"] = None
        self._data["AirTerminal:DualDuct:VAV"] = None
        self._data["AirTerminal:DualDuct:VAV:OutdoorAir"] = None
        self._data["ZoneHVAC:AirDistributionUnit"] = None
        self._data["ZoneHVAC:EquipmentList"] = None
        self._data["ZoneHVAC:EquipmentConnections"] = None
        self._data["Fan:ConstantVolume"] = None
        self._data["Fan:VariableVolume"] = None
        self._data["Fan:OnOff"] = None
        self._data["Fan:ZoneExhaust"] = None
        self._data["FanPerformance:NightVentilation"] = None
        self._data["Fan:ComponentModel"] = None
        self._data["Coil:Cooling:Water"] = None
        self._data["Coil:Cooling:Water:DetailedGeometry"] = None
        self._data["Coil:Cooling:DX:SingleSpeed"] = None
        self._data["Coil:Cooling:DX:TwoSpeed"] = None
        self._data["Coil:Cooling:DX:MultiSpeed"] = None
        self._data["Coil:Cooling:DX:VariableSpeed"] = None
        self._data["Coil:Cooling:DX:TwoStageWithHumidityControlMode"] = None
        self._data["CoilPerformance:DX:Cooling"] = None
        self._data["Coil:Cooling:DX:VariableRefrigerantFlow"] = None
        self._data["Coil:Heating:DX:VariableRefrigerantFlow"] = None
        self._data["Coil:Heating:Water"] = None
        self._data["Coil:Heating:Steam"] = None
        self._data["Coil:Heating:Electric"] = None
        self._data["Coil:Heating:Electric:MultiStage"] = None
        self._data["Coil:Heating:Gas"] = None
        self._data["Coil:Heating:Gas:MultiStage"] = None
        self._data["Coil:Heating:Desuperheater"] = None
        self._data["Coil:Heating:DX:SingleSpeed"] = None
        self._data["Coil:Heating:DX:MultiSpeed"] = None
        self._data["Coil:Heating:DX:VariableSpeed"] = None
        self._data["Coil:Cooling:WaterToAirHeatPump:ParameterEstimation"] = None
        self._data["Coil:Heating:WaterToAirHeatPump:ParameterEstimation"] = None
        self._data["Coil:Cooling:WaterToAirHeatPump:EquationFit"] = None
        self._data["Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit"] = None
        self._data["Coil:Heating:WaterToAirHeatPump:EquationFit"] = None
        self._data["Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit"] = None
        self._data["Coil:WaterHeating:AirToWaterHeatPump"] = None
        self._data["Coil:WaterHeating:Desuperheater"] = None
        self._data["CoilSystem:Cooling:DX"] = None
        self._data["CoilSystem:Heating:DX"] = None
        self._data["CoilSystem:Cooling:Water:HeatExchangerAssisted"] = None
        self._data["CoilSystem:Cooling:DX:HeatExchangerAssisted"] = None
        self._data["Coil:Cooling:DX:SingleSpeed:ThermalStorage"] = None
        self._data["Humidifier:Steam:Electric"] = None
        self._data["Dehumidifier:Desiccant:NoFans"] = None
        self._data["Dehumidifier:Desiccant:System"] = None
        self._data["HeatExchanger:AirToAir:FlatPlate"] = None
        self._data["HeatExchanger:AirToAir:SensibleAndLatent"] = None
        self._data["HeatExchanger:Desiccant:BalancedFlow"] = None
        self._data["HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"] = None
        self._data["AirLoopHVAC:UnitarySystem"] = None
        self._data["UnitarySystemPerformance:HeatPump:Multispeed"] = None
        self._data["AirLoopHVAC:Unitary:Furnace:HeatOnly"] = None
        self._data["AirLoopHVAC:Unitary:Furnace:HeatCool"] = None
        self._data["AirLoopHVAC:UnitaryHeatOnly"] = None
        self._data["AirLoopHVAC:UnitaryHeatCool"] = None
        self._data["AirLoopHVAC:UnitaryHeatPump:AirToAir"] = None
        self._data["AirLoopHVAC:UnitaryHeatPump:WaterToAir"] = None
        self._data["AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass"] = None
        self._data["AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed"] = None
        self._data["AirConditioner:VariableRefrigerantFlow"] = None
        self._data["ZoneTerminalUnitList"] = None
        self._data["Controller:WaterCoil"] = None
        self._data["Controller:OutdoorAir"] = None
        self._data["Controller:MechanicalVentilation"] = None
        self._data["AirLoopHVAC:ControllerList"] = None
        self._data["AirLoopHVAC"] = None
        self._data["AirLoopHVAC:OutdoorAirSystem:EquipmentList"] = None
        self._data["AirLoopHVAC:OutdoorAirSystem"] = None
        self._data["OutdoorAir:Mixer"] = None
        self._data["AirLoopHVAC:SupplyPath"] = None
        self._data["AirLoopHVAC:ReturnPath"] = None
        self._data["Branch"] = None
        self._data["ConnectorList"] = None
        self._data["OutdoorAir:Node"] = None
        self._data["Pipe:Adiabatic"] = None
        self._data["Pipe:Adiabatic:Steam"] = None
        self._data["Pipe:Indoor"] = None
        self._data["Pipe:Outdoor"] = None
        self._data["Pipe:Underground"] = None
        self._data["PipingSystem:Underground:Domain"] = None
        self._data["PipingSystem:Underground:PipeCircuit"] = None
        self._data["PipingSystem:Underground:PipeSegment"] = None
        self._data["Duct"] = None
        self._data["Pump:VariableSpeed"] = None
        self._data["Pump:ConstantSpeed"] = None
        self._data["Pump:VariableSpeed:Condensate"] = None
        self._data["HeaderedPumps:ConstantSpeed"] = None
        self._data["TemperingValve"] = None
        self._data["LoadProfile:Plant"] = None
        self._data["SolarCollectorPerformance:FlatPlate"] = None
        self._data["SolarCollector:FlatPlate:Water"] = None
        self._data["SolarCollectorPerformance:PhotovoltaicThermal:Simple"] = None
        self._data["SolarCollector:IntegralCollectorStorage"] = None
        self._data["SolarCollectorPerformance:IntegralCollectorStorage"] = None
        self._data["SolarCollector:UnglazedTranspired"] = None
        self._data["SolarCollector:UnglazedTranspired:Multisystem"] = None
        self._data["Boiler:HotWater"] = None
        self._data["Boiler:Steam"] = None
        self._data["Chiller:Electric:EIR"] = None
        self._data["Chiller:Electric:ReformulatedEIR"] = None
        self._data["Chiller:Electric"] = None
        self._data["Chiller:Absorption:Indirect"] = None
        self._data["Chiller:Absorption"] = None
        self._data["Chiller:ConstantCOP"] = None
        self._data["Chiller:EngineDriven"] = None
        self._data["Chiller:CombustionTurbine"] = None
        self._data["ChillerHeater:Absorption:DirectFired"] = None
        self._data["ChillerHeater:Absorption:DoubleEffect"] = None
        self._data["HeatPump:WaterToWater:EquationFit:Heating"] = None
        self._data["HeatPump:WaterToWater:EquationFit:Cooling"] = None
        self._data["HeatPump:WaterToWater:ParameterEstimation:Cooling"] = None
        self._data["HeatPump:WaterToWater:ParameterEstimation:Heating"] = None
        self._data["DistrictCooling"] = None
        self._data["DistrictHeating"] = None
        self._data["PlantComponent:TemperatureSource"] = None
        self._data["CentralHeatPumpSystem"] = None
        self._data["ChillerHeaterPerformance:Electric:EIR"] = None
        self._data["CoolingTower:SingleSpeed"] = None
        self._data["CoolingTower:TwoSpeed"] = None
        self._data["CoolingTower:VariableSpeed:Merkel"] = None
        self._data["CoolingTower:VariableSpeed"] = None
        self._data["CoolingTowerPerformance:CoolTools"] = None
        self._data["CoolingTowerPerformance:YorkCalc"] = None
        self._data["EvaporativeFluidCooler:SingleSpeed"] = None
        self._data["EvaporativeFluidCooler:TwoSpeed"] = None
        self._data["FluidCooler:SingleSpeed"] = None
        self._data["FluidCooler:TwoSpeed"] = None
        self._data["GroundHeatExchanger:Vertical"] = None
        self._data["GroundHeatExchanger:Pond"] = None
        self._data["GroundHeatExchanger:Surface"] = None
        self._data["GroundHeatExchanger:HorizontalTrench"] = None
        self._data["HeatExchanger:FluidToFluid"] = None
        self._data["WaterHeater:Mixed"] = None
        self._data["WaterHeater:Stratified"] = None
        self._data["WaterHeater:Sizing"] = None
        self._data["WaterHeater:HeatPump"] = None
        self._data["ThermalStorage:Ice:Simple"] = None
        self._data["ThermalStorage:Ice:Detailed"] = None
        self._data["ThermalStorage:ChilledWater:Mixed"] = None
        self._data["ThermalStorage:ChilledWater:Stratified"] = None
        self._data["PlantLoop"] = None
        self._data["CondenserLoop"] = None
        self._data["PlantEquipmentList"] = None
        self._data["CondenserEquipmentList"] = None
        self._data["PlantEquipmentOperation:Uncontrolled"] = None
        self._data["PlantEquipmentOperation:CoolingLoad"] = None
        self._data["PlantEquipmentOperation:HeatingLoad"] = None
        self._data["PlantEquipmentOperation:OutdoorDryBulb"] = None
        self._data["PlantEquipmentOperation:OutdoorWetBulb"] = None
        self._data["PlantEquipmentOperation:OutdoorRelativeHumidity"] = None
        self._data["PlantEquipmentOperation:OutdoorDewpoint"] = None
        self._data["PlantEquipmentOperation:ComponentSetpoint"] = None
        self._data["PlantEquipmentOperation:OutdoorDryBulbDifference"] = None
        self._data["PlantEquipmentOperation:OutdoorWetBulbDifference"] = None
        self._data["PlantEquipmentOperation:OutdoorDewpointDifference"] = None
        self._data["PlantEquipmentOperationSchemes"] = None
        self._data["CondenserEquipmentOperationSchemes"] = None
        self._data["EnergyManagementSystem:Sensor"] = None
        self._data["EnergyManagementSystem:Actuator"] = None
        self._data["EnergyManagementSystem:ProgramCallingManager"] = None
        self._data["EnergyManagementSystem:OutputVariable"] = None
        self._data["EnergyManagementSystem:MeteredOutputVariable"] = None
        self._data["EnergyManagementSystem:TrendVariable"] = None
        self._data["EnergyManagementSystem:InternalVariable"] = None
        self._data["EnergyManagementSystem:CurveOrTableIndexVariable"] = None
        self._data["EnergyManagementSystem:ConstructionIndexVariable"] = None
        self._data["ExternalInterface"] = None
        self._data["ExternalInterface:Schedule"] = None
        self._data["ExternalInterface:Variable"] = None
        self._data["ExternalInterface:Actuator"] = None
        self._data["ExternalInterface:FunctionalMockupUnitImport"] = None
        self._data["ExternalInterface:FunctionalMockupUnitImport:From:Variable"] = None
        self._data["ExternalInterface:FunctionalMockupUnitImport:To:Schedule"] = None
        self._data["ExternalInterface:FunctionalMockupUnitImport:To:Actuator"] = None
        self._data["ExternalInterface:FunctionalMockupUnitImport:To:Variable"] = None
        self._data["ExternalInterface:FunctionalMockupUnitExport:From:Variable"] = None
        self._data["ExternalInterface:FunctionalMockupUnitExport:To:Schedule"] = None
        self._data["ExternalInterface:FunctionalMockupUnitExport:To:Actuator"] = None
        self._data["ExternalInterface:FunctionalMockupUnitExport:To:Variable"] = None
        self._data["ZoneHVAC:ForcedAir:UserDefined"] = None
        self._data["AirTerminal:SingleDuct:UserDefined"] = None
        self._data["Coil:UserDefined"] = None
        self._data["PlantComponent:UserDefined"] = None
        self._data["PlantEquipmentOperation:UserDefined"] = None
        self._data["AvailabilityManager:Scheduled"] = None
        self._data["AvailabilityManager:ScheduledOn"] = None
        self._data["AvailabilityManager:ScheduledOff"] = None
        self._data["AvailabilityManager:OptimumStart"] = None
        self._data["AvailabilityManager:NightCycle"] = None
        self._data["AvailabilityManager:DifferentialThermostat"] = None
        self._data["AvailabilityManager:HighTemperatureTurnOff"] = None
        self._data["AvailabilityManager:HighTemperatureTurnOn"] = None
        self._data["AvailabilityManager:LowTemperatureTurnOff"] = None
        self._data["AvailabilityManager:LowTemperatureTurnOn"] = None
        self._data["AvailabilityManager:NightVentilation"] = None
        self._data["AvailabilityManager:HybridVentilation"] = None
        self._data["AvailabilityManagerAssignmentList"] = None
        self._data["SetpointManager:Scheduled"] = None
        self._data["SetpointManager:Scheduled:DualSetpoint"] = None
        self._data["SetpointManager:OutdoorAirReset"] = None
        self._data["SetpointManager:SingleZone:Reheat"] = None
        self._data["SetpointManager:SingleZone:Heating"] = None
        self._data["SetpointManager:SingleZone:Cooling"] = None
        self._data["SetpointManager:SingleZone:Humidity:Minimum"] = None
        self._data["SetpointManager:SingleZone:Humidity:Maximum"] = None
        self._data["SetpointManager:MixedAir"] = None
        self._data["SetpointManager:OutdoorAirPretreat"] = None
        self._data["SetpointManager:Warmest"] = None
        self._data["SetpointManager:Coldest"] = None
        self._data["SetpointManager:ReturnAirBypassFlow"] = None
        self._data["SetpointManager:WarmestTemperatureFlow"] = None
        self._data["SetpointManager:MultiZone:Heating:Average"] = None
        self._data["SetpointManager:MultiZone:Cooling:Average"] = None
        self._data["SetpointManager:MultiZone:MinimumHumidity:Average"] = None
        self._data["SetpointManager:MultiZone:MaximumHumidity:Average"] = None
        self._data["SetpointManager:MultiZone:Humidity:Minimum"] = None
        self._data["SetpointManager:MultiZone:Humidity:Maximum"] = None
        self._data["SetpointManager:FollowOutdoorAirTemperature"] = None
        self._data["SetpointManager:FollowSystemNodeTemperature"] = None
        self._data["SetpointManager:FollowGroundTemperature"] = None
        self._data["SetpointManager:CondenserEnteringReset"] = None
        self._data["SetpointManager:CondenserEnteringReset:Ideal"] = None
        self._data["SetpointManager:SingleZone:OneStageCooling"] = None
        self._data["SetpointManager:SingleZone:OneStageHeating"] = None
        self._data["Refrigeration:Case"] = None
        self._data["Refrigeration:CompressorRack"] = None
        self._data["Refrigeration:CaseAndWalkInList"] = None
        self._data["Refrigeration:Condenser:AirCooled"] = None
        self._data["Refrigeration:Condenser:EvaporativeCooled"] = None
        self._data["Refrigeration:Condenser:WaterCooled"] = None
        self._data["Refrigeration:Condenser:Cascade"] = None
        self._data["Refrigeration:GasCooler:AirCooled"] = None
        self._data["Refrigeration:TransferLoadList"] = None
        self._data["Refrigeration:Subcooler"] = None
        self._data["Refrigeration:Compressor"] = None
        self._data["Refrigeration:CompressorList"] = None
        self._data["Refrigeration:System"] = None
        self._data["Refrigeration:TranscriticalSystem"] = None
        self._data["Refrigeration:SecondarySystem"] = None
        self._data["Refrigeration:WalkIn"] = None
        self._data["Refrigeration:AirChiller"] = None
        self._data["DemandManagerAssignmentList"] = None
        self._data["DemandManager:ExteriorLights"] = None
        self._data["DemandManager:Lights"] = None
        self._data["DemandManager:ElectricEquipment"] = None
        self._data["DemandManager:Thermostats"] = None
        self._data["Generator:InternalCombustionEngine"] = None
        self._data["Generator:CombustionTurbine"] = None
        self._data["Generator:MicroTurbine"] = None
        self._data["Generator:Photovoltaic"] = None
        self._data["PhotovoltaicPerformance:Simple"] = None
        self._data["PhotovoltaicPerformance:EquivalentOne-Diode"] = None
        self._data["PhotovoltaicPerformance:Sandia"] = None
        self._data["Generator:FuelCell"] = None
        self._data["Generator:FuelCell:PowerModule"] = None
        self._data["Generator:FuelCell:AirSupply"] = None
        self._data["Generator:FuelCell:WaterSupply"] = None
        self._data["Generator:FuelCell:AuxiliaryHeater"] = None
        self._data["Generator:FuelCell:ExhaustGasToWaterHeatExchanger"] = None
        self._data["Generator:FuelCell:ElectricalStorage"] = None
        self._data["Generator:FuelCell:Inverter"] = None
        self._data["Generator:FuelCell:StackCooler"] = None
        self._data["Generator:MicroCHP"] = None
        self._data["Generator:MicroCHP:NonNormalizedParameters"] = None
        self._data["Generator:FuelSupply"] = None
        self._data["Generator:WindTurbine"] = None
        self._data["ElectricLoadCenter:Generators"] = None
        self._data["ElectricLoadCenter:Inverter:Simple"] = None
        self._data["ElectricLoadCenter:Inverter:FunctionOfPower"] = None
        self._data["ElectricLoadCenter:Inverter:LookUpTable"] = None
        self._data["ElectricLoadCenter:Storage:Simple"] = None
        self._data["ElectricLoadCenter:Storage:Battery"] = None
        self._data["ElectricLoadCenter:Transformer"] = None
        self._data["ElectricLoadCenter:Distribution"] = None
        self._data["WaterUse:Equipment"] = None
        self._data["WaterUse:Connections"] = None
        self._data["WaterUse:Storage"] = None
        self._data["WaterUse:Well"] = None
        self._data["WaterUse:RainCollector"] = None
        self._data["FaultModel:TemperatureSensorOffset:OutdoorAir"] = None
        self._data["FaultModel:HumiditySensorOffset:OutdoorAir"] = None
        self._data["FaultModel:EnthalpySensorOffset:OutdoorAir"] = None
        self._data["FaultModel:PressureSensorOffset:OutdoorAir"] = None
        self._data["FaultModel:TemperatureSensorOffset:ReturnAir"] = None
        self._data["FaultModel:EnthalpySensorOffset:ReturnAir"] = None
        self._data["FaultModel:Fouling:Coil"] = None
        self._data["Curve:Linear"] = None
        self._data["Curve:QuadLinear"] = None
        self._data["Curve:Quadratic"] = None
        self._data["Curve:Cubic"] = None
        self._data["Curve:Quartic"] = None
        self._data["Curve:Exponent"] = None
        self._data["Curve:Bicubic"] = None
        self._data["Curve:Biquadratic"] = None
        self._data["Curve:QuadraticLinear"] = None
        self._data["Curve:Triquadratic"] = None
        self._data["Curve:Functional:PressureDrop"] = None
        self._data["Curve:FanPressureRise"] = None
        self._data["Curve:ExponentialSkewNormal"] = None
        self._data["Curve:Sigmoid"] = None
        self._data["Curve:RectangularHyperbola1"] = None
        self._data["Curve:RectangularHyperbola2"] = None
        self._data["Curve:ExponentialDecay"] = None
        self._data["Curve:DoubleExponentialDecay"] = None
        self._data["FluidProperties:Name"] = None
        self._data["FluidProperties:GlycolConcentration"] = None
        self._data["FluidProperties:Temperatures"] = None
        self._data["FluidProperties:Saturated"] = None
        self._data["FluidProperties:Superheated"] = None
        self._data["FluidProperties:Concentration"] = None
        self._data["CurrencyType"] = None
        self._data["ComponentCost:Adjustments"] = None
        self._data["ComponentCost:Reference"] = None
        self._data["ComponentCost:LineItem"] = None
        self._data["UtilityCost:Tariff"] = None
        self._data["UtilityCost:Qualify"] = None
        self._data["UtilityCost:Charge:Simple"] = None
        self._data["UtilityCost:Charge:Block"] = None
        self._data["UtilityCost:Ratchet"] = None
        self._data["UtilityCost:Variable"] = None
        self._data["UtilityCost:Computation"] = None
        self._data["LifeCycleCost:Parameters"] = None
        self._data["LifeCycleCost:RecurringCosts"] = None
        self._data["LifeCycleCost:NonrecurringCost"] = None
        self._data["LifeCycleCost:UsePriceEscalation"] = None
        self._data["LifeCycleCost:UseAdjustment"] = None
        self._data["Parametric:SetValueForRun"] = None
        self._data["Parametric:Logic"] = None
        self._data["Parametric:RunControl"] = None
        self._data["Parametric:FileNameSuffix"] = None
        self._data["Output:VariableDictionary"] = None
        self._data["Output:Surfaces:List"] = None
        self._data["Output:Surfaces:Drawing"] = None
        self._data["Output:Schedules"] = None
        self._data["Output:Constructions"] = None
        self._data["Output:EnergyManagementSystem"] = None
        self._data["OutputControl:SurfaceColorScheme"] = None
        self._data["Output:Table:SummaryReports"] = None
        self._data["Output:Table:TimeBins"] = None
        self._data["Output:Table:Monthly"] = None
        self._data["OutputControl:Table:Style"] = None
        self._data["OutputControl:ReportingTolerances"] = None
        self._data["Output:Variable"] = None
        self._data["Output:Meter"] = None
        self._data["Output:Meter:MeterFileOnly"] = None
        self._data["Output:Meter:Cumulative"] = None
        self._data["Output:Meter:Cumulative:MeterFileOnly"] = None
        self._data["Meter:Custom"] = None
        self._data["Meter:CustomDecrement"] = None
        self._data["Output:SQLite"] = None
        self._data["Output:EnvironmentalImpactFactors"] = None
        self._data["EnvironmentalImpactFactors"] = None
        self._data["FuelFactors"] = None
        self._data["Output:Diagnostics"] = None
        self._data["Output:DebuggingData"] = None
        self._data["Output:PreprocessorMessage"] = None


    def set(self, data):
        self._data[data.internal_name] = data        
   

    def save(self, path, check=True):
        """ Save data to path
        
            Args:
                path (str): path where data should be saved
        """
        with open(path, 'w') as f:
            if check:
                for key in self._data:
                    if self._data[key] is None and key in self.required_objects:
                        raise ValueError('{} is not valid.'.format(key))
            for key in self._data:
                if self._data[key] is not None:
                    f.write(self._data[key].export() + "\n")

    @classmethod
    def _create_datadict(cls, internal_name):
        """ Creates an object depending on `internal_name`
        
            Args:
                internal_name (str): IDD name
                
            Raises:
                ValueError: if `internal_name` cannot be matched to a data dictionary object
        """
        if internal_name == "Lead Input":
            return LeadInput()
        if internal_name == "Simulation Data":
            return SimulationData()
        if internal_name == "Version":
            return Version()
        if internal_name == "SimulationControl":
            return SimulationControl()
        if internal_name == "Building":
            return Building()
        if internal_name == "ShadowCalculation":
            return ShadowCalculation()
        if internal_name == "SurfaceConvectionAlgorithm:Inside":
            return SurfaceConvectionAlgorithmInside()
        if internal_name == "SurfaceConvectionAlgorithm:Outside":
            return SurfaceConvectionAlgorithmOutside()
        if internal_name == "HeatBalanceAlgorithm":
            return HeatBalanceAlgorithm()
        if internal_name == "HeatBalanceSettings:ConductionFiniteDifference":
            return HeatBalanceSettingsConductionFiniteDifference()
        if internal_name == "ZoneAirHeatBalanceAlgorithm":
            return ZoneAirHeatBalanceAlgorithm()
        if internal_name == "ZoneAirContaminantBalance":
            return ZoneAirContaminantBalance()
        if internal_name == "ZoneAirMassFlowConservation":
            return ZoneAirMassFlowConservation()
        if internal_name == "ZoneCapacitanceMultiplier:ResearchSpecial":
            return ZoneCapacitanceMultiplierResearchSpecial()
        if internal_name == "Timestep":
            return Timestep()
        if internal_name == "ConvergenceLimits":
            return ConvergenceLimits()
        if internal_name == "ProgramControl":
            return ProgramControl()
        if internal_name == "Compliance:Building":
            return ComplianceBuilding()
        if internal_name == "Site:Location":
            return SiteLocation()
        if internal_name == "SizingPeriod:DesignDay":
            return SizingPeriodDesignDay()
        if internal_name == "SizingPeriod:WeatherFileDays":
            return SizingPeriodWeatherFileDays()
        if internal_name == "SizingPeriod:WeatherFileConditionType":
            return SizingPeriodWeatherFileConditionType()
        if internal_name == "RunPeriod":
            return RunPeriod()
        if internal_name == "RunPeriod:CustomRange":
            return RunPeriodCustomRange()
        if internal_name == "RunPeriodControl:SpecialDays":
            return RunPeriodControlSpecialDays()
        if internal_name == "RunPeriodControl:DaylightSavingTime":
            return RunPeriodControlDaylightSavingTime()
        if internal_name == "WeatherProperty:SkyTemperature":
            return WeatherPropertySkyTemperature()
        if internal_name == "Site:WeatherStation":
            return SiteWeatherStation()
        if internal_name == "Site:HeightVariation":
            return SiteHeightVariation()
        if internal_name == "Site:GroundTemperature:BuildingSurface":
            return SiteGroundTemperatureBuildingSurface()
        if internal_name == "Site:GroundTemperature:FCfactorMethod":
            return SiteGroundTemperatureFcfactorMethod()
        if internal_name == "Site:GroundTemperature:Shallow":
            return SiteGroundTemperatureShallow()
        if internal_name == "Site:GroundTemperature:Deep":
            return SiteGroundTemperatureDeep()
        if internal_name == "Site:GroundDomain":
            return SiteGroundDomain()
        if internal_name == "Site:GroundReflectance":
            return SiteGroundReflectance()
        if internal_name == "Site:GroundReflectance:SnowModifier":
            return SiteGroundReflectanceSnowModifier()
        if internal_name == "Site:WaterMainsTemperature":
            return SiteWaterMainsTemperature()
        if internal_name == "Site:Precipitation":
            return SitePrecipitation()
        if internal_name == "RoofIrrigation":
            return RoofIrrigation()
        if internal_name == "Site:SolarAndVisibleSpectrum":
            return SiteSolarAndVisibleSpectrum()
        if internal_name == "Site:SpectrumData":
            return SiteSpectrumData()
        if internal_name == "ScheduleTypeLimits":
            return ScheduleTypeLimits()
        if internal_name == "Schedule:Day:Hourly":
            return ScheduleDayHourly()
        if internal_name == "Schedule:Day:Interval":
            return ScheduleDayInterval()
        if internal_name == "Schedule:Week:Daily":
            return ScheduleWeekDaily()
        if internal_name == "Schedule:Week:Compact":
            return ScheduleWeekCompact()
        if internal_name == "Schedule:Constant":
            return ScheduleConstant()
        if internal_name == "Schedule:File":
            return ScheduleFile()
        if internal_name == "Material":
            return Material()
        if internal_name == "Material:NoMass":
            return MaterialNoMass()
        if internal_name == "Material:InfraredTransparent":
            return MaterialInfraredTransparent()
        if internal_name == "Material:AirGap":
            return MaterialAirGap()
        if internal_name == "Material:RoofVegetation":
            return MaterialRoofVegetation()
        if internal_name == "WindowMaterial:SimpleGlazingSystem":
            return WindowMaterialSimpleGlazingSystem()
        if internal_name == "WindowMaterial:Glazing":
            return WindowMaterialGlazing()
        if internal_name == "WindowMaterial:GlazingGroup:Thermochromic":
            return WindowMaterialGlazingGroupThermochromic()
        if internal_name == "WindowMaterial:Glazing:RefractionExtinctionMethod":
            return WindowMaterialGlazingRefractionExtinctionMethod()
        if internal_name == "WindowMaterial:Gas":
            return WindowMaterialGas()
        if internal_name == "WindowGap:SupportPillar":
            return WindowGapSupportPillar()
        if internal_name == "WindowGap:DeflectionState":
            return WindowGapDeflectionState()
        if internal_name == "WindowMaterial:GasMixture":
            return WindowMaterialGasMixture()
        if internal_name == "WindowMaterial:Gap":
            return WindowMaterialGap()
        if internal_name == "WindowMaterial:Shade":
            return WindowMaterialShade()
        if internal_name == "WindowMaterial:ComplexShade":
            return WindowMaterialComplexShade()
        if internal_name == "WindowMaterial:Blind":
            return WindowMaterialBlind()
        if internal_name == "WindowMaterial:Screen":
            return WindowMaterialScreen()
        if internal_name == "WindowMaterial:Shade:EquivalentLayer":
            return WindowMaterialShadeEquivalentLayer()
        if internal_name == "WindowMaterial:Drape:EquivalentLayer":
            return WindowMaterialDrapeEquivalentLayer()
        if internal_name == "WindowMaterial:Blind:EquivalentLayer":
            return WindowMaterialBlindEquivalentLayer()
        if internal_name == "WindowMaterial:Screen:EquivalentLayer":
            return WindowMaterialScreenEquivalentLayer()
        if internal_name == "WindowMaterial:Glazing:EquivalentLayer":
            return WindowMaterialGlazingEquivalentLayer()
        if internal_name == "Construction:WindowEquivalentLayer":
            return ConstructionWindowEquivalentLayer()
        if internal_name == "WindowMaterial:Gap:EquivalentLayer":
            return WindowMaterialGapEquivalentLayer()
        if internal_name == "MaterialProperty:MoisturePenetrationDepth:Settings":
            return MaterialPropertyMoisturePenetrationDepthSettings()
        if internal_name == "MaterialProperty:PhaseChange":
            return MaterialPropertyPhaseChange()
        if internal_name == "MaterialProperty:VariableThermalConductivity":
            return MaterialPropertyVariableThermalConductivity()
        if internal_name == "MaterialProperty:HeatAndMoistureTransfer:Settings":
            return MaterialPropertyHeatAndMoistureTransferSettings()
        if internal_name == "MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm":
            return MaterialPropertyHeatAndMoistureTransferSorptionIsotherm()
        if internal_name == "MaterialProperty:HeatAndMoistureTransfer:Suction":
            return MaterialPropertyHeatAndMoistureTransferSuction()
        if internal_name == "MaterialProperty:HeatAndMoistureTransfer:Redistribution":
            return MaterialPropertyHeatAndMoistureTransferRedistribution()
        if internal_name == "MaterialProperty:HeatAndMoistureTransfer:Diffusion":
            return MaterialPropertyHeatAndMoistureTransferDiffusion()
        if internal_name == "MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity":
            return MaterialPropertyHeatAndMoistureTransferThermalConductivity()
        if internal_name == "Construction":
            return Construction()
        if internal_name == "Construction:CfactorUndergroundWall":
            return ConstructionCfactorUndergroundWall()
        if internal_name == "Construction:FfactorGroundFloor":
            return ConstructionFfactorGroundFloor()
        if internal_name == "Construction:InternalSource":
            return ConstructionInternalSource()
        if internal_name == "WindowThermalModel:Params":
            return WindowThermalModelParams()
        if internal_name == "Construction:ComplexFenestrationState":
            return ConstructionComplexFenestrationState()
        if internal_name == "Construction:WindowDataFile":
            return ConstructionWindowDataFile()
        if internal_name == "GlobalGeometryRules":
            return GlobalGeometryRules()
        if internal_name == "GeometryTransform":
            return GeometryTransform()
        if internal_name == "Zone":
            return Zone()
        if internal_name == "ZoneGroup":
            return ZoneGroup()
        if internal_name == "BuildingSurface:Detailed":
            return BuildingSurfaceDetailed()
        if internal_name == "Wall:Detailed":
            return WallDetailed()
        if internal_name == "RoofCeiling:Detailed":
            return RoofCeilingDetailed()
        if internal_name == "Floor:Detailed":
            return FloorDetailed()
        if internal_name == "Wall:Exterior":
            return WallExterior()
        if internal_name == "Wall:Adiabatic":
            return WallAdiabatic()
        if internal_name == "Wall:Underground":
            return WallUnderground()
        if internal_name == "Wall:Interzone":
            return WallInterzone()
        if internal_name == "Roof":
            return Roof()
        if internal_name == "Ceiling:Adiabatic":
            return CeilingAdiabatic()
        if internal_name == "Ceiling:Interzone":
            return CeilingInterzone()
        if internal_name == "Floor:GroundContact":
            return FloorGroundContact()
        if internal_name == "Floor:Adiabatic":
            return FloorAdiabatic()
        if internal_name == "Floor:Interzone":
            return FloorInterzone()
        if internal_name == "FenestrationSurface:Detailed":
            return FenestrationSurfaceDetailed()
        if internal_name == "Window":
            return Window()
        if internal_name == "Door":
            return Door()
        if internal_name == "GlazedDoor":
            return GlazedDoor()
        if internal_name == "Window:Interzone":
            return WindowInterzone()
        if internal_name == "Door:Interzone":
            return DoorInterzone()
        if internal_name == "GlazedDoor:Interzone":
            return GlazedDoorInterzone()
        if internal_name == "WindowProperty:ShadingControl":
            return WindowPropertyShadingControl()
        if internal_name == "WindowProperty:FrameAndDivider":
            return WindowPropertyFrameAndDivider()
        if internal_name == "WindowProperty:AirflowControl":
            return WindowPropertyAirflowControl()
        if internal_name == "WindowProperty:StormWindow":
            return WindowPropertyStormWindow()
        if internal_name == "InternalMass":
            return InternalMass()
        if internal_name == "Shading:Site":
            return ShadingSite()
        if internal_name == "Shading:Building":
            return ShadingBuilding()
        if internal_name == "Shading:Site:Detailed":
            return ShadingSiteDetailed()
        if internal_name == "Shading:Building:Detailed":
            return ShadingBuildingDetailed()
        if internal_name == "Shading:Overhang":
            return ShadingOverhang()
        if internal_name == "Shading:Overhang:Projection":
            return ShadingOverhangProjection()
        if internal_name == "Shading:Fin":
            return ShadingFin()
        if internal_name == "Shading:Fin:Projection":
            return ShadingFinProjection()
        if internal_name == "Shading:Zone:Detailed":
            return ShadingZoneDetailed()
        if internal_name == "ShadingProperty:Reflectance":
            return ShadingPropertyReflectance()
        if internal_name == "SurfaceProperty:HeatTransferAlgorithm":
            return SurfacePropertyHeatTransferAlgorithm()
        if internal_name == "SurfaceProperty:HeatTransferAlgorithm:MultipleSurface":
            return SurfacePropertyHeatTransferAlgorithmMultipleSurface()
        if internal_name == "SurfaceProperty:HeatTransferAlgorithm:SurfaceList":
            return SurfacePropertyHeatTransferAlgorithmSurfaceList()
        if internal_name == "SurfaceProperty:HeatTransferAlgorithm:Construction":
            return SurfacePropertyHeatTransferAlgorithmConstruction()
        if internal_name == "SurfaceControl:MovableInsulation":
            return SurfaceControlMovableInsulation()
        if internal_name == "SurfaceProperty:OtherSideCoefficients":
            return SurfacePropertyOtherSideCoefficients()
        if internal_name == "SurfaceProperty:OtherSideConditionsModel":
            return SurfacePropertyOtherSideConditionsModel()
        if internal_name == "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections":
            return SurfaceConvectionAlgorithmInsideAdaptiveModelSelections()
        if internal_name == "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections":
            return SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections()
        if internal_name == "SurfaceConvectionAlgorithm:Inside:UserCurve":
            return SurfaceConvectionAlgorithmInsideUserCurve()
        if internal_name == "SurfaceConvectionAlgorithm:Outside:UserCurve":
            return SurfaceConvectionAlgorithmOutsideUserCurve()
        if internal_name == "SurfaceProperty:ConvectionCoefficients":
            return SurfacePropertyConvectionCoefficients()
        if internal_name == "SurfaceProperty:ConvectionCoefficients:MultipleSurface":
            return SurfacePropertyConvectionCoefficientsMultipleSurface()
        if internal_name == "SurfaceProperties:VaporCoefficients":
            return SurfacePropertiesVaporCoefficients()
        if internal_name == "SurfaceProperty:ExteriorNaturalVentedCavity":
            return SurfacePropertyExteriorNaturalVentedCavity()
        if internal_name == "SurfaceProperty:SolarIncidentInside":
            return SurfacePropertySolarIncidentInside()
        if internal_name == "ComplexFenestrationProperty:SolarAbsorbedLayers":
            return ComplexFenestrationPropertySolarAbsorbedLayers()
        if internal_name == "ZoneProperty:UserViewFactors:bySurfaceName":
            return ZonePropertyUserViewFactorsBySurfaceName()
        if internal_name == "GroundHeatTransfer:Control":
            return GroundHeatTransferControl()
        if internal_name == "GroundHeatTransfer:Slab:Materials":
            return GroundHeatTransferSlabMaterials()
        if internal_name == "GroundHeatTransfer:Slab:MatlProps":
            return GroundHeatTransferSlabMatlProps()
        if internal_name == "GroundHeatTransfer:Slab:BoundConds":
            return GroundHeatTransferSlabBoundConds()
        if internal_name == "GroundHeatTransfer:Slab:BldgProps":
            return GroundHeatTransferSlabBldgProps()
        if internal_name == "GroundHeatTransfer:Slab:Insulation":
            return GroundHeatTransferSlabInsulation()
        if internal_name == "GroundHeatTransfer:Slab:EquivalentSlab":
            return GroundHeatTransferSlabEquivalentSlab()
        if internal_name == "GroundHeatTransfer:Slab:AutoGrid":
            return GroundHeatTransferSlabAutoGrid()
        if internal_name == "GroundHeatTransfer:Slab:ManualGrid":
            return GroundHeatTransferSlabManualGrid()
        if internal_name == "GroundHeatTransfer:Basement:SimParameters":
            return GroundHeatTransferBasementSimParameters()
        if internal_name == "GroundHeatTransfer:Basement:MatlProps":
            return GroundHeatTransferBasementMatlProps()
        if internal_name == "GroundHeatTransfer:Basement:Insulation":
            return GroundHeatTransferBasementInsulation()
        if internal_name == "GroundHeatTransfer:Basement:SurfaceProps":
            return GroundHeatTransferBasementSurfaceProps()
        if internal_name == "GroundHeatTransfer:Basement:BldgData":
            return GroundHeatTransferBasementBldgData()
        if internal_name == "GroundHeatTransfer:Basement:Interior":
            return GroundHeatTransferBasementInterior()
        if internal_name == "GroundHeatTransfer:Basement:ComBldg":
            return GroundHeatTransferBasementComBldg()
        if internal_name == "GroundHeatTransfer:Basement:EquivSlab":
            return GroundHeatTransferBasementEquivSlab()
        if internal_name == "GroundHeatTransfer:Basement:EquivAutoGrid":
            return GroundHeatTransferBasementEquivAutoGrid()
        if internal_name == "GroundHeatTransfer:Basement:AutoGrid":
            return GroundHeatTransferBasementAutoGrid()
        if internal_name == "GroundHeatTransfer:Basement:ManualGrid":
            return GroundHeatTransferBasementManualGrid()
        if internal_name == "RoomAirModelType":
            return RoomAirModelType()
        if internal_name == "RoomAir:TemperaturePattern:UserDefined":
            return RoomAirTemperaturePatternUserDefined()
        if internal_name == "RoomAir:TemperaturePattern:ConstantGradient":
            return RoomAirTemperaturePatternConstantGradient()
        if internal_name == "RoomAir:TemperaturePattern:TwoGradient":
            return RoomAirTemperaturePatternTwoGradient()
        if internal_name == "RoomAir:TemperaturePattern:NondimensionalHeight":
            return RoomAirTemperaturePatternNondimensionalHeight()
        if internal_name == "RoomAir:TemperaturePattern:SurfaceMapping":
            return RoomAirTemperaturePatternSurfaceMapping()
        if internal_name == "RoomAir:Node":
            return RoomAirNode()
        if internal_name == "RoomAirSettings:OneNodeDisplacementVentilation":
            return RoomAirSettingsOneNodeDisplacementVentilation()
        if internal_name == "RoomAirSettings:ThreeNodeDisplacementVentilation":
            return RoomAirSettingsThreeNodeDisplacementVentilation()
        if internal_name == "RoomAirSettings:CrossVentilation":
            return RoomAirSettingsCrossVentilation()
        if internal_name == "RoomAirSettings:UnderFloorAirDistributionInterior":
            return RoomAirSettingsUnderFloorAirDistributionInterior()
        if internal_name == "RoomAirSettings:UnderFloorAirDistributionExterior":
            return RoomAirSettingsUnderFloorAirDistributionExterior()
        if internal_name == "People":
            return People()
        if internal_name == "ComfortViewFactorAngles":
            return ComfortViewFactorAngles()
        if internal_name == "Lights":
            return Lights()
        if internal_name == "ElectricEquipment":
            return ElectricEquipment()
        if internal_name == "GasEquipment":
            return GasEquipment()
        if internal_name == "HotWaterEquipment":
            return HotWaterEquipment()
        if internal_name == "SteamEquipment":
            return SteamEquipment()
        if internal_name == "OtherEquipment":
            return OtherEquipment()
        if internal_name == "ZoneBaseboard:OutdoorTemperatureControlled":
            return ZoneBaseboardOutdoorTemperatureControlled()
        if internal_name == "ZoneContaminantSourceAndSink:CarbonDioxide":
            return ZoneContaminantSourceAndSinkCarbonDioxide()
        if internal_name == "ZoneContaminantSourceAndSink:Generic:Constant":
            return ZoneContaminantSourceAndSinkGenericConstant()
        if internal_name == "SurfaceContaminantSourceAndSink:Generic:PressureDriven":
            return SurfaceContaminantSourceAndSinkGenericPressureDriven()
        if internal_name == "ZoneContaminantSourceAndSink:Generic:CutoffModel":
            return ZoneContaminantSourceAndSinkGenericCutoffModel()
        if internal_name == "ZoneContaminantSourceAndSink:Generic:DecaySource":
            return ZoneContaminantSourceAndSinkGenericDecaySource()
        if internal_name == "SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion":
            return SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion()
        if internal_name == "SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink":
            return SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink()
        if internal_name == "ZoneContaminantSourceAndSink:Generic:DepositionRateSink":
            return ZoneContaminantSourceAndSinkGenericDepositionRateSink()
        if internal_name == "Daylighting:Controls":
            return DaylightingControls()
        if internal_name == "Daylighting:DELight:Controls":
            return DaylightingDelightControls()
        if internal_name == "Daylighting:DELight:ReferencePoint":
            return DaylightingDelightReferencePoint()
        if internal_name == "Daylighting:DELight:ComplexFenestration":
            return DaylightingDelightComplexFenestration()
        if internal_name == "DaylightingDevice:Tubular":
            return DaylightingDeviceTubular()
        if internal_name == "DaylightingDevice:Shelf":
            return DaylightingDeviceShelf()
        if internal_name == "DaylightingDevice:LightWell":
            return DaylightingDeviceLightWell()
        if internal_name == "Output:DaylightFactors":
            return OutputDaylightFactors()
        if internal_name == "Output:IlluminanceMap":
            return OutputIlluminanceMap()
        if internal_name == "OutputControl:IlluminanceMap:Style":
            return OutputControlIlluminanceMapStyle()
        if internal_name == "ZoneInfiltration:DesignFlowRate":
            return ZoneInfiltrationDesignFlowRate()
        if internal_name == "ZoneInfiltration:EffectiveLeakageArea":
            return ZoneInfiltrationEffectiveLeakageArea()
        if internal_name == "ZoneInfiltration:FlowCoefficient":
            return ZoneInfiltrationFlowCoefficient()
        if internal_name == "ZoneVentilation:DesignFlowRate":
            return ZoneVentilationDesignFlowRate()
        if internal_name == "ZoneVentilation:WindandStackOpenArea":
            return ZoneVentilationWindandStackOpenArea()
        if internal_name == "ZoneAirBalance:OutdoorAir":
            return ZoneAirBalanceOutdoorAir()
        if internal_name == "ZoneMixing":
            return ZoneMixing()
        if internal_name == "ZoneCrossMixing":
            return ZoneCrossMixing()
        if internal_name == "ZoneRefrigerationDoorMixing":
            return ZoneRefrigerationDoorMixing()
        if internal_name == "ZoneEarthtube":
            return ZoneEarthtube()
        if internal_name == "ZoneCoolTower:Shower":
            return ZoneCoolTowerShower()
        if internal_name == "ZoneThermalChimney":
            return ZoneThermalChimney()
        if internal_name == "AirflowNetwork:SimulationControl":
            return AirflowNetworkSimulationControl()
        if internal_name == "AirflowNetwork:MultiZone:Zone":
            return AirflowNetworkMultiZoneZone()
        if internal_name == "AirflowNetwork:MultiZone:Surface":
            return AirflowNetworkMultiZoneSurface()
        if internal_name == "AirflowNetwork:MultiZone:ReferenceCrackConditions":
            return AirflowNetworkMultiZoneReferenceCrackConditions()
        if internal_name == "AirflowNetwork:MultiZone:Surface:Crack":
            return AirflowNetworkMultiZoneSurfaceCrack()
        if internal_name == "AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea":
            return AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea()
        if internal_name == "AirflowNetwork:MultiZone:Component:DetailedOpening":
            return AirflowNetworkMultiZoneComponentDetailedOpening()
        if internal_name == "AirflowNetwork:MultiZone:Component:SimpleOpening":
            return AirflowNetworkMultiZoneComponentSimpleOpening()
        if internal_name == "AirflowNetwork:MultiZone:Component:HorizontalOpening":
            return AirflowNetworkMultiZoneComponentHorizontalOpening()
        if internal_name == "AirflowNetwork:MultiZone:Component:ZoneExhaustFan":
            return AirflowNetworkMultiZoneComponentZoneExhaustFan()
        if internal_name == "AirflowNetwork:MultiZone:ExternalNode":
            return AirflowNetworkMultiZoneExternalNode()
        if internal_name == "AirflowNetwork:MultiZone:WindPressureCoefficientArray":
            return AirflowNetworkMultiZoneWindPressureCoefficientArray()
        if internal_name == "AirflowNetwork:MultiZone:WindPressureCoefficientValues":
            return AirflowNetworkMultiZoneWindPressureCoefficientValues()
        if internal_name == "AirflowNetwork:Distribution:Node":
            return AirflowNetworkDistributionNode()
        if internal_name == "AirflowNetwork:Distribution:Component:Leak":
            return AirflowNetworkDistributionComponentLeak()
        if internal_name == "AirflowNetwork:Distribution:Component:LeakageRatio":
            return AirflowNetworkDistributionComponentLeakageRatio()
        if internal_name == "AirflowNetwork:Distribution:Component:Duct":
            return AirflowNetworkDistributionComponentDuct()
        if internal_name == "AirflowNetwork:Distribution:Component:Fan":
            return AirflowNetworkDistributionComponentFan()
        if internal_name == "AirflowNetwork:Distribution:Component:Coil":
            return AirflowNetworkDistributionComponentCoil()
        if internal_name == "AirflowNetwork:Distribution:Component:HeatExchanger":
            return AirflowNetworkDistributionComponentHeatExchanger()
        if internal_name == "AirflowNetwork:Distribution:Component:TerminalUnit":
            return AirflowNetworkDistributionComponentTerminalUnit()
        if internal_name == "AirflowNetwork:Distribution:Component:ConstantPressureDrop":
            return AirflowNetworkDistributionComponentConstantPressureDrop()
        if internal_name == "AirflowNetwork:Distribution:Linkage":
            return AirflowNetworkDistributionLinkage()
        if internal_name == "Exterior:Lights":
            return ExteriorLights()
        if internal_name == "Exterior:FuelEquipment":
            return ExteriorFuelEquipment()
        if internal_name == "Exterior:WaterEquipment":
            return ExteriorWaterEquipment()
        if internal_name == "HVACTemplate:Thermostat":
            return HvactemplateThermostat()
        if internal_name == "HVACTemplate:Zone:IdealLoadsAirSystem":
            return HvactemplateZoneIdealLoadsAirSystem()
        if internal_name == "HVACTemplate:Zone:BaseboardHeat":
            return HvactemplateZoneBaseboardHeat()
        if internal_name == "HVACTemplate:Zone:FanCoil":
            return HvactemplateZoneFanCoil()
        if internal_name == "HVACTemplate:Zone:PTAC":
            return HvactemplateZonePtac()
        if internal_name == "HVACTemplate:Zone:PTHP":
            return HvactemplateZonePthp()
        if internal_name == "HVACTemplate:Zone:WaterToAirHeatPump":
            return HvactemplateZoneWaterToAirHeatPump()
        if internal_name == "HVACTemplate:Zone:VRF":
            return HvactemplateZoneVrf()
        if internal_name == "HVACTemplate:Zone:Unitary":
            return HvactemplateZoneUnitary()
        if internal_name == "HVACTemplate:Zone:VAV":
            return HvactemplateZoneVav()
        if internal_name == "HVACTemplate:Zone:VAV:FanPowered":
            return HvactemplateZoneVavFanPowered()
        if internal_name == "HVACTemplate:Zone:VAV:HeatAndCool":
            return HvactemplateZoneVavHeatAndCool()
        if internal_name == "HVACTemplate:Zone:ConstantVolume":
            return HvactemplateZoneConstantVolume()
        if internal_name == "HVACTemplate:Zone:DualDuct":
            return HvactemplateZoneDualDuct()
        if internal_name == "HVACTemplate:System:VRF":
            return HvactemplateSystemVrf()
        if internal_name == "HVACTemplate:System:Unitary":
            return HvactemplateSystemUnitary()
        if internal_name == "HVACTemplate:System:UnitaryHeatPump:AirToAir":
            return HvactemplateSystemUnitaryHeatPumpAirToAir()
        if internal_name == "HVACTemplate:System:UnitarySystem":
            return HvactemplateSystemUnitarySystem()
        if internal_name == "HVACTemplate:System:VAV":
            return HvactemplateSystemVav()
        if internal_name == "HVACTemplate:System:PackagedVAV":
            return HvactemplateSystemPackagedVav()
        if internal_name == "HVACTemplate:System:ConstantVolume":
            return HvactemplateSystemConstantVolume()
        if internal_name == "HVACTemplate:System:DualDuct":
            return HvactemplateSystemDualDuct()
        if internal_name == "HVACTemplate:System:DedicatedOutdoorAir":
            return HvactemplateSystemDedicatedOutdoorAir()
        if internal_name == "HVACTemplate:Plant:ChilledWaterLoop":
            return HvactemplatePlantChilledWaterLoop()
        if internal_name == "HVACTemplate:Plant:Chiller":
            return HvactemplatePlantChiller()
        if internal_name == "HVACTemplate:Plant:Chiller:ObjectReference":
            return HvactemplatePlantChillerObjectReference()
        if internal_name == "HVACTemplate:Plant:Tower":
            return HvactemplatePlantTower()
        if internal_name == "HVACTemplate:Plant:Tower:ObjectReference":
            return HvactemplatePlantTowerObjectReference()
        if internal_name == "HVACTemplate:Plant:HotWaterLoop":
            return HvactemplatePlantHotWaterLoop()
        if internal_name == "HVACTemplate:Plant:Boiler":
            return HvactemplatePlantBoiler()
        if internal_name == "HVACTemplate:Plant:Boiler:ObjectReference":
            return HvactemplatePlantBoilerObjectReference()
        if internal_name == "HVACTemplate:Plant:MixedWaterLoop":
            return HvactemplatePlantMixedWaterLoop()
        if internal_name == "DesignSpecification:OutdoorAir":
            return DesignSpecificationOutdoorAir()
        if internal_name == "DesignSpecification:ZoneAirDistribution":
            return DesignSpecificationZoneAirDistribution()
        if internal_name == "Sizing:Parameters":
            return SizingParameters()
        if internal_name == "Sizing:Zone":
            return SizingZone()
        if internal_name == "DesignSpecification:ZoneHVAC:Sizing":
            return DesignSpecificationZoneHvacSizing()
        if internal_name == "Sizing:System":
            return SizingSystem()
        if internal_name == "Sizing:Plant":
            return SizingPlant()
        if internal_name == "OutputControl:Sizing:Style":
            return OutputControlSizingStyle()
        if internal_name == "ZoneControl:Humidistat":
            return ZoneControlHumidistat()
        if internal_name == "ZoneControl:Thermostat":
            return ZoneControlThermostat()
        if internal_name == "ZoneControl:Thermostat:OperativeTemperature":
            return ZoneControlThermostatOperativeTemperature()
        if internal_name == "ZoneControl:Thermostat:ThermalComfort":
            return ZoneControlThermostatThermalComfort()
        if internal_name == "ZoneControl:Thermostat:TemperatureAndHumidity":
            return ZoneControlThermostatTemperatureAndHumidity()
        if internal_name == "ThermostatSetpoint:SingleHeating":
            return ThermostatSetpointSingleHeating()
        if internal_name == "ThermostatSetpoint:SingleCooling":
            return ThermostatSetpointSingleCooling()
        if internal_name == "ThermostatSetpoint:SingleHeatingOrCooling":
            return ThermostatSetpointSingleHeatingOrCooling()
        if internal_name == "ThermostatSetpoint:DualSetpoint":
            return ThermostatSetpointDualSetpoint()
        if internal_name == "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating":
            return ThermostatSetpointThermalComfortFangerSingleHeating()
        if internal_name == "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling":
            return ThermostatSetpointThermalComfortFangerSingleCooling()
        if internal_name == "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling":
            return ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling()
        if internal_name == "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint":
            return ThermostatSetpointThermalComfortFangerDualSetpoint()
        if internal_name == "ZoneControl:Thermostat:StagedDualSetpoint":
            return ZoneControlThermostatStagedDualSetpoint()
        if internal_name == "ZoneControl:ContaminantController":
            return ZoneControlContaminantController()
        if internal_name == "ZoneHVAC:IdealLoadsAirSystem":
            return ZoneHvacIdealLoadsAirSystem()
        if internal_name == "ZoneHVAC:FourPipeFanCoil":
            return ZoneHvacFourPipeFanCoil()
        if internal_name == "ZoneHVAC:WindowAirConditioner":
            return ZoneHvacWindowAirConditioner()
        if internal_name == "ZoneHVAC:PackagedTerminalAirConditioner":
            return ZoneHvacPackagedTerminalAirConditioner()
        if internal_name == "ZoneHVAC:PackagedTerminalHeatPump":
            return ZoneHvacPackagedTerminalHeatPump()
        if internal_name == "ZoneHVAC:WaterToAirHeatPump":
            return ZoneHvacWaterToAirHeatPump()
        if internal_name == "ZoneHVAC:Dehumidifier:DX":
            return ZoneHvacDehumidifierDx()
        if internal_name == "ZoneHVAC:EnergyRecoveryVentilator":
            return ZoneHvacEnergyRecoveryVentilator()
        if internal_name == "ZoneHVAC:EnergyRecoveryVentilator:Controller":
            return ZoneHvacEnergyRecoveryVentilatorController()
        if internal_name == "ZoneHVAC:UnitVentilator":
            return ZoneHvacUnitVentilator()
        if internal_name == "ZoneHVAC:UnitHeater":
            return ZoneHvacUnitHeater()
        if internal_name == "ZoneHVAC:EvaporativeCoolerUnit":
            return ZoneHvacEvaporativeCoolerUnit()
        if internal_name == "ZoneHVAC:OutdoorAirUnit":
            return ZoneHvacOutdoorAirUnit()
        if internal_name == "ZoneHVAC:OutdoorAirUnit:EquipmentList":
            return ZoneHvacOutdoorAirUnitEquipmentList()
        if internal_name == "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow":
            return ZoneHvacTerminalUnitVariableRefrigerantFlow()
        if internal_name == "ZoneHVAC:Baseboard:RadiantConvective:Water":
            return ZoneHvacBaseboardRadiantConvectiveWater()
        if internal_name == "ZoneHVAC:Baseboard:RadiantConvective:Steam":
            return ZoneHvacBaseboardRadiantConvectiveSteam()
        if internal_name == "ZoneHVAC:Baseboard:RadiantConvective:Electric":
            return ZoneHvacBaseboardRadiantConvectiveElectric()
        if internal_name == "ZoneHVAC:Baseboard:Convective:Water":
            return ZoneHvacBaseboardConvectiveWater()
        if internal_name == "ZoneHVAC:Baseboard:Convective:Electric":
            return ZoneHvacBaseboardConvectiveElectric()
        if internal_name == "ZoneHVAC:LowTemperatureRadiant:VariableFlow":
            return ZoneHvacLowTemperatureRadiantVariableFlow()
        if internal_name == "ZoneHVAC:LowTemperatureRadiant:ConstantFlow":
            return ZoneHvacLowTemperatureRadiantConstantFlow()
        if internal_name == "ZoneHVAC:LowTemperatureRadiant:Electric":
            return ZoneHvacLowTemperatureRadiantElectric()
        if internal_name == "ZoneHVAC:LowTemperatureRadiant:SurfaceGroup":
            return ZoneHvacLowTemperatureRadiantSurfaceGroup()
        if internal_name == "ZoneHVAC:HighTemperatureRadiant":
            return ZoneHvacHighTemperatureRadiant()
        if internal_name == "ZoneHVAC:VentilatedSlab":
            return ZoneHvacVentilatedSlab()
        if internal_name == "ZoneHVAC:VentilatedSlab:SlabGroup":
            return ZoneHvacVentilatedSlabSlabGroup()
        if internal_name == "AirTerminal:SingleDuct:Uncontrolled":
            return AirTerminalSingleDuctUncontrolled()
        if internal_name == "AirTerminal:SingleDuct:ConstantVolume:Reheat":
            return AirTerminalSingleDuctConstantVolumeReheat()
        if internal_name == "AirTerminal:SingleDuct:VAV:NoReheat":
            return AirTerminalSingleDuctVavNoReheat()
        if internal_name == "AirTerminal:SingleDuct:VAV:Reheat":
            return AirTerminalSingleDuctVavReheat()
        if internal_name == "AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan":
            return AirTerminalSingleDuctVavReheatVariableSpeedFan()
        if internal_name == "AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat":
            return AirTerminalSingleDuctVavHeatAndCoolNoReheat()
        if internal_name == "AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat":
            return AirTerminalSingleDuctVavHeatAndCoolReheat()
        if internal_name == "AirTerminal:SingleDuct:SeriesPIU:Reheat":
            return AirTerminalSingleDuctSeriesPiuReheat()
        if internal_name == "AirTerminal:SingleDuct:ParallelPIU:Reheat":
            return AirTerminalSingleDuctParallelPiuReheat()
        if internal_name == "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction":
            return AirTerminalSingleDuctConstantVolumeFourPipeInduction()
        if internal_name == "AirTerminal:SingleDuct:ConstantVolume:CooledBeam":
            return AirTerminalSingleDuctConstantVolumeCooledBeam()
        if internal_name == "AirTerminal:SingleDuct:InletSideMixer":
            return AirTerminalSingleDuctInletSideMixer()
        if internal_name == "AirTerminal:SingleDuct:SupplySideMixer":
            return AirTerminalSingleDuctSupplySideMixer()
        if internal_name == "AirTerminal:DualDuct:ConstantVolume":
            return AirTerminalDualDuctConstantVolume()
        if internal_name == "AirTerminal:DualDuct:VAV":
            return AirTerminalDualDuctVav()
        if internal_name == "AirTerminal:DualDuct:VAV:OutdoorAir":
            return AirTerminalDualDuctVavOutdoorAir()
        if internal_name == "ZoneHVAC:AirDistributionUnit":
            return ZoneHvacAirDistributionUnit()
        if internal_name == "ZoneHVAC:EquipmentList":
            return ZoneHvacEquipmentList()
        if internal_name == "ZoneHVAC:EquipmentConnections":
            return ZoneHvacEquipmentConnections()
        if internal_name == "Fan:ConstantVolume":
            return FanConstantVolume()
        if internal_name == "Fan:VariableVolume":
            return FanVariableVolume()
        if internal_name == "Fan:OnOff":
            return FanOnOff()
        if internal_name == "Fan:ZoneExhaust":
            return FanZoneExhaust()
        if internal_name == "FanPerformance:NightVentilation":
            return FanPerformanceNightVentilation()
        if internal_name == "Fan:ComponentModel":
            return FanComponentModel()
        if internal_name == "Coil:Cooling:Water":
            return CoilCoolingWater()
        if internal_name == "Coil:Cooling:Water:DetailedGeometry":
            return CoilCoolingWaterDetailedGeometry()
        if internal_name == "Coil:Cooling:DX:SingleSpeed":
            return CoilCoolingDxSingleSpeed()
        if internal_name == "Coil:Cooling:DX:TwoSpeed":
            return CoilCoolingDxTwoSpeed()
        if internal_name == "Coil:Cooling:DX:MultiSpeed":
            return CoilCoolingDxMultiSpeed()
        if internal_name == "Coil:Cooling:DX:VariableSpeed":
            return CoilCoolingDxVariableSpeed()
        if internal_name == "Coil:Cooling:DX:TwoStageWithHumidityControlMode":
            return CoilCoolingDxTwoStageWithHumidityControlMode()
        if internal_name == "CoilPerformance:DX:Cooling":
            return CoilPerformanceDxCooling()
        if internal_name == "Coil:Cooling:DX:VariableRefrigerantFlow":
            return CoilCoolingDxVariableRefrigerantFlow()
        if internal_name == "Coil:Heating:DX:VariableRefrigerantFlow":
            return CoilHeatingDxVariableRefrigerantFlow()
        if internal_name == "Coil:Heating:Water":
            return CoilHeatingWater()
        if internal_name == "Coil:Heating:Steam":
            return CoilHeatingSteam()
        if internal_name == "Coil:Heating:Electric":
            return CoilHeatingElectric()
        if internal_name == "Coil:Heating:Electric:MultiStage":
            return CoilHeatingElectricMultiStage()
        if internal_name == "Coil:Heating:Gas":
            return CoilHeatingGas()
        if internal_name == "Coil:Heating:Gas:MultiStage":
            return CoilHeatingGasMultiStage()
        if internal_name == "Coil:Heating:Desuperheater":
            return CoilHeatingDesuperheater()
        if internal_name == "Coil:Heating:DX:SingleSpeed":
            return CoilHeatingDxSingleSpeed()
        if internal_name == "Coil:Heating:DX:MultiSpeed":
            return CoilHeatingDxMultiSpeed()
        if internal_name == "Coil:Heating:DX:VariableSpeed":
            return CoilHeatingDxVariableSpeed()
        if internal_name == "Coil:Cooling:WaterToAirHeatPump:ParameterEstimation":
            return CoilCoolingWaterToAirHeatPumpParameterEstimation()
        if internal_name == "Coil:Heating:WaterToAirHeatPump:ParameterEstimation":
            return CoilHeatingWaterToAirHeatPumpParameterEstimation()
        if internal_name == "Coil:Cooling:WaterToAirHeatPump:EquationFit":
            return CoilCoolingWaterToAirHeatPumpEquationFit()
        if internal_name == "Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit":
            return CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit()
        if internal_name == "Coil:Heating:WaterToAirHeatPump:EquationFit":
            return CoilHeatingWaterToAirHeatPumpEquationFit()
        if internal_name == "Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit":
            return CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit()
        if internal_name == "Coil:WaterHeating:AirToWaterHeatPump":
            return CoilWaterHeatingAirToWaterHeatPump()
        if internal_name == "Coil:WaterHeating:Desuperheater":
            return CoilWaterHeatingDesuperheater()
        if internal_name == "CoilSystem:Cooling:DX":
            return CoilSystemCoolingDx()
        if internal_name == "CoilSystem:Heating:DX":
            return CoilSystemHeatingDx()
        if internal_name == "CoilSystem:Cooling:Water:HeatExchangerAssisted":
            return CoilSystemCoolingWaterHeatExchangerAssisted()
        if internal_name == "CoilSystem:Cooling:DX:HeatExchangerAssisted":
            return CoilSystemCoolingDxHeatExchangerAssisted()
        if internal_name == "Coil:Cooling:DX:SingleSpeed:ThermalStorage":
            return CoilCoolingDxSingleSpeedThermalStorage()
        if internal_name == "Humidifier:Steam:Electric":
            return HumidifierSteamElectric()
        if internal_name == "Dehumidifier:Desiccant:NoFans":
            return DehumidifierDesiccantNoFans()
        if internal_name == "Dehumidifier:Desiccant:System":
            return DehumidifierDesiccantSystem()
        if internal_name == "HeatExchanger:AirToAir:FlatPlate":
            return HeatExchangerAirToAirFlatPlate()
        if internal_name == "HeatExchanger:AirToAir:SensibleAndLatent":
            return HeatExchangerAirToAirSensibleAndLatent()
        if internal_name == "HeatExchanger:Desiccant:BalancedFlow":
            return HeatExchangerDesiccantBalancedFlow()
        if internal_name == "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1":
            return HeatExchangerDesiccantBalancedFlowPerformanceDataType1()
        if internal_name == "AirLoopHVAC:UnitarySystem":
            return AirLoopHvacUnitarySystem()
        if internal_name == "UnitarySystemPerformance:HeatPump:Multispeed":
            return UnitarySystemPerformanceHeatPumpMultispeed()
        if internal_name == "AirLoopHVAC:Unitary:Furnace:HeatOnly":
            return AirLoopHvacUnitaryFurnaceHeatOnly()
        if internal_name == "AirLoopHVAC:Unitary:Furnace:HeatCool":
            return AirLoopHvacUnitaryFurnaceHeatCool()
        if internal_name == "AirLoopHVAC:UnitaryHeatOnly":
            return AirLoopHvacUnitaryHeatOnly()
        if internal_name == "AirLoopHVAC:UnitaryHeatCool":
            return AirLoopHvacUnitaryHeatCool()
        if internal_name == "AirLoopHVAC:UnitaryHeatPump:AirToAir":
            return AirLoopHvacUnitaryHeatPumpAirToAir()
        if internal_name == "AirLoopHVAC:UnitaryHeatPump:WaterToAir":
            return AirLoopHvacUnitaryHeatPumpWaterToAir()
        if internal_name == "AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass":
            return AirLoopHvacUnitaryHeatCoolVavchangeoverBypass()
        if internal_name == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed":
            return AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed()
        if internal_name == "AirConditioner:VariableRefrigerantFlow":
            return AirConditionerVariableRefrigerantFlow()
        if internal_name == "ZoneTerminalUnitList":
            return ZoneTerminalUnitList()
        if internal_name == "Controller:WaterCoil":
            return ControllerWaterCoil()
        if internal_name == "Controller:OutdoorAir":
            return ControllerOutdoorAir()
        if internal_name == "Controller:MechanicalVentilation":
            return ControllerMechanicalVentilation()
        if internal_name == "AirLoopHVAC:ControllerList":
            return AirLoopHvacControllerList()
        if internal_name == "AirLoopHVAC":
            return AirLoopHvac()
        if internal_name == "AirLoopHVAC:OutdoorAirSystem:EquipmentList":
            return AirLoopHvacOutdoorAirSystemEquipmentList()
        if internal_name == "AirLoopHVAC:OutdoorAirSystem":
            return AirLoopHvacOutdoorAirSystem()
        if internal_name == "OutdoorAir:Mixer":
            return OutdoorAirMixer()
        if internal_name == "AirLoopHVAC:SupplyPath":
            return AirLoopHvacSupplyPath()
        if internal_name == "AirLoopHVAC:ReturnPath":
            return AirLoopHvacReturnPath()
        if internal_name == "Branch":
            return Branch()
        if internal_name == "ConnectorList":
            return ConnectorList()
        if internal_name == "OutdoorAir:Node":
            return OutdoorAirNode()
        if internal_name == "Pipe:Adiabatic":
            return PipeAdiabatic()
        if internal_name == "Pipe:Adiabatic:Steam":
            return PipeAdiabaticSteam()
        if internal_name == "Pipe:Indoor":
            return PipeIndoor()
        if internal_name == "Pipe:Outdoor":
            return PipeOutdoor()
        if internal_name == "Pipe:Underground":
            return PipeUnderground()
        if internal_name == "PipingSystem:Underground:Domain":
            return PipingSystemUndergroundDomain()
        if internal_name == "PipingSystem:Underground:PipeCircuit":
            return PipingSystemUndergroundPipeCircuit()
        if internal_name == "PipingSystem:Underground:PipeSegment":
            return PipingSystemUndergroundPipeSegment()
        if internal_name == "Duct":
            return Duct()
        if internal_name == "Pump:VariableSpeed":
            return PumpVariableSpeed()
        if internal_name == "Pump:ConstantSpeed":
            return PumpConstantSpeed()
        if internal_name == "Pump:VariableSpeed:Condensate":
            return PumpVariableSpeedCondensate()
        if internal_name == "HeaderedPumps:ConstantSpeed":
            return HeaderedPumpsConstantSpeed()
        if internal_name == "TemperingValve":
            return TemperingValve()
        if internal_name == "LoadProfile:Plant":
            return LoadProfilePlant()
        if internal_name == "SolarCollectorPerformance:FlatPlate":
            return SolarCollectorPerformanceFlatPlate()
        if internal_name == "SolarCollector:FlatPlate:Water":
            return SolarCollectorFlatPlateWater()
        if internal_name == "SolarCollectorPerformance:PhotovoltaicThermal:Simple":
            return SolarCollectorPerformancePhotovoltaicThermalSimple()
        if internal_name == "SolarCollector:IntegralCollectorStorage":
            return SolarCollectorIntegralCollectorStorage()
        if internal_name == "SolarCollectorPerformance:IntegralCollectorStorage":
            return SolarCollectorPerformanceIntegralCollectorStorage()
        if internal_name == "SolarCollector:UnglazedTranspired":
            return SolarCollectorUnglazedTranspired()
        if internal_name == "SolarCollector:UnglazedTranspired:Multisystem":
            return SolarCollectorUnglazedTranspiredMultisystem()
        if internal_name == "Boiler:HotWater":
            return BoilerHotWater()
        if internal_name == "Boiler:Steam":
            return BoilerSteam()
        if internal_name == "Chiller:Electric:EIR":
            return ChillerElectricEir()
        if internal_name == "Chiller:Electric:ReformulatedEIR":
            return ChillerElectricReformulatedEir()
        if internal_name == "Chiller:Electric":
            return ChillerElectric()
        if internal_name == "Chiller:Absorption:Indirect":
            return ChillerAbsorptionIndirect()
        if internal_name == "Chiller:Absorption":
            return ChillerAbsorption()
        if internal_name == "Chiller:ConstantCOP":
            return ChillerConstantCop()
        if internal_name == "Chiller:EngineDriven":
            return ChillerEngineDriven()
        if internal_name == "Chiller:CombustionTurbine":
            return ChillerCombustionTurbine()
        if internal_name == "ChillerHeater:Absorption:DirectFired":
            return ChillerHeaterAbsorptionDirectFired()
        if internal_name == "ChillerHeater:Absorption:DoubleEffect":
            return ChillerHeaterAbsorptionDoubleEffect()
        if internal_name == "HeatPump:WaterToWater:EquationFit:Heating":
            return HeatPumpWaterToWaterEquationFitHeating()
        if internal_name == "HeatPump:WaterToWater:EquationFit:Cooling":
            return HeatPumpWaterToWaterEquationFitCooling()
        if internal_name == "HeatPump:WaterToWater:ParameterEstimation:Cooling":
            return HeatPumpWaterToWaterParameterEstimationCooling()
        if internal_name == "HeatPump:WaterToWater:ParameterEstimation:Heating":
            return HeatPumpWaterToWaterParameterEstimationHeating()
        if internal_name == "DistrictCooling":
            return DistrictCooling()
        if internal_name == "DistrictHeating":
            return DistrictHeating()
        if internal_name == "PlantComponent:TemperatureSource":
            return PlantComponentTemperatureSource()
        if internal_name == "CentralHeatPumpSystem":
            return CentralHeatPumpSystem()
        if internal_name == "ChillerHeaterPerformance:Electric:EIR":
            return ChillerHeaterPerformanceElectricEir()
        if internal_name == "CoolingTower:SingleSpeed":
            return CoolingTowerSingleSpeed()
        if internal_name == "CoolingTower:TwoSpeed":
            return CoolingTowerTwoSpeed()
        if internal_name == "CoolingTower:VariableSpeed:Merkel":
            return CoolingTowerVariableSpeedMerkel()
        if internal_name == "CoolingTower:VariableSpeed":
            return CoolingTowerVariableSpeed()
        if internal_name == "CoolingTowerPerformance:CoolTools":
            return CoolingTowerPerformanceCoolTools()
        if internal_name == "CoolingTowerPerformance:YorkCalc":
            return CoolingTowerPerformanceYorkCalc()
        if internal_name == "EvaporativeFluidCooler:SingleSpeed":
            return EvaporativeFluidCoolerSingleSpeed()
        if internal_name == "EvaporativeFluidCooler:TwoSpeed":
            return EvaporativeFluidCoolerTwoSpeed()
        if internal_name == "FluidCooler:SingleSpeed":
            return FluidCoolerSingleSpeed()
        if internal_name == "FluidCooler:TwoSpeed":
            return FluidCoolerTwoSpeed()
        if internal_name == "GroundHeatExchanger:Vertical":
            return GroundHeatExchangerVertical()
        if internal_name == "GroundHeatExchanger:Pond":
            return GroundHeatExchangerPond()
        if internal_name == "GroundHeatExchanger:Surface":
            return GroundHeatExchangerSurface()
        if internal_name == "GroundHeatExchanger:HorizontalTrench":
            return GroundHeatExchangerHorizontalTrench()
        if internal_name == "HeatExchanger:FluidToFluid":
            return HeatExchangerFluidToFluid()
        if internal_name == "WaterHeater:Mixed":
            return WaterHeaterMixed()
        if internal_name == "WaterHeater:Stratified":
            return WaterHeaterStratified()
        if internal_name == "WaterHeater:Sizing":
            return WaterHeaterSizing()
        if internal_name == "WaterHeater:HeatPump":
            return WaterHeaterHeatPump()
        if internal_name == "ThermalStorage:Ice:Simple":
            return ThermalStorageIceSimple()
        if internal_name == "ThermalStorage:Ice:Detailed":
            return ThermalStorageIceDetailed()
        if internal_name == "ThermalStorage:ChilledWater:Mixed":
            return ThermalStorageChilledWaterMixed()
        if internal_name == "ThermalStorage:ChilledWater:Stratified":
            return ThermalStorageChilledWaterStratified()
        if internal_name == "PlantLoop":
            return PlantLoop()
        if internal_name == "CondenserLoop":
            return CondenserLoop()
        if internal_name == "PlantEquipmentList":
            return PlantEquipmentList()
        if internal_name == "CondenserEquipmentList":
            return CondenserEquipmentList()
        if internal_name == "PlantEquipmentOperation:Uncontrolled":
            return PlantEquipmentOperationUncontrolled()
        if internal_name == "PlantEquipmentOperation:CoolingLoad":
            return PlantEquipmentOperationCoolingLoad()
        if internal_name == "PlantEquipmentOperation:HeatingLoad":
            return PlantEquipmentOperationHeatingLoad()
        if internal_name == "PlantEquipmentOperation:OutdoorDryBulb":
            return PlantEquipmentOperationOutdoorDryBulb()
        if internal_name == "PlantEquipmentOperation:OutdoorWetBulb":
            return PlantEquipmentOperationOutdoorWetBulb()
        if internal_name == "PlantEquipmentOperation:OutdoorRelativeHumidity":
            return PlantEquipmentOperationOutdoorRelativeHumidity()
        if internal_name == "PlantEquipmentOperation:OutdoorDewpoint":
            return PlantEquipmentOperationOutdoorDewpoint()
        if internal_name == "PlantEquipmentOperation:ComponentSetpoint":
            return PlantEquipmentOperationComponentSetpoint()
        if internal_name == "PlantEquipmentOperation:OutdoorDryBulbDifference":
            return PlantEquipmentOperationOutdoorDryBulbDifference()
        if internal_name == "PlantEquipmentOperation:OutdoorWetBulbDifference":
            return PlantEquipmentOperationOutdoorWetBulbDifference()
        if internal_name == "PlantEquipmentOperation:OutdoorDewpointDifference":
            return PlantEquipmentOperationOutdoorDewpointDifference()
        if internal_name == "PlantEquipmentOperationSchemes":
            return PlantEquipmentOperationSchemes()
        if internal_name == "CondenserEquipmentOperationSchemes":
            return CondenserEquipmentOperationSchemes()
        if internal_name == "EnergyManagementSystem:Sensor":
            return EnergyManagementSystemSensor()
        if internal_name == "EnergyManagementSystem:Actuator":
            return EnergyManagementSystemActuator()
        if internal_name == "EnergyManagementSystem:ProgramCallingManager":
            return EnergyManagementSystemProgramCallingManager()
        if internal_name == "EnergyManagementSystem:OutputVariable":
            return EnergyManagementSystemOutputVariable()
        if internal_name == "EnergyManagementSystem:MeteredOutputVariable":
            return EnergyManagementSystemMeteredOutputVariable()
        if internal_name == "EnergyManagementSystem:TrendVariable":
            return EnergyManagementSystemTrendVariable()
        if internal_name == "EnergyManagementSystem:InternalVariable":
            return EnergyManagementSystemInternalVariable()
        if internal_name == "EnergyManagementSystem:CurveOrTableIndexVariable":
            return EnergyManagementSystemCurveOrTableIndexVariable()
        if internal_name == "EnergyManagementSystem:ConstructionIndexVariable":
            return EnergyManagementSystemConstructionIndexVariable()
        if internal_name == "ExternalInterface":
            return ExternalInterface()
        if internal_name == "ExternalInterface:Schedule":
            return ExternalInterfaceSchedule()
        if internal_name == "ExternalInterface:Variable":
            return ExternalInterfaceVariable()
        if internal_name == "ExternalInterface:Actuator":
            return ExternalInterfaceActuator()
        if internal_name == "ExternalInterface:FunctionalMockupUnitImport":
            return ExternalInterfaceFunctionalMockupUnitImport()
        if internal_name == "ExternalInterface:FunctionalMockupUnitImport:From:Variable":
            return ExternalInterfaceFunctionalMockupUnitImportFromVariable()
        if internal_name == "ExternalInterface:FunctionalMockupUnitImport:To:Schedule":
            return ExternalInterfaceFunctionalMockupUnitImportToSchedule()
        if internal_name == "ExternalInterface:FunctionalMockupUnitImport:To:Actuator":
            return ExternalInterfaceFunctionalMockupUnitImportToActuator()
        if internal_name == "ExternalInterface:FunctionalMockupUnitImport:To:Variable":
            return ExternalInterfaceFunctionalMockupUnitImportToVariable()
        if internal_name == "ExternalInterface:FunctionalMockupUnitExport:From:Variable":
            return ExternalInterfaceFunctionalMockupUnitExportFromVariable()
        if internal_name == "ExternalInterface:FunctionalMockupUnitExport:To:Schedule":
            return ExternalInterfaceFunctionalMockupUnitExportToSchedule()
        if internal_name == "ExternalInterface:FunctionalMockupUnitExport:To:Actuator":
            return ExternalInterfaceFunctionalMockupUnitExportToActuator()
        if internal_name == "ExternalInterface:FunctionalMockupUnitExport:To:Variable":
            return ExternalInterfaceFunctionalMockupUnitExportToVariable()
        if internal_name == "ZoneHVAC:ForcedAir:UserDefined":
            return ZoneHvacForcedAirUserDefined()
        if internal_name == "AirTerminal:SingleDuct:UserDefined":
            return AirTerminalSingleDuctUserDefined()
        if internal_name == "Coil:UserDefined":
            return CoilUserDefined()
        if internal_name == "PlantComponent:UserDefined":
            return PlantComponentUserDefined()
        if internal_name == "PlantEquipmentOperation:UserDefined":
            return PlantEquipmentOperationUserDefined()
        if internal_name == "AvailabilityManager:Scheduled":
            return AvailabilityManagerScheduled()
        if internal_name == "AvailabilityManager:ScheduledOn":
            return AvailabilityManagerScheduledOn()
        if internal_name == "AvailabilityManager:ScheduledOff":
            return AvailabilityManagerScheduledOff()
        if internal_name == "AvailabilityManager:OptimumStart":
            return AvailabilityManagerOptimumStart()
        if internal_name == "AvailabilityManager:NightCycle":
            return AvailabilityManagerNightCycle()
        if internal_name == "AvailabilityManager:DifferentialThermostat":
            return AvailabilityManagerDifferentialThermostat()
        if internal_name == "AvailabilityManager:HighTemperatureTurnOff":
            return AvailabilityManagerHighTemperatureTurnOff()
        if internal_name == "AvailabilityManager:HighTemperatureTurnOn":
            return AvailabilityManagerHighTemperatureTurnOn()
        if internal_name == "AvailabilityManager:LowTemperatureTurnOff":
            return AvailabilityManagerLowTemperatureTurnOff()
        if internal_name == "AvailabilityManager:LowTemperatureTurnOn":
            return AvailabilityManagerLowTemperatureTurnOn()
        if internal_name == "AvailabilityManager:NightVentilation":
            return AvailabilityManagerNightVentilation()
        if internal_name == "AvailabilityManager:HybridVentilation":
            return AvailabilityManagerHybridVentilation()
        if internal_name == "AvailabilityManagerAssignmentList":
            return AvailabilityManagerAssignmentList()
        if internal_name == "SetpointManager:Scheduled":
            return SetpointManagerScheduled()
        if internal_name == "SetpointManager:Scheduled:DualSetpoint":
            return SetpointManagerScheduledDualSetpoint()
        if internal_name == "SetpointManager:OutdoorAirReset":
            return SetpointManagerOutdoorAirReset()
        if internal_name == "SetpointManager:SingleZone:Reheat":
            return SetpointManagerSingleZoneReheat()
        if internal_name == "SetpointManager:SingleZone:Heating":
            return SetpointManagerSingleZoneHeating()
        if internal_name == "SetpointManager:SingleZone:Cooling":
            return SetpointManagerSingleZoneCooling()
        if internal_name == "SetpointManager:SingleZone:Humidity:Minimum":
            return SetpointManagerSingleZoneHumidityMinimum()
        if internal_name == "SetpointManager:SingleZone:Humidity:Maximum":
            return SetpointManagerSingleZoneHumidityMaximum()
        if internal_name == "SetpointManager:MixedAir":
            return SetpointManagerMixedAir()
        if internal_name == "SetpointManager:OutdoorAirPretreat":
            return SetpointManagerOutdoorAirPretreat()
        if internal_name == "SetpointManager:Warmest":
            return SetpointManagerWarmest()
        if internal_name == "SetpointManager:Coldest":
            return SetpointManagerColdest()
        if internal_name == "SetpointManager:ReturnAirBypassFlow":
            return SetpointManagerReturnAirBypassFlow()
        if internal_name == "SetpointManager:WarmestTemperatureFlow":
            return SetpointManagerWarmestTemperatureFlow()
        if internal_name == "SetpointManager:MultiZone:Heating:Average":
            return SetpointManagerMultiZoneHeatingAverage()
        if internal_name == "SetpointManager:MultiZone:Cooling:Average":
            return SetpointManagerMultiZoneCoolingAverage()
        if internal_name == "SetpointManager:MultiZone:MinimumHumidity:Average":
            return SetpointManagerMultiZoneMinimumHumidityAverage()
        if internal_name == "SetpointManager:MultiZone:MaximumHumidity:Average":
            return SetpointManagerMultiZoneMaximumHumidityAverage()
        if internal_name == "SetpointManager:MultiZone:Humidity:Minimum":
            return SetpointManagerMultiZoneHumidityMinimum()
        if internal_name == "SetpointManager:MultiZone:Humidity:Maximum":
            return SetpointManagerMultiZoneHumidityMaximum()
        if internal_name == "SetpointManager:FollowOutdoorAirTemperature":
            return SetpointManagerFollowOutdoorAirTemperature()
        if internal_name == "SetpointManager:FollowSystemNodeTemperature":
            return SetpointManagerFollowSystemNodeTemperature()
        if internal_name == "SetpointManager:FollowGroundTemperature":
            return SetpointManagerFollowGroundTemperature()
        if internal_name == "SetpointManager:CondenserEnteringReset":
            return SetpointManagerCondenserEnteringReset()
        if internal_name == "SetpointManager:CondenserEnteringReset:Ideal":
            return SetpointManagerCondenserEnteringResetIdeal()
        if internal_name == "SetpointManager:SingleZone:OneStageCooling":
            return SetpointManagerSingleZoneOneStageCooling()
        if internal_name == "SetpointManager:SingleZone:OneStageHeating":
            return SetpointManagerSingleZoneOneStageHeating()
        if internal_name == "Refrigeration:Case":
            return RefrigerationCase()
        if internal_name == "Refrigeration:CompressorRack":
            return RefrigerationCompressorRack()
        if internal_name == "Refrigeration:CaseAndWalkInList":
            return RefrigerationCaseAndWalkInList()
        if internal_name == "Refrigeration:Condenser:AirCooled":
            return RefrigerationCondenserAirCooled()
        if internal_name == "Refrigeration:Condenser:EvaporativeCooled":
            return RefrigerationCondenserEvaporativeCooled()
        if internal_name == "Refrigeration:Condenser:WaterCooled":
            return RefrigerationCondenserWaterCooled()
        if internal_name == "Refrigeration:Condenser:Cascade":
            return RefrigerationCondenserCascade()
        if internal_name == "Refrigeration:GasCooler:AirCooled":
            return RefrigerationGasCoolerAirCooled()
        if internal_name == "Refrigeration:TransferLoadList":
            return RefrigerationTransferLoadList()
        if internal_name == "Refrigeration:Subcooler":
            return RefrigerationSubcooler()
        if internal_name == "Refrigeration:Compressor":
            return RefrigerationCompressor()
        if internal_name == "Refrigeration:CompressorList":
            return RefrigerationCompressorList()
        if internal_name == "Refrigeration:System":
            return RefrigerationSystem()
        if internal_name == "Refrigeration:TranscriticalSystem":
            return RefrigerationTranscriticalSystem()
        if internal_name == "Refrigeration:SecondarySystem":
            return RefrigerationSecondarySystem()
        if internal_name == "Refrigeration:WalkIn":
            return RefrigerationWalkIn()
        if internal_name == "Refrigeration:AirChiller":
            return RefrigerationAirChiller()
        if internal_name == "DemandManagerAssignmentList":
            return DemandManagerAssignmentList()
        if internal_name == "DemandManager:ExteriorLights":
            return DemandManagerExteriorLights()
        if internal_name == "DemandManager:Lights":
            return DemandManagerLights()
        if internal_name == "DemandManager:ElectricEquipment":
            return DemandManagerElectricEquipment()
        if internal_name == "DemandManager:Thermostats":
            return DemandManagerThermostats()
        if internal_name == "Generator:InternalCombustionEngine":
            return GeneratorInternalCombustionEngine()
        if internal_name == "Generator:CombustionTurbine":
            return GeneratorCombustionTurbine()
        if internal_name == "Generator:MicroTurbine":
            return GeneratorMicroTurbine()
        if internal_name == "Generator:Photovoltaic":
            return GeneratorPhotovoltaic()
        if internal_name == "PhotovoltaicPerformance:Simple":
            return PhotovoltaicPerformanceSimple()
        if internal_name == "PhotovoltaicPerformance:EquivalentOne-Diode":
            return PhotovoltaicPerformanceEquivalentOneDiode()
        if internal_name == "PhotovoltaicPerformance:Sandia":
            return PhotovoltaicPerformanceSandia()
        if internal_name == "Generator:FuelCell":
            return GeneratorFuelCell()
        if internal_name == "Generator:FuelCell:PowerModule":
            return GeneratorFuelCellPowerModule()
        if internal_name == "Generator:FuelCell:AirSupply":
            return GeneratorFuelCellAirSupply()
        if internal_name == "Generator:FuelCell:WaterSupply":
            return GeneratorFuelCellWaterSupply()
        if internal_name == "Generator:FuelCell:AuxiliaryHeater":
            return GeneratorFuelCellAuxiliaryHeater()
        if internal_name == "Generator:FuelCell:ExhaustGasToWaterHeatExchanger":
            return GeneratorFuelCellExhaustGasToWaterHeatExchanger()
        if internal_name == "Generator:FuelCell:ElectricalStorage":
            return GeneratorFuelCellElectricalStorage()
        if internal_name == "Generator:FuelCell:Inverter":
            return GeneratorFuelCellInverter()
        if internal_name == "Generator:FuelCell:StackCooler":
            return GeneratorFuelCellStackCooler()
        if internal_name == "Generator:MicroCHP":
            return GeneratorMicroChp()
        if internal_name == "Generator:MicroCHP:NonNormalizedParameters":
            return GeneratorMicroChpNonNormalizedParameters()
        if internal_name == "Generator:FuelSupply":
            return GeneratorFuelSupply()
        if internal_name == "Generator:WindTurbine":
            return GeneratorWindTurbine()
        if internal_name == "ElectricLoadCenter:Generators":
            return ElectricLoadCenterGenerators()
        if internal_name == "ElectricLoadCenter:Inverter:Simple":
            return ElectricLoadCenterInverterSimple()
        if internal_name == "ElectricLoadCenter:Inverter:FunctionOfPower":
            return ElectricLoadCenterInverterFunctionOfPower()
        if internal_name == "ElectricLoadCenter:Inverter:LookUpTable":
            return ElectricLoadCenterInverterLookUpTable()
        if internal_name == "ElectricLoadCenter:Storage:Simple":
            return ElectricLoadCenterStorageSimple()
        if internal_name == "ElectricLoadCenter:Storage:Battery":
            return ElectricLoadCenterStorageBattery()
        if internal_name == "ElectricLoadCenter:Transformer":
            return ElectricLoadCenterTransformer()
        if internal_name == "ElectricLoadCenter:Distribution":
            return ElectricLoadCenterDistribution()
        if internal_name == "WaterUse:Equipment":
            return WaterUseEquipment()
        if internal_name == "WaterUse:Connections":
            return WaterUseConnections()
        if internal_name == "WaterUse:Storage":
            return WaterUseStorage()
        if internal_name == "WaterUse:Well":
            return WaterUseWell()
        if internal_name == "WaterUse:RainCollector":
            return WaterUseRainCollector()
        if internal_name == "FaultModel:TemperatureSensorOffset:OutdoorAir":
            return FaultModelTemperatureSensorOffsetOutdoorAir()
        if internal_name == "FaultModel:HumiditySensorOffset:OutdoorAir":
            return FaultModelHumiditySensorOffsetOutdoorAir()
        if internal_name == "FaultModel:EnthalpySensorOffset:OutdoorAir":
            return FaultModelEnthalpySensorOffsetOutdoorAir()
        if internal_name == "FaultModel:PressureSensorOffset:OutdoorAir":
            return FaultModelPressureSensorOffsetOutdoorAir()
        if internal_name == "FaultModel:TemperatureSensorOffset:ReturnAir":
            return FaultModelTemperatureSensorOffsetReturnAir()
        if internal_name == "FaultModel:EnthalpySensorOffset:ReturnAir":
            return FaultModelEnthalpySensorOffsetReturnAir()
        if internal_name == "FaultModel:Fouling:Coil":
            return FaultModelFoulingCoil()
        if internal_name == "Curve:Linear":
            return CurveLinear()
        if internal_name == "Curve:QuadLinear":
            return CurveQuadLinear()
        if internal_name == "Curve:Quadratic":
            return CurveQuadratic()
        if internal_name == "Curve:Cubic":
            return CurveCubic()
        if internal_name == "Curve:Quartic":
            return CurveQuartic()
        if internal_name == "Curve:Exponent":
            return CurveExponent()
        if internal_name == "Curve:Bicubic":
            return CurveBicubic()
        if internal_name == "Curve:Biquadratic":
            return CurveBiquadratic()
        if internal_name == "Curve:QuadraticLinear":
            return CurveQuadraticLinear()
        if internal_name == "Curve:Triquadratic":
            return CurveTriquadratic()
        if internal_name == "Curve:Functional:PressureDrop":
            return CurveFunctionalPressureDrop()
        if internal_name == "Curve:FanPressureRise":
            return CurveFanPressureRise()
        if internal_name == "Curve:ExponentialSkewNormal":
            return CurveExponentialSkewNormal()
        if internal_name == "Curve:Sigmoid":
            return CurveSigmoid()
        if internal_name == "Curve:RectangularHyperbola1":
            return CurveRectangularHyperbola1()
        if internal_name == "Curve:RectangularHyperbola2":
            return CurveRectangularHyperbola2()
        if internal_name == "Curve:ExponentialDecay":
            return CurveExponentialDecay()
        if internal_name == "Curve:DoubleExponentialDecay":
            return CurveDoubleExponentialDecay()
        if internal_name == "FluidProperties:Name":
            return FluidPropertiesName()
        if internal_name == "FluidProperties:GlycolConcentration":
            return FluidPropertiesGlycolConcentration()
        if internal_name == "FluidProperties:Temperatures":
            return FluidPropertiesTemperatures()
        if internal_name == "FluidProperties:Saturated":
            return FluidPropertiesSaturated()
        if internal_name == "FluidProperties:Superheated":
            return FluidPropertiesSuperheated()
        if internal_name == "FluidProperties:Concentration":
            return FluidPropertiesConcentration()
        if internal_name == "CurrencyType":
            return CurrencyType()
        if internal_name == "ComponentCost:Adjustments":
            return ComponentCostAdjustments()
        if internal_name == "ComponentCost:Reference":
            return ComponentCostReference()
        if internal_name == "ComponentCost:LineItem":
            return ComponentCostLineItem()
        if internal_name == "UtilityCost:Tariff":
            return UtilityCostTariff()
        if internal_name == "UtilityCost:Qualify":
            return UtilityCostQualify()
        if internal_name == "UtilityCost:Charge:Simple":
            return UtilityCostChargeSimple()
        if internal_name == "UtilityCost:Charge:Block":
            return UtilityCostChargeBlock()
        if internal_name == "UtilityCost:Ratchet":
            return UtilityCostRatchet()
        if internal_name == "UtilityCost:Variable":
            return UtilityCostVariable()
        if internal_name == "UtilityCost:Computation":
            return UtilityCostComputation()
        if internal_name == "LifeCycleCost:Parameters":
            return LifeCycleCostParameters()
        if internal_name == "LifeCycleCost:RecurringCosts":
            return LifeCycleCostRecurringCosts()
        if internal_name == "LifeCycleCost:NonrecurringCost":
            return LifeCycleCostNonrecurringCost()
        if internal_name == "LifeCycleCost:UsePriceEscalation":
            return LifeCycleCostUsePriceEscalation()
        if internal_name == "LifeCycleCost:UseAdjustment":
            return LifeCycleCostUseAdjustment()
        if internal_name == "Parametric:SetValueForRun":
            return ParametricSetValueForRun()
        if internal_name == "Parametric:Logic":
            return ParametricLogic()
        if internal_name == "Parametric:RunControl":
            return ParametricRunControl()
        if internal_name == "Parametric:FileNameSuffix":
            return ParametricFileNameSuffix()
        if internal_name == "Output:VariableDictionary":
            return OutputVariableDictionary()
        if internal_name == "Output:Surfaces:List":
            return OutputSurfacesList()
        if internal_name == "Output:Surfaces:Drawing":
            return OutputSurfacesDrawing()
        if internal_name == "Output:Schedules":
            return OutputSchedules()
        if internal_name == "Output:Constructions":
            return OutputConstructions()
        if internal_name == "Output:EnergyManagementSystem":
            return OutputEnergyManagementSystem()
        if internal_name == "OutputControl:SurfaceColorScheme":
            return OutputControlSurfaceColorScheme()
        if internal_name == "Output:Table:SummaryReports":
            return OutputTableSummaryReports()
        if internal_name == "Output:Table:TimeBins":
            return OutputTableTimeBins()
        if internal_name == "Output:Table:Monthly":
            return OutputTableMonthly()
        if internal_name == "OutputControl:Table:Style":
            return OutputControlTableStyle()
        if internal_name == "OutputControl:ReportingTolerances":
            return OutputControlReportingTolerances()
        if internal_name == "Output:Variable":
            return OutputVariable()
        if internal_name == "Output:Meter":
            return OutputMeter()
        if internal_name == "Output:Meter:MeterFileOnly":
            return OutputMeterMeterFileOnly()
        if internal_name == "Output:Meter:Cumulative":
            return OutputMeterCumulative()
        if internal_name == "Output:Meter:Cumulative:MeterFileOnly":
            return OutputMeterCumulativeMeterFileOnly()
        if internal_name == "Meter:Custom":
            return MeterCustom()
        if internal_name == "Meter:CustomDecrement":
            return MeterCustomDecrement()
        if internal_name == "Output:SQLite":
            return OutputSqlite()
        if internal_name == "Output:EnvironmentalImpactFactors":
            return OutputEnvironmentalImpactFactors()
        if internal_name == "EnvironmentalImpactFactors":
            return EnvironmentalImpactFactors()
        if internal_name == "FuelFactors":
            return FuelFactors()
        if internal_name == "Output:Diagnostics":
            return OutputDiagnostics()
        if internal_name == "Output:DebuggingData":
            return OutputDebuggingData()
        if internal_name == "Output:PreprocessorMessage":
            return OutputPreprocessorMessage()
        raise ValueError("No DataDictionary known for {}".format(internal_name))

    def read(self, path):
        """Read IDF data from path
        
           Args:
               path (str): path to read data from
        """
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                match_obj_name = re.search(r"^([A-Z][A-Z/ \d]+),", line)
                if match_obj_name is not None:
                    internal_name = match_obj_name.group(1)
                    if internal_name in self._data:
                        self._data[internal_name] = self._create_datadict(internal_name)
                        data_line = line[len(internal_name) + 1:]
                        vals = data_line.strip().split(',')
                        self._data[internal_name].read(vals)