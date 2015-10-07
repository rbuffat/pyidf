""" Data objects in group "Zone HVAC Radiative"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ZoneHvacBaseboardRadiantConvectiveWater(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:Baseboard:RadiantConvective:Water`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'fraction of radiant energy to surface 1',
                                                  {'name': u'Fraction of Radiant Energy to Surface 1',
                                                   'pyname': u'fraction_of_radiant_energy_to_surface_1',
                                                   'maximum': 1.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
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
                                      (u'rated average water temperature',
                                       {'name': u'Rated Average Water Temperature',
                                        'pyname': u'rated_average_water_temperature',
                                        'default': 87.78,
                                        'maximum': 150.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 20.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'rated water mass flow rate',
                                       {'name': u'Rated Water Mass Flow Rate',
                                        'pyname': u'rated_water_mass_flow_rate',
                                        'default': 0.063,
                                        'minimum>': 0.0,
                                        'maximum': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Kg/s'}),
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum water flow rate',
                                       {'name': u'Maximum Water Flow Rate',
                                        'pyname': u'maximum_water_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction of radiant energy incident on people',
                                       {'name': u'Fraction of Radiant Energy Incident on People',
                                        'pyname': u'fraction_of_radiant_energy_incident_on_people',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 12,
               'name': u'ZoneHVAC:Baseboard:RadiantConvective:Water',
               'pyname': u'ZoneHvacBaseboardRadiantConvectiveWater',
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
    def rated_average_water_temperature(self):
        """field `Rated Average Water Temperature`

        |  Rated average water temperature is the average of the inlet and outlet water temperatures
        |  at rated conditions.
        |  Units: C
        |  Default value: 87.78
        |  value >= 20.0
        |  value <= 150.0

        Args:
            value (float): value for IDD Field `Rated Average Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_average_water_temperature` or None if not set

        """
        return self["Rated Average Water Temperature"]

    @rated_average_water_temperature.setter
    def rated_average_water_temperature(self, value=87.78):
        """Corresponds to IDD field `Rated Average Water Temperature`"""
        self["Rated Average Water Temperature"] = value

    @property
    def rated_water_mass_flow_rate(self):
        """field `Rated Water Mass Flow Rate`

        |  Standard is I=B=R Rating document where all baseboards are rated at either 0.063 kg/s (1 gpm)
        |  or 0.252 kg/s (4 gpm).  It is recommended that users find data for the baseboard heater that
        |  corresponds to performance at 0.063 kg/s unless the flow rate is expected to be above 0.252 kg/s.
        |  If the flow rate is expected to be above 0.252 kg/s, this field should be 0.252 kg/s.
        |  Units: Kg/s
        |  Default value: 0.063
        |  value <= 10.0

        Args:
            value (float): value for IDD Field `Rated Water Mass Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_water_mass_flow_rate` or None if not set

        """
        return self["Rated Water Mass Flow Rate"]

    @rated_water_mass_flow_rate.setter
    def rated_water_mass_flow_rate(self, value=0.063):
        """Corresponds to IDD field `Rated Water Mass Flow Rate`"""
        self["Rated Water Mass Flow Rate"] = value

    @property
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity. Required field when the heating design capacity method
        |  HeatingDesignCapacity. This input field is rated heating capacity. Users must multiply the
        |  actual finned length published in the literature to determine the rated capacity. Rated
        |  Capacity is for an inlet air dry-bulb temperature of 18.0C, the Rated Water Mass Flow Rate
        |  of 0.063kg/s or 0.252kg/s, and the Rated Average Water Temperature between 32.2C and 115.6C.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def maximum_water_flow_rate(self):
        """field `Maximum Water Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_water_flow_rate` or None if not set

        """
        return self["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Water Flow Rate`"""
        self["Maximum Water Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """field `Fraction of Radiant Energy Incident on People`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set

        """
        return self["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """Corresponds to IDD field `Fraction of Radiant Energy Incident on
        People`"""
        self["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
        fraction_of_radiant_energy_to_surface_1 = self.check_value(
            "Fraction of Radiant Energy to Surface 1",
            fraction_of_radiant_energy_to_surface_1)
        vals.append(fraction_of_radiant_energy_to_surface_1)
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




class ZoneHvacBaseboardRadiantConvectiveSteam(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:Baseboard:RadiantConvective:Steam`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'fraction of radiant energy to surface 1',
                                                  {'name': u'Fraction of Radiant Energy to Surface 1',
                                                   'pyname': u'fraction_of_radiant_energy_to_surface_1',
                                                   'maximum': 1.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
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
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'degree of subcooling',
                                       {'name': u'Degree of SubCooling',
                                        'pyname': u'degree_of_subcooling',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum steam flow rate',
                                       {'name': u'Maximum Steam Flow Rate',
                                        'pyname': u'maximum_steam_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction of radiant energy incident on people',
                                       {'name': u'Fraction of Radiant Energy Incident on People',
                                        'pyname': u'fraction_of_radiant_energy_incident_on_people',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 11,
               'name': u'ZoneHVAC:Baseboard:RadiantConvective:Steam',
               'pyname': u'ZoneHvacBaseboardRadiantConvectiveSteam',
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
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def degree_of_subcooling(self):
        """field `Degree of SubCooling`

        |  Units: deltaC
        |  Default value: 5.0
        |  value >= 1.0

        Args:
            value (float): value for IDD Field `Degree of SubCooling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `degree_of_subcooling` or None if not set

        """
        return self["Degree of SubCooling"]

    @degree_of_subcooling.setter
    def degree_of_subcooling(self, value=5.0):
        """Corresponds to IDD field `Degree of SubCooling`"""
        self["Degree of SubCooling"] = value

    @property
    def maximum_steam_flow_rate(self):
        """field `Maximum Steam Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_steam_flow_rate` or None if not set

        """
        return self["Maximum Steam Flow Rate"]

    @maximum_steam_flow_rate.setter
    def maximum_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Steam Flow Rate`"""
        self["Maximum Steam Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """field `Fraction of Radiant Energy Incident on People`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set

        """
        return self["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """Corresponds to IDD field `Fraction of Radiant Energy Incident on
        People`"""
        self["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
        fraction_of_radiant_energy_to_surface_1 = self.check_value(
            "Fraction of Radiant Energy to Surface 1",
            fraction_of_radiant_energy_to_surface_1)
        vals.append(fraction_of_radiant_energy_to_surface_1)
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




class ZoneHvacBaseboardRadiantConvectiveElectric(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:Baseboard:RadiantConvective:Electric`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'fraction of radiant energy to surface 1',
                                                  {'name': u'Fraction of Radiant Energy to Surface 1',
                                                   'pyname': u'fraction_of_radiant_energy_to_surface_1',
                                                   'maximum': 1.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
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
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'efficiency',
                                       {'name': u'Efficiency',
                                        'pyname': u'efficiency',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction of radiant energy incident on people',
                                       {'name': u'Fraction of Radiant Energy Incident on People',
                                        'pyname': u'fraction_of_radiant_energy_incident_on_people',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 8,
               'name': u'ZoneHVAC:Baseboard:RadiantConvective:Electric',
               'pyname': u'ZoneHvacBaseboardRadiantConvectiveElectric',
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
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def efficiency(self):
        """field `Efficiency`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `efficiency` or None if not set

        """
        return self["Efficiency"]

    @efficiency.setter
    def efficiency(self, value=1.0):
        """Corresponds to IDD field `Efficiency`"""
        self["Efficiency"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """field `Fraction of Radiant Energy Incident on People`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set

        """
        return self["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """Corresponds to IDD field `Fraction of Radiant Energy Incident on
        People`"""
        self["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
        fraction_of_radiant_energy_to_surface_1 = self.check_value(
            "Fraction of Radiant Energy to Surface 1",
            fraction_of_radiant_energy_to_surface_1)
        vals.append(fraction_of_radiant_energy_to_surface_1)
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




class ZoneHvacBaseboardConvectiveWater(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:Baseboard:Convective:Water`
        Hot water baseboard heater, convection-only. Natural convection hydronic heating unit.
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
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'u-factor times area value',
                                       {'name': u'U-Factor Times Area Value',
                                        'pyname': u'ufactor_times_area_value',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/K'}),
                                      (u'maximum water flow rate',
                                       {'name': u'Maximum Water Flow Rate',
                                        'pyname': u'maximum_water_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:Baseboard:Convective:Water',
               'pyname': u'ZoneHvacBaseboardConvectiveWater',
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
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def ufactor_times_area_value(self):
        """field `U-Factor Times Area Value`

        |  Units: W/K

        Args:
            value (float or "Autosize"): value for IDD Field `U-Factor Times Area Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `ufactor_times_area_value` or None if not set
        """
        return self["U-Factor Times Area Value"]

    @ufactor_times_area_value.setter
    def ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD field `U-Factor Times Area Value`

        """
        self["U-Factor Times Area Value"] = value

    @property
    def maximum_water_flow_rate(self):
        """field `Maximum Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_water_flow_rate` or None if not set

        """
        return self["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Water Flow Rate`"""
        self["Maximum Water Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value




class ZoneHvacBaseboardConvectiveElectric(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:Baseboard:Convective:Electric`
        Electric baseboard heater, convection-only. Natural convection electric heating unit.
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
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'efficiency',
                                       {'name': u'Efficiency',
                                        'pyname': u'efficiency',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:Baseboard:Convective:Electric',
               'pyname': u'ZoneHvacBaseboardConvectiveElectric',
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
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def efficiency(self):
        """field `Efficiency`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `efficiency` or None if not set

        """
        return self["Efficiency"]

    @efficiency.setter
    def efficiency(self, value=1.0):
        """Corresponds to IDD field `Efficiency`"""
        self["Efficiency"] = value




class ZoneHvacLowTemperatureRadiantVariableFlow(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:VariableFlow`
        Low temperature hydronic radiant heating and/or cooling system embedded in a building
        surface (wall, ceiling, or floor). Controlled by varying the hot or chilled water
        flow to the unit.
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
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'surface name or radiant surface group name',
                                       {'name': u'Surface Name or Radiant Surface Group Name',
                                        'pyname': u'surface_name_or_radiant_surface_group_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hydronic tubing inside diameter',
                                       {'name': u'Hydronic Tubing Inside Diameter',
                                        'pyname': u'hydronic_tubing_inside_diameter',
                                        'default': 0.013,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'hydronic tubing length',
                                       {'name': u'Hydronic Tubing Length',
                                        'pyname': u'hydronic_tubing_length',
                                        'default': 'autosize',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'temperature control type',
                                       {'name': u'Temperature Control Type',
                                        'pyname': u'temperature_control_type',
                                        'default': u'MeanAirTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MeanAirTemperature',
                                                            u'MeanRadiantTemperature',
                                                            u'OperativeTemperature',
                                                            u'OutdoorDryBulbTemperature',
                                                            u'OutdoorWetBulbTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum hot water flow',
                                       {'name': u'Maximum Hot Water Flow',
                                        'pyname': u'maximum_hot_water_flow',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'heating water inlet node name',
                                       {'name': u'Heating Water Inlet Node Name',
                                        'pyname': u'heating_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heating water outlet node name',
                                       {'name': u'Heating Water Outlet Node Name',
                                        'pyname': u'heating_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heating control throttling range',
                                       {'name': u'Heating Control Throttling Range',
                                        'pyname': u'heating_control_throttling_range',
                                        'default': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.5,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'heating control temperature schedule name',
                                       {'name': u'Heating Control Temperature Schedule Name',
                                        'pyname': u'heating_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling design capacity method',
                                       {'name': u'Cooling Design Capacity Method',
                                        'pyname': u'cooling_design_capacity_method',
                                        'default': u'CoolingDesignCapacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'CoolingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling design capacity',
                                       {'name': u'Cooling Design Capacity',
                                        'pyname': u'cooling_design_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'cooling design capacity per floor area',
                                       {'name': u'Cooling Design Capacity Per Floor Area',
                                        'pyname': u'cooling_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized cooling design capacity',
                                       {'name': u'Fraction of Autosized Cooling Design Capacity',
                                        'pyname': u'fraction_of_autosized_cooling_design_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum cold water flow',
                                       {'name': u'Maximum Cold Water Flow',
                                        'pyname': u'maximum_cold_water_flow',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling water inlet node name',
                                       {'name': u'Cooling Water Inlet Node Name',
                                        'pyname': u'cooling_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cooling water outlet node name',
                                       {'name': u'Cooling Water Outlet Node Name',
                                        'pyname': u'cooling_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cooling control throttling range',
                                       {'name': u'Cooling Control Throttling Range',
                                        'pyname': u'cooling_control_throttling_range',
                                        'default': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.5,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'cooling control temperature schedule name',
                                       {'name': u'Cooling Control Temperature Schedule Name',
                                        'pyname': u'cooling_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condensation control type',
                                       {'name': u'Condensation Control Type',
                                        'pyname': u'condensation_control_type',
                                        'default': u'SimpleOff',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Off',
                                                            u'SimpleOff',
                                                            u'VariableOff'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'condensation control dewpoint offset',
                                       {'name': u'Condensation Control Dewpoint Offset',
                                        'pyname': u'condensation_control_dewpoint_offset',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'number of circuits',
                                       {'name': u'Number of Circuits',
                                        'pyname': u'number_of_circuits',
                                        'default': u'OnePerSurface',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'OnePerSurface',
                                                            u'CalculateFromCircuitLength'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'circuit length',
                                       {'name': u'Circuit Length',
                                        'pyname': u'circuit_length',
                                        'default': 106.7,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 29,
               'name': u'ZoneHVAC:LowTemperatureRadiant:VariableFlow',
               'pyname': u'ZoneHvacLowTemperatureRadiantVariableFlow',
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

        |  Name of zone system is serving

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
    def surface_name_or_radiant_surface_group_name(self):
        """field `Surface Name or Radiant Surface Group Name`

        |  Identifies surfaces that radiant system is embedded in.
        |  For a system with multiple surfaces, enter the name of
        |  a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set

        """
        return self["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """Corresponds to IDD field `Surface Name or Radiant Surface Group
        Name`"""
        self["Surface Name or Radiant Surface Group Name"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """field `Hydronic Tubing Inside Diameter`

        |  Units: m
        |  IP-Units: in
        |  Default value: 0.013

        Args:
            value (float): value for IDD Field `Hydronic Tubing Inside Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set

        """
        return self["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=0.013):
        """Corresponds to IDD field `Hydronic Tubing Inside Diameter`"""
        self["Hydronic Tubing Inside Diameter"] = value

    @property
    def hydronic_tubing_length(self):
        """field `Hydronic Tubing Length`

        |  (total length of pipe embedded in surface)
        |  Units: m
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Hydronic Tubing Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `hydronic_tubing_length` or None if not set

        """
        return self["Hydronic Tubing Length"]

    @hydronic_tubing_length.setter
    def hydronic_tubing_length(self, value="autosize"):
        """Corresponds to IDD field `Hydronic Tubing Length`"""
        self["Hydronic Tubing Length"] = value

    @property
    def temperature_control_type(self):
        """field `Temperature Control Type`

        |  (Temperature on which unit is controlled)
        |  Default value: MeanAirTemperature

        Args:
            value (str): value for IDD Field `Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_control_type` or None if not set

        """
        return self["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="MeanAirTemperature"):
        """Corresponds to IDD field `Temperature Control Type`"""
        self["Temperature Control Type"] = value

    @property
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def maximum_hot_water_flow(self):
        """field `Maximum Hot Water Flow`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_flow` or None if not set

        """
        return self["Maximum Hot Water Flow"]

    @maximum_hot_water_flow.setter
    def maximum_hot_water_flow(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water Flow`"""
        self["Maximum Hot Water Flow"] = value

    @property
    def heating_water_inlet_node_name(self):
        """field `Heating Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_water_inlet_node_name` or None if not set

        """
        return self["Heating Water Inlet Node Name"]

    @heating_water_inlet_node_name.setter
    def heating_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Heating Water Inlet Node Name`"""
        self["Heating Water Inlet Node Name"] = value

    @property
    def heating_water_outlet_node_name(self):
        """field `Heating Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_water_outlet_node_name` or None if not set

        """
        return self["Heating Water Outlet Node Name"]

    @heating_water_outlet_node_name.setter
    def heating_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Heating Water Outlet Node Name`"""
        self["Heating Water Outlet Node Name"] = value

    @property
    def heating_control_throttling_range(self):
        """field `Heating Control Throttling Range`

        |  Units: deltaC
        |  Default value: 0.5
        |  value >= 0.5

        Args:
            value (float): value for IDD Field `Heating Control Throttling Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_control_throttling_range` or None if not set

        """
        return self["Heating Control Throttling Range"]

    @heating_control_throttling_range.setter
    def heating_control_throttling_range(self, value=0.5):
        """Corresponds to IDD field `Heating Control Throttling Range`"""
        self["Heating Control Throttling Range"] = value

    @property
    def heating_control_temperature_schedule_name(self):
        """field `Heating Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_control_temperature_schedule_name` or None if not set

        """
        return self["Heating Control Temperature Schedule Name"]

    @heating_control_temperature_schedule_name.setter
    def heating_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Control Temperature Schedule
        Name`"""
        self["Heating Control Temperature Schedule Name"] = value

    @property
    def cooling_design_capacity_method(self):
        """field `Cooling Design Capacity Method`

        |  Enter the method used to determine the cooling design capacity for scalable sizing.
        |  CoolingDesignCapacity => selected when the design cooling capacity value is specified or
        |  auto-sized. CapacityPerFloorArea => selected when the design cooling capacity is determined
        |  from user specified cooling capacity per floor area and total floor area of cooled zone
        |  served by the hydrolic unit. FractionOfAutosizedCoolingCapacity => is selected when the
        |  design cooling capacity is determined from a user specified fraction and the auto-sized
        |  design cooling capacity of the system.
        |  Default value: CoolingDesignCapacity

        Args:
            value (str): value for IDD Field `Cooling Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set

        """
        return self["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="CoolingDesignCapacity"):
        """Corresponds to IDD field `Cooling Design Capacity Method`"""
        self["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """field `Cooling Design Capacity`

        |  Enter the design cooling capacity. Required field when the cooling design capacity method
        |  CoolingDesignCapacity.
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_design_capacity` or None if not set

        """
        return self["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """Corresponds to IDD field `Cooling Design Capacity`"""
        self["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """field `Cooling Design Capacity Per Floor Area`

        |  Enter the cooling design capacity per total floor area of cooled zones served by the unit.
        |  Required field when the cooling design capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set

        """
        return self["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Cooling Design Capacity Per Floor Area`"""
        self["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """field `Fraction of Autosized Cooling Design Capacity`

        |  Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        |  design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """Corresponds to IDD field `Fraction of Autosized Cooling Design
        Capacity`"""
        self["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def maximum_cold_water_flow(self):
        """field `Maximum Cold Water Flow`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cold Water Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_cold_water_flow` or None if not set

        """
        return self["Maximum Cold Water Flow"]

    @maximum_cold_water_flow.setter
    def maximum_cold_water_flow(self, value=None):
        """Corresponds to IDD field `Maximum Cold Water Flow`"""
        self["Maximum Cold Water Flow"] = value

    @property
    def cooling_water_inlet_node_name(self):
        """field `Cooling Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_water_inlet_node_name` or None if not set

        """
        return self["Cooling Water Inlet Node Name"]

    @cooling_water_inlet_node_name.setter
    def cooling_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Cooling Water Inlet Node Name`"""
        self["Cooling Water Inlet Node Name"] = value

    @property
    def cooling_water_outlet_node_name(self):
        """field `Cooling Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_water_outlet_node_name` or None if not set

        """
        return self["Cooling Water Outlet Node Name"]

    @cooling_water_outlet_node_name.setter
    def cooling_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Cooling Water Outlet Node Name`"""
        self["Cooling Water Outlet Node Name"] = value

    @property
    def cooling_control_throttling_range(self):
        """field `Cooling Control Throttling Range`

        |  Units: deltaC
        |  Default value: 0.5
        |  value >= 0.5

        Args:
            value (float): value for IDD Field `Cooling Control Throttling Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_control_throttling_range` or None if not set

        """
        return self["Cooling Control Throttling Range"]

    @cooling_control_throttling_range.setter
    def cooling_control_throttling_range(self, value=0.5):
        """Corresponds to IDD field `Cooling Control Throttling Range`"""
        self["Cooling Control Throttling Range"] = value

    @property
    def cooling_control_temperature_schedule_name(self):
        """field `Cooling Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_control_temperature_schedule_name` or None if not set

        """
        return self["Cooling Control Temperature Schedule Name"]

    @cooling_control_temperature_schedule_name.setter
    def cooling_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Control Temperature Schedule
        Name`"""
        self["Cooling Control Temperature Schedule Name"] = value

    @property
    def condensation_control_type(self):
        """field `Condensation Control Type`

        |  Default value: SimpleOff

        Args:
            value (str): value for IDD Field `Condensation Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condensation_control_type` or None if not set

        """
        return self["Condensation Control Type"]

    @condensation_control_type.setter
    def condensation_control_type(self, value="SimpleOff"):
        """Corresponds to IDD field `Condensation Control Type`"""
        self["Condensation Control Type"] = value

    @property
    def condensation_control_dewpoint_offset(self):
        """field `Condensation Control Dewpoint Offset`

        |  Units: C
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Condensation Control Dewpoint Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensation_control_dewpoint_offset` or None if not set

        """
        return self["Condensation Control Dewpoint Offset"]

    @condensation_control_dewpoint_offset.setter
    def condensation_control_dewpoint_offset(self, value=1.0):
        """Corresponds to IDD field `Condensation Control Dewpoint Offset`"""
        self["Condensation Control Dewpoint Offset"] = value

    @property
    def number_of_circuits(self):
        """field `Number of Circuits`

        |  Default value: OnePerSurface

        Args:
            value (str): value for IDD Field `Number of Circuits`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `number_of_circuits` or None if not set

        """
        return self["Number of Circuits"]

    @number_of_circuits.setter
    def number_of_circuits(self, value="OnePerSurface"):
        """Corresponds to IDD field `Number of Circuits`"""
        self["Number of Circuits"] = value

    @property
    def circuit_length(self):
        """field `Circuit Length`

        |  Units: m
        |  Default value: 106.7

        Args:
            value (float): value for IDD Field `Circuit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `circuit_length` or None if not set

        """
        return self["Circuit Length"]

    @circuit_length.setter
    def circuit_length(self, value=106.7):
        """Corresponds to IDD field `Circuit Length`"""
        self["Circuit Length"] = value




class ZoneHvacLowTemperatureRadiantConstantFlow(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:ConstantFlow`
        Low temperature hydronic radiant heating and/or cooling system embedded in a building
        surface (wall, ceiling, or floor). Controlled by varying the hot or chilled water
        temperature circulating through the unit.
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
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'surface name or radiant surface group name',
                                       {'name': u'Surface Name or Radiant Surface Group Name',
                                        'pyname': u'surface_name_or_radiant_surface_group_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hydronic tubing inside diameter',
                                       {'name': u'Hydronic Tubing Inside Diameter',
                                        'pyname': u'hydronic_tubing_inside_diameter',
                                        'default': 0.013,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'hydronic tubing length',
                                       {'name': u'Hydronic Tubing Length',
                                        'pyname': u'hydronic_tubing_length',
                                        'default': 'autosize',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'temperature control type',
                                       {'name': u'Temperature Control Type',
                                        'pyname': u'temperature_control_type',
                                        'default': u'MeanAirTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MeanAirTemperature',
                                                            u'MeanRadiantTemperature',
                                                            u'OperativeTemperature',
                                                            u'OutdoorDryBulbTemperature',
                                                            u'OutdoorWetBulbTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'rated flow rate',
                                       {'name': u'Rated Flow Rate',
                                        'pyname': u'rated_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'pump flow rate schedule name',
                                       {'name': u'Pump Flow Rate Schedule Name',
                                        'pyname': u'pump_flow_rate_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated pump head',
                                       {'name': u'Rated Pump Head',
                                        'pyname': u'rated_pump_head',
                                        'default': 179352.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'Pa'}),
                                      (u'rated power consumption',
                                       {'name': u'Rated Power Consumption',
                                        'pyname': u'rated_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'motor efficiency',
                                       {'name': u'Motor Efficiency',
                                        'pyname': u'motor_efficiency',
                                        'default': 0.9,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction of motor inefficiencies to fluid stream',
                                       {'name': u'Fraction of Motor Inefficiencies to Fluid Stream',
                                        'pyname': u'fraction_of_motor_inefficiencies_to_fluid_stream',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'heating water inlet node name',
                                       {'name': u'Heating Water Inlet Node Name',
                                        'pyname': u'heating_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heating water outlet node name',
                                       {'name': u'Heating Water Outlet Node Name',
                                        'pyname': u'heating_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heating high water temperature schedule name',
                                       {'name': u'Heating High Water Temperature Schedule Name',
                                        'pyname': u'heating_high_water_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating low water temperature schedule name',
                                       {'name': u'Heating Low Water Temperature Schedule Name',
                                        'pyname': u'heating_low_water_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating high control temperature schedule name',
                                       {'name': u'Heating High Control Temperature Schedule Name',
                                        'pyname': u'heating_high_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating low control temperature schedule name',
                                       {'name': u'Heating Low Control Temperature Schedule Name',
                                        'pyname': u'heating_low_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling water inlet node name',
                                       {'name': u'Cooling Water Inlet Node Name',
                                        'pyname': u'cooling_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cooling water outlet node name',
                                       {'name': u'Cooling Water Outlet Node Name',
                                        'pyname': u'cooling_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cooling high water temperature schedule name',
                                       {'name': u'Cooling High Water Temperature Schedule Name',
                                        'pyname': u'cooling_high_water_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling low water temperature schedule name',
                                       {'name': u'Cooling Low Water Temperature Schedule Name',
                                        'pyname': u'cooling_low_water_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling high control temperature schedule name',
                                       {'name': u'Cooling High Control Temperature Schedule Name',
                                        'pyname': u'cooling_high_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling low control temperature schedule name',
                                       {'name': u'Cooling Low Control Temperature Schedule Name',
                                        'pyname': u'cooling_low_control_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condensation control type',
                                       {'name': u'Condensation Control Type',
                                        'pyname': u'condensation_control_type',
                                        'default': u'SimpleOff',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Off',
                                                            u'SimpleOff',
                                                            u'VariableOff'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'condensation control dewpoint offset',
                                       {'name': u'Condensation Control Dewpoint Offset',
                                        'pyname': u'condensation_control_dewpoint_offset',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'number of circuits',
                                       {'name': u'Number of Circuits',
                                        'pyname': u'number_of_circuits',
                                        'default': u'OnePerSurface',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'OnePerSurface',
                                                            u'CalculateFromCircuitLength'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'circuit length',
                                       {'name': u'Circuit Length',
                                        'pyname': u'circuit_length',
                                        'default': 106.7,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 29,
               'name': u'ZoneHVAC:LowTemperatureRadiant:ConstantFlow',
               'pyname': u'ZoneHvacLowTemperatureRadiantConstantFlow',
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

        |  Name of zone system is serving

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
    def surface_name_or_radiant_surface_group_name(self):
        """field `Surface Name or Radiant Surface Group Name`

        |  Identifies surfaces that radiant system is embedded in.
        |  For a system with multiple surfaces, enter the name of
        |  a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set

        """
        return self["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """Corresponds to IDD field `Surface Name or Radiant Surface Group
        Name`"""
        self["Surface Name or Radiant Surface Group Name"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """field `Hydronic Tubing Inside Diameter`

        |  Units: m
        |  Default value: 0.013

        Args:
            value (float): value for IDD Field `Hydronic Tubing Inside Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set

        """
        return self["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=0.013):
        """Corresponds to IDD field `Hydronic Tubing Inside Diameter`"""
        self["Hydronic Tubing Inside Diameter"] = value

    @property
    def hydronic_tubing_length(self):
        """field `Hydronic Tubing Length`

        |  Total length of pipe embedded in surface
        |  Units: m
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Hydronic Tubing Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `hydronic_tubing_length` or None if not set

        """
        return self["Hydronic Tubing Length"]

    @hydronic_tubing_length.setter
    def hydronic_tubing_length(self, value="autosize"):
        """Corresponds to IDD field `Hydronic Tubing Length`"""
        self["Hydronic Tubing Length"] = value

    @property
    def temperature_control_type(self):
        """field `Temperature Control Type`

        |  Temperature used to control system
        |  Default value: MeanAirTemperature

        Args:
            value (str): value for IDD Field `Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_control_type` or None if not set

        """
        return self["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="MeanAirTemperature"):
        """Corresponds to IDD field `Temperature Control Type`"""
        self["Temperature Control Type"] = value

    @property
    def rated_flow_rate(self):
        """field `Rated Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Rated Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `rated_flow_rate` or None if not set

        """
        return self["Rated Flow Rate"]

    @rated_flow_rate.setter
    def rated_flow_rate(self, value=None):
        """Corresponds to IDD field `Rated Flow Rate`"""
        self["Rated Flow Rate"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """field `Pump Flow Rate Schedule Name`

        |  Modifies the Rated Flow Rate of the pump on a time basis
        |  the default is that the pump is ON and runs according to its other
        |  operational requirements specified above.  The schedule is for special
        |  pump operations. Values here are between 0 and 1 and are multipliers
        |  on the previous field (Rated Flow Rate).

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set

        """
        return self["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """Corresponds to IDD field `Pump Flow Rate Schedule Name`"""
        self["Pump Flow Rate Schedule Name"] = value

    @property
    def rated_pump_head(self):
        """field `Rated Pump Head`

        |  default head is 60 feet
        |  Units: Pa
        |  Default value: 179352.0

        Args:
            value (float): value for IDD Field `Rated Pump Head`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_pump_head` or None if not set

        """
        return self["Rated Pump Head"]

    @rated_pump_head.setter
    def rated_pump_head(self, value=179352.0):
        """Corresponds to IDD field `Rated Pump Head`"""
        self["Rated Pump Head"] = value

    @property
    def rated_power_consumption(self):
        """field `Rated Power Consumption`

        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Power Consumption`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_power_consumption` or None if not set

        """
        return self["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """Corresponds to IDD field `Rated Power Consumption`"""
        self["Rated Power Consumption"] = value

    @property
    def motor_efficiency(self):
        """field `Motor Efficiency`

        |  Default value: 0.9
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Motor Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `motor_efficiency` or None if not set

        """
        return self["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9):
        """Corresponds to IDD field `Motor Efficiency`"""
        self["Motor Efficiency"] = value

    @property
    def fraction_of_motor_inefficiencies_to_fluid_stream(self):
        """field `Fraction of Motor Inefficiencies to Fluid Stream`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_motor_inefficiencies_to_fluid_stream` or None if not set

        """
        return self["Fraction of Motor Inefficiencies to Fluid Stream"]

    @fraction_of_motor_inefficiencies_to_fluid_stream.setter
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=None):
        """Corresponds to IDD field `Fraction of Motor Inefficiencies to Fluid
        Stream`"""
        self["Fraction of Motor Inefficiencies to Fluid Stream"] = value

    @property
    def heating_water_inlet_node_name(self):
        """field `Heating Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_water_inlet_node_name` or None if not set

        """
        return self["Heating Water Inlet Node Name"]

    @heating_water_inlet_node_name.setter
    def heating_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Heating Water Inlet Node Name`"""
        self["Heating Water Inlet Node Name"] = value

    @property
    def heating_water_outlet_node_name(self):
        """field `Heating Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_water_outlet_node_name` or None if not set

        """
        return self["Heating Water Outlet Node Name"]

    @heating_water_outlet_node_name.setter
    def heating_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Heating Water Outlet Node Name`"""
        self["Heating Water Outlet Node Name"] = value

    @property
    def heating_high_water_temperature_schedule_name(self):
        """field `Heating High Water Temperature Schedule Name`

        |  Water and control temperatures for heating work together to provide
        |  a linear function that determines the water temperature sent to the
        |  radiant system.  The current control temperature (see Temperature Control Type above) is
        |  compared to the high and low control temperatures at the current time.
        |  If the control temperature is above the high temperature, then the
        |  inlet water temperature is set to the low water temperature.  If the
        |  control temperature is below the low temperature, then the inlet
        |  water temperature is set to the high water temperature.  If the control
        |  temperature is between the high and low value, then the inlet water
        |  temperature is linearly interpolated between the low and high water
        |  temperature values.

        Args:
            value (str): value for IDD Field `Heating High Water Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_high_water_temperature_schedule_name` or None if not set

        """
        return self["Heating High Water Temperature Schedule Name"]

    @heating_high_water_temperature_schedule_name.setter
    def heating_high_water_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating High Water Temperature Schedule
        Name`"""
        self["Heating High Water Temperature Schedule Name"] = value

    @property
    def heating_low_water_temperature_schedule_name(self):
        """field `Heating Low Water Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Water Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_low_water_temperature_schedule_name` or None if not set

        """
        return self["Heating Low Water Temperature Schedule Name"]

    @heating_low_water_temperature_schedule_name.setter
    def heating_low_water_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Low Water Temperature Schedule
        Name`"""
        self["Heating Low Water Temperature Schedule Name"] = value

    @property
    def heating_high_control_temperature_schedule_name(self):
        """field `Heating High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating High Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_high_control_temperature_schedule_name` or None if not set

        """
        return self["Heating High Control Temperature Schedule Name"]

    @heating_high_control_temperature_schedule_name.setter
    def heating_high_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating High Control Temperature Schedule
        Name`"""
        self["Heating High Control Temperature Schedule Name"] = value

    @property
    def heating_low_control_temperature_schedule_name(self):
        """field `Heating Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_low_control_temperature_schedule_name` or None if not set

        """
        return self["Heating Low Control Temperature Schedule Name"]

    @heating_low_control_temperature_schedule_name.setter
    def heating_low_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Low Control Temperature Schedule
        Name`"""
        self["Heating Low Control Temperature Schedule Name"] = value

    @property
    def cooling_water_inlet_node_name(self):
        """field `Cooling Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_water_inlet_node_name` or None if not set

        """
        return self["Cooling Water Inlet Node Name"]

    @cooling_water_inlet_node_name.setter
    def cooling_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Cooling Water Inlet Node Name`"""
        self["Cooling Water Inlet Node Name"] = value

    @property
    def cooling_water_outlet_node_name(self):
        """field `Cooling Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_water_outlet_node_name` or None if not set

        """
        return self["Cooling Water Outlet Node Name"]

    @cooling_water_outlet_node_name.setter
    def cooling_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Cooling Water Outlet Node Name`"""
        self["Cooling Water Outlet Node Name"] = value

    @property
    def cooling_high_water_temperature_schedule_name(self):
        """field `Cooling High Water Temperature Schedule Name`

        |  See note for Heating High Water Temperature Schedule above for
        |  interpretation information (or see the Input/Output Reference).

        Args:
            value (str): value for IDD Field `Cooling High Water Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_high_water_temperature_schedule_name` or None if not set

        """
        return self["Cooling High Water Temperature Schedule Name"]

    @cooling_high_water_temperature_schedule_name.setter
    def cooling_high_water_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling High Water Temperature Schedule
        Name`"""
        self["Cooling High Water Temperature Schedule Name"] = value

    @property
    def cooling_low_water_temperature_schedule_name(self):
        """field `Cooling Low Water Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Water Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_low_water_temperature_schedule_name` or None if not set

        """
        return self["Cooling Low Water Temperature Schedule Name"]

    @cooling_low_water_temperature_schedule_name.setter
    def cooling_low_water_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Low Water Temperature Schedule
        Name`"""
        self["Cooling Low Water Temperature Schedule Name"] = value

    @property
    def cooling_high_control_temperature_schedule_name(self):
        """field `Cooling High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling High Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_high_control_temperature_schedule_name` or None if not set

        """
        return self["Cooling High Control Temperature Schedule Name"]

    @cooling_high_control_temperature_schedule_name.setter
    def cooling_high_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling High Control Temperature Schedule
        Name`"""
        self["Cooling High Control Temperature Schedule Name"] = value

    @property
    def cooling_low_control_temperature_schedule_name(self):
        """field `Cooling Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_low_control_temperature_schedule_name` or None if not set

        """
        return self["Cooling Low Control Temperature Schedule Name"]

    @cooling_low_control_temperature_schedule_name.setter
    def cooling_low_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Low Control Temperature Schedule
        Name`"""
        self["Cooling Low Control Temperature Schedule Name"] = value

    @property
    def condensation_control_type(self):
        """field `Condensation Control Type`

        |  Default value: SimpleOff

        Args:
            value (str): value for IDD Field `Condensation Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condensation_control_type` or None if not set

        """
        return self["Condensation Control Type"]

    @condensation_control_type.setter
    def condensation_control_type(self, value="SimpleOff"):
        """Corresponds to IDD field `Condensation Control Type`"""
        self["Condensation Control Type"] = value

    @property
    def condensation_control_dewpoint_offset(self):
        """field `Condensation Control Dewpoint Offset`

        |  Units: C
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Condensation Control Dewpoint Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condensation_control_dewpoint_offset` or None if not set

        """
        return self["Condensation Control Dewpoint Offset"]

    @condensation_control_dewpoint_offset.setter
    def condensation_control_dewpoint_offset(self, value=1.0):
        """Corresponds to IDD field `Condensation Control Dewpoint Offset`"""
        self["Condensation Control Dewpoint Offset"] = value

    @property
    def number_of_circuits(self):
        """field `Number of Circuits`

        |  Default value: OnePerSurface

        Args:
            value (str): value for IDD Field `Number of Circuits`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `number_of_circuits` or None if not set

        """
        return self["Number of Circuits"]

    @number_of_circuits.setter
    def number_of_circuits(self, value="OnePerSurface"):
        """Corresponds to IDD field `Number of Circuits`"""
        self["Number of Circuits"] = value

    @property
    def circuit_length(self):
        """field `Circuit Length`

        |  Units: m
        |  Default value: 106.7

        Args:
            value (float): value for IDD Field `Circuit Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `circuit_length` or None if not set

        """
        return self["Circuit Length"]

    @circuit_length.setter
    def circuit_length(self, value=106.7):
        """Corresponds to IDD field `Circuit Length`"""
        self["Circuit Length"] = value




class ZoneHvacLowTemperatureRadiantElectric(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:Electric`
        Electric resistance low temperature radiant system
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
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'surface name or radiant surface group name',
                                       {'name': u'Surface Name or Radiant Surface Group Name',
                                        'pyname': u'surface_name_or_radiant_surface_group_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature control type',
                                       {'name': u'Temperature Control Type',
                                        'pyname': u'temperature_control_type',
                                        'default': u'MeanAirTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MeanAirTemperature',
                                                            u'MeanRadiantTemperature',
                                                            u'OperativeTemperature',
                                                            u'OutdoorDryBulbTemperature',
                                                            u'OutdoorWetBulbTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating throttling range',
                                       {'name': u'Heating Throttling Range',
                                        'pyname': u'heating_throttling_range',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'heating setpoint temperature schedule name',
                                       {'name': u'Heating Setpoint Temperature Schedule Name',
                                        'pyname': u'heating_setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:LowTemperatureRadiant:Electric',
               'pyname': u'ZoneHvacLowTemperatureRadiantElectric',
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

        |  Name of zone system is serving

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
    def surface_name_or_radiant_surface_group_name(self):
        """field `Surface Name or Radiant Surface Group Name`

        |  Identifies surfaces that radiant system is embedded in.
        |  For a system with multiple surfaces, enter the name of
        |  a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set

        """
        return self["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """Corresponds to IDD field `Surface Name or Radiant Surface Group
        Name`"""
        self["Surface Name or Radiant Surface Group Name"] = value

    @property
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the maximum electrical heating design capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  IP-Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def temperature_control_type(self):
        """field `Temperature Control Type`

        |  Temperature used to control unit
        |  Default value: MeanAirTemperature

        Args:
            value (str): value for IDD Field `Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_control_type` or None if not set

        """
        return self["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="MeanAirTemperature"):
        """Corresponds to IDD field `Temperature Control Type`"""
        self["Temperature Control Type"] = value

    @property
    def heating_throttling_range(self):
        """field `Heating Throttling Range`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Heating Throttling Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_throttling_range` or None if not set

        """
        return self["Heating Throttling Range"]

    @heating_throttling_range.setter
    def heating_throttling_range(self, value=None):
        """Corresponds to IDD field `Heating Throttling Range`"""
        self["Heating Throttling Range"] = value

    @property
    def heating_setpoint_temperature_schedule_name(self):
        """field `Heating Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Setpoint Temperature Schedule
        Name`"""
        self["Heating Setpoint Temperature Schedule Name"] = value




class ZoneHvacLowTemperatureRadiantSurfaceGroup(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:SurfaceGroup`
        This is used to allow the coordinate control of several radiant system surfaces.
        Note that the following flow fractions must sum up to 1.0
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'flow fraction for surface 1',
                                                  {'name': u'Flow Fraction for Surface 1',
                                                   'pyname': u'flow_fraction_for_surface_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': 'real'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:LowTemperatureRadiant:SurfaceGroup',
               'pyname': u'ZoneHvacLowTemperatureRadiantSurfaceGroup',
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

    def add_extensible(self,
                       surface_1_name=None,
                       flow_fraction_for_surface_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            flow_fraction_for_surface_1 (float): value for IDD Field `Flow Fraction for Surface 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
        flow_fraction_for_surface_1 = self.check_value(
            "Flow Fraction for Surface 1",
            flow_fraction_for_surface_1)
        vals.append(flow_fraction_for_surface_1)
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




class ZoneHvacHighTemperatureRadiant(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:HighTemperatureRadiant`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    _schema = {'extensible-fields': OrderedDict([(u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'fraction of radiant energy to surface 1',
                                                  {'name': u'Fraction of Radiant Energy to Surface 1',
                                                   'pyname': u'fraction_of_radiant_energy_to_surface_1',
                                                   'maximum': 1.0,
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': 'real'})]),
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
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fuel type',
                                       {'name': u'Fuel Type',
                                        'pyname': u'fuel_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'NaturalGas',
                                                            u'Electricity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'combustion efficiency',
                                       {'name': u'Combustion Efficiency',
                                        'pyname': u'combustion_efficiency',
                                        'default': 0.9,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fraction of input converted to radiant energy',
                                       {'name': u'Fraction of Input Converted to Radiant Energy',
                                        'pyname': u'fraction_of_input_converted_to_radiant_energy',
                                        'default': 0.7,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fraction of input converted to latent energy',
                                       {'name': u'Fraction of Input Converted to Latent Energy',
                                        'pyname': u'fraction_of_input_converted_to_latent_energy',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fraction of input that is lost',
                                       {'name': u'Fraction of Input that Is Lost',
                                        'pyname': u'fraction_of_input_that_is_lost',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'temperature control type',
                                       {'name': u'Temperature Control Type',
                                        'pyname': u'temperature_control_type',
                                        'default': u'OperativeTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MeanAirTemperature',
                                                            u'MeanRadiantTemperature',
                                                            u'OperativeTemperature',
                                                            u'MeanAirTemperatureSetpoint',
                                                            u'MeanRadiantTemperatureSetpoint',
                                                            u'OperativeTemperatureSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating throttling range',
                                       {'name': u'Heating Throttling Range',
                                        'pyname': u'heating_throttling_range',
                                        'default': 2.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'heating setpoint temperature schedule name',
                                       {'name': u'Heating Setpoint Temperature Schedule Name',
                                        'pyname': u'heating_setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fraction of radiant energy incident on people',
                                       {'name': u'Fraction of Radiant Energy Incident on People',
                                        'pyname': u'fraction_of_radiant_energy_incident_on_people',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:HighTemperatureRadiant',
               'pyname': u'ZoneHvacHighTemperatureRadiant',
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

        |  Name of zone system is serving

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
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`

        |  Enter the method used to determine the maximum heating power input capacity.
        |  HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        |  is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        |  determine from user specified heating capacity per floor area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set

        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area.Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`

        |  Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set

        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def fuel_type(self):
        """field `Fuel Type`

        |  Natural gas or electricity

        Args:
            value (str): value for IDD Field `Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fuel_type` or None if not set

        """
        return self["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """Corresponds to IDD field `Fuel Type`"""
        self["Fuel Type"] = value

    @property
    def combustion_efficiency(self):
        """field `Combustion Efficiency`

        |  Not used for non-gas radiant heaters
        |  Default value: 0.9
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Combustion Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `combustion_efficiency` or None if not set

        """
        return self["Combustion Efficiency"]

    @combustion_efficiency.setter
    def combustion_efficiency(self, value=0.9):
        """Corresponds to IDD field `Combustion Efficiency`"""
        self["Combustion Efficiency"] = value

    @property
    def fraction_of_input_converted_to_radiant_energy(self):
        """field `Fraction of Input Converted to Radiant Energy`

        |  Radiant+latent+lost fractions must sum to 1 or less, remainder is considered convective heat
        |  Default value: 0.7
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Input Converted to Radiant Energy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_input_converted_to_radiant_energy` or None if not set

        """
        return self["Fraction of Input Converted to Radiant Energy"]

    @fraction_of_input_converted_to_radiant_energy.setter
    def fraction_of_input_converted_to_radiant_energy(self, value=0.7):
        """Corresponds to IDD field `Fraction of Input Converted to Radiant
        Energy`"""
        self["Fraction of Input Converted to Radiant Energy"] = value

    @property
    def fraction_of_input_converted_to_latent_energy(self):
        """field `Fraction of Input Converted to Latent Energy`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Input Converted to Latent Energy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_input_converted_to_latent_energy` or None if not set

        """
        return self["Fraction of Input Converted to Latent Energy"]

    @fraction_of_input_converted_to_latent_energy.setter
    def fraction_of_input_converted_to_latent_energy(self, value=None):
        """Corresponds to IDD field `Fraction of Input Converted to Latent
        Energy`"""
        self["Fraction of Input Converted to Latent Energy"] = value

    @property
    def fraction_of_input_that_is_lost(self):
        """field `Fraction of Input that Is Lost`

        |  Fraction of input vented to outdoor environment
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Input that Is Lost`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_input_that_is_lost` or None if not set

        """
        return self["Fraction of Input that Is Lost"]

    @fraction_of_input_that_is_lost.setter
    def fraction_of_input_that_is_lost(self, value=None):
        """Corresponds to IDD field `Fraction of Input that Is Lost`"""
        self["Fraction of Input that Is Lost"] = value

    @property
    def temperature_control_type(self):
        """field `Temperature Control Type`

        |  Temperature type used to control unit
        |  Default value: OperativeTemperature

        Args:
            value (str): value for IDD Field `Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_control_type` or None if not set

        """
        return self["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="OperativeTemperature"):
        """Corresponds to IDD field `Temperature Control Type`"""
        self["Temperature Control Type"] = value

    @property
    def heating_throttling_range(self):
        """field `Heating Throttling Range`

        |  Units: deltaC
        |  Default value: 2.0

        Args:
            value (float): value for IDD Field `Heating Throttling Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_throttling_range` or None if not set

        """
        return self["Heating Throttling Range"]

    @heating_throttling_range.setter
    def heating_throttling_range(self, value=2.0):
        """Corresponds to IDD field `Heating Throttling Range`"""
        self["Heating Throttling Range"] = value

    @property
    def heating_setpoint_temperature_schedule_name(self):
        """field `Heating Setpoint Temperature Schedule Name`

        |  This setpoint is an "operative temperature" setpoint

        Args:
            value (str): value for IDD Field `Heating Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Setpoint Temperature Schedule
        Name`"""
        self["Heating Setpoint Temperature Schedule Name"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """field `Fraction of Radiant Energy Incident on People`

        |  This will affect thermal comfort but from an energy balance standpoint this value
        |  gets added to the convective gains from the radiant heater
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set

        """
        return self["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """Corresponds to IDD field `Fraction of Radiant Energy Incident on
        People`"""
        self["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
        fraction_of_radiant_energy_to_surface_1 = self.check_value(
            "Fraction of Radiant Energy to Surface 1",
            fraction_of_radiant_energy_to_surface_1)
        vals.append(fraction_of_radiant_energy_to_surface_1)
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




class ZoneHvacVentilatedSlab(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:VentilatedSlab`
        Ventilated slab system where outdoor air flows through hollow cores in a building
        surface (wall, ceiling, or floor).
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
                                      (u'surface name or radiant surface group name',
                                       {'name': u'Surface Name or Radiant Surface Group Name',
                                        'pyname': u'surface_name_or_radiant_surface_group_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
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
                                        'accepted-values': [u'VariablePercent',
                                                            u'FixedTemperature',
                                                            u'FixedAmount'],
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
                                      (u'system configuration type',
                                       {'name': u'System Configuration Type',
                                        'pyname': u'system_configuration_type',
                                        'default': u'SlabOnly',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'SlabOnly',
                                                            u'SlabAndZone',
                                                            u'SeriesSlabs'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'hollow core inside diameter',
                                       {'name': u'Hollow Core Inside Diameter',
                                        'pyname': u'hollow_core_inside_diameter',
                                        'default': 0.05,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'hollow core length',
                                       {'name': u'Hollow Core Length',
                                        'pyname': u'hollow_core_length',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'number of cores',
                                       {'name': u'Number of Cores',
                                        'pyname': u'number_of_cores',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'temperature control type',
                                       {'name': u'Temperature Control Type',
                                        'pyname': u'temperature_control_type',
                                        'default': u'OutdoorDryBulbTemperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'MeanAirTemperature',
                                                            u'MeanRadiantTemperature',
                                                            u'OperativeTemperature',
                                                            u'OutdoorDryBulbTemperature',
                                                            u'OutdoorWetBulbTemperature',
                                                            u'SurfaceTemperature',
                                                            u'ZoneAirDewPointTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating high air temperature schedule name',
                                       {'name': u'Heating High Air Temperature Schedule Name',
                                        'pyname': u'heating_high_air_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating low air temperature schedule name',
                                       {'name': u'Heating Low Air Temperature Schedule Name',
                                        'pyname': u'heating_low_air_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating high control temperature schedule name',
                                       {'name': u'Heating High Control Temperature Schedule Name',
                                        'pyname': u'heating_high_control_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating low control temperature schedule name',
                                       {'name': u'Heating Low Control Temperature Schedule Name',
                                        'pyname': u'heating_low_control_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling high air temperature schedule name',
                                       {'name': u'Cooling High Air Temperature Schedule Name',
                                        'pyname': u'cooling_high_air_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling low air temperature schedule name',
                                       {'name': u'Cooling Low Air Temperature Schedule Name',
                                        'pyname': u'cooling_low_air_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling high control temperature schedule name',
                                       {'name': u'Cooling High Control Temperature Schedule Name',
                                        'pyname': u'cooling_high_control_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling low control temperature schedule name',
                                       {'name': u'Cooling Low Control Temperature Schedule Name',
                                        'pyname': u'cooling_low_control_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'return air node name',
                                       {'name': u'Return Air Node Name',
                                        'pyname': u'return_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'slab in node name',
                                       {'name': u'Slab In Node Name',
                                        'pyname': u'slab_in_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone supply air node name',
                                       {'name': u'Zone Supply Air Node Name',
                                        'pyname': u'zone_supply_air_node_name',
                                        'required-field': False,
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
                                      (u'relief air node name',
                                       {'name': u'Relief Air Node Name',
                                        'pyname': u'relief_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air mixer outlet node name',
                                       {'name': u'Outdoor Air Mixer Outlet Node Name',
                                        'pyname': u'outdoor_air_mixer_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'fan outlet node name',
                                       {'name': u'Fan Outlet Node Name',
                                        'pyname': u'fan_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'fan name',
                                       {'name': u'Fan Name',
                                        'pyname': u'fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'coil option type',
                                       {'name': u'Coil Option Type',
                                        'pyname': u'coil_option_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'Heating',
                                                            u'Cooling',
                                                            u'HeatingAndCooling'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
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
                                      (u'hot water or steam inlet node name',
                                       {'name': u'Hot Water or Steam Inlet Node Name',
                                        'pyname': u'hot_water_or_steam_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
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
                                      (u'cold water inlet node name',
                                       {'name': u'Cold Water Inlet Node Name',
                                        'pyname': u'cold_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
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
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:VentilatedSlab',
               'pyname': u'ZoneHvacVentilatedSlab',
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
    def surface_name_or_radiant_surface_group_name(self):
        """field `Surface Name or Radiant Surface Group Name`

        |  (name of surface system is embedded in) or list of surfaces

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set

        """
        return self["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """Corresponds to IDD field `Surface Name or Radiant Surface Group
        Name`"""
        self["Surface Name or Radiant Surface Group Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

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

        |  schedule values multiply the minimum outdoor air flow rate
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

        |  Note that this depends on the control type as to whether schedule values are a fraction or temperature

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
    def system_configuration_type(self):
        """field `System Configuration Type`

        |  Default value: SlabOnly

        Args:
            value (str): value for IDD Field `System Configuration Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `system_configuration_type` or None if not set

        """
        return self["System Configuration Type"]

    @system_configuration_type.setter
    def system_configuration_type(self, value="SlabOnly"):
        """Corresponds to IDD field `System Configuration Type`"""
        self["System Configuration Type"] = value

    @property
    def hollow_core_inside_diameter(self):
        """field `Hollow Core Inside Diameter`

        |  Units: m
        |  IP-Units: in
        |  Default value: 0.05

        Args:
            value (float): value for IDD Field `Hollow Core Inside Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hollow_core_inside_diameter` or None if not set

        """
        return self["Hollow Core Inside Diameter"]

    @hollow_core_inside_diameter.setter
    def hollow_core_inside_diameter(self, value=0.05):
        """Corresponds to IDD field `Hollow Core Inside Diameter`"""
        self["Hollow Core Inside Diameter"] = value

    @property
    def hollow_core_length(self):
        """field `Hollow Core Length`

        |  (length of core cavity embedded in surface)
        |  Units: m

        Args:
            value (float): value for IDD Field `Hollow Core Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hollow_core_length` or None if not set

        """
        return self["Hollow Core Length"]

    @hollow_core_length.setter
    def hollow_core_length(self, value=None):
        """Corresponds to IDD field `Hollow Core Length`"""
        self["Hollow Core Length"] = value

    @property
    def number_of_cores(self):
        """field `Number of Cores`

        |  flow will be divided evenly among the cores

        Args:
            value (float): value for IDD Field `Number of Cores`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `number_of_cores` or None if not set

        """
        return self["Number of Cores"]

    @number_of_cores.setter
    def number_of_cores(self, value=None):
        """Corresponds to IDD field `Number of Cores`"""
        self["Number of Cores"] = value

    @property
    def temperature_control_type(self):
        """field `Temperature Control Type`

        |  (temperature on which unit is controlled)
        |  Default value: OutdoorDryBulbTemperature

        Args:
            value (str): value for IDD Field `Temperature Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_control_type` or None if not set

        """
        return self["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="OutdoorDryBulbTemperature"):
        """Corresponds to IDD field `Temperature Control Type`"""
        self["Temperature Control Type"] = value

    @property
    def heating_high_air_temperature_schedule_name(self):
        """field `Heating High Air Temperature Schedule Name`

        |  Air and control temperatures for heating work together to provide
        |  a linear function that determines the air temperature sent to the
        |  radiant system. The current control temperature (see A14) is
        |  compared to the high and low control temperatures at the current time.
        |  If the control temperature is above the high temperature, then the
        |  inlet air temperature is set to the low air temperature. If the
        |  control temperature is below the low temperature, then the inlet
        |  air temperature is set to the high air temperature. If the control
        |  temperature is between the high and low value, then the inlet air
        |  temperature is linearly interpolated between the low and high air
        |  temperature values.

        Args:
            value (str): value for IDD Field `Heating High Air Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_high_air_temperature_schedule_name` or None if not set

        """
        return self["Heating High Air Temperature Schedule Name"]

    @heating_high_air_temperature_schedule_name.setter
    def heating_high_air_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating High Air Temperature Schedule
        Name`"""
        self["Heating High Air Temperature Schedule Name"] = value

    @property
    def heating_low_air_temperature_schedule_name(self):
        """field `Heating Low Air Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Air Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_low_air_temperature_schedule_name` or None if not set

        """
        return self["Heating Low Air Temperature Schedule Name"]

    @heating_low_air_temperature_schedule_name.setter
    def heating_low_air_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Low Air Temperature Schedule
        Name`"""
        self["Heating Low Air Temperature Schedule Name"] = value

    @property
    def heating_high_control_temperature_schedule_name(self):
        """field `Heating High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating High Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_high_control_temperature_schedule_name` or None if not set

        """
        return self["Heating High Control Temperature Schedule Name"]

    @heating_high_control_temperature_schedule_name.setter
    def heating_high_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating High Control Temperature Schedule
        Name`"""
        self["Heating High Control Temperature Schedule Name"] = value

    @property
    def heating_low_control_temperature_schedule_name(self):
        """field `Heating Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_low_control_temperature_schedule_name` or None if not set

        """
        return self["Heating Low Control Temperature Schedule Name"]

    @heating_low_control_temperature_schedule_name.setter
    def heating_low_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Low Control Temperature Schedule
        Name`"""
        self["Heating Low Control Temperature Schedule Name"] = value

    @property
    def cooling_high_air_temperature_schedule_name(self):
        """field `Cooling High Air Temperature Schedule Name`

        |  See note for heating high air temperature schedule above for
        |  interpretation information (or see the Input/Output Reference).

        Args:
            value (str): value for IDD Field `Cooling High Air Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_high_air_temperature_schedule_name` or None if not set

        """
        return self["Cooling High Air Temperature Schedule Name"]

    @cooling_high_air_temperature_schedule_name.setter
    def cooling_high_air_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling High Air Temperature Schedule
        Name`"""
        self["Cooling High Air Temperature Schedule Name"] = value

    @property
    def cooling_low_air_temperature_schedule_name(self):
        """field `Cooling Low Air Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Air Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_low_air_temperature_schedule_name` or None if not set

        """
        return self["Cooling Low Air Temperature Schedule Name"]

    @cooling_low_air_temperature_schedule_name.setter
    def cooling_low_air_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Low Air Temperature Schedule
        Name`"""
        self["Cooling Low Air Temperature Schedule Name"] = value

    @property
    def cooling_high_control_temperature_schedule_name(self):
        """field `Cooling High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling High Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_high_control_temperature_schedule_name` or None if not set

        """
        return self["Cooling High Control Temperature Schedule Name"]

    @cooling_high_control_temperature_schedule_name.setter
    def cooling_high_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling High Control Temperature Schedule
        Name`"""
        self["Cooling High Control Temperature Schedule Name"] = value

    @property
    def cooling_low_control_temperature_schedule_name(self):
        """field `Cooling Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Control Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_low_control_temperature_schedule_name` or None if not set

        """
        return self["Cooling Low Control Temperature Schedule Name"]

    @cooling_low_control_temperature_schedule_name.setter
    def cooling_low_control_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Low Control Temperature Schedule
        Name`"""
        self["Cooling Low Control Temperature Schedule Name"] = value

    @property
    def return_air_node_name(self):
        """field `Return Air Node Name`

        |  This is the zone return air inlet to the ventilated slab system outdoor air mixer.
        |  This node is typically a zone exhaust node (do not connect to "Zone Return Air Node").

        Args:
            value (str): value for IDD Field `Return Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_air_node_name` or None if not set

        """
        return self["Return Air Node Name"]

    @return_air_node_name.setter
    def return_air_node_name(self, value=None):
        """Corresponds to IDD field `Return Air Node Name`"""
        self["Return Air Node Name"] = value

    @property
    def slab_in_node_name(self):
        """field `Slab In Node Name`

        |  This is the node entering the slab or series of slabs after the fan and coil(s).

        Args:
            value (str): value for IDD Field `Slab In Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slab_in_node_name` or None if not set

        """
        return self["Slab In Node Name"]

    @slab_in_node_name.setter
    def slab_in_node_name(self, value=None):
        """Corresponds to IDD field `Slab In Node Name`"""
        self["Slab In Node Name"] = value

    @property
    def zone_supply_air_node_name(self):
        """field `Zone Supply Air Node Name`

        |  This is the node name exiting the slab.
        |  This node is typically a zone inlet node.
        |  Leave blank when the system configuration is SlabOnly or SeriesSlabs.

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
    def outdoor_air_node_name(self):
        """field `Outdoor Air Node Name`

        |  This node is the outdoor air inlet to the ventilated slab oa mixer.
        |  This node should also be specified in an OutdoorAir:Node or OutdoorAir:NodeList object.

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
    def relief_air_node_name(self):
        """field `Relief Air Node Name`

        |  This node is the relief air node from the ventilated slab outdoor air mixer.

        Args:
            value (str): value for IDD Field `Relief Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `relief_air_node_name` or None if not set

        """
        return self["Relief Air Node Name"]

    @relief_air_node_name.setter
    def relief_air_node_name(self, value=None):
        """Corresponds to IDD field `Relief Air Node Name`"""
        self["Relief Air Node Name"] = value

    @property
    def outdoor_air_mixer_outlet_node_name(self):
        """field `Outdoor Air Mixer Outlet Node Name`

        |  This is the node name leaving the outdoor air mixer and entering the fan and coil(s).

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_mixer_outlet_node_name` or None if not set

        """
        return self["Outdoor Air Mixer Outlet Node Name"]

    @outdoor_air_mixer_outlet_node_name.setter
    def outdoor_air_mixer_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Mixer Outlet Node Name`"""
        self["Outdoor Air Mixer Outlet Node Name"] = value

    @property
    def fan_outlet_node_name(self):
        """field `Fan Outlet Node Name`

        |  This is the node name of the fan outlet.

        Args:
            value (str): value for IDD Field `Fan Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_outlet_node_name` or None if not set

        """
        return self["Fan Outlet Node Name"]

    @fan_outlet_node_name.setter
    def fan_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Fan Outlet Node Name`"""
        self["Fan Outlet Node Name"] = value

    @property
    def fan_name(self):
        """field `Fan Name`

        |  Allowable fan type is Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_name` or None if not set

        """
        return self["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """Corresponds to IDD field `Fan Name`"""
        self["Fan Name"] = value

    @property
    def coil_option_type(self):
        """field `Coil Option Type`

        Args:
            value (str): value for IDD Field `Coil Option Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `coil_option_type` or None if not set

        """
        return self["Coil Option Type"]

    @coil_option_type.setter
    def coil_option_type(self, value=None):
        """Corresponds to IDD field `Coil Option Type`"""
        self["Coil Option Type"] = value

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
    def hot_water_or_steam_inlet_node_name(self):
        """field `Hot Water or Steam Inlet Node Name`

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set

        """
        return self["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water or Steam Inlet Node Name`"""
        self["Hot Water or Steam Inlet Node Name"] = value

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
    def cold_water_inlet_node_name(self):
        """field `Cold Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cold Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_water_inlet_node_name` or None if not set

        """
        return self["Cold Water Inlet Node Name"]

    @cold_water_inlet_node_name.setter
    def cold_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Cold Water Inlet Node Name`"""
        self["Cold Water Inlet Node Name"] = value

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




class ZoneHvacVentilatedSlabSlabGroup(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:VentilatedSlab:SlabGroup`
        This is used to allow the coordinate control of several ventilated slab system
        surfaces. Note that the flow fractions must sum up to 1.0.
        The number of surfaces can be expanded beyond 10, if necessary, by adding more
        groups to the end of the list
    """
    _schema = {'extensible-fields': OrderedDict([(u'zone 1 name',
                                                  {'name': u'Zone 1 Name',
                                                   'pyname': u'zone_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'surface 1 name',
                                                  {'name': u'Surface 1 Name',
                                                   'pyname': u'surface_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'}),
                                                 (u'core diameter for surface 1',
                                                  {'name': u'Core Diameter for Surface 1',
                                                   'pyname': u'core_diameter_for_surface_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm'}),
                                                 (u'core length for surface 1',
                                                  {'name': u'Core Length for Surface 1',
                                                   'pyname': u'core_length_for_surface_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': u'real',
                                                   'unit': u'm'}),
                                                 (u'core numbers for surface 1',
                                                  {'name': u'Core Numbers for Surface 1',
                                                   'pyname': u'core_numbers_for_surface_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'minimum': 0.0,
                                                   'autocalculatable': False,
                                                   'type': 'real'}),
                                                 (u'slab inlet node name for surface 1',
                                                  {'name': u'Slab Inlet Node Name for Surface 1',
                                                   'pyname': u'slab_inlet_node_name_for_surface_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'}),
                                                 (u'slab outlet node name for surface 1',
                                                  {'name': u'Slab Outlet Node Name for Surface 1',
                                                   'pyname': u'slab_outlet_node_name_for_surface_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Zone HVAC Radiative',
               'min-fields': 0,
               'name': u'ZoneHVAC:VentilatedSlab:SlabGroup',
               'pyname': u'ZoneHvacVentilatedSlabSlabGroup',
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

    def add_extensible(self,
                       zone_1_name=None,
                       surface_1_name=None,
                       core_diameter_for_surface_1=None,
                       core_length_for_surface_1=None,
                       core_numbers_for_surface_1=None,
                       slab_inlet_node_name_for_surface_1=None,
                       slab_outlet_node_name_for_surface_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            zone_1_name (str): value for IDD Field `Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            core_diameter_for_surface_1 (float): value for IDD Field `Core Diameter for Surface 1`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            core_length_for_surface_1 (float): value for IDD Field `Core Length for Surface 1`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            core_numbers_for_surface_1 (float): value for IDD Field `Core Numbers for Surface 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            slab_inlet_node_name_for_surface_1 (str): value for IDD Field `Slab Inlet Node Name for Surface 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            slab_outlet_node_name_for_surface_1 (str): value for IDD Field `Slab Outlet Node Name for Surface 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        zone_1_name = self.check_value("Zone 1 Name", zone_1_name)
        vals.append(zone_1_name)
        surface_1_name = self.check_value("Surface 1 Name", surface_1_name)
        vals.append(surface_1_name)
        core_diameter_for_surface_1 = self.check_value(
            "Core Diameter for Surface 1",
            core_diameter_for_surface_1)
        vals.append(core_diameter_for_surface_1)
        core_length_for_surface_1 = self.check_value(
            "Core Length for Surface 1",
            core_length_for_surface_1)
        vals.append(core_length_for_surface_1)
        core_numbers_for_surface_1 = self.check_value(
            "Core Numbers for Surface 1",
            core_numbers_for_surface_1)
        vals.append(core_numbers_for_surface_1)
        slab_inlet_node_name_for_surface_1 = self.check_value(
            "Slab Inlet Node Name for Surface 1",
            slab_inlet_node_name_for_surface_1)
        vals.append(slab_inlet_node_name_for_surface_1)
        slab_outlet_node_name_for_surface_1 = self.check_value(
            "Slab Outlet Node Name for Surface 1",
            slab_outlet_node_name_for_surface_1)
        vals.append(slab_outlet_node_name_for_surface_1)
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


