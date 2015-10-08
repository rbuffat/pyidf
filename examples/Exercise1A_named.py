import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF

idf_file_path = r"Exercise1A.idf"


if __name__ == '__main__':

    logging.info("start")
    pyidf.validation_level = ValidationLevel.transition
    idf = IDF()

    obj1 = IDF._create_datadict("Version")
    obj1["Version Identifier"] = "8.4"
    idf.add(obj1)

    obj2 = IDF._create_datadict("Building")
    obj2["Name"] = "Exercise 1A"
    obj2["North Axis"] = 0.0
    obj2["Terrain"] = "Country"
    obj2["Loads Convergence Tolerance Value"] = 0.04
    obj2["Temperature Convergence Tolerance Value"] = 0.4
    obj2["Solar Distribution"] = "FullInteriorAndExterior"
    obj2["Maximum Number of Warmup Days"] = None
    obj2["Minimum Number of Warmup Days"] = 6
    idf.add(obj2)

    obj3 = IDF._create_datadict("Timestep")
    obj3["Number of Timesteps per Hour"] = 4
    idf.add(obj3)

    obj4 = IDF._create_datadict("SurfaceConvectionAlgorithm:Inside")
    obj4["Algorithm"] = "TARP"
    idf.add(obj4)

    obj5 = IDF._create_datadict("SurfaceConvectionAlgorithm:Outside")
    obj5["Algorithm"] = "TARP"
    idf.add(obj5)

    obj6 = IDF._create_datadict("HeatBalanceAlgorithm")
    obj6["Algorithm"] = "ConductionTransferFunction"
    idf.add(obj6)

    obj7 = IDF._create_datadict("ShadowCalculation")
    obj7["Calculation Method"] = "AverageOverDaysInFrequency"
    obj7["Calculation Frequency"] = 20
    idf.add(obj7)

    obj8 = IDF._create_datadict("SimulationControl")
    obj8["Do Zone Sizing Calculation"] = "No"
    obj8["Do System Sizing Calculation"] = "No"
    obj8["Do Plant Sizing Calculation"] = "No"
    obj8["Run Simulation for Sizing Periods"] = "Yes"
    obj8["Run Simulation for Weather File Run Periods"] = "No"
    idf.add(obj8)

    obj9 = IDF._create_datadict("Site:Location")
    obj9["Name"] = "CHICAGO_IL_USA TMY2-94846"
    obj9["Latitude"] = 41.78
    obj9["Longitude"] = -87.75
    obj9["Time Zone"] = -6.0
    obj9["Elevation"] = 190.0
    idf.add(obj9)

    obj10 = IDF._create_datadict("SizingPeriod:DesignDay")
    obj10["Name"] = "CHICAGO_IL_USA Cooling .4% Conditions DB=>MWB"
    obj10["Month"] = 7
    obj10["Day of Month"] = 21
    obj10["Day Type"] = "SummerDesignDay"
    obj10["Maximum Dry-Bulb Temperature"] = 32.8
    obj10["Daily Dry-Bulb Temperature Range"] = 10.9
    obj10["Dry-Bulb Temperature Range Modifier Type"] = None
    obj10["Dry-Bulb Temperature Range Modifier Day Schedule Name"] = None
    obj10["Humidity Condition Type"] = "Wetbulb"
    obj10["Wetbulb or DewPoint at Maximum Dry-Bulb"] = 23.6
    obj10["Humidity Condition Day Schedule Name"] = None
    obj10["Humidity Ratio at Maximum Dry-Bulb"] = None
    obj10["Enthalpy at Maximum Dry-Bulb"] = None
    obj10["Daily Wet-Bulb Temperature Range"] = None
    obj10["Barometric Pressure"] = 99063.21
    obj10["Wind Speed"] = 0.0
    obj10["Wind Direction"] = 0.0
    obj10["Rain Indicator"] = "No"
    obj10["Snow Indicator"] = "No"
    obj10["Daylight Saving Time Indicator"] = "No"
    obj10["Solar Model Indicator"] = "ASHRAEClearSky"
    obj10["Beam Solar Day Schedule Name"] = None
    obj10["Diffuse Solar Day Schedule Name"] = None
    obj10["ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"] = None
    obj10[
        "ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"] = None
    obj10["Sky Clearness"] = 1.0
    idf.add(obj10)

    obj11 = IDF._create_datadict("SizingPeriod:DesignDay")
    obj11["Name"] = "CHICAGO_IL_USA Heating 99.6% Conditions"
    obj11["Month"] = 1
    obj11["Day of Month"] = 21
    obj11["Day Type"] = "WinterDesignDay"
    obj11["Maximum Dry-Bulb Temperature"] = -21.2
    obj11["Daily Dry-Bulb Temperature Range"] = 0.0
    obj11["Dry-Bulb Temperature Range Modifier Type"] = None
    obj11["Dry-Bulb Temperature Range Modifier Day Schedule Name"] = None
    obj11["Humidity Condition Type"] = "Wetbulb"
    obj11["Wetbulb or DewPoint at Maximum Dry-Bulb"] = -21.2
    obj11["Humidity Condition Day Schedule Name"] = None
    obj11["Humidity Ratio at Maximum Dry-Bulb"] = None
    obj11["Enthalpy at Maximum Dry-Bulb"] = None
    obj11["Daily Wet-Bulb Temperature Range"] = None
    obj11["Barometric Pressure"] = 99063.21
    obj11["Wind Speed"] = 4.6
    obj11["Wind Direction"] = 270.0
    obj11["Rain Indicator"] = "No"
    obj11["Snow Indicator"] = "No"
    obj11["Daylight Saving Time Indicator"] = "No"
    obj11["Solar Model Indicator"] = "ASHRAEClearSky"
    obj11["Beam Solar Day Schedule Name"] = None
    obj11["Diffuse Solar Day Schedule Name"] = None
    obj11["ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"] = None
    obj11[
        "ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"] = None
    obj11["Sky Clearness"] = 0.0
    idf.add(obj11)

    obj12 = IDF._create_datadict("Site:GroundTemperature:BuildingSurface")
    obj12["January Ground Temperature"] = 18.3
    obj12["February Ground Temperature"] = 18.2
    obj12["March Ground Temperature"] = 18.3
    obj12["April Ground Temperature"] = 18.4
    obj12["May Ground Temperature"] = 20.1
    obj12["June Ground Temperature"] = 22.0
    obj12["July Ground Temperature"] = 22.3
    obj12["August Ground Temperature"] = 22.5
    obj12["September Ground Temperature"] = 22.5
    obj12["October Ground Temperature"] = 20.7
    obj12["November Ground Temperature"] = 18.9
    obj12["December Ground Temperature"] = 18.5
    idf.add(obj12)

    obj13 = IDF._create_datadict("Material")
    obj13["Name"] = "PLASTERBOARD-1"
    obj13["Roughness"] = "MediumSmooth"
    obj13["Thickness"] = 0.012
    obj13["Conductivity"] = 0.16
    obj13["Density"] = 950.0
    obj13["Specific Heat"] = 840.0
    obj13["Thermal Absorptance"] = 0.9
    obj13["Solar Absorptance"] = 0.6
    obj13["Visible Absorptance"] = 0.6
    idf.add(obj13)

    obj14 = IDF._create_datadict("Material")
    obj14["Name"] = "FIBERGLASS QUILT-1"
    obj14["Roughness"] = "Rough"
    obj14["Thickness"] = 0.066
    obj14["Conductivity"] = 0.04
    obj14["Density"] = 12.0
    obj14["Specific Heat"] = 840.0
    obj14["Thermal Absorptance"] = 0.9
    obj14["Solar Absorptance"] = 0.6
    obj14["Visible Absorptance"] = 0.6
    idf.add(obj14)

    obj15 = IDF._create_datadict("Material")
    obj15["Name"] = "WOOD SIDING-1"
    obj15["Roughness"] = "Rough"
    obj15["Thickness"] = 0.009
    obj15["Conductivity"] = 0.14
    obj15["Density"] = 530.0
    obj15["Specific Heat"] = 900.0
    obj15["Thermal Absorptance"] = 0.9
    obj15["Solar Absorptance"] = 0.6
    obj15["Visible Absorptance"] = 0.6
    idf.add(obj15)

    obj16 = IDF._create_datadict("Material")
    obj16["Name"] = "PLASTERBOARD-2"
    obj16["Roughness"] = "Rough"
    obj16["Thickness"] = 0.01
    obj16["Conductivity"] = 0.16
    obj16["Density"] = 950.0
    obj16["Specific Heat"] = 840.0
    obj16["Thermal Absorptance"] = 0.9
    obj16["Solar Absorptance"] = 0.6
    obj16["Visible Absorptance"] = 0.6
    idf.add(obj16)

    obj17 = IDF._create_datadict("Material")
    obj17["Name"] = "FIBERGLASS QUILT-2"
    obj17["Roughness"] = "Rough"
    obj17["Thickness"] = 0.1118
    obj17["Conductivity"] = 0.04
    obj17["Density"] = 12.0
    obj17["Specific Heat"] = 840.0
    obj17["Thermal Absorptance"] = 0.9
    obj17["Solar Absorptance"] = 0.6
    obj17["Visible Absorptance"] = 0.6
    idf.add(obj17)

    obj18 = IDF._create_datadict("Material")
    obj18["Name"] = "ROOF DECK"
    obj18["Roughness"] = "Rough"
    obj18["Thickness"] = 0.019
    obj18["Conductivity"] = 0.14
    obj18["Density"] = 530.0
    obj18["Specific Heat"] = 900.0
    obj18["Thermal Absorptance"] = 0.9
    obj18["Solar Absorptance"] = 0.6
    obj18["Visible Absorptance"] = 0.6
    idf.add(obj18)

    obj19 = IDF._create_datadict("Material")
    obj19["Name"] = "HF-C5"
    obj19["Roughness"] = "MediumRough"
    obj19["Thickness"] = 0.1015
    obj19["Conductivity"] = 1.7296
    obj19["Density"] = 2243.0
    obj19["Specific Heat"] = 837.0
    obj19["Thermal Absorptance"] = 0.9
    obj19["Solar Absorptance"] = 0.65
    obj19["Visible Absorptance"] = 0.65
    idf.add(obj19)

    obj20 = IDF._create_datadict("Construction")
    obj20["Name"] = "LTWALL"
    obj20["Outside Layer"] = "WOOD SIDING-1"
    obj20["Layer 2"] = "FIBERGLASS QUILT-1"
    obj20["Layer 3"] = "PLASTERBOARD-1"
    idf.add(obj20)

    obj21 = IDF._create_datadict("Construction")
    obj21["Name"] = "LTFLOOR"
    obj21["Outside Layer"] = "HF-C5"
    idf.add(obj21)

    obj22 = IDF._create_datadict("Construction")
    obj22["Name"] = "LTROOF"
    obj22["Outside Layer"] = "ROOF DECK"
    obj22["Layer 2"] = "FIBERGLASS QUILT-2"
    obj22["Layer 3"] = "PLASTERBOARD-2"
    idf.add(obj22)

    obj23 = IDF._create_datadict("Zone")
    obj23["Name"] = "ZONE ONE"
    obj23["Direction of Relative North"] = 0.0
    obj23["X Origin"] = 0.0
    obj23["Y Origin"] = 0.0
    obj23["Z Origin"] = 0.0
    obj23["Type"] = 1
    obj23["Multiplier"] = 1
    obj23["Ceiling Height"] = 2.7
    obj23["Volume"] = 129.6
    idf.add(obj23)

    obj24 = IDF._create_datadict("GlobalGeometryRules")
    obj24["Starting Vertex Position"] = "UpperLeftCorner"
    obj24["Vertex Entry Direction"] = "Counterclockwise"
    obj24["Coordinate System"] = "World"
    idf.add(obj24)

    obj25 = IDF._create_datadict("BuildingSurface:Detailed")
    obj25["Name"] = "SURFACE NORTH"
    obj25["Surface Type"] = "Wall"
    obj25["Construction Name"] = "LTWALL"
    obj25["Zone Name"] = "ZONE ONE"
    obj25["Outside Boundary Condition"] = "Outdoors"
    obj25["Outside Boundary Condition Object"] = None
    obj25["Sun Exposure"] = "SunExposed"
    obj25["Wind Exposure"] = "WindExposed"
    obj25["View Factor to Ground"] = 0.5
    obj25["Number of Vertices"] = 4.0
    obj25.add_extensible(8.0, 6.0, 2.7)
    obj25.add_extensible(8.0, 6.0, 0.0)
    obj25.add_extensible(0.0, 6.0, 0.0)
    obj25.add_extensible(0.0, 6.0, 2.7)
    idf.add(obj25)

    obj26 = IDF._create_datadict("BuildingSurface:Detailed")
    obj26["Name"] = "ZONE SURFACE EAST"
    obj26["Surface Type"] = "Wall"
    obj26["Construction Name"] = "LTWALL"
    obj26["Zone Name"] = "ZONE ONE"
    obj26["Outside Boundary Condition"] = "Outdoors"
    obj26["Outside Boundary Condition Object"] = None
    obj26["Sun Exposure"] = "SunExposed"
    obj26["Wind Exposure"] = "WindExposed"
    obj26["View Factor to Ground"] = 0.5
    obj26["Number of Vertices"] = 4.0
    obj26.add_extensible(8.0, 0.0, 2.7)
    obj26.add_extensible(8.0, 0.0, 0.0)
    obj26.add_extensible(8.0, 6.0, 0.0)
    obj26.add_extensible(8.0, 6.0, 2.7)
    idf.add(obj26)

    obj27 = IDF._create_datadict("BuildingSurface:Detailed")
    obj27["Name"] = "ZONE SURFACE SOUTH"
    obj27["Surface Type"] = "Wall"
    obj27["Construction Name"] = "LTWALL"
    obj27["Zone Name"] = "ZONE ONE"
    obj27["Outside Boundary Condition"] = "Outdoors"
    obj27["Outside Boundary Condition Object"] = None
    obj27["Sun Exposure"] = "SunExposed"
    obj27["Wind Exposure"] = "WindExposed"
    obj27["View Factor to Ground"] = 0.5
    obj27["Number of Vertices"] = 4.0
    obj27.add_extensible(0.0, 0.0, 2.7)
    obj27.add_extensible(0.0, 0.0, 0.0)
    obj27.add_extensible(8.0, 0.0, 0.0)
    obj27.add_extensible(8.0, 0.0, 2.7)
    idf.add(obj27)

    obj28 = IDF._create_datadict("BuildingSurface:Detailed")
    obj28["Name"] = "ZONE SURFACE WEST"
    obj28["Surface Type"] = "Wall"
    obj28["Construction Name"] = "LTWALL"
    obj28["Zone Name"] = "ZONE ONE"
    obj28["Outside Boundary Condition"] = "Outdoors"
    obj28["Outside Boundary Condition Object"] = None
    obj28["Sun Exposure"] = "SunExposed"
    obj28["Wind Exposure"] = "WindExposed"
    obj28["View Factor to Ground"] = 0.5
    obj28["Number of Vertices"] = 4.0
    obj28.add_extensible(0.0, 6.0, 2.7)
    obj28.add_extensible(0.0, 6.0, 0.0)
    obj28.add_extensible(0.0, 0.0, 0.0)
    obj28.add_extensible(0.0, 0.0, 2.7)
    idf.add(obj28)

    obj29 = IDF._create_datadict("BuildingSurface:Detailed")
    obj29["Name"] = "ZONE SURFACE FLOOR"
    obj29["Surface Type"] = "Floor"
    obj29["Construction Name"] = "LTFLOOR"
    obj29["Zone Name"] = "ZONE ONE"
    obj29["Outside Boundary Condition"] = "Ground"
    obj29["Outside Boundary Condition Object"] = None
    obj29["Sun Exposure"] = "NoSun"
    obj29["Wind Exposure"] = "NoWind"
    obj29["View Factor to Ground"] = 0.0
    obj29["Number of Vertices"] = 4.0
    obj29.add_extensible(0.0, 0.0, 0.0)
    obj29.add_extensible(0.0, 6.0, 0.0)
    obj29.add_extensible(8.0, 6.0, 0.0)
    obj29.add_extensible(8.0, 0.0, 0.0)
    idf.add(obj29)

    obj30 = IDF._create_datadict("BuildingSurface:Detailed")
    obj30["Name"] = "ZONE SURFACE ROOF"
    obj30["Surface Type"] = "Roof"
    obj30["Construction Name"] = "LTROOF"
    obj30["Zone Name"] = "ZONE ONE"
    obj30["Outside Boundary Condition"] = "Outdoors"
    obj30["Outside Boundary Condition Object"] = None
    obj30["Sun Exposure"] = "SunExposed"
    obj30["Wind Exposure"] = "WindExposed"
    obj30["View Factor to Ground"] = 0.0
    obj30["Number of Vertices"] = 4.0
    obj30.add_extensible(0.0, 6.0, 2.7)
    obj30.add_extensible(0.0, 0.0, 2.7)
    obj30.add_extensible(8.0, 0.0, 2.7)
    obj30.add_extensible(8.0, 6.0, 2.7)
    idf.add(obj30)

    obj31 = IDF._create_datadict("ScheduleTypeLimits")
    obj31["Name"] = "Any Number"
    idf.add(obj31)

    obj32 = IDF._create_datadict("Schedule:Compact")
    obj32["Name"] = "ALWAYS 4"
    obj32["Schedule Type Limits Name"] = "Any Number"
    obj32.add_extensible("Through: 12/31")
    obj32.add_extensible("For: AllDays")
    obj32.add_extensible("Until: 24:00")
    obj32.add_extensible("4")
    idf.add(obj32)

    obj33 = IDF._create_datadict("Schedule:Compact")
    obj33["Name"] = "ALWAYS 20"
    obj33["Schedule Type Limits Name"] = "Any Number"
    obj33.add_extensible("Through: 12/31")
    obj33.add_extensible("For: AllDays")
    obj33.add_extensible("Until: 24:00")
    obj33.add_extensible("20")
    idf.add(obj33)

    obj34 = IDF._create_datadict("Schedule:Compact")
    obj34["Name"] = "ALWAYS 24"
    obj34["Schedule Type Limits Name"] = "Any Number"
    obj34.add_extensible("Through: 12/31")
    obj34.add_extensible("For: AllDays")
    obj34.add_extensible("Until: 24:00")
    obj34.add_extensible("24")
    idf.add(obj34)

    obj35 = IDF._create_datadict("ZoneHVAC:EquipmentConnections")
    obj35["Zone Name"] = "ZONE ONE"
    obj35["Zone Conditioning Equipment List Name"] = "ZONE ONE Equipment"
    obj35["Zone Air Inlet Node or NodeList Name"] = "ZONE ONE Supply Inlet"
    obj35["Zone Air Exhaust Node or NodeList Name"] = None
    obj35["Zone Air Node Name"] = "ZONE ONE Zone Air Node"
    obj35["Zone Return Air Node Name"] = "ZONE ONE Return Outlet"
    idf.add(obj35)

    obj36 = IDF._create_datadict("ZoneHVAC:EquipmentList")
    obj36["Name"] = "ZONE ONE Equipment"
    obj36.add_extensible(
        "ZoneHVAC:IdealLoadsAirSystem",
        "ZONE ONE Purchased Air",
        1,
        1)
    idf.add(obj36)

    obj37 = IDF._create_datadict("ZoneHVAC:IdealLoadsAirSystem")
    obj37["Name"] = "ZONE ONE Purchased Air"
    obj37["Availability Schedule Name"] = None
    obj37["Zone Supply Air Node Name"] = "ZONE ONE Supply Inlet"
    obj37["Zone Exhaust Air Node Name"] = None
    obj37["Maximum Heating Supply Air Temperature"] = 50.0
    obj37["Minimum Cooling Supply Air Temperature"] = 13.0
    obj37["Maximum Heating Supply Air Humidity Ratio"] = 0.015
    obj37["Minimum Cooling Supply Air Humidity Ratio"] = 0.01
    obj37["Heating Limit"] = "NoLimit"
    obj37["Maximum Heating Air Flow Rate"] = None
    obj37["Maximum Sensible Heating Capacity"] = None
    obj37["Cooling Limit"] = "NoLimit"
    obj37["Maximum Cooling Air Flow Rate"] = None
    obj37["Maximum Total Cooling Capacity"] = None
    obj37["Heating Availability Schedule Name"] = None
    obj37["Cooling Availability Schedule Name"] = None
    obj37["Dehumidification Control Type"] = "ConstantSupplyHumidityRatio"
    obj37["Cooling Sensible Heat Ratio"] = None
    obj37["Humidification Control Type"] = "ConstantSupplyHumidityRatio"
    obj37["Design Specification Outdoor Air Object Name"] = None
    obj37["Outdoor Air Inlet Node Name"] = None
    obj37["Demand Controlled Ventilation Type"] = None
    obj37["Outdoor Air Economizer Type"] = None
    obj37["Heat Recovery Type"] = None
    obj37["Sensible Heat Recovery Effectiveness"] = None
    obj37["Latent Heat Recovery Effectiveness"] = None
    idf.add(obj37)

    obj38 = IDF._create_datadict("ZoneControl:Thermostat")
    obj38["Name"] = "ZONE ONE Thermostat"
    obj38["Zone or ZoneList Name"] = "ZONE ONE"
    obj38["Control Type Schedule Name"] = "ALWAYS 4"
    obj38["Control 1 Object Type"] = "ThermostatSetpoint:DualSetpoint"
    obj38["Control 1 Name"] = "Office Thermostat Dual SP Control"
    idf.add(obj38)

    obj39 = IDF._create_datadict("ThermostatSetpoint:DualSetpoint")
    obj39["Name"] = "Office Thermostat Dual SP Control"
    obj39["Heating Setpoint Temperature Schedule Name"] = "ALWAYS 20"
    obj39["Cooling Setpoint Temperature Schedule Name"] = "ALWAYS 24"
    idf.add(obj39)

    obj40 = IDF._create_datadict("Output:Variable")
    obj40["Key Value"] = "*"
    obj40["Variable Name"] = "Site Outdoor Air Drybulb Temperature"
    obj40["Reporting Frequency"] = "Hourly"
    idf.add(obj40)

    obj41 = IDF._create_datadict("Output:Variable")
    obj41["Key Value"] = "*"
    obj41["Variable Name"] = "Zone Air System Sensible Cooling Energy"
    obj41["Reporting Frequency"] = "Hourly"
    idf.add(obj41)

    obj42 = IDF._create_datadict("Output:Variable")
    obj42["Key Value"] = "*"
    obj42["Variable Name"] = "Zone Air System Sensible Heating Energy"
    obj42["Reporting Frequency"] = "Hourly"
    idf.add(obj42)

    obj43 = IDF._create_datadict("Output:Variable")
    obj43["Key Value"] = "*"
    obj43["Variable Name"] = "Zone Air Temperature"
    obj43["Reporting Frequency"] = "Hourly"
    idf.add(obj43)

    obj44 = IDF._create_datadict("Output:Meter")
    obj44["Name"] = "DistrictHeating:Facility"
    obj44["Reporting Frequency"] = "Hourly"
    idf.add(obj44)

    obj45 = IDF._create_datadict("Output:Meter")
    obj45["Name"] = "DistrictCooling:Facility"
    obj45["Reporting Frequency"] = "Hourly"
    idf.add(obj45)

    obj46 = IDF._create_datadict("Output:Surfaces:Drawing")
    obj46["Report Type"] = "DXF"
    idf.add(obj46)

    obj47 = IDF._create_datadict("Output:Constructions")
    obj47["Details Type 1"] = "Constructions"
    idf.add(obj47)

    obj48 = IDF._create_datadict("Output:VariableDictionary")
    obj48["Key Field"] = "Regular"
    idf.add(obj48)

    idf.save(idf_file_path)
