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

    required_objects = ["building", "globalgeometryrules"]
    unique_objects = [
        "zoneairheatbalancealgorithm",
        "surfaceconvectionalgorithm:outside:adaptivemodelselections",
        "outputcontrol:sizing:style",
        "runperiodcontrol:daylightsavingtime",
        "building",
        "zoneairmassflowconservation",
        "zoneaircontaminantbalance",
        "site:groundtemperature:shallow",
        "site:solarandvisiblespectrum",
        "output:debuggingdata",
        "outputcontrol:illuminancemap:style",
        "site:heightvariation",
        "lifecyclecost:parameters",
        "timestep",
        "convergencelimits",
        "heatbalancesettings:conductionfinitedifference",
        "version",
        "airflownetwork:simulationcontrol",
        "site:weatherstation",
        "globalgeometryrules",
        "output:energymanagementsystem",
        "shadowcalculation",
        "site:groundreflectance",
        "site:groundtemperature:buildingsurface",
        "surfaceconvectionalgorithm:inside",
        "hvactemplate:plant:chilledwaterloop",
        "site:location",
        "parametric:logic",
        "parametric:runcontrol",
        "surfaceconvectionalgorithm:inside:adaptivemodelselections",
        "zonecapacitancemultiplier:researchspecial",
        "compliance:building",
        "sizing:parameters",
        "hvactemplate:plant:hotwaterloop",
        "site:groundtemperature:deep",
        "hvactemplate:plant:mixedwaterloop",
        "outputcontrol:reportingtolerances",
        "simulationcontrol",
        "output:sqlite",
        "site:groundtemperature:fcfactormethod",
        "heatbalancealgorithm",
        "parametric:filenamesuffix",
        "geometrytransform",
        "outputcontrol:table:style",
        "surfaceconvectionalgorithm:outside",
        "output:table:summaryreports",
        "currencytype"]

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
        self._data["schedule:week:daily"] = []
        self._data["schedule:week:compact"] = []
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
        self._data[
            "materialproperty:heatandmoisturetransfer:sorptionisotherm"] = []
        self._data["materialproperty:heatandmoisturetransfer:suction"] = []
        self._data[
            "materialproperty:heatandmoisturetransfer:redistribution"] = []
        self._data["materialproperty:heatandmoisturetransfer:diffusion"] = []
        self._data[
            "materialproperty:heatandmoisturetransfer:thermalconductivity"] = []
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
        self._data[
            "surfaceproperty:heattransferalgorithm:multiplesurface"] = []
        self._data["surfaceproperty:heattransferalgorithm:surfacelist"] = []
        self._data["surfaceproperty:heattransferalgorithm:construction"] = []
        self._data["surfacecontrol:movableinsulation"] = []
        self._data["surfaceproperty:othersidecoefficients"] = []
        self._data["surfaceproperty:othersideconditionsmodel"] = []
        self._data[
            "surfaceconvectionalgorithm:inside:adaptivemodelselections"] = []
        self._data[
            "surfaceconvectionalgorithm:outside:adaptivemodelselections"] = []
        self._data["surfaceconvectionalgorithm:inside:usercurve"] = []
        self._data["surfaceconvectionalgorithm:outside:usercurve"] = []
        self._data["surfaceproperty:convectioncoefficients"] = []
        self._data[
            "surfaceproperty:convectioncoefficients:multiplesurface"] = []
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
        self._data[
            "surfacecontaminantsourceandsink:generic:pressuredriven"] = []
        self._data["zonecontaminantsourceandsink:generic:cutoffmodel"] = []
        self._data["zonecontaminantsourceandsink:generic:decaysource"] = []
        self._data[
            "surfacecontaminantsourceandsink:generic:boundarylayerdiffusion"] = []
        self._data[
            "surfacecontaminantsourceandsink:generic:depositionvelocitysink"] = []
        self._data[
            "zonecontaminantsourceandsink:generic:depositionratesink"] = []
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
        self._data[
            "airflownetwork:multizone:surface:effectiveleakagearea"] = []
        self._data["airflownetwork:multizone:component:detailedopening"] = []
        self._data["airflownetwork:multizone:component:simpleopening"] = []
        self._data["airflownetwork:multizone:component:horizontalopening"] = []
        self._data["airflownetwork:multizone:component:zoneexhaustfan"] = []
        self._data["airflownetwork:multizone:externalnode"] = []
        self._data[
            "airflownetwork:multizone:windpressurecoefficientarray"] = []
        self._data[
            "airflownetwork:multizone:windpressurecoefficientvalues"] = []
        self._data["airflownetwork:distribution:node"] = []
        self._data["airflownetwork:distribution:component:leak"] = []
        self._data["airflownetwork:distribution:component:leakageratio"] = []
        self._data["airflownetwork:distribution:component:duct"] = []
        self._data["airflownetwork:distribution:component:fan"] = []
        self._data["airflownetwork:distribution:component:coil"] = []
        self._data["airflownetwork:distribution:component:heatexchanger"] = []
        self._data["airflownetwork:distribution:component:terminalunit"] = []
        self._data[
            "airflownetwork:distribution:component:constantpressuredrop"] = []
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
        self._data[
            "thermostatsetpoint:thermalcomfort:fanger:singleheating"] = []
        self._data[
            "thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = []
        self._data[
            "thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = []
        self._data[
            "thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = []
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
        self._data[
            "airterminal:singleduct:constantvolume:fourpipeinduction"] = []
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
        self._data[
            "coil:cooling:watertoairheatpump:variablespeedequationfit"] = []
        self._data["coil:heating:watertoairheatpump:equationfit"] = []
        self._data[
            "coil:heating:watertoairheatpump:variablespeedequationfit"] = []
        self._data["coil:waterheating:airtowaterheatpump"] = []
        self._data["coil:waterheating:desuperheater"] = []
        self._data["coilsystem:cooling:dx"] = []
        self._data["coilsystem:heating:dx"] = []
        self._data["coilsystem:cooling:water:heatexchangerassisted"] = []
        self._data["coilsystem:cooling:dx:heatexchangerassisted"] = []
        self._data["coil:cooling:dx:singlespeed:thermalstorage"] = []
        self._data["humidifier:steam:electric"] = []
        self._data["dehumidifier:desiccant:nofans"] = []
        self._data["dehumidifier:desiccant:system"] = []
        self._data["heatexchanger:airtoair:flatplate"] = []
        self._data["heatexchanger:airtoair:sensibleandlatent"] = []
        self._data["heatexchanger:desiccant:balancedflow"] = []
        self._data[
            "heatexchanger:desiccant:balancedflow:performancedatatype1"] = []
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
        self._data["airloophvac:supplypath"] = []
        self._data["airloophvac:returnpath"] = []
        self._data["branch"] = []
        self._data["connectorlist"] = []
        self._data["outdoorair:node"] = []
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
        self._data["temperingvalve"] = []
        self._data["loadprofile:plant"] = []
        self._data["solarcollectorperformance:flatplate"] = []
        self._data["solarcollector:flatplate:water"] = []
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
        self._data[
            "externalinterface:functionalmockupunitimport:from:variable"] = []
        self._data[
            "externalinterface:functionalmockupunitimport:to:schedule"] = []
        self._data[
            "externalinterface:functionalmockupunitimport:to:actuator"] = []
        self._data[
            "externalinterface:functionalmockupunitimport:to:variable"] = []
        self._data[
            "externalinterface:functionalmockupunitexport:from:variable"] = []
        self._data[
            "externalinterface:functionalmockupunitexport:to:schedule"] = []
        self._data[
            "externalinterface:functionalmockupunitexport:to:actuator"] = []
        self._data[
            "externalinterface:functionalmockupunitexport:to:variable"] = []
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
        if internal_name.lower(
        ) == "heatbalancesettings:conductionfinitedifference":
            return HeatBalanceSettingsConductionFiniteDifference()
        if internal_name.lower() == "zoneairheatbalancealgorithm":
            return ZoneAirHeatBalanceAlgorithm()
        if internal_name.lower() == "zoneaircontaminantbalance":
            return ZoneAirContaminantBalance()
        if internal_name.lower() == "zoneairmassflowconservation":
            return ZoneAirMassFlowConservation()
        if internal_name.lower(
        ) == "zonecapacitancemultiplier:researchspecial":
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
        if internal_name.lower() == "schedule:week:daily":
            return ScheduleWeekDaily()
        if internal_name.lower() == "schedule:week:compact":
            return ScheduleWeekCompact()
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
        if internal_name.lower(
        ) == "windowmaterial:glazinggroup:thermochromic":
            return WindowMaterialGlazingGroupThermochromic()
        if internal_name.lower(
        ) == "windowmaterial:glazing:refractionextinctionmethod":
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
        if internal_name.lower(
        ) == "materialproperty:moisturepenetrationdepth:settings":
            return MaterialPropertyMoisturePenetrationDepthSettings()
        if internal_name.lower() == "materialproperty:phasechange":
            return MaterialPropertyPhaseChange()
        if internal_name.lower(
        ) == "materialproperty:variablethermalconductivity":
            return MaterialPropertyVariableThermalConductivity()
        if internal_name.lower(
        ) == "materialproperty:heatandmoisturetransfer:settings":
            return MaterialPropertyHeatAndMoistureTransferSettings()
        if internal_name.lower(
        ) == "materialproperty:heatandmoisturetransfer:sorptionisotherm":
            return MaterialPropertyHeatAndMoistureTransferSorptionIsotherm()
        if internal_name.lower(
        ) == "materialproperty:heatandmoisturetransfer:suction":
            return MaterialPropertyHeatAndMoistureTransferSuction()
        if internal_name.lower(
        ) == "materialproperty:heatandmoisturetransfer:redistribution":
            return MaterialPropertyHeatAndMoistureTransferRedistribution()
        if internal_name.lower(
        ) == "materialproperty:heatandmoisturetransfer:diffusion":
            return MaterialPropertyHeatAndMoistureTransferDiffusion()
        if internal_name.lower(
        ) == "materialproperty:heatandmoisturetransfer:thermalconductivity":
            return MaterialPropertyHeatAndMoistureTransferThermalConductivity()
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
        if internal_name.lower(
        ) == "surfaceproperty:heattransferalgorithm:multiplesurface":
            return SurfacePropertyHeatTransferAlgorithmMultipleSurface()
        if internal_name.lower(
        ) == "surfaceproperty:heattransferalgorithm:surfacelist":
            return SurfacePropertyHeatTransferAlgorithmSurfaceList()
        if internal_name.lower(
        ) == "surfaceproperty:heattransferalgorithm:construction":
            return SurfacePropertyHeatTransferAlgorithmConstruction()
        if internal_name.lower() == "surfacecontrol:movableinsulation":
            return SurfaceControlMovableInsulation()
        if internal_name.lower() == "surfaceproperty:othersidecoefficients":
            return SurfacePropertyOtherSideCoefficients()
        if internal_name.lower() == "surfaceproperty:othersideconditionsmodel":
            return SurfacePropertyOtherSideConditionsModel()
        if internal_name.lower(
        ) == "surfaceconvectionalgorithm:inside:adaptivemodelselections":
            return SurfaceConvectionAlgorithmInsideAdaptiveModelSelections()
        if internal_name.lower(
        ) == "surfaceconvectionalgorithm:outside:adaptivemodelselections":
            return SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections()
        if internal_name.lower(
        ) == "surfaceconvectionalgorithm:inside:usercurve":
            return SurfaceConvectionAlgorithmInsideUserCurve()
        if internal_name.lower(
        ) == "surfaceconvectionalgorithm:outside:usercurve":
            return SurfaceConvectionAlgorithmOutsideUserCurve()
        if internal_name.lower() == "surfaceproperty:convectioncoefficients":
            return SurfacePropertyConvectionCoefficients()
        if internal_name.lower(
        ) == "surfaceproperty:convectioncoefficients:multiplesurface":
            return SurfacePropertyConvectionCoefficientsMultipleSurface()
        if internal_name.lower() == "surfaceproperties:vaporcoefficients":
            return SurfacePropertiesVaporCoefficients()
        if internal_name.lower(
        ) == "surfaceproperty:exteriornaturalventedcavity":
            return SurfacePropertyExteriorNaturalVentedCavity()
        if internal_name.lower() == "surfaceproperty:solarincidentinside":
            return SurfacePropertySolarIncidentInside()
        if internal_name.lower(
        ) == "complexfenestrationproperty:solarabsorbedlayers":
            return ComplexFenestrationPropertySolarAbsorbedLayers()
        if internal_name.lower(
        ) == "zoneproperty:userviewfactors:bysurfacename":
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
        if internal_name.lower(
        ) == "groundheattransfer:basement:simparameters":
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
        if internal_name.lower(
        ) == "groundheattransfer:basement:equivautogrid":
            return GroundHeatTransferBasementEquivAutoGrid()
        if internal_name.lower() == "groundheattransfer:basement:autogrid":
            return GroundHeatTransferBasementAutoGrid()
        if internal_name.lower() == "groundheattransfer:basement:manualgrid":
            return GroundHeatTransferBasementManualGrid()
        if internal_name.lower() == "roomairmodeltype":
            return RoomAirModelType()
        if internal_name.lower() == "roomair:temperaturepattern:userdefined":
            return RoomAirTemperaturePatternUserDefined()
        if internal_name.lower(
        ) == "roomair:temperaturepattern:constantgradient":
            return RoomAirTemperaturePatternConstantGradient()
        if internal_name.lower() == "roomair:temperaturepattern:twogradient":
            return RoomAirTemperaturePatternTwoGradient()
        if internal_name.lower(
        ) == "roomair:temperaturepattern:nondimensionalheight":
            return RoomAirTemperaturePatternNondimensionalHeight()
        if internal_name.lower(
        ) == "roomair:temperaturepattern:surfacemapping":
            return RoomAirTemperaturePatternSurfaceMapping()
        if internal_name.lower() == "roomair:node":
            return RoomAirNode()
        if internal_name.lower(
        ) == "roomairsettings:onenodedisplacementventilation":
            return RoomAirSettingsOneNodeDisplacementVentilation()
        if internal_name.lower(
        ) == "roomairsettings:threenodedisplacementventilation":
            return RoomAirSettingsThreeNodeDisplacementVentilation()
        if internal_name.lower() == "roomairsettings:crossventilation":
            return RoomAirSettingsCrossVentilation()
        if internal_name.lower(
        ) == "roomairsettings:underfloorairdistributioninterior":
            return RoomAirSettingsUnderFloorAirDistributionInterior()
        if internal_name.lower(
        ) == "roomairsettings:underfloorairdistributionexterior":
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
        if internal_name.lower(
        ) == "zonebaseboard:outdoortemperaturecontrolled":
            return ZoneBaseboardOutdoorTemperatureControlled()
        if internal_name.lower(
        ) == "zonecontaminantsourceandsink:carbondioxide":
            return ZoneContaminantSourceAndSinkCarbonDioxide()
        if internal_name.lower(
        ) == "zonecontaminantsourceandsink:generic:constant":
            return ZoneContaminantSourceAndSinkGenericConstant()
        if internal_name.lower(
        ) == "surfacecontaminantsourceandsink:generic:pressuredriven":
            return SurfaceContaminantSourceAndSinkGenericPressureDriven()
        if internal_name.lower(
        ) == "zonecontaminantsourceandsink:generic:cutoffmodel":
            return ZoneContaminantSourceAndSinkGenericCutoffModel()
        if internal_name.lower(
        ) == "zonecontaminantsourceandsink:generic:decaysource":
            return ZoneContaminantSourceAndSinkGenericDecaySource()
        if internal_name.lower(
        ) == "surfacecontaminantsourceandsink:generic:boundarylayerdiffusion":
            return SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion()
        if internal_name.lower(
        ) == "surfacecontaminantsourceandsink:generic:depositionvelocitysink":
            return SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink()
        if internal_name.lower(
        ) == "zonecontaminantsourceandsink:generic:depositionratesink":
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
        if internal_name.lower(
        ) == "airflownetwork:multizone:referencecrackconditions":
            return AirflowNetworkMultiZoneReferenceCrackConditions()
        if internal_name.lower() == "airflownetwork:multizone:surface:crack":
            return AirflowNetworkMultiZoneSurfaceCrack()
        if internal_name.lower(
        ) == "airflownetwork:multizone:surface:effectiveleakagearea":
            return AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea()
        if internal_name.lower(
        ) == "airflownetwork:multizone:component:detailedopening":
            return AirflowNetworkMultiZoneComponentDetailedOpening()
        if internal_name.lower(
        ) == "airflownetwork:multizone:component:simpleopening":
            return AirflowNetworkMultiZoneComponentSimpleOpening()
        if internal_name.lower(
        ) == "airflownetwork:multizone:component:horizontalopening":
            return AirflowNetworkMultiZoneComponentHorizontalOpening()
        if internal_name.lower(
        ) == "airflownetwork:multizone:component:zoneexhaustfan":
            return AirflowNetworkMultiZoneComponentZoneExhaustFan()
        if internal_name.lower() == "airflownetwork:multizone:externalnode":
            return AirflowNetworkMultiZoneExternalNode()
        if internal_name.lower(
        ) == "airflownetwork:multizone:windpressurecoefficientarray":
            return AirflowNetworkMultiZoneWindPressureCoefficientArray()
        if internal_name.lower(
        ) == "airflownetwork:multizone:windpressurecoefficientvalues":
            return AirflowNetworkMultiZoneWindPressureCoefficientValues()
        if internal_name.lower() == "airflownetwork:distribution:node":
            return AirflowNetworkDistributionNode()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:leak":
            return AirflowNetworkDistributionComponentLeak()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:leakageratio":
            return AirflowNetworkDistributionComponentLeakageRatio()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:duct":
            return AirflowNetworkDistributionComponentDuct()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:fan":
            return AirflowNetworkDistributionComponentFan()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:coil":
            return AirflowNetworkDistributionComponentCoil()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:heatexchanger":
            return AirflowNetworkDistributionComponentHeatExchanger()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:terminalunit":
            return AirflowNetworkDistributionComponentTerminalUnit()
        if internal_name.lower(
        ) == "airflownetwork:distribution:component:constantpressuredrop":
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
        if internal_name.lower(
        ) == "hvactemplate:system:unitaryheatpump:airtoair":
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
        if internal_name.lower(
        ) == "hvactemplate:plant:chiller:objectreference":
            return HvactemplatePlantChillerObjectReference()
        if internal_name.lower() == "hvactemplate:plant:tower":
            return HvactemplatePlantTower()
        if internal_name.lower() == "hvactemplate:plant:tower:objectreference":
            return HvactemplatePlantTowerObjectReference()
        if internal_name.lower() == "hvactemplate:plant:hotwaterloop":
            return HvactemplatePlantHotWaterLoop()
        if internal_name.lower() == "hvactemplate:plant:boiler":
            return HvactemplatePlantBoiler()
        if internal_name.lower(
        ) == "hvactemplate:plant:boiler:objectreference":
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
        if internal_name.lower(
        ) == "zonecontrol:thermostat:operativetemperature":
            return ZoneControlThermostatOperativeTemperature()
        if internal_name.lower() == "zonecontrol:thermostat:thermalcomfort":
            return ZoneControlThermostatThermalComfort()
        if internal_name.lower(
        ) == "zonecontrol:thermostat:temperatureandhumidity":
            return ZoneControlThermostatTemperatureAndHumidity()
        if internal_name.lower() == "thermostatsetpoint:singleheating":
            return ThermostatSetpointSingleHeating()
        if internal_name.lower() == "thermostatsetpoint:singlecooling":
            return ThermostatSetpointSingleCooling()
        if internal_name.lower(
        ) == "thermostatsetpoint:singleheatingorcooling":
            return ThermostatSetpointSingleHeatingOrCooling()
        if internal_name.lower() == "thermostatsetpoint:dualsetpoint":
            return ThermostatSetpointDualSetpoint()
        if internal_name.lower(
        ) == "thermostatsetpoint:thermalcomfort:fanger:singleheating":
            return ThermostatSetpointThermalComfortFangerSingleHeating()
        if internal_name.lower(
        ) == "thermostatsetpoint:thermalcomfort:fanger:singlecooling":
            return ThermostatSetpointThermalComfortFangerSingleCooling()
        if internal_name.lower(
        ) == "thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling":
            return ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling()
        if internal_name.lower(
        ) == "thermostatsetpoint:thermalcomfort:fanger:dualsetpoint":
            return ThermostatSetpointThermalComfortFangerDualSetpoint()
        if internal_name.lower(
        ) == "zonecontrol:thermostat:stageddualsetpoint":
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
        if internal_name.lower(
        ) == "zonehvac:energyrecoveryventilator:controller":
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
        if internal_name.lower(
        ) == "zonehvac:terminalunit:variablerefrigerantflow":
            return ZoneHvacTerminalUnitVariableRefrigerantFlow()
        if internal_name.lower(
        ) == "zonehvac:baseboard:radiantconvective:water":
            return ZoneHvacBaseboardRadiantConvectiveWater()
        if internal_name.lower(
        ) == "zonehvac:baseboard:radiantconvective:steam":
            return ZoneHvacBaseboardRadiantConvectiveSteam()
        if internal_name.lower(
        ) == "zonehvac:baseboard:radiantconvective:electric":
            return ZoneHvacBaseboardRadiantConvectiveElectric()
        if internal_name.lower() == "zonehvac:baseboard:convective:water":
            return ZoneHvacBaseboardConvectiveWater()
        if internal_name.lower() == "zonehvac:baseboard:convective:electric":
            return ZoneHvacBaseboardConvectiveElectric()
        if internal_name.lower(
        ) == "zonehvac:lowtemperatureradiant:variableflow":
            return ZoneHvacLowTemperatureRadiantVariableFlow()
        if internal_name.lower(
        ) == "zonehvac:lowtemperatureradiant:constantflow":
            return ZoneHvacLowTemperatureRadiantConstantFlow()
        if internal_name.lower() == "zonehvac:lowtemperatureradiant:electric":
            return ZoneHvacLowTemperatureRadiantElectric()
        if internal_name.lower(
        ) == "zonehvac:lowtemperatureradiant:surfacegroup":
            return ZoneHvacLowTemperatureRadiantSurfaceGroup()
        if internal_name.lower() == "zonehvac:hightemperatureradiant":
            return ZoneHvacHighTemperatureRadiant()
        if internal_name.lower() == "zonehvac:ventilatedslab":
            return ZoneHvacVentilatedSlab()
        if internal_name.lower() == "zonehvac:ventilatedslab:slabgroup":
            return ZoneHvacVentilatedSlabSlabGroup()
        if internal_name.lower() == "airterminal:singleduct:uncontrolled":
            return AirTerminalSingleDuctUncontrolled()
        if internal_name.lower(
        ) == "airterminal:singleduct:constantvolume:reheat":
            return AirTerminalSingleDuctConstantVolumeReheat()
        if internal_name.lower() == "airterminal:singleduct:vav:noreheat":
            return AirTerminalSingleDuctVavNoReheat()
        if internal_name.lower() == "airterminal:singleduct:vav:reheat":
            return AirTerminalSingleDuctVavReheat()
        if internal_name.lower(
        ) == "airterminal:singleduct:vav:reheat:variablespeedfan":
            return AirTerminalSingleDuctVavReheatVariableSpeedFan()
        if internal_name.lower(
        ) == "airterminal:singleduct:vav:heatandcool:noreheat":
            return AirTerminalSingleDuctVavHeatAndCoolNoReheat()
        if internal_name.lower(
        ) == "airterminal:singleduct:vav:heatandcool:reheat":
            return AirTerminalSingleDuctVavHeatAndCoolReheat()
        if internal_name.lower() == "airterminal:singleduct:seriespiu:reheat":
            return AirTerminalSingleDuctSeriesPiuReheat()
        if internal_name.lower(
        ) == "airterminal:singleduct:parallelpiu:reheat":
            return AirTerminalSingleDuctParallelPiuReheat()
        if internal_name.lower(
        ) == "airterminal:singleduct:constantvolume:fourpipeinduction":
            return AirTerminalSingleDuctConstantVolumeFourPipeInduction()
        if internal_name.lower(
        ) == "airterminal:singleduct:constantvolume:cooledbeam":
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
        if internal_name.lower(
        ) == "coil:cooling:dx:twostagewithhumiditycontrolmode":
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
        if internal_name.lower(
        ) == "coil:cooling:watertoairheatpump:parameterestimation":
            return CoilCoolingWaterToAirHeatPumpParameterEstimation()
        if internal_name.lower(
        ) == "coil:heating:watertoairheatpump:parameterestimation":
            return CoilHeatingWaterToAirHeatPumpParameterEstimation()
        if internal_name.lower(
        ) == "coil:cooling:watertoairheatpump:equationfit":
            return CoilCoolingWaterToAirHeatPumpEquationFit()
        if internal_name.lower(
        ) == "coil:cooling:watertoairheatpump:variablespeedequationfit":
            return CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit()
        if internal_name.lower(
        ) == "coil:heating:watertoairheatpump:equationfit":
            return CoilHeatingWaterToAirHeatPumpEquationFit()
        if internal_name.lower(
        ) == "coil:heating:watertoairheatpump:variablespeedequationfit":
            return CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit()
        if internal_name.lower() == "coil:waterheating:airtowaterheatpump":
            return CoilWaterHeatingAirToWaterHeatPump()
        if internal_name.lower() == "coil:waterheating:desuperheater":
            return CoilWaterHeatingDesuperheater()
        if internal_name.lower() == "coilsystem:cooling:dx":
            return CoilSystemCoolingDx()
        if internal_name.lower() == "coilsystem:heating:dx":
            return CoilSystemHeatingDx()
        if internal_name.lower(
        ) == "coilsystem:cooling:water:heatexchangerassisted":
            return CoilSystemCoolingWaterHeatExchangerAssisted()
        if internal_name.lower(
        ) == "coilsystem:cooling:dx:heatexchangerassisted":
            return CoilSystemCoolingDxHeatExchangerAssisted()
        if internal_name.lower(
        ) == "coil:cooling:dx:singlespeed:thermalstorage":
            return CoilCoolingDxSingleSpeedThermalStorage()
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
        if internal_name.lower(
        ) == "heatexchanger:desiccant:balancedflow:performancedatatype1":
            return HeatExchangerDesiccantBalancedFlowPerformanceDataType1()
        if internal_name.lower() == "airloophvac:unitarysystem":
            return AirLoopHvacUnitarySystem()
        if internal_name.lower(
        ) == "unitarysystemperformance:heatpump:multispeed":
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
        if internal_name.lower(
        ) == "airloophvac:unitaryheatcool:vavchangeoverbypass":
            return AirLoopHvacUnitaryHeatCoolVavchangeoverBypass()
        if internal_name.lower(
        ) == "airloophvac:unitaryheatpump:airtoair:multispeed":
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
        if internal_name.lower(
        ) == "airloophvac:outdoorairsystem:equipmentlist":
            return AirLoopHvacOutdoorAirSystemEquipmentList()
        if internal_name.lower() == "airloophvac:outdoorairsystem":
            return AirLoopHvacOutdoorAirSystem()
        if internal_name.lower() == "outdoorair:mixer":
            return OutdoorAirMixer()
        if internal_name.lower() == "airloophvac:supplypath":
            return AirLoopHvacSupplyPath()
        if internal_name.lower() == "airloophvac:returnpath":
            return AirLoopHvacReturnPath()
        if internal_name.lower() == "branch":
            return Branch()
        if internal_name.lower() == "connectorlist":
            return ConnectorList()
        if internal_name.lower() == "outdoorair:node":
            return OutdoorAirNode()
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
        if internal_name.lower() == "temperingvalve":
            return TemperingValve()
        if internal_name.lower() == "loadprofile:plant":
            return LoadProfilePlant()
        if internal_name.lower() == "solarcollectorperformance:flatplate":
            return SolarCollectorPerformanceFlatPlate()
        if internal_name.lower() == "solarcollector:flatplate:water":
            return SolarCollectorFlatPlateWater()
        if internal_name.lower(
        ) == "solarcollectorperformance:photovoltaicthermal:simple":
            return SolarCollectorPerformancePhotovoltaicThermalSimple()
        if internal_name.lower() == "solarcollector:integralcollectorstorage":
            return SolarCollectorIntegralCollectorStorage()
        if internal_name.lower(
        ) == "solarcollectorperformance:integralcollectorstorage":
            return SolarCollectorPerformanceIntegralCollectorStorage()
        if internal_name.lower() == "solarcollector:unglazedtranspired":
            return SolarCollectorUnglazedTranspired()
        if internal_name.lower(
        ) == "solarcollector:unglazedtranspired:multisystem":
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
        if internal_name.lower(
        ) == "heatpump:watertowater:equationfit:heating":
            return HeatPumpWaterToWaterEquationFitHeating()
        if internal_name.lower(
        ) == "heatpump:watertowater:equationfit:cooling":
            return HeatPumpWaterToWaterEquationFitCooling()
        if internal_name.lower(
        ) == "heatpump:watertowater:parameterestimation:cooling":
            return HeatPumpWaterToWaterParameterEstimationCooling()
        if internal_name.lower(
        ) == "heatpump:watertowater:parameterestimation:heating":
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
        if internal_name.lower(
        ) == "plantequipmentoperation:outdoorrelativehumidity":
            return PlantEquipmentOperationOutdoorRelativeHumidity()
        if internal_name.lower() == "plantequipmentoperation:outdoordewpoint":
            return PlantEquipmentOperationOutdoorDewpoint()
        if internal_name.lower(
        ) == "plantequipmentoperation:componentsetpoint":
            return PlantEquipmentOperationComponentSetpoint()
        if internal_name.lower(
        ) == "plantequipmentoperation:outdoordrybulbdifference":
            return PlantEquipmentOperationOutdoorDryBulbDifference()
        if internal_name.lower(
        ) == "plantequipmentoperation:outdoorwetbulbdifference":
            return PlantEquipmentOperationOutdoorWetBulbDifference()
        if internal_name.lower(
        ) == "plantequipmentoperation:outdoordewpointdifference":
            return PlantEquipmentOperationOutdoorDewpointDifference()
        if internal_name.lower() == "plantequipmentoperationschemes":
            return PlantEquipmentOperationSchemes()
        if internal_name.lower() == "condenserequipmentoperationschemes":
            return CondenserEquipmentOperationSchemes()
        if internal_name.lower() == "energymanagementsystem:sensor":
            return EnergyManagementSystemSensor()
        if internal_name.lower() == "energymanagementsystem:actuator":
            return EnergyManagementSystemActuator()
        if internal_name.lower(
        ) == "energymanagementsystem:programcallingmanager":
            return EnergyManagementSystemProgramCallingManager()
        if internal_name.lower() == "energymanagementsystem:outputvariable":
            return EnergyManagementSystemOutputVariable()
        if internal_name.lower(
        ) == "energymanagementsystem:meteredoutputvariable":
            return EnergyManagementSystemMeteredOutputVariable()
        if internal_name.lower() == "energymanagementsystem:trendvariable":
            return EnergyManagementSystemTrendVariable()
        if internal_name.lower() == "energymanagementsystem:internalvariable":
            return EnergyManagementSystemInternalVariable()
        if internal_name.lower(
        ) == "energymanagementsystem:curveortableindexvariable":
            return EnergyManagementSystemCurveOrTableIndexVariable()
        if internal_name.lower(
        ) == "energymanagementsystem:constructionindexvariable":
            return EnergyManagementSystemConstructionIndexVariable()
        if internal_name.lower() == "externalinterface":
            return ExternalInterface()
        if internal_name.lower() == "externalinterface:schedule":
            return ExternalInterfaceSchedule()
        if internal_name.lower() == "externalinterface:variable":
            return ExternalInterfaceVariable()
        if internal_name.lower() == "externalinterface:actuator":
            return ExternalInterfaceActuator()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitimport":
            return ExternalInterfaceFunctionalMockupUnitImport()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitimport:from:variable":
            return ExternalInterfaceFunctionalMockupUnitImportFromVariable()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitimport:to:schedule":
            return ExternalInterfaceFunctionalMockupUnitImportToSchedule()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitimport:to:actuator":
            return ExternalInterfaceFunctionalMockupUnitImportToActuator()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitimport:to:variable":
            return ExternalInterfaceFunctionalMockupUnitImportToVariable()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitexport:from:variable":
            return ExternalInterfaceFunctionalMockupUnitExportFromVariable()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitexport:to:schedule":
            return ExternalInterfaceFunctionalMockupUnitExportToSchedule()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitexport:to:actuator":
            return ExternalInterfaceFunctionalMockupUnitExportToActuator()
        if internal_name.lower(
        ) == "externalinterface:functionalmockupunitexport:to:variable":
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
        if internal_name.lower(
        ) == "availabilitymanager:differentialthermostat":
            return AvailabilityManagerDifferentialThermostat()
        if internal_name.lower(
        ) == "availabilitymanager:hightemperatureturnoff":
            return AvailabilityManagerHighTemperatureTurnOff()
        if internal_name.lower(
        ) == "availabilitymanager:hightemperatureturnon":
            return AvailabilityManagerHighTemperatureTurnOn()
        if internal_name.lower(
        ) == "availabilitymanager:lowtemperatureturnoff":
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
        if internal_name.lower(
        ) == "setpointmanager:singlezone:humidity:minimum":
            return SetpointManagerSingleZoneHumidityMinimum()
        if internal_name.lower(
        ) == "setpointmanager:singlezone:humidity:maximum":
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
        if internal_name.lower(
        ) == "setpointmanager:multizone:heating:average":
            return SetpointManagerMultiZoneHeatingAverage()
        if internal_name.lower(
        ) == "setpointmanager:multizone:cooling:average":
            return SetpointManagerMultiZoneCoolingAverage()
        if internal_name.lower(
        ) == "setpointmanager:multizone:minimumhumidity:average":
            return SetpointManagerMultiZoneMinimumHumidityAverage()
        if internal_name.lower(
        ) == "setpointmanager:multizone:maximumhumidity:average":
            return SetpointManagerMultiZoneMaximumHumidityAverage()
        if internal_name.lower(
        ) == "setpointmanager:multizone:humidity:minimum":
            return SetpointManagerMultiZoneHumidityMinimum()
        if internal_name.lower(
        ) == "setpointmanager:multizone:humidity:maximum":
            return SetpointManagerMultiZoneHumidityMaximum()
        if internal_name.lower(
        ) == "setpointmanager:followoutdoorairtemperature":
            return SetpointManagerFollowOutdoorAirTemperature()
        if internal_name.lower(
        ) == "setpointmanager:followsystemnodetemperature":
            return SetpointManagerFollowSystemNodeTemperature()
        if internal_name.lower() == "setpointmanager:followgroundtemperature":
            return SetpointManagerFollowGroundTemperature()
        if internal_name.lower() == "setpointmanager:condenserenteringreset":
            return SetpointManagerCondenserEnteringReset()
        if internal_name.lower(
        ) == "setpointmanager:condenserenteringreset:ideal":
            return SetpointManagerCondenserEnteringResetIdeal()
        if internal_name.lower(
        ) == "setpointmanager:singlezone:onestagecooling":
            return SetpointManagerSingleZoneOneStageCooling()
        if internal_name.lower(
        ) == "setpointmanager:singlezone:onestageheating":
            return SetpointManagerSingleZoneOneStageHeating()
        if internal_name.lower() == "refrigeration:case":
            return RefrigerationCase()
        if internal_name.lower() == "refrigeration:compressorrack":
            return RefrigerationCompressorRack()
        if internal_name.lower() == "refrigeration:caseandwalkinlist":
            return RefrigerationCaseAndWalkInList()
        if internal_name.lower() == "refrigeration:condenser:aircooled":
            return RefrigerationCondenserAirCooled()
        if internal_name.lower(
        ) == "refrigeration:condenser:evaporativecooled":
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
        if internal_name.lower(
        ) == "photovoltaicperformance:equivalentone-diode":
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
        if internal_name.lower(
        ) == "generator:fuelcell:exhaustgastowaterheatexchanger":
            return GeneratorFuelCellExhaustGasToWaterHeatExchanger()
        if internal_name.lower() == "generator:fuelcell:electricalstorage":
            return GeneratorFuelCellElectricalStorage()
        if internal_name.lower() == "generator:fuelcell:inverter":
            return GeneratorFuelCellInverter()
        if internal_name.lower() == "generator:fuelcell:stackcooler":
            return GeneratorFuelCellStackCooler()
        if internal_name.lower() == "generator:microchp":
            return GeneratorMicroChp()
        if internal_name.lower(
        ) == "generator:microchp:nonnormalizedparameters":
            return GeneratorMicroChpNonNormalizedParameters()
        if internal_name.lower() == "generator:fuelsupply":
            return GeneratorFuelSupply()
        if internal_name.lower() == "generator:windturbine":
            return GeneratorWindTurbine()
        if internal_name.lower() == "electricloadcenter:generators":
            return ElectricLoadCenterGenerators()
        if internal_name.lower() == "electricloadcenter:inverter:simple":
            return ElectricLoadCenterInverterSimple()
        if internal_name.lower(
        ) == "electricloadcenter:inverter:functionofpower":
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
        if internal_name.lower(
        ) == "faultmodel:temperaturesensoroffset:outdoorair":
            return FaultModelTemperatureSensorOffsetOutdoorAir()
        if internal_name.lower(
        ) == "faultmodel:humiditysensoroffset:outdoorair":
            return FaultModelHumiditySensorOffsetOutdoorAir()
        if internal_name.lower(
        ) == "faultmodel:enthalpysensoroffset:outdoorair":
            return FaultModelEnthalpySensorOffsetOutdoorAir()
        if internal_name.lower(
        ) == "faultmodel:pressuresensoroffset:outdoorair":
            return FaultModelPressureSensorOffsetOutdoorAir()
        if internal_name.lower(
        ) == "faultmodel:temperaturesensoroffset:returnair":
            return FaultModelTemperatureSensorOffsetReturnAir()
        if internal_name.lower(
        ) == "faultmodel:enthalpysensoroffset:returnair":
            return FaultModelEnthalpySensorOffsetReturnAir()
        if internal_name.lower() == "faultmodel:fouling:coil":
            return FaultModelFoulingCoil()
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
        raise ValueError(
            "No DataDictionary known for {}".format(internal_name))

    def read(self, path):
        """Read IDF data from path

           Args:
               path (str): path to read data from
        """
        with open(path, "r") as f:
            current_object = None
            current_vals = []

            for line in f:

                line = line.strip()
                if re.search(r"^\s*!", line) is not None:
                    continue
                if len(line) == 0:
                    continue

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
                            print "{} is not a valid data dictionary name".format(current_object)
#                             raise ValueError("{} is not a valid data dictionary name".format(current_object))
                        else:
                            data_object = self._create_datadict(current_object)
                            data_object.read(current_vals)
                            self._data[current_object].append(data_object)

                        current_object = None
                        current_vals = []
