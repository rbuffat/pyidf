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

    required_objects = ["Building", "GlobalGeometryRules"]
    unique_objects = [
        "HVACTemplate:Plant:MixedWaterLoop",
        "SurfaceConvectionAlgorithm:Inside",
        "Site:Location",
        "RunPeriodControl:DaylightSavingTime",
        "ShadowCalculation",
        "ZoneAirContaminantBalance",
        "Site:GroundTemperature:Shallow",
        "Compliance:Building",
        "Parametric:FileNameSuffix",
        "Site:GroundReflectance",
        "OutputControl:Sizing:Style",
        "ZoneAirHeatBalanceAlgorithm",
        "OutputControl:ReportingTolerances",
        "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections",
        "Output:SQLite",
        "HeatBalanceSettings:ConductionFiniteDifference",
        "Building",
        "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections",
        "GeometryTransform",
        "SurfaceConvectionAlgorithm:Outside",
        "CurrencyType",
        "Site:GroundTemperature:Deep",
        "Output:EnergyManagementSystem",
        "HVACTemplate:Plant:HotWaterLoop",
        "Timestep",
        "Parametric:Logic",
        "Sizing:Parameters",
        "Version",
        "LifeCycleCost:Parameters",
        "HeatBalanceAlgorithm",
        "Site:WeatherStation",
        "Output:Table:SummaryReports",
        "AirflowNetwork:SimulationControl",
        "Site:GroundTemperature:BuildingSurface",
        "HVACTemplate:Plant:ChilledWaterLoop",
        "SimulationControl",
        "Site:GroundTemperature:FCfactorMethod",
        "ConvergenceLimits",
        "ZoneAirMassFlowConservation",
        "ZoneCapacitanceMultiplier:ResearchSpecial",
        "OutputControl:Table:Style",
        "Parametric:RunControl",
        "Site:SolarAndVisibleSpectrum",
        "Output:DebuggingData",
        "GlobalGeometryRules",
        "OutputControl:IlluminanceMap:Style",
        "Site:HeightVariation"]

    def __init__(self):
        """ Inits IDF with no data dictionary set."""
        self._data = OrderedDict()
        self._data["Lead Input"] = []
        self._data["Simulation Data"] = []
        self._data["Version"] = []
        self._data["SimulationControl"] = []
        self._data["Building"] = []
        self._data["ShadowCalculation"] = []
        self._data["SurfaceConvectionAlgorithm:Inside"] = []
        self._data["SurfaceConvectionAlgorithm:Outside"] = []
        self._data["HeatBalanceAlgorithm"] = []
        self._data["HeatBalanceSettings:ConductionFiniteDifference"] = []
        self._data["ZoneAirHeatBalanceAlgorithm"] = []
        self._data["ZoneAirContaminantBalance"] = []
        self._data["ZoneAirMassFlowConservation"] = []
        self._data["ZoneCapacitanceMultiplier:ResearchSpecial"] = []
        self._data["Timestep"] = []
        self._data["ConvergenceLimits"] = []
        self._data["ProgramControl"] = []
        self._data["Compliance:Building"] = []
        self._data["Site:Location"] = []
        self._data["SizingPeriod:DesignDay"] = []
        self._data["SizingPeriod:WeatherFileDays"] = []
        self._data["SizingPeriod:WeatherFileConditionType"] = []
        self._data["RunPeriod"] = []
        self._data["RunPeriod:CustomRange"] = []
        self._data["RunPeriodControl:SpecialDays"] = []
        self._data["RunPeriodControl:DaylightSavingTime"] = []
        self._data["WeatherProperty:SkyTemperature"] = []
        self._data["Site:WeatherStation"] = []
        self._data["Site:HeightVariation"] = []
        self._data["Site:GroundTemperature:BuildingSurface"] = []
        self._data["Site:GroundTemperature:FCfactorMethod"] = []
        self._data["Site:GroundTemperature:Shallow"] = []
        self._data["Site:GroundTemperature:Deep"] = []
        self._data["Site:GroundDomain"] = []
        self._data["Site:GroundReflectance"] = []
        self._data["Site:GroundReflectance:SnowModifier"] = []
        self._data["Site:WaterMainsTemperature"] = []
        self._data["Site:Precipitation"] = []
        self._data["RoofIrrigation"] = []
        self._data["Site:SolarAndVisibleSpectrum"] = []
        self._data["Site:SpectrumData"] = []
        self._data["ScheduleTypeLimits"] = []
        self._data["Schedule:Day:Hourly"] = []
        self._data["Schedule:Day:Interval"] = []
        self._data["Schedule:Week:Daily"] = []
        self._data["Schedule:Week:Compact"] = []
        self._data["Schedule:Constant"] = []
        self._data["Schedule:File"] = []
        self._data["Material"] = []
        self._data["Material:NoMass"] = []
        self._data["Material:InfraredTransparent"] = []
        self._data["Material:AirGap"] = []
        self._data["Material:RoofVegetation"] = []
        self._data["WindowMaterial:SimpleGlazingSystem"] = []
        self._data["WindowMaterial:Glazing"] = []
        self._data["WindowMaterial:GlazingGroup:Thermochromic"] = []
        self._data["WindowMaterial:Glazing:RefractionExtinctionMethod"] = []
        self._data["WindowMaterial:Gas"] = []
        self._data["WindowGap:SupportPillar"] = []
        self._data["WindowGap:DeflectionState"] = []
        self._data["WindowMaterial:GasMixture"] = []
        self._data["WindowMaterial:Gap"] = []
        self._data["WindowMaterial:Shade"] = []
        self._data["WindowMaterial:ComplexShade"] = []
        self._data["WindowMaterial:Blind"] = []
        self._data["WindowMaterial:Screen"] = []
        self._data["WindowMaterial:Shade:EquivalentLayer"] = []
        self._data["WindowMaterial:Drape:EquivalentLayer"] = []
        self._data["WindowMaterial:Blind:EquivalentLayer"] = []
        self._data["WindowMaterial:Screen:EquivalentLayer"] = []
        self._data["WindowMaterial:Glazing:EquivalentLayer"] = []
        self._data["Construction:WindowEquivalentLayer"] = []
        self._data["WindowMaterial:Gap:EquivalentLayer"] = []
        self._data["MaterialProperty:MoisturePenetrationDepth:Settings"] = []
        self._data["MaterialProperty:PhaseChange"] = []
        self._data["MaterialProperty:VariableThermalConductivity"] = []
        self._data["MaterialProperty:HeatAndMoistureTransfer:Settings"] = []
        self._data[
            "MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm"] = []
        self._data["MaterialProperty:HeatAndMoistureTransfer:Suction"] = []
        self._data[
            "MaterialProperty:HeatAndMoistureTransfer:Redistribution"] = []
        self._data["MaterialProperty:HeatAndMoistureTransfer:Diffusion"] = []
        self._data[
            "MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity"] = []
        self._data["Construction"] = []
        self._data["Construction:CfactorUndergroundWall"] = []
        self._data["Construction:FfactorGroundFloor"] = []
        self._data["Construction:InternalSource"] = []
        self._data["WindowThermalModel:Params"] = []
        self._data["Construction:ComplexFenestrationState"] = []
        self._data["Construction:WindowDataFile"] = []
        self._data["GlobalGeometryRules"] = []
        self._data["GeometryTransform"] = []
        self._data["Zone"] = []
        self._data["ZoneGroup"] = []
        self._data["BuildingSurface:Detailed"] = []
        self._data["Wall:Detailed"] = []
        self._data["RoofCeiling:Detailed"] = []
        self._data["Floor:Detailed"] = []
        self._data["Wall:Exterior"] = []
        self._data["Wall:Adiabatic"] = []
        self._data["Wall:Underground"] = []
        self._data["Wall:Interzone"] = []
        self._data["Roof"] = []
        self._data["Ceiling:Adiabatic"] = []
        self._data["Ceiling:Interzone"] = []
        self._data["Floor:GroundContact"] = []
        self._data["Floor:Adiabatic"] = []
        self._data["Floor:Interzone"] = []
        self._data["FenestrationSurface:Detailed"] = []
        self._data["Window"] = []
        self._data["Door"] = []
        self._data["GlazedDoor"] = []
        self._data["Window:Interzone"] = []
        self._data["Door:Interzone"] = []
        self._data["GlazedDoor:Interzone"] = []
        self._data["WindowProperty:ShadingControl"] = []
        self._data["WindowProperty:FrameAndDivider"] = []
        self._data["WindowProperty:AirflowControl"] = []
        self._data["WindowProperty:StormWindow"] = []
        self._data["InternalMass"] = []
        self._data["Shading:Site"] = []
        self._data["Shading:Building"] = []
        self._data["Shading:Site:Detailed"] = []
        self._data["Shading:Building:Detailed"] = []
        self._data["Shading:Overhang"] = []
        self._data["Shading:Overhang:Projection"] = []
        self._data["Shading:Fin"] = []
        self._data["Shading:Fin:Projection"] = []
        self._data["Shading:Zone:Detailed"] = []
        self._data["ShadingProperty:Reflectance"] = []
        self._data["SurfaceProperty:HeatTransferAlgorithm"] = []
        self._data[
            "SurfaceProperty:HeatTransferAlgorithm:MultipleSurface"] = []
        self._data["SurfaceProperty:HeatTransferAlgorithm:SurfaceList"] = []
        self._data["SurfaceProperty:HeatTransferAlgorithm:Construction"] = []
        self._data["SurfaceControl:MovableInsulation"] = []
        self._data["SurfaceProperty:OtherSideCoefficients"] = []
        self._data["SurfaceProperty:OtherSideConditionsModel"] = []
        self._data[
            "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections"] = []
        self._data[
            "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections"] = []
        self._data["SurfaceConvectionAlgorithm:Inside:UserCurve"] = []
        self._data["SurfaceConvectionAlgorithm:Outside:UserCurve"] = []
        self._data["SurfaceProperty:ConvectionCoefficients"] = []
        self._data[
            "SurfaceProperty:ConvectionCoefficients:MultipleSurface"] = []
        self._data["SurfaceProperties:VaporCoefficients"] = []
        self._data["SurfaceProperty:ExteriorNaturalVentedCavity"] = []
        self._data["SurfaceProperty:SolarIncidentInside"] = []
        self._data["ComplexFenestrationProperty:SolarAbsorbedLayers"] = []
        self._data["ZoneProperty:UserViewFactors:bySurfaceName"] = []
        self._data["GroundHeatTransfer:Control"] = []
        self._data["GroundHeatTransfer:Slab:Materials"] = []
        self._data["GroundHeatTransfer:Slab:MatlProps"] = []
        self._data["GroundHeatTransfer:Slab:BoundConds"] = []
        self._data["GroundHeatTransfer:Slab:BldgProps"] = []
        self._data["GroundHeatTransfer:Slab:Insulation"] = []
        self._data["GroundHeatTransfer:Slab:EquivalentSlab"] = []
        self._data["GroundHeatTransfer:Slab:AutoGrid"] = []
        self._data["GroundHeatTransfer:Slab:ManualGrid"] = []
        self._data["GroundHeatTransfer:Basement:SimParameters"] = []
        self._data["GroundHeatTransfer:Basement:MatlProps"] = []
        self._data["GroundHeatTransfer:Basement:Insulation"] = []
        self._data["GroundHeatTransfer:Basement:SurfaceProps"] = []
        self._data["GroundHeatTransfer:Basement:BldgData"] = []
        self._data["GroundHeatTransfer:Basement:Interior"] = []
        self._data["GroundHeatTransfer:Basement:ComBldg"] = []
        self._data["GroundHeatTransfer:Basement:EquivSlab"] = []
        self._data["GroundHeatTransfer:Basement:EquivAutoGrid"] = []
        self._data["GroundHeatTransfer:Basement:AutoGrid"] = []
        self._data["GroundHeatTransfer:Basement:ManualGrid"] = []
        self._data["RoomAirModelType"] = []
        self._data["RoomAir:TemperaturePattern:UserDefined"] = []
        self._data["RoomAir:TemperaturePattern:ConstantGradient"] = []
        self._data["RoomAir:TemperaturePattern:TwoGradient"] = []
        self._data["RoomAir:TemperaturePattern:NondimensionalHeight"] = []
        self._data["RoomAir:TemperaturePattern:SurfaceMapping"] = []
        self._data["RoomAir:Node"] = []
        self._data["RoomAirSettings:OneNodeDisplacementVentilation"] = []
        self._data["RoomAirSettings:ThreeNodeDisplacementVentilation"] = []
        self._data["RoomAirSettings:CrossVentilation"] = []
        self._data["RoomAirSettings:UnderFloorAirDistributionInterior"] = []
        self._data["RoomAirSettings:UnderFloorAirDistributionExterior"] = []
        self._data["People"] = []
        self._data["ComfortViewFactorAngles"] = []
        self._data["Lights"] = []
        self._data["ElectricEquipment"] = []
        self._data["GasEquipment"] = []
        self._data["HotWaterEquipment"] = []
        self._data["SteamEquipment"] = []
        self._data["OtherEquipment"] = []
        self._data["ZoneBaseboard:OutdoorTemperatureControlled"] = []
        self._data["ZoneContaminantSourceAndSink:CarbonDioxide"] = []
        self._data["ZoneContaminantSourceAndSink:Generic:Constant"] = []
        self._data[
            "SurfaceContaminantSourceAndSink:Generic:PressureDriven"] = []
        self._data["ZoneContaminantSourceAndSink:Generic:CutoffModel"] = []
        self._data["ZoneContaminantSourceAndSink:Generic:DecaySource"] = []
        self._data[
            "SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"] = []
        self._data[
            "SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"] = []
        self._data[
            "ZoneContaminantSourceAndSink:Generic:DepositionRateSink"] = []
        self._data["Daylighting:Controls"] = []
        self._data["Daylighting:DELight:Controls"] = []
        self._data["Daylighting:DELight:ReferencePoint"] = []
        self._data["Daylighting:DELight:ComplexFenestration"] = []
        self._data["DaylightingDevice:Tubular"] = []
        self._data["DaylightingDevice:Shelf"] = []
        self._data["DaylightingDevice:LightWell"] = []
        self._data["Output:DaylightFactors"] = []
        self._data["Output:IlluminanceMap"] = []
        self._data["OutputControl:IlluminanceMap:Style"] = []
        self._data["ZoneInfiltration:DesignFlowRate"] = []
        self._data["ZoneInfiltration:EffectiveLeakageArea"] = []
        self._data["ZoneInfiltration:FlowCoefficient"] = []
        self._data["ZoneVentilation:DesignFlowRate"] = []
        self._data["ZoneVentilation:WindandStackOpenArea"] = []
        self._data["ZoneAirBalance:OutdoorAir"] = []
        self._data["ZoneMixing"] = []
        self._data["ZoneCrossMixing"] = []
        self._data["ZoneRefrigerationDoorMixing"] = []
        self._data["ZoneEarthtube"] = []
        self._data["ZoneCoolTower:Shower"] = []
        self._data["ZoneThermalChimney"] = []
        self._data["AirflowNetwork:SimulationControl"] = []
        self._data["AirflowNetwork:MultiZone:Zone"] = []
        self._data["AirflowNetwork:MultiZone:Surface"] = []
        self._data["AirflowNetwork:MultiZone:ReferenceCrackConditions"] = []
        self._data["AirflowNetwork:MultiZone:Surface:Crack"] = []
        self._data[
            "AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea"] = []
        self._data["AirflowNetwork:MultiZone:Component:DetailedOpening"] = []
        self._data["AirflowNetwork:MultiZone:Component:SimpleOpening"] = []
        self._data["AirflowNetwork:MultiZone:Component:HorizontalOpening"] = []
        self._data["AirflowNetwork:MultiZone:Component:ZoneExhaustFan"] = []
        self._data["AirflowNetwork:MultiZone:ExternalNode"] = []
        self._data[
            "AirflowNetwork:MultiZone:WindPressureCoefficientArray"] = []
        self._data[
            "AirflowNetwork:MultiZone:WindPressureCoefficientValues"] = []
        self._data["AirflowNetwork:Distribution:Node"] = []
        self._data["AirflowNetwork:Distribution:Component:Leak"] = []
        self._data["AirflowNetwork:Distribution:Component:LeakageRatio"] = []
        self._data["AirflowNetwork:Distribution:Component:Duct"] = []
        self._data["AirflowNetwork:Distribution:Component:Fan"] = []
        self._data["AirflowNetwork:Distribution:Component:Coil"] = []
        self._data["AirflowNetwork:Distribution:Component:HeatExchanger"] = []
        self._data["AirflowNetwork:Distribution:Component:TerminalUnit"] = []
        self._data[
            "AirflowNetwork:Distribution:Component:ConstantPressureDrop"] = []
        self._data["AirflowNetwork:Distribution:Linkage"] = []
        self._data["Exterior:Lights"] = []
        self._data["Exterior:FuelEquipment"] = []
        self._data["Exterior:WaterEquipment"] = []
        self._data["HVACTemplate:Thermostat"] = []
        self._data["HVACTemplate:Zone:IdealLoadsAirSystem"] = []
        self._data["HVACTemplate:Zone:BaseboardHeat"] = []
        self._data["HVACTemplate:Zone:FanCoil"] = []
        self._data["HVACTemplate:Zone:PTAC"] = []
        self._data["HVACTemplate:Zone:PTHP"] = []
        self._data["HVACTemplate:Zone:WaterToAirHeatPump"] = []
        self._data["HVACTemplate:Zone:VRF"] = []
        self._data["HVACTemplate:Zone:Unitary"] = []
        self._data["HVACTemplate:Zone:VAV"] = []
        self._data["HVACTemplate:Zone:VAV:FanPowered"] = []
        self._data["HVACTemplate:Zone:VAV:HeatAndCool"] = []
        self._data["HVACTemplate:Zone:ConstantVolume"] = []
        self._data["HVACTemplate:Zone:DualDuct"] = []
        self._data["HVACTemplate:System:VRF"] = []
        self._data["HVACTemplate:System:Unitary"] = []
        self._data["HVACTemplate:System:UnitaryHeatPump:AirToAir"] = []
        self._data["HVACTemplate:System:UnitarySystem"] = []
        self._data["HVACTemplate:System:VAV"] = []
        self._data["HVACTemplate:System:PackagedVAV"] = []
        self._data["HVACTemplate:System:ConstantVolume"] = []
        self._data["HVACTemplate:System:DualDuct"] = []
        self._data["HVACTemplate:System:DedicatedOutdoorAir"] = []
        self._data["HVACTemplate:Plant:ChilledWaterLoop"] = []
        self._data["HVACTemplate:Plant:Chiller"] = []
        self._data["HVACTemplate:Plant:Chiller:ObjectReference"] = []
        self._data["HVACTemplate:Plant:Tower"] = []
        self._data["HVACTemplate:Plant:Tower:ObjectReference"] = []
        self._data["HVACTemplate:Plant:HotWaterLoop"] = []
        self._data["HVACTemplate:Plant:Boiler"] = []
        self._data["HVACTemplate:Plant:Boiler:ObjectReference"] = []
        self._data["HVACTemplate:Plant:MixedWaterLoop"] = []
        self._data["DesignSpecification:OutdoorAir"] = []
        self._data["DesignSpecification:ZoneAirDistribution"] = []
        self._data["Sizing:Parameters"] = []
        self._data["Sizing:Zone"] = []
        self._data["DesignSpecification:ZoneHVAC:Sizing"] = []
        self._data["Sizing:System"] = []
        self._data["Sizing:Plant"] = []
        self._data["OutputControl:Sizing:Style"] = []
        self._data["ZoneControl:Humidistat"] = []
        self._data["ZoneControl:Thermostat"] = []
        self._data["ZoneControl:Thermostat:OperativeTemperature"] = []
        self._data["ZoneControl:Thermostat:ThermalComfort"] = []
        self._data["ZoneControl:Thermostat:TemperatureAndHumidity"] = []
        self._data["ThermostatSetpoint:SingleHeating"] = []
        self._data["ThermostatSetpoint:SingleCooling"] = []
        self._data["ThermostatSetpoint:SingleHeatingOrCooling"] = []
        self._data["ThermostatSetpoint:DualSetpoint"] = []
        self._data[
            "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"] = []
        self._data[
            "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"] = []
        self._data[
            "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"] = []
        self._data[
            "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"] = []
        self._data["ZoneControl:Thermostat:StagedDualSetpoint"] = []
        self._data["ZoneControl:ContaminantController"] = []
        self._data["ZoneHVAC:IdealLoadsAirSystem"] = []
        self._data["ZoneHVAC:FourPipeFanCoil"] = []
        self._data["ZoneHVAC:WindowAirConditioner"] = []
        self._data["ZoneHVAC:PackagedTerminalAirConditioner"] = []
        self._data["ZoneHVAC:PackagedTerminalHeatPump"] = []
        self._data["ZoneHVAC:WaterToAirHeatPump"] = []
        self._data["ZoneHVAC:Dehumidifier:DX"] = []
        self._data["ZoneHVAC:EnergyRecoveryVentilator"] = []
        self._data["ZoneHVAC:EnergyRecoveryVentilator:Controller"] = []
        self._data["ZoneHVAC:UnitVentilator"] = []
        self._data["ZoneHVAC:UnitHeater"] = []
        self._data["ZoneHVAC:EvaporativeCoolerUnit"] = []
        self._data["ZoneHVAC:OutdoorAirUnit"] = []
        self._data["ZoneHVAC:OutdoorAirUnit:EquipmentList"] = []
        self._data["ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"] = []
        self._data["ZoneHVAC:Baseboard:RadiantConvective:Water"] = []
        self._data["ZoneHVAC:Baseboard:RadiantConvective:Steam"] = []
        self._data["ZoneHVAC:Baseboard:RadiantConvective:Electric"] = []
        self._data["ZoneHVAC:Baseboard:Convective:Water"] = []
        self._data["ZoneHVAC:Baseboard:Convective:Electric"] = []
        self._data["ZoneHVAC:LowTemperatureRadiant:VariableFlow"] = []
        self._data["ZoneHVAC:LowTemperatureRadiant:ConstantFlow"] = []
        self._data["ZoneHVAC:LowTemperatureRadiant:Electric"] = []
        self._data["ZoneHVAC:LowTemperatureRadiant:SurfaceGroup"] = []
        self._data["ZoneHVAC:HighTemperatureRadiant"] = []
        self._data["ZoneHVAC:VentilatedSlab"] = []
        self._data["ZoneHVAC:VentilatedSlab:SlabGroup"] = []
        self._data["AirTerminal:SingleDuct:Uncontrolled"] = []
        self._data["AirTerminal:SingleDuct:ConstantVolume:Reheat"] = []
        self._data["AirTerminal:SingleDuct:VAV:NoReheat"] = []
        self._data["AirTerminal:SingleDuct:VAV:Reheat"] = []
        self._data["AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan"] = []
        self._data["AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"] = []
        self._data["AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"] = []
        self._data["AirTerminal:SingleDuct:SeriesPIU:Reheat"] = []
        self._data["AirTerminal:SingleDuct:ParallelPIU:Reheat"] = []
        self._data[
            "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"] = []
        self._data["AirTerminal:SingleDuct:ConstantVolume:CooledBeam"] = []
        self._data["AirTerminal:SingleDuct:InletSideMixer"] = []
        self._data["AirTerminal:SingleDuct:SupplySideMixer"] = []
        self._data["AirTerminal:DualDuct:ConstantVolume"] = []
        self._data["AirTerminal:DualDuct:VAV"] = []
        self._data["AirTerminal:DualDuct:VAV:OutdoorAir"] = []
        self._data["ZoneHVAC:AirDistributionUnit"] = []
        self._data["ZoneHVAC:EquipmentList"] = []
        self._data["ZoneHVAC:EquipmentConnections"] = []
        self._data["Fan:ConstantVolume"] = []
        self._data["Fan:VariableVolume"] = []
        self._data["Fan:OnOff"] = []
        self._data["Fan:ZoneExhaust"] = []
        self._data["FanPerformance:NightVentilation"] = []
        self._data["Fan:ComponentModel"] = []
        self._data["Coil:Cooling:Water"] = []
        self._data["Coil:Cooling:Water:DetailedGeometry"] = []
        self._data["Coil:Cooling:DX:SingleSpeed"] = []
        self._data["Coil:Cooling:DX:TwoSpeed"] = []
        self._data["Coil:Cooling:DX:MultiSpeed"] = []
        self._data["Coil:Cooling:DX:VariableSpeed"] = []
        self._data["Coil:Cooling:DX:TwoStageWithHumidityControlMode"] = []
        self._data["CoilPerformance:DX:Cooling"] = []
        self._data["Coil:Cooling:DX:VariableRefrigerantFlow"] = []
        self._data["Coil:Heating:DX:VariableRefrigerantFlow"] = []
        self._data["Coil:Heating:Water"] = []
        self._data["Coil:Heating:Steam"] = []
        self._data["Coil:Heating:Electric"] = []
        self._data["Coil:Heating:Electric:MultiStage"] = []
        self._data["Coil:Heating:Gas"] = []
        self._data["Coil:Heating:Gas:MultiStage"] = []
        self._data["Coil:Heating:Desuperheater"] = []
        self._data["Coil:Heating:DX:SingleSpeed"] = []
        self._data["Coil:Heating:DX:MultiSpeed"] = []
        self._data["Coil:Heating:DX:VariableSpeed"] = []
        self._data["Coil:Cooling:WaterToAirHeatPump:ParameterEstimation"] = []
        self._data["Coil:Heating:WaterToAirHeatPump:ParameterEstimation"] = []
        self._data["Coil:Cooling:WaterToAirHeatPump:EquationFit"] = []
        self._data[
            "Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit"] = []
        self._data["Coil:Heating:WaterToAirHeatPump:EquationFit"] = []
        self._data[
            "Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit"] = []
        self._data["Coil:WaterHeating:AirToWaterHeatPump"] = []
        self._data["Coil:WaterHeating:Desuperheater"] = []
        self._data["CoilSystem:Cooling:DX"] = []
        self._data["CoilSystem:Heating:DX"] = []
        self._data["CoilSystem:Cooling:Water:HeatExchangerAssisted"] = []
        self._data["CoilSystem:Cooling:DX:HeatExchangerAssisted"] = []
        self._data["Coil:Cooling:DX:SingleSpeed:ThermalStorage"] = []
        self._data["Humidifier:Steam:Electric"] = []
        self._data["Dehumidifier:Desiccant:NoFans"] = []
        self._data["Dehumidifier:Desiccant:System"] = []
        self._data["HeatExchanger:AirToAir:FlatPlate"] = []
        self._data["HeatExchanger:AirToAir:SensibleAndLatent"] = []
        self._data["HeatExchanger:Desiccant:BalancedFlow"] = []
        self._data[
            "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"] = []
        self._data["AirLoopHVAC:UnitarySystem"] = []
        self._data["UnitarySystemPerformance:HeatPump:Multispeed"] = []
        self._data["AirLoopHVAC:Unitary:Furnace:HeatOnly"] = []
        self._data["AirLoopHVAC:Unitary:Furnace:HeatCool"] = []
        self._data["AirLoopHVAC:UnitaryHeatOnly"] = []
        self._data["AirLoopHVAC:UnitaryHeatCool"] = []
        self._data["AirLoopHVAC:UnitaryHeatPump:AirToAir"] = []
        self._data["AirLoopHVAC:UnitaryHeatPump:WaterToAir"] = []
        self._data["AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass"] = []
        self._data["AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed"] = []
        self._data["AirConditioner:VariableRefrigerantFlow"] = []
        self._data["ZoneTerminalUnitList"] = []
        self._data["Controller:WaterCoil"] = []
        self._data["Controller:OutdoorAir"] = []
        self._data["Controller:MechanicalVentilation"] = []
        self._data["AirLoopHVAC:ControllerList"] = []
        self._data["AirLoopHVAC"] = []
        self._data["AirLoopHVAC:OutdoorAirSystem:EquipmentList"] = []
        self._data["AirLoopHVAC:OutdoorAirSystem"] = []
        self._data["OutdoorAir:Mixer"] = []
        self._data["AirLoopHVAC:SupplyPath"] = []
        self._data["AirLoopHVAC:ReturnPath"] = []
        self._data["Branch"] = []
        self._data["ConnectorList"] = []
        self._data["OutdoorAir:Node"] = []
        self._data["Pipe:Adiabatic"] = []
        self._data["Pipe:Adiabatic:Steam"] = []
        self._data["Pipe:Indoor"] = []
        self._data["Pipe:Outdoor"] = []
        self._data["Pipe:Underground"] = []
        self._data["PipingSystem:Underground:Domain"] = []
        self._data["PipingSystem:Underground:PipeCircuit"] = []
        self._data["PipingSystem:Underground:PipeSegment"] = []
        self._data["Duct"] = []
        self._data["Pump:VariableSpeed"] = []
        self._data["Pump:ConstantSpeed"] = []
        self._data["Pump:VariableSpeed:Condensate"] = []
        self._data["HeaderedPumps:ConstantSpeed"] = []
        self._data["TemperingValve"] = []
        self._data["LoadProfile:Plant"] = []
        self._data["SolarCollectorPerformance:FlatPlate"] = []
        self._data["SolarCollector:FlatPlate:Water"] = []
        self._data["SolarCollectorPerformance:PhotovoltaicThermal:Simple"] = []
        self._data["SolarCollector:IntegralCollectorStorage"] = []
        self._data["SolarCollectorPerformance:IntegralCollectorStorage"] = []
        self._data["SolarCollector:UnglazedTranspired"] = []
        self._data["SolarCollector:UnglazedTranspired:Multisystem"] = []
        self._data["Boiler:HotWater"] = []
        self._data["Boiler:Steam"] = []
        self._data["Chiller:Electric:EIR"] = []
        self._data["Chiller:Electric:ReformulatedEIR"] = []
        self._data["Chiller:Electric"] = []
        self._data["Chiller:Absorption:Indirect"] = []
        self._data["Chiller:Absorption"] = []
        self._data["Chiller:ConstantCOP"] = []
        self._data["Chiller:EngineDriven"] = []
        self._data["Chiller:CombustionTurbine"] = []
        self._data["ChillerHeater:Absorption:DirectFired"] = []
        self._data["ChillerHeater:Absorption:DoubleEffect"] = []
        self._data["HeatPump:WaterToWater:EquationFit:Heating"] = []
        self._data["HeatPump:WaterToWater:EquationFit:Cooling"] = []
        self._data["HeatPump:WaterToWater:ParameterEstimation:Cooling"] = []
        self._data["HeatPump:WaterToWater:ParameterEstimation:Heating"] = []
        self._data["DistrictCooling"] = []
        self._data["DistrictHeating"] = []
        self._data["PlantComponent:TemperatureSource"] = []
        self._data["CentralHeatPumpSystem"] = []
        self._data["ChillerHeaterPerformance:Electric:EIR"] = []
        self._data["CoolingTower:SingleSpeed"] = []
        self._data["CoolingTower:TwoSpeed"] = []
        self._data["CoolingTower:VariableSpeed:Merkel"] = []
        self._data["CoolingTower:VariableSpeed"] = []
        self._data["CoolingTowerPerformance:CoolTools"] = []
        self._data["CoolingTowerPerformance:YorkCalc"] = []
        self._data["EvaporativeFluidCooler:SingleSpeed"] = []
        self._data["EvaporativeFluidCooler:TwoSpeed"] = []
        self._data["FluidCooler:SingleSpeed"] = []
        self._data["FluidCooler:TwoSpeed"] = []
        self._data["GroundHeatExchanger:Vertical"] = []
        self._data["GroundHeatExchanger:Pond"] = []
        self._data["GroundHeatExchanger:Surface"] = []
        self._data["GroundHeatExchanger:HorizontalTrench"] = []
        self._data["HeatExchanger:FluidToFluid"] = []
        self._data["WaterHeater:Mixed"] = []
        self._data["WaterHeater:Stratified"] = []
        self._data["WaterHeater:Sizing"] = []
        self._data["WaterHeater:HeatPump"] = []
        self._data["ThermalStorage:Ice:Simple"] = []
        self._data["ThermalStorage:Ice:Detailed"] = []
        self._data["ThermalStorage:ChilledWater:Mixed"] = []
        self._data["ThermalStorage:ChilledWater:Stratified"] = []
        self._data["PlantLoop"] = []
        self._data["CondenserLoop"] = []
        self._data["PlantEquipmentList"] = []
        self._data["CondenserEquipmentList"] = []
        self._data["PlantEquipmentOperation:Uncontrolled"] = []
        self._data["PlantEquipmentOperation:CoolingLoad"] = []
        self._data["PlantEquipmentOperation:HeatingLoad"] = []
        self._data["PlantEquipmentOperation:OutdoorDryBulb"] = []
        self._data["PlantEquipmentOperation:OutdoorWetBulb"] = []
        self._data["PlantEquipmentOperation:OutdoorRelativeHumidity"] = []
        self._data["PlantEquipmentOperation:OutdoorDewpoint"] = []
        self._data["PlantEquipmentOperation:ComponentSetpoint"] = []
        self._data["PlantEquipmentOperation:OutdoorDryBulbDifference"] = []
        self._data["PlantEquipmentOperation:OutdoorWetBulbDifference"] = []
        self._data["PlantEquipmentOperation:OutdoorDewpointDifference"] = []
        self._data["PlantEquipmentOperationSchemes"] = []
        self._data["CondenserEquipmentOperationSchemes"] = []
        self._data["EnergyManagementSystem:Sensor"] = []
        self._data["EnergyManagementSystem:Actuator"] = []
        self._data["EnergyManagementSystem:ProgramCallingManager"] = []
        self._data["EnergyManagementSystem:OutputVariable"] = []
        self._data["EnergyManagementSystem:MeteredOutputVariable"] = []
        self._data["EnergyManagementSystem:TrendVariable"] = []
        self._data["EnergyManagementSystem:InternalVariable"] = []
        self._data["EnergyManagementSystem:CurveOrTableIndexVariable"] = []
        self._data["EnergyManagementSystem:ConstructionIndexVariable"] = []
        self._data["ExternalInterface"] = []
        self._data["ExternalInterface:Schedule"] = []
        self._data["ExternalInterface:Variable"] = []
        self._data["ExternalInterface:Actuator"] = []
        self._data["ExternalInterface:FunctionalMockupUnitImport"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitImport:From:Variable"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitImport:To:Schedule"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitImport:To:Actuator"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitImport:To:Variable"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitExport:From:Variable"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitExport:To:Schedule"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitExport:To:Actuator"] = []
        self._data[
            "ExternalInterface:FunctionalMockupUnitExport:To:Variable"] = []
        self._data["ZoneHVAC:ForcedAir:UserDefined"] = []
        self._data["AirTerminal:SingleDuct:UserDefined"] = []
        self._data["Coil:UserDefined"] = []
        self._data["PlantComponent:UserDefined"] = []
        self._data["PlantEquipmentOperation:UserDefined"] = []
        self._data["AvailabilityManager:Scheduled"] = []
        self._data["AvailabilityManager:ScheduledOn"] = []
        self._data["AvailabilityManager:ScheduledOff"] = []
        self._data["AvailabilityManager:OptimumStart"] = []
        self._data["AvailabilityManager:NightCycle"] = []
        self._data["AvailabilityManager:DifferentialThermostat"] = []
        self._data["AvailabilityManager:HighTemperatureTurnOff"] = []
        self._data["AvailabilityManager:HighTemperatureTurnOn"] = []
        self._data["AvailabilityManager:LowTemperatureTurnOff"] = []
        self._data["AvailabilityManager:LowTemperatureTurnOn"] = []
        self._data["AvailabilityManager:NightVentilation"] = []
        self._data["AvailabilityManager:HybridVentilation"] = []
        self._data["AvailabilityManagerAssignmentList"] = []
        self._data["SetpointManager:Scheduled"] = []
        self._data["SetpointManager:Scheduled:DualSetpoint"] = []
        self._data["SetpointManager:OutdoorAirReset"] = []
        self._data["SetpointManager:SingleZone:Reheat"] = []
        self._data["SetpointManager:SingleZone:Heating"] = []
        self._data["SetpointManager:SingleZone:Cooling"] = []
        self._data["SetpointManager:SingleZone:Humidity:Minimum"] = []
        self._data["SetpointManager:SingleZone:Humidity:Maximum"] = []
        self._data["SetpointManager:MixedAir"] = []
        self._data["SetpointManager:OutdoorAirPretreat"] = []
        self._data["SetpointManager:Warmest"] = []
        self._data["SetpointManager:Coldest"] = []
        self._data["SetpointManager:ReturnAirBypassFlow"] = []
        self._data["SetpointManager:WarmestTemperatureFlow"] = []
        self._data["SetpointManager:MultiZone:Heating:Average"] = []
        self._data["SetpointManager:MultiZone:Cooling:Average"] = []
        self._data["SetpointManager:MultiZone:MinimumHumidity:Average"] = []
        self._data["SetpointManager:MultiZone:MaximumHumidity:Average"] = []
        self._data["SetpointManager:MultiZone:Humidity:Minimum"] = []
        self._data["SetpointManager:MultiZone:Humidity:Maximum"] = []
        self._data["SetpointManager:FollowOutdoorAirTemperature"] = []
        self._data["SetpointManager:FollowSystemNodeTemperature"] = []
        self._data["SetpointManager:FollowGroundTemperature"] = []
        self._data["SetpointManager:CondenserEnteringReset"] = []
        self._data["SetpointManager:CondenserEnteringReset:Ideal"] = []
        self._data["SetpointManager:SingleZone:OneStageCooling"] = []
        self._data["SetpointManager:SingleZone:OneStageHeating"] = []
        self._data["Refrigeration:Case"] = []
        self._data["Refrigeration:CompressorRack"] = []
        self._data["Refrigeration:CaseAndWalkInList"] = []
        self._data["Refrigeration:Condenser:AirCooled"] = []
        self._data["Refrigeration:Condenser:EvaporativeCooled"] = []
        self._data["Refrigeration:Condenser:WaterCooled"] = []
        self._data["Refrigeration:Condenser:Cascade"] = []
        self._data["Refrigeration:GasCooler:AirCooled"] = []
        self._data["Refrigeration:TransferLoadList"] = []
        self._data["Refrigeration:Subcooler"] = []
        self._data["Refrigeration:Compressor"] = []
        self._data["Refrigeration:CompressorList"] = []
        self._data["Refrigeration:System"] = []
        self._data["Refrigeration:TranscriticalSystem"] = []
        self._data["Refrigeration:SecondarySystem"] = []
        self._data["Refrigeration:WalkIn"] = []
        self._data["Refrigeration:AirChiller"] = []
        self._data["DemandManagerAssignmentList"] = []
        self._data["DemandManager:ExteriorLights"] = []
        self._data["DemandManager:Lights"] = []
        self._data["DemandManager:ElectricEquipment"] = []
        self._data["DemandManager:Thermostats"] = []
        self._data["Generator:InternalCombustionEngine"] = []
        self._data["Generator:CombustionTurbine"] = []
        self._data["Generator:MicroTurbine"] = []
        self._data["Generator:Photovoltaic"] = []
        self._data["PhotovoltaicPerformance:Simple"] = []
        self._data["PhotovoltaicPerformance:EquivalentOne-Diode"] = []
        self._data["PhotovoltaicPerformance:Sandia"] = []
        self._data["Generator:FuelCell"] = []
        self._data["Generator:FuelCell:PowerModule"] = []
        self._data["Generator:FuelCell:AirSupply"] = []
        self._data["Generator:FuelCell:WaterSupply"] = []
        self._data["Generator:FuelCell:AuxiliaryHeater"] = []
        self._data["Generator:FuelCell:ExhaustGasToWaterHeatExchanger"] = []
        self._data["Generator:FuelCell:ElectricalStorage"] = []
        self._data["Generator:FuelCell:Inverter"] = []
        self._data["Generator:FuelCell:StackCooler"] = []
        self._data["Generator:MicroCHP"] = []
        self._data["Generator:MicroCHP:NonNormalizedParameters"] = []
        self._data["Generator:FuelSupply"] = []
        self._data["Generator:WindTurbine"] = []
        self._data["ElectricLoadCenter:Generators"] = []
        self._data["ElectricLoadCenter:Inverter:Simple"] = []
        self._data["ElectricLoadCenter:Inverter:FunctionOfPower"] = []
        self._data["ElectricLoadCenter:Inverter:LookUpTable"] = []
        self._data["ElectricLoadCenter:Storage:Simple"] = []
        self._data["ElectricLoadCenter:Storage:Battery"] = []
        self._data["ElectricLoadCenter:Transformer"] = []
        self._data["ElectricLoadCenter:Distribution"] = []
        self._data["WaterUse:Equipment"] = []
        self._data["WaterUse:Connections"] = []
        self._data["WaterUse:Storage"] = []
        self._data["WaterUse:Well"] = []
        self._data["WaterUse:RainCollector"] = []
        self._data["FaultModel:TemperatureSensorOffset:OutdoorAir"] = []
        self._data["FaultModel:HumiditySensorOffset:OutdoorAir"] = []
        self._data["FaultModel:EnthalpySensorOffset:OutdoorAir"] = []
        self._data["FaultModel:PressureSensorOffset:OutdoorAir"] = []
        self._data["FaultModel:TemperatureSensorOffset:ReturnAir"] = []
        self._data["FaultModel:EnthalpySensorOffset:ReturnAir"] = []
        self._data["FaultModel:Fouling:Coil"] = []
        self._data["Curve:Linear"] = []
        self._data["Curve:QuadLinear"] = []
        self._data["Curve:Quadratic"] = []
        self._data["Curve:Cubic"] = []
        self._data["Curve:Quartic"] = []
        self._data["Curve:Exponent"] = []
        self._data["Curve:Bicubic"] = []
        self._data["Curve:Biquadratic"] = []
        self._data["Curve:QuadraticLinear"] = []
        self._data["Curve:Triquadratic"] = []
        self._data["Curve:Functional:PressureDrop"] = []
        self._data["Curve:FanPressureRise"] = []
        self._data["Curve:ExponentialSkewNormal"] = []
        self._data["Curve:Sigmoid"] = []
        self._data["Curve:RectangularHyperbola1"] = []
        self._data["Curve:RectangularHyperbola2"] = []
        self._data["Curve:ExponentialDecay"] = []
        self._data["Curve:DoubleExponentialDecay"] = []
        self._data["FluidProperties:Name"] = []
        self._data["FluidProperties:GlycolConcentration"] = []
        self._data["FluidProperties:Temperatures"] = []
        self._data["FluidProperties:Saturated"] = []
        self._data["FluidProperties:Superheated"] = []
        self._data["FluidProperties:Concentration"] = []
        self._data["CurrencyType"] = []
        self._data["ComponentCost:Adjustments"] = []
        self._data["ComponentCost:Reference"] = []
        self._data["ComponentCost:LineItem"] = []
        self._data["UtilityCost:Tariff"] = []
        self._data["UtilityCost:Qualify"] = []
        self._data["UtilityCost:Charge:Simple"] = []
        self._data["UtilityCost:Charge:Block"] = []
        self._data["UtilityCost:Ratchet"] = []
        self._data["UtilityCost:Variable"] = []
        self._data["UtilityCost:Computation"] = []
        self._data["LifeCycleCost:Parameters"] = []
        self._data["LifeCycleCost:RecurringCosts"] = []
        self._data["LifeCycleCost:NonrecurringCost"] = []
        self._data["LifeCycleCost:UsePriceEscalation"] = []
        self._data["LifeCycleCost:UseAdjustment"] = []
        self._data["Parametric:SetValueForRun"] = []
        self._data["Parametric:Logic"] = []
        self._data["Parametric:RunControl"] = []
        self._data["Parametric:FileNameSuffix"] = []
        self._data["Output:VariableDictionary"] = []
        self._data["Output:Surfaces:List"] = []
        self._data["Output:Surfaces:Drawing"] = []
        self._data["Output:Schedules"] = []
        self._data["Output:Constructions"] = []
        self._data["Output:EnergyManagementSystem"] = []
        self._data["OutputControl:SurfaceColorScheme"] = []
        self._data["Output:Table:SummaryReports"] = []
        self._data["Output:Table:TimeBins"] = []
        self._data["Output:Table:Monthly"] = []
        self._data["OutputControl:Table:Style"] = []
        self._data["OutputControl:ReportingTolerances"] = []
        self._data["Output:Variable"] = []
        self._data["Output:Meter"] = []
        self._data["Output:Meter:MeterFileOnly"] = []
        self._data["Output:Meter:Cumulative"] = []
        self._data["Output:Meter:Cumulative:MeterFileOnly"] = []
        self._data["Meter:Custom"] = []
        self._data["Meter:CustomDecrement"] = []
        self._data["Output:SQLite"] = []
        self._data["Output:EnvironmentalImpactFactors"] = []
        self._data["EnvironmentalImpactFactors"] = []
        self._data["FuelFactors"] = []
        self._data["Output:Diagnostics"] = []
        self._data["Output:DebuggingData"] = []
        self._data["Output:PreprocessorMessage"] = []

    def set(self, data):
        self._data[data.internal_name].append(data)

    def save(self, path, check=True):
        """ Save data to path

            Args:
                path (str): path where data should be save

            Raises:
                ValueError: if required objects are not present or
                    unique objects are not unique
        """
        with open(path, 'w') as f:
            if check:
                for key in self._data:
                    if len(
                            self._data[key]) == 0 and key in self.required_objects:
                        raise ValueError('{} is not valid.'.format(key))
                    if key in self.unique_objects and len(self._data[key]) > 0:
                        raise ValueError(
                            '{} is not unique: {}'.format(
                                key, len(
                                    self._data[key])))
            for key in self._data:
                if len(self._data[key]) > 0:
                    for data_object in self._data[key]:
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
        raise ValueError(
            "No DataDictionary known for {}".format(internal_name))

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
                        self._data[internal_name] = self._create_datadict(
                            internal_name)
                        data_line = line[len(internal_name) + 1:]
                        vals = data_line.strip().split(',')
                        self._data[internal_name].read(vals)
