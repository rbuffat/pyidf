import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import Building
from pyidf.thermal_zones_and_surfaces import GlobalGeometryRules
from pyidf.thermal_zones_and_surfaces import BuildingSurfaceDetailed
from pyidf.output_reporting import OutputSurfacesDrawing
from pyidf.output_reporting import OutputVariable
from pyidf.simulation_parameters import HeatBalanceAlgorithm
from pyidf.simulation_parameters import Version
from pyidf.simulation_parameters import SurfaceConvectionAlgorithmInside
from pyidf.zone_hvac_equipment_connections import ZoneHvacEquipmentConnections
from pyidf.simulation_parameters import SurfaceConvectionAlgorithmOutside
from pyidf.simulation_parameters import ShadowCalculation
from pyidf.simulation_parameters import Timestep
from pyidf.zone_hvac_forced_air_units import ZoneHvacIdealLoadsAirSystem
from pyidf.simulation_parameters import SimulationControl
from pyidf.location_and_climate import SiteGroundTemperatureBuildingSurface
from pyidf.location_and_climate import SiteLocation
from pyidf.surface_construction_elements import Construction
from pyidf.output_reporting import OutputConstructions
from pyidf.output_reporting import OutputVariableDictionary
from pyidf.output_reporting import OutputMeter
from pyidf.thermal_zones_and_surfaces import Zone
from pyidf.surface_construction_elements import Material
from pyidf.schedules import ScheduleCompact
from pyidf.location_and_climate import SizingPeriodDesignDay
from pyidf.zone_hvac_controls_and_thermostats import ZoneControlThermostat
from pyidf.schedules import ScheduleTypeLimits
from pyidf.zone_hvac_equipment_connections import ZoneHvacEquipmentList
from pyidf.zone_hvac_controls_and_thermostats import ThermostatSetpointDualSetpoint

idf_file_path = r"Exercise1A.idf"


if __name__ == '__main__':

    logging.info("start")
    pyidf.validation_level = ValidationLevel.transition
    idf = IDF()

    obj1 = Version()
    obj1.version_identifier = "8.4"
    idf.add(obj1)

    obj2 = Building()
    obj2.name = "Exercise 1A"
    obj2.north_axis = 0.0
    obj2.terrain = "Country"
    obj2.loads_convergence_tolerance_value = 0.04
    obj2.temperature_convergence_tolerance_value = 0.4
    obj2.solar_distribution = "FullInteriorAndExterior"
    obj2.maximum_number_of_warmup_days = None
    obj2.minimum_number_of_warmup_days = 6
    idf.add(obj2)

    obj3 = Timestep()
    obj3.number_of_timesteps_per_hour = 4
    idf.add(obj3)

    obj4 = SurfaceConvectionAlgorithmInside()
    obj4.algorithm = "TARP"
    idf.add(obj4)

    obj5 = SurfaceConvectionAlgorithmOutside()
    obj5.algorithm = "TARP"
    idf.add(obj5)

    obj6 = HeatBalanceAlgorithm()
    obj6.algorithm = "ConductionTransferFunction"
    idf.add(obj6)

    obj7 = ShadowCalculation()
    obj7.calculation_method = "AverageOverDaysInFrequency"
    obj7.calculation_frequency = 20
    idf.add(obj7)

    obj8 = SimulationControl()
    obj8.do_zone_sizing_calculation = "No"
    obj8.do_system_sizing_calculation = "No"
    obj8.do_plant_sizing_calculation = "No"
    obj8.run_simulation_for_sizing_periods = "Yes"
    obj8.run_simulation_for_weather_file_run_periods = "No"
    idf.add(obj8)

    obj9 = SiteLocation()
    obj9.name = "CHICAGO_IL_USA TMY2-94846"
    obj9.latitude = 41.78
    obj9.longitude = -87.75
    obj9.time_zone = -6.0
    obj9.elevation = 190.0
    idf.add(obj9)

    obj10 = SizingPeriodDesignDay()
    obj10.name = "CHICAGO_IL_USA Cooling .4% Conditions DB=>MWB"
    obj10.month = 7
    obj10.day_of_month = 21
    obj10.day_type = "SummerDesignDay"
    obj10.maximum_drybulb_temperature = 32.8
    obj10.daily_drybulb_temperature_range = 10.9
    obj10.drybulb_temperature_range_modifier_type = None
    obj10.drybulb_temperature_range_modifier_day_schedule_name = None
    obj10.humidity_condition_type = "Wetbulb"
    obj10.wetbulb_or_dewpoint_at_maximum_drybulb = 23.6
    obj10.humidity_condition_day_schedule_name = None
    obj10.humidity_ratio_at_maximum_drybulb = None
    obj10.enthalpy_at_maximum_drybulb = None
    obj10.daily_wetbulb_temperature_range = None
    obj10.barometric_pressure = 99063.21
    obj10.wind_speed = 0.0
    obj10.wind_direction = 0.0
    obj10.rain_indicator = "No"
    obj10.snow_indicator = "No"
    obj10.daylight_saving_time_indicator = "No"
    obj10.solar_model_indicator = "ASHRAEClearSky"
    obj10.beam_solar_day_schedule_name = None
    obj10.diffuse_solar_day_schedule_name = None
    obj10.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = None
    obj10.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = None
    obj10.sky_clearness = 1.0
    idf.add(obj10)

    obj11 = SizingPeriodDesignDay()
    obj11.name = "CHICAGO_IL_USA Heating 99.6% Conditions"
    obj11.month = 1
    obj11.day_of_month = 21
    obj11.day_type = "WinterDesignDay"
    obj11.maximum_drybulb_temperature = -21.2
    obj11.daily_drybulb_temperature_range = 0.0
    obj11.drybulb_temperature_range_modifier_type = None
    obj11.drybulb_temperature_range_modifier_day_schedule_name = None
    obj11.humidity_condition_type = "Wetbulb"
    obj11.wetbulb_or_dewpoint_at_maximum_drybulb = -21.2
    obj11.humidity_condition_day_schedule_name = None
    obj11.humidity_ratio_at_maximum_drybulb = None
    obj11.enthalpy_at_maximum_drybulb = None
    obj11.daily_wetbulb_temperature_range = None
    obj11.barometric_pressure = 99063.21
    obj11.wind_speed = 4.6
    obj11.wind_direction = 270.0
    obj11.rain_indicator = "No"
    obj11.snow_indicator = "No"
    obj11.daylight_saving_time_indicator = "No"
    obj11.solar_model_indicator = "ASHRAEClearSky"
    obj11.beam_solar_day_schedule_name = None
    obj11.diffuse_solar_day_schedule_name = None
    obj11.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = None
    obj11.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = None
    obj11.sky_clearness = 0.0
    idf.add(obj11)

    obj12 = SiteGroundTemperatureBuildingSurface()
    obj12.january_ground_temperature = 18.3
    obj12.february_ground_temperature = 18.2
    obj12.march_ground_temperature = 18.3
    obj12.april_ground_temperature = 18.4
    obj12.may_ground_temperature = 20.1
    obj12.june_ground_temperature = 22.0
    obj12.july_ground_temperature = 22.3
    obj12.august_ground_temperature = 22.5
    obj12.september_ground_temperature = 22.5
    obj12.october_ground_temperature = 20.7
    obj12.november_ground_temperature = 18.9
    obj12.december_ground_temperature = 18.5
    idf.add(obj12)

    obj13 = Material()
    obj13.name = "PLASTERBOARD-1"
    obj13.roughness = "MediumSmooth"
    obj13.thickness = 0.012
    obj13.conductivity = 0.16
    obj13.density = 950.0
    obj13.specific_heat = 840.0
    obj13.thermal_absorptance = 0.9
    obj13.solar_absorptance = 0.6
    obj13.visible_absorptance = 0.6
    idf.add(obj13)

    obj14 = Material()
    obj14.name = "FIBERGLASS QUILT-1"
    obj14.roughness = "Rough"
    obj14.thickness = 0.066
    obj14.conductivity = 0.04
    obj14.density = 12.0
    obj14.specific_heat = 840.0
    obj14.thermal_absorptance = 0.9
    obj14.solar_absorptance = 0.6
    obj14.visible_absorptance = 0.6
    idf.add(obj14)

    obj15 = Material()
    obj15.name = "WOOD SIDING-1"
    obj15.roughness = "Rough"
    obj15.thickness = 0.009
    obj15.conductivity = 0.14
    obj15.density = 530.0
    obj15.specific_heat = 900.0
    obj15.thermal_absorptance = 0.9
    obj15.solar_absorptance = 0.6
    obj15.visible_absorptance = 0.6
    idf.add(obj15)

    obj16 = Material()
    obj16.name = "PLASTERBOARD-2"
    obj16.roughness = "Rough"
    obj16.thickness = 0.01
    obj16.conductivity = 0.16
    obj16.density = 950.0
    obj16.specific_heat = 840.0
    obj16.thermal_absorptance = 0.9
    obj16.solar_absorptance = 0.6
    obj16.visible_absorptance = 0.6
    idf.add(obj16)

    obj17 = Material()
    obj17.name = "FIBERGLASS QUILT-2"
    obj17.roughness = "Rough"
    obj17.thickness = 0.1118
    obj17.conductivity = 0.04
    obj17.density = 12.0
    obj17.specific_heat = 840.0
    obj17.thermal_absorptance = 0.9
    obj17.solar_absorptance = 0.6
    obj17.visible_absorptance = 0.6
    idf.add(obj17)

    obj18 = Material()
    obj18.name = "ROOF DECK"
    obj18.roughness = "Rough"
    obj18.thickness = 0.019
    obj18.conductivity = 0.14
    obj18.density = 530.0
    obj18.specific_heat = 900.0
    obj18.thermal_absorptance = 0.9
    obj18.solar_absorptance = 0.6
    obj18.visible_absorptance = 0.6
    idf.add(obj18)

    obj19 = Material()
    obj19.name = "HF-C5"
    obj19.roughness = "MediumRough"
    obj19.thickness = 0.1015
    obj19.conductivity = 1.7296
    obj19.density = 2243.0
    obj19.specific_heat = 837.0
    obj19.thermal_absorptance = 0.9
    obj19.solar_absorptance = 0.65
    obj19.visible_absorptance = 0.65
    idf.add(obj19)

    obj20 = Construction()
    obj20.name = "LTWALL"
    obj20.outside_layer = "WOOD SIDING-1"
    obj20.layer_2 = "FIBERGLASS QUILT-1"
    obj20.layer_3 = "PLASTERBOARD-1"
    idf.add(obj20)

    obj21 = Construction()
    obj21.name = "LTFLOOR"
    obj21.outside_layer = "HF-C5"
    idf.add(obj21)

    obj22 = Construction()
    obj22.name = "LTROOF"
    obj22.outside_layer = "ROOF DECK"
    obj22.layer_2 = "FIBERGLASS QUILT-2"
    obj22.layer_3 = "PLASTERBOARD-2"
    idf.add(obj22)

    obj23 = Zone()
    obj23.name = "ZONE ONE"
    obj23.direction_of_relative_north = 0.0
    obj23.x_origin = 0.0
    obj23.y_origin = 0.0
    obj23.z_origin = 0.0
    obj23.type = 1
    obj23.multiplier = 1
    obj23.ceiling_height = 2.7
    obj23.volume = 129.6
    idf.add(obj23)

    obj24 = GlobalGeometryRules()
    obj24.starting_vertex_position = "UpperLeftCorner"
    obj24.vertex_entry_direction = "Counterclockwise"
    obj24.coordinate_system = "World"
    idf.add(obj24)

    obj25 = BuildingSurfaceDetailed()
    obj25.name = "SURFACE NORTH"
    obj25.surface_type = "Wall"
    obj25.construction_name = "LTWALL"
    obj25.zone_name = "ZONE ONE"
    obj25.outside_boundary_condition = "Outdoors"
    obj25.outside_boundary_condition_object = None
    obj25.sun_exposure = "SunExposed"
    obj25.wind_exposure = "WindExposed"
    obj25.view_factor_to_ground = 0.5
    obj25.number_of_vertices = 4.0
    obj25.add_extensible(8.0, 6.0, 2.7)
    obj25.add_extensible(8.0, 6.0, 0.0)
    obj25.add_extensible(0.0, 6.0, 0.0)
    obj25.add_extensible(0.0, 6.0, 2.7)
    idf.add(obj25)

    obj26 = BuildingSurfaceDetailed()
    obj26.name = "ZONE SURFACE EAST"
    obj26.surface_type = "Wall"
    obj26.construction_name = "LTWALL"
    obj26.zone_name = "ZONE ONE"
    obj26.outside_boundary_condition = "Outdoors"
    obj26.outside_boundary_condition_object = None
    obj26.sun_exposure = "SunExposed"
    obj26.wind_exposure = "WindExposed"
    obj26.view_factor_to_ground = 0.5
    obj26.number_of_vertices = 4.0
    obj26.add_extensible(8.0, 0.0, 2.7)
    obj26.add_extensible(8.0, 0.0, 0.0)
    obj26.add_extensible(8.0, 6.0, 0.0)
    obj26.add_extensible(8.0, 6.0, 2.7)
    idf.add(obj26)

    obj27 = BuildingSurfaceDetailed()
    obj27.name = "ZONE SURFACE SOUTH"
    obj27.surface_type = "Wall"
    obj27.construction_name = "LTWALL"
    obj27.zone_name = "ZONE ONE"
    obj27.outside_boundary_condition = "Outdoors"
    obj27.outside_boundary_condition_object = None
    obj27.sun_exposure = "SunExposed"
    obj27.wind_exposure = "WindExposed"
    obj27.view_factor_to_ground = 0.5
    obj27.number_of_vertices = 4.0
    obj27.add_extensible(0.0, 0.0, 2.7)
    obj27.add_extensible(0.0, 0.0, 0.0)
    obj27.add_extensible(8.0, 0.0, 0.0)
    obj27.add_extensible(8.0, 0.0, 2.7)
    idf.add(obj27)

    obj28 = BuildingSurfaceDetailed()
    obj28.name = "ZONE SURFACE WEST"
    obj28.surface_type = "Wall"
    obj28.construction_name = "LTWALL"
    obj28.zone_name = "ZONE ONE"
    obj28.outside_boundary_condition = "Outdoors"
    obj28.outside_boundary_condition_object = None
    obj28.sun_exposure = "SunExposed"
    obj28.wind_exposure = "WindExposed"
    obj28.view_factor_to_ground = 0.5
    obj28.number_of_vertices = 4.0
    obj28.add_extensible(0.0, 6.0, 2.7)
    obj28.add_extensible(0.0, 6.0, 0.0)
    obj28.add_extensible(0.0, 0.0, 0.0)
    obj28.add_extensible(0.0, 0.0, 2.7)
    idf.add(obj28)

    obj29 = BuildingSurfaceDetailed()
    obj29.name = "ZONE SURFACE FLOOR"
    obj29.surface_type = "Floor"
    obj29.construction_name = "LTFLOOR"
    obj29.zone_name = "ZONE ONE"
    obj29.outside_boundary_condition = "Ground"
    obj29.outside_boundary_condition_object = None
    obj29.sun_exposure = "NoSun"
    obj29.wind_exposure = "NoWind"
    obj29.view_factor_to_ground = 0.0
    obj29.number_of_vertices = 4.0
    obj29.add_extensible(0.0, 0.0, 0.0)
    obj29.add_extensible(0.0, 6.0, 0.0)
    obj29.add_extensible(8.0, 6.0, 0.0)
    obj29.add_extensible(8.0, 0.0, 0.0)
    idf.add(obj29)

    obj30 = BuildingSurfaceDetailed()
    obj30.name = "ZONE SURFACE ROOF"
    obj30.surface_type = "Roof"
    obj30.construction_name = "LTROOF"
    obj30.zone_name = "ZONE ONE"
    obj30.outside_boundary_condition = "Outdoors"
    obj30.outside_boundary_condition_object = None
    obj30.sun_exposure = "SunExposed"
    obj30.wind_exposure = "WindExposed"
    obj30.view_factor_to_ground = 0.0
    obj30.number_of_vertices = 4.0
    obj30.add_extensible(0.0, 6.0, 2.7)
    obj30.add_extensible(0.0, 0.0, 2.7)
    obj30.add_extensible(8.0, 0.0, 2.7)
    obj30.add_extensible(8.0, 6.0, 2.7)
    idf.add(obj30)

    obj31 = ScheduleTypeLimits()
    obj31.name = "Any Number"
    idf.add(obj31)

    obj32 = ScheduleCompact()
    obj32.name = "ALWAYS 4"
    obj32.schedule_type_limits_name = "Any Number"
    obj32.add_extensible("Through: 12/31")
    obj32.add_extensible("For: AllDays")
    obj32.add_extensible("Until: 24:00")
    obj32.add_extensible("4")
    idf.add(obj32)

    obj33 = ScheduleCompact()
    obj33.name = "ALWAYS 20"
    obj33.schedule_type_limits_name = "Any Number"
    obj33.add_extensible("Through: 12/31")
    obj33.add_extensible("For: AllDays")
    obj33.add_extensible("Until: 24:00")
    obj33.add_extensible("20")
    idf.add(obj33)

    obj34 = ScheduleCompact()
    obj34.name = "ALWAYS 24"
    obj34.schedule_type_limits_name = "Any Number"
    obj34.add_extensible("Through: 12/31")
    obj34.add_extensible("For: AllDays")
    obj34.add_extensible("Until: 24:00")
    obj34.add_extensible("24")
    idf.add(obj34)

    obj35 = ZoneHvacEquipmentConnections()
    obj35.zone_name = "ZONE ONE"
    obj35.zone_conditioning_equipment_list_name = "ZONE ONE Equipment"
    obj35.zone_air_inlet_node_or_nodelist_name = "ZONE ONE Supply Inlet"
    obj35.zone_air_exhaust_node_or_nodelist_name = None
    obj35.zone_air_node_name = "ZONE ONE Zone Air Node"
    obj35.zone_return_air_node_name = "ZONE ONE Return Outlet"
    idf.add(obj35)

    obj36 = ZoneHvacEquipmentList()
    obj36.name = "ZONE ONE Equipment"
    obj36.add_extensible(
        "ZoneHVAC:IdealLoadsAirSystem",
        "ZONE ONE Purchased Air",
        1,
        1)
    idf.add(obj36)

    obj37 = ZoneHvacIdealLoadsAirSystem()
    obj37.name = "ZONE ONE Purchased Air"
    obj37.availability_schedule_name = None
    obj37.zone_supply_air_node_name = "ZONE ONE Supply Inlet"
    obj37.zone_exhaust_air_node_name = None
    obj37.maximum_heating_supply_air_temperature = 50.0
    obj37.minimum_cooling_supply_air_temperature = 13.0
    obj37.maximum_heating_supply_air_humidity_ratio = 0.015
    obj37.minimum_cooling_supply_air_humidity_ratio = 0.01
    obj37.heating_limit = "NoLimit"
    obj37.maximum_heating_air_flow_rate = None
    obj37.maximum_sensible_heating_capacity = None
    obj37.cooling_limit = "NoLimit"
    obj37.maximum_cooling_air_flow_rate = None
    obj37.maximum_total_cooling_capacity = None
    obj37.heating_availability_schedule_name = None
    obj37.cooling_availability_schedule_name = None
    obj37.dehumidification_control_type = "ConstantSupplyHumidityRatio"
    obj37.cooling_sensible_heat_ratio = None
    obj37.humidification_control_type = "ConstantSupplyHumidityRatio"
    obj37.design_specification_outdoor_air_object_name = None
    obj37.outdoor_air_inlet_node_name = None
    obj37.demand_controlled_ventilation_type = None
    obj37.outdoor_air_economizer_type = None
    obj37.heat_recovery_type = None
    obj37.sensible_heat_recovery_effectiveness = None
    obj37.latent_heat_recovery_effectiveness = None
    idf.add(obj37)

    obj38 = ZoneControlThermostat()
    obj38.name = "ZONE ONE Thermostat"
    obj38.zone_or_zonelist_name = "ZONE ONE"
    obj38.control_type_schedule_name = "ALWAYS 4"
    obj38.control_1_object_type = "ThermostatSetpoint:DualSetpoint"
    obj38.control_1_name = "Office Thermostat Dual SP Control"
    idf.add(obj38)

    obj39 = ThermostatSetpointDualSetpoint()
    obj39.name = "Office Thermostat Dual SP Control"
    obj39.heating_setpoint_temperature_schedule_name = "ALWAYS 20"
    obj39.cooling_setpoint_temperature_schedule_name = "ALWAYS 24"
    idf.add(obj39)

    obj40 = OutputVariable()
    obj40.key_value = "*"
    obj40.variable_name = "Site Outdoor Air Drybulb Temperature"
    obj40.reporting_frequency = "Hourly"
    idf.add(obj40)

    obj41 = OutputVariable()
    obj41.key_value = "*"
    obj41.variable_name = "Zone Air System Sensible Cooling Energy"
    obj41.reporting_frequency = "Hourly"
    idf.add(obj41)

    obj42 = OutputVariable()
    obj42.key_value = "*"
    obj42.variable_name = "Zone Air System Sensible Heating Energy"
    obj42.reporting_frequency = "Hourly"
    idf.add(obj42)

    obj43 = OutputVariable()
    obj43.key_value = "*"
    obj43.variable_name = "Zone Air Temperature"
    obj43.reporting_frequency = "Hourly"
    idf.add(obj43)

    obj44 = OutputMeter()
    obj44.name = "DistrictHeating:Facility"
    obj44.reporting_frequency = "Hourly"
    idf.add(obj44)

    obj45 = OutputMeter()
    obj45.name = "DistrictCooling:Facility"
    obj45.reporting_frequency = "Hourly"
    idf.add(obj45)

    obj46 = OutputSurfacesDrawing()
    obj46.report_type = "DXF"
    idf.add(obj46)

    obj47 = OutputConstructions()
    obj47.details_type_1 = "Constructions"
    idf.add(obj47)

    obj48 = OutputVariableDictionary()
    obj48.key_field = "Regular"
    idf.add(obj48)

    idf.save(idf_file_path)
