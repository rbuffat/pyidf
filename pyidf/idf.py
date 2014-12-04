#!/usr/bin/python
"""
WARNING: This is an automatically generated file.
It is based on a modified Energy+.idd specification file.

Do not expect (yet) that it actually works!

Generation date: 2014-12-04

"""
import six
import re
import logging
from collections import OrderedDict
from internal_gains import *
from water_heaters_and_thermal_storage import *
from demand_limiting_controls import *
from variable_refrigerant_flow_equipment import *
from condenser_equipment_and_heat_exchangers import *
from exterior_equipment import *
from energy_management_system import *
from schedules import *
from non import *
from location_and_climate import *
from unitary_equipment import *
from economics import *
from zone_hvac_radiative import *
from parametrics import *
from external_interface import *
from performance_tables import *
from water_systems import *
from fluid_properties import *
from coils import *
from evaporative_coolers import *
from humidifiers_and_dehumidifiers import *
from zone_hvac_controls_and_thermostats import *
from simulation_parameters import *
from operational_faults import *
from performance_curves import *
from output_reporting import *
from fans import *
from compliance_objects import *
from refrigeration import *
from advanced_construction import *
from heat_recovery import *
from daylighting import *
from node import *
from plant import *
from zone_hvac_forced_air_units import *
from plant_heating_and_cooling_equipment import *
from solar_collectors import *
from zone_hvac_air_loop_terminal_units import *
from surface_construction_elements import *
from pumps import *
from zone_hvac_equipment_connections import *
from setpoint_managers import *
from hvac_design_objects import *
from zone_airflow import *
from room_air_models import *
from user_defined_hvac_and_plant_component_models import *
from thermal_zones_and_surfaces import *
from system_availability_managers import *
from natural_ventilation_and_duct_leakage import *
from detailed_ground_heat_transfer import *
from air_distribution import *
from controllers import *
from hvac_templates import *
from energyplus import *
from electric_load_center import *


logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())


class IDF(object):
    """ Represents an EnergyPlus IDF input file
    """

    required_objects = ["building", "globalgeometryrules"]
    unique_objects = ["zoneairheatbalancealgorithm", "surfaceconvectionalgorithm:outside:adaptivemodelselections", "outputcontrol:sizing:style", "runperiodcontrol:daylightsavingtime", "building", "zoneairmassflowconservation", "zoneaircontaminantbalance", "site:groundtemperature:shallow", "site:solarandvisiblespectrum", "output:debuggingdata", "outputcontrol:illuminancemap:style", "site:heightvariation", "lifecyclecost:parameters", "timestep", "convergencelimits", "heatbalancesettings:conductionfinitedifference", "version", "airflownetwork:simulationcontrol", "site:weatherstation", "globalgeometryrules", "output:energymanagementsystem", "shadowcalculation", "site:groundreflectance", "site:groundtemperature:buildingsurface", "surfaceconvectionalgorithm:inside", "hvactemplate:plant:chilledwaterloop", "site:location", "parametric:logic", "parametric:runcontrol", "surfaceconvectionalgorithm:inside:adaptivemodelselections", "zonecapacitancemultiplier:researchspecial", "compliance:building", "sizing:parameters", "hvactemplate:plant:hotwaterloop", "site:groundtemperature:deep", "hvactemplate:plant:mixedwaterloop", "outputcontrol:reportingtolerances", "simulationcontrol", "output:sqlite", "site:groundtemperature:fcfactormethod", "heatbalancealgorithm", "parametric:filenamesuffix", "geometrytransform", "outputcontrol:table:style", "surfaceconvectionalgorithm:outside", "output:table:summaryreports", "currencytype"]

    def __init__(self):
        """ Inits IDF with no data dictionary set."""
        self._data = OrderedDict()
        self._data["lead input"] = []
        self._data["simulation data"] = []
        self._data["version"] = []
        self._data["simulationcontrol"] = []
        self._data["building"] = []
        self._data["shadowcalculation"] = []
        self._data["surfaceconvectionalgorithm:inside"] = []
        self._data["surfaceconvectionalgorithm:outside"] = []
        self._data["heatbalancealgorithm"] = []
        self._data["heatbalancesettings:conductionfinitedifference"] = []
        self._data["zoneairheatbalancealgorithm"] = []
        self._data["zoneaircontaminantbalance"] = []
        self._data["zoneairmassflowconservation"] = []
        self._data["zonecapacitancemultiplier:researchspecial"] = []
        self._data["timestep"] = []
        self._data["convergencelimits"] = []
        self._data["programcontrol"] = []
        self._data["compliance:building"] = []
        self._data["site:location"] = []
        self._data["sizingperiod:designday"] = []
        self._data["sizingperiod:weatherfiledays"] = []
        self._data["sizingperiod:weatherfileconditiontype"] = []
        self._data["runperiod"] = []
        self._data["runperiod:customrange"] = []
        self._data["runperiodcontrol:specialdays"] = []
        self._data["runperiodcontrol:daylightsavingtime"] = []
        self._data["weatherproperty:skytemperature"] = []
        self._data["site:weatherstation"] = []
        self._data["site:heightvariation"] = []
        self._data["site:groundtemperature:buildingsurface"] = []
        self._data["site:groundtemperature:fcfactormethod"] = []
        self._data["site:groundtemperature:shallow"] = []
        self._data["site:groundtemperature:deep"] = []
        self._data["site:grounddomain"] = []
        self._data["site:groundreflectance"] = []
        self._data["site:groundreflectance:snowmodifier"] = []
        self._data["site:watermainstemperature"] = []
        self._data["site:precipitation"] = []
        self._data["roofirrigation"] = []
        self._data["site:solarandvisiblespectrum"] = []
        self._data["site:spectrumdata"] = []
        self._data["scheduletypelimits"] = []
        self._data["schedule:day:hourly"] = []
        self._data["schedule:day:interval"] = []
        self._data["schedule:day:list"] = []
        self._data["schedule:week:daily"] = []
        self._data["schedule:week:compact"] = []
        self._data["schedule:year"] = []
        self._data["schedule:compact"] = []
        self._data["schedule:constant"] = []
        self._data["schedule:file"] = []
        self._data["material"] = []
        self._data["material:nomass"] = []
        self._data["material:infraredtransparent"] = []
        self._data["material:airgap"] = []
        self._data["material:roofvegetation"] = []
        self._data["windowmaterial:simpleglazingsystem"] = []
        self._data["windowmaterial:glazing"] = []
        self._data["windowmaterial:glazinggroup:thermochromic"] = []
        self._data["windowmaterial:glazing:refractionextinctionmethod"] = []
        self._data["windowmaterial:gas"] = []
        self._data["windowgap:supportpillar"] = []
        self._data["windowgap:deflectionstate"] = []
        self._data["windowmaterial:gasmixture"] = []
        self._data["windowmaterial:gap"] = []
        self._data["windowmaterial:shade"] = []
        self._data["windowmaterial:complexshade"] = []
        self._data["windowmaterial:blind"] = []
        self._data["windowmaterial:screen"] = []
        self._data["windowmaterial:shade:equivalentlayer"] = []
        self._data["windowmaterial:drape:equivalentlayer"] = []
        self._data["windowmaterial:blind:equivalentlayer"] = []
        self._data["windowmaterial:screen:equivalentlayer"] = []
        self._data["windowmaterial:glazing:equivalentlayer"] = []
        self._data["construction:windowequivalentlayer"] = []
        self._data["windowmaterial:gap:equivalentlayer"] = []
        self._data["materialproperty:moisturepenetrationdepth:settings"] = []
        self._data["materialproperty:phasechange"] = []
        self._data["materialproperty:variablethermalconductivity"] = []
        self._data["materialproperty:heatandmoisturetransfer:settings"] = []
        self._data["materialproperty:heatandmoisturetransfer:sorptionisotherm"] = []
        self._data["materialproperty:heatandmoisturetransfer:suction"] = []
        self._data["materialproperty:heatandmoisturetransfer:redistribution"] = []
        self._data["materialproperty:heatandmoisturetransfer:diffusion"] = []
        self._data["materialproperty:heatandmoisturetransfer:thermalconductivity"] = []
        self._data["materialproperty:glazingspectraldata"] = []
        self._data["construction"] = []
        self._data["construction:cfactorundergroundwall"] = []
        self._data["construction:ffactorgroundfloor"] = []
        self._data["construction:internalsource"] = []
        self._data["windowthermalmodel:params"] = []
        self._data["construction:complexfenestrationstate"] = []
        self._data["construction:windowdatafile"] = []
        self._data["globalgeometryrules"] = []
        self._data["geometrytransform"] = []
        self._data["zone"] = []
        self._data["zonelist"] = []
        self._data["zonegroup"] = []
        self._data["buildingsurface:detailed"] = []
        self._data["wall:detailed"] = []
        self._data["roofceiling:detailed"] = []
        self._data["floor:detailed"] = []
        self._data["wall:exterior"] = []
        self._data["wall:adiabatic"] = []
        self._data["wall:underground"] = []
        self._data["wall:interzone"] = []
        self._data["roof"] = []
        self._data["ceiling:adiabatic"] = []
        self._data["ceiling:interzone"] = []
        self._data["floor:groundcontact"] = []
        self._data["floor:adiabatic"] = []
        self._data["floor:interzone"] = []
        self._data["fenestrationsurface:detailed"] = []
        self._data["window"] = []
        self._data["door"] = []
        self._data["glazeddoor"] = []
        self._data["window:interzone"] = []
        self._data["door:interzone"] = []
        self._data["glazeddoor:interzone"] = []
        self._data["windowproperty:shadingcontrol"] = []
        self._data["windowproperty:frameanddivider"] = []
        self._data["windowproperty:airflowcontrol"] = []
        self._data["windowproperty:stormwindow"] = []
        self._data["internalmass"] = []
        self._data["shading:site"] = []
        self._data["shading:building"] = []
        self._data["shading:site:detailed"] = []
        self._data["shading:building:detailed"] = []
        self._data["shading:overhang"] = []
        self._data["shading:overhang:projection"] = []
        self._data["shading:fin"] = []
        self._data["shading:fin:projection"] = []
        self._data["shading:zone:detailed"] = []
        self._data["shadingproperty:reflectance"] = []
        self._data["surfaceproperty:heattransferalgorithm"] = []
        self._data["surfaceproperty:heattransferalgorithm:multiplesurface"] = []
        self._data["surfaceproperty:heattransferalgorithm:surfacelist"] = []
        self._data["surfaceproperty:heattransferalgorithm:construction"] = []
        self._data["surfacecontrol:movableinsulation"] = []
        self._data["surfaceproperty:othersidecoefficients"] = []
        self._data["surfaceproperty:othersideconditionsmodel"] = []
        self._data["surfaceconvectionalgorithm:inside:adaptivemodelselections"] = []
        self._data["surfaceconvectionalgorithm:outside:adaptivemodelselections"] = []
        self._data["surfaceconvectionalgorithm:inside:usercurve"] = []
        self._data["surfaceconvectionalgorithm:outside:usercurve"] = []
        self._data["surfaceproperty:convectioncoefficients"] = []
        self._data["surfaceproperty:convectioncoefficients:multiplesurface"] = []
        self._data["surfaceproperties:vaporcoefficients"] = []
        self._data["surfaceproperty:exteriornaturalventedcavity"] = []
        self._data["surfaceproperty:solarincidentinside"] = []
        self._data["complexfenestrationproperty:solarabsorbedlayers"] = []
        self._data["zoneproperty:userviewfactors:bysurfacename"] = []
        self._data["groundheattransfer:control"] = []
        self._data["groundheattransfer:slab:materials"] = []
        self._data["groundheattransfer:slab:matlprops"] = []
        self._data["groundheattransfer:slab:boundconds"] = []
        self._data["groundheattransfer:slab:bldgprops"] = []
        self._data["groundheattransfer:slab:insulation"] = []
        self._data["groundheattransfer:slab:equivalentslab"] = []
        self._data["groundheattransfer:slab:autogrid"] = []
        self._data["groundheattransfer:slab:manualgrid"] = []
        self._data["groundheattransfer:slab:xface"] = []
        self._data["groundheattransfer:slab:yface"] = []
        self._data["groundheattransfer:slab:zface"] = []
        self._data["groundheattransfer:basement:simparameters"] = []
        self._data["groundheattransfer:basement:matlprops"] = []
        self._data["groundheattransfer:basement:insulation"] = []
        self._data["groundheattransfer:basement:surfaceprops"] = []
        self._data["groundheattransfer:basement:bldgdata"] = []
        self._data["groundheattransfer:basement:interior"] = []
        self._data["groundheattransfer:basement:combldg"] = []
        self._data["groundheattransfer:basement:equivslab"] = []
        self._data["groundheattransfer:basement:equivautogrid"] = []
        self._data["groundheattransfer:basement:autogrid"] = []
        self._data["groundheattransfer:basement:manualgrid"] = []
        self._data["groundheattransfer:basement:xface"] = []
        self._data["groundheattransfer:basement:yface"] = []
        self._data["groundheattransfer:basement:zface"] = []
        self._data["roomairmodeltype"] = []
        self._data["roomair:temperaturepattern:userdefined"] = []
        self._data["roomair:temperaturepattern:constantgradient"] = []
        self._data["roomair:temperaturepattern:twogradient"] = []
        self._data["roomair:temperaturepattern:nondimensionalheight"] = []
        self._data["roomair:temperaturepattern:surfacemapping"] = []
        self._data["roomair:node"] = []
        self._data["roomairsettings:onenodedisplacementventilation"] = []
        self._data["roomairsettings:threenodedisplacementventilation"] = []
        self._data["roomairsettings:crossventilation"] = []
        self._data["roomairsettings:underfloorairdistributioninterior"] = []
        self._data["roomairsettings:underfloorairdistributionexterior"] = []
        self._data["people"] = []
        self._data["comfortviewfactorangles"] = []
        self._data["lights"] = []
        self._data["electricequipment"] = []
        self._data["gasequipment"] = []
        self._data["hotwaterequipment"] = []
        self._data["steamequipment"] = []
        self._data["otherequipment"] = []
        self._data["zonebaseboard:outdoortemperaturecontrolled"] = []
        self._data["zonecontaminantsourceandsink:carbondioxide"] = []
        self._data["zonecontaminantsourceandsink:generic:constant"] = []
        self._data["surfacecontaminantsourceandsink:generic:pressuredriven"] = []
        self._data["zonecontaminantsourceandsink:generic:cutoffmodel"] = []
        self._data["zonecontaminantsourceandsink:generic:decaysource"] = []
        self._data["surfacecontaminantsourceandsink:generic:boundarylayerdiffusion"] = []
        self._data["surfacecontaminantsourceandsink:generic:depositionvelocitysink"] = []
        self._data["zonecontaminantsourceandsink:generic:depositionratesink"] = []
        self._data["daylighting:controls"] = []
        self._data["daylighting:delight:controls"] = []
        self._data["daylighting:delight:referencepoint"] = []
        self._data["daylighting:delight:complexfenestration"] = []
        self._data["daylightingdevice:tubular"] = []
        self._data["daylightingdevice:shelf"] = []
        self._data["daylightingdevice:lightwell"] = []
        self._data["output:daylightfactors"] = []
        self._data["output:illuminancemap"] = []
        self._data["outputcontrol:illuminancemap:style"] = []
        self._data["zoneinfiltration:designflowrate"] = []
        self._data["zoneinfiltration:effectiveleakagearea"] = []
        self._data["zoneinfiltration:flowcoefficient"] = []
        self._data["zoneventilation:designflowrate"] = []
        self._data["zoneventilation:windandstackopenarea"] = []
        self._data["zoneairbalance:outdoorair"] = []
        self._data["zonemixing"] = []
        self._data["zonecrossmixing"] = []
        self._data["zonerefrigerationdoormixing"] = []
        self._data["zoneearthtube"] = []
        self._data["zonecooltower:shower"] = []
        self._data["zonethermalchimney"] = []
        self._data["airflownetwork:simulationcontrol"] = []
        self._data["airflownetwork:multizone:zone"] = []
        self._data["airflownetwork:multizone:surface"] = []
        self._data["airflownetwork:multizone:referencecrackconditions"] = []
        self._data["airflownetwork:multizone:surface:crack"] = []
        self._data["airflownetwork:multizone:surface:effectiveleakagearea"] = []
        self._data["airflownetwork:multizone:component:detailedopening"] = []
        self._data["airflownetwork:multizone:component:simpleopening"] = []
        self._data["airflownetwork:multizone:component:horizontalopening"] = []
        self._data["airflownetwork:multizone:component:zoneexhaustfan"] = []
        self._data["airflownetwork:multizone:externalnode"] = []
        self._data["airflownetwork:multizone:windpressurecoefficientarray"] = []
        self._data["airflownetwork:multizone:windpressurecoefficientvalues"] = []
        self._data["airflownetwork:distribution:node"] = []
        self._data["airflownetwork:distribution:component:leak"] = []
        self._data["airflownetwork:distribution:component:leakageratio"] = []
        self._data["airflownetwork:distribution:component:duct"] = []
        self._data["airflownetwork:distribution:component:fan"] = []
        self._data["airflownetwork:distribution:component:coil"] = []
        self._data["airflownetwork:distribution:component:heatexchanger"] = []
        self._data["airflownetwork:distribution:component:terminalunit"] = []
        self._data["airflownetwork:distribution:component:constantpressuredrop"] = []
        self._data["airflownetwork:distribution:linkage"] = []
        self._data["exterior:lights"] = []
        self._data["exterior:fuelequipment"] = []
        self._data["exterior:waterequipment"] = []
        self._data["hvactemplate:thermostat"] = []
        self._data["hvactemplate:zone:idealloadsairsystem"] = []
        self._data["hvactemplate:zone:baseboardheat"] = []
        self._data["hvactemplate:zone:fancoil"] = []
        self._data["hvactemplate:zone:ptac"] = []
        self._data["hvactemplate:zone:pthp"] = []
        self._data["hvactemplate:zone:watertoairheatpump"] = []
        self._data["hvactemplate:zone:vrf"] = []
        self._data["hvactemplate:zone:unitary"] = []
        self._data["hvactemplate:zone:vav"] = []
        self._data["hvactemplate:zone:vav:fanpowered"] = []
        self._data["hvactemplate:zone:vav:heatandcool"] = []
        self._data["hvactemplate:zone:constantvolume"] = []
        self._data["hvactemplate:zone:dualduct"] = []
        self._data["hvactemplate:system:vrf"] = []
        self._data["hvactemplate:system:unitary"] = []
        self._data["hvactemplate:system:unitaryheatpump:airtoair"] = []
        self._data["hvactemplate:system:unitarysystem"] = []
        self._data["hvactemplate:system:vav"] = []
        self._data["hvactemplate:system:packagedvav"] = []
        self._data["hvactemplate:system:constantvolume"] = []
        self._data["hvactemplate:system:dualduct"] = []
        self._data["hvactemplate:system:dedicatedoutdoorair"] = []
        self._data["hvactemplate:plant:chilledwaterloop"] = []
        self._data["hvactemplate:plant:chiller"] = []
        self._data["hvactemplate:plant:chiller:objectreference"] = []
        self._data["hvactemplate:plant:tower"] = []
        self._data["hvactemplate:plant:tower:objectreference"] = []
        self._data["hvactemplate:plant:hotwaterloop"] = []
        self._data["hvactemplate:plant:boiler"] = []
        self._data["hvactemplate:plant:boiler:objectreference"] = []
        self._data["hvactemplate:plant:mixedwaterloop"] = []
        self._data["designspecification:outdoorair"] = []
        self._data["designspecification:zoneairdistribution"] = []
        self._data["sizing:parameters"] = []
        self._data["sizing:zone"] = []
        self._data["designspecification:zonehvac:sizing"] = []
        self._data["sizing:system"] = []
        self._data["sizing:plant"] = []
        self._data["outputcontrol:sizing:style"] = []
        self._data["zonecontrol:humidistat"] = []
        self._data["zonecontrol:thermostat"] = []
        self._data["zonecontrol:thermostat:operativetemperature"] = []
        self._data["zonecontrol:thermostat:thermalcomfort"] = []
        self._data["zonecontrol:thermostat:temperatureandhumidity"] = []
        self._data["thermostatsetpoint:singleheating"] = []
        self._data["thermostatsetpoint:singlecooling"] = []
        self._data["thermostatsetpoint:singleheatingorcooling"] = []
        self._data["thermostatsetpoint:dualsetpoint"] = []
        self._data["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = []
        self._data["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = []
        self._data["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = []
        self._data["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = []
        self._data["zonecontrol:thermostat:stageddualsetpoint"] = []
        self._data["zonecontrol:contaminantcontroller"] = []
        self._data["zonehvac:idealloadsairsystem"] = []
        self._data["zonehvac:fourpipefancoil"] = []
        self._data["zonehvac:windowairconditioner"] = []
        self._data["zonehvac:packagedterminalairconditioner"] = []
        self._data["zonehvac:packagedterminalheatpump"] = []
        self._data["zonehvac:watertoairheatpump"] = []
        self._data["zonehvac:dehumidifier:dx"] = []
        self._data["zonehvac:energyrecoveryventilator"] = []
        self._data["zonehvac:energyrecoveryventilator:controller"] = []
        self._data["zonehvac:unitventilator"] = []
        self._data["zonehvac:unitheater"] = []
        self._data["zonehvac:evaporativecoolerunit"] = []
        self._data["zonehvac:outdoorairunit"] = []
        self._data["zonehvac:outdoorairunit:equipmentlist"] = []
        self._data["zonehvac:terminalunit:variablerefrigerantflow"] = []
        self._data["zonehvac:baseboard:radiantconvective:water"] = []
        self._data["zonehvac:baseboard:radiantconvective:steam"] = []
        self._data["zonehvac:baseboard:radiantconvective:electric"] = []
        self._data["zonehvac:baseboard:convective:water"] = []
        self._data["zonehvac:baseboard:convective:electric"] = []
        self._data["zonehvac:lowtemperatureradiant:variableflow"] = []
        self._data["zonehvac:lowtemperatureradiant:constantflow"] = []
        self._data["zonehvac:lowtemperatureradiant:electric"] = []
        self._data["zonehvac:lowtemperatureradiant:surfacegroup"] = []
        self._data["zonehvac:hightemperatureradiant"] = []
        self._data["zonehvac:ventilatedslab"] = []
        self._data["zonehvac:ventilatedslab:slabgroup"] = []
        self._data["airterminal:singleduct:uncontrolled"] = []
        self._data["airterminal:singleduct:constantvolume:reheat"] = []
        self._data["airterminal:singleduct:vav:noreheat"] = []
        self._data["airterminal:singleduct:vav:reheat"] = []
        self._data["airterminal:singleduct:vav:reheat:variablespeedfan"] = []
        self._data["airterminal:singleduct:vav:heatandcool:noreheat"] = []
        self._data["airterminal:singleduct:vav:heatandcool:reheat"] = []
        self._data["airterminal:singleduct:seriespiu:reheat"] = []
        self._data["airterminal:singleduct:parallelpiu:reheat"] = []
        self._data["airterminal:singleduct:constantvolume:fourpipeinduction"] = []
        self._data["airterminal:singleduct:constantvolume:cooledbeam"] = []
        self._data["airterminal:singleduct:inletsidemixer"] = []
        self._data["airterminal:singleduct:supplysidemixer"] = []
        self._data["airterminal:dualduct:constantvolume"] = []
        self._data["airterminal:dualduct:vav"] = []
        self._data["airterminal:dualduct:vav:outdoorair"] = []
        self._data["zonehvac:airdistributionunit"] = []
        self._data["zonehvac:equipmentlist"] = []
        self._data["zonehvac:equipmentconnections"] = []
        self._data["fan:constantvolume"] = []
        self._data["fan:variablevolume"] = []
        self._data["fan:onoff"] = []
        self._data["fan:zoneexhaust"] = []
        self._data["fanperformance:nightventilation"] = []
        self._data["fan:componentmodel"] = []
        self._data["coil:cooling:water"] = []
        self._data["coil:cooling:water:detailedgeometry"] = []
        self._data["coil:cooling:dx:singlespeed"] = []
        self._data["coil:cooling:dx:twospeed"] = []
        self._data["coil:cooling:dx:multispeed"] = []
        self._data["coil:cooling:dx:variablespeed"] = []
        self._data["coil:cooling:dx:twostagewithhumiditycontrolmode"] = []
        self._data["coilperformance:dx:cooling"] = []
        self._data["coil:cooling:dx:variablerefrigerantflow"] = []
        self._data["coil:heating:dx:variablerefrigerantflow"] = []
        self._data["coil:heating:water"] = []
        self._data["coil:heating:steam"] = []
        self._data["coil:heating:electric"] = []
        self._data["coil:heating:electric:multistage"] = []
        self._data["coil:heating:gas"] = []
        self._data["coil:heating:gas:multistage"] = []
        self._data["coil:heating:desuperheater"] = []
        self._data["coil:heating:dx:singlespeed"] = []
        self._data["coil:heating:dx:multispeed"] = []
        self._data["coil:heating:dx:variablespeed"] = []
        self._data["coil:cooling:watertoairheatpump:parameterestimation"] = []
        self._data["coil:heating:watertoairheatpump:parameterestimation"] = []
        self._data["coil:cooling:watertoairheatpump:equationfit"] = []
        self._data["coil:cooling:watertoairheatpump:variablespeedequationfit"] = []
        self._data["coil:heating:watertoairheatpump:equationfit"] = []
        self._data["coil:heating:watertoairheatpump:variablespeedequationfit"] = []
        self._data["coil:waterheating:airtowaterheatpump"] = []
        self._data["coil:waterheating:desuperheater"] = []
        self._data["coilsystem:cooling:dx"] = []
        self._data["coilsystem:heating:dx"] = []
        self._data["coilsystem:cooling:water:heatexchangerassisted"] = []
        self._data["coilsystem:cooling:dx:heatexchangerassisted"] = []
        self._data["coil:cooling:dx:singlespeed:thermalstorage"] = []
        self._data["evaporativecooler:direct:celdekpad"] = []
        self._data["evaporativecooler:indirect:celdekpad"] = []
        self._data["evaporativecooler:indirect:wetcoil"] = []
        self._data["evaporativecooler:indirect:researchspecial"] = []
        self._data["evaporativecooler:direct:researchspecial"] = []
        self._data["humidifier:steam:electric"] = []
        self._data["dehumidifier:desiccant:nofans"] = []
        self._data["dehumidifier:desiccant:system"] = []
        self._data["heatexchanger:airtoair:flatplate"] = []
        self._data["heatexchanger:airtoair:sensibleandlatent"] = []
        self._data["heatexchanger:desiccant:balancedflow"] = []
        self._data["heatexchanger:desiccant:balancedflow:performancedatatype1"] = []
        self._data["airloophvac:unitarysystem"] = []
        self._data["unitarysystemperformance:heatpump:multispeed"] = []
        self._data["airloophvac:unitary:furnace:heatonly"] = []
        self._data["airloophvac:unitary:furnace:heatcool"] = []
        self._data["airloophvac:unitaryheatonly"] = []
        self._data["airloophvac:unitaryheatcool"] = []
        self._data["airloophvac:unitaryheatpump:airtoair"] = []
        self._data["airloophvac:unitaryheatpump:watertoair"] = []
        self._data["airloophvac:unitaryheatcool:vavchangeoverbypass"] = []
        self._data["airloophvac:unitaryheatpump:airtoair:multispeed"] = []
        self._data["airconditioner:variablerefrigerantflow"] = []
        self._data["zoneterminalunitlist"] = []
        self._data["controller:watercoil"] = []
        self._data["controller:outdoorair"] = []
        self._data["controller:mechanicalventilation"] = []
        self._data["airloophvac:controllerlist"] = []
        self._data["airloophvac"] = []
        self._data["airloophvac:outdoorairsystem:equipmentlist"] = []
        self._data["airloophvac:outdoorairsystem"] = []
        self._data["outdoorair:mixer"] = []
        self._data["airloophvac:zonesplitter"] = []
        self._data["airloophvac:supplyplenum"] = []
        self._data["airloophvac:supplypath"] = []
        self._data["airloophvac:zonemixer"] = []
        self._data["airloophvac:returnplenum"] = []
        self._data["airloophvac:returnpath"] = []
        self._data["branch"] = []
        self._data["branchlist"] = []
        self._data["connector:splitter"] = []
        self._data["connector:mixer"] = []
        self._data["connectorlist"] = []
        self._data["nodelist"] = []
        self._data["outdoorair:node"] = []
        self._data["outdoorair:nodelist"] = []
        self._data["pipe:adiabatic"] = []
        self._data["pipe:adiabatic:steam"] = []
        self._data["pipe:indoor"] = []
        self._data["pipe:outdoor"] = []
        self._data["pipe:underground"] = []
        self._data["pipingsystem:underground:domain"] = []
        self._data["pipingsystem:underground:pipecircuit"] = []
        self._data["pipingsystem:underground:pipesegment"] = []
        self._data["duct"] = []
        self._data["pump:variablespeed"] = []
        self._data["pump:constantspeed"] = []
        self._data["pump:variablespeed:condensate"] = []
        self._data["headeredpumps:constantspeed"] = []
        self._data["headeredpumps:variablespeed"] = []
        self._data["temperingvalve"] = []
        self._data["loadprofile:plant"] = []
        self._data["solarcollectorperformance:flatplate"] = []
        self._data["solarcollector:flatplate:water"] = []
        self._data["solarcollector:flatplate:photovoltaicthermal"] = []
        self._data["solarcollectorperformance:photovoltaicthermal:simple"] = []
        self._data["solarcollector:integralcollectorstorage"] = []
        self._data["solarcollectorperformance:integralcollectorstorage"] = []
        self._data["solarcollector:unglazedtranspired"] = []
        self._data["solarcollector:unglazedtranspired:multisystem"] = []
        self._data["boiler:hotwater"] = []
        self._data["boiler:steam"] = []
        self._data["chiller:electric:eir"] = []
        self._data["chiller:electric:reformulatedeir"] = []
        self._data["chiller:electric"] = []
        self._data["chiller:absorption:indirect"] = []
        self._data["chiller:absorption"] = []
        self._data["chiller:constantcop"] = []
        self._data["chiller:enginedriven"] = []
        self._data["chiller:combustionturbine"] = []
        self._data["chillerheater:absorption:directfired"] = []
        self._data["chillerheater:absorption:doubleeffect"] = []
        self._data["heatpump:watertowater:equationfit:heating"] = []
        self._data["heatpump:watertowater:equationfit:cooling"] = []
        self._data["heatpump:watertowater:parameterestimation:cooling"] = []
        self._data["heatpump:watertowater:parameterestimation:heating"] = []
        self._data["districtcooling"] = []
        self._data["districtheating"] = []
        self._data["plantcomponent:temperaturesource"] = []
        self._data["centralheatpumpsystem"] = []
        self._data["chillerheaterperformance:electric:eir"] = []
        self._data["coolingtower:singlespeed"] = []
        self._data["coolingtower:twospeed"] = []
        self._data["coolingtower:variablespeed:merkel"] = []
        self._data["coolingtower:variablespeed"] = []
        self._data["coolingtowerperformance:cooltools"] = []
        self._data["coolingtowerperformance:yorkcalc"] = []
        self._data["evaporativefluidcooler:singlespeed"] = []
        self._data["evaporativefluidcooler:twospeed"] = []
        self._data["fluidcooler:singlespeed"] = []
        self._data["fluidcooler:twospeed"] = []
        self._data["groundheatexchanger:vertical"] = []
        self._data["groundheatexchanger:pond"] = []
        self._data["groundheatexchanger:surface"] = []
        self._data["groundheatexchanger:horizontaltrench"] = []
        self._data["heatexchanger:fluidtofluid"] = []
        self._data["waterheater:mixed"] = []
        self._data["waterheater:stratified"] = []
        self._data["waterheater:sizing"] = []
        self._data["waterheater:heatpump"] = []
        self._data["thermalstorage:ice:simple"] = []
        self._data["thermalstorage:ice:detailed"] = []
        self._data["thermalstorage:chilledwater:mixed"] = []
        self._data["thermalstorage:chilledwater:stratified"] = []
        self._data["plantloop"] = []
        self._data["condenserloop"] = []
        self._data["plantequipmentlist"] = []
        self._data["condenserequipmentlist"] = []
        self._data["plantequipmentoperation:uncontrolled"] = []
        self._data["plantequipmentoperation:coolingload"] = []
        self._data["plantequipmentoperation:heatingload"] = []
        self._data["plantequipmentoperation:outdoordrybulb"] = []
        self._data["plantequipmentoperation:outdoorwetbulb"] = []
        self._data["plantequipmentoperation:outdoorrelativehumidity"] = []
        self._data["plantequipmentoperation:outdoordewpoint"] = []
        self._data["plantequipmentoperation:componentsetpoint"] = []
        self._data["plantequipmentoperation:outdoordrybulbdifference"] = []
        self._data["plantequipmentoperation:outdoorwetbulbdifference"] = []
        self._data["plantequipmentoperation:outdoordewpointdifference"] = []
        self._data["plantequipmentoperationschemes"] = []
        self._data["condenserequipmentoperationschemes"] = []
        self._data["energymanagementsystem:sensor"] = []
        self._data["energymanagementsystem:actuator"] = []
        self._data["energymanagementsystem:programcallingmanager"] = []
        self._data["energymanagementsystem:program"] = []
        self._data["energymanagementsystem:subroutine"] = []
        self._data["energymanagementsystem:globalvariable"] = []
        self._data["energymanagementsystem:outputvariable"] = []
        self._data["energymanagementsystem:meteredoutputvariable"] = []
        self._data["energymanagementsystem:trendvariable"] = []
        self._data["energymanagementsystem:internalvariable"] = []
        self._data["energymanagementsystem:curveortableindexvariable"] = []
        self._data["energymanagementsystem:constructionindexvariable"] = []
        self._data["externalinterface"] = []
        self._data["externalinterface:schedule"] = []
        self._data["externalinterface:variable"] = []
        self._data["externalinterface:actuator"] = []
        self._data["externalinterface:functionalmockupunitimport"] = []
        self._data["externalinterface:functionalmockupunitimport:from:variable"] = []
        self._data["externalinterface:functionalmockupunitimport:to:schedule"] = []
        self._data["externalinterface:functionalmockupunitimport:to:actuator"] = []
        self._data["externalinterface:functionalmockupunitimport:to:variable"] = []
        self._data["externalinterface:functionalmockupunitexport:from:variable"] = []
        self._data["externalinterface:functionalmockupunitexport:to:schedule"] = []
        self._data["externalinterface:functionalmockupunitexport:to:actuator"] = []
        self._data["externalinterface:functionalmockupunitexport:to:variable"] = []
        self._data["zonehvac:forcedair:userdefined"] = []
        self._data["airterminal:singleduct:userdefined"] = []
        self._data["coil:userdefined"] = []
        self._data["plantcomponent:userdefined"] = []
        self._data["plantequipmentoperation:userdefined"] = []
        self._data["availabilitymanager:scheduled"] = []
        self._data["availabilitymanager:scheduledon"] = []
        self._data["availabilitymanager:scheduledoff"] = []
        self._data["availabilitymanager:optimumstart"] = []
        self._data["availabilitymanager:nightcycle"] = []
        self._data["availabilitymanager:differentialthermostat"] = []
        self._data["availabilitymanager:hightemperatureturnoff"] = []
        self._data["availabilitymanager:hightemperatureturnon"] = []
        self._data["availabilitymanager:lowtemperatureturnoff"] = []
        self._data["availabilitymanager:lowtemperatureturnon"] = []
        self._data["availabilitymanager:nightventilation"] = []
        self._data["availabilitymanager:hybridventilation"] = []
        self._data["availabilitymanagerassignmentlist"] = []
        self._data["setpointmanager:scheduled"] = []
        self._data["setpointmanager:scheduled:dualsetpoint"] = []
        self._data["setpointmanager:outdoorairreset"] = []
        self._data["setpointmanager:singlezone:reheat"] = []
        self._data["setpointmanager:singlezone:heating"] = []
        self._data["setpointmanager:singlezone:cooling"] = []
        self._data["setpointmanager:singlezone:humidity:minimum"] = []
        self._data["setpointmanager:singlezone:humidity:maximum"] = []
        self._data["setpointmanager:mixedair"] = []
        self._data["setpointmanager:outdoorairpretreat"] = []
        self._data["setpointmanager:warmest"] = []
        self._data["setpointmanager:coldest"] = []
        self._data["setpointmanager:returnairbypassflow"] = []
        self._data["setpointmanager:warmesttemperatureflow"] = []
        self._data["setpointmanager:multizone:heating:average"] = []
        self._data["setpointmanager:multizone:cooling:average"] = []
        self._data["setpointmanager:multizone:minimumhumidity:average"] = []
        self._data["setpointmanager:multizone:maximumhumidity:average"] = []
        self._data["setpointmanager:multizone:humidity:minimum"] = []
        self._data["setpointmanager:multizone:humidity:maximum"] = []
        self._data["setpointmanager:followoutdoorairtemperature"] = []
        self._data["setpointmanager:followsystemnodetemperature"] = []
        self._data["setpointmanager:followgroundtemperature"] = []
        self._data["setpointmanager:condenserenteringreset"] = []
        self._data["setpointmanager:condenserenteringreset:ideal"] = []
        self._data["setpointmanager:singlezone:onestagecooling"] = []
        self._data["setpointmanager:singlezone:onestageheating"] = []
        self._data["refrigeration:case"] = []
        self._data["refrigeration:compressorrack"] = []
        self._data["refrigeration:caseandwalkinlist"] = []
        self._data["refrigeration:condenser:aircooled"] = []
        self._data["refrigeration:condenser:evaporativecooled"] = []
        self._data["refrigeration:condenser:watercooled"] = []
        self._data["refrigeration:condenser:cascade"] = []
        self._data["refrigeration:gascooler:aircooled"] = []
        self._data["refrigeration:transferloadlist"] = []
        self._data["refrigeration:subcooler"] = []
        self._data["refrigeration:compressor"] = []
        self._data["refrigeration:compressorlist"] = []
        self._data["refrigeration:system"] = []
        self._data["refrigeration:transcriticalsystem"] = []
        self._data["refrigeration:secondarysystem"] = []
        self._data["refrigeration:walkin"] = []
        self._data["refrigeration:airchiller"] = []
        self._data["zonehvac:refrigerationchillerset"] = []
        self._data["demandmanagerassignmentlist"] = []
        self._data["demandmanager:exteriorlights"] = []
        self._data["demandmanager:lights"] = []
        self._data["demandmanager:electricequipment"] = []
        self._data["demandmanager:thermostats"] = []
        self._data["generator:internalcombustionengine"] = []
        self._data["generator:combustionturbine"] = []
        self._data["generator:microturbine"] = []
        self._data["generator:photovoltaic"] = []
        self._data["photovoltaicperformance:simple"] = []
        self._data["photovoltaicperformance:equivalentone-diode"] = []
        self._data["photovoltaicperformance:sandia"] = []
        self._data["generator:fuelcell"] = []
        self._data["generator:fuelcell:powermodule"] = []
        self._data["generator:fuelcell:airsupply"] = []
        self._data["generator:fuelcell:watersupply"] = []
        self._data["generator:fuelcell:auxiliaryheater"] = []
        self._data["generator:fuelcell:exhaustgastowaterheatexchanger"] = []
        self._data["generator:fuelcell:electricalstorage"] = []
        self._data["generator:fuelcell:inverter"] = []
        self._data["generator:fuelcell:stackcooler"] = []
        self._data["generator:microchp"] = []
        self._data["generator:microchp:nonnormalizedparameters"] = []
        self._data["generator:fuelsupply"] = []
        self._data["generator:windturbine"] = []
        self._data["electricloadcenter:generators"] = []
        self._data["electricloadcenter:inverter:simple"] = []
        self._data["electricloadcenter:inverter:functionofpower"] = []
        self._data["electricloadcenter:inverter:lookuptable"] = []
        self._data["electricloadcenter:storage:simple"] = []
        self._data["electricloadcenter:storage:battery"] = []
        self._data["electricloadcenter:transformer"] = []
        self._data["electricloadcenter:distribution"] = []
        self._data["wateruse:equipment"] = []
        self._data["wateruse:connections"] = []
        self._data["wateruse:storage"] = []
        self._data["wateruse:well"] = []
        self._data["wateruse:raincollector"] = []
        self._data["faultmodel:temperaturesensoroffset:outdoorair"] = []
        self._data["faultmodel:humiditysensoroffset:outdoorair"] = []
        self._data["faultmodel:enthalpysensoroffset:outdoorair"] = []
        self._data["faultmodel:pressuresensoroffset:outdoorair"] = []
        self._data["faultmodel:temperaturesensoroffset:returnair"] = []
        self._data["faultmodel:enthalpysensoroffset:returnair"] = []
        self._data["faultmodel:fouling:coil"] = []
        self._data["matrix:twodimension"] = []
        self._data["curve:linear"] = []
        self._data["curve:quadlinear"] = []
        self._data["curve:quadratic"] = []
        self._data["curve:cubic"] = []
        self._data["curve:quartic"] = []
        self._data["curve:exponent"] = []
        self._data["curve:bicubic"] = []
        self._data["curve:biquadratic"] = []
        self._data["curve:quadraticlinear"] = []
        self._data["curve:triquadratic"] = []
        self._data["curve:functional:pressuredrop"] = []
        self._data["curve:fanpressurerise"] = []
        self._data["curve:exponentialskewnormal"] = []
        self._data["curve:sigmoid"] = []
        self._data["curve:rectangularhyperbola1"] = []
        self._data["curve:rectangularhyperbola2"] = []
        self._data["curve:exponentialdecay"] = []
        self._data["curve:doubleexponentialdecay"] = []
        self._data["table:oneindependentvariable"] = []
        self._data["table:twoindependentvariables"] = []
        self._data["table:multivariablelookup"] = []
        self._data["fluidproperties:name"] = []
        self._data["fluidproperties:glycolconcentration"] = []
        self._data["fluidproperties:temperatures"] = []
        self._data["fluidproperties:saturated"] = []
        self._data["fluidproperties:superheated"] = []
        self._data["fluidproperties:concentration"] = []
        self._data["currencytype"] = []
        self._data["componentcost:adjustments"] = []
        self._data["componentcost:reference"] = []
        self._data["componentcost:lineitem"] = []
        self._data["utilitycost:tariff"] = []
        self._data["utilitycost:qualify"] = []
        self._data["utilitycost:charge:simple"] = []
        self._data["utilitycost:charge:block"] = []
        self._data["utilitycost:ratchet"] = []
        self._data["utilitycost:variable"] = []
        self._data["utilitycost:computation"] = []
        self._data["lifecyclecost:parameters"] = []
        self._data["lifecyclecost:recurringcosts"] = []
        self._data["lifecyclecost:nonrecurringcost"] = []
        self._data["lifecyclecost:usepriceescalation"] = []
        self._data["lifecyclecost:useadjustment"] = []
        self._data["parametric:setvalueforrun"] = []
        self._data["parametric:logic"] = []
        self._data["parametric:runcontrol"] = []
        self._data["parametric:filenamesuffix"] = []
        self._data["output:variabledictionary"] = []
        self._data["output:surfaces:list"] = []
        self._data["output:surfaces:drawing"] = []
        self._data["output:schedules"] = []
        self._data["output:constructions"] = []
        self._data["output:energymanagementsystem"] = []
        self._data["outputcontrol:surfacecolorscheme"] = []
        self._data["output:table:summaryreports"] = []
        self._data["output:table:timebins"] = []
        self._data["output:table:monthly"] = []
        self._data["outputcontrol:table:style"] = []
        self._data["outputcontrol:reportingtolerances"] = []
        self._data["output:variable"] = []
        self._data["output:meter"] = []
        self._data["output:meter:meterfileonly"] = []
        self._data["output:meter:cumulative"] = []
        self._data["output:meter:cumulative:meterfileonly"] = []
        self._data["meter:custom"] = []
        self._data["meter:customdecrement"] = []
        self._data["output:sqlite"] = []
        self._data["output:environmentalimpactfactors"] = []
        self._data["environmentalimpactfactors"] = []
        self._data["fuelfactors"] = []
        self._data["output:diagnostics"] = []
        self._data["output:debuggingdata"] = []
        self._data["output:preprocessormessage"] = []
        self.comment_headers = []
   
   
    def add(self, dataobject):
        """ Adds a data object to the IDF. If data object is unique, it replaces an
        eventual existing data object

        Args:
            dataobject: the data object
        """
        lower_name = dataobject.internal_name.lower()
        if lower_name in self.unique_objects:
            self._data[lower_name] = [dataobject]
        else:
            self._data[lower_name].append(dataobject)        

    def get(self, name):
        """ Returns a list of all objects

            Args:
                name (str): IDD name of objects (see helper.DataObject)
            Returns: 
                list: list of objects

            Raises:
                ValueError: if no objects are found
        """
        if isinstance(name, str):
            name_lower = name.lower()
            if name_lower not in self._data:
                raise ValueError("{} is not a valid name".format(name))
            else:
                return self._data[name_lower]
        raise ValueError("Objects not found")

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
                    if len(self._data[key]) == 0 and key in self.required_objects:
                        raise ValueError('{} is not valid.'.format(key))
                    if key in self.unique_objects and len(self._data[key]) > 1:
                        raise ValueError('{} is not unique: {}'.format(key,
                                                                       len(self._data[key])))
                    for obj in self._data[key]:
                        obj.check(strict=True)

            for key in self._data:
                if len(self._data[key]) > 0:
                    for dobj in self._data[key]:
                        if dobj.schema['format'] == "singleline":
                            vals = [dobj.schema['name']]
                            vals += [v[1] for v in dobj.export()]
                            f.write("\n  {};\n".format(",".join(vals)))
                        elif dobj.schema['format'] == "vertices":
                            f.write("\n  {},\n".format(dobj.schema['name']))
                            vals = dobj.export()
                            cval = len(vals)
                            i = 0
                            while i < cval:

                                if ((i + 2) < cval and "x" in vals[i][0].lower() and 
                                    "y" in vals[i + 1][0].lower() and "z" in vals[i + 2][0].lower()):
                                    val = ",".join([vals[i][1], vals[i + 1][1], vals[i + 2][1]])
                                    comment = ",".join([vals[i][0], vals[i + 1][0], vals[i + 2][0]])
                                    i += 3
                                else: 
                                    val = vals[i][1]
                                    comment = vals[i][0]
                                    i += 1

                                sep = ','
                                if i >= cval:
                                    sep = ';'
                                blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                   sep=sep,
                                                                                   blanks=blanks,
                                                                                   comment=comment))
                        elif dobj.schema['format'] == "compactschedule":
                            f.write("\n  {},\n".format(dobj.schema['name']))
                            vals = dobj.export()
                            cval = len(vals)
                            i = 0
                            while i < cval:

                                if "until" in vals[i][1].lower():
                                    j = i + 1
                                    while j < cval:
                                        jval = vals[j][1].lower()
                                        if "for" in jval or "until" in jval:
                                            break
                                        j += 1
                                    val = ",".join([vals[i][1]] + [vals[t][1] for t in range(i + 1, j) ])
                                    comment = " Fields {} - {}".format(i + 1, j + 1)
                                    i += (j - i)
                                else: 
                                    val = vals[i][1]
                                    comment = vals[i][0]
                                    i += 1

                                sep = ','
                                if i >= cval:
                                    sep = ';'
                                blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                   sep=sep,
                                                                                   blanks=blanks,
                                                                                   comment=comment))
                        elif dobj.schema['format'] == "fluidproperty":

                            f.write("\n  {},\n".format(dobj.schema['name']))
                            vals = dobj.export()
                            cval = len(vals)
                            i = 0
                            while i < cval:

                                is_fluidprops = True
                                for j in range(min(7, cval - i)):

                                    # Test the next values
                                    fluidprops_match = re.search(r"([0-9]|value|property)", vals[i + j][0])
                                    if fluidprops_match is None:
                                        is_fluidprops = False
                                        break

                                if  is_fluidprops:                                    
                                    val = ",".join([vals[i + j][1] for j in range(min(7, cval - i))])
                                    comment = ""
                                    i += min(7, cval - i)
                                else:
                                    val = vals[i][1]
                                    comment = vals[i][0]
                                    i += 1

                                sep = ','
                                if i >= cval:
                                    sep = ';'
                                blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                   sep=sep,
                                                                                   blanks=blanks,
                                                                                   comment=comment))
                        elif dobj.schema['format'] == "spectral":
                            f.write("\n  {},\n".format(dobj.schema['name']))
                            vals = dobj.export()
                            cval = len(vals)
                            i = 0
                            while i < cval:

                                start = i
                                end = min(i + 4, cval)

                                if False not in ["name" not in jval[0].lower() for jval in vals[start:end]]:
                                    val = ",".join([vals[j][1] for j in range(start, end) ])
                                    i += (end - start)
                                    comment = ""
                                else: 
                                    val = vals[i][1]
                                    comment = vals[i][0]
                                    i += 1

                                sep = ','
                                if i >= cval:
                                    sep = ';'
                                blanks = ' ' * max(30 - 4 - len(val) - 2, 2)

                                f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val,
                                                                                   sep=sep,
                                                                                   blanks=blanks,
                                                                                   comment=comment))

                        else:
                            f.write("\n  {},\n".format(dobj.schema['name']))
                            vals = dobj.export()
                            cval = len(vals)
                            for i, val in enumerate(vals):

                                sep = ','
                                if i == (cval - 1):
                                    sep = ';'
                                blanks = ' ' * max(30 - 4 - len(val[1]) - 2, 2)
                                comment = val[0]

                                f.write("    {val}{sep}{blanks}!- {comment}\n".format(val=val[1],
                                                                                   sep=sep,
                                                                                   blanks=blanks,
                                                                                   comment=comment))

    def read(self, path):
        """Read IDF data from path

           Args:
               path (str): path to read data from
        """
        with open(path, "r") as f:
            current_object = None
            current_vals = []

            # First lines are header comments
            header = True

            for line in f:

                line = line.strip()
                if re.search(r"^\s*!", line) is not None:
                    if header:
                        self.comment_headers.append(line)
                    continue
                if len(line) == 0:
                    continue

                header = False

                line_comments = line.split("!")
                line_match = re.search(r"\s*([\S ]*[,;])\s*", line_comments[0])
                if line_match is None:
                    print "Not matched: ", line
                    continue
                else:
                    line = line_match.group(1)

                splits = line.split(";")

                for i, split in enumerate(splits):

                    split = split.strip()
                    if len(split) > 0 and split[-1] == ',':
                        split = split[:-1]

                    splitvals = split.split(",")
                    
                    if i > 1 and len(split) == 0:
                        continue

                    for j, val in enumerate(splitvals):

                        val = val.strip()

                        if j == len(splitvals) and len(val) == 0:
                            continue

                        if val == '' and current_object is None:
                            continue

                        if current_object is None:
                            current_object = val.lower()
                        else:
                            current_vals.append(val)

                    if len(splits) > 1 and current_object is not None:

                        if current_object not in self._data:
                            logging.error("{} is not a valid data dictionary name".format(current_object))

                        else:
                            data_object = self._create_datadict(current_object)
                            data_object.read(current_vals)
                            self._data[current_object].append(data_object)

                        current_object = None
                        current_vals = []
    @property
    def lead_inputs(self):
        """ Get list of all `LeadInput` objects
        """
        return self._data["leadinput"]
    @property
    def simulation_datas(self):
        """ Get list of all `SimulationData` objects
        """
        return self._data["simulationdata"]
    @property
    def versions(self):
        """ Get list of all `Version` objects
        """
        return self._data["version"]
    @property
    def simulationcontrols(self):
        """ Get list of all `SimulationControl` objects
        """
        return self._data["simulationcontrol"]
    @property
    def buildings(self):
        """ Get list of all `Building` objects
        """
        return self._data["building"]
    @property
    def shadowcalculations(self):
        """ Get list of all `ShadowCalculation` objects
        """
        return self._data["shadowcalculation"]
    @property
    def surfaceconvectionalgorithminsides(self):
        """ Get list of all `SurfaceConvectionAlgorithmInside` objects
        """
        return self._data["surfaceconvectionalgorithminside"]
    @property
    def surfaceconvectionalgorithmoutsides(self):
        """ Get list of all `SurfaceConvectionAlgorithmOutside` objects
        """
        return self._data["surfaceconvectionalgorithmoutside"]
    @property
    def heatbalancealgorithms(self):
        """ Get list of all `HeatBalanceAlgorithm` objects
        """
        return self._data["heatbalancealgorithm"]
    @property
    def heatbalancesettingsconductionfinitedifferences(self):
        """ Get list of all `HeatBalanceSettingsConductionFiniteDifference` objects
        """
        return self._data["heatbalancesettingsconductionfinitedifference"]
    @property
    def zoneairheatbalancealgorithms(self):
        """ Get list of all `ZoneAirHeatBalanceAlgorithm` objects
        """
        return self._data["zoneairheatbalancealgorithm"]
    @property
    def zoneaircontaminantbalances(self):
        """ Get list of all `ZoneAirContaminantBalance` objects
        """
        return self._data["zoneaircontaminantbalance"]
    @property
    def zoneairmassflowconservations(self):
        """ Get list of all `ZoneAirMassFlowConservation` objects
        """
        return self._data["zoneairmassflowconservation"]
    @property
    def zonecapacitancemultiplierresearchspecials(self):
        """ Get list of all `ZoneCapacitanceMultiplierResearchSpecial` objects
        """
        return self._data["zonecapacitancemultiplierresearchspecial"]
    @property
    def timesteps(self):
        """ Get list of all `Timestep` objects
        """
        return self._data["timestep"]
    @property
    def convergencelimitss(self):
        """ Get list of all `ConvergenceLimits` objects
        """
        return self._data["convergencelimits"]
    @property
    def programcontrols(self):
        """ Get list of all `ProgramControl` objects
        """
        return self._data["programcontrol"]
    @property
    def compliancebuildings(self):
        """ Get list of all `ComplianceBuilding` objects
        """
        return self._data["compliancebuilding"]
    @property
    def sitelocations(self):
        """ Get list of all `SiteLocation` objects
        """
        return self._data["sitelocation"]
    @property
    def sizingperioddesigndays(self):
        """ Get list of all `SizingPeriodDesignDay` objects
        """
        return self._data["sizingperioddesignday"]
    @property
    def sizingperiodweatherfiledayss(self):
        """ Get list of all `SizingPeriodWeatherFileDays` objects
        """
        return self._data["sizingperiodweatherfiledays"]
    @property
    def sizingperiodweatherfileconditiontypes(self):
        """ Get list of all `SizingPeriodWeatherFileConditionType` objects
        """
        return self._data["sizingperiodweatherfileconditiontype"]
    @property
    def runperiods(self):
        """ Get list of all `RunPeriod` objects
        """
        return self._data["runperiod"]
    @property
    def runperiodcustomranges(self):
        """ Get list of all `RunPeriodCustomRange` objects
        """
        return self._data["runperiodcustomrange"]
    @property
    def runperiodcontrolspecialdayss(self):
        """ Get list of all `RunPeriodControlSpecialDays` objects
        """
        return self._data["runperiodcontrolspecialdays"]
    @property
    def runperiodcontroldaylightsavingtimes(self):
        """ Get list of all `RunPeriodControlDaylightSavingTime` objects
        """
        return self._data["runperiodcontroldaylightsavingtime"]
    @property
    def weatherpropertyskytemperatures(self):
        """ Get list of all `WeatherPropertySkyTemperature` objects
        """
        return self._data["weatherpropertyskytemperature"]
    @property
    def siteweatherstations(self):
        """ Get list of all `SiteWeatherStation` objects
        """
        return self._data["siteweatherstation"]
    @property
    def siteheightvariations(self):
        """ Get list of all `SiteHeightVariation` objects
        """
        return self._data["siteheightvariation"]
    @property
    def sitegroundtemperaturebuildingsurfaces(self):
        """ Get list of all `SiteGroundTemperatureBuildingSurface` objects
        """
        return self._data["sitegroundtemperaturebuildingsurface"]
    @property
    def sitegroundtemperaturefcfactormethods(self):
        """ Get list of all `SiteGroundTemperatureFcfactorMethod` objects
        """
        return self._data["sitegroundtemperaturefcfactormethod"]
    @property
    def sitegroundtemperatureshallows(self):
        """ Get list of all `SiteGroundTemperatureShallow` objects
        """
        return self._data["sitegroundtemperatureshallow"]
    @property
    def sitegroundtemperaturedeeps(self):
        """ Get list of all `SiteGroundTemperatureDeep` objects
        """
        return self._data["sitegroundtemperaturedeep"]
    @property
    def sitegrounddomains(self):
        """ Get list of all `SiteGroundDomain` objects
        """
        return self._data["sitegrounddomain"]
    @property
    def sitegroundreflectances(self):
        """ Get list of all `SiteGroundReflectance` objects
        """
        return self._data["sitegroundreflectance"]
    @property
    def sitegroundreflectancesnowmodifiers(self):
        """ Get list of all `SiteGroundReflectanceSnowModifier` objects
        """
        return self._data["sitegroundreflectancesnowmodifier"]
    @property
    def sitewatermainstemperatures(self):
        """ Get list of all `SiteWaterMainsTemperature` objects
        """
        return self._data["sitewatermainstemperature"]
    @property
    def siteprecipitations(self):
        """ Get list of all `SitePrecipitation` objects
        """
        return self._data["siteprecipitation"]
    @property
    def roofirrigations(self):
        """ Get list of all `RoofIrrigation` objects
        """
        return self._data["roofirrigation"]
    @property
    def sitesolarandvisiblespectrums(self):
        """ Get list of all `SiteSolarAndVisibleSpectrum` objects
        """
        return self._data["sitesolarandvisiblespectrum"]
    @property
    def sitespectrumdatas(self):
        """ Get list of all `SiteSpectrumData` objects
        """
        return self._data["sitespectrumdata"]
    @property
    def scheduletypelimitss(self):
        """ Get list of all `ScheduleTypeLimits` objects
        """
        return self._data["scheduletypelimits"]
    @property
    def scheduledayhourlys(self):
        """ Get list of all `ScheduleDayHourly` objects
        """
        return self._data["scheduledayhourly"]
    @property
    def scheduledayintervals(self):
        """ Get list of all `ScheduleDayInterval` objects
        """
        return self._data["scheduledayinterval"]
    @property
    def scheduledaylists(self):
        """ Get list of all `ScheduleDayList` objects
        """
        return self._data["scheduledaylist"]
    @property
    def scheduleweekdailys(self):
        """ Get list of all `ScheduleWeekDaily` objects
        """
        return self._data["scheduleweekdaily"]
    @property
    def scheduleweekcompacts(self):
        """ Get list of all `ScheduleWeekCompact` objects
        """
        return self._data["scheduleweekcompact"]
    @property
    def scheduleyears(self):
        """ Get list of all `ScheduleYear` objects
        """
        return self._data["scheduleyear"]
    @property
    def schedulecompacts(self):
        """ Get list of all `ScheduleCompact` objects
        """
        return self._data["schedulecompact"]
    @property
    def scheduleconstants(self):
        """ Get list of all `ScheduleConstant` objects
        """
        return self._data["scheduleconstant"]
    @property
    def schedulefiles(self):
        """ Get list of all `ScheduleFile` objects
        """
        return self._data["schedulefile"]
    @property
    def materials(self):
        """ Get list of all `Material` objects
        """
        return self._data["material"]
    @property
    def materialnomasss(self):
        """ Get list of all `MaterialNoMass` objects
        """
        return self._data["materialnomass"]
    @property
    def materialinfraredtransparents(self):
        """ Get list of all `MaterialInfraredTransparent` objects
        """
        return self._data["materialinfraredtransparent"]
    @property
    def materialairgaps(self):
        """ Get list of all `MaterialAirGap` objects
        """
        return self._data["materialairgap"]
    @property
    def materialroofvegetations(self):
        """ Get list of all `MaterialRoofVegetation` objects
        """
        return self._data["materialroofvegetation"]
    @property
    def windowmaterialsimpleglazingsystems(self):
        """ Get list of all `WindowMaterialSimpleGlazingSystem` objects
        """
        return self._data["windowmaterialsimpleglazingsystem"]
    @property
    def windowmaterialglazings(self):
        """ Get list of all `WindowMaterialGlazing` objects
        """
        return self._data["windowmaterialglazing"]
    @property
    def windowmaterialglazinggroupthermochromics(self):
        """ Get list of all `WindowMaterialGlazingGroupThermochromic` objects
        """
        return self._data["windowmaterialglazinggroupthermochromic"]
    @property
    def windowmaterialglazingrefractionextinctionmethods(self):
        """ Get list of all `WindowMaterialGlazingRefractionExtinctionMethod` objects
        """
        return self._data["windowmaterialglazingrefractionextinctionmethod"]
    @property
    def windowmaterialgass(self):
        """ Get list of all `WindowMaterialGas` objects
        """
        return self._data["windowmaterialgas"]
    @property
    def windowgapsupportpillars(self):
        """ Get list of all `WindowGapSupportPillar` objects
        """
        return self._data["windowgapsupportpillar"]
    @property
    def windowgapdeflectionstates(self):
        """ Get list of all `WindowGapDeflectionState` objects
        """
        return self._data["windowgapdeflectionstate"]
    @property
    def windowmaterialgasmixtures(self):
        """ Get list of all `WindowMaterialGasMixture` objects
        """
        return self._data["windowmaterialgasmixture"]
    @property
    def windowmaterialgaps(self):
        """ Get list of all `WindowMaterialGap` objects
        """
        return self._data["windowmaterialgap"]
    @property
    def windowmaterialshades(self):
        """ Get list of all `WindowMaterialShade` objects
        """
        return self._data["windowmaterialshade"]
    @property
    def windowmaterialcomplexshades(self):
        """ Get list of all `WindowMaterialComplexShade` objects
        """
        return self._data["windowmaterialcomplexshade"]
    @property
    def windowmaterialblinds(self):
        """ Get list of all `WindowMaterialBlind` objects
        """
        return self._data["windowmaterialblind"]
    @property
    def windowmaterialscreens(self):
        """ Get list of all `WindowMaterialScreen` objects
        """
        return self._data["windowmaterialscreen"]
    @property
    def windowmaterialshadeequivalentlayers(self):
        """ Get list of all `WindowMaterialShadeEquivalentLayer` objects
        """
        return self._data["windowmaterialshadeequivalentlayer"]
    @property
    def windowmaterialdrapeequivalentlayers(self):
        """ Get list of all `WindowMaterialDrapeEquivalentLayer` objects
        """
        return self._data["windowmaterialdrapeequivalentlayer"]
    @property
    def windowmaterialblindequivalentlayers(self):
        """ Get list of all `WindowMaterialBlindEquivalentLayer` objects
        """
        return self._data["windowmaterialblindequivalentlayer"]
    @property
    def windowmaterialscreenequivalentlayers(self):
        """ Get list of all `WindowMaterialScreenEquivalentLayer` objects
        """
        return self._data["windowmaterialscreenequivalentlayer"]
    @property
    def windowmaterialglazingequivalentlayers(self):
        """ Get list of all `WindowMaterialGlazingEquivalentLayer` objects
        """
        return self._data["windowmaterialglazingequivalentlayer"]
    @property
    def constructionwindowequivalentlayers(self):
        """ Get list of all `ConstructionWindowEquivalentLayer` objects
        """
        return self._data["constructionwindowequivalentlayer"]
    @property
    def windowmaterialgapequivalentlayers(self):
        """ Get list of all `WindowMaterialGapEquivalentLayer` objects
        """
        return self._data["windowmaterialgapequivalentlayer"]
    @property
    def materialpropertymoisturepenetrationdepthsettingss(self):
        """ Get list of all `MaterialPropertyMoisturePenetrationDepthSettings` objects
        """
        return self._data["materialpropertymoisturepenetrationdepthsettings"]
    @property
    def materialpropertyphasechanges(self):
        """ Get list of all `MaterialPropertyPhaseChange` objects
        """
        return self._data["materialpropertyphasechange"]
    @property
    def materialpropertyvariablethermalconductivitys(self):
        """ Get list of all `MaterialPropertyVariableThermalConductivity` objects
        """
        return self._data["materialpropertyvariablethermalconductivity"]
    @property
    def materialpropertyheatandmoisturetransfersettingss(self):
        """ Get list of all `MaterialPropertyHeatAndMoistureTransferSettings` objects
        """
        return self._data["materialpropertyheatandmoisturetransfersettings"]
    @property
    def materialpropertyheatandmoisturetransfersorptionisotherms(self):
        """ Get list of all `MaterialPropertyHeatAndMoistureTransferSorptionIsotherm` objects
        """
        return self._data["materialpropertyheatandmoisturetransfersorptionisotherm"]
    @property
    def materialpropertyheatandmoisturetransfersuctions(self):
        """ Get list of all `MaterialPropertyHeatAndMoistureTransferSuction` objects
        """
        return self._data["materialpropertyheatandmoisturetransfersuction"]
    @property
    def materialpropertyheatandmoisturetransferredistributions(self):
        """ Get list of all `MaterialPropertyHeatAndMoistureTransferRedistribution` objects
        """
        return self._data["materialpropertyheatandmoisturetransferredistribution"]
    @property
    def materialpropertyheatandmoisturetransferdiffusions(self):
        """ Get list of all `MaterialPropertyHeatAndMoistureTransferDiffusion` objects
        """
        return self._data["materialpropertyheatandmoisturetransferdiffusion"]
    @property
    def materialpropertyheatandmoisturetransferthermalconductivitys(self):
        """ Get list of all `MaterialPropertyHeatAndMoistureTransferThermalConductivity` objects
        """
        return self._data["materialpropertyheatandmoisturetransferthermalconductivity"]
    @property
    def materialpropertyglazingspectraldatas(self):
        """ Get list of all `MaterialPropertyGlazingSpectralData` objects
        """
        return self._data["materialpropertyglazingspectraldata"]
    @property
    def constructions(self):
        """ Get list of all `Construction` objects
        """
        return self._data["construction"]
    @property
    def constructioncfactorundergroundwalls(self):
        """ Get list of all `ConstructionCfactorUndergroundWall` objects
        """
        return self._data["constructioncfactorundergroundwall"]
    @property
    def constructionffactorgroundfloors(self):
        """ Get list of all `ConstructionFfactorGroundFloor` objects
        """
        return self._data["constructionffactorgroundfloor"]
    @property
    def constructioninternalsources(self):
        """ Get list of all `ConstructionInternalSource` objects
        """
        return self._data["constructioninternalsource"]
    @property
    def windowthermalmodelparamss(self):
        """ Get list of all `WindowThermalModelParams` objects
        """
        return self._data["windowthermalmodelparams"]
    @property
    def constructioncomplexfenestrationstates(self):
        """ Get list of all `ConstructionComplexFenestrationState` objects
        """
        return self._data["constructioncomplexfenestrationstate"]
    @property
    def constructionwindowdatafiles(self):
        """ Get list of all `ConstructionWindowDataFile` objects
        """
        return self._data["constructionwindowdatafile"]
    @property
    def globalgeometryruless(self):
        """ Get list of all `GlobalGeometryRules` objects
        """
        return self._data["globalgeometryrules"]
    @property
    def geometrytransforms(self):
        """ Get list of all `GeometryTransform` objects
        """
        return self._data["geometrytransform"]
    @property
    def zones(self):
        """ Get list of all `Zone` objects
        """
        return self._data["zone"]
    @property
    def zonelists(self):
        """ Get list of all `ZoneList` objects
        """
        return self._data["zonelist"]
    @property
    def zonegroups(self):
        """ Get list of all `ZoneGroup` objects
        """
        return self._data["zonegroup"]
    @property
    def buildingsurfacedetaileds(self):
        """ Get list of all `BuildingSurfaceDetailed` objects
        """
        return self._data["buildingsurfacedetailed"]
    @property
    def walldetaileds(self):
        """ Get list of all `WallDetailed` objects
        """
        return self._data["walldetailed"]
    @property
    def roofceilingdetaileds(self):
        """ Get list of all `RoofCeilingDetailed` objects
        """
        return self._data["roofceilingdetailed"]
    @property
    def floordetaileds(self):
        """ Get list of all `FloorDetailed` objects
        """
        return self._data["floordetailed"]
    @property
    def wallexteriors(self):
        """ Get list of all `WallExterior` objects
        """
        return self._data["wallexterior"]
    @property
    def walladiabatics(self):
        """ Get list of all `WallAdiabatic` objects
        """
        return self._data["walladiabatic"]
    @property
    def wallundergrounds(self):
        """ Get list of all `WallUnderground` objects
        """
        return self._data["wallunderground"]
    @property
    def wallinterzones(self):
        """ Get list of all `WallInterzone` objects
        """
        return self._data["wallinterzone"]
    @property
    def roofs(self):
        """ Get list of all `Roof` objects
        """
        return self._data["roof"]
    @property
    def ceilingadiabatics(self):
        """ Get list of all `CeilingAdiabatic` objects
        """
        return self._data["ceilingadiabatic"]
    @property
    def ceilinginterzones(self):
        """ Get list of all `CeilingInterzone` objects
        """
        return self._data["ceilinginterzone"]
    @property
    def floorgroundcontacts(self):
        """ Get list of all `FloorGroundContact` objects
        """
        return self._data["floorgroundcontact"]
    @property
    def flooradiabatics(self):
        """ Get list of all `FloorAdiabatic` objects
        """
        return self._data["flooradiabatic"]
    @property
    def floorinterzones(self):
        """ Get list of all `FloorInterzone` objects
        """
        return self._data["floorinterzone"]
    @property
    def fenestrationsurfacedetaileds(self):
        """ Get list of all `FenestrationSurfaceDetailed` objects
        """
        return self._data["fenestrationsurfacedetailed"]
    @property
    def windows(self):
        """ Get list of all `Window` objects
        """
        return self._data["window"]
    @property
    def doors(self):
        """ Get list of all `Door` objects
        """
        return self._data["door"]
    @property
    def glazeddoors(self):
        """ Get list of all `GlazedDoor` objects
        """
        return self._data["glazeddoor"]
    @property
    def windowinterzones(self):
        """ Get list of all `WindowInterzone` objects
        """
        return self._data["windowinterzone"]
    @property
    def doorinterzones(self):
        """ Get list of all `DoorInterzone` objects
        """
        return self._data["doorinterzone"]
    @property
    def glazeddoorinterzones(self):
        """ Get list of all `GlazedDoorInterzone` objects
        """
        return self._data["glazeddoorinterzone"]
    @property
    def windowpropertyshadingcontrols(self):
        """ Get list of all `WindowPropertyShadingControl` objects
        """
        return self._data["windowpropertyshadingcontrol"]
    @property
    def windowpropertyframeanddividers(self):
        """ Get list of all `WindowPropertyFrameAndDivider` objects
        """
        return self._data["windowpropertyframeanddivider"]
    @property
    def windowpropertyairflowcontrols(self):
        """ Get list of all `WindowPropertyAirflowControl` objects
        """
        return self._data["windowpropertyairflowcontrol"]
    @property
    def windowpropertystormwindows(self):
        """ Get list of all `WindowPropertyStormWindow` objects
        """
        return self._data["windowpropertystormwindow"]
    @property
    def internalmasss(self):
        """ Get list of all `InternalMass` objects
        """
        return self._data["internalmass"]
    @property
    def shadingsites(self):
        """ Get list of all `ShadingSite` objects
        """
        return self._data["shadingsite"]
    @property
    def shadingbuildings(self):
        """ Get list of all `ShadingBuilding` objects
        """
        return self._data["shadingbuilding"]
    @property
    def shadingsitedetaileds(self):
        """ Get list of all `ShadingSiteDetailed` objects
        """
        return self._data["shadingsitedetailed"]
    @property
    def shadingbuildingdetaileds(self):
        """ Get list of all `ShadingBuildingDetailed` objects
        """
        return self._data["shadingbuildingdetailed"]
    @property
    def shadingoverhangs(self):
        """ Get list of all `ShadingOverhang` objects
        """
        return self._data["shadingoverhang"]
    @property
    def shadingoverhangprojections(self):
        """ Get list of all `ShadingOverhangProjection` objects
        """
        return self._data["shadingoverhangprojection"]
    @property
    def shadingfins(self):
        """ Get list of all `ShadingFin` objects
        """
        return self._data["shadingfin"]
    @property
    def shadingfinprojections(self):
        """ Get list of all `ShadingFinProjection` objects
        """
        return self._data["shadingfinprojection"]
    @property
    def shadingzonedetaileds(self):
        """ Get list of all `ShadingZoneDetailed` objects
        """
        return self._data["shadingzonedetailed"]
    @property
    def shadingpropertyreflectances(self):
        """ Get list of all `ShadingPropertyReflectance` objects
        """
        return self._data["shadingpropertyreflectance"]
    @property
    def surfacepropertyheattransferalgorithms(self):
        """ Get list of all `SurfacePropertyHeatTransferAlgorithm` objects
        """
        return self._data["surfacepropertyheattransferalgorithm"]
    @property
    def surfacepropertyheattransferalgorithmmultiplesurfaces(self):
        """ Get list of all `SurfacePropertyHeatTransferAlgorithmMultipleSurface` objects
        """
        return self._data["surfacepropertyheattransferalgorithmmultiplesurface"]
    @property
    def surfacepropertyheattransferalgorithmsurfacelists(self):
        """ Get list of all `SurfacePropertyHeatTransferAlgorithmSurfaceList` objects
        """
        return self._data["surfacepropertyheattransferalgorithmsurfacelist"]
    @property
    def surfacepropertyheattransferalgorithmconstructions(self):
        """ Get list of all `SurfacePropertyHeatTransferAlgorithmConstruction` objects
        """
        return self._data["surfacepropertyheattransferalgorithmconstruction"]
    @property
    def surfacecontrolmovableinsulations(self):
        """ Get list of all `SurfaceControlMovableInsulation` objects
        """
        return self._data["surfacecontrolmovableinsulation"]
    @property
    def surfacepropertyothersidecoefficientss(self):
        """ Get list of all `SurfacePropertyOtherSideCoefficients` objects
        """
        return self._data["surfacepropertyothersidecoefficients"]
    @property
    def surfacepropertyothersideconditionsmodels(self):
        """ Get list of all `SurfacePropertyOtherSideConditionsModel` objects
        """
        return self._data["surfacepropertyothersideconditionsmodel"]
    @property
    def surfaceconvectionalgorithminsideadaptivemodelselectionss(self):
        """ Get list of all `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections` objects
        """
        return self._data["surfaceconvectionalgorithminsideadaptivemodelselections"]
    @property
    def surfaceconvectionalgorithmoutsideadaptivemodelselectionss(self):
        """ Get list of all `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections` objects
        """
        return self._data["surfaceconvectionalgorithmoutsideadaptivemodelselections"]
    @property
    def surfaceconvectionalgorithminsideusercurves(self):
        """ Get list of all `SurfaceConvectionAlgorithmInsideUserCurve` objects
        """
        return self._data["surfaceconvectionalgorithminsideusercurve"]
    @property
    def surfaceconvectionalgorithmoutsideusercurves(self):
        """ Get list of all `SurfaceConvectionAlgorithmOutsideUserCurve` objects
        """
        return self._data["surfaceconvectionalgorithmoutsideusercurve"]
    @property
    def surfacepropertyconvectioncoefficientss(self):
        """ Get list of all `SurfacePropertyConvectionCoefficients` objects
        """
        return self._data["surfacepropertyconvectioncoefficients"]
    @property
    def surfacepropertyconvectioncoefficientsmultiplesurfaces(self):
        """ Get list of all `SurfacePropertyConvectionCoefficientsMultipleSurface` objects
        """
        return self._data["surfacepropertyconvectioncoefficientsmultiplesurface"]
    @property
    def surfacepropertiesvaporcoefficientss(self):
        """ Get list of all `SurfacePropertiesVaporCoefficients` objects
        """
        return self._data["surfacepropertiesvaporcoefficients"]
    @property
    def surfacepropertyexteriornaturalventedcavitys(self):
        """ Get list of all `SurfacePropertyExteriorNaturalVentedCavity` objects
        """
        return self._data["surfacepropertyexteriornaturalventedcavity"]
    @property
    def surfacepropertysolarincidentinsides(self):
        """ Get list of all `SurfacePropertySolarIncidentInside` objects
        """
        return self._data["surfacepropertysolarincidentinside"]
    @property
    def complexfenestrationpropertysolarabsorbedlayerss(self):
        """ Get list of all `ComplexFenestrationPropertySolarAbsorbedLayers` objects
        """
        return self._data["complexfenestrationpropertysolarabsorbedlayers"]
    @property
    def zonepropertyuserviewfactorsbysurfacenames(self):
        """ Get list of all `ZonePropertyUserViewFactorsBySurfaceName` objects
        """
        return self._data["zonepropertyuserviewfactorsbysurfacename"]
    @property
    def groundheattransfercontrols(self):
        """ Get list of all `GroundHeatTransferControl` objects
        """
        return self._data["groundheattransfercontrol"]
    @property
    def groundheattransferslabmaterialss(self):
        """ Get list of all `GroundHeatTransferSlabMaterials` objects
        """
        return self._data["groundheattransferslabmaterials"]
    @property
    def groundheattransferslabmatlpropss(self):
        """ Get list of all `GroundHeatTransferSlabMatlProps` objects
        """
        return self._data["groundheattransferslabmatlprops"]
    @property
    def groundheattransferslabboundcondss(self):
        """ Get list of all `GroundHeatTransferSlabBoundConds` objects
        """
        return self._data["groundheattransferslabboundconds"]
    @property
    def groundheattransferslabbldgpropss(self):
        """ Get list of all `GroundHeatTransferSlabBldgProps` objects
        """
        return self._data["groundheattransferslabbldgprops"]
    @property
    def groundheattransferslabinsulations(self):
        """ Get list of all `GroundHeatTransferSlabInsulation` objects
        """
        return self._data["groundheattransferslabinsulation"]
    @property
    def groundheattransferslabequivalentslabs(self):
        """ Get list of all `GroundHeatTransferSlabEquivalentSlab` objects
        """
        return self._data["groundheattransferslabequivalentslab"]
    @property
    def groundheattransferslabautogrids(self):
        """ Get list of all `GroundHeatTransferSlabAutoGrid` objects
        """
        return self._data["groundheattransferslabautogrid"]
    @property
    def groundheattransferslabmanualgrids(self):
        """ Get list of all `GroundHeatTransferSlabManualGrid` objects
        """
        return self._data["groundheattransferslabmanualgrid"]
    @property
    def groundheattransferslabxfaces(self):
        """ Get list of all `GroundHeatTransferSlabXface` objects
        """
        return self._data["groundheattransferslabxface"]
    @property
    def groundheattransferslabyfaces(self):
        """ Get list of all `GroundHeatTransferSlabYface` objects
        """
        return self._data["groundheattransferslabyface"]
    @property
    def groundheattransferslabzfaces(self):
        """ Get list of all `GroundHeatTransferSlabZface` objects
        """
        return self._data["groundheattransferslabzface"]
    @property
    def groundheattransferbasementsimparameterss(self):
        """ Get list of all `GroundHeatTransferBasementSimParameters` objects
        """
        return self._data["groundheattransferbasementsimparameters"]
    @property
    def groundheattransferbasementmatlpropss(self):
        """ Get list of all `GroundHeatTransferBasementMatlProps` objects
        """
        return self._data["groundheattransferbasementmatlprops"]
    @property
    def groundheattransferbasementinsulations(self):
        """ Get list of all `GroundHeatTransferBasementInsulation` objects
        """
        return self._data["groundheattransferbasementinsulation"]
    @property
    def groundheattransferbasementsurfacepropss(self):
        """ Get list of all `GroundHeatTransferBasementSurfaceProps` objects
        """
        return self._data["groundheattransferbasementsurfaceprops"]
    @property
    def groundheattransferbasementbldgdatas(self):
        """ Get list of all `GroundHeatTransferBasementBldgData` objects
        """
        return self._data["groundheattransferbasementbldgdata"]
    @property
    def groundheattransferbasementinteriors(self):
        """ Get list of all `GroundHeatTransferBasementInterior` objects
        """
        return self._data["groundheattransferbasementinterior"]
    @property
    def groundheattransferbasementcombldgs(self):
        """ Get list of all `GroundHeatTransferBasementComBldg` objects
        """
        return self._data["groundheattransferbasementcombldg"]
    @property
    def groundheattransferbasementequivslabs(self):
        """ Get list of all `GroundHeatTransferBasementEquivSlab` objects
        """
        return self._data["groundheattransferbasementequivslab"]
    @property
    def groundheattransferbasementequivautogrids(self):
        """ Get list of all `GroundHeatTransferBasementEquivAutoGrid` objects
        """
        return self._data["groundheattransferbasementequivautogrid"]
    @property
    def groundheattransferbasementautogrids(self):
        """ Get list of all `GroundHeatTransferBasementAutoGrid` objects
        """
        return self._data["groundheattransferbasementautogrid"]
    @property
    def groundheattransferbasementmanualgrids(self):
        """ Get list of all `GroundHeatTransferBasementManualGrid` objects
        """
        return self._data["groundheattransferbasementmanualgrid"]
    @property
    def groundheattransferbasementxfaces(self):
        """ Get list of all `GroundHeatTransferBasementXface` objects
        """
        return self._data["groundheattransferbasementxface"]
    @property
    def groundheattransferbasementyfaces(self):
        """ Get list of all `GroundHeatTransferBasementYface` objects
        """
        return self._data["groundheattransferbasementyface"]
    @property
    def groundheattransferbasementzfaces(self):
        """ Get list of all `GroundHeatTransferBasementZface` objects
        """
        return self._data["groundheattransferbasementzface"]
    @property
    def roomairmodeltypes(self):
        """ Get list of all `RoomAirModelType` objects
        """
        return self._data["roomairmodeltype"]
    @property
    def roomairtemperaturepatternuserdefineds(self):
        """ Get list of all `RoomAirTemperaturePatternUserDefined` objects
        """
        return self._data["roomairtemperaturepatternuserdefined"]
    @property
    def roomairtemperaturepatternconstantgradients(self):
        """ Get list of all `RoomAirTemperaturePatternConstantGradient` objects
        """
        return self._data["roomairtemperaturepatternconstantgradient"]
    @property
    def roomairtemperaturepatterntwogradients(self):
        """ Get list of all `RoomAirTemperaturePatternTwoGradient` objects
        """
        return self._data["roomairtemperaturepatterntwogradient"]
    @property
    def roomairtemperaturepatternnondimensionalheights(self):
        """ Get list of all `RoomAirTemperaturePatternNondimensionalHeight` objects
        """
        return self._data["roomairtemperaturepatternnondimensionalheight"]
    @property
    def roomairtemperaturepatternsurfacemappings(self):
        """ Get list of all `RoomAirTemperaturePatternSurfaceMapping` objects
        """
        return self._data["roomairtemperaturepatternsurfacemapping"]
    @property
    def roomairnodes(self):
        """ Get list of all `RoomAirNode` objects
        """
        return self._data["roomairnode"]
    @property
    def roomairsettingsonenodedisplacementventilations(self):
        """ Get list of all `RoomAirSettingsOneNodeDisplacementVentilation` objects
        """
        return self._data["roomairsettingsonenodedisplacementventilation"]
    @property
    def roomairsettingsthreenodedisplacementventilations(self):
        """ Get list of all `RoomAirSettingsThreeNodeDisplacementVentilation` objects
        """
        return self._data["roomairsettingsthreenodedisplacementventilation"]
    @property
    def roomairsettingscrossventilations(self):
        """ Get list of all `RoomAirSettingsCrossVentilation` objects
        """
        return self._data["roomairsettingscrossventilation"]
    @property
    def roomairsettingsunderfloorairdistributioninteriors(self):
        """ Get list of all `RoomAirSettingsUnderFloorAirDistributionInterior` objects
        """
        return self._data["roomairsettingsunderfloorairdistributioninterior"]
    @property
    def roomairsettingsunderfloorairdistributionexteriors(self):
        """ Get list of all `RoomAirSettingsUnderFloorAirDistributionExterior` objects
        """
        return self._data["roomairsettingsunderfloorairdistributionexterior"]
    @property
    def peoples(self):
        """ Get list of all `People` objects
        """
        return self._data["people"]
    @property
    def comfortviewfactorangless(self):
        """ Get list of all `ComfortViewFactorAngles` objects
        """
        return self._data["comfortviewfactorangles"]
    @property
    def lightss(self):
        """ Get list of all `Lights` objects
        """
        return self._data["lights"]
    @property
    def electricequipments(self):
        """ Get list of all `ElectricEquipment` objects
        """
        return self._data["electricequipment"]
    @property
    def gasequipments(self):
        """ Get list of all `GasEquipment` objects
        """
        return self._data["gasequipment"]
    @property
    def hotwaterequipments(self):
        """ Get list of all `HotWaterEquipment` objects
        """
        return self._data["hotwaterequipment"]
    @property
    def steamequipments(self):
        """ Get list of all `SteamEquipment` objects
        """
        return self._data["steamequipment"]
    @property
    def otherequipments(self):
        """ Get list of all `OtherEquipment` objects
        """
        return self._data["otherequipment"]
    @property
    def zonebaseboardoutdoortemperaturecontrolleds(self):
        """ Get list of all `ZoneBaseboardOutdoorTemperatureControlled` objects
        """
        return self._data["zonebaseboardoutdoortemperaturecontrolled"]
    @property
    def zonecontaminantsourceandsinkcarbondioxides(self):
        """ Get list of all `ZoneContaminantSourceAndSinkCarbonDioxide` objects
        """
        return self._data["zonecontaminantsourceandsinkcarbondioxide"]
    @property
    def zonecontaminantsourceandsinkgenericconstants(self):
        """ Get list of all `ZoneContaminantSourceAndSinkGenericConstant` objects
        """
        return self._data["zonecontaminantsourceandsinkgenericconstant"]
    @property
    def surfacecontaminantsourceandsinkgenericpressuredrivens(self):
        """ Get list of all `SurfaceContaminantSourceAndSinkGenericPressureDriven` objects
        """
        return self._data["surfacecontaminantsourceandsinkgenericpressuredriven"]
    @property
    def zonecontaminantsourceandsinkgenericcutoffmodels(self):
        """ Get list of all `ZoneContaminantSourceAndSinkGenericCutoffModel` objects
        """
        return self._data["zonecontaminantsourceandsinkgenericcutoffmodel"]
    @property
    def zonecontaminantsourceandsinkgenericdecaysources(self):
        """ Get list of all `ZoneContaminantSourceAndSinkGenericDecaySource` objects
        """
        return self._data["zonecontaminantsourceandsinkgenericdecaysource"]
    @property
    def surfacecontaminantsourceandsinkgenericboundarylayerdiffusions(self):
        """ Get list of all `SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion` objects
        """
        return self._data["surfacecontaminantsourceandsinkgenericboundarylayerdiffusion"]
    @property
    def surfacecontaminantsourceandsinkgenericdepositionvelocitysinks(self):
        """ Get list of all `SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink` objects
        """
        return self._data["surfacecontaminantsourceandsinkgenericdepositionvelocitysink"]
    @property
    def zonecontaminantsourceandsinkgenericdepositionratesinks(self):
        """ Get list of all `ZoneContaminantSourceAndSinkGenericDepositionRateSink` objects
        """
        return self._data["zonecontaminantsourceandsinkgenericdepositionratesink"]
    @property
    def daylightingcontrolss(self):
        """ Get list of all `DaylightingControls` objects
        """
        return self._data["daylightingcontrols"]
    @property
    def daylightingdelightcontrolss(self):
        """ Get list of all `DaylightingDelightControls` objects
        """
        return self._data["daylightingdelightcontrols"]
    @property
    def daylightingdelightreferencepoints(self):
        """ Get list of all `DaylightingDelightReferencePoint` objects
        """
        return self._data["daylightingdelightreferencepoint"]
    @property
    def daylightingdelightcomplexfenestrations(self):
        """ Get list of all `DaylightingDelightComplexFenestration` objects
        """
        return self._data["daylightingdelightcomplexfenestration"]
    @property
    def daylightingdevicetubulars(self):
        """ Get list of all `DaylightingDeviceTubular` objects
        """
        return self._data["daylightingdevicetubular"]
    @property
    def daylightingdeviceshelfs(self):
        """ Get list of all `DaylightingDeviceShelf` objects
        """
        return self._data["daylightingdeviceshelf"]
    @property
    def daylightingdevicelightwells(self):
        """ Get list of all `DaylightingDeviceLightWell` objects
        """
        return self._data["daylightingdevicelightwell"]
    @property
    def outputdaylightfactorss(self):
        """ Get list of all `OutputDaylightFactors` objects
        """
        return self._data["outputdaylightfactors"]
    @property
    def outputilluminancemaps(self):
        """ Get list of all `OutputIlluminanceMap` objects
        """
        return self._data["outputilluminancemap"]
    @property
    def outputcontrolilluminancemapstyles(self):
        """ Get list of all `OutputControlIlluminanceMapStyle` objects
        """
        return self._data["outputcontrolilluminancemapstyle"]
    @property
    def zoneinfiltrationdesignflowrates(self):
        """ Get list of all `ZoneInfiltrationDesignFlowRate` objects
        """
        return self._data["zoneinfiltrationdesignflowrate"]
    @property
    def zoneinfiltrationeffectiveleakageareas(self):
        """ Get list of all `ZoneInfiltrationEffectiveLeakageArea` objects
        """
        return self._data["zoneinfiltrationeffectiveleakagearea"]
    @property
    def zoneinfiltrationflowcoefficients(self):
        """ Get list of all `ZoneInfiltrationFlowCoefficient` objects
        """
        return self._data["zoneinfiltrationflowcoefficient"]
    @property
    def zoneventilationdesignflowrates(self):
        """ Get list of all `ZoneVentilationDesignFlowRate` objects
        """
        return self._data["zoneventilationdesignflowrate"]
    @property
    def zoneventilationwindandstackopenareas(self):
        """ Get list of all `ZoneVentilationWindandStackOpenArea` objects
        """
        return self._data["zoneventilationwindandstackopenarea"]
    @property
    def zoneairbalanceoutdoorairs(self):
        """ Get list of all `ZoneAirBalanceOutdoorAir` objects
        """
        return self._data["zoneairbalanceoutdoorair"]
    @property
    def zonemixings(self):
        """ Get list of all `ZoneMixing` objects
        """
        return self._data["zonemixing"]
    @property
    def zonecrossmixings(self):
        """ Get list of all `ZoneCrossMixing` objects
        """
        return self._data["zonecrossmixing"]
    @property
    def zonerefrigerationdoormixings(self):
        """ Get list of all `ZoneRefrigerationDoorMixing` objects
        """
        return self._data["zonerefrigerationdoormixing"]
    @property
    def zoneearthtubes(self):
        """ Get list of all `ZoneEarthtube` objects
        """
        return self._data["zoneearthtube"]
    @property
    def zonecooltowershowers(self):
        """ Get list of all `ZoneCoolTowerShower` objects
        """
        return self._data["zonecooltowershower"]
    @property
    def zonethermalchimneys(self):
        """ Get list of all `ZoneThermalChimney` objects
        """
        return self._data["zonethermalchimney"]
    @property
    def airflownetworksimulationcontrols(self):
        """ Get list of all `AirflowNetworkSimulationControl` objects
        """
        return self._data["airflownetworksimulationcontrol"]
    @property
    def airflownetworkmultizonezones(self):
        """ Get list of all `AirflowNetworkMultiZoneZone` objects
        """
        return self._data["airflownetworkmultizonezone"]
    @property
    def airflownetworkmultizonesurfaces(self):
        """ Get list of all `AirflowNetworkMultiZoneSurface` objects
        """
        return self._data["airflownetworkmultizonesurface"]
    @property
    def airflownetworkmultizonereferencecrackconditionss(self):
        """ Get list of all `AirflowNetworkMultiZoneReferenceCrackConditions` objects
        """
        return self._data["airflownetworkmultizonereferencecrackconditions"]
    @property
    def airflownetworkmultizonesurfacecracks(self):
        """ Get list of all `AirflowNetworkMultiZoneSurfaceCrack` objects
        """
        return self._data["airflownetworkmultizonesurfacecrack"]
    @property
    def airflownetworkmultizonesurfaceeffectiveleakageareas(self):
        """ Get list of all `AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea` objects
        """
        return self._data["airflownetworkmultizonesurfaceeffectiveleakagearea"]
    @property
    def airflownetworkmultizonecomponentdetailedopenings(self):
        """ Get list of all `AirflowNetworkMultiZoneComponentDetailedOpening` objects
        """
        return self._data["airflownetworkmultizonecomponentdetailedopening"]
    @property
    def airflownetworkmultizonecomponentsimpleopenings(self):
        """ Get list of all `AirflowNetworkMultiZoneComponentSimpleOpening` objects
        """
        return self._data["airflownetworkmultizonecomponentsimpleopening"]
    @property
    def airflownetworkmultizonecomponenthorizontalopenings(self):
        """ Get list of all `AirflowNetworkMultiZoneComponentHorizontalOpening` objects
        """
        return self._data["airflownetworkmultizonecomponenthorizontalopening"]
    @property
    def airflownetworkmultizonecomponentzoneexhaustfans(self):
        """ Get list of all `AirflowNetworkMultiZoneComponentZoneExhaustFan` objects
        """
        return self._data["airflownetworkmultizonecomponentzoneexhaustfan"]
    @property
    def airflownetworkmultizoneexternalnodes(self):
        """ Get list of all `AirflowNetworkMultiZoneExternalNode` objects
        """
        return self._data["airflownetworkmultizoneexternalnode"]
    @property
    def airflownetworkmultizonewindpressurecoefficientarrays(self):
        """ Get list of all `AirflowNetworkMultiZoneWindPressureCoefficientArray` objects
        """
        return self._data["airflownetworkmultizonewindpressurecoefficientarray"]
    @property
    def airflownetworkmultizonewindpressurecoefficientvaluess(self):
        """ Get list of all `AirflowNetworkMultiZoneWindPressureCoefficientValues` objects
        """
        return self._data["airflownetworkmultizonewindpressurecoefficientvalues"]
    @property
    def airflownetworkdistributionnodes(self):
        """ Get list of all `AirflowNetworkDistributionNode` objects
        """
        return self._data["airflownetworkdistributionnode"]
    @property
    def airflownetworkdistributioncomponentleaks(self):
        """ Get list of all `AirflowNetworkDistributionComponentLeak` objects
        """
        return self._data["airflownetworkdistributioncomponentleak"]
    @property
    def airflownetworkdistributioncomponentleakageratios(self):
        """ Get list of all `AirflowNetworkDistributionComponentLeakageRatio` objects
        """
        return self._data["airflownetworkdistributioncomponentleakageratio"]
    @property
    def airflownetworkdistributioncomponentducts(self):
        """ Get list of all `AirflowNetworkDistributionComponentDuct` objects
        """
        return self._data["airflownetworkdistributioncomponentduct"]
    @property
    def airflownetworkdistributioncomponentfans(self):
        """ Get list of all `AirflowNetworkDistributionComponentFan` objects
        """
        return self._data["airflownetworkdistributioncomponentfan"]
    @property
    def airflownetworkdistributioncomponentcoils(self):
        """ Get list of all `AirflowNetworkDistributionComponentCoil` objects
        """
        return self._data["airflownetworkdistributioncomponentcoil"]
    @property
    def airflownetworkdistributioncomponentheatexchangers(self):
        """ Get list of all `AirflowNetworkDistributionComponentHeatExchanger` objects
        """
        return self._data["airflownetworkdistributioncomponentheatexchanger"]
    @property
    def airflownetworkdistributioncomponentterminalunits(self):
        """ Get list of all `AirflowNetworkDistributionComponentTerminalUnit` objects
        """
        return self._data["airflownetworkdistributioncomponentterminalunit"]
    @property
    def airflownetworkdistributioncomponentconstantpressuredrops(self):
        """ Get list of all `AirflowNetworkDistributionComponentConstantPressureDrop` objects
        """
        return self._data["airflownetworkdistributioncomponentconstantpressuredrop"]
    @property
    def airflownetworkdistributionlinkages(self):
        """ Get list of all `AirflowNetworkDistributionLinkage` objects
        """
        return self._data["airflownetworkdistributionlinkage"]
    @property
    def exteriorlightss(self):
        """ Get list of all `ExteriorLights` objects
        """
        return self._data["exteriorlights"]
    @property
    def exteriorfuelequipments(self):
        """ Get list of all `ExteriorFuelEquipment` objects
        """
        return self._data["exteriorfuelequipment"]
    @property
    def exteriorwaterequipments(self):
        """ Get list of all `ExteriorWaterEquipment` objects
        """
        return self._data["exteriorwaterequipment"]
    @property
    def hvactemplatethermostats(self):
        """ Get list of all `HvactemplateThermostat` objects
        """
        return self._data["hvactemplatethermostat"]
    @property
    def hvactemplatezoneidealloadsairsystems(self):
        """ Get list of all `HvactemplateZoneIdealLoadsAirSystem` objects
        """
        return self._data["hvactemplatezoneidealloadsairsystem"]
    @property
    def hvactemplatezonebaseboardheats(self):
        """ Get list of all `HvactemplateZoneBaseboardHeat` objects
        """
        return self._data["hvactemplatezonebaseboardheat"]
    @property
    def hvactemplatezonefancoils(self):
        """ Get list of all `HvactemplateZoneFanCoil` objects
        """
        return self._data["hvactemplatezonefancoil"]
    @property
    def hvactemplatezoneptacs(self):
        """ Get list of all `HvactemplateZonePtac` objects
        """
        return self._data["hvactemplatezoneptac"]
    @property
    def hvactemplatezonepthps(self):
        """ Get list of all `HvactemplateZonePthp` objects
        """
        return self._data["hvactemplatezonepthp"]
    @property
    def hvactemplatezonewatertoairheatpumps(self):
        """ Get list of all `HvactemplateZoneWaterToAirHeatPump` objects
        """
        return self._data["hvactemplatezonewatertoairheatpump"]
    @property
    def hvactemplatezonevrfs(self):
        """ Get list of all `HvactemplateZoneVrf` objects
        """
        return self._data["hvactemplatezonevrf"]
    @property
    def hvactemplatezoneunitarys(self):
        """ Get list of all `HvactemplateZoneUnitary` objects
        """
        return self._data["hvactemplatezoneunitary"]
    @property
    def hvactemplatezonevavs(self):
        """ Get list of all `HvactemplateZoneVav` objects
        """
        return self._data["hvactemplatezonevav"]
    @property
    def hvactemplatezonevavfanpowereds(self):
        """ Get list of all `HvactemplateZoneVavFanPowered` objects
        """
        return self._data["hvactemplatezonevavfanpowered"]
    @property
    def hvactemplatezonevavheatandcools(self):
        """ Get list of all `HvactemplateZoneVavHeatAndCool` objects
        """
        return self._data["hvactemplatezonevavheatandcool"]
    @property
    def hvactemplatezoneconstantvolumes(self):
        """ Get list of all `HvactemplateZoneConstantVolume` objects
        """
        return self._data["hvactemplatezoneconstantvolume"]
    @property
    def hvactemplatezonedualducts(self):
        """ Get list of all `HvactemplateZoneDualDuct` objects
        """
        return self._data["hvactemplatezonedualduct"]
    @property
    def hvactemplatesystemvrfs(self):
        """ Get list of all `HvactemplateSystemVrf` objects
        """
        return self._data["hvactemplatesystemvrf"]
    @property
    def hvactemplatesystemunitarys(self):
        """ Get list of all `HvactemplateSystemUnitary` objects
        """
        return self._data["hvactemplatesystemunitary"]
    @property
    def hvactemplatesystemunitaryheatpumpairtoairs(self):
        """ Get list of all `HvactemplateSystemUnitaryHeatPumpAirToAir` objects
        """
        return self._data["hvactemplatesystemunitaryheatpumpairtoair"]
    @property
    def hvactemplatesystemunitarysystems(self):
        """ Get list of all `HvactemplateSystemUnitarySystem` objects
        """
        return self._data["hvactemplatesystemunitarysystem"]
    @property
    def hvactemplatesystemvavs(self):
        """ Get list of all `HvactemplateSystemVav` objects
        """
        return self._data["hvactemplatesystemvav"]
    @property
    def hvactemplatesystempackagedvavs(self):
        """ Get list of all `HvactemplateSystemPackagedVav` objects
        """
        return self._data["hvactemplatesystempackagedvav"]
    @property
    def hvactemplatesystemconstantvolumes(self):
        """ Get list of all `HvactemplateSystemConstantVolume` objects
        """
        return self._data["hvactemplatesystemconstantvolume"]
    @property
    def hvactemplatesystemdualducts(self):
        """ Get list of all `HvactemplateSystemDualDuct` objects
        """
        return self._data["hvactemplatesystemdualduct"]
    @property
    def hvactemplatesystemdedicatedoutdoorairs(self):
        """ Get list of all `HvactemplateSystemDedicatedOutdoorAir` objects
        """
        return self._data["hvactemplatesystemdedicatedoutdoorair"]
    @property
    def hvactemplateplantchilledwaterloops(self):
        """ Get list of all `HvactemplatePlantChilledWaterLoop` objects
        """
        return self._data["hvactemplateplantchilledwaterloop"]
    @property
    def hvactemplateplantchillers(self):
        """ Get list of all `HvactemplatePlantChiller` objects
        """
        return self._data["hvactemplateplantchiller"]
    @property
    def hvactemplateplantchillerobjectreferences(self):
        """ Get list of all `HvactemplatePlantChillerObjectReference` objects
        """
        return self._data["hvactemplateplantchillerobjectreference"]
    @property
    def hvactemplateplanttowers(self):
        """ Get list of all `HvactemplatePlantTower` objects
        """
        return self._data["hvactemplateplanttower"]
    @property
    def hvactemplateplanttowerobjectreferences(self):
        """ Get list of all `HvactemplatePlantTowerObjectReference` objects
        """
        return self._data["hvactemplateplanttowerobjectreference"]
    @property
    def hvactemplateplanthotwaterloops(self):
        """ Get list of all `HvactemplatePlantHotWaterLoop` objects
        """
        return self._data["hvactemplateplanthotwaterloop"]
    @property
    def hvactemplateplantboilers(self):
        """ Get list of all `HvactemplatePlantBoiler` objects
        """
        return self._data["hvactemplateplantboiler"]
    @property
    def hvactemplateplantboilerobjectreferences(self):
        """ Get list of all `HvactemplatePlantBoilerObjectReference` objects
        """
        return self._data["hvactemplateplantboilerobjectreference"]
    @property
    def hvactemplateplantmixedwaterloops(self):
        """ Get list of all `HvactemplatePlantMixedWaterLoop` objects
        """
        return self._data["hvactemplateplantmixedwaterloop"]
    @property
    def designspecificationoutdoorairs(self):
        """ Get list of all `DesignSpecificationOutdoorAir` objects
        """
        return self._data["designspecificationoutdoorair"]
    @property
    def designspecificationzoneairdistributions(self):
        """ Get list of all `DesignSpecificationZoneAirDistribution` objects
        """
        return self._data["designspecificationzoneairdistribution"]
    @property
    def sizingparameterss(self):
        """ Get list of all `SizingParameters` objects
        """
        return self._data["sizingparameters"]
    @property
    def sizingzones(self):
        """ Get list of all `SizingZone` objects
        """
        return self._data["sizingzone"]
    @property
    def designspecificationzonehvacsizings(self):
        """ Get list of all `DesignSpecificationZoneHvacSizing` objects
        """
        return self._data["designspecificationzonehvacsizing"]
    @property
    def sizingsystems(self):
        """ Get list of all `SizingSystem` objects
        """
        return self._data["sizingsystem"]
    @property
    def sizingplants(self):
        """ Get list of all `SizingPlant` objects
        """
        return self._data["sizingplant"]
    @property
    def outputcontrolsizingstyles(self):
        """ Get list of all `OutputControlSizingStyle` objects
        """
        return self._data["outputcontrolsizingstyle"]
    @property
    def zonecontrolhumidistats(self):
        """ Get list of all `ZoneControlHumidistat` objects
        """
        return self._data["zonecontrolhumidistat"]
    @property
    def zonecontrolthermostats(self):
        """ Get list of all `ZoneControlThermostat` objects
        """
        return self._data["zonecontrolthermostat"]
    @property
    def zonecontrolthermostatoperativetemperatures(self):
        """ Get list of all `ZoneControlThermostatOperativeTemperature` objects
        """
        return self._data["zonecontrolthermostatoperativetemperature"]
    @property
    def zonecontrolthermostatthermalcomforts(self):
        """ Get list of all `ZoneControlThermostatThermalComfort` objects
        """
        return self._data["zonecontrolthermostatthermalcomfort"]
    @property
    def zonecontrolthermostattemperatureandhumiditys(self):
        """ Get list of all `ZoneControlThermostatTemperatureAndHumidity` objects
        """
        return self._data["zonecontrolthermostattemperatureandhumidity"]
    @property
    def thermostatsetpointsingleheatings(self):
        """ Get list of all `ThermostatSetpointSingleHeating` objects
        """
        return self._data["thermostatsetpointsingleheating"]
    @property
    def thermostatsetpointsinglecoolings(self):
        """ Get list of all `ThermostatSetpointSingleCooling` objects
        """
        return self._data["thermostatsetpointsinglecooling"]
    @property
    def thermostatsetpointsingleheatingorcoolings(self):
        """ Get list of all `ThermostatSetpointSingleHeatingOrCooling` objects
        """
        return self._data["thermostatsetpointsingleheatingorcooling"]
    @property
    def thermostatsetpointdualsetpoints(self):
        """ Get list of all `ThermostatSetpointDualSetpoint` objects
        """
        return self._data["thermostatsetpointdualsetpoint"]
    @property
    def thermostatsetpointthermalcomfortfangersingleheatings(self):
        """ Get list of all `ThermostatSetpointThermalComfortFangerSingleHeating` objects
        """
        return self._data["thermostatsetpointthermalcomfortfangersingleheating"]
    @property
    def thermostatsetpointthermalcomfortfangersinglecoolings(self):
        """ Get list of all `ThermostatSetpointThermalComfortFangerSingleCooling` objects
        """
        return self._data["thermostatsetpointthermalcomfortfangersinglecooling"]
    @property
    def thermostatsetpointthermalcomfortfangersingleheatingorcoolings(self):
        """ Get list of all `ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling` objects
        """
        return self._data["thermostatsetpointthermalcomfortfangersingleheatingorcooling"]
    @property
    def thermostatsetpointthermalcomfortfangerdualsetpoints(self):
        """ Get list of all `ThermostatSetpointThermalComfortFangerDualSetpoint` objects
        """
        return self._data["thermostatsetpointthermalcomfortfangerdualsetpoint"]
    @property
    def zonecontrolthermostatstageddualsetpoints(self):
        """ Get list of all `ZoneControlThermostatStagedDualSetpoint` objects
        """
        return self._data["zonecontrolthermostatstageddualsetpoint"]
    @property
    def zonecontrolcontaminantcontrollers(self):
        """ Get list of all `ZoneControlContaminantController` objects
        """
        return self._data["zonecontrolcontaminantcontroller"]
    @property
    def zonehvacidealloadsairsystems(self):
        """ Get list of all `ZoneHvacIdealLoadsAirSystem` objects
        """
        return self._data["zonehvacidealloadsairsystem"]
    @property
    def zonehvacfourpipefancoils(self):
        """ Get list of all `ZoneHvacFourPipeFanCoil` objects
        """
        return self._data["zonehvacfourpipefancoil"]
    @property
    def zonehvacwindowairconditioners(self):
        """ Get list of all `ZoneHvacWindowAirConditioner` objects
        """
        return self._data["zonehvacwindowairconditioner"]
    @property
    def zonehvacpackagedterminalairconditioners(self):
        """ Get list of all `ZoneHvacPackagedTerminalAirConditioner` objects
        """
        return self._data["zonehvacpackagedterminalairconditioner"]
    @property
    def zonehvacpackagedterminalheatpumps(self):
        """ Get list of all `ZoneHvacPackagedTerminalHeatPump` objects
        """
        return self._data["zonehvacpackagedterminalheatpump"]
    @property
    def zonehvacwatertoairheatpumps(self):
        """ Get list of all `ZoneHvacWaterToAirHeatPump` objects
        """
        return self._data["zonehvacwatertoairheatpump"]
    @property
    def zonehvacdehumidifierdxs(self):
        """ Get list of all `ZoneHvacDehumidifierDx` objects
        """
        return self._data["zonehvacdehumidifierdx"]
    @property
    def zonehvacenergyrecoveryventilators(self):
        """ Get list of all `ZoneHvacEnergyRecoveryVentilator` objects
        """
        return self._data["zonehvacenergyrecoveryventilator"]
    @property
    def zonehvacenergyrecoveryventilatorcontrollers(self):
        """ Get list of all `ZoneHvacEnergyRecoveryVentilatorController` objects
        """
        return self._data["zonehvacenergyrecoveryventilatorcontroller"]
    @property
    def zonehvacunitventilators(self):
        """ Get list of all `ZoneHvacUnitVentilator` objects
        """
        return self._data["zonehvacunitventilator"]
    @property
    def zonehvacunitheaters(self):
        """ Get list of all `ZoneHvacUnitHeater` objects
        """
        return self._data["zonehvacunitheater"]
    @property
    def zonehvacevaporativecoolerunits(self):
        """ Get list of all `ZoneHvacEvaporativeCoolerUnit` objects
        """
        return self._data["zonehvacevaporativecoolerunit"]
    @property
    def zonehvacoutdoorairunits(self):
        """ Get list of all `ZoneHvacOutdoorAirUnit` objects
        """
        return self._data["zonehvacoutdoorairunit"]
    @property
    def zonehvacoutdoorairunitequipmentlists(self):
        """ Get list of all `ZoneHvacOutdoorAirUnitEquipmentList` objects
        """
        return self._data["zonehvacoutdoorairunitequipmentlist"]
    @property
    def zonehvacterminalunitvariablerefrigerantflows(self):
        """ Get list of all `ZoneHvacTerminalUnitVariableRefrigerantFlow` objects
        """
        return self._data["zonehvacterminalunitvariablerefrigerantflow"]
    @property
    def zonehvacbaseboardradiantconvectivewaters(self):
        """ Get list of all `ZoneHvacBaseboardRadiantConvectiveWater` objects
        """
        return self._data["zonehvacbaseboardradiantconvectivewater"]
    @property
    def zonehvacbaseboardradiantconvectivesteams(self):
        """ Get list of all `ZoneHvacBaseboardRadiantConvectiveSteam` objects
        """
        return self._data["zonehvacbaseboardradiantconvectivesteam"]
    @property
    def zonehvacbaseboardradiantconvectiveelectrics(self):
        """ Get list of all `ZoneHvacBaseboardRadiantConvectiveElectric` objects
        """
        return self._data["zonehvacbaseboardradiantconvectiveelectric"]
    @property
    def zonehvacbaseboardconvectivewaters(self):
        """ Get list of all `ZoneHvacBaseboardConvectiveWater` objects
        """
        return self._data["zonehvacbaseboardconvectivewater"]
    @property
    def zonehvacbaseboardconvectiveelectrics(self):
        """ Get list of all `ZoneHvacBaseboardConvectiveElectric` objects
        """
        return self._data["zonehvacbaseboardconvectiveelectric"]
    @property
    def zonehvaclowtemperatureradiantvariableflows(self):
        """ Get list of all `ZoneHvacLowTemperatureRadiantVariableFlow` objects
        """
        return self._data["zonehvaclowtemperatureradiantvariableflow"]
    @property
    def zonehvaclowtemperatureradiantconstantflows(self):
        """ Get list of all `ZoneHvacLowTemperatureRadiantConstantFlow` objects
        """
        return self._data["zonehvaclowtemperatureradiantconstantflow"]
    @property
    def zonehvaclowtemperatureradiantelectrics(self):
        """ Get list of all `ZoneHvacLowTemperatureRadiantElectric` objects
        """
        return self._data["zonehvaclowtemperatureradiantelectric"]
    @property
    def zonehvaclowtemperatureradiantsurfacegroups(self):
        """ Get list of all `ZoneHvacLowTemperatureRadiantSurfaceGroup` objects
        """
        return self._data["zonehvaclowtemperatureradiantsurfacegroup"]
    @property
    def zonehvachightemperatureradiants(self):
        """ Get list of all `ZoneHvacHighTemperatureRadiant` objects
        """
        return self._data["zonehvachightemperatureradiant"]
    @property
    def zonehvacventilatedslabs(self):
        """ Get list of all `ZoneHvacVentilatedSlab` objects
        """
        return self._data["zonehvacventilatedslab"]
    @property
    def zonehvacventilatedslabslabgroups(self):
        """ Get list of all `ZoneHvacVentilatedSlabSlabGroup` objects
        """
        return self._data["zonehvacventilatedslabslabgroup"]
    @property
    def airterminalsingleductuncontrolleds(self):
        """ Get list of all `AirTerminalSingleDuctUncontrolled` objects
        """
        return self._data["airterminalsingleductuncontrolled"]
    @property
    def airterminalsingleductconstantvolumereheats(self):
        """ Get list of all `AirTerminalSingleDuctConstantVolumeReheat` objects
        """
        return self._data["airterminalsingleductconstantvolumereheat"]
    @property
    def airterminalsingleductvavnoreheats(self):
        """ Get list of all `AirTerminalSingleDuctVavNoReheat` objects
        """
        return self._data["airterminalsingleductvavnoreheat"]
    @property
    def airterminalsingleductvavreheats(self):
        """ Get list of all `AirTerminalSingleDuctVavReheat` objects
        """
        return self._data["airterminalsingleductvavreheat"]
    @property
    def airterminalsingleductvavreheatvariablespeedfans(self):
        """ Get list of all `AirTerminalSingleDuctVavReheatVariableSpeedFan` objects
        """
        return self._data["airterminalsingleductvavreheatvariablespeedfan"]
    @property
    def airterminalsingleductvavheatandcoolnoreheats(self):
        """ Get list of all `AirTerminalSingleDuctVavHeatAndCoolNoReheat` objects
        """
        return self._data["airterminalsingleductvavheatandcoolnoreheat"]
    @property
    def airterminalsingleductvavheatandcoolreheats(self):
        """ Get list of all `AirTerminalSingleDuctVavHeatAndCoolReheat` objects
        """
        return self._data["airterminalsingleductvavheatandcoolreheat"]
    @property
    def airterminalsingleductseriespiureheats(self):
        """ Get list of all `AirTerminalSingleDuctSeriesPiuReheat` objects
        """
        return self._data["airterminalsingleductseriespiureheat"]
    @property
    def airterminalsingleductparallelpiureheats(self):
        """ Get list of all `AirTerminalSingleDuctParallelPiuReheat` objects
        """
        return self._data["airterminalsingleductparallelpiureheat"]
    @property
    def airterminalsingleductconstantvolumefourpipeinductions(self):
        """ Get list of all `AirTerminalSingleDuctConstantVolumeFourPipeInduction` objects
        """
        return self._data["airterminalsingleductconstantvolumefourpipeinduction"]
    @property
    def airterminalsingleductconstantvolumecooledbeams(self):
        """ Get list of all `AirTerminalSingleDuctConstantVolumeCooledBeam` objects
        """
        return self._data["airterminalsingleductconstantvolumecooledbeam"]
    @property
    def airterminalsingleductinletsidemixers(self):
        """ Get list of all `AirTerminalSingleDuctInletSideMixer` objects
        """
        return self._data["airterminalsingleductinletsidemixer"]
    @property
    def airterminalsingleductsupplysidemixers(self):
        """ Get list of all `AirTerminalSingleDuctSupplySideMixer` objects
        """
        return self._data["airterminalsingleductsupplysidemixer"]
    @property
    def airterminaldualductconstantvolumes(self):
        """ Get list of all `AirTerminalDualDuctConstantVolume` objects
        """
        return self._data["airterminaldualductconstantvolume"]
    @property
    def airterminaldualductvavs(self):
        """ Get list of all `AirTerminalDualDuctVav` objects
        """
        return self._data["airterminaldualductvav"]
    @property
    def airterminaldualductvavoutdoorairs(self):
        """ Get list of all `AirTerminalDualDuctVavOutdoorAir` objects
        """
        return self._data["airterminaldualductvavoutdoorair"]
    @property
    def zonehvacairdistributionunits(self):
        """ Get list of all `ZoneHvacAirDistributionUnit` objects
        """
        return self._data["zonehvacairdistributionunit"]
    @property
    def zonehvacequipmentlists(self):
        """ Get list of all `ZoneHvacEquipmentList` objects
        """
        return self._data["zonehvacequipmentlist"]
    @property
    def zonehvacequipmentconnectionss(self):
        """ Get list of all `ZoneHvacEquipmentConnections` objects
        """
        return self._data["zonehvacequipmentconnections"]
    @property
    def fanconstantvolumes(self):
        """ Get list of all `FanConstantVolume` objects
        """
        return self._data["fanconstantvolume"]
    @property
    def fanvariablevolumes(self):
        """ Get list of all `FanVariableVolume` objects
        """
        return self._data["fanvariablevolume"]
    @property
    def fanonoffs(self):
        """ Get list of all `FanOnOff` objects
        """
        return self._data["fanonoff"]
    @property
    def fanzoneexhausts(self):
        """ Get list of all `FanZoneExhaust` objects
        """
        return self._data["fanzoneexhaust"]
    @property
    def fanperformancenightventilations(self):
        """ Get list of all `FanPerformanceNightVentilation` objects
        """
        return self._data["fanperformancenightventilation"]
    @property
    def fancomponentmodels(self):
        """ Get list of all `FanComponentModel` objects
        """
        return self._data["fancomponentmodel"]
    @property
    def coilcoolingwaters(self):
        """ Get list of all `CoilCoolingWater` objects
        """
        return self._data["coilcoolingwater"]
    @property
    def coilcoolingwaterdetailedgeometrys(self):
        """ Get list of all `CoilCoolingWaterDetailedGeometry` objects
        """
        return self._data["coilcoolingwaterdetailedgeometry"]
    @property
    def coilcoolingdxsinglespeeds(self):
        """ Get list of all `CoilCoolingDxSingleSpeed` objects
        """
        return self._data["coilcoolingdxsinglespeed"]
    @property
    def coilcoolingdxtwospeeds(self):
        """ Get list of all `CoilCoolingDxTwoSpeed` objects
        """
        return self._data["coilcoolingdxtwospeed"]
    @property
    def coilcoolingdxmultispeeds(self):
        """ Get list of all `CoilCoolingDxMultiSpeed` objects
        """
        return self._data["coilcoolingdxmultispeed"]
    @property
    def coilcoolingdxvariablespeeds(self):
        """ Get list of all `CoilCoolingDxVariableSpeed` objects
        """
        return self._data["coilcoolingdxvariablespeed"]
    @property
    def coilcoolingdxtwostagewithhumiditycontrolmodes(self):
        """ Get list of all `CoilCoolingDxTwoStageWithHumidityControlMode` objects
        """
        return self._data["coilcoolingdxtwostagewithhumiditycontrolmode"]
    @property
    def coilperformancedxcoolings(self):
        """ Get list of all `CoilPerformanceDxCooling` objects
        """
        return self._data["coilperformancedxcooling"]
    @property
    def coilcoolingdxvariablerefrigerantflows(self):
        """ Get list of all `CoilCoolingDxVariableRefrigerantFlow` objects
        """
        return self._data["coilcoolingdxvariablerefrigerantflow"]
    @property
    def coilheatingdxvariablerefrigerantflows(self):
        """ Get list of all `CoilHeatingDxVariableRefrigerantFlow` objects
        """
        return self._data["coilheatingdxvariablerefrigerantflow"]
    @property
    def coilheatingwaters(self):
        """ Get list of all `CoilHeatingWater` objects
        """
        return self._data["coilheatingwater"]
    @property
    def coilheatingsteams(self):
        """ Get list of all `CoilHeatingSteam` objects
        """
        return self._data["coilheatingsteam"]
    @property
    def coilheatingelectrics(self):
        """ Get list of all `CoilHeatingElectric` objects
        """
        return self._data["coilheatingelectric"]
    @property
    def coilheatingelectricmultistages(self):
        """ Get list of all `CoilHeatingElectricMultiStage` objects
        """
        return self._data["coilheatingelectricmultistage"]
    @property
    def coilheatinggass(self):
        """ Get list of all `CoilHeatingGas` objects
        """
        return self._data["coilheatinggas"]
    @property
    def coilheatinggasmultistages(self):
        """ Get list of all `CoilHeatingGasMultiStage` objects
        """
        return self._data["coilheatinggasmultistage"]
    @property
    def coilheatingdesuperheaters(self):
        """ Get list of all `CoilHeatingDesuperheater` objects
        """
        return self._data["coilheatingdesuperheater"]
    @property
    def coilheatingdxsinglespeeds(self):
        """ Get list of all `CoilHeatingDxSingleSpeed` objects
        """
        return self._data["coilheatingdxsinglespeed"]
    @property
    def coilheatingdxmultispeeds(self):
        """ Get list of all `CoilHeatingDxMultiSpeed` objects
        """
        return self._data["coilheatingdxmultispeed"]
    @property
    def coilheatingdxvariablespeeds(self):
        """ Get list of all `CoilHeatingDxVariableSpeed` objects
        """
        return self._data["coilheatingdxvariablespeed"]
    @property
    def coilcoolingwatertoairheatpumpparameterestimations(self):
        """ Get list of all `CoilCoolingWaterToAirHeatPumpParameterEstimation` objects
        """
        return self._data["coilcoolingwatertoairheatpumpparameterestimation"]
    @property
    def coilheatingwatertoairheatpumpparameterestimations(self):
        """ Get list of all `CoilHeatingWaterToAirHeatPumpParameterEstimation` objects
        """
        return self._data["coilheatingwatertoairheatpumpparameterestimation"]
    @property
    def coilcoolingwatertoairheatpumpequationfits(self):
        """ Get list of all `CoilCoolingWaterToAirHeatPumpEquationFit` objects
        """
        return self._data["coilcoolingwatertoairheatpumpequationfit"]
    @property
    def coilcoolingwatertoairheatpumpvariablespeedequationfits(self):
        """ Get list of all `CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit` objects
        """
        return self._data["coilcoolingwatertoairheatpumpvariablespeedequationfit"]
    @property
    def coilheatingwatertoairheatpumpequationfits(self):
        """ Get list of all `CoilHeatingWaterToAirHeatPumpEquationFit` objects
        """
        return self._data["coilheatingwatertoairheatpumpequationfit"]
    @property
    def coilheatingwatertoairheatpumpvariablespeedequationfits(self):
        """ Get list of all `CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit` objects
        """
        return self._data["coilheatingwatertoairheatpumpvariablespeedequationfit"]
    @property
    def coilwaterheatingairtowaterheatpumps(self):
        """ Get list of all `CoilWaterHeatingAirToWaterHeatPump` objects
        """
        return self._data["coilwaterheatingairtowaterheatpump"]
    @property
    def coilwaterheatingdesuperheaters(self):
        """ Get list of all `CoilWaterHeatingDesuperheater` objects
        """
        return self._data["coilwaterheatingdesuperheater"]
    @property
    def coilsystemcoolingdxs(self):
        """ Get list of all `CoilSystemCoolingDx` objects
        """
        return self._data["coilsystemcoolingdx"]
    @property
    def coilsystemheatingdxs(self):
        """ Get list of all `CoilSystemHeatingDx` objects
        """
        return self._data["coilsystemheatingdx"]
    @property
    def coilsystemcoolingwaterheatexchangerassisteds(self):
        """ Get list of all `CoilSystemCoolingWaterHeatExchangerAssisted` objects
        """
        return self._data["coilsystemcoolingwaterheatexchangerassisted"]
    @property
    def coilsystemcoolingdxheatexchangerassisteds(self):
        """ Get list of all `CoilSystemCoolingDxHeatExchangerAssisted` objects
        """
        return self._data["coilsystemcoolingdxheatexchangerassisted"]
    @property
    def coilcoolingdxsinglespeedthermalstorages(self):
        """ Get list of all `CoilCoolingDxSingleSpeedThermalStorage` objects
        """
        return self._data["coilcoolingdxsinglespeedthermalstorage"]
    @property
    def evaporativecoolerdirectceldekpads(self):
        """ Get list of all `EvaporativeCoolerDirectCelDekPad` objects
        """
        return self._data["evaporativecoolerdirectceldekpad"]
    @property
    def evaporativecoolerindirectceldekpads(self):
        """ Get list of all `EvaporativeCoolerIndirectCelDekPad` objects
        """
        return self._data["evaporativecoolerindirectceldekpad"]
    @property
    def evaporativecoolerindirectwetcoils(self):
        """ Get list of all `EvaporativeCoolerIndirectWetCoil` objects
        """
        return self._data["evaporativecoolerindirectwetcoil"]
    @property
    def evaporativecoolerindirectresearchspecials(self):
        """ Get list of all `EvaporativeCoolerIndirectResearchSpecial` objects
        """
        return self._data["evaporativecoolerindirectresearchspecial"]
    @property
    def evaporativecoolerdirectresearchspecials(self):
        """ Get list of all `EvaporativeCoolerDirectResearchSpecial` objects
        """
        return self._data["evaporativecoolerdirectresearchspecial"]
    @property
    def humidifiersteamelectrics(self):
        """ Get list of all `HumidifierSteamElectric` objects
        """
        return self._data["humidifiersteamelectric"]
    @property
    def dehumidifierdesiccantnofanss(self):
        """ Get list of all `DehumidifierDesiccantNoFans` objects
        """
        return self._data["dehumidifierdesiccantnofans"]
    @property
    def dehumidifierdesiccantsystems(self):
        """ Get list of all `DehumidifierDesiccantSystem` objects
        """
        return self._data["dehumidifierdesiccantsystem"]
    @property
    def heatexchangerairtoairflatplates(self):
        """ Get list of all `HeatExchangerAirToAirFlatPlate` objects
        """
        return self._data["heatexchangerairtoairflatplate"]
    @property
    def heatexchangerairtoairsensibleandlatents(self):
        """ Get list of all `HeatExchangerAirToAirSensibleAndLatent` objects
        """
        return self._data["heatexchangerairtoairsensibleandlatent"]
    @property
    def heatexchangerdesiccantbalancedflows(self):
        """ Get list of all `HeatExchangerDesiccantBalancedFlow` objects
        """
        return self._data["heatexchangerdesiccantbalancedflow"]
    @property
    def heatexchangerdesiccantbalancedflowperformancedatatype1s(self):
        """ Get list of all `HeatExchangerDesiccantBalancedFlowPerformanceDataType1` objects
        """
        return self._data["heatexchangerdesiccantbalancedflowperformancedatatype1"]
    @property
    def airloophvacunitarysystems(self):
        """ Get list of all `AirLoopHvacUnitarySystem` objects
        """
        return self._data["airloophvacunitarysystem"]
    @property
    def unitarysystemperformanceheatpumpmultispeeds(self):
        """ Get list of all `UnitarySystemPerformanceHeatPumpMultispeed` objects
        """
        return self._data["unitarysystemperformanceheatpumpmultispeed"]
    @property
    def airloophvacunitaryfurnaceheatonlys(self):
        """ Get list of all `AirLoopHvacUnitaryFurnaceHeatOnly` objects
        """
        return self._data["airloophvacunitaryfurnaceheatonly"]
    @property
    def airloophvacunitaryfurnaceheatcools(self):
        """ Get list of all `AirLoopHvacUnitaryFurnaceHeatCool` objects
        """
        return self._data["airloophvacunitaryfurnaceheatcool"]
    @property
    def airloophvacunitaryheatonlys(self):
        """ Get list of all `AirLoopHvacUnitaryHeatOnly` objects
        """
        return self._data["airloophvacunitaryheatonly"]
    @property
    def airloophvacunitaryheatcools(self):
        """ Get list of all `AirLoopHvacUnitaryHeatCool` objects
        """
        return self._data["airloophvacunitaryheatcool"]
    @property
    def airloophvacunitaryheatpumpairtoairs(self):
        """ Get list of all `AirLoopHvacUnitaryHeatPumpAirToAir` objects
        """
        return self._data["airloophvacunitaryheatpumpairtoair"]
    @property
    def airloophvacunitaryheatpumpwatertoairs(self):
        """ Get list of all `AirLoopHvacUnitaryHeatPumpWaterToAir` objects
        """
        return self._data["airloophvacunitaryheatpumpwatertoair"]
    @property
    def airloophvacunitaryheatcoolvavchangeoverbypasss(self):
        """ Get list of all `AirLoopHvacUnitaryHeatCoolVavchangeoverBypass` objects
        """
        return self._data["airloophvacunitaryheatcoolvavchangeoverbypass"]
    @property
    def airloophvacunitaryheatpumpairtoairmultispeeds(self):
        """ Get list of all `AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed` objects
        """
        return self._data["airloophvacunitaryheatpumpairtoairmultispeed"]
    @property
    def airconditionervariablerefrigerantflows(self):
        """ Get list of all `AirConditionerVariableRefrigerantFlow` objects
        """
        return self._data["airconditionervariablerefrigerantflow"]
    @property
    def zoneterminalunitlists(self):
        """ Get list of all `ZoneTerminalUnitList` objects
        """
        return self._data["zoneterminalunitlist"]
    @property
    def controllerwatercoils(self):
        """ Get list of all `ControllerWaterCoil` objects
        """
        return self._data["controllerwatercoil"]
    @property
    def controlleroutdoorairs(self):
        """ Get list of all `ControllerOutdoorAir` objects
        """
        return self._data["controlleroutdoorair"]
    @property
    def controllermechanicalventilations(self):
        """ Get list of all `ControllerMechanicalVentilation` objects
        """
        return self._data["controllermechanicalventilation"]
    @property
    def airloophvaccontrollerlists(self):
        """ Get list of all `AirLoopHvacControllerList` objects
        """
        return self._data["airloophvaccontrollerlist"]
    @property
    def airloophvacs(self):
        """ Get list of all `AirLoopHvac` objects
        """
        return self._data["airloophvac"]
    @property
    def airloophvacoutdoorairsystemequipmentlists(self):
        """ Get list of all `AirLoopHvacOutdoorAirSystemEquipmentList` objects
        """
        return self._data["airloophvacoutdoorairsystemequipmentlist"]
    @property
    def airloophvacoutdoorairsystems(self):
        """ Get list of all `AirLoopHvacOutdoorAirSystem` objects
        """
        return self._data["airloophvacoutdoorairsystem"]
    @property
    def outdoorairmixers(self):
        """ Get list of all `OutdoorAirMixer` objects
        """
        return self._data["outdoorairmixer"]
    @property
    def airloophvaczonesplitters(self):
        """ Get list of all `AirLoopHvacZoneSplitter` objects
        """
        return self._data["airloophvaczonesplitter"]
    @property
    def airloophvacsupplyplenums(self):
        """ Get list of all `AirLoopHvacSupplyPlenum` objects
        """
        return self._data["airloophvacsupplyplenum"]
    @property
    def airloophvacsupplypaths(self):
        """ Get list of all `AirLoopHvacSupplyPath` objects
        """
        return self._data["airloophvacsupplypath"]
    @property
    def airloophvaczonemixers(self):
        """ Get list of all `AirLoopHvacZoneMixer` objects
        """
        return self._data["airloophvaczonemixer"]
    @property
    def airloophvacreturnplenums(self):
        """ Get list of all `AirLoopHvacReturnPlenum` objects
        """
        return self._data["airloophvacreturnplenum"]
    @property
    def airloophvacreturnpaths(self):
        """ Get list of all `AirLoopHvacReturnPath` objects
        """
        return self._data["airloophvacreturnpath"]
    @property
    def branchs(self):
        """ Get list of all `Branch` objects
        """
        return self._data["branch"]
    @property
    def branchlists(self):
        """ Get list of all `BranchList` objects
        """
        return self._data["branchlist"]
    @property
    def connectorsplitters(self):
        """ Get list of all `ConnectorSplitter` objects
        """
        return self._data["connectorsplitter"]
    @property
    def connectormixers(self):
        """ Get list of all `ConnectorMixer` objects
        """
        return self._data["connectormixer"]
    @property
    def connectorlists(self):
        """ Get list of all `ConnectorList` objects
        """
        return self._data["connectorlist"]
    @property
    def nodelists(self):
        """ Get list of all `NodeList` objects
        """
        return self._data["nodelist"]
    @property
    def outdoorairnodes(self):
        """ Get list of all `OutdoorAirNode` objects
        """
        return self._data["outdoorairnode"]
    @property
    def outdoorairnodelists(self):
        """ Get list of all `OutdoorAirNodeList` objects
        """
        return self._data["outdoorairnodelist"]
    @property
    def pipeadiabatics(self):
        """ Get list of all `PipeAdiabatic` objects
        """
        return self._data["pipeadiabatic"]
    @property
    def pipeadiabaticsteams(self):
        """ Get list of all `PipeAdiabaticSteam` objects
        """
        return self._data["pipeadiabaticsteam"]
    @property
    def pipeindoors(self):
        """ Get list of all `PipeIndoor` objects
        """
        return self._data["pipeindoor"]
    @property
    def pipeoutdoors(self):
        """ Get list of all `PipeOutdoor` objects
        """
        return self._data["pipeoutdoor"]
    @property
    def pipeundergrounds(self):
        """ Get list of all `PipeUnderground` objects
        """
        return self._data["pipeunderground"]
    @property
    def pipingsystemundergrounddomains(self):
        """ Get list of all `PipingSystemUndergroundDomain` objects
        """
        return self._data["pipingsystemundergrounddomain"]
    @property
    def pipingsystemundergroundpipecircuits(self):
        """ Get list of all `PipingSystemUndergroundPipeCircuit` objects
        """
        return self._data["pipingsystemundergroundpipecircuit"]
    @property
    def pipingsystemundergroundpipesegments(self):
        """ Get list of all `PipingSystemUndergroundPipeSegment` objects
        """
        return self._data["pipingsystemundergroundpipesegment"]
    @property
    def ducts(self):
        """ Get list of all `Duct` objects
        """
        return self._data["duct"]
    @property
    def pumpvariablespeeds(self):
        """ Get list of all `PumpVariableSpeed` objects
        """
        return self._data["pumpvariablespeed"]
    @property
    def pumpconstantspeeds(self):
        """ Get list of all `PumpConstantSpeed` objects
        """
        return self._data["pumpconstantspeed"]
    @property
    def pumpvariablespeedcondensates(self):
        """ Get list of all `PumpVariableSpeedCondensate` objects
        """
        return self._data["pumpvariablespeedcondensate"]
    @property
    def headeredpumpsconstantspeeds(self):
        """ Get list of all `HeaderedPumpsConstantSpeed` objects
        """
        return self._data["headeredpumpsconstantspeed"]
    @property
    def headeredpumpsvariablespeeds(self):
        """ Get list of all `HeaderedPumpsVariableSpeed` objects
        """
        return self._data["headeredpumpsvariablespeed"]
    @property
    def temperingvalves(self):
        """ Get list of all `TemperingValve` objects
        """
        return self._data["temperingvalve"]
    @property
    def loadprofileplants(self):
        """ Get list of all `LoadProfilePlant` objects
        """
        return self._data["loadprofileplant"]
    @property
    def solarcollectorperformanceflatplates(self):
        """ Get list of all `SolarCollectorPerformanceFlatPlate` objects
        """
        return self._data["solarcollectorperformanceflatplate"]
    @property
    def solarcollectorflatplatewaters(self):
        """ Get list of all `SolarCollectorFlatPlateWater` objects
        """
        return self._data["solarcollectorflatplatewater"]
    @property
    def solarcollectorflatplatephotovoltaicthermals(self):
        """ Get list of all `SolarCollectorFlatPlatePhotovoltaicThermal` objects
        """
        return self._data["solarcollectorflatplatephotovoltaicthermal"]
    @property
    def solarcollectorperformancephotovoltaicthermalsimples(self):
        """ Get list of all `SolarCollectorPerformancePhotovoltaicThermalSimple` objects
        """
        return self._data["solarcollectorperformancephotovoltaicthermalsimple"]
    @property
    def solarcollectorintegralcollectorstorages(self):
        """ Get list of all `SolarCollectorIntegralCollectorStorage` objects
        """
        return self._data["solarcollectorintegralcollectorstorage"]
    @property
    def solarcollectorperformanceintegralcollectorstorages(self):
        """ Get list of all `SolarCollectorPerformanceIntegralCollectorStorage` objects
        """
        return self._data["solarcollectorperformanceintegralcollectorstorage"]
    @property
    def solarcollectorunglazedtranspireds(self):
        """ Get list of all `SolarCollectorUnglazedTranspired` objects
        """
        return self._data["solarcollectorunglazedtranspired"]
    @property
    def solarcollectorunglazedtranspiredmultisystems(self):
        """ Get list of all `SolarCollectorUnglazedTranspiredMultisystem` objects
        """
        return self._data["solarcollectorunglazedtranspiredmultisystem"]
    @property
    def boilerhotwaters(self):
        """ Get list of all `BoilerHotWater` objects
        """
        return self._data["boilerhotwater"]
    @property
    def boilersteams(self):
        """ Get list of all `BoilerSteam` objects
        """
        return self._data["boilersteam"]
    @property
    def chillerelectriceirs(self):
        """ Get list of all `ChillerElectricEir` objects
        """
        return self._data["chillerelectriceir"]
    @property
    def chillerelectricreformulatedeirs(self):
        """ Get list of all `ChillerElectricReformulatedEir` objects
        """
        return self._data["chillerelectricreformulatedeir"]
    @property
    def chillerelectrics(self):
        """ Get list of all `ChillerElectric` objects
        """
        return self._data["chillerelectric"]
    @property
    def chillerabsorptionindirects(self):
        """ Get list of all `ChillerAbsorptionIndirect` objects
        """
        return self._data["chillerabsorptionindirect"]
    @property
    def chillerabsorptions(self):
        """ Get list of all `ChillerAbsorption` objects
        """
        return self._data["chillerabsorption"]
    @property
    def chillerconstantcops(self):
        """ Get list of all `ChillerConstantCop` objects
        """
        return self._data["chillerconstantcop"]
    @property
    def chillerenginedrivens(self):
        """ Get list of all `ChillerEngineDriven` objects
        """
        return self._data["chillerenginedriven"]
    @property
    def chillercombustionturbines(self):
        """ Get list of all `ChillerCombustionTurbine` objects
        """
        return self._data["chillercombustionturbine"]
    @property
    def chillerheaterabsorptiondirectfireds(self):
        """ Get list of all `ChillerHeaterAbsorptionDirectFired` objects
        """
        return self._data["chillerheaterabsorptiondirectfired"]
    @property
    def chillerheaterabsorptiondoubleeffects(self):
        """ Get list of all `ChillerHeaterAbsorptionDoubleEffect` objects
        """
        return self._data["chillerheaterabsorptiondoubleeffect"]
    @property
    def heatpumpwatertowaterequationfitheatings(self):
        """ Get list of all `HeatPumpWaterToWaterEquationFitHeating` objects
        """
        return self._data["heatpumpwatertowaterequationfitheating"]
    @property
    def heatpumpwatertowaterequationfitcoolings(self):
        """ Get list of all `HeatPumpWaterToWaterEquationFitCooling` objects
        """
        return self._data["heatpumpwatertowaterequationfitcooling"]
    @property
    def heatpumpwatertowaterparameterestimationcoolings(self):
        """ Get list of all `HeatPumpWaterToWaterParameterEstimationCooling` objects
        """
        return self._data["heatpumpwatertowaterparameterestimationcooling"]
    @property
    def heatpumpwatertowaterparameterestimationheatings(self):
        """ Get list of all `HeatPumpWaterToWaterParameterEstimationHeating` objects
        """
        return self._data["heatpumpwatertowaterparameterestimationheating"]
    @property
    def districtcoolings(self):
        """ Get list of all `DistrictCooling` objects
        """
        return self._data["districtcooling"]
    @property
    def districtheatings(self):
        """ Get list of all `DistrictHeating` objects
        """
        return self._data["districtheating"]
    @property
    def plantcomponenttemperaturesources(self):
        """ Get list of all `PlantComponentTemperatureSource` objects
        """
        return self._data["plantcomponenttemperaturesource"]
    @property
    def centralheatpumpsystems(self):
        """ Get list of all `CentralHeatPumpSystem` objects
        """
        return self._data["centralheatpumpsystem"]
    @property
    def chillerheaterperformanceelectriceirs(self):
        """ Get list of all `ChillerHeaterPerformanceElectricEir` objects
        """
        return self._data["chillerheaterperformanceelectriceir"]
    @property
    def coolingtowersinglespeeds(self):
        """ Get list of all `CoolingTowerSingleSpeed` objects
        """
        return self._data["coolingtowersinglespeed"]
    @property
    def coolingtowertwospeeds(self):
        """ Get list of all `CoolingTowerTwoSpeed` objects
        """
        return self._data["coolingtowertwospeed"]
    @property
    def coolingtowervariablespeedmerkels(self):
        """ Get list of all `CoolingTowerVariableSpeedMerkel` objects
        """
        return self._data["coolingtowervariablespeedmerkel"]
    @property
    def coolingtowervariablespeeds(self):
        """ Get list of all `CoolingTowerVariableSpeed` objects
        """
        return self._data["coolingtowervariablespeed"]
    @property
    def coolingtowerperformancecooltoolss(self):
        """ Get list of all `CoolingTowerPerformanceCoolTools` objects
        """
        return self._data["coolingtowerperformancecooltools"]
    @property
    def coolingtowerperformanceyorkcalcs(self):
        """ Get list of all `CoolingTowerPerformanceYorkCalc` objects
        """
        return self._data["coolingtowerperformanceyorkcalc"]
    @property
    def evaporativefluidcoolersinglespeeds(self):
        """ Get list of all `EvaporativeFluidCoolerSingleSpeed` objects
        """
        return self._data["evaporativefluidcoolersinglespeed"]
    @property
    def evaporativefluidcoolertwospeeds(self):
        """ Get list of all `EvaporativeFluidCoolerTwoSpeed` objects
        """
        return self._data["evaporativefluidcoolertwospeed"]
    @property
    def fluidcoolersinglespeeds(self):
        """ Get list of all `FluidCoolerSingleSpeed` objects
        """
        return self._data["fluidcoolersinglespeed"]
    @property
    def fluidcoolertwospeeds(self):
        """ Get list of all `FluidCoolerTwoSpeed` objects
        """
        return self._data["fluidcoolertwospeed"]
    @property
    def groundheatexchangerverticals(self):
        """ Get list of all `GroundHeatExchangerVertical` objects
        """
        return self._data["groundheatexchangervertical"]
    @property
    def groundheatexchangerponds(self):
        """ Get list of all `GroundHeatExchangerPond` objects
        """
        return self._data["groundheatexchangerpond"]
    @property
    def groundheatexchangersurfaces(self):
        """ Get list of all `GroundHeatExchangerSurface` objects
        """
        return self._data["groundheatexchangersurface"]
    @property
    def groundheatexchangerhorizontaltrenchs(self):
        """ Get list of all `GroundHeatExchangerHorizontalTrench` objects
        """
        return self._data["groundheatexchangerhorizontaltrench"]
    @property
    def heatexchangerfluidtofluids(self):
        """ Get list of all `HeatExchangerFluidToFluid` objects
        """
        return self._data["heatexchangerfluidtofluid"]
    @property
    def waterheatermixeds(self):
        """ Get list of all `WaterHeaterMixed` objects
        """
        return self._data["waterheatermixed"]
    @property
    def waterheaterstratifieds(self):
        """ Get list of all `WaterHeaterStratified` objects
        """
        return self._data["waterheaterstratified"]
    @property
    def waterheatersizings(self):
        """ Get list of all `WaterHeaterSizing` objects
        """
        return self._data["waterheatersizing"]
    @property
    def waterheaterheatpumps(self):
        """ Get list of all `WaterHeaterHeatPump` objects
        """
        return self._data["waterheaterheatpump"]
    @property
    def thermalstorageicesimples(self):
        """ Get list of all `ThermalStorageIceSimple` objects
        """
        return self._data["thermalstorageicesimple"]
    @property
    def thermalstorageicedetaileds(self):
        """ Get list of all `ThermalStorageIceDetailed` objects
        """
        return self._data["thermalstorageicedetailed"]
    @property
    def thermalstoragechilledwatermixeds(self):
        """ Get list of all `ThermalStorageChilledWaterMixed` objects
        """
        return self._data["thermalstoragechilledwatermixed"]
    @property
    def thermalstoragechilledwaterstratifieds(self):
        """ Get list of all `ThermalStorageChilledWaterStratified` objects
        """
        return self._data["thermalstoragechilledwaterstratified"]
    @property
    def plantloops(self):
        """ Get list of all `PlantLoop` objects
        """
        return self._data["plantloop"]
    @property
    def condenserloops(self):
        """ Get list of all `CondenserLoop` objects
        """
        return self._data["condenserloop"]
    @property
    def plantequipmentlists(self):
        """ Get list of all `PlantEquipmentList` objects
        """
        return self._data["plantequipmentlist"]
    @property
    def condenserequipmentlists(self):
        """ Get list of all `CondenserEquipmentList` objects
        """
        return self._data["condenserequipmentlist"]
    @property
    def plantequipmentoperationuncontrolleds(self):
        """ Get list of all `PlantEquipmentOperationUncontrolled` objects
        """
        return self._data["plantequipmentoperationuncontrolled"]
    @property
    def plantequipmentoperationcoolingloads(self):
        """ Get list of all `PlantEquipmentOperationCoolingLoad` objects
        """
        return self._data["plantequipmentoperationcoolingload"]
    @property
    def plantequipmentoperationheatingloads(self):
        """ Get list of all `PlantEquipmentOperationHeatingLoad` objects
        """
        return self._data["plantequipmentoperationheatingload"]
    @property
    def plantequipmentoperationoutdoordrybulbs(self):
        """ Get list of all `PlantEquipmentOperationOutdoorDryBulb` objects
        """
        return self._data["plantequipmentoperationoutdoordrybulb"]
    @property
    def plantequipmentoperationoutdoorwetbulbs(self):
        """ Get list of all `PlantEquipmentOperationOutdoorWetBulb` objects
        """
        return self._data["plantequipmentoperationoutdoorwetbulb"]
    @property
    def plantequipmentoperationoutdoorrelativehumiditys(self):
        """ Get list of all `PlantEquipmentOperationOutdoorRelativeHumidity` objects
        """
        return self._data["plantequipmentoperationoutdoorrelativehumidity"]
    @property
    def plantequipmentoperationoutdoordewpoints(self):
        """ Get list of all `PlantEquipmentOperationOutdoorDewpoint` objects
        """
        return self._data["plantequipmentoperationoutdoordewpoint"]
    @property
    def plantequipmentoperationcomponentsetpoints(self):
        """ Get list of all `PlantEquipmentOperationComponentSetpoint` objects
        """
        return self._data["plantequipmentoperationcomponentsetpoint"]
    @property
    def plantequipmentoperationoutdoordrybulbdifferences(self):
        """ Get list of all `PlantEquipmentOperationOutdoorDryBulbDifference` objects
        """
        return self._data["plantequipmentoperationoutdoordrybulbdifference"]
    @property
    def plantequipmentoperationoutdoorwetbulbdifferences(self):
        """ Get list of all `PlantEquipmentOperationOutdoorWetBulbDifference` objects
        """
        return self._data["plantequipmentoperationoutdoorwetbulbdifference"]
    @property
    def plantequipmentoperationoutdoordewpointdifferences(self):
        """ Get list of all `PlantEquipmentOperationOutdoorDewpointDifference` objects
        """
        return self._data["plantequipmentoperationoutdoordewpointdifference"]
    @property
    def plantequipmentoperationschemess(self):
        """ Get list of all `PlantEquipmentOperationSchemes` objects
        """
        return self._data["plantequipmentoperationschemes"]
    @property
    def condenserequipmentoperationschemess(self):
        """ Get list of all `CondenserEquipmentOperationSchemes` objects
        """
        return self._data["condenserequipmentoperationschemes"]
    @property
    def energymanagementsystemsensors(self):
        """ Get list of all `EnergyManagementSystemSensor` objects
        """
        return self._data["energymanagementsystemsensor"]
    @property
    def energymanagementsystemactuators(self):
        """ Get list of all `EnergyManagementSystemActuator` objects
        """
        return self._data["energymanagementsystemactuator"]
    @property
    def energymanagementsystemprogramcallingmanagers(self):
        """ Get list of all `EnergyManagementSystemProgramCallingManager` objects
        """
        return self._data["energymanagementsystemprogramcallingmanager"]
    @property
    def energymanagementsystemprograms(self):
        """ Get list of all `EnergyManagementSystemProgram` objects
        """
        return self._data["energymanagementsystemprogram"]
    @property
    def energymanagementsystemsubroutines(self):
        """ Get list of all `EnergyManagementSystemSubroutine` objects
        """
        return self._data["energymanagementsystemsubroutine"]
    @property
    def energymanagementsystemglobalvariables(self):
        """ Get list of all `EnergyManagementSystemGlobalVariable` objects
        """
        return self._data["energymanagementsystemglobalvariable"]
    @property
    def energymanagementsystemoutputvariables(self):
        """ Get list of all `EnergyManagementSystemOutputVariable` objects
        """
        return self._data["energymanagementsystemoutputvariable"]
    @property
    def energymanagementsystemmeteredoutputvariables(self):
        """ Get list of all `EnergyManagementSystemMeteredOutputVariable` objects
        """
        return self._data["energymanagementsystemmeteredoutputvariable"]
    @property
    def energymanagementsystemtrendvariables(self):
        """ Get list of all `EnergyManagementSystemTrendVariable` objects
        """
        return self._data["energymanagementsystemtrendvariable"]
    @property
    def energymanagementsysteminternalvariables(self):
        """ Get list of all `EnergyManagementSystemInternalVariable` objects
        """
        return self._data["energymanagementsysteminternalvariable"]
    @property
    def energymanagementsystemcurveortableindexvariables(self):
        """ Get list of all `EnergyManagementSystemCurveOrTableIndexVariable` objects
        """
        return self._data["energymanagementsystemcurveortableindexvariable"]
    @property
    def energymanagementsystemconstructionindexvariables(self):
        """ Get list of all `EnergyManagementSystemConstructionIndexVariable` objects
        """
        return self._data["energymanagementsystemconstructionindexvariable"]
    @property
    def externalinterfaces(self):
        """ Get list of all `ExternalInterface` objects
        """
        return self._data["externalinterface"]
    @property
    def externalinterfaceschedules(self):
        """ Get list of all `ExternalInterfaceSchedule` objects
        """
        return self._data["externalinterfaceschedule"]
    @property
    def externalinterfacevariables(self):
        """ Get list of all `ExternalInterfaceVariable` objects
        """
        return self._data["externalinterfacevariable"]
    @property
    def externalinterfaceactuators(self):
        """ Get list of all `ExternalInterfaceActuator` objects
        """
        return self._data["externalinterfaceactuator"]
    @property
    def externalinterfacefunctionalmockupunitimports(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitImport` objects
        """
        return self._data["externalinterfacefunctionalmockupunitimport"]
    @property
    def externalinterfacefunctionalmockupunitimportfromvariables(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitImportFromVariable` objects
        """
        return self._data["externalinterfacefunctionalmockupunitimportfromvariable"]
    @property
    def externalinterfacefunctionalmockupunitimporttoschedules(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitImportToSchedule` objects
        """
        return self._data["externalinterfacefunctionalmockupunitimporttoschedule"]
    @property
    def externalinterfacefunctionalmockupunitimporttoactuators(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitImportToActuator` objects
        """
        return self._data["externalinterfacefunctionalmockupunitimporttoactuator"]
    @property
    def externalinterfacefunctionalmockupunitimporttovariables(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitImportToVariable` objects
        """
        return self._data["externalinterfacefunctionalmockupunitimporttovariable"]
    @property
    def externalinterfacefunctionalmockupunitexportfromvariables(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitExportFromVariable` objects
        """
        return self._data["externalinterfacefunctionalmockupunitexportfromvariable"]
    @property
    def externalinterfacefunctionalmockupunitexporttoschedules(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitExportToSchedule` objects
        """
        return self._data["externalinterfacefunctionalmockupunitexporttoschedule"]
    @property
    def externalinterfacefunctionalmockupunitexporttoactuators(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitExportToActuator` objects
        """
        return self._data["externalinterfacefunctionalmockupunitexporttoactuator"]
    @property
    def externalinterfacefunctionalmockupunitexporttovariables(self):
        """ Get list of all `ExternalInterfaceFunctionalMockupUnitExportToVariable` objects
        """
        return self._data["externalinterfacefunctionalmockupunitexporttovariable"]
    @property
    def zonehvacforcedairuserdefineds(self):
        """ Get list of all `ZoneHvacForcedAirUserDefined` objects
        """
        return self._data["zonehvacforcedairuserdefined"]
    @property
    def airterminalsingleductuserdefineds(self):
        """ Get list of all `AirTerminalSingleDuctUserDefined` objects
        """
        return self._data["airterminalsingleductuserdefined"]
    @property
    def coiluserdefineds(self):
        """ Get list of all `CoilUserDefined` objects
        """
        return self._data["coiluserdefined"]
    @property
    def plantcomponentuserdefineds(self):
        """ Get list of all `PlantComponentUserDefined` objects
        """
        return self._data["plantcomponentuserdefined"]
    @property
    def plantequipmentoperationuserdefineds(self):
        """ Get list of all `PlantEquipmentOperationUserDefined` objects
        """
        return self._data["plantequipmentoperationuserdefined"]
    @property
    def availabilitymanagerscheduleds(self):
        """ Get list of all `AvailabilityManagerScheduled` objects
        """
        return self._data["availabilitymanagerscheduled"]
    @property
    def availabilitymanagerscheduledons(self):
        """ Get list of all `AvailabilityManagerScheduledOn` objects
        """
        return self._data["availabilitymanagerscheduledon"]
    @property
    def availabilitymanagerscheduledoffs(self):
        """ Get list of all `AvailabilityManagerScheduledOff` objects
        """
        return self._data["availabilitymanagerscheduledoff"]
    @property
    def availabilitymanageroptimumstarts(self):
        """ Get list of all `AvailabilityManagerOptimumStart` objects
        """
        return self._data["availabilitymanageroptimumstart"]
    @property
    def availabilitymanagernightcycles(self):
        """ Get list of all `AvailabilityManagerNightCycle` objects
        """
        return self._data["availabilitymanagernightcycle"]
    @property
    def availabilitymanagerdifferentialthermostats(self):
        """ Get list of all `AvailabilityManagerDifferentialThermostat` objects
        """
        return self._data["availabilitymanagerdifferentialthermostat"]
    @property
    def availabilitymanagerhightemperatureturnoffs(self):
        """ Get list of all `AvailabilityManagerHighTemperatureTurnOff` objects
        """
        return self._data["availabilitymanagerhightemperatureturnoff"]
    @property
    def availabilitymanagerhightemperatureturnons(self):
        """ Get list of all `AvailabilityManagerHighTemperatureTurnOn` objects
        """
        return self._data["availabilitymanagerhightemperatureturnon"]
    @property
    def availabilitymanagerlowtemperatureturnoffs(self):
        """ Get list of all `AvailabilityManagerLowTemperatureTurnOff` objects
        """
        return self._data["availabilitymanagerlowtemperatureturnoff"]
    @property
    def availabilitymanagerlowtemperatureturnons(self):
        """ Get list of all `AvailabilityManagerLowTemperatureTurnOn` objects
        """
        return self._data["availabilitymanagerlowtemperatureturnon"]
    @property
    def availabilitymanagernightventilations(self):
        """ Get list of all `AvailabilityManagerNightVentilation` objects
        """
        return self._data["availabilitymanagernightventilation"]
    @property
    def availabilitymanagerhybridventilations(self):
        """ Get list of all `AvailabilityManagerHybridVentilation` objects
        """
        return self._data["availabilitymanagerhybridventilation"]
    @property
    def availabilitymanagerassignmentlists(self):
        """ Get list of all `AvailabilityManagerAssignmentList` objects
        """
        return self._data["availabilitymanagerassignmentlist"]
    @property
    def setpointmanagerscheduleds(self):
        """ Get list of all `SetpointManagerScheduled` objects
        """
        return self._data["setpointmanagerscheduled"]
    @property
    def setpointmanagerscheduleddualsetpoints(self):
        """ Get list of all `SetpointManagerScheduledDualSetpoint` objects
        """
        return self._data["setpointmanagerscheduleddualsetpoint"]
    @property
    def setpointmanageroutdoorairresets(self):
        """ Get list of all `SetpointManagerOutdoorAirReset` objects
        """
        return self._data["setpointmanageroutdoorairreset"]
    @property
    def setpointmanagersinglezonereheats(self):
        """ Get list of all `SetpointManagerSingleZoneReheat` objects
        """
        return self._data["setpointmanagersinglezonereheat"]
    @property
    def setpointmanagersinglezoneheatings(self):
        """ Get list of all `SetpointManagerSingleZoneHeating` objects
        """
        return self._data["setpointmanagersinglezoneheating"]
    @property
    def setpointmanagersinglezonecoolings(self):
        """ Get list of all `SetpointManagerSingleZoneCooling` objects
        """
        return self._data["setpointmanagersinglezonecooling"]
    @property
    def setpointmanagersinglezonehumidityminimums(self):
        """ Get list of all `SetpointManagerSingleZoneHumidityMinimum` objects
        """
        return self._data["setpointmanagersinglezonehumidityminimum"]
    @property
    def setpointmanagersinglezonehumiditymaximums(self):
        """ Get list of all `SetpointManagerSingleZoneHumidityMaximum` objects
        """
        return self._data["setpointmanagersinglezonehumiditymaximum"]
    @property
    def setpointmanagermixedairs(self):
        """ Get list of all `SetpointManagerMixedAir` objects
        """
        return self._data["setpointmanagermixedair"]
    @property
    def setpointmanageroutdoorairpretreats(self):
        """ Get list of all `SetpointManagerOutdoorAirPretreat` objects
        """
        return self._data["setpointmanageroutdoorairpretreat"]
    @property
    def setpointmanagerwarmests(self):
        """ Get list of all `SetpointManagerWarmest` objects
        """
        return self._data["setpointmanagerwarmest"]
    @property
    def setpointmanagercoldests(self):
        """ Get list of all `SetpointManagerColdest` objects
        """
        return self._data["setpointmanagercoldest"]
    @property
    def setpointmanagerreturnairbypassflows(self):
        """ Get list of all `SetpointManagerReturnAirBypassFlow` objects
        """
        return self._data["setpointmanagerreturnairbypassflow"]
    @property
    def setpointmanagerwarmesttemperatureflows(self):
        """ Get list of all `SetpointManagerWarmestTemperatureFlow` objects
        """
        return self._data["setpointmanagerwarmesttemperatureflow"]
    @property
    def setpointmanagermultizoneheatingaverages(self):
        """ Get list of all `SetpointManagerMultiZoneHeatingAverage` objects
        """
        return self._data["setpointmanagermultizoneheatingaverage"]
    @property
    def setpointmanagermultizonecoolingaverages(self):
        """ Get list of all `SetpointManagerMultiZoneCoolingAverage` objects
        """
        return self._data["setpointmanagermultizonecoolingaverage"]
    @property
    def setpointmanagermultizoneminimumhumidityaverages(self):
        """ Get list of all `SetpointManagerMultiZoneMinimumHumidityAverage` objects
        """
        return self._data["setpointmanagermultizoneminimumhumidityaverage"]
    @property
    def setpointmanagermultizonemaximumhumidityaverages(self):
        """ Get list of all `SetpointManagerMultiZoneMaximumHumidityAverage` objects
        """
        return self._data["setpointmanagermultizonemaximumhumidityaverage"]
    @property
    def setpointmanagermultizonehumidityminimums(self):
        """ Get list of all `SetpointManagerMultiZoneHumidityMinimum` objects
        """
        return self._data["setpointmanagermultizonehumidityminimum"]
    @property
    def setpointmanagermultizonehumiditymaximums(self):
        """ Get list of all `SetpointManagerMultiZoneHumidityMaximum` objects
        """
        return self._data["setpointmanagermultizonehumiditymaximum"]
    @property
    def setpointmanagerfollowoutdoorairtemperatures(self):
        """ Get list of all `SetpointManagerFollowOutdoorAirTemperature` objects
        """
        return self._data["setpointmanagerfollowoutdoorairtemperature"]
    @property
    def setpointmanagerfollowsystemnodetemperatures(self):
        """ Get list of all `SetpointManagerFollowSystemNodeTemperature` objects
        """
        return self._data["setpointmanagerfollowsystemnodetemperature"]
    @property
    def setpointmanagerfollowgroundtemperatures(self):
        """ Get list of all `SetpointManagerFollowGroundTemperature` objects
        """
        return self._data["setpointmanagerfollowgroundtemperature"]
    @property
    def setpointmanagercondenserenteringresets(self):
        """ Get list of all `SetpointManagerCondenserEnteringReset` objects
        """
        return self._data["setpointmanagercondenserenteringreset"]
    @property
    def setpointmanagercondenserenteringresetideals(self):
        """ Get list of all `SetpointManagerCondenserEnteringResetIdeal` objects
        """
        return self._data["setpointmanagercondenserenteringresetideal"]
    @property
    def setpointmanagersinglezoneonestagecoolings(self):
        """ Get list of all `SetpointManagerSingleZoneOneStageCooling` objects
        """
        return self._data["setpointmanagersinglezoneonestagecooling"]
    @property
    def setpointmanagersinglezoneonestageheatings(self):
        """ Get list of all `SetpointManagerSingleZoneOneStageHeating` objects
        """
        return self._data["setpointmanagersinglezoneonestageheating"]
    @property
    def refrigerationcases(self):
        """ Get list of all `RefrigerationCase` objects
        """
        return self._data["refrigerationcase"]
    @property
    def refrigerationcompressorracks(self):
        """ Get list of all `RefrigerationCompressorRack` objects
        """
        return self._data["refrigerationcompressorrack"]
    @property
    def refrigerationcaseandwalkinlists(self):
        """ Get list of all `RefrigerationCaseAndWalkInList` objects
        """
        return self._data["refrigerationcaseandwalkinlist"]
    @property
    def refrigerationcondenseraircooleds(self):
        """ Get list of all `RefrigerationCondenserAirCooled` objects
        """
        return self._data["refrigerationcondenseraircooled"]
    @property
    def refrigerationcondenserevaporativecooleds(self):
        """ Get list of all `RefrigerationCondenserEvaporativeCooled` objects
        """
        return self._data["refrigerationcondenserevaporativecooled"]
    @property
    def refrigerationcondenserwatercooleds(self):
        """ Get list of all `RefrigerationCondenserWaterCooled` objects
        """
        return self._data["refrigerationcondenserwatercooled"]
    @property
    def refrigerationcondensercascades(self):
        """ Get list of all `RefrigerationCondenserCascade` objects
        """
        return self._data["refrigerationcondensercascade"]
    @property
    def refrigerationgascooleraircooleds(self):
        """ Get list of all `RefrigerationGasCoolerAirCooled` objects
        """
        return self._data["refrigerationgascooleraircooled"]
    @property
    def refrigerationtransferloadlists(self):
        """ Get list of all `RefrigerationTransferLoadList` objects
        """
        return self._data["refrigerationtransferloadlist"]
    @property
    def refrigerationsubcoolers(self):
        """ Get list of all `RefrigerationSubcooler` objects
        """
        return self._data["refrigerationsubcooler"]
    @property
    def refrigerationcompressors(self):
        """ Get list of all `RefrigerationCompressor` objects
        """
        return self._data["refrigerationcompressor"]
    @property
    def refrigerationcompressorlists(self):
        """ Get list of all `RefrigerationCompressorList` objects
        """
        return self._data["refrigerationcompressorlist"]
    @property
    def refrigerationsystems(self):
        """ Get list of all `RefrigerationSystem` objects
        """
        return self._data["refrigerationsystem"]
    @property
    def refrigerationtranscriticalsystems(self):
        """ Get list of all `RefrigerationTranscriticalSystem` objects
        """
        return self._data["refrigerationtranscriticalsystem"]
    @property
    def refrigerationsecondarysystems(self):
        """ Get list of all `RefrigerationSecondarySystem` objects
        """
        return self._data["refrigerationsecondarysystem"]
    @property
    def refrigerationwalkins(self):
        """ Get list of all `RefrigerationWalkIn` objects
        """
        return self._data["refrigerationwalkin"]
    @property
    def refrigerationairchillers(self):
        """ Get list of all `RefrigerationAirChiller` objects
        """
        return self._data["refrigerationairchiller"]
    @property
    def zonehvacrefrigerationchillersets(self):
        """ Get list of all `ZoneHvacRefrigerationChillerSet` objects
        """
        return self._data["zonehvacrefrigerationchillerset"]
    @property
    def demandmanagerassignmentlists(self):
        """ Get list of all `DemandManagerAssignmentList` objects
        """
        return self._data["demandmanagerassignmentlist"]
    @property
    def demandmanagerexteriorlightss(self):
        """ Get list of all `DemandManagerExteriorLights` objects
        """
        return self._data["demandmanagerexteriorlights"]
    @property
    def demandmanagerlightss(self):
        """ Get list of all `DemandManagerLights` objects
        """
        return self._data["demandmanagerlights"]
    @property
    def demandmanagerelectricequipments(self):
        """ Get list of all `DemandManagerElectricEquipment` objects
        """
        return self._data["demandmanagerelectricequipment"]
    @property
    def demandmanagerthermostatss(self):
        """ Get list of all `DemandManagerThermostats` objects
        """
        return self._data["demandmanagerthermostats"]
    @property
    def generatorinternalcombustionengines(self):
        """ Get list of all `GeneratorInternalCombustionEngine` objects
        """
        return self._data["generatorinternalcombustionengine"]
    @property
    def generatorcombustionturbines(self):
        """ Get list of all `GeneratorCombustionTurbine` objects
        """
        return self._data["generatorcombustionturbine"]
    @property
    def generatormicroturbines(self):
        """ Get list of all `GeneratorMicroTurbine` objects
        """
        return self._data["generatormicroturbine"]
    @property
    def generatorphotovoltaics(self):
        """ Get list of all `GeneratorPhotovoltaic` objects
        """
        return self._data["generatorphotovoltaic"]
    @property
    def photovoltaicperformancesimples(self):
        """ Get list of all `PhotovoltaicPerformanceSimple` objects
        """
        return self._data["photovoltaicperformancesimple"]
    @property
    def photovoltaicperformanceequivalentonediodes(self):
        """ Get list of all `PhotovoltaicPerformanceEquivalentOneDiode` objects
        """
        return self._data["photovoltaicperformanceequivalentonediode"]
    @property
    def photovoltaicperformancesandias(self):
        """ Get list of all `PhotovoltaicPerformanceSandia` objects
        """
        return self._data["photovoltaicperformancesandia"]
    @property
    def generatorfuelcells(self):
        """ Get list of all `GeneratorFuelCell` objects
        """
        return self._data["generatorfuelcell"]
    @property
    def generatorfuelcellpowermodules(self):
        """ Get list of all `GeneratorFuelCellPowerModule` objects
        """
        return self._data["generatorfuelcellpowermodule"]
    @property
    def generatorfuelcellairsupplys(self):
        """ Get list of all `GeneratorFuelCellAirSupply` objects
        """
        return self._data["generatorfuelcellairsupply"]
    @property
    def generatorfuelcellwatersupplys(self):
        """ Get list of all `GeneratorFuelCellWaterSupply` objects
        """
        return self._data["generatorfuelcellwatersupply"]
    @property
    def generatorfuelcellauxiliaryheaters(self):
        """ Get list of all `GeneratorFuelCellAuxiliaryHeater` objects
        """
        return self._data["generatorfuelcellauxiliaryheater"]
    @property
    def generatorfuelcellexhaustgastowaterheatexchangers(self):
        """ Get list of all `GeneratorFuelCellExhaustGasToWaterHeatExchanger` objects
        """
        return self._data["generatorfuelcellexhaustgastowaterheatexchanger"]
    @property
    def generatorfuelcellelectricalstorages(self):
        """ Get list of all `GeneratorFuelCellElectricalStorage` objects
        """
        return self._data["generatorfuelcellelectricalstorage"]
    @property
    def generatorfuelcellinverters(self):
        """ Get list of all `GeneratorFuelCellInverter` objects
        """
        return self._data["generatorfuelcellinverter"]
    @property
    def generatorfuelcellstackcoolers(self):
        """ Get list of all `GeneratorFuelCellStackCooler` objects
        """
        return self._data["generatorfuelcellstackcooler"]
    @property
    def generatormicrochps(self):
        """ Get list of all `GeneratorMicroChp` objects
        """
        return self._data["generatormicrochp"]
    @property
    def generatormicrochpnonnormalizedparameterss(self):
        """ Get list of all `GeneratorMicroChpNonNormalizedParameters` objects
        """
        return self._data["generatormicrochpnonnormalizedparameters"]
    @property
    def generatorfuelsupplys(self):
        """ Get list of all `GeneratorFuelSupply` objects
        """
        return self._data["generatorfuelsupply"]
    @property
    def generatorwindturbines(self):
        """ Get list of all `GeneratorWindTurbine` objects
        """
        return self._data["generatorwindturbine"]
    @property
    def electricloadcentergeneratorss(self):
        """ Get list of all `ElectricLoadCenterGenerators` objects
        """
        return self._data["electricloadcentergenerators"]
    @property
    def electricloadcenterinvertersimples(self):
        """ Get list of all `ElectricLoadCenterInverterSimple` objects
        """
        return self._data["electricloadcenterinvertersimple"]
    @property
    def electricloadcenterinverterfunctionofpowers(self):
        """ Get list of all `ElectricLoadCenterInverterFunctionOfPower` objects
        """
        return self._data["electricloadcenterinverterfunctionofpower"]
    @property
    def electricloadcenterinverterlookuptables(self):
        """ Get list of all `ElectricLoadCenterInverterLookUpTable` objects
        """
        return self._data["electricloadcenterinverterlookuptable"]
    @property
    def electricloadcenterstoragesimples(self):
        """ Get list of all `ElectricLoadCenterStorageSimple` objects
        """
        return self._data["electricloadcenterstoragesimple"]
    @property
    def electricloadcenterstoragebatterys(self):
        """ Get list of all `ElectricLoadCenterStorageBattery` objects
        """
        return self._data["electricloadcenterstoragebattery"]
    @property
    def electricloadcentertransformers(self):
        """ Get list of all `ElectricLoadCenterTransformer` objects
        """
        return self._data["electricloadcentertransformer"]
    @property
    def electricloadcenterdistributions(self):
        """ Get list of all `ElectricLoadCenterDistribution` objects
        """
        return self._data["electricloadcenterdistribution"]
    @property
    def wateruseequipments(self):
        """ Get list of all `WaterUseEquipment` objects
        """
        return self._data["wateruseequipment"]
    @property
    def wateruseconnectionss(self):
        """ Get list of all `WaterUseConnections` objects
        """
        return self._data["wateruseconnections"]
    @property
    def waterusestorages(self):
        """ Get list of all `WaterUseStorage` objects
        """
        return self._data["waterusestorage"]
    @property
    def waterusewells(self):
        """ Get list of all `WaterUseWell` objects
        """
        return self._data["waterusewell"]
    @property
    def wateruseraincollectors(self):
        """ Get list of all `WaterUseRainCollector` objects
        """
        return self._data["wateruseraincollector"]
    @property
    def faultmodeltemperaturesensoroffsetoutdoorairs(self):
        """ Get list of all `FaultModelTemperatureSensorOffsetOutdoorAir` objects
        """
        return self._data["faultmodeltemperaturesensoroffsetoutdoorair"]
    @property
    def faultmodelhumiditysensoroffsetoutdoorairs(self):
        """ Get list of all `FaultModelHumiditySensorOffsetOutdoorAir` objects
        """
        return self._data["faultmodelhumiditysensoroffsetoutdoorair"]
    @property
    def faultmodelenthalpysensoroffsetoutdoorairs(self):
        """ Get list of all `FaultModelEnthalpySensorOffsetOutdoorAir` objects
        """
        return self._data["faultmodelenthalpysensoroffsetoutdoorair"]
    @property
    def faultmodelpressuresensoroffsetoutdoorairs(self):
        """ Get list of all `FaultModelPressureSensorOffsetOutdoorAir` objects
        """
        return self._data["faultmodelpressuresensoroffsetoutdoorair"]
    @property
    def faultmodeltemperaturesensoroffsetreturnairs(self):
        """ Get list of all `FaultModelTemperatureSensorOffsetReturnAir` objects
        """
        return self._data["faultmodeltemperaturesensoroffsetreturnair"]
    @property
    def faultmodelenthalpysensoroffsetreturnairs(self):
        """ Get list of all `FaultModelEnthalpySensorOffsetReturnAir` objects
        """
        return self._data["faultmodelenthalpysensoroffsetreturnair"]
    @property
    def faultmodelfoulingcoils(self):
        """ Get list of all `FaultModelFoulingCoil` objects
        """
        return self._data["faultmodelfoulingcoil"]
    @property
    def matrixtwodimensions(self):
        """ Get list of all `MatrixTwoDimension` objects
        """
        return self._data["matrixtwodimension"]
    @property
    def curvelinears(self):
        """ Get list of all `CurveLinear` objects
        """
        return self._data["curvelinear"]
    @property
    def curvequadlinears(self):
        """ Get list of all `CurveQuadLinear` objects
        """
        return self._data["curvequadlinear"]
    @property
    def curvequadratics(self):
        """ Get list of all `CurveQuadratic` objects
        """
        return self._data["curvequadratic"]
    @property
    def curvecubics(self):
        """ Get list of all `CurveCubic` objects
        """
        return self._data["curvecubic"]
    @property
    def curvequartics(self):
        """ Get list of all `CurveQuartic` objects
        """
        return self._data["curvequartic"]
    @property
    def curveexponents(self):
        """ Get list of all `CurveExponent` objects
        """
        return self._data["curveexponent"]
    @property
    def curvebicubics(self):
        """ Get list of all `CurveBicubic` objects
        """
        return self._data["curvebicubic"]
    @property
    def curvebiquadratics(self):
        """ Get list of all `CurveBiquadratic` objects
        """
        return self._data["curvebiquadratic"]
    @property
    def curvequadraticlinears(self):
        """ Get list of all `CurveQuadraticLinear` objects
        """
        return self._data["curvequadraticlinear"]
    @property
    def curvetriquadratics(self):
        """ Get list of all `CurveTriquadratic` objects
        """
        return self._data["curvetriquadratic"]
    @property
    def curvefunctionalpressuredrops(self):
        """ Get list of all `CurveFunctionalPressureDrop` objects
        """
        return self._data["curvefunctionalpressuredrop"]
    @property
    def curvefanpressurerises(self):
        """ Get list of all `CurveFanPressureRise` objects
        """
        return self._data["curvefanpressurerise"]
    @property
    def curveexponentialskewnormals(self):
        """ Get list of all `CurveExponentialSkewNormal` objects
        """
        return self._data["curveexponentialskewnormal"]
    @property
    def curvesigmoids(self):
        """ Get list of all `CurveSigmoid` objects
        """
        return self._data["curvesigmoid"]
    @property
    def curverectangularhyperbola1s(self):
        """ Get list of all `CurveRectangularHyperbola1` objects
        """
        return self._data["curverectangularhyperbola1"]
    @property
    def curverectangularhyperbola2s(self):
        """ Get list of all `CurveRectangularHyperbola2` objects
        """
        return self._data["curverectangularhyperbola2"]
    @property
    def curveexponentialdecays(self):
        """ Get list of all `CurveExponentialDecay` objects
        """
        return self._data["curveexponentialdecay"]
    @property
    def curvedoubleexponentialdecays(self):
        """ Get list of all `CurveDoubleExponentialDecay` objects
        """
        return self._data["curvedoubleexponentialdecay"]
    @property
    def tableoneindependentvariables(self):
        """ Get list of all `TableOneIndependentVariable` objects
        """
        return self._data["tableoneindependentvariable"]
    @property
    def tabletwoindependentvariabless(self):
        """ Get list of all `TableTwoIndependentVariables` objects
        """
        return self._data["tabletwoindependentvariables"]
    @property
    def tablemultivariablelookups(self):
        """ Get list of all `TableMultiVariableLookup` objects
        """
        return self._data["tablemultivariablelookup"]
    @property
    def fluidpropertiesnames(self):
        """ Get list of all `FluidPropertiesName` objects
        """
        return self._data["fluidpropertiesname"]
    @property
    def fluidpropertiesglycolconcentrations(self):
        """ Get list of all `FluidPropertiesGlycolConcentration` objects
        """
        return self._data["fluidpropertiesglycolconcentration"]
    @property
    def fluidpropertiestemperaturess(self):
        """ Get list of all `FluidPropertiesTemperatures` objects
        """
        return self._data["fluidpropertiestemperatures"]
    @property
    def fluidpropertiessaturateds(self):
        """ Get list of all `FluidPropertiesSaturated` objects
        """
        return self._data["fluidpropertiessaturated"]
    @property
    def fluidpropertiessuperheateds(self):
        """ Get list of all `FluidPropertiesSuperheated` objects
        """
        return self._data["fluidpropertiessuperheated"]
    @property
    def fluidpropertiesconcentrations(self):
        """ Get list of all `FluidPropertiesConcentration` objects
        """
        return self._data["fluidpropertiesconcentration"]
    @property
    def currencytypes(self):
        """ Get list of all `CurrencyType` objects
        """
        return self._data["currencytype"]
    @property
    def componentcostadjustmentss(self):
        """ Get list of all `ComponentCostAdjustments` objects
        """
        return self._data["componentcostadjustments"]
    @property
    def componentcostreferences(self):
        """ Get list of all `ComponentCostReference` objects
        """
        return self._data["componentcostreference"]
    @property
    def componentcostlineitems(self):
        """ Get list of all `ComponentCostLineItem` objects
        """
        return self._data["componentcostlineitem"]
    @property
    def utilitycosttariffs(self):
        """ Get list of all `UtilityCostTariff` objects
        """
        return self._data["utilitycosttariff"]
    @property
    def utilitycostqualifys(self):
        """ Get list of all `UtilityCostQualify` objects
        """
        return self._data["utilitycostqualify"]
    @property
    def utilitycostchargesimples(self):
        """ Get list of all `UtilityCostChargeSimple` objects
        """
        return self._data["utilitycostchargesimple"]
    @property
    def utilitycostchargeblocks(self):
        """ Get list of all `UtilityCostChargeBlock` objects
        """
        return self._data["utilitycostchargeblock"]
    @property
    def utilitycostratchets(self):
        """ Get list of all `UtilityCostRatchet` objects
        """
        return self._data["utilitycostratchet"]
    @property
    def utilitycostvariables(self):
        """ Get list of all `UtilityCostVariable` objects
        """
        return self._data["utilitycostvariable"]
    @property
    def utilitycostcomputations(self):
        """ Get list of all `UtilityCostComputation` objects
        """
        return self._data["utilitycostcomputation"]
    @property
    def lifecyclecostparameterss(self):
        """ Get list of all `LifeCycleCostParameters` objects
        """
        return self._data["lifecyclecostparameters"]
    @property
    def lifecyclecostrecurringcostss(self):
        """ Get list of all `LifeCycleCostRecurringCosts` objects
        """
        return self._data["lifecyclecostrecurringcosts"]
    @property
    def lifecyclecostnonrecurringcosts(self):
        """ Get list of all `LifeCycleCostNonrecurringCost` objects
        """
        return self._data["lifecyclecostnonrecurringcost"]
    @property
    def lifecyclecostusepriceescalations(self):
        """ Get list of all `LifeCycleCostUsePriceEscalation` objects
        """
        return self._data["lifecyclecostusepriceescalation"]
    @property
    def lifecyclecostuseadjustments(self):
        """ Get list of all `LifeCycleCostUseAdjustment` objects
        """
        return self._data["lifecyclecostuseadjustment"]
    @property
    def parametricsetvalueforruns(self):
        """ Get list of all `ParametricSetValueForRun` objects
        """
        return self._data["parametricsetvalueforrun"]
    @property
    def parametriclogics(self):
        """ Get list of all `ParametricLogic` objects
        """
        return self._data["parametriclogic"]
    @property
    def parametricruncontrols(self):
        """ Get list of all `ParametricRunControl` objects
        """
        return self._data["parametricruncontrol"]
    @property
    def parametricfilenamesuffixs(self):
        """ Get list of all `ParametricFileNameSuffix` objects
        """
        return self._data["parametricfilenamesuffix"]
    @property
    def outputvariabledictionarys(self):
        """ Get list of all `OutputVariableDictionary` objects
        """
        return self._data["outputvariabledictionary"]
    @property
    def outputsurfaceslists(self):
        """ Get list of all `OutputSurfacesList` objects
        """
        return self._data["outputsurfaceslist"]
    @property
    def outputsurfacesdrawings(self):
        """ Get list of all `OutputSurfacesDrawing` objects
        """
        return self._data["outputsurfacesdrawing"]
    @property
    def outputscheduless(self):
        """ Get list of all `OutputSchedules` objects
        """
        return self._data["outputschedules"]
    @property
    def outputconstructionss(self):
        """ Get list of all `OutputConstructions` objects
        """
        return self._data["outputconstructions"]
    @property
    def outputenergymanagementsystems(self):
        """ Get list of all `OutputEnergyManagementSystem` objects
        """
        return self._data["outputenergymanagementsystem"]
    @property
    def outputcontrolsurfacecolorschemes(self):
        """ Get list of all `OutputControlSurfaceColorScheme` objects
        """
        return self._data["outputcontrolsurfacecolorscheme"]
    @property
    def outputtablesummaryreportss(self):
        """ Get list of all `OutputTableSummaryReports` objects
        """
        return self._data["outputtablesummaryreports"]
    @property
    def outputtabletimebinss(self):
        """ Get list of all `OutputTableTimeBins` objects
        """
        return self._data["outputtabletimebins"]
    @property
    def outputtablemonthlys(self):
        """ Get list of all `OutputTableMonthly` objects
        """
        return self._data["outputtablemonthly"]
    @property
    def outputcontroltablestyles(self):
        """ Get list of all `OutputControlTableStyle` objects
        """
        return self._data["outputcontroltablestyle"]
    @property
    def outputcontrolreportingtolerancess(self):
        """ Get list of all `OutputControlReportingTolerances` objects
        """
        return self._data["outputcontrolreportingtolerances"]
    @property
    def outputvariables(self):
        """ Get list of all `OutputVariable` objects
        """
        return self._data["outputvariable"]
    @property
    def outputmeters(self):
        """ Get list of all `OutputMeter` objects
        """
        return self._data["outputmeter"]
    @property
    def outputmetermeterfileonlys(self):
        """ Get list of all `OutputMeterMeterFileOnly` objects
        """
        return self._data["outputmetermeterfileonly"]
    @property
    def outputmetercumulatives(self):
        """ Get list of all `OutputMeterCumulative` objects
        """
        return self._data["outputmetercumulative"]
    @property
    def outputmetercumulativemeterfileonlys(self):
        """ Get list of all `OutputMeterCumulativeMeterFileOnly` objects
        """
        return self._data["outputmetercumulativemeterfileonly"]
    @property
    def metercustoms(self):
        """ Get list of all `MeterCustom` objects
        """
        return self._data["metercustom"]
    @property
    def metercustomdecrements(self):
        """ Get list of all `MeterCustomDecrement` objects
        """
        return self._data["metercustomdecrement"]
    @property
    def outputsqlites(self):
        """ Get list of all `OutputSqlite` objects
        """
        return self._data["outputsqlite"]
    @property
    def outputenvironmentalimpactfactorss(self):
        """ Get list of all `OutputEnvironmentalImpactFactors` objects
        """
        return self._data["outputenvironmentalimpactfactors"]
    @property
    def environmentalimpactfactorss(self):
        """ Get list of all `EnvironmentalImpactFactors` objects
        """
        return self._data["environmentalimpactfactors"]
    @property
    def fuelfactorss(self):
        """ Get list of all `FuelFactors` objects
        """
        return self._data["fuelfactors"]
    @property
    def outputdiagnosticss(self):
        """ Get list of all `OutputDiagnostics` objects
        """
        return self._data["outputdiagnostics"]
    @property
    def outputdebuggingdatas(self):
        """ Get list of all `OutputDebuggingData` objects
        """
        return self._data["outputdebuggingdata"]
    @property
    def outputpreprocessormessages(self):
        """ Get list of all `OutputPreprocessorMessage` objects
        """
        return self._data["outputpreprocessormessage"]

    @classmethod
    def _create_datadict(cls, internal_name):
        """ Creates an object depending on `internal_name`

            Args:
                internal_name (str): IDD name

            Raises:
                ValueError: if `internal_name` cannot be matched to a data dictionary object
        """
        if internal_name.lower() == "lead input":
            return LeadInput()
        if internal_name.lower() == "simulation data":
            return SimulationData()
        if internal_name.lower() == "version":
            return Version()
        if internal_name.lower() == "simulationcontrol":
            return SimulationControl()
        if internal_name.lower() == "building":
            return Building()
        if internal_name.lower() == "shadowcalculation":
            return ShadowCalculation()
        if internal_name.lower() == "surfaceconvectionalgorithm:inside":
            return SurfaceConvectionAlgorithmInside()
        if internal_name.lower() == "surfaceconvectionalgorithm:outside":
            return SurfaceConvectionAlgorithmOutside()
        if internal_name.lower() == "heatbalancealgorithm":
            return HeatBalanceAlgorithm()
        if internal_name.lower() == "heatbalancesettings:conductionfinitedifference":
            return HeatBalanceSettingsConductionFiniteDifference()
        if internal_name.lower() == "zoneairheatbalancealgorithm":
            return ZoneAirHeatBalanceAlgorithm()
        if internal_name.lower() == "zoneaircontaminantbalance":
            return ZoneAirContaminantBalance()
        if internal_name.lower() == "zoneairmassflowconservation":
            return ZoneAirMassFlowConservation()
        if internal_name.lower() == "zonecapacitancemultiplier:researchspecial":
            return ZoneCapacitanceMultiplierResearchSpecial()
        if internal_name.lower() == "timestep":
            return Timestep()
        if internal_name.lower() == "convergencelimits":
            return ConvergenceLimits()
        if internal_name.lower() == "programcontrol":
            return ProgramControl()
        if internal_name.lower() == "compliance:building":
            return ComplianceBuilding()
        if internal_name.lower() == "site:location":
            return SiteLocation()
        if internal_name.lower() == "sizingperiod:designday":
            return SizingPeriodDesignDay()
        if internal_name.lower() == "sizingperiod:weatherfiledays":
            return SizingPeriodWeatherFileDays()
        if internal_name.lower() == "sizingperiod:weatherfileconditiontype":
            return SizingPeriodWeatherFileConditionType()
        if internal_name.lower() == "runperiod":
            return RunPeriod()
        if internal_name.lower() == "runperiod:customrange":
            return RunPeriodCustomRange()
        if internal_name.lower() == "runperiodcontrol:specialdays":
            return RunPeriodControlSpecialDays()
        if internal_name.lower() == "runperiodcontrol:daylightsavingtime":
            return RunPeriodControlDaylightSavingTime()
        if internal_name.lower() == "weatherproperty:skytemperature":
            return WeatherPropertySkyTemperature()
        if internal_name.lower() == "site:weatherstation":
            return SiteWeatherStation()
        if internal_name.lower() == "site:heightvariation":
            return SiteHeightVariation()
        if internal_name.lower() == "site:groundtemperature:buildingsurface":
            return SiteGroundTemperatureBuildingSurface()
        if internal_name.lower() == "site:groundtemperature:fcfactormethod":
            return SiteGroundTemperatureFcfactorMethod()
        if internal_name.lower() == "site:groundtemperature:shallow":
            return SiteGroundTemperatureShallow()
        if internal_name.lower() == "site:groundtemperature:deep":
            return SiteGroundTemperatureDeep()
        if internal_name.lower() == "site:grounddomain":
            return SiteGroundDomain()
        if internal_name.lower() == "site:groundreflectance":
            return SiteGroundReflectance()
        if internal_name.lower() == "site:groundreflectance:snowmodifier":
            return SiteGroundReflectanceSnowModifier()
        if internal_name.lower() == "site:watermainstemperature":
            return SiteWaterMainsTemperature()
        if internal_name.lower() == "site:precipitation":
            return SitePrecipitation()
        if internal_name.lower() == "roofirrigation":
            return RoofIrrigation()
        if internal_name.lower() == "site:solarandvisiblespectrum":
            return SiteSolarAndVisibleSpectrum()
        if internal_name.lower() == "site:spectrumdata":
            return SiteSpectrumData()
        if internal_name.lower() == "scheduletypelimits":
            return ScheduleTypeLimits()
        if internal_name.lower() == "schedule:day:hourly":
            return ScheduleDayHourly()
        if internal_name.lower() == "schedule:day:interval":
            return ScheduleDayInterval()
        if internal_name.lower() == "schedule:day:list":
            return ScheduleDayList()
        if internal_name.lower() == "schedule:week:daily":
            return ScheduleWeekDaily()
        if internal_name.lower() == "schedule:week:compact":
            return ScheduleWeekCompact()
        if internal_name.lower() == "schedule:year":
            return ScheduleYear()
        if internal_name.lower() == "schedule:compact":
            return ScheduleCompact()
        if internal_name.lower() == "schedule:constant":
            return ScheduleConstant()
        if internal_name.lower() == "schedule:file":
            return ScheduleFile()
        if internal_name.lower() == "material":
            return Material()
        if internal_name.lower() == "material:nomass":
            return MaterialNoMass()
        if internal_name.lower() == "material:infraredtransparent":
            return MaterialInfraredTransparent()
        if internal_name.lower() == "material:airgap":
            return MaterialAirGap()
        if internal_name.lower() == "material:roofvegetation":
            return MaterialRoofVegetation()
        if internal_name.lower() == "windowmaterial:simpleglazingsystem":
            return WindowMaterialSimpleGlazingSystem()
        if internal_name.lower() == "windowmaterial:glazing":
            return WindowMaterialGlazing()
        if internal_name.lower() == "windowmaterial:glazinggroup:thermochromic":
            return WindowMaterialGlazingGroupThermochromic()
        if internal_name.lower() == "windowmaterial:glazing:refractionextinctionmethod":
            return WindowMaterialGlazingRefractionExtinctionMethod()
        if internal_name.lower() == "windowmaterial:gas":
            return WindowMaterialGas()
        if internal_name.lower() == "windowgap:supportpillar":
            return WindowGapSupportPillar()
        if internal_name.lower() == "windowgap:deflectionstate":
            return WindowGapDeflectionState()
        if internal_name.lower() == "windowmaterial:gasmixture":
            return WindowMaterialGasMixture()
        if internal_name.lower() == "windowmaterial:gap":
            return WindowMaterialGap()
        if internal_name.lower() == "windowmaterial:shade":
            return WindowMaterialShade()
        if internal_name.lower() == "windowmaterial:complexshade":
            return WindowMaterialComplexShade()
        if internal_name.lower() == "windowmaterial:blind":
            return WindowMaterialBlind()
        if internal_name.lower() == "windowmaterial:screen":
            return WindowMaterialScreen()
        if internal_name.lower() == "windowmaterial:shade:equivalentlayer":
            return WindowMaterialShadeEquivalentLayer()
        if internal_name.lower() == "windowmaterial:drape:equivalentlayer":
            return WindowMaterialDrapeEquivalentLayer()
        if internal_name.lower() == "windowmaterial:blind:equivalentlayer":
            return WindowMaterialBlindEquivalentLayer()
        if internal_name.lower() == "windowmaterial:screen:equivalentlayer":
            return WindowMaterialScreenEquivalentLayer()
        if internal_name.lower() == "windowmaterial:glazing:equivalentlayer":
            return WindowMaterialGlazingEquivalentLayer()
        if internal_name.lower() == "construction:windowequivalentlayer":
            return ConstructionWindowEquivalentLayer()
        if internal_name.lower() == "windowmaterial:gap:equivalentlayer":
            return WindowMaterialGapEquivalentLayer()
        if internal_name.lower() == "materialproperty:moisturepenetrationdepth:settings":
            return MaterialPropertyMoisturePenetrationDepthSettings()
        if internal_name.lower() == "materialproperty:phasechange":
            return MaterialPropertyPhaseChange()
        if internal_name.lower() == "materialproperty:variablethermalconductivity":
            return MaterialPropertyVariableThermalConductivity()
        if internal_name.lower() == "materialproperty:heatandmoisturetransfer:settings":
            return MaterialPropertyHeatAndMoistureTransferSettings()
        if internal_name.lower() == "materialproperty:heatandmoisturetransfer:sorptionisotherm":
            return MaterialPropertyHeatAndMoistureTransferSorptionIsotherm()
        if internal_name.lower() == "materialproperty:heatandmoisturetransfer:suction":
            return MaterialPropertyHeatAndMoistureTransferSuction()
        if internal_name.lower() == "materialproperty:heatandmoisturetransfer:redistribution":
            return MaterialPropertyHeatAndMoistureTransferRedistribution()
        if internal_name.lower() == "materialproperty:heatandmoisturetransfer:diffusion":
            return MaterialPropertyHeatAndMoistureTransferDiffusion()
        if internal_name.lower() == "materialproperty:heatandmoisturetransfer:thermalconductivity":
            return MaterialPropertyHeatAndMoistureTransferThermalConductivity()
        if internal_name.lower() == "materialproperty:glazingspectraldata":
            return MaterialPropertyGlazingSpectralData()
        if internal_name.lower() == "construction":
            return Construction()
        if internal_name.lower() == "construction:cfactorundergroundwall":
            return ConstructionCfactorUndergroundWall()
        if internal_name.lower() == "construction:ffactorgroundfloor":
            return ConstructionFfactorGroundFloor()
        if internal_name.lower() == "construction:internalsource":
            return ConstructionInternalSource()
        if internal_name.lower() == "windowthermalmodel:params":
            return WindowThermalModelParams()
        if internal_name.lower() == "construction:complexfenestrationstate":
            return ConstructionComplexFenestrationState()
        if internal_name.lower() == "construction:windowdatafile":
            return ConstructionWindowDataFile()
        if internal_name.lower() == "globalgeometryrules":
            return GlobalGeometryRules()
        if internal_name.lower() == "geometrytransform":
            return GeometryTransform()
        if internal_name.lower() == "zone":
            return Zone()
        if internal_name.lower() == "zonelist":
            return ZoneList()
        if internal_name.lower() == "zonegroup":
            return ZoneGroup()
        if internal_name.lower() == "buildingsurface:detailed":
            return BuildingSurfaceDetailed()
        if internal_name.lower() == "wall:detailed":
            return WallDetailed()
        if internal_name.lower() == "roofceiling:detailed":
            return RoofCeilingDetailed()
        if internal_name.lower() == "floor:detailed":
            return FloorDetailed()
        if internal_name.lower() == "wall:exterior":
            return WallExterior()
        if internal_name.lower() == "wall:adiabatic":
            return WallAdiabatic()
        if internal_name.lower() == "wall:underground":
            return WallUnderground()
        if internal_name.lower() == "wall:interzone":
            return WallInterzone()
        if internal_name.lower() == "roof":
            return Roof()
        if internal_name.lower() == "ceiling:adiabatic":
            return CeilingAdiabatic()
        if internal_name.lower() == "ceiling:interzone":
            return CeilingInterzone()
        if internal_name.lower() == "floor:groundcontact":
            return FloorGroundContact()
        if internal_name.lower() == "floor:adiabatic":
            return FloorAdiabatic()
        if internal_name.lower() == "floor:interzone":
            return FloorInterzone()
        if internal_name.lower() == "fenestrationsurface:detailed":
            return FenestrationSurfaceDetailed()
        if internal_name.lower() == "window":
            return Window()
        if internal_name.lower() == "door":
            return Door()
        if internal_name.lower() == "glazeddoor":
            return GlazedDoor()
        if internal_name.lower() == "window:interzone":
            return WindowInterzone()
        if internal_name.lower() == "door:interzone":
            return DoorInterzone()
        if internal_name.lower() == "glazeddoor:interzone":
            return GlazedDoorInterzone()
        if internal_name.lower() == "windowproperty:shadingcontrol":
            return WindowPropertyShadingControl()
        if internal_name.lower() == "windowproperty:frameanddivider":
            return WindowPropertyFrameAndDivider()
        if internal_name.lower() == "windowproperty:airflowcontrol":
            return WindowPropertyAirflowControl()
        if internal_name.lower() == "windowproperty:stormwindow":
            return WindowPropertyStormWindow()
        if internal_name.lower() == "internalmass":
            return InternalMass()
        if internal_name.lower() == "shading:site":
            return ShadingSite()
        if internal_name.lower() == "shading:building":
            return ShadingBuilding()
        if internal_name.lower() == "shading:site:detailed":
            return ShadingSiteDetailed()
        if internal_name.lower() == "shading:building:detailed":
            return ShadingBuildingDetailed()
        if internal_name.lower() == "shading:overhang":
            return ShadingOverhang()
        if internal_name.lower() == "shading:overhang:projection":
            return ShadingOverhangProjection()
        if internal_name.lower() == "shading:fin":
            return ShadingFin()
        if internal_name.lower() == "shading:fin:projection":
            return ShadingFinProjection()
        if internal_name.lower() == "shading:zone:detailed":
            return ShadingZoneDetailed()
        if internal_name.lower() == "shadingproperty:reflectance":
            return ShadingPropertyReflectance()
        if internal_name.lower() == "surfaceproperty:heattransferalgorithm":
            return SurfacePropertyHeatTransferAlgorithm()
        if internal_name.lower() == "surfaceproperty:heattransferalgorithm:multiplesurface":
            return SurfacePropertyHeatTransferAlgorithmMultipleSurface()
        if internal_name.lower() == "surfaceproperty:heattransferalgorithm:surfacelist":
            return SurfacePropertyHeatTransferAlgorithmSurfaceList()
        if internal_name.lower() == "surfaceproperty:heattransferalgorithm:construction":
            return SurfacePropertyHeatTransferAlgorithmConstruction()
        if internal_name.lower() == "surfacecontrol:movableinsulation":
            return SurfaceControlMovableInsulation()
        if internal_name.lower() == "surfaceproperty:othersidecoefficients":
            return SurfacePropertyOtherSideCoefficients()
        if internal_name.lower() == "surfaceproperty:othersideconditionsmodel":
            return SurfacePropertyOtherSideConditionsModel()
        if internal_name.lower() == "surfaceconvectionalgorithm:inside:adaptivemodelselections":
            return SurfaceConvectionAlgorithmInsideAdaptiveModelSelections()
        if internal_name.lower() == "surfaceconvectionalgorithm:outside:adaptivemodelselections":
            return SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections()
        if internal_name.lower() == "surfaceconvectionalgorithm:inside:usercurve":
            return SurfaceConvectionAlgorithmInsideUserCurve()
        if internal_name.lower() == "surfaceconvectionalgorithm:outside:usercurve":
            return SurfaceConvectionAlgorithmOutsideUserCurve()
        if internal_name.lower() == "surfaceproperty:convectioncoefficients":
            return SurfacePropertyConvectionCoefficients()
        if internal_name.lower() == "surfaceproperty:convectioncoefficients:multiplesurface":
            return SurfacePropertyConvectionCoefficientsMultipleSurface()
        if internal_name.lower() == "surfaceproperties:vaporcoefficients":
            return SurfacePropertiesVaporCoefficients()
        if internal_name.lower() == "surfaceproperty:exteriornaturalventedcavity":
            return SurfacePropertyExteriorNaturalVentedCavity()
        if internal_name.lower() == "surfaceproperty:solarincidentinside":
            return SurfacePropertySolarIncidentInside()
        if internal_name.lower() == "complexfenestrationproperty:solarabsorbedlayers":
            return ComplexFenestrationPropertySolarAbsorbedLayers()
        if internal_name.lower() == "zoneproperty:userviewfactors:bysurfacename":
            return ZonePropertyUserViewFactorsBySurfaceName()
        if internal_name.lower() == "groundheattransfer:control":
            return GroundHeatTransferControl()
        if internal_name.lower() == "groundheattransfer:slab:materials":
            return GroundHeatTransferSlabMaterials()
        if internal_name.lower() == "groundheattransfer:slab:matlprops":
            return GroundHeatTransferSlabMatlProps()
        if internal_name.lower() == "groundheattransfer:slab:boundconds":
            return GroundHeatTransferSlabBoundConds()
        if internal_name.lower() == "groundheattransfer:slab:bldgprops":
            return GroundHeatTransferSlabBldgProps()
        if internal_name.lower() == "groundheattransfer:slab:insulation":
            return GroundHeatTransferSlabInsulation()
        if internal_name.lower() == "groundheattransfer:slab:equivalentslab":
            return GroundHeatTransferSlabEquivalentSlab()
        if internal_name.lower() == "groundheattransfer:slab:autogrid":
            return GroundHeatTransferSlabAutoGrid()
        if internal_name.lower() == "groundheattransfer:slab:manualgrid":
            return GroundHeatTransferSlabManualGrid()
        if internal_name.lower() == "groundheattransfer:slab:xface":
            return GroundHeatTransferSlabXface()
        if internal_name.lower() == "groundheattransfer:slab:yface":
            return GroundHeatTransferSlabYface()
        if internal_name.lower() == "groundheattransfer:slab:zface":
            return GroundHeatTransferSlabZface()
        if internal_name.lower() == "groundheattransfer:basement:simparameters":
            return GroundHeatTransferBasementSimParameters()
        if internal_name.lower() == "groundheattransfer:basement:matlprops":
            return GroundHeatTransferBasementMatlProps()
        if internal_name.lower() == "groundheattransfer:basement:insulation":
            return GroundHeatTransferBasementInsulation()
        if internal_name.lower() == "groundheattransfer:basement:surfaceprops":
            return GroundHeatTransferBasementSurfaceProps()
        if internal_name.lower() == "groundheattransfer:basement:bldgdata":
            return GroundHeatTransferBasementBldgData()
        if internal_name.lower() == "groundheattransfer:basement:interior":
            return GroundHeatTransferBasementInterior()
        if internal_name.lower() == "groundheattransfer:basement:combldg":
            return GroundHeatTransferBasementComBldg()
        if internal_name.lower() == "groundheattransfer:basement:equivslab":
            return GroundHeatTransferBasementEquivSlab()
        if internal_name.lower() == "groundheattransfer:basement:equivautogrid":
            return GroundHeatTransferBasementEquivAutoGrid()
        if internal_name.lower() == "groundheattransfer:basement:autogrid":
            return GroundHeatTransferBasementAutoGrid()
        if internal_name.lower() == "groundheattransfer:basement:manualgrid":
            return GroundHeatTransferBasementManualGrid()
        if internal_name.lower() == "groundheattransfer:basement:xface":
            return GroundHeatTransferBasementXface()
        if internal_name.lower() == "groundheattransfer:basement:yface":
            return GroundHeatTransferBasementYface()
        if internal_name.lower() == "groundheattransfer:basement:zface":
            return GroundHeatTransferBasementZface()
        if internal_name.lower() == "roomairmodeltype":
            return RoomAirModelType()
        if internal_name.lower() == "roomair:temperaturepattern:userdefined":
            return RoomAirTemperaturePatternUserDefined()
        if internal_name.lower() == "roomair:temperaturepattern:constantgradient":
            return RoomAirTemperaturePatternConstantGradient()
        if internal_name.lower() == "roomair:temperaturepattern:twogradient":
            return RoomAirTemperaturePatternTwoGradient()
        if internal_name.lower() == "roomair:temperaturepattern:nondimensionalheight":
            return RoomAirTemperaturePatternNondimensionalHeight()
        if internal_name.lower() == "roomair:temperaturepattern:surfacemapping":
            return RoomAirTemperaturePatternSurfaceMapping()
        if internal_name.lower() == "roomair:node":
            return RoomAirNode()
        if internal_name.lower() == "roomairsettings:onenodedisplacementventilation":
            return RoomAirSettingsOneNodeDisplacementVentilation()
        if internal_name.lower() == "roomairsettings:threenodedisplacementventilation":
            return RoomAirSettingsThreeNodeDisplacementVentilation()
        if internal_name.lower() == "roomairsettings:crossventilation":
            return RoomAirSettingsCrossVentilation()
        if internal_name.lower() == "roomairsettings:underfloorairdistributioninterior":
            return RoomAirSettingsUnderFloorAirDistributionInterior()
        if internal_name.lower() == "roomairsettings:underfloorairdistributionexterior":
            return RoomAirSettingsUnderFloorAirDistributionExterior()
        if internal_name.lower() == "people":
            return People()
        if internal_name.lower() == "comfortviewfactorangles":
            return ComfortViewFactorAngles()
        if internal_name.lower() == "lights":
            return Lights()
        if internal_name.lower() == "electricequipment":
            return ElectricEquipment()
        if internal_name.lower() == "gasequipment":
            return GasEquipment()
        if internal_name.lower() == "hotwaterequipment":
            return HotWaterEquipment()
        if internal_name.lower() == "steamequipment":
            return SteamEquipment()
        if internal_name.lower() == "otherequipment":
            return OtherEquipment()
        if internal_name.lower() == "zonebaseboard:outdoortemperaturecontrolled":
            return ZoneBaseboardOutdoorTemperatureControlled()
        if internal_name.lower() == "zonecontaminantsourceandsink:carbondioxide":
            return ZoneContaminantSourceAndSinkCarbonDioxide()
        if internal_name.lower() == "zonecontaminantsourceandsink:generic:constant":
            return ZoneContaminantSourceAndSinkGenericConstant()
        if internal_name.lower() == "surfacecontaminantsourceandsink:generic:pressuredriven":
            return SurfaceContaminantSourceAndSinkGenericPressureDriven()
        if internal_name.lower() == "zonecontaminantsourceandsink:generic:cutoffmodel":
            return ZoneContaminantSourceAndSinkGenericCutoffModel()
        if internal_name.lower() == "zonecontaminantsourceandsink:generic:decaysource":
            return ZoneContaminantSourceAndSinkGenericDecaySource()
        if internal_name.lower() == "surfacecontaminantsourceandsink:generic:boundarylayerdiffusion":
            return SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion()
        if internal_name.lower() == "surfacecontaminantsourceandsink:generic:depositionvelocitysink":
            return SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink()
        if internal_name.lower() == "zonecontaminantsourceandsink:generic:depositionratesink":
            return ZoneContaminantSourceAndSinkGenericDepositionRateSink()
        if internal_name.lower() == "daylighting:controls":
            return DaylightingControls()
        if internal_name.lower() == "daylighting:delight:controls":
            return DaylightingDelightControls()
        if internal_name.lower() == "daylighting:delight:referencepoint":
            return DaylightingDelightReferencePoint()
        if internal_name.lower() == "daylighting:delight:complexfenestration":
            return DaylightingDelightComplexFenestration()
        if internal_name.lower() == "daylightingdevice:tubular":
            return DaylightingDeviceTubular()
        if internal_name.lower() == "daylightingdevice:shelf":
            return DaylightingDeviceShelf()
        if internal_name.lower() == "daylightingdevice:lightwell":
            return DaylightingDeviceLightWell()
        if internal_name.lower() == "output:daylightfactors":
            return OutputDaylightFactors()
        if internal_name.lower() == "output:illuminancemap":
            return OutputIlluminanceMap()
        if internal_name.lower() == "outputcontrol:illuminancemap:style":
            return OutputControlIlluminanceMapStyle()
        if internal_name.lower() == "zoneinfiltration:designflowrate":
            return ZoneInfiltrationDesignFlowRate()
        if internal_name.lower() == "zoneinfiltration:effectiveleakagearea":
            return ZoneInfiltrationEffectiveLeakageArea()
        if internal_name.lower() == "zoneinfiltration:flowcoefficient":
            return ZoneInfiltrationFlowCoefficient()
        if internal_name.lower() == "zoneventilation:designflowrate":
            return ZoneVentilationDesignFlowRate()
        if internal_name.lower() == "zoneventilation:windandstackopenarea":
            return ZoneVentilationWindandStackOpenArea()
        if internal_name.lower() == "zoneairbalance:outdoorair":
            return ZoneAirBalanceOutdoorAir()
        if internal_name.lower() == "zonemixing":
            return ZoneMixing()
        if internal_name.lower() == "zonecrossmixing":
            return ZoneCrossMixing()
        if internal_name.lower() == "zonerefrigerationdoormixing":
            return ZoneRefrigerationDoorMixing()
        if internal_name.lower() == "zoneearthtube":
            return ZoneEarthtube()
        if internal_name.lower() == "zonecooltower:shower":
            return ZoneCoolTowerShower()
        if internal_name.lower() == "zonethermalchimney":
            return ZoneThermalChimney()
        if internal_name.lower() == "airflownetwork:simulationcontrol":
            return AirflowNetworkSimulationControl()
        if internal_name.lower() == "airflownetwork:multizone:zone":
            return AirflowNetworkMultiZoneZone()
        if internal_name.lower() == "airflownetwork:multizone:surface":
            return AirflowNetworkMultiZoneSurface()
        if internal_name.lower() == "airflownetwork:multizone:referencecrackconditions":
            return AirflowNetworkMultiZoneReferenceCrackConditions()
        if internal_name.lower() == "airflownetwork:multizone:surface:crack":
            return AirflowNetworkMultiZoneSurfaceCrack()
        if internal_name.lower() == "airflownetwork:multizone:surface:effectiveleakagearea":
            return AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea()
        if internal_name.lower() == "airflownetwork:multizone:component:detailedopening":
            return AirflowNetworkMultiZoneComponentDetailedOpening()
        if internal_name.lower() == "airflownetwork:multizone:component:simpleopening":
            return AirflowNetworkMultiZoneComponentSimpleOpening()
        if internal_name.lower() == "airflownetwork:multizone:component:horizontalopening":
            return AirflowNetworkMultiZoneComponentHorizontalOpening()
        if internal_name.lower() == "airflownetwork:multizone:component:zoneexhaustfan":
            return AirflowNetworkMultiZoneComponentZoneExhaustFan()
        if internal_name.lower() == "airflownetwork:multizone:externalnode":
            return AirflowNetworkMultiZoneExternalNode()
        if internal_name.lower() == "airflownetwork:multizone:windpressurecoefficientarray":
            return AirflowNetworkMultiZoneWindPressureCoefficientArray()
        if internal_name.lower() == "airflownetwork:multizone:windpressurecoefficientvalues":
            return AirflowNetworkMultiZoneWindPressureCoefficientValues()
        if internal_name.lower() == "airflownetwork:distribution:node":
            return AirflowNetworkDistributionNode()
        if internal_name.lower() == "airflownetwork:distribution:component:leak":
            return AirflowNetworkDistributionComponentLeak()
        if internal_name.lower() == "airflownetwork:distribution:component:leakageratio":
            return AirflowNetworkDistributionComponentLeakageRatio()
        if internal_name.lower() == "airflownetwork:distribution:component:duct":
            return AirflowNetworkDistributionComponentDuct()
        if internal_name.lower() == "airflownetwork:distribution:component:fan":
            return AirflowNetworkDistributionComponentFan()
        if internal_name.lower() == "airflownetwork:distribution:component:coil":
            return AirflowNetworkDistributionComponentCoil()
        if internal_name.lower() == "airflownetwork:distribution:component:heatexchanger":
            return AirflowNetworkDistributionComponentHeatExchanger()
        if internal_name.lower() == "airflownetwork:distribution:component:terminalunit":
            return AirflowNetworkDistributionComponentTerminalUnit()
        if internal_name.lower() == "airflownetwork:distribution:component:constantpressuredrop":
            return AirflowNetworkDistributionComponentConstantPressureDrop()
        if internal_name.lower() == "airflownetwork:distribution:linkage":
            return AirflowNetworkDistributionLinkage()
        if internal_name.lower() == "exterior:lights":
            return ExteriorLights()
        if internal_name.lower() == "exterior:fuelequipment":
            return ExteriorFuelEquipment()
        if internal_name.lower() == "exterior:waterequipment":
            return ExteriorWaterEquipment()
        if internal_name.lower() == "hvactemplate:thermostat":
            return HvactemplateThermostat()
        if internal_name.lower() == "hvactemplate:zone:idealloadsairsystem":
            return HvactemplateZoneIdealLoadsAirSystem()
        if internal_name.lower() == "hvactemplate:zone:baseboardheat":
            return HvactemplateZoneBaseboardHeat()
        if internal_name.lower() == "hvactemplate:zone:fancoil":
            return HvactemplateZoneFanCoil()
        if internal_name.lower() == "hvactemplate:zone:ptac":
            return HvactemplateZonePtac()
        if internal_name.lower() == "hvactemplate:zone:pthp":
            return HvactemplateZonePthp()
        if internal_name.lower() == "hvactemplate:zone:watertoairheatpump":
            return HvactemplateZoneWaterToAirHeatPump()
        if internal_name.lower() == "hvactemplate:zone:vrf":
            return HvactemplateZoneVrf()
        if internal_name.lower() == "hvactemplate:zone:unitary":
            return HvactemplateZoneUnitary()
        if internal_name.lower() == "hvactemplate:zone:vav":
            return HvactemplateZoneVav()
        if internal_name.lower() == "hvactemplate:zone:vav:fanpowered":
            return HvactemplateZoneVavFanPowered()
        if internal_name.lower() == "hvactemplate:zone:vav:heatandcool":
            return HvactemplateZoneVavHeatAndCool()
        if internal_name.lower() == "hvactemplate:zone:constantvolume":
            return HvactemplateZoneConstantVolume()
        if internal_name.lower() == "hvactemplate:zone:dualduct":
            return HvactemplateZoneDualDuct()
        if internal_name.lower() == "hvactemplate:system:vrf":
            return HvactemplateSystemVrf()
        if internal_name.lower() == "hvactemplate:system:unitary":
            return HvactemplateSystemUnitary()
        if internal_name.lower() == "hvactemplate:system:unitaryheatpump:airtoair":
            return HvactemplateSystemUnitaryHeatPumpAirToAir()
        if internal_name.lower() == "hvactemplate:system:unitarysystem":
            return HvactemplateSystemUnitarySystem()
        if internal_name.lower() == "hvactemplate:system:vav":
            return HvactemplateSystemVav()
        if internal_name.lower() == "hvactemplate:system:packagedvav":
            return HvactemplateSystemPackagedVav()
        if internal_name.lower() == "hvactemplate:system:constantvolume":
            return HvactemplateSystemConstantVolume()
        if internal_name.lower() == "hvactemplate:system:dualduct":
            return HvactemplateSystemDualDuct()
        if internal_name.lower() == "hvactemplate:system:dedicatedoutdoorair":
            return HvactemplateSystemDedicatedOutdoorAir()
        if internal_name.lower() == "hvactemplate:plant:chilledwaterloop":
            return HvactemplatePlantChilledWaterLoop()
        if internal_name.lower() == "hvactemplate:plant:chiller":
            return HvactemplatePlantChiller()
        if internal_name.lower() == "hvactemplate:plant:chiller:objectreference":
            return HvactemplatePlantChillerObjectReference()
        if internal_name.lower() == "hvactemplate:plant:tower":
            return HvactemplatePlantTower()
        if internal_name.lower() == "hvactemplate:plant:tower:objectreference":
            return HvactemplatePlantTowerObjectReference()
        if internal_name.lower() == "hvactemplate:plant:hotwaterloop":
            return HvactemplatePlantHotWaterLoop()
        if internal_name.lower() == "hvactemplate:plant:boiler":
            return HvactemplatePlantBoiler()
        if internal_name.lower() == "hvactemplate:plant:boiler:objectreference":
            return HvactemplatePlantBoilerObjectReference()
        if internal_name.lower() == "hvactemplate:plant:mixedwaterloop":
            return HvactemplatePlantMixedWaterLoop()
        if internal_name.lower() == "designspecification:outdoorair":
            return DesignSpecificationOutdoorAir()
        if internal_name.lower() == "designspecification:zoneairdistribution":
            return DesignSpecificationZoneAirDistribution()
        if internal_name.lower() == "sizing:parameters":
            return SizingParameters()
        if internal_name.lower() == "sizing:zone":
            return SizingZone()
        if internal_name.lower() == "designspecification:zonehvac:sizing":
            return DesignSpecificationZoneHvacSizing()
        if internal_name.lower() == "sizing:system":
            return SizingSystem()
        if internal_name.lower() == "sizing:plant":
            return SizingPlant()
        if internal_name.lower() == "outputcontrol:sizing:style":
            return OutputControlSizingStyle()
        if internal_name.lower() == "zonecontrol:humidistat":
            return ZoneControlHumidistat()
        if internal_name.lower() == "zonecontrol:thermostat":
            return ZoneControlThermostat()
        if internal_name.lower() == "zonecontrol:thermostat:operativetemperature":
            return ZoneControlThermostatOperativeTemperature()
        if internal_name.lower() == "zonecontrol:thermostat:thermalcomfort":
            return ZoneControlThermostatThermalComfort()
        if internal_name.lower() == "zonecontrol:thermostat:temperatureandhumidity":
            return ZoneControlThermostatTemperatureAndHumidity()
        if internal_name.lower() == "thermostatsetpoint:singleheating":
            return ThermostatSetpointSingleHeating()
        if internal_name.lower() == "thermostatsetpoint:singlecooling":
            return ThermostatSetpointSingleCooling()
        if internal_name.lower() == "thermostatsetpoint:singleheatingorcooling":
            return ThermostatSetpointSingleHeatingOrCooling()
        if internal_name.lower() == "thermostatsetpoint:dualsetpoint":
            return ThermostatSetpointDualSetpoint()
        if internal_name.lower() == "thermostatsetpoint:thermalcomfort:fanger:singleheating":
            return ThermostatSetpointThermalComfortFangerSingleHeating()
        if internal_name.lower() == "thermostatsetpoint:thermalcomfort:fanger:singlecooling":
            return ThermostatSetpointThermalComfortFangerSingleCooling()
        if internal_name.lower() == "thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling":
            return ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling()
        if internal_name.lower() == "thermostatsetpoint:thermalcomfort:fanger:dualsetpoint":
            return ThermostatSetpointThermalComfortFangerDualSetpoint()
        if internal_name.lower() == "zonecontrol:thermostat:stageddualsetpoint":
            return ZoneControlThermostatStagedDualSetpoint()
        if internal_name.lower() == "zonecontrol:contaminantcontroller":
            return ZoneControlContaminantController()
        if internal_name.lower() == "zonehvac:idealloadsairsystem":
            return ZoneHvacIdealLoadsAirSystem()
        if internal_name.lower() == "zonehvac:fourpipefancoil":
            return ZoneHvacFourPipeFanCoil()
        if internal_name.lower() == "zonehvac:windowairconditioner":
            return ZoneHvacWindowAirConditioner()
        if internal_name.lower() == "zonehvac:packagedterminalairconditioner":
            return ZoneHvacPackagedTerminalAirConditioner()
        if internal_name.lower() == "zonehvac:packagedterminalheatpump":
            return ZoneHvacPackagedTerminalHeatPump()
        if internal_name.lower() == "zonehvac:watertoairheatpump":
            return ZoneHvacWaterToAirHeatPump()
        if internal_name.lower() == "zonehvac:dehumidifier:dx":
            return ZoneHvacDehumidifierDx()
        if internal_name.lower() == "zonehvac:energyrecoveryventilator":
            return ZoneHvacEnergyRecoveryVentilator()
        if internal_name.lower() == "zonehvac:energyrecoveryventilator:controller":
            return ZoneHvacEnergyRecoveryVentilatorController()
        if internal_name.lower() == "zonehvac:unitventilator":
            return ZoneHvacUnitVentilator()
        if internal_name.lower() == "zonehvac:unitheater":
            return ZoneHvacUnitHeater()
        if internal_name.lower() == "zonehvac:evaporativecoolerunit":
            return ZoneHvacEvaporativeCoolerUnit()
        if internal_name.lower() == "zonehvac:outdoorairunit":
            return ZoneHvacOutdoorAirUnit()
        if internal_name.lower() == "zonehvac:outdoorairunit:equipmentlist":
            return ZoneHvacOutdoorAirUnitEquipmentList()
        if internal_name.lower() == "zonehvac:terminalunit:variablerefrigerantflow":
            return ZoneHvacTerminalUnitVariableRefrigerantFlow()
        if internal_name.lower() == "zonehvac:baseboard:radiantconvective:water":
            return ZoneHvacBaseboardRadiantConvectiveWater()
        if internal_name.lower() == "zonehvac:baseboard:radiantconvective:steam":
            return ZoneHvacBaseboardRadiantConvectiveSteam()
        if internal_name.lower() == "zonehvac:baseboard:radiantconvective:electric":
            return ZoneHvacBaseboardRadiantConvectiveElectric()
        if internal_name.lower() == "zonehvac:baseboard:convective:water":
            return ZoneHvacBaseboardConvectiveWater()
        if internal_name.lower() == "zonehvac:baseboard:convective:electric":
            return ZoneHvacBaseboardConvectiveElectric()
        if internal_name.lower() == "zonehvac:lowtemperatureradiant:variableflow":
            return ZoneHvacLowTemperatureRadiantVariableFlow()
        if internal_name.lower() == "zonehvac:lowtemperatureradiant:constantflow":
            return ZoneHvacLowTemperatureRadiantConstantFlow()
        if internal_name.lower() == "zonehvac:lowtemperatureradiant:electric":
            return ZoneHvacLowTemperatureRadiantElectric()
        if internal_name.lower() == "zonehvac:lowtemperatureradiant:surfacegroup":
            return ZoneHvacLowTemperatureRadiantSurfaceGroup()
        if internal_name.lower() == "zonehvac:hightemperatureradiant":
            return ZoneHvacHighTemperatureRadiant()
        if internal_name.lower() == "zonehvac:ventilatedslab":
            return ZoneHvacVentilatedSlab()
        if internal_name.lower() == "zonehvac:ventilatedslab:slabgroup":
            return ZoneHvacVentilatedSlabSlabGroup()
        if internal_name.lower() == "airterminal:singleduct:uncontrolled":
            return AirTerminalSingleDuctUncontrolled()
        if internal_name.lower() == "airterminal:singleduct:constantvolume:reheat":
            return AirTerminalSingleDuctConstantVolumeReheat()
        if internal_name.lower() == "airterminal:singleduct:vav:noreheat":
            return AirTerminalSingleDuctVavNoReheat()
        if internal_name.lower() == "airterminal:singleduct:vav:reheat":
            return AirTerminalSingleDuctVavReheat()
        if internal_name.lower() == "airterminal:singleduct:vav:reheat:variablespeedfan":
            return AirTerminalSingleDuctVavReheatVariableSpeedFan()
        if internal_name.lower() == "airterminal:singleduct:vav:heatandcool:noreheat":
            return AirTerminalSingleDuctVavHeatAndCoolNoReheat()
        if internal_name.lower() == "airterminal:singleduct:vav:heatandcool:reheat":
            return AirTerminalSingleDuctVavHeatAndCoolReheat()
        if internal_name.lower() == "airterminal:singleduct:seriespiu:reheat":
            return AirTerminalSingleDuctSeriesPiuReheat()
        if internal_name.lower() == "airterminal:singleduct:parallelpiu:reheat":
            return AirTerminalSingleDuctParallelPiuReheat()
        if internal_name.lower() == "airterminal:singleduct:constantvolume:fourpipeinduction":
            return AirTerminalSingleDuctConstantVolumeFourPipeInduction()
        if internal_name.lower() == "airterminal:singleduct:constantvolume:cooledbeam":
            return AirTerminalSingleDuctConstantVolumeCooledBeam()
        if internal_name.lower() == "airterminal:singleduct:inletsidemixer":
            return AirTerminalSingleDuctInletSideMixer()
        if internal_name.lower() == "airterminal:singleduct:supplysidemixer":
            return AirTerminalSingleDuctSupplySideMixer()
        if internal_name.lower() == "airterminal:dualduct:constantvolume":
            return AirTerminalDualDuctConstantVolume()
        if internal_name.lower() == "airterminal:dualduct:vav":
            return AirTerminalDualDuctVav()
        if internal_name.lower() == "airterminal:dualduct:vav:outdoorair":
            return AirTerminalDualDuctVavOutdoorAir()
        if internal_name.lower() == "zonehvac:airdistributionunit":
            return ZoneHvacAirDistributionUnit()
        if internal_name.lower() == "zonehvac:equipmentlist":
            return ZoneHvacEquipmentList()
        if internal_name.lower() == "zonehvac:equipmentconnections":
            return ZoneHvacEquipmentConnections()
        if internal_name.lower() == "fan:constantvolume":
            return FanConstantVolume()
        if internal_name.lower() == "fan:variablevolume":
            return FanVariableVolume()
        if internal_name.lower() == "fan:onoff":
            return FanOnOff()
        if internal_name.lower() == "fan:zoneexhaust":
            return FanZoneExhaust()
        if internal_name.lower() == "fanperformance:nightventilation":
            return FanPerformanceNightVentilation()
        if internal_name.lower() == "fan:componentmodel":
            return FanComponentModel()
        if internal_name.lower() == "coil:cooling:water":
            return CoilCoolingWater()
        if internal_name.lower() == "coil:cooling:water:detailedgeometry":
            return CoilCoolingWaterDetailedGeometry()
        if internal_name.lower() == "coil:cooling:dx:singlespeed":
            return CoilCoolingDxSingleSpeed()
        if internal_name.lower() == "coil:cooling:dx:twospeed":
            return CoilCoolingDxTwoSpeed()
        if internal_name.lower() == "coil:cooling:dx:multispeed":
            return CoilCoolingDxMultiSpeed()
        if internal_name.lower() == "coil:cooling:dx:variablespeed":
            return CoilCoolingDxVariableSpeed()
        if internal_name.lower() == "coil:cooling:dx:twostagewithhumiditycontrolmode":
            return CoilCoolingDxTwoStageWithHumidityControlMode()
        if internal_name.lower() == "coilperformance:dx:cooling":
            return CoilPerformanceDxCooling()
        if internal_name.lower() == "coil:cooling:dx:variablerefrigerantflow":
            return CoilCoolingDxVariableRefrigerantFlow()
        if internal_name.lower() == "coil:heating:dx:variablerefrigerantflow":
            return CoilHeatingDxVariableRefrigerantFlow()
        if internal_name.lower() == "coil:heating:water":
            return CoilHeatingWater()
        if internal_name.lower() == "coil:heating:steam":
            return CoilHeatingSteam()
        if internal_name.lower() == "coil:heating:electric":
            return CoilHeatingElectric()
        if internal_name.lower() == "coil:heating:electric:multistage":
            return CoilHeatingElectricMultiStage()
        if internal_name.lower() == "coil:heating:gas":
            return CoilHeatingGas()
        if internal_name.lower() == "coil:heating:gas:multistage":
            return CoilHeatingGasMultiStage()
        if internal_name.lower() == "coil:heating:desuperheater":
            return CoilHeatingDesuperheater()
        if internal_name.lower() == "coil:heating:dx:singlespeed":
            return CoilHeatingDxSingleSpeed()
        if internal_name.lower() == "coil:heating:dx:multispeed":
            return CoilHeatingDxMultiSpeed()
        if internal_name.lower() == "coil:heating:dx:variablespeed":
            return CoilHeatingDxVariableSpeed()
        if internal_name.lower() == "coil:cooling:watertoairheatpump:parameterestimation":
            return CoilCoolingWaterToAirHeatPumpParameterEstimation()
        if internal_name.lower() == "coil:heating:watertoairheatpump:parameterestimation":
            return CoilHeatingWaterToAirHeatPumpParameterEstimation()
        if internal_name.lower() == "coil:cooling:watertoairheatpump:equationfit":
            return CoilCoolingWaterToAirHeatPumpEquationFit()
        if internal_name.lower() == "coil:cooling:watertoairheatpump:variablespeedequationfit":
            return CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit()
        if internal_name.lower() == "coil:heating:watertoairheatpump:equationfit":
            return CoilHeatingWaterToAirHeatPumpEquationFit()
        if internal_name.lower() == "coil:heating:watertoairheatpump:variablespeedequationfit":
            return CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit()
        if internal_name.lower() == "coil:waterheating:airtowaterheatpump":
            return CoilWaterHeatingAirToWaterHeatPump()
        if internal_name.lower() == "coil:waterheating:desuperheater":
            return CoilWaterHeatingDesuperheater()
        if internal_name.lower() == "coilsystem:cooling:dx":
            return CoilSystemCoolingDx()
        if internal_name.lower() == "coilsystem:heating:dx":
            return CoilSystemHeatingDx()
        if internal_name.lower() == "coilsystem:cooling:water:heatexchangerassisted":
            return CoilSystemCoolingWaterHeatExchangerAssisted()
        if internal_name.lower() == "coilsystem:cooling:dx:heatexchangerassisted":
            return CoilSystemCoolingDxHeatExchangerAssisted()
        if internal_name.lower() == "coil:cooling:dx:singlespeed:thermalstorage":
            return CoilCoolingDxSingleSpeedThermalStorage()
        if internal_name.lower() == "evaporativecooler:direct:celdekpad":
            return EvaporativeCoolerDirectCelDekPad()
        if internal_name.lower() == "evaporativecooler:indirect:celdekpad":
            return EvaporativeCoolerIndirectCelDekPad()
        if internal_name.lower() == "evaporativecooler:indirect:wetcoil":
            return EvaporativeCoolerIndirectWetCoil()
        if internal_name.lower() == "evaporativecooler:indirect:researchspecial":
            return EvaporativeCoolerIndirectResearchSpecial()
        if internal_name.lower() == "evaporativecooler:direct:researchspecial":
            return EvaporativeCoolerDirectResearchSpecial()
        if internal_name.lower() == "humidifier:steam:electric":
            return HumidifierSteamElectric()
        if internal_name.lower() == "dehumidifier:desiccant:nofans":
            return DehumidifierDesiccantNoFans()
        if internal_name.lower() == "dehumidifier:desiccant:system":
            return DehumidifierDesiccantSystem()
        if internal_name.lower() == "heatexchanger:airtoair:flatplate":
            return HeatExchangerAirToAirFlatPlate()
        if internal_name.lower() == "heatexchanger:airtoair:sensibleandlatent":
            return HeatExchangerAirToAirSensibleAndLatent()
        if internal_name.lower() == "heatexchanger:desiccant:balancedflow":
            return HeatExchangerDesiccantBalancedFlow()
        if internal_name.lower() == "heatexchanger:desiccant:balancedflow:performancedatatype1":
            return HeatExchangerDesiccantBalancedFlowPerformanceDataType1()
        if internal_name.lower() == "airloophvac:unitarysystem":
            return AirLoopHvacUnitarySystem()
        if internal_name.lower() == "unitarysystemperformance:heatpump:multispeed":
            return UnitarySystemPerformanceHeatPumpMultispeed()
        if internal_name.lower() == "airloophvac:unitary:furnace:heatonly":
            return AirLoopHvacUnitaryFurnaceHeatOnly()
        if internal_name.lower() == "airloophvac:unitary:furnace:heatcool":
            return AirLoopHvacUnitaryFurnaceHeatCool()
        if internal_name.lower() == "airloophvac:unitaryheatonly":
            return AirLoopHvacUnitaryHeatOnly()
        if internal_name.lower() == "airloophvac:unitaryheatcool":
            return AirLoopHvacUnitaryHeatCool()
        if internal_name.lower() == "airloophvac:unitaryheatpump:airtoair":
            return AirLoopHvacUnitaryHeatPumpAirToAir()
        if internal_name.lower() == "airloophvac:unitaryheatpump:watertoair":
            return AirLoopHvacUnitaryHeatPumpWaterToAir()
        if internal_name.lower() == "airloophvac:unitaryheatcool:vavchangeoverbypass":
            return AirLoopHvacUnitaryHeatCoolVavchangeoverBypass()
        if internal_name.lower() == "airloophvac:unitaryheatpump:airtoair:multispeed":
            return AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed()
        if internal_name.lower() == "airconditioner:variablerefrigerantflow":
            return AirConditionerVariableRefrigerantFlow()
        if internal_name.lower() == "zoneterminalunitlist":
            return ZoneTerminalUnitList()
        if internal_name.lower() == "controller:watercoil":
            return ControllerWaterCoil()
        if internal_name.lower() == "controller:outdoorair":
            return ControllerOutdoorAir()
        if internal_name.lower() == "controller:mechanicalventilation":
            return ControllerMechanicalVentilation()
        if internal_name.lower() == "airloophvac:controllerlist":
            return AirLoopHvacControllerList()
        if internal_name.lower() == "airloophvac":
            return AirLoopHvac()
        if internal_name.lower() == "airloophvac:outdoorairsystem:equipmentlist":
            return AirLoopHvacOutdoorAirSystemEquipmentList()
        if internal_name.lower() == "airloophvac:outdoorairsystem":
            return AirLoopHvacOutdoorAirSystem()
        if internal_name.lower() == "outdoorair:mixer":
            return OutdoorAirMixer()
        if internal_name.lower() == "airloophvac:zonesplitter":
            return AirLoopHvacZoneSplitter()
        if internal_name.lower() == "airloophvac:supplyplenum":
            return AirLoopHvacSupplyPlenum()
        if internal_name.lower() == "airloophvac:supplypath":
            return AirLoopHvacSupplyPath()
        if internal_name.lower() == "airloophvac:zonemixer":
            return AirLoopHvacZoneMixer()
        if internal_name.lower() == "airloophvac:returnplenum":
            return AirLoopHvacReturnPlenum()
        if internal_name.lower() == "airloophvac:returnpath":
            return AirLoopHvacReturnPath()
        if internal_name.lower() == "branch":
            return Branch()
        if internal_name.lower() == "branchlist":
            return BranchList()
        if internal_name.lower() == "connector:splitter":
            return ConnectorSplitter()
        if internal_name.lower() == "connector:mixer":
            return ConnectorMixer()
        if internal_name.lower() == "connectorlist":
            return ConnectorList()
        if internal_name.lower() == "nodelist":
            return NodeList()
        if internal_name.lower() == "outdoorair:node":
            return OutdoorAirNode()
        if internal_name.lower() == "outdoorair:nodelist":
            return OutdoorAirNodeList()
        if internal_name.lower() == "pipe:adiabatic":
            return PipeAdiabatic()
        if internal_name.lower() == "pipe:adiabatic:steam":
            return PipeAdiabaticSteam()
        if internal_name.lower() == "pipe:indoor":
            return PipeIndoor()
        if internal_name.lower() == "pipe:outdoor":
            return PipeOutdoor()
        if internal_name.lower() == "pipe:underground":
            return PipeUnderground()
        if internal_name.lower() == "pipingsystem:underground:domain":
            return PipingSystemUndergroundDomain()
        if internal_name.lower() == "pipingsystem:underground:pipecircuit":
            return PipingSystemUndergroundPipeCircuit()
        if internal_name.lower() == "pipingsystem:underground:pipesegment":
            return PipingSystemUndergroundPipeSegment()
        if internal_name.lower() == "duct":
            return Duct()
        if internal_name.lower() == "pump:variablespeed":
            return PumpVariableSpeed()
        if internal_name.lower() == "pump:constantspeed":
            return PumpConstantSpeed()
        if internal_name.lower() == "pump:variablespeed:condensate":
            return PumpVariableSpeedCondensate()
        if internal_name.lower() == "headeredpumps:constantspeed":
            return HeaderedPumpsConstantSpeed()
        if internal_name.lower() == "headeredpumps:variablespeed":
            return HeaderedPumpsVariableSpeed()
        if internal_name.lower() == "temperingvalve":
            return TemperingValve()
        if internal_name.lower() == "loadprofile:plant":
            return LoadProfilePlant()
        if internal_name.lower() == "solarcollectorperformance:flatplate":
            return SolarCollectorPerformanceFlatPlate()
        if internal_name.lower() == "solarcollector:flatplate:water":
            return SolarCollectorFlatPlateWater()
        if internal_name.lower() == "solarcollector:flatplate:photovoltaicthermal":
            return SolarCollectorFlatPlatePhotovoltaicThermal()
        if internal_name.lower() == "solarcollectorperformance:photovoltaicthermal:simple":
            return SolarCollectorPerformancePhotovoltaicThermalSimple()
        if internal_name.lower() == "solarcollector:integralcollectorstorage":
            return SolarCollectorIntegralCollectorStorage()
        if internal_name.lower() == "solarcollectorperformance:integralcollectorstorage":
            return SolarCollectorPerformanceIntegralCollectorStorage()
        if internal_name.lower() == "solarcollector:unglazedtranspired":
            return SolarCollectorUnglazedTranspired()
        if internal_name.lower() == "solarcollector:unglazedtranspired:multisystem":
            return SolarCollectorUnglazedTranspiredMultisystem()
        if internal_name.lower() == "boiler:hotwater":
            return BoilerHotWater()
        if internal_name.lower() == "boiler:steam":
            return BoilerSteam()
        if internal_name.lower() == "chiller:electric:eir":
            return ChillerElectricEir()
        if internal_name.lower() == "chiller:electric:reformulatedeir":
            return ChillerElectricReformulatedEir()
        if internal_name.lower() == "chiller:electric":
            return ChillerElectric()
        if internal_name.lower() == "chiller:absorption:indirect":
            return ChillerAbsorptionIndirect()
        if internal_name.lower() == "chiller:absorption":
            return ChillerAbsorption()
        if internal_name.lower() == "chiller:constantcop":
            return ChillerConstantCop()
        if internal_name.lower() == "chiller:enginedriven":
            return ChillerEngineDriven()
        if internal_name.lower() == "chiller:combustionturbine":
            return ChillerCombustionTurbine()
        if internal_name.lower() == "chillerheater:absorption:directfired":
            return ChillerHeaterAbsorptionDirectFired()
        if internal_name.lower() == "chillerheater:absorption:doubleeffect":
            return ChillerHeaterAbsorptionDoubleEffect()
        if internal_name.lower() == "heatpump:watertowater:equationfit:heating":
            return HeatPumpWaterToWaterEquationFitHeating()
        if internal_name.lower() == "heatpump:watertowater:equationfit:cooling":
            return HeatPumpWaterToWaterEquationFitCooling()
        if internal_name.lower() == "heatpump:watertowater:parameterestimation:cooling":
            return HeatPumpWaterToWaterParameterEstimationCooling()
        if internal_name.lower() == "heatpump:watertowater:parameterestimation:heating":
            return HeatPumpWaterToWaterParameterEstimationHeating()
        if internal_name.lower() == "districtcooling":
            return DistrictCooling()
        if internal_name.lower() == "districtheating":
            return DistrictHeating()
        if internal_name.lower() == "plantcomponent:temperaturesource":
            return PlantComponentTemperatureSource()
        if internal_name.lower() == "centralheatpumpsystem":
            return CentralHeatPumpSystem()
        if internal_name.lower() == "chillerheaterperformance:electric:eir":
            return ChillerHeaterPerformanceElectricEir()
        if internal_name.lower() == "coolingtower:singlespeed":
            return CoolingTowerSingleSpeed()
        if internal_name.lower() == "coolingtower:twospeed":
            return CoolingTowerTwoSpeed()
        if internal_name.lower() == "coolingtower:variablespeed:merkel":
            return CoolingTowerVariableSpeedMerkel()
        if internal_name.lower() == "coolingtower:variablespeed":
            return CoolingTowerVariableSpeed()
        if internal_name.lower() == "coolingtowerperformance:cooltools":
            return CoolingTowerPerformanceCoolTools()
        if internal_name.lower() == "coolingtowerperformance:yorkcalc":
            return CoolingTowerPerformanceYorkCalc()
        if internal_name.lower() == "evaporativefluidcooler:singlespeed":
            return EvaporativeFluidCoolerSingleSpeed()
        if internal_name.lower() == "evaporativefluidcooler:twospeed":
            return EvaporativeFluidCoolerTwoSpeed()
        if internal_name.lower() == "fluidcooler:singlespeed":
            return FluidCoolerSingleSpeed()
        if internal_name.lower() == "fluidcooler:twospeed":
            return FluidCoolerTwoSpeed()
        if internal_name.lower() == "groundheatexchanger:vertical":
            return GroundHeatExchangerVertical()
        if internal_name.lower() == "groundheatexchanger:pond":
            return GroundHeatExchangerPond()
        if internal_name.lower() == "groundheatexchanger:surface":
            return GroundHeatExchangerSurface()
        if internal_name.lower() == "groundheatexchanger:horizontaltrench":
            return GroundHeatExchangerHorizontalTrench()
        if internal_name.lower() == "heatexchanger:fluidtofluid":
            return HeatExchangerFluidToFluid()
        if internal_name.lower() == "waterheater:mixed":
            return WaterHeaterMixed()
        if internal_name.lower() == "waterheater:stratified":
            return WaterHeaterStratified()
        if internal_name.lower() == "waterheater:sizing":
            return WaterHeaterSizing()
        if internal_name.lower() == "waterheater:heatpump":
            return WaterHeaterHeatPump()
        if internal_name.lower() == "thermalstorage:ice:simple":
            return ThermalStorageIceSimple()
        if internal_name.lower() == "thermalstorage:ice:detailed":
            return ThermalStorageIceDetailed()
        if internal_name.lower() == "thermalstorage:chilledwater:mixed":
            return ThermalStorageChilledWaterMixed()
        if internal_name.lower() == "thermalstorage:chilledwater:stratified":
            return ThermalStorageChilledWaterStratified()
        if internal_name.lower() == "plantloop":
            return PlantLoop()
        if internal_name.lower() == "condenserloop":
            return CondenserLoop()
        if internal_name.lower() == "plantequipmentlist":
            return PlantEquipmentList()
        if internal_name.lower() == "condenserequipmentlist":
            return CondenserEquipmentList()
        if internal_name.lower() == "plantequipmentoperation:uncontrolled":
            return PlantEquipmentOperationUncontrolled()
        if internal_name.lower() == "plantequipmentoperation:coolingload":
            return PlantEquipmentOperationCoolingLoad()
        if internal_name.lower() == "plantequipmentoperation:heatingload":
            return PlantEquipmentOperationHeatingLoad()
        if internal_name.lower() == "plantequipmentoperation:outdoordrybulb":
            return PlantEquipmentOperationOutdoorDryBulb()
        if internal_name.lower() == "plantequipmentoperation:outdoorwetbulb":
            return PlantEquipmentOperationOutdoorWetBulb()
        if internal_name.lower() == "plantequipmentoperation:outdoorrelativehumidity":
            return PlantEquipmentOperationOutdoorRelativeHumidity()
        if internal_name.lower() == "plantequipmentoperation:outdoordewpoint":
            return PlantEquipmentOperationOutdoorDewpoint()
        if internal_name.lower() == "plantequipmentoperation:componentsetpoint":
            return PlantEquipmentOperationComponentSetpoint()
        if internal_name.lower() == "plantequipmentoperation:outdoordrybulbdifference":
            return PlantEquipmentOperationOutdoorDryBulbDifference()
        if internal_name.lower() == "plantequipmentoperation:outdoorwetbulbdifference":
            return PlantEquipmentOperationOutdoorWetBulbDifference()
        if internal_name.lower() == "plantequipmentoperation:outdoordewpointdifference":
            return PlantEquipmentOperationOutdoorDewpointDifference()
        if internal_name.lower() == "plantequipmentoperationschemes":
            return PlantEquipmentOperationSchemes()
        if internal_name.lower() == "condenserequipmentoperationschemes":
            return CondenserEquipmentOperationSchemes()
        if internal_name.lower() == "energymanagementsystem:sensor":
            return EnergyManagementSystemSensor()
        if internal_name.lower() == "energymanagementsystem:actuator":
            return EnergyManagementSystemActuator()
        if internal_name.lower() == "energymanagementsystem:programcallingmanager":
            return EnergyManagementSystemProgramCallingManager()
        if internal_name.lower() == "energymanagementsystem:program":
            return EnergyManagementSystemProgram()
        if internal_name.lower() == "energymanagementsystem:subroutine":
            return EnergyManagementSystemSubroutine()
        if internal_name.lower() == "energymanagementsystem:globalvariable":
            return EnergyManagementSystemGlobalVariable()
        if internal_name.lower() == "energymanagementsystem:outputvariable":
            return EnergyManagementSystemOutputVariable()
        if internal_name.lower() == "energymanagementsystem:meteredoutputvariable":
            return EnergyManagementSystemMeteredOutputVariable()
        if internal_name.lower() == "energymanagementsystem:trendvariable":
            return EnergyManagementSystemTrendVariable()
        if internal_name.lower() == "energymanagementsystem:internalvariable":
            return EnergyManagementSystemInternalVariable()
        if internal_name.lower() == "energymanagementsystem:curveortableindexvariable":
            return EnergyManagementSystemCurveOrTableIndexVariable()
        if internal_name.lower() == "energymanagementsystem:constructionindexvariable":
            return EnergyManagementSystemConstructionIndexVariable()
        if internal_name.lower() == "externalinterface":
            return ExternalInterface()
        if internal_name.lower() == "externalinterface:schedule":
            return ExternalInterfaceSchedule()
        if internal_name.lower() == "externalinterface:variable":
            return ExternalInterfaceVariable()
        if internal_name.lower() == "externalinterface:actuator":
            return ExternalInterfaceActuator()
        if internal_name.lower() == "externalinterface:functionalmockupunitimport":
            return ExternalInterfaceFunctionalMockupUnitImport()
        if internal_name.lower() == "externalinterface:functionalmockupunitimport:from:variable":
            return ExternalInterfaceFunctionalMockupUnitImportFromVariable()
        if internal_name.lower() == "externalinterface:functionalmockupunitimport:to:schedule":
            return ExternalInterfaceFunctionalMockupUnitImportToSchedule()
        if internal_name.lower() == "externalinterface:functionalmockupunitimport:to:actuator":
            return ExternalInterfaceFunctionalMockupUnitImportToActuator()
        if internal_name.lower() == "externalinterface:functionalmockupunitimport:to:variable":
            return ExternalInterfaceFunctionalMockupUnitImportToVariable()
        if internal_name.lower() == "externalinterface:functionalmockupunitexport:from:variable":
            return ExternalInterfaceFunctionalMockupUnitExportFromVariable()
        if internal_name.lower() == "externalinterface:functionalmockupunitexport:to:schedule":
            return ExternalInterfaceFunctionalMockupUnitExportToSchedule()
        if internal_name.lower() == "externalinterface:functionalmockupunitexport:to:actuator":
            return ExternalInterfaceFunctionalMockupUnitExportToActuator()
        if internal_name.lower() == "externalinterface:functionalmockupunitexport:to:variable":
            return ExternalInterfaceFunctionalMockupUnitExportToVariable()
        if internal_name.lower() == "zonehvac:forcedair:userdefined":
            return ZoneHvacForcedAirUserDefined()
        if internal_name.lower() == "airterminal:singleduct:userdefined":
            return AirTerminalSingleDuctUserDefined()
        if internal_name.lower() == "coil:userdefined":
            return CoilUserDefined()
        if internal_name.lower() == "plantcomponent:userdefined":
            return PlantComponentUserDefined()
        if internal_name.lower() == "plantequipmentoperation:userdefined":
            return PlantEquipmentOperationUserDefined()
        if internal_name.lower() == "availabilitymanager:scheduled":
            return AvailabilityManagerScheduled()
        if internal_name.lower() == "availabilitymanager:scheduledon":
            return AvailabilityManagerScheduledOn()
        if internal_name.lower() == "availabilitymanager:scheduledoff":
            return AvailabilityManagerScheduledOff()
        if internal_name.lower() == "availabilitymanager:optimumstart":
            return AvailabilityManagerOptimumStart()
        if internal_name.lower() == "availabilitymanager:nightcycle":
            return AvailabilityManagerNightCycle()
        if internal_name.lower() == "availabilitymanager:differentialthermostat":
            return AvailabilityManagerDifferentialThermostat()
        if internal_name.lower() == "availabilitymanager:hightemperatureturnoff":
            return AvailabilityManagerHighTemperatureTurnOff()
        if internal_name.lower() == "availabilitymanager:hightemperatureturnon":
            return AvailabilityManagerHighTemperatureTurnOn()
        if internal_name.lower() == "availabilitymanager:lowtemperatureturnoff":
            return AvailabilityManagerLowTemperatureTurnOff()
        if internal_name.lower() == "availabilitymanager:lowtemperatureturnon":
            return AvailabilityManagerLowTemperatureTurnOn()
        if internal_name.lower() == "availabilitymanager:nightventilation":
            return AvailabilityManagerNightVentilation()
        if internal_name.lower() == "availabilitymanager:hybridventilation":
            return AvailabilityManagerHybridVentilation()
        if internal_name.lower() == "availabilitymanagerassignmentlist":
            return AvailabilityManagerAssignmentList()
        if internal_name.lower() == "setpointmanager:scheduled":
            return SetpointManagerScheduled()
        if internal_name.lower() == "setpointmanager:scheduled:dualsetpoint":
            return SetpointManagerScheduledDualSetpoint()
        if internal_name.lower() == "setpointmanager:outdoorairreset":
            return SetpointManagerOutdoorAirReset()
        if internal_name.lower() == "setpointmanager:singlezone:reheat":
            return SetpointManagerSingleZoneReheat()
        if internal_name.lower() == "setpointmanager:singlezone:heating":
            return SetpointManagerSingleZoneHeating()
        if internal_name.lower() == "setpointmanager:singlezone:cooling":
            return SetpointManagerSingleZoneCooling()
        if internal_name.lower() == "setpointmanager:singlezone:humidity:minimum":
            return SetpointManagerSingleZoneHumidityMinimum()
        if internal_name.lower() == "setpointmanager:singlezone:humidity:maximum":
            return SetpointManagerSingleZoneHumidityMaximum()
        if internal_name.lower() == "setpointmanager:mixedair":
            return SetpointManagerMixedAir()
        if internal_name.lower() == "setpointmanager:outdoorairpretreat":
            return SetpointManagerOutdoorAirPretreat()
        if internal_name.lower() == "setpointmanager:warmest":
            return SetpointManagerWarmest()
        if internal_name.lower() == "setpointmanager:coldest":
            return SetpointManagerColdest()
        if internal_name.lower() == "setpointmanager:returnairbypassflow":
            return SetpointManagerReturnAirBypassFlow()
        if internal_name.lower() == "setpointmanager:warmesttemperatureflow":
            return SetpointManagerWarmestTemperatureFlow()
        if internal_name.lower() == "setpointmanager:multizone:heating:average":
            return SetpointManagerMultiZoneHeatingAverage()
        if internal_name.lower() == "setpointmanager:multizone:cooling:average":
            return SetpointManagerMultiZoneCoolingAverage()
        if internal_name.lower() == "setpointmanager:multizone:minimumhumidity:average":
            return SetpointManagerMultiZoneMinimumHumidityAverage()
        if internal_name.lower() == "setpointmanager:multizone:maximumhumidity:average":
            return SetpointManagerMultiZoneMaximumHumidityAverage()
        if internal_name.lower() == "setpointmanager:multizone:humidity:minimum":
            return SetpointManagerMultiZoneHumidityMinimum()
        if internal_name.lower() == "setpointmanager:multizone:humidity:maximum":
            return SetpointManagerMultiZoneHumidityMaximum()
        if internal_name.lower() == "setpointmanager:followoutdoorairtemperature":
            return SetpointManagerFollowOutdoorAirTemperature()
        if internal_name.lower() == "setpointmanager:followsystemnodetemperature":
            return SetpointManagerFollowSystemNodeTemperature()
        if internal_name.lower() == "setpointmanager:followgroundtemperature":
            return SetpointManagerFollowGroundTemperature()
        if internal_name.lower() == "setpointmanager:condenserenteringreset":
            return SetpointManagerCondenserEnteringReset()
        if internal_name.lower() == "setpointmanager:condenserenteringreset:ideal":
            return SetpointManagerCondenserEnteringResetIdeal()
        if internal_name.lower() == "setpointmanager:singlezone:onestagecooling":
            return SetpointManagerSingleZoneOneStageCooling()
        if internal_name.lower() == "setpointmanager:singlezone:onestageheating":
            return SetpointManagerSingleZoneOneStageHeating()
        if internal_name.lower() == "refrigeration:case":
            return RefrigerationCase()
        if internal_name.lower() == "refrigeration:compressorrack":
            return RefrigerationCompressorRack()
        if internal_name.lower() == "refrigeration:caseandwalkinlist":
            return RefrigerationCaseAndWalkInList()
        if internal_name.lower() == "refrigeration:condenser:aircooled":
            return RefrigerationCondenserAirCooled()
        if internal_name.lower() == "refrigeration:condenser:evaporativecooled":
            return RefrigerationCondenserEvaporativeCooled()
        if internal_name.lower() == "refrigeration:condenser:watercooled":
            return RefrigerationCondenserWaterCooled()
        if internal_name.lower() == "refrigeration:condenser:cascade":
            return RefrigerationCondenserCascade()
        if internal_name.lower() == "refrigeration:gascooler:aircooled":
            return RefrigerationGasCoolerAirCooled()
        if internal_name.lower() == "refrigeration:transferloadlist":
            return RefrigerationTransferLoadList()
        if internal_name.lower() == "refrigeration:subcooler":
            return RefrigerationSubcooler()
        if internal_name.lower() == "refrigeration:compressor":
            return RefrigerationCompressor()
        if internal_name.lower() == "refrigeration:compressorlist":
            return RefrigerationCompressorList()
        if internal_name.lower() == "refrigeration:system":
            return RefrigerationSystem()
        if internal_name.lower() == "refrigeration:transcriticalsystem":
            return RefrigerationTranscriticalSystem()
        if internal_name.lower() == "refrigeration:secondarysystem":
            return RefrigerationSecondarySystem()
        if internal_name.lower() == "refrigeration:walkin":
            return RefrigerationWalkIn()
        if internal_name.lower() == "refrigeration:airchiller":
            return RefrigerationAirChiller()
        if internal_name.lower() == "zonehvac:refrigerationchillerset":
            return ZoneHvacRefrigerationChillerSet()
        if internal_name.lower() == "demandmanagerassignmentlist":
            return DemandManagerAssignmentList()
        if internal_name.lower() == "demandmanager:exteriorlights":
            return DemandManagerExteriorLights()
        if internal_name.lower() == "demandmanager:lights":
            return DemandManagerLights()
        if internal_name.lower() == "demandmanager:electricequipment":
            return DemandManagerElectricEquipment()
        if internal_name.lower() == "demandmanager:thermostats":
            return DemandManagerThermostats()
        if internal_name.lower() == "generator:internalcombustionengine":
            return GeneratorInternalCombustionEngine()
        if internal_name.lower() == "generator:combustionturbine":
            return GeneratorCombustionTurbine()
        if internal_name.lower() == "generator:microturbine":
            return GeneratorMicroTurbine()
        if internal_name.lower() == "generator:photovoltaic":
            return GeneratorPhotovoltaic()
        if internal_name.lower() == "photovoltaicperformance:simple":
            return PhotovoltaicPerformanceSimple()
        if internal_name.lower() == "photovoltaicperformance:equivalentone-diode":
            return PhotovoltaicPerformanceEquivalentOneDiode()
        if internal_name.lower() == "photovoltaicperformance:sandia":
            return PhotovoltaicPerformanceSandia()
        if internal_name.lower() == "generator:fuelcell":
            return GeneratorFuelCell()
        if internal_name.lower() == "generator:fuelcell:powermodule":
            return GeneratorFuelCellPowerModule()
        if internal_name.lower() == "generator:fuelcell:airsupply":
            return GeneratorFuelCellAirSupply()
        if internal_name.lower() == "generator:fuelcell:watersupply":
            return GeneratorFuelCellWaterSupply()
        if internal_name.lower() == "generator:fuelcell:auxiliaryheater":
            return GeneratorFuelCellAuxiliaryHeater()
        if internal_name.lower() == "generator:fuelcell:exhaustgastowaterheatexchanger":
            return GeneratorFuelCellExhaustGasToWaterHeatExchanger()
        if internal_name.lower() == "generator:fuelcell:electricalstorage":
            return GeneratorFuelCellElectricalStorage()
        if internal_name.lower() == "generator:fuelcell:inverter":
            return GeneratorFuelCellInverter()
        if internal_name.lower() == "generator:fuelcell:stackcooler":
            return GeneratorFuelCellStackCooler()
        if internal_name.lower() == "generator:microchp":
            return GeneratorMicroChp()
        if internal_name.lower() == "generator:microchp:nonnormalizedparameters":
            return GeneratorMicroChpNonNormalizedParameters()
        if internal_name.lower() == "generator:fuelsupply":
            return GeneratorFuelSupply()
        if internal_name.lower() == "generator:windturbine":
            return GeneratorWindTurbine()
        if internal_name.lower() == "electricloadcenter:generators":
            return ElectricLoadCenterGenerators()
        if internal_name.lower() == "electricloadcenter:inverter:simple":
            return ElectricLoadCenterInverterSimple()
        if internal_name.lower() == "electricloadcenter:inverter:functionofpower":
            return ElectricLoadCenterInverterFunctionOfPower()
        if internal_name.lower() == "electricloadcenter:inverter:lookuptable":
            return ElectricLoadCenterInverterLookUpTable()
        if internal_name.lower() == "electricloadcenter:storage:simple":
            return ElectricLoadCenterStorageSimple()
        if internal_name.lower() == "electricloadcenter:storage:battery":
            return ElectricLoadCenterStorageBattery()
        if internal_name.lower() == "electricloadcenter:transformer":
            return ElectricLoadCenterTransformer()
        if internal_name.lower() == "electricloadcenter:distribution":
            return ElectricLoadCenterDistribution()
        if internal_name.lower() == "wateruse:equipment":
            return WaterUseEquipment()
        if internal_name.lower() == "wateruse:connections":
            return WaterUseConnections()
        if internal_name.lower() == "wateruse:storage":
            return WaterUseStorage()
        if internal_name.lower() == "wateruse:well":
            return WaterUseWell()
        if internal_name.lower() == "wateruse:raincollector":
            return WaterUseRainCollector()
        if internal_name.lower() == "faultmodel:temperaturesensoroffset:outdoorair":
            return FaultModelTemperatureSensorOffsetOutdoorAir()
        if internal_name.lower() == "faultmodel:humiditysensoroffset:outdoorair":
            return FaultModelHumiditySensorOffsetOutdoorAir()
        if internal_name.lower() == "faultmodel:enthalpysensoroffset:outdoorair":
            return FaultModelEnthalpySensorOffsetOutdoorAir()
        if internal_name.lower() == "faultmodel:pressuresensoroffset:outdoorair":
            return FaultModelPressureSensorOffsetOutdoorAir()
        if internal_name.lower() == "faultmodel:temperaturesensoroffset:returnair":
            return FaultModelTemperatureSensorOffsetReturnAir()
        if internal_name.lower() == "faultmodel:enthalpysensoroffset:returnair":
            return FaultModelEnthalpySensorOffsetReturnAir()
        if internal_name.lower() == "faultmodel:fouling:coil":
            return FaultModelFoulingCoil()
        if internal_name.lower() == "matrix:twodimension":
            return MatrixTwoDimension()
        if internal_name.lower() == "curve:linear":
            return CurveLinear()
        if internal_name.lower() == "curve:quadlinear":
            return CurveQuadLinear()
        if internal_name.lower() == "curve:quadratic":
            return CurveQuadratic()
        if internal_name.lower() == "curve:cubic":
            return CurveCubic()
        if internal_name.lower() == "curve:quartic":
            return CurveQuartic()
        if internal_name.lower() == "curve:exponent":
            return CurveExponent()
        if internal_name.lower() == "curve:bicubic":
            return CurveBicubic()
        if internal_name.lower() == "curve:biquadratic":
            return CurveBiquadratic()
        if internal_name.lower() == "curve:quadraticlinear":
            return CurveQuadraticLinear()
        if internal_name.lower() == "curve:triquadratic":
            return CurveTriquadratic()
        if internal_name.lower() == "curve:functional:pressuredrop":
            return CurveFunctionalPressureDrop()
        if internal_name.lower() == "curve:fanpressurerise":
            return CurveFanPressureRise()
        if internal_name.lower() == "curve:exponentialskewnormal":
            return CurveExponentialSkewNormal()
        if internal_name.lower() == "curve:sigmoid":
            return CurveSigmoid()
        if internal_name.lower() == "curve:rectangularhyperbola1":
            return CurveRectangularHyperbola1()
        if internal_name.lower() == "curve:rectangularhyperbola2":
            return CurveRectangularHyperbola2()
        if internal_name.lower() == "curve:exponentialdecay":
            return CurveExponentialDecay()
        if internal_name.lower() == "curve:doubleexponentialdecay":
            return CurveDoubleExponentialDecay()
        if internal_name.lower() == "table:oneindependentvariable":
            return TableOneIndependentVariable()
        if internal_name.lower() == "table:twoindependentvariables":
            return TableTwoIndependentVariables()
        if internal_name.lower() == "table:multivariablelookup":
            return TableMultiVariableLookup()
        if internal_name.lower() == "fluidproperties:name":
            return FluidPropertiesName()
        if internal_name.lower() == "fluidproperties:glycolconcentration":
            return FluidPropertiesGlycolConcentration()
        if internal_name.lower() == "fluidproperties:temperatures":
            return FluidPropertiesTemperatures()
        if internal_name.lower() == "fluidproperties:saturated":
            return FluidPropertiesSaturated()
        if internal_name.lower() == "fluidproperties:superheated":
            return FluidPropertiesSuperheated()
        if internal_name.lower() == "fluidproperties:concentration":
            return FluidPropertiesConcentration()
        if internal_name.lower() == "currencytype":
            return CurrencyType()
        if internal_name.lower() == "componentcost:adjustments":
            return ComponentCostAdjustments()
        if internal_name.lower() == "componentcost:reference":
            return ComponentCostReference()
        if internal_name.lower() == "componentcost:lineitem":
            return ComponentCostLineItem()
        if internal_name.lower() == "utilitycost:tariff":
            return UtilityCostTariff()
        if internal_name.lower() == "utilitycost:qualify":
            return UtilityCostQualify()
        if internal_name.lower() == "utilitycost:charge:simple":
            return UtilityCostChargeSimple()
        if internal_name.lower() == "utilitycost:charge:block":
            return UtilityCostChargeBlock()
        if internal_name.lower() == "utilitycost:ratchet":
            return UtilityCostRatchet()
        if internal_name.lower() == "utilitycost:variable":
            return UtilityCostVariable()
        if internal_name.lower() == "utilitycost:computation":
            return UtilityCostComputation()
        if internal_name.lower() == "lifecyclecost:parameters":
            return LifeCycleCostParameters()
        if internal_name.lower() == "lifecyclecost:recurringcosts":
            return LifeCycleCostRecurringCosts()
        if internal_name.lower() == "lifecyclecost:nonrecurringcost":
            return LifeCycleCostNonrecurringCost()
        if internal_name.lower() == "lifecyclecost:usepriceescalation":
            return LifeCycleCostUsePriceEscalation()
        if internal_name.lower() == "lifecyclecost:useadjustment":
            return LifeCycleCostUseAdjustment()
        if internal_name.lower() == "parametric:setvalueforrun":
            return ParametricSetValueForRun()
        if internal_name.lower() == "parametric:logic":
            return ParametricLogic()
        if internal_name.lower() == "parametric:runcontrol":
            return ParametricRunControl()
        if internal_name.lower() == "parametric:filenamesuffix":
            return ParametricFileNameSuffix()
        if internal_name.lower() == "output:variabledictionary":
            return OutputVariableDictionary()
        if internal_name.lower() == "output:surfaces:list":
            return OutputSurfacesList()
        if internal_name.lower() == "output:surfaces:drawing":
            return OutputSurfacesDrawing()
        if internal_name.lower() == "output:schedules":
            return OutputSchedules()
        if internal_name.lower() == "output:constructions":
            return OutputConstructions()
        if internal_name.lower() == "output:energymanagementsystem":
            return OutputEnergyManagementSystem()
        if internal_name.lower() == "outputcontrol:surfacecolorscheme":
            return OutputControlSurfaceColorScheme()
        if internal_name.lower() == "output:table:summaryreports":
            return OutputTableSummaryReports()
        if internal_name.lower() == "output:table:timebins":
            return OutputTableTimeBins()
        if internal_name.lower() == "output:table:monthly":
            return OutputTableMonthly()
        if internal_name.lower() == "outputcontrol:table:style":
            return OutputControlTableStyle()
        if internal_name.lower() == "outputcontrol:reportingtolerances":
            return OutputControlReportingTolerances()
        if internal_name.lower() == "output:variable":
            return OutputVariable()
        if internal_name.lower() == "output:meter":
            return OutputMeter()
        if internal_name.lower() == "output:meter:meterfileonly":
            return OutputMeterMeterFileOnly()
        if internal_name.lower() == "output:meter:cumulative":
            return OutputMeterCumulative()
        if internal_name.lower() == "output:meter:cumulative:meterfileonly":
            return OutputMeterCumulativeMeterFileOnly()
        if internal_name.lower() == "meter:custom":
            return MeterCustom()
        if internal_name.lower() == "meter:customdecrement":
            return MeterCustomDecrement()
        if internal_name.lower() == "output:sqlite":
            return OutputSqlite()
        if internal_name.lower() == "output:environmentalimpactfactors":
            return OutputEnvironmentalImpactFactors()
        if internal_name.lower() == "environmentalimpactfactors":
            return EnvironmentalImpactFactors()
        if internal_name.lower() == "fuelfactors":
            return FuelFactors()
        if internal_name.lower() == "output:diagnostics":
            return OutputDiagnostics()
        if internal_name.lower() == "output:debuggingdata":
            return OutputDebuggingData()
        if internal_name.lower() == "output:preprocessormessage":
            return OutputPreprocessorMessage()
        raise ValueError("No DataDictionary known for {}".format(internal_name))

    def __getitem__(self, val):
        if isinstance(val, six.string_types):
            return self._data[val.lower()]
        elif isinstance(val, int):
            i = 0
            for objs in self._data.values():
                for obj in objs:
                    i += 1
                    if i  == val:
                        return obj
    
    def __len__(self):
        count = 0
        for objs in self._data.values():
            count += len(objs)
        return count

    def __iter__(self):
        for val in self._data.values():
            if len(val) > 0:
                yield val