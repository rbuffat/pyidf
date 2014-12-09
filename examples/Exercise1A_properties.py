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
    obj = Version()
    obj.version_identifier = "8.2"
    idf.add(obj)

    obj = Building()
    obj.name = "Exercise 1A"
    obj.north_axis = 0.0
    obj.terrain = "Country"
    obj.loads_convergence_tolerance_value = 0.04
    obj.temperature_convergence_tolerance_value = 0.4
    obj.solar_distribution = "FullInteriorAndExterior"
    obj.maximum_number_of_warmup_days = None
    obj.minimum_number_of_warmup_days = 6
    idf.add(obj)

    obj = Timestep()
    obj.number_of_timesteps_per_hour = 4
    idf.add(obj)

    obj = SurfaceConvectionAlgorithmInside()
    obj.algorithm = "TARP"
    idf.add(obj)

    obj = SurfaceConvectionAlgorithmOutside()
    obj.algorithm = "TARP"
    idf.add(obj)

    obj = HeatBalanceAlgorithm()
    obj.algorithm = "ConductionTransferFunction"
    idf.add(obj)

    obj = ShadowCalculation()
    obj.calculation_method = "AverageOverDaysInFrequency"
    obj.calculation_frequency = 20
    idf.add(obj)

    obj = SimulationControl()
    obj.do_zone_sizing_calculation = "No"
    obj.do_system_sizing_calculation = "No"
    obj.do_plant_sizing_calculation = "No"
    obj.run_simulation_for_sizing_periods = "Yes"
    obj.run_simulation_for_weather_file_run_periods = "No"
    idf.add(obj)

    obj = SiteLocation()
    obj.name = "CHICAGO_IL_USA TMY2-94846"
    obj.latitude = 41.78
    obj.longitude = -87.75
    obj.time_zone = -6.0
    obj.elevation = 190.0
    idf.add(obj)

    obj = SizingPeriodDesignDay()
    obj.name = "CHICAGO_IL_USA Cooling .4% Conditions DB=>MWB"
    obj.month = 7
    obj.day_of_month = 21
    obj.day_type = "SummerDesignDay"
    obj.maximum_drybulb_temperature = 32.8
    obj.daily_drybulb_temperature_range = 10.9
    obj.drybulb_temperature_range_modifier_type = None
    obj.drybulb_temperature_range_modifier_day_schedule_name = None
    obj.humidity_condition_type = "Wetbulb"
    obj.wetbulb_or_dewpoint_at_maximum_drybulb = 23.6
    obj.humidity_condition_day_schedule_name = None
    obj.humidity_ratio_at_maximum_drybulb = None
    obj.enthalpy_at_maximum_drybulb_will_require_units_transition_ = None
    obj.daily_wetbulb_temperature_range = None
    obj.barometric_pressure = 99063.21
    obj.wind_speed = 0.0
    obj.wind_direction = 0.0
    obj.rain_indicator = "No"
    obj.snow_indicator = "No"
    obj.daylight_saving_time_indicator = "No"
    obj.solar_model_indicator = "ASHRAEClearSky"
    obj.beam_solar_day_schedule_name = None
    obj.diffuse_solar_day_schedule_name = None
    obj.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = None
    obj.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = None
    obj.sky_clearness = 1.0
    idf.add(obj)

    obj = SizingPeriodDesignDay()
    obj.name = "CHICAGO_IL_USA Heating 99.6% Conditions"
    obj.month = 1
    obj.day_of_month = 21
    obj.day_type = "WinterDesignDay"
    obj.maximum_drybulb_temperature = -21.2
    obj.daily_drybulb_temperature_range = 0.0
    obj.drybulb_temperature_range_modifier_type = None
    obj.drybulb_temperature_range_modifier_day_schedule_name = None
    obj.humidity_condition_type = "Wetbulb"
    obj.wetbulb_or_dewpoint_at_maximum_drybulb = -21.2
    obj.humidity_condition_day_schedule_name = None
    obj.humidity_ratio_at_maximum_drybulb = None
    obj.enthalpy_at_maximum_drybulb_will_require_units_transition_ = None
    obj.daily_wetbulb_temperature_range = None
    obj.barometric_pressure = 99063.21
    obj.wind_speed = 4.6
    obj.wind_direction = 270.0
    obj.rain_indicator = "No"
    obj.snow_indicator = "No"
    obj.daylight_saving_time_indicator = "No"
    obj.solar_model_indicator = "ASHRAEClearSky"
    obj.beam_solar_day_schedule_name = None
    obj.diffuse_solar_day_schedule_name = None
    obj.ashrae_clear_sky_optical_depth_for_beam_irradiance_taub = None
    obj.ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud = None
    obj.sky_clearness = 0.0
    idf.add(obj)

    obj = SiteGroundTemperatureBuildingSurface()
    obj.january_ground_temperature = 18.3
    obj.february_ground_temperature = 18.2
    obj.march_ground_temperature = 18.3
    obj.april_ground_temperature = 18.4
    obj.may_ground_temperature = 20.1
    obj.june_ground_temperature = 22.0
    obj.july_ground_temperature = 22.3
    obj.august_ground_temperature = 22.5
    obj.september_ground_temperature = 22.5
    obj.october_ground_temperature = 20.7
    obj.november_ground_temperature = 18.9
    obj.december_ground_temperature = 18.5
    idf.add(obj)

    obj = Material()
    obj.name = "PLASTERBOARD-1"
    obj.roughness = "MediumSmooth"
    obj.thickness = 0.012
    obj.conductivity = 0.16
    obj.density = 950.0
    obj.specific_heat = 840.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.6
    obj.visible_absorptance = 0.6
    idf.add(obj)

    obj = Material()
    obj.name = "FIBERGLASS QUILT-1"
    obj.roughness = "Rough"
    obj.thickness = 0.066
    obj.conductivity = 0.04
    obj.density = 12.0
    obj.specific_heat = 840.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.6
    obj.visible_absorptance = 0.6
    idf.add(obj)

    obj = Material()
    obj.name = "WOOD SIDING-1"
    obj.roughness = "Rough"
    obj.thickness = 0.009
    obj.conductivity = 0.14
    obj.density = 530.0
    obj.specific_heat = 900.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.6
    obj.visible_absorptance = 0.6
    idf.add(obj)

    obj = Material()
    obj.name = "PLASTERBOARD-2"
    obj.roughness = "Rough"
    obj.thickness = 0.01
    obj.conductivity = 0.16
    obj.density = 950.0
    obj.specific_heat = 840.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.6
    obj.visible_absorptance = 0.6
    idf.add(obj)

    obj = Material()
    obj.name = "FIBERGLASS QUILT-2"
    obj.roughness = "Rough"
    obj.thickness = 0.1118
    obj.conductivity = 0.04
    obj.density = 12.0
    obj.specific_heat = 840.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.6
    obj.visible_absorptance = 0.6
    idf.add(obj)

    obj = Material()
    obj.name = "ROOF DECK"
    obj.roughness = "Rough"
    obj.thickness = 0.019
    obj.conductivity = 0.14
    obj.density = 530.0
    obj.specific_heat = 900.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.6
    obj.visible_absorptance = 0.6
    idf.add(obj)

    obj = Material()
    obj.name = "HF-C5"
    obj.roughness = "MediumRough"
    obj.thickness = 0.1015
    obj.conductivity = 1.7296
    obj.density = 2243.0
    obj.specific_heat = 837.0
    obj.thermal_absorptance = 0.9
    obj.solar_absorptance = 0.65
    obj.visible_absorptance = 0.65
    idf.add(obj)

    obj = Construction()
    obj.name = "LTWALL"
    obj.outside_layer = "WOOD SIDING-1"
    obj.layer_2 = "FIBERGLASS QUILT-1"
    obj.layer_3 = "PLASTERBOARD-1"
    idf.add(obj)

    obj = Construction()
    obj.name = "LTFLOOR"
    obj.outside_layer = "HF-C5"
    idf.add(obj)

    obj = Construction()
    obj.name = "LTROOF"
    obj.outside_layer = "ROOF DECK"
    obj.layer_2 = "FIBERGLASS QUILT-2"
    obj.layer_3 = "PLASTERBOARD-2"
    idf.add(obj)

    obj = Zone()
    obj.name = "ZONE ONE"
    obj.direction_of_relative_north = 0.0
    obj.x_origin = 0.0
    obj.y_origin = 0.0
    obj.z_origin = 0.0
    obj.type = 1
    obj.multiplier = 1
    obj.ceiling_height = 2.7
    obj.volume = 129.6
    idf.add(obj)

    obj = GlobalGeometryRules()
    obj.starting_vertex_position = "UpperLeftCorner"
    obj.vertex_entry_direction = "Counterclockwise"
    obj.coordinate_system = "World"
    idf.add(obj)

    obj = BuildingSurfaceDetailed()
    obj.name = "SURFACE NORTH"
    obj.surface_type = "Wall"
    obj.construction_name = "LTWALL"
    obj.zone_name = "ZONE ONE"
    obj.outside_boundary_condition = "Outdoors"
    obj.outside_boundary_condition_object = None
    obj.sun_exposure = "SunExposed"
    obj.wind_exposure = "WindExposed"
    obj.view_factor_to_ground = 0.5
    obj.number_of_vertices = 4.0
    obj.add_extensible(8.0, 6.0, 2.7)
    obj.add_extensible(8.0, 6.0, 0.0)
    obj.add_extensible(0.0, 6.0, 0.0)
    obj.add_extensible(0.0, 6.0, 2.7)
    idf.add(obj)

    obj = BuildingSurfaceDetailed()
    obj.name = "ZONE SURFACE EAST"
    obj.surface_type = "Wall"
    obj.construction_name = "LTWALL"
    obj.zone_name = "ZONE ONE"
    obj.outside_boundary_condition = "Outdoors"
    obj.outside_boundary_condition_object = None
    obj.sun_exposure = "SunExposed"
    obj.wind_exposure = "WindExposed"
    obj.view_factor_to_ground = 0.5
    obj.number_of_vertices = 4.0
    obj.add_extensible(8.0, 0.0, 2.7)
    obj.add_extensible(8.0, 0.0, 0.0)
    obj.add_extensible(8.0, 6.0, 0.0)
    obj.add_extensible(8.0, 6.0, 2.7)
    idf.add(obj)

    obj = BuildingSurfaceDetailed()
    obj.name = "ZONE SURFACE SOUTH"
    obj.surface_type = "Wall"
    obj.construction_name = "LTWALL"
    obj.zone_name = "ZONE ONE"
    obj.outside_boundary_condition = "Outdoors"
    obj.outside_boundary_condition_object = None
    obj.sun_exposure = "SunExposed"
    obj.wind_exposure = "WindExposed"
    obj.view_factor_to_ground = 0.5
    obj.number_of_vertices = 4.0
    obj.add_extensible(0.0, 0.0, 2.7)
    obj.add_extensible(0.0, 0.0, 0.0)
    obj.add_extensible(8.0, 0.0, 0.0)
    obj.add_extensible(8.0, 0.0, 2.7)
    idf.add(obj)

    obj = BuildingSurfaceDetailed()
    obj.name = "ZONE SURFACE WEST"
    obj.surface_type = "Wall"
    obj.construction_name = "LTWALL"
    obj.zone_name = "ZONE ONE"
    obj.outside_boundary_condition = "Outdoors"
    obj.outside_boundary_condition_object = None
    obj.sun_exposure = "SunExposed"
    obj.wind_exposure = "WindExposed"
    obj.view_factor_to_ground = 0.5
    obj.number_of_vertices = 4.0
    obj.add_extensible(0.0, 6.0, 2.7)
    obj.add_extensible(0.0, 6.0, 0.0)
    obj.add_extensible(0.0, 0.0, 0.0)
    obj.add_extensible(0.0, 0.0, 2.7)
    idf.add(obj)

    obj = BuildingSurfaceDetailed()
    obj.name = "ZONE SURFACE FLOOR"
    obj.surface_type = "Floor"
    obj.construction_name = "LTFLOOR"
    obj.zone_name = "ZONE ONE"
    obj.outside_boundary_condition = "Ground"
    obj.outside_boundary_condition_object = None
    obj.sun_exposure = "NoSun"
    obj.wind_exposure = "NoWind"
    obj.view_factor_to_ground = 0.0
    obj.number_of_vertices = 4.0
    obj.add_extensible(0.0, 0.0, 0.0)
    obj.add_extensible(0.0, 6.0, 0.0)
    obj.add_extensible(8.0, 6.0, 0.0)
    obj.add_extensible(8.0, 0.0, 0.0)
    idf.add(obj)

    obj = BuildingSurfaceDetailed()
    obj.name = "ZONE SURFACE ROOF"
    obj.surface_type = "Roof"
    obj.construction_name = "LTROOF"
    obj.zone_name = "ZONE ONE"
    obj.outside_boundary_condition = "Outdoors"
    obj.outside_boundary_condition_object = None
    obj.sun_exposure = "SunExposed"
    obj.wind_exposure = "WindExposed"
    obj.view_factor_to_ground = 0.0
    obj.number_of_vertices = 4.0
    obj.add_extensible(0.0, 6.0, 2.7)
    obj.add_extensible(0.0, 0.0, 2.7)
    obj.add_extensible(8.0, 0.0, 2.7)
    obj.add_extensible(8.0, 6.0, 2.7)
    idf.add(obj)

    obj = ScheduleTypeLimits()
    obj.name = "Any Number"
    idf.add(obj)

    obj = ScheduleCompact()
    obj.name = "ALWAYS 4"
    obj.schedule_type_limits_name = "Any Number"
    obj.add_extensible("Through: 12/31")
    obj.add_extensible("For: AllDays")
    obj.add_extensible("Until: 24:00")
    obj.add_extensible("4")
    idf.add(obj)

    obj = ScheduleCompact()
    obj.name = "ALWAYS 20"
    obj.schedule_type_limits_name = "Any Number"
    obj.add_extensible("Through: 12/31")
    obj.add_extensible("For: AllDays")
    obj.add_extensible("Until: 24:00")
    obj.add_extensible("20")
    idf.add(obj)

    obj = ScheduleCompact()
    obj.name = "ALWAYS 24"
    obj.schedule_type_limits_name = "Any Number"
    obj.add_extensible("Through: 12/31")
    obj.add_extensible("For: AllDays")
    obj.add_extensible("Until: 24:00")
    obj.add_extensible("24")
    idf.add(obj)

    obj = ZoneHvacEquipmentConnections()
    obj.zone_name = "ZONE ONE"
    obj.zone_conditioning_equipment_list_name = "ZONE ONE Equipment"
    obj.zone_air_inlet_node_or_nodelist_name = "ZONE ONE Supply Inlet"
    obj.zone_air_exhaust_node_or_nodelist_name = None
    obj.zone_air_node_name = "ZONE ONE Zone Air Node"
    obj.zone_return_air_node_name = "ZONE ONE Return Outlet"
    idf.add(obj)

    obj = ZoneHvacEquipmentList()
    obj.name = "ZONE ONE Equipment"
    obj.add_extensible(
        "ZoneHVAC:IdealLoadsAirSystem",
        "ZONE ONE Purchased Air",
        1,
        1)
    idf.add(obj)

    obj = ZoneHvacIdealLoadsAirSystem()
    obj.name = "ZONE ONE Purchased Air"
    obj.availability_schedule_name = None
    obj.zone_supply_air_node_name = "ZONE ONE Supply Inlet"
    obj.zone_exhaust_air_node_name = None
    obj.maximum_heating_supply_air_temperature = 50.0
    obj.minimum_cooling_supply_air_temperature = 13.0
    obj.maximum_heating_supply_air_humidity_ratio = 0.015
    obj.minimum_cooling_supply_air_humidity_ratio = 0.01
    obj.heating_limit = "NoLimit"
    obj.maximum_heating_air_flow_rate = None
    obj.maximum_sensible_heating_capacity = None
    obj.cooling_limit = "NoLimit"
    obj.maximum_cooling_air_flow_rate = None
    obj.maximum_total_cooling_capacity = None
    obj.heating_availability_schedule_name = None
    obj.cooling_availability_schedule_name = None
    obj.dehumidification_control_type = "ConstantSupplyHumidityRatio"
    obj.cooling_sensible_heat_ratio = None
    obj.humidification_control_type = "ConstantSupplyHumidityRatio"
    obj.design_specification_outdoor_air_object_name = None
    obj.outdoor_air_inlet_node_name = None
    obj.demand_controlled_ventilation_type = None
    obj.outdoor_air_economizer_type = None
    obj.heat_recovery_type = None
    obj.sensible_heat_recovery_effectiveness = None
    obj.latent_heat_recovery_effectiveness = None
    idf.add(obj)

    obj = ZoneControlThermostat()
    obj.name = "ZONE ONE Thermostat"
    obj.zone_or_zonelist_name = "ZONE ONE"
    obj.control_type_schedule_name = "ALWAYS 4"
    obj.control_1_object_type = "ThermostatSetpoint:DualSetpoint"
    obj.control_1_name = "Office Thermostat Dual SP Control"
    idf.add(obj)

    obj = ThermostatSetpointDualSetpoint()
    obj.name = "Office Thermostat Dual SP Control"
    obj.heating_setpoint_temperature_schedule_name = "ALWAYS 20"
    obj.cooling_setpoint_temperature_schedule_name = "ALWAYS 24"
    idf.add(obj)

    obj = OutputVariable()
    obj.key_value = "*"
    obj.variable_name = "Site Outdoor Air Drybulb Temperature"
    obj.reporting_frequency = "Hourly"
    idf.add(obj)

    obj = OutputVariable()
    obj.key_value = "*"
    obj.variable_name = "Zone Air System Sensible Cooling Energy"
    obj.reporting_frequency = "Hourly"
    idf.add(obj)

    obj = OutputVariable()
    obj.key_value = "*"
    obj.variable_name = "Zone Air System Sensible Heating Energy"
    obj.reporting_frequency = "Hourly"
    idf.add(obj)

    obj = OutputVariable()
    obj.key_value = "*"
    obj.variable_name = "Zone Air Temperature"
    obj.reporting_frequency = "Hourly"
    idf.add(obj)

    obj = OutputMeter()
    obj.name = "DistrictHeating:Facility"
    obj.reporting_frequency = "Hourly"
    idf.add(obj)

    obj = OutputMeter()
    obj.name = "DistrictCooling:Facility"
    obj.reporting_frequency = "Hourly"
    idf.add(obj)

    obj = OutputSurfacesDrawing()
    obj.report_type = "DXF"
    idf.add(obj)

    obj = OutputConstructions()
    obj.details_type_1 = "Constructions"
    idf.add(obj)

    obj = OutputVariableDictionary()
    obj.key_field = "Regular"
    idf.add(obj)

    idf.save(idf_file_path)
