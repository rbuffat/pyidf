""" Data objects in group "Solar Collectors"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class SolarCollectorPerformanceFlatPlate(DataObject):

    """ Corresponds to IDD object `SolarCollectorPerformance:FlatPlate`
        Thermal and optical performance parameters for a single flat plate solar collector
        module. These parameters are based on the testing methodologies described in ASHRAE
        Standards 93 and 96 which are used Solar Rating and Certification Corporation (SRCC)
        Directory of SRCC Certified Solar Collector Ratings. See EnergyPlus DataSets file
        SolarCollectors.idf.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'gross area',
                                       {'name': u'Gross Area',
                                        'pyname': u'gross_area',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'test fluid',
                                       {'name': u'Test Fluid',
                                        'pyname': u'test_fluid',
                                        'default': u'Water',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Water'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'test flow rate',
                                       {'name': u'Test Flow Rate',
                                        'pyname': u'test_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'test correlation type',
                                       {'name': u'Test Correlation Type',
                                        'pyname': u'test_correlation_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Inlet',
                                                            u'Average',
                                                            u'Outlet'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'coefficient 1 of efficiency equation',
                                       {'name': u'Coefficient 1 of Efficiency Equation',
                                        'pyname': u'coefficient_1_of_efficiency_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'coefficient 2 of efficiency equation',
                                       {'name': u'Coefficient 2 of Efficiency Equation',
                                        'pyname': u'coefficient_2_of_efficiency_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'coefficient 3 of efficiency equation',
                                       {'name': u'Coefficient 3 of Efficiency Equation',
                                        'pyname': u'coefficient_3_of_efficiency_equation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K2'}),
                                      (u'coefficient 2 of incident angle modifier',
                                       {'name': u'Coefficient 2 of Incident Angle Modifier',
                                        'pyname': u'coefficient_2_of_incident_angle_modifier',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient 3 of incident angle modifier',
                                       {'name': u'Coefficient 3 of Incident Angle Modifier',
                                        'pyname': u'coefficient_3_of_incident_angle_modifier',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollectorPerformance:FlatPlate',
               'pyname': u'SolarCollectorPerformanceFlatPlate',
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
    def gross_area(self):
        """field `Gross Area`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Gross Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gross_area` or None if not set

        """
        return self["Gross Area"]

    @gross_area.setter
    def gross_area(self, value=None):
        """Corresponds to IDD field `Gross Area`"""
        self["Gross Area"] = value

    @property
    def test_fluid(self):
        """field `Test Fluid`

        |  Default value: Water

        Args:
            value (str): value for IDD Field `Test Fluid`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `test_fluid` or None if not set

        """
        return self["Test Fluid"]

    @test_fluid.setter
    def test_fluid(self, value="Water"):
        """Corresponds to IDD field `Test Fluid`"""
        self["Test Fluid"] = value

    @property
    def test_flow_rate(self):
        """field `Test Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Test Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `test_flow_rate` or None if not set

        """
        return self["Test Flow Rate"]

    @test_flow_rate.setter
    def test_flow_rate(self, value=None):
        """Corresponds to IDD field `Test Flow Rate`"""
        self["Test Flow Rate"] = value

    @property
    def test_correlation_type(self):
        """field `Test Correlation Type`

        Args:
            value (str): value for IDD Field `Test Correlation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `test_correlation_type` or None if not set

        """
        return self["Test Correlation Type"]

    @test_correlation_type.setter
    def test_correlation_type(self, value=None):
        """Corresponds to IDD field `Test Correlation Type`"""
        self["Test Correlation Type"] = value

    @property
    def coefficient_1_of_efficiency_equation(self):
        """field `Coefficient 1 of Efficiency Equation`

        |  Y-intercept term
        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Coefficient 1 of Efficiency Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient_1_of_efficiency_equation` or None if not set

        """
        return self["Coefficient 1 of Efficiency Equation"]

    @coefficient_1_of_efficiency_equation.setter
    def coefficient_1_of_efficiency_equation(self, value=None):
        """Corresponds to IDD field `Coefficient 1 of Efficiency Equation`"""
        self["Coefficient 1 of Efficiency Equation"] = value

    @property
    def coefficient_2_of_efficiency_equation(self):
        """field `Coefficient 2 of Efficiency Equation`

        |  1st Order term
        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Coefficient 2 of Efficiency Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient_2_of_efficiency_equation` or None if not set

        """
        return self["Coefficient 2 of Efficiency Equation"]

    @coefficient_2_of_efficiency_equation.setter
    def coefficient_2_of_efficiency_equation(self, value=None):
        """Corresponds to IDD field `Coefficient 2 of Efficiency Equation`"""
        self["Coefficient 2 of Efficiency Equation"] = value

    @property
    def coefficient_3_of_efficiency_equation(self):
        """field `Coefficient 3 of Efficiency Equation`

        |  2nd order term
        |  Units: W/m2-K2

        Args:
            value (float): value for IDD Field `Coefficient 3 of Efficiency Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient_3_of_efficiency_equation` or None if not set

        """
        return self["Coefficient 3 of Efficiency Equation"]

    @coefficient_3_of_efficiency_equation.setter
    def coefficient_3_of_efficiency_equation(self, value=None):
        """Corresponds to IDD field `Coefficient 3 of Efficiency Equation`"""
        self["Coefficient 3 of Efficiency Equation"] = value

    @property
    def coefficient_2_of_incident_angle_modifier(self):
        """field `Coefficient 2 of Incident Angle Modifier`

        |  1st order term

        Args:
            value (float): value for IDD Field `Coefficient 2 of Incident Angle Modifier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient_2_of_incident_angle_modifier` or None if not set

        """
        return self["Coefficient 2 of Incident Angle Modifier"]

    @coefficient_2_of_incident_angle_modifier.setter
    def coefficient_2_of_incident_angle_modifier(self, value=None):
        """Corresponds to IDD field `Coefficient 2 of Incident Angle
        Modifier`"""
        self["Coefficient 2 of Incident Angle Modifier"] = value

    @property
    def coefficient_3_of_incident_angle_modifier(self):
        """field `Coefficient 3 of Incident Angle Modifier`

        |  2nd order term

        Args:
            value (float): value for IDD Field `Coefficient 3 of Incident Angle Modifier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient_3_of_incident_angle_modifier` or None if not set

        """
        return self["Coefficient 3 of Incident Angle Modifier"]

    @coefficient_3_of_incident_angle_modifier.setter
    def coefficient_3_of_incident_angle_modifier(self, value=None):
        """Corresponds to IDD field `Coefficient 3 of Incident Angle
        Modifier`"""
        self["Coefficient 3 of Incident Angle Modifier"] = value




class SolarCollectorFlatPlateWater(DataObject):

    """ Corresponds to IDD object `SolarCollector:FlatPlate:Water`
        Flat plate water solar collector (single glazed, unglazed, or evacuated tube).
        Thermal and optical properties are taken from the referenced
        SolarCollectorPerformance:FlatPlate object. Collector tilt, azimuth, and gross area
        are taken from the referenced building surface or shading surface. The collector
        surface participates normally in all shading calculations.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'solarcollectorperformance name',
                                       {'name': u'SolarCollectorPerformance Name',
                                        'pyname': u'solarcollectorperformance_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum flow rate',
                                       {'name': u'Maximum Flow Rate',
                                        'pyname': u'maximum_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollector:FlatPlate:Water',
               'pyname': u'SolarCollectorFlatPlateWater',
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
    def solarcollectorperformance_name(self):
        """field `SolarCollectorPerformance Name`

        Args:
            value (str): value for IDD Field `SolarCollectorPerformance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solarcollectorperformance_name` or None if not set

        """
        return self["SolarCollectorPerformance Name"]

    @solarcollectorperformance_name.setter
    def solarcollectorperformance_name(self, value=None):
        """Corresponds to IDD field `SolarCollectorPerformance Name`"""
        self["SolarCollectorPerformance Name"] = value

    @property
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def inlet_node_name(self):
        """field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value

    @property
    def maximum_flow_rate(self):
        """field `Maximum Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`"""
        self["Maximum Flow Rate"] = value




class SolarCollectorFlatPlatePhotovoltaicThermal(DataObject):

    """ Corresponds to IDD object `SolarCollector:FlatPlate:PhotovoltaicThermal`
        Models hybrid photovoltaic-thermal (PVT) solar collectors that convert incident solar
        energy into both electricity and useful thermal energy by heating air or water.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'photovoltaic-thermal model performance name',
                                       {'name': u'Photovoltaic-Thermal Model Performance Name',
                                        'pyname': u'photovoltaicthermal_model_performance_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'photovoltaic name',
                                       {'name': u'Photovoltaic Name',
                                        'pyname': u'photovoltaic_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thermal working fluid type',
                                       {'name': u'Thermal Working Fluid Type',
                                        'pyname': u'thermal_working_fluid_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Water',
                                                            u'Air'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
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
                                      (u'design flow rate',
                                       {'name': u'Design Flow Rate',
                                        'pyname': u'design_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollector:FlatPlate:PhotovoltaicThermal',
               'pyname': u'SolarCollectorFlatPlatePhotovoltaicThermal',
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
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def photovoltaicthermal_model_performance_name(self):
        """field `Photovoltaic-Thermal Model Performance Name`


        Args:
            value (str): value for IDD Field `Photovoltaic-Thermal Model Performance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `photovoltaicthermal_model_performance_name` or None if not set
        """
        return self["Photovoltaic-Thermal Model Performance Name"]

    @photovoltaicthermal_model_performance_name.setter
    def photovoltaicthermal_model_performance_name(self, value=None):
        """  Corresponds to IDD field `Photovoltaic-Thermal Model Performance Name`

        """
        self["Photovoltaic-Thermal Model Performance Name"] = value

    @property
    def photovoltaic_name(self):
        """field `Photovoltaic Name`

        |  Enter the name of a Generator:Photovoltaic object.

        Args:
            value (str): value for IDD Field `Photovoltaic Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `photovoltaic_name` or None if not set

        """
        return self["Photovoltaic Name"]

    @photovoltaic_name.setter
    def photovoltaic_name(self, value=None):
        """Corresponds to IDD field `Photovoltaic Name`"""
        self["Photovoltaic Name"] = value

    @property
    def thermal_working_fluid_type(self):
        """field `Thermal Working Fluid Type`

        Args:
            value (str): value for IDD Field `Thermal Working Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_working_fluid_type` or None if not set

        """
        return self["Thermal Working Fluid Type"]

    @thermal_working_fluid_type.setter
    def thermal_working_fluid_type(self, value=None):
        """Corresponds to IDD field `Thermal Working Fluid Type`"""
        self["Thermal Working Fluid Type"] = value

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
    def design_flow_rate(self):
        """field `Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_flow_rate` or None if not set

        """
        return self["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Flow Rate`"""
        self["Design Flow Rate"] = value




class SolarCollectorPerformancePhotovoltaicThermalSimple(DataObject):

    """ Corresponds to IDD object `SolarCollectorPerformance:PhotovoltaicThermal:Simple`
        Thermal performance parameters for a hybrid photovoltaic-thermal (PVT) solar collector.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fraction of surface area with active thermal collector',
                                       {'name': u'Fraction of Surface Area with Active Thermal Collector',
                                        'pyname': u'fraction_of_surface_area_with_active_thermal_collector',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'thermal conversion efficiency input mode type',
                                       {'name': u'Thermal Conversion Efficiency Input Mode Type',
                                        'pyname': u'thermal_conversion_efficiency_input_mode_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'value for thermal conversion efficiency if fixed',
                                       {'name': u'Value for Thermal Conversion Efficiency if Fixed',
                                        'pyname': u'value_for_thermal_conversion_efficiency_if_fixed',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'thermal conversion efficiency schedule name',
                                       {'name': u'Thermal Conversion Efficiency Schedule Name',
                                        'pyname': u'thermal_conversion_efficiency_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'front surface emittance',
                                       {'name': u'Front Surface Emittance',
                                        'pyname': u'front_surface_emittance',
                                        'default': 0.84,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollectorPerformance:PhotovoltaicThermal:Simple',
               'pyname': u'SolarCollectorPerformancePhotovoltaicThermalSimple',
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
    def fraction_of_surface_area_with_active_thermal_collector(self):
        """field `Fraction of Surface Area with Active Thermal Collector`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Surface Area with Active Thermal Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_surface_area_with_active_thermal_collector` or None if not set

        """
        return self["Fraction of Surface Area with Active Thermal Collector"]

    @fraction_of_surface_area_with_active_thermal_collector.setter
    def fraction_of_surface_area_with_active_thermal_collector(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Surface Area with Active
        Thermal Collector`"""
        self["Fraction of Surface Area with Active Thermal Collector"] = value

    @property
    def thermal_conversion_efficiency_input_mode_type(self):
        """field `Thermal Conversion Efficiency Input Mode Type`

        Args:
            value (str): value for IDD Field `Thermal Conversion Efficiency Input Mode Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_conversion_efficiency_input_mode_type` or None if not set

        """
        return self["Thermal Conversion Efficiency Input Mode Type"]

    @thermal_conversion_efficiency_input_mode_type.setter
    def thermal_conversion_efficiency_input_mode_type(self, value=None):
        """Corresponds to IDD field `Thermal Conversion Efficiency Input Mode
        Type`"""
        self["Thermal Conversion Efficiency Input Mode Type"] = value

    @property
    def value_for_thermal_conversion_efficiency_if_fixed(self):
        """field `Value for Thermal Conversion Efficiency if Fixed`

        |  Efficiency = (thermal power generated [W])/(incident solar[W])
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Value for Thermal Conversion Efficiency if Fixed`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `value_for_thermal_conversion_efficiency_if_fixed` or None if not set

        """
        return self["Value for Thermal Conversion Efficiency if Fixed"]

    @value_for_thermal_conversion_efficiency_if_fixed.setter
    def value_for_thermal_conversion_efficiency_if_fixed(self, value=None):
        """Corresponds to IDD field `Value for Thermal Conversion Efficiency if
        Fixed`"""
        self["Value for Thermal Conversion Efficiency if Fixed"] = value

    @property
    def thermal_conversion_efficiency_schedule_name(self):
        """field `Thermal Conversion Efficiency Schedule Name`

        Args:
            value (str): value for IDD Field `Thermal Conversion Efficiency Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_conversion_efficiency_schedule_name` or None if not set

        """
        return self["Thermal Conversion Efficiency Schedule Name"]

    @thermal_conversion_efficiency_schedule_name.setter
    def thermal_conversion_efficiency_schedule_name(self, value=None):
        """Corresponds to IDD field `Thermal Conversion Efficiency Schedule
        Name`"""
        self["Thermal Conversion Efficiency Schedule Name"] = value

    @property
    def front_surface_emittance(self):
        """field `Front Surface Emittance`

        |  Default value: 0.84
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Front Surface Emittance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `front_surface_emittance` or None if not set

        """
        return self["Front Surface Emittance"]

    @front_surface_emittance.setter
    def front_surface_emittance(self, value=0.84):
        """Corresponds to IDD field `Front Surface Emittance`"""
        self["Front Surface Emittance"] = value




class SolarCollectorIntegralCollectorStorage(DataObject):

    """ Corresponds to IDD object `SolarCollector:IntegralCollectorStorage`
        Glazed solar collector with integral storage unit. Thermal and optical properties are
        taken from the referenced SolarCollectorPerformance:IntegralCollectorStorage object.
        Collector tilt, azimuth, and gross area are taken from the referenced building surface
        or shading surface. The collector surface participates normally in all shading
        calculations.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'integralcollectorstorageparameters name',
                                       {'name': u'IntegralCollectorStorageParameters Name',
                                        'pyname': u'integralcollectorstorageparameters_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'bottom surface boundary conditions type',
                                       {'name': u'Bottom Surface Boundary Conditions Type',
                                        'pyname': u'bottom_surface_boundary_conditions_type',
                                        'default': u'AmbientAir',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'OtherSideConditionsModel',
                                                            u'AmbientAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'boundary condition model name',
                                       {'name': u'Boundary Condition Model Name',
                                        'pyname': u'boundary_condition_model_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum flow rate',
                                       {'name': u'Maximum Flow Rate',
                                        'pyname': u'maximum_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollector:IntegralCollectorStorage',
               'pyname': u'SolarCollectorIntegralCollectorStorage',
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
    def integralcollectorstorageparameters_name(self):
        """field `IntegralCollectorStorageParameters Name`

        Args:
            value (str): value for IDD Field `IntegralCollectorStorageParameters Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `integralcollectorstorageparameters_name` or None if not set

        """
        return self["IntegralCollectorStorageParameters Name"]

    @integralcollectorstorageparameters_name.setter
    def integralcollectorstorageparameters_name(self, value=None):
        """Corresponds to IDD field `IntegralCollectorStorageParameters
        Name`"""
        self["IntegralCollectorStorageParameters Name"] = value

    @property
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def bottom_surface_boundary_conditions_type(self):
        """field `Bottom Surface Boundary Conditions Type`

        |  Default value: AmbientAir

        Args:
            value (str): value for IDD Field `Bottom Surface Boundary Conditions Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `bottom_surface_boundary_conditions_type` or None if not set

        """
        return self["Bottom Surface Boundary Conditions Type"]

    @bottom_surface_boundary_conditions_type.setter
    def bottom_surface_boundary_conditions_type(self, value="AmbientAir"):
        """Corresponds to IDD field `Bottom Surface Boundary Conditions
        Type`"""
        self["Bottom Surface Boundary Conditions Type"] = value

    @property
    def boundary_condition_model_name(self):
        """field `Boundary Condition Model Name`

        |  Enter the name of a SurfaceProperty:OtherSideConditionsModel
        |  object. Specified only if the boundary condition type is
        |  OtherSideConditionsModel, otherwise leave it blank

        Args:
            value (str): value for IDD Field `Boundary Condition Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `boundary_condition_model_name` or None if not set

        """
        return self["Boundary Condition Model Name"]

    @boundary_condition_model_name.setter
    def boundary_condition_model_name(self, value=None):
        """Corresponds to IDD field `Boundary Condition Model Name`"""
        self["Boundary Condition Model Name"] = value

    @property
    def inlet_node_name(self):
        """field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value

    @property
    def maximum_flow_rate(self):
        """field `Maximum Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_flow_rate` or None if not set

        """
        return self["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Flow Rate`"""
        self["Maximum Flow Rate"] = value




class SolarCollectorPerformanceIntegralCollectorStorage(DataObject):

    """ Corresponds to IDD object `SolarCollectorPerformance:IntegralCollectorStorage`
        Thermal and optical performance parameters for a single glazed solar collector with
        integral storage unit.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'ics collector type',
                                       {'name': u'ICS Collector Type',
                                        'pyname': u'ics_collector_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'RectangularTank'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'gross area',
                                       {'name': u'Gross Area',
                                        'pyname': u'gross_area',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'collector water volume',
                                       {'name': u'Collector Water Volume',
                                        'pyname': u'collector_water_volume',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'bottom heat loss conductance',
                                       {'name': u'Bottom Heat Loss Conductance',
                                        'pyname': u'bottom_heat_loss_conductance',
                                        'default': 0.4,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'side heat loss conductance',
                                       {'name': u'Side Heat Loss Conductance',
                                        'pyname': u'side_heat_loss_conductance',
                                        'default': 0.6,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'aspect ratio',
                                       {'name': u'Aspect Ratio',
                                        'pyname': u'aspect_ratio',
                                        'default': 0.8,
                                        'minimum>': 0.5,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'm'}),
                                      (u'collector side height',
                                       {'name': u'Collector Side Height',
                                        'pyname': u'collector_side_height',
                                        'default': 0.2,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 0.3,
                                        'unit': u'm'}),
                                      (u'thermal mass of absorber plate',
                                       {'name': u'Thermal Mass of Absorber Plate',
                                        'pyname': u'thermal_mass_of_absorber_plate',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/m2-K'}),
                                      (u'number of covers',
                                       {'name': u'Number of Covers',
                                        'pyname': u'number_of_covers',
                                        'default': 2,
                                        'maximum': 2,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'cover spacing',
                                       {'name': u'Cover Spacing',
                                        'pyname': u'cover_spacing',
                                        'default': 0.05,
                                        'minimum>': 0.0,
                                        'maximum': 0.2,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'refractive index of outer cover',
                                       {'name': u'Refractive Index of Outer Cover',
                                        'pyname': u'refractive_index_of_outer_cover',
                                        'default': 1.526,
                                        'maximum': 2.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'extinction coefficient times thickness of outer cover',
                                       {'name': u'Extinction Coefficient Times Thickness of Outer Cover',
                                        'pyname': u'extinction_coefficient_times_thickness_of_outer_cover',
                                        'default': 0.045,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'emissivity of outer cover',
                                       {'name': u'Emissivity of Outer Cover',
                                        'pyname': u'emissivity_of_outer_cover',
                                        'default': 0.88,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'refractive index of inner cover',
                                       {'name': u'Refractive Index of Inner Cover',
                                        'pyname': u'refractive_index_of_inner_cover',
                                        'default': 1.37,
                                        'maximum': 2.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'extinction coefficient times thickness of the inner cover',
                                       {'name': u'Extinction Coefficient Times Thickness of the inner Cover',
                                        'pyname': u'extinction_coefficient_times_thickness_of_the_inner_cover',
                                        'default': 0.008,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'emissivity of inner cover',
                                       {'name': u'Emissivity of Inner Cover',
                                        'pyname': u'emissivity_of_inner_cover',
                                        'default': 0.88,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'absorptance of absorber plate',
                                       {'name': u'Absorptance of Absorber Plate',
                                        'pyname': u'absorptance_of_absorber_plate',
                                        'default': 0.96,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'}),
                                      (u'emissivity of absorber plate',
                                       {'name': u'Emissivity of Absorber Plate',
                                        'pyname': u'emissivity_of_absorber_plate',
                                        'default': 0.3,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'maximum<': 1.0,
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollectorPerformance:IntegralCollectorStorage',
               'pyname': u'SolarCollectorPerformanceIntegralCollectorStorage',
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
    def ics_collector_type(self):
        """field `ICS Collector Type`

        |  Currently only RectangularTank ICS collector type is available.

        Args:
            value (str): value for IDD Field `ICS Collector Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ics_collector_type` or None if not set

        """
        return self["ICS Collector Type"]

    @ics_collector_type.setter
    def ics_collector_type(self, value=None):
        """Corresponds to IDD field `ICS Collector Type`"""
        self["ICS Collector Type"] = value

    @property
    def gross_area(self):
        """field `Gross Area`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Gross Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gross_area` or None if not set

        """
        return self["Gross Area"]

    @gross_area.setter
    def gross_area(self, value=None):
        """Corresponds to IDD field `Gross Area`"""
        self["Gross Area"] = value

    @property
    def collector_water_volume(self):
        """field `Collector Water Volume`

        |  Units: m3

        Args:
            value (float): value for IDD Field `Collector Water Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `collector_water_volume` or None if not set

        """
        return self["Collector Water Volume"]

    @collector_water_volume.setter
    def collector_water_volume(self, value=None):
        """Corresponds to IDD field `Collector Water Volume`"""
        self["Collector Water Volume"] = value

    @property
    def bottom_heat_loss_conductance(self):
        """field `Bottom Heat Loss Conductance`

        |  Heat loss conductance of the collector bottom insulation
        |  Units: W/m2-K
        |  Default value: 0.4

        Args:
            value (float): value for IDD Field `Bottom Heat Loss Conductance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `bottom_heat_loss_conductance` or None if not set

        """
        return self["Bottom Heat Loss Conductance"]

    @bottom_heat_loss_conductance.setter
    def bottom_heat_loss_conductance(self, value=0.4):
        """Corresponds to IDD field `Bottom Heat Loss Conductance`"""
        self["Bottom Heat Loss Conductance"] = value

    @property
    def side_heat_loss_conductance(self):
        """field `Side Heat Loss Conductance`

        |  heat loss conductance of the collector side insulation
        |  Units: W/m2-K
        |  Default value: 0.6

        Args:
            value (float): value for IDD Field `Side Heat Loss Conductance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `side_heat_loss_conductance` or None if not set

        """
        return self["Side Heat Loss Conductance"]

    @side_heat_loss_conductance.setter
    def side_heat_loss_conductance(self, value=0.6):
        """Corresponds to IDD field `Side Heat Loss Conductance`"""
        self["Side Heat Loss Conductance"] = value

    @property
    def aspect_ratio(self):
        """field `Aspect Ratio`

        |  This value is ratio of the width (short side) to length
        |  (long side of) of the collector.  Used to calculate the
        |  perimeter of the collector
        |  Units: m
        |  Default value: 0.8
        |  value > 0.5
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Aspect Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `aspect_ratio` or None if not set

        """
        return self["Aspect Ratio"]

    @aspect_ratio.setter
    def aspect_ratio(self, value=0.8):
        """Corresponds to IDD field `Aspect Ratio`"""
        self["Aspect Ratio"] = value

    @property
    def collector_side_height(self):
        """field `Collector Side Height`

        |  This value is used to estimate collector side area for the heat
        |  loss calculation through the collector side
        |  Units: m
        |  Default value: 0.2
        |  value < 0.3

        Args:
            value (float): value for IDD Field `Collector Side Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `collector_side_height` or None if not set

        """
        return self["Collector Side Height"]

    @collector_side_height.setter
    def collector_side_height(self, value=0.2):
        """Corresponds to IDD field `Collector Side Height`"""
        self["Collector Side Height"] = value

    @property
    def thermal_mass_of_absorber_plate(self):
        """field `Thermal Mass of Absorber Plate`

        |  Calculated from the specific heat, density and thickness
        |  of the absorber plate.
        |  Units: J/m2-K

        Args:
            value (float): value for IDD Field `Thermal Mass of Absorber Plate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_mass_of_absorber_plate` or None if not set

        """
        return self["Thermal Mass of Absorber Plate"]

    @thermal_mass_of_absorber_plate.setter
    def thermal_mass_of_absorber_plate(self, value=None):
        """Corresponds to IDD field `Thermal Mass of Absorber Plate`"""
        self["Thermal Mass of Absorber Plate"] = value

    @property
    def number_of_covers(self):
        """field `Number of Covers`

        |  Number of transparent covers. Common practice is to use low-iron
        |  glass as the outer cover and very thin transparent sheet such as
        |  Teflon as the inner cover.
        |  Default value: 2
        |  value >= 1
        |  value <= 2

        Args:
            value (int): value for IDD Field `Number of Covers`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_covers` or None if not set

        """
        return self["Number of Covers"]

    @number_of_covers.setter
    def number_of_covers(self, value=2):
        """Corresponds to IDD field `Number of Covers`"""
        self["Number of Covers"] = value

    @property
    def cover_spacing(self):
        """field `Cover Spacing`

        |  The gap between the transparent covers and between the inner cover
        |  and the absorber plate
        |  Units: m
        |  Default value: 0.05
        |  value <= 0.2

        Args:
            value (float): value for IDD Field `Cover Spacing`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cover_spacing` or None if not set

        """
        return self["Cover Spacing"]

    @cover_spacing.setter
    def cover_spacing(self, value=0.05):
        """Corresponds to IDD field `Cover Spacing`"""
        self["Cover Spacing"] = value

    @property
    def refractive_index_of_outer_cover(self):
        """field `Refractive Index of Outer Cover`

        |  Refractive index of outer cover. Typically low-iron glass is used
        |  as the outer cover material, and used as the default outer cover
        |  with a value of 1.526.
        |  Units: dimensionless
        |  Default value: 1.526
        |  value >= 1.0
        |  value <= 2.0

        Args:
            value (float): value for IDD Field `Refractive Index of Outer Cover`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `refractive_index_of_outer_cover` or None if not set

        """
        return self["Refractive Index of Outer Cover"]

    @refractive_index_of_outer_cover.setter
    def refractive_index_of_outer_cover(self, value=1.526):
        """Corresponds to IDD field `Refractive Index of Outer Cover`"""
        self["Refractive Index of Outer Cover"] = value

    @property
    def extinction_coefficient_times_thickness_of_outer_cover(self):
        """field `Extinction Coefficient Times Thickness of Outer Cover`

        |  Clear glass has extinction coefficient of about 15 [1/m]
        |  and with thickness of 3.0mm, the product of the extinction
        |  coefficient and thickness becomes 0.045 (=15 * 0.003)
        |  Units: dimensionless
        |  Default value: 0.045

        Args:
            value (float): value for IDD Field `Extinction Coefficient Times Thickness of Outer Cover`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `extinction_coefficient_times_thickness_of_outer_cover` or None if not set

        """
        return self["Extinction Coefficient Times Thickness of Outer Cover"]

    @extinction_coefficient_times_thickness_of_outer_cover.setter
    def extinction_coefficient_times_thickness_of_outer_cover(
            self,
            value=0.045):
        """Corresponds to IDD field `Extinction Coefficient Times Thickness of
        Outer Cover`"""
        self["Extinction Coefficient Times Thickness of Outer Cover"] = value

    @property
    def emissivity_of_outer_cover(self):
        """field `Emissivity of Outer Cover`

        |  Thermal emissivity of the outer cover, commonly glass is used as
        |  the out collector cover material.
        |  Units: dimensionless
        |  Default value: 0.88
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Emissivity of Outer Cover`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `emissivity_of_outer_cover` or None if not set

        """
        return self["Emissivity of Outer Cover"]

    @emissivity_of_outer_cover.setter
    def emissivity_of_outer_cover(self, value=0.88):
        """Corresponds to IDD field `Emissivity of Outer Cover`"""
        self["Emissivity of Outer Cover"] = value

    @property
    def refractive_index_of_inner_cover(self):
        """field `Refractive Index of Inner Cover`

        |  Typical material is very thin sheet of Teflon (PTFE). The default
        |  value is refractive index of Teflon.
        |  Units: dimensionless
        |  Default value: 1.37
        |  value >= 1.0
        |  value <= 2.0

        Args:
            value (float): value for IDD Field `Refractive Index of Inner Cover`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `refractive_index_of_inner_cover` or None if not set

        """
        return self["Refractive Index of Inner Cover"]

    @refractive_index_of_inner_cover.setter
    def refractive_index_of_inner_cover(self, value=1.37):
        """Corresponds to IDD field `Refractive Index of Inner Cover`"""
        self["Refractive Index of Inner Cover"] = value

    @property
    def extinction_coefficient_times_thickness_of_the_inner_cover(self):
        """field `Extinction Coefficient Times Thickness of the inner Cover`

        |  Default inner cover is very thin sheet of Teflon with
        |  extinction coefficient of approximately 40.0 and a thickness
        |  0.2mm yields a default value of 0.008.
        |  Units: dimensionless
        |  Default value: 0.008

        Args:
            value (float): value for IDD Field `Extinction Coefficient Times Thickness of the inner Cover`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `extinction_coefficient_times_thickness_of_the_inner_cover` or None if not set

        """
        return self[
            "Extinction Coefficient Times Thickness of the inner Cover"]

    @extinction_coefficient_times_thickness_of_the_inner_cover.setter
    def extinction_coefficient_times_thickness_of_the_inner_cover(
            self,
            value=0.008):
        """Corresponds to IDD field `Extinction Coefficient Times Thickness of
        the inner Cover`"""
        self[
            "Extinction Coefficient Times Thickness of the inner Cover"] = value

    @property
    def emissivity_of_inner_cover(self):
        """field `Emissivity of Inner Cover`

        |  Thermal emissivity of the inner cover material
        |  Units: dimensionless
        |  Default value: 0.88
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Emissivity of Inner Cover`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `emissivity_of_inner_cover` or None if not set

        """
        return self["Emissivity of Inner Cover"]

    @emissivity_of_inner_cover.setter
    def emissivity_of_inner_cover(self, value=0.88):
        """Corresponds to IDD field `Emissivity of Inner Cover`"""
        self["Emissivity of Inner Cover"] = value

    @property
    def absorptance_of_absorber_plate(self):
        """field `Absorptance of Absorber Plate`

        |  The absorber plate solar absorptance.  Copper is assumed as
        |  the default absorber plate.
        |  Units: dimensionless
        |  Default value: 0.96
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Absorptance of Absorber Plate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `absorptance_of_absorber_plate` or None if not set

        """
        return self["Absorptance of Absorber Plate"]

    @absorptance_of_absorber_plate.setter
    def absorptance_of_absorber_plate(self, value=0.96):
        """Corresponds to IDD field `Absorptance of Absorber Plate`"""
        self["Absorptance of Absorber Plate"] = value

    @property
    def emissivity_of_absorber_plate(self):
        """field `Emissivity of Absorber Plate`

        |  Thermal emissivity of the absorber plate
        |  Units: dimensionless
        |  Default value: 0.3
        |  value < 1.0

        Args:
            value (float): value for IDD Field `Emissivity of Absorber Plate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `emissivity_of_absorber_plate` or None if not set

        """
        return self["Emissivity of Absorber Plate"]

    @emissivity_of_absorber_plate.setter
    def emissivity_of_absorber_plate(self, value=0.3):
        """Corresponds to IDD field `Emissivity of Absorber Plate`"""
        self["Emissivity of Absorber Plate"] = value




class SolarCollectorUnglazedTranspired(DataObject):

    """ Corresponds to IDD object `SolarCollector:UnglazedTranspired`
        Unglazed transpired solar collector (UTSC) used to condition outdoor air. This type of
        collector is generally used to heat air drawn through perforated absorbers and also
        recover heat conducted out through the underlying surface. This object represents a
        single collector attached to one or more building or shading surfaces and to one or
        more outdoor air systems.
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
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
                                        'type': u'alpha'}),
                                      (u'boundary conditions model name',
                                       {'name': u'Boundary Conditions Model Name',
                                        'pyname': u'boundary_conditions_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint node name',
                                       {'name': u'Setpoint Node Name',
                                        'pyname': u'setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone node name',
                                       {'name': u'Zone Node Name',
                                        'pyname': u'zone_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'free heating setpoint schedule name',
                                       {'name': u'Free Heating Setpoint Schedule Name',
                                        'pyname': u'free_heating_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'diameter of perforations in collector',
                                       {'name': u'Diameter of Perforations in Collector',
                                        'pyname': u'diameter_of_perforations_in_collector',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'distance between perforations in collector',
                                       {'name': u'Distance Between Perforations in Collector',
                                        'pyname': u'distance_between_perforations_in_collector',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'thermal emissivity of collector surface',
                                       {'name': u'Thermal Emissivity of Collector Surface',
                                        'pyname': u'thermal_emissivity_of_collector_surface',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'solar absorbtivity of collector surface',
                                       {'name': u'Solar Absorbtivity of Collector Surface',
                                        'pyname': u'solar_absorbtivity_of_collector_surface',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'effective overall height of collector',
                                       {'name': u'Effective Overall Height of Collector',
                                        'pyname': u'effective_overall_height_of_collector',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'effective gap thickness of plenum behind collector',
                                       {'name': u'Effective Gap Thickness of Plenum Behind Collector',
                                        'pyname': u'effective_gap_thickness_of_plenum_behind_collector',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'effective cross section area of plenum behind collector',
                                       {'name': u'Effective Cross Section Area of Plenum Behind Collector',
                                        'pyname': u'effective_cross_section_area_of_plenum_behind_collector',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'hole layout pattern for pitch',
                                       {'name': u'Hole Layout Pattern for Pitch',
                                        'pyname': u'hole_layout_pattern_for_pitch',
                                        'default': u'Square',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Triangle',
                                                            u'Square'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heat exchange effectiveness correlation',
                                       {'name': u'Heat Exchange Effectiveness Correlation',
                                        'pyname': u'heat_exchange_effectiveness_correlation',
                                        'default': u'Kutscher1994',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Kutscher1994',
                                                            u'VanDeckerHollandsBrunger2001'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ratio of actual collector surface area to projected surface area',
                                       {'name': u'Ratio of Actual Collector Surface Area to Projected Surface Area',
                                        'pyname': u'ratio_of_actual_collector_surface_area_to_projected_surface_area',
                                        'default': 1.0,
                                        'maximum': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'roughness of collector',
                                       {'name': u'Roughness of Collector',
                                        'pyname': u'roughness_of_collector',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'VeryRough',
                                                            u'Rough',
                                                            u'MediumRough',
                                                            u'MediumSmooth',
                                                            u'Smooth',
                                                            u'VerySmooth'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'collector thickness',
                                       {'name': u'Collector Thickness',
                                        'pyname': u'collector_thickness',
                                        'maximum': 0.007,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0005,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'effectiveness for perforations with respect to wind',
                                       {'name': u'Effectiveness for Perforations with Respect to Wind',
                                        'pyname': u'effectiveness_for_perforations_with_respect_to_wind',
                                        'default': 0.25,
                                        'minimum>': 0.0,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'discharge coefficient for openings with respect to buoyancy driven flow',
                                       {'name': u'Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow',
                                        'pyname': u'discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow',
                                        'default': 0.65,
                                        'minimum>': 0.0,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 23,
               'name': u'SolarCollector:UnglazedTranspired',
               'pyname': u'SolarCollectorUnglazedTranspired',
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
    def boundary_conditions_model_name(self):
        """field `Boundary Conditions Model Name`

        |  Enter the name of a SurfaceProperty:OtherSideConditionsModel object

        Args:
            value (str): value for IDD Field `Boundary Conditions Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `boundary_conditions_model_name` or None if not set

        """
        return self["Boundary Conditions Model Name"]

    @boundary_conditions_model_name.setter
    def boundary_conditions_model_name(self, value=None):
        """Corresponds to IDD field `Boundary Conditions Model Name`"""
        self["Boundary Conditions Model Name"] = value

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this collector. Schedule value > 0 means it is available.
        |  If this field is blank, the collector is always available.

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
    def inlet_node_name(self):
        """field `Inlet Node Name`

        |  required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        |  required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value

    @property
    def setpoint_node_name(self):
        """field `Setpoint Node Name`

        |  This node is where the mixed air setpoint is determined.
        |  required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_node_name` or None if not set

        """
        return self["Setpoint Node Name"]

    @setpoint_node_name.setter
    def setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint Node Name`"""
        self["Setpoint Node Name"] = value

    @property
    def zone_node_name(self):
        """field `Zone Node Name`

        |  This node is used to identify the affected zone
        |  required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `Zone Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_node_name` or None if not set

        """
        return self["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """Corresponds to IDD field `Zone Node Name`"""
        self["Zone Node Name"] = value

    @property
    def free_heating_setpoint_schedule_name(self):
        """field `Free Heating Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Free Heating Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `free_heating_setpoint_schedule_name` or None if not set

        """
        return self["Free Heating Setpoint Schedule Name"]

    @free_heating_setpoint_schedule_name.setter
    def free_heating_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Free Heating Setpoint Schedule Name`"""
        self["Free Heating Setpoint Schedule Name"] = value

    @property
    def diameter_of_perforations_in_collector(self):
        """field `Diameter of Perforations in Collector`

        |  Units: m

        Args:
            value (float): value for IDD Field `Diameter of Perforations in Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `diameter_of_perforations_in_collector` or None if not set

        """
        return self["Diameter of Perforations in Collector"]

    @diameter_of_perforations_in_collector.setter
    def diameter_of_perforations_in_collector(self, value=None):
        """Corresponds to IDD field `Diameter of Perforations in Collector`"""
        self["Diameter of Perforations in Collector"] = value

    @property
    def distance_between_perforations_in_collector(self):
        """field `Distance Between Perforations in Collector`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance Between Perforations in Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_between_perforations_in_collector` or None if not set

        """
        return self["Distance Between Perforations in Collector"]

    @distance_between_perforations_in_collector.setter
    def distance_between_perforations_in_collector(self, value=None):
        """Corresponds to IDD field `Distance Between Perforations in
        Collector`"""
        self["Distance Between Perforations in Collector"] = value

    @property
    def thermal_emissivity_of_collector_surface(self):
        """field `Thermal Emissivity of Collector Surface`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Thermal Emissivity of Collector Surface`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `thermal_emissivity_of_collector_surface` or None if not set

        """
        return self["Thermal Emissivity of Collector Surface"]

    @thermal_emissivity_of_collector_surface.setter
    def thermal_emissivity_of_collector_surface(self, value=None):
        """Corresponds to IDD field `Thermal Emissivity of Collector
        Surface`"""
        self["Thermal Emissivity of Collector Surface"] = value

    @property
    def solar_absorbtivity_of_collector_surface(self):
        """field `Solar Absorbtivity of Collector Surface`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Solar Absorbtivity of Collector Surface`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `solar_absorbtivity_of_collector_surface` or None if not set

        """
        return self["Solar Absorbtivity of Collector Surface"]

    @solar_absorbtivity_of_collector_surface.setter
    def solar_absorbtivity_of_collector_surface(self, value=None):
        """Corresponds to IDD field `Solar Absorbtivity of Collector
        Surface`"""
        self["Solar Absorbtivity of Collector Surface"] = value

    @property
    def effective_overall_height_of_collector(self):
        """field `Effective Overall Height of Collector`

        Args:
            value (float): value for IDD Field `Effective Overall Height of Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_overall_height_of_collector` or None if not set

        """
        return self["Effective Overall Height of Collector"]

    @effective_overall_height_of_collector.setter
    def effective_overall_height_of_collector(self, value=None):
        """Corresponds to IDD field `Effective Overall Height of Collector`"""
        self["Effective Overall Height of Collector"] = value

    @property
    def effective_gap_thickness_of_plenum_behind_collector(self):
        """field `Effective Gap Thickness of Plenum Behind Collector`

        |  if corrugated, use average depth
        |  Units: m

        Args:
            value (float): value for IDD Field `Effective Gap Thickness of Plenum Behind Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_gap_thickness_of_plenum_behind_collector` or None if not set

        """
        return self["Effective Gap Thickness of Plenum Behind Collector"]

    @effective_gap_thickness_of_plenum_behind_collector.setter
    def effective_gap_thickness_of_plenum_behind_collector(self, value=None):
        """Corresponds to IDD field `Effective Gap Thickness of Plenum Behind
        Collector`"""
        self["Effective Gap Thickness of Plenum Behind Collector"] = value

    @property
    def effective_cross_section_area_of_plenum_behind_collector(self):
        """field `Effective Cross Section Area of Plenum Behind Collector`

        |  if corrugated, use average depth
        |  Units: m2

        Args:
            value (float): value for IDD Field `Effective Cross Section Area of Plenum Behind Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_cross_section_area_of_plenum_behind_collector` or None if not set

        """
        return self["Effective Cross Section Area of Plenum Behind Collector"]

    @effective_cross_section_area_of_plenum_behind_collector.setter
    def effective_cross_section_area_of_plenum_behind_collector(
            self,
            value=None):
        """Corresponds to IDD field `Effective Cross Section Area of Plenum
        Behind Collector`"""
        self["Effective Cross Section Area of Plenum Behind Collector"] = value

    @property
    def hole_layout_pattern_for_pitch(self):
        """field `Hole Layout Pattern for Pitch`

        |  Default value: Square

        Args:
            value (str): value for IDD Field `Hole Layout Pattern for Pitch`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hole_layout_pattern_for_pitch` or None if not set

        """
        return self["Hole Layout Pattern for Pitch"]

    @hole_layout_pattern_for_pitch.setter
    def hole_layout_pattern_for_pitch(self, value="Square"):
        """Corresponds to IDD field `Hole Layout Pattern for Pitch`"""
        self["Hole Layout Pattern for Pitch"] = value

    @property
    def heat_exchange_effectiveness_correlation(self):
        """field `Heat Exchange Effectiveness Correlation`

        |  Default value: Kutscher1994

        Args:
            value (str): value for IDD Field `Heat Exchange Effectiveness Correlation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_exchange_effectiveness_correlation` or None if not set

        """
        return self["Heat Exchange Effectiveness Correlation"]

    @heat_exchange_effectiveness_correlation.setter
    def heat_exchange_effectiveness_correlation(self, value="Kutscher1994"):
        """Corresponds to IDD field `Heat Exchange Effectiveness
        Correlation`"""
        self["Heat Exchange Effectiveness Correlation"] = value

    @property
    def ratio_of_actual_collector_surface_area_to_projected_surface_area(self):
        """field `Ratio of Actual Collector Surface Area to Projected Surface
        Area`

        |  This parameter is used to help account for corrugations in the collector
        |  Units: dimensionless
        |  Default value: 1.0
        |  value >= 1.0
        |  value <= 2.0

        Args:
            value (float): value for IDD Field `Ratio of Actual Collector Surface Area to Projected Surface Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ratio_of_actual_collector_surface_area_to_projected_surface_area` or None if not set

        """
        return self[
            "Ratio of Actual Collector Surface Area to Projected Surface Area"]

    @ratio_of_actual_collector_surface_area_to_projected_surface_area.setter
    def ratio_of_actual_collector_surface_area_to_projected_surface_area(
            self,
            value=1.0):
        """Corresponds to IDD field `Ratio of Actual Collector Surface Area to
        Projected Surface Area`"""
        self[
            "Ratio of Actual Collector Surface Area to Projected Surface Area"] = value

    @property
    def roughness_of_collector(self):
        """field `Roughness of Collector`

        Args:
            value (str): value for IDD Field `Roughness of Collector`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `roughness_of_collector` or None if not set

        """
        return self["Roughness of Collector"]

    @roughness_of_collector.setter
    def roughness_of_collector(self, value=None):
        """Corresponds to IDD field `Roughness of Collector`"""
        self["Roughness of Collector"] = value

    @property
    def collector_thickness(self):
        """field `Collector Thickness`

        |  Collector thickness is not required for Kutscher correlation
        |  Collector thickness is required for Van Decker et al. correlation
        |  Units: m
        |  value >= 0.0005
        |  value <= 0.007

        Args:
            value (float): value for IDD Field `Collector Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `collector_thickness` or None if not set

        """
        return self["Collector Thickness"]

    @collector_thickness.setter
    def collector_thickness(self, value=None):
        """Corresponds to IDD field `Collector Thickness`"""
        self["Collector Thickness"] = value

    @property
    def effectiveness_for_perforations_with_respect_to_wind(self):
        """field `Effectiveness for Perforations with Respect to Wind`

        |  Cv
        |  Units: dimensionless
        |  Default value: 0.25
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Effectiveness for Perforations with Respect to Wind`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effectiveness_for_perforations_with_respect_to_wind` or None if not set

        """
        return self["Effectiveness for Perforations with Respect to Wind"]

    @effectiveness_for_perforations_with_respect_to_wind.setter
    def effectiveness_for_perforations_with_respect_to_wind(self, value=0.25):
        """Corresponds to IDD field `Effectiveness for Perforations with
        Respect to Wind`"""
        self["Effectiveness for Perforations with Respect to Wind"] = value

    @property
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(
            self):
        """field `Discharge Coefficient for Openings with Respect to Buoyancy
        Driven Flow`

        |  Cd
        |  Units: dimensionless
        |  Default value: 0.65
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow` or None if not set

        """
        return self[
            "Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"]

    @discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow.setter
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(
            self,
            value=0.65):
        """Corresponds to IDD field `Discharge Coefficient for Openings with
        Respect to Buoyancy Driven Flow`"""
        self[
            "Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
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




class SolarCollectorUnglazedTranspiredMultisystem(DataObject):

    """ Corresponds to IDD object `SolarCollector:UnglazedTranspired:Multisystem`
        quad-tuples of inlet, outlet, control, and zone nodes
        for multiple different outdoor air systems attached to same collector
    """
    _schema = {'extensible-fields': OrderedDict([(u'outdoor air system 1 collector inlet node',
                                                  {'name': u'Outdoor Air System 1 Collector Inlet Node',
                                                   'pyname': u'outdoor_air_system_1_collector_inlet_node',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'}),
                                                 (u'outdoor air system 1 collector outlet node',
                                                  {'name': u'Outdoor Air System 1 Collector Outlet Node',
                                                   'pyname': u'outdoor_air_system_1_collector_outlet_node',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'}),
                                                 (u'outdoor air system 1 mixed air node',
                                                  {'name': u'Outdoor Air System 1 Mixed Air Node',
                                                   'pyname': u'outdoor_air_system_1_mixed_air_node',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'}),
                                                 (u'outdoor air system 1 zone node',
                                                  {'name': u'Outdoor Air System 1 Zone Node',
                                                   'pyname': u'outdoor_air_system_1_zone_node',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'})]),
               'fields': OrderedDict([(u'solar collector name',
                                       {'name': u'Solar Collector Name',
                                        'pyname': u'solar_collector_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Solar Collectors',
               'min-fields': 0,
               'name': u'SolarCollector:UnglazedTranspired:Multisystem',
               'pyname': u'SolarCollectorUnglazedTranspiredMultisystem',
               'required-object': False,
               'unique-object': False}

    @property
    def solar_collector_name(self):
        """field `Solar Collector Name`

        |  Enter the name of a SolarCollector:UnglazedTranspired object.

        Args:
            value (str): value for IDD Field `Solar Collector Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_collector_name` or None if not set

        """
        return self["Solar Collector Name"]

    @solar_collector_name.setter
    def solar_collector_name(self, value=None):
        """Corresponds to IDD field `Solar Collector Name`"""
        self["Solar Collector Name"] = value

    def add_extensible(self,
                       outdoor_air_system_1_collector_inlet_node=None,
                       outdoor_air_system_1_collector_outlet_node=None,
                       outdoor_air_system_1_mixed_air_node=None,
                       outdoor_air_system_1_zone_node=None,
                       ):
        """Add values for extensible fields.

        Args:

            outdoor_air_system_1_collector_inlet_node (str): value for IDD Field `Outdoor Air System 1 Collector Inlet Node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            outdoor_air_system_1_collector_outlet_node (str): value for IDD Field `Outdoor Air System 1 Collector Outlet Node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            outdoor_air_system_1_mixed_air_node (str): value for IDD Field `Outdoor Air System 1 Mixed Air Node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            outdoor_air_system_1_zone_node (str): value for IDD Field `Outdoor Air System 1 Zone Node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        outdoor_air_system_1_collector_inlet_node = self.check_value(
            "Outdoor Air System 1 Collector Inlet Node",
            outdoor_air_system_1_collector_inlet_node)
        vals.append(outdoor_air_system_1_collector_inlet_node)
        outdoor_air_system_1_collector_outlet_node = self.check_value(
            "Outdoor Air System 1 Collector Outlet Node",
            outdoor_air_system_1_collector_outlet_node)
        vals.append(outdoor_air_system_1_collector_outlet_node)
        outdoor_air_system_1_mixed_air_node = self.check_value(
            "Outdoor Air System 1 Mixed Air Node",
            outdoor_air_system_1_mixed_air_node)
        vals.append(outdoor_air_system_1_mixed_air_node)
        outdoor_air_system_1_zone_node = self.check_value(
            "Outdoor Air System 1 Zone Node",
            outdoor_air_system_1_zone_node)
        vals.append(outdoor_air_system_1_zone_node)
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


