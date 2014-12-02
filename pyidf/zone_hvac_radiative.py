from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ZoneHvacBaseboardRadiantConvectiveWater(object):
    """ Corresponds to IDD object `ZoneHVAC:Baseboard:RadiantConvective:Water`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    internal_name = "ZoneHVAC:Baseboard:RadiantConvective:Water"
    field_count = 14
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Heating Design Capacity Method", "Maximum Water Flow Rate", "Fraction Radiant"]
    extensible_fields = 2
    format = None
    min_fields = 12
    extensible_keys = ["Surface 1 Name", "Fraction of Radiant Energy to Surface 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:Baseboard:RadiantConvective:Water`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Rated Average Water Temperature"] = None
        self._data["Rated Water Mass Flow Rate"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Maximum Water Flow Rate"] = None
        self._data["Convergence Tolerance"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction of Radiant Energy Incident on People"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_average_water_temperature = None
        else:
            self.rated_average_water_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_water_mass_flow_rate = None
        else:
            self.rated_water_mass_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate = None
        else:
            self.maximum_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_radiant_energy_incident_on_people = None
        else:
            self.fraction_of_radiant_energy_incident_on_people = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.inlet_node_name`')
        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def rated_average_water_temperature(self):
        """Get rated_average_water_temperature

        Returns:
            float: the value of `rated_average_water_temperature` or None if not set
        """
        return self._data["Rated Average Water Temperature"]

    @rated_average_water_temperature.setter
    def rated_average_water_temperature(self, value=87.78):
        """  Corresponds to IDD Field `Rated Average Water Temperature`
        Rated average water temperature is the average of the inlet and outlet water temperatures
        at rated conditions.

        Args:
            value (float): value for IDD Field `Rated Average Water Temperature`
                Units: C
                Default value: 87.78
                value >= 20.0
                value <= 150.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.rated_average_water_temperature`'.format(value))
            if value < 20.0:
                raise ValueError('value need to be greater or equal 20.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.rated_average_water_temperature`')
            if value > 150.0:
                raise ValueError('value need to be smaller 150.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.rated_average_water_temperature`')
        self._data["Rated Average Water Temperature"] = value

    @property
    def rated_water_mass_flow_rate(self):
        """Get rated_water_mass_flow_rate

        Returns:
            float: the value of `rated_water_mass_flow_rate` or None if not set
        """
        return self._data["Rated Water Mass Flow Rate"]

    @rated_water_mass_flow_rate.setter
    def rated_water_mass_flow_rate(self, value=0.063):
        """  Corresponds to IDD Field `Rated Water Mass Flow Rate`
        Standard is I=B=R Rating document where all baseboards are rated at either 0.063 kg/s (1 gpm)
        or 0.252 kg/s (4 gpm).  It is recommended that users find data for the baseboard heater that
        corresponds to performance at 0.063 kg/s unless the flow rate is expected to be above 0.252 kg/s.
        If the flow rate is expected to be above 0.252 kg/s, this field should be 0.252 kg/s.

        Args:
            value (float): value for IDD Field `Rated Water Mass Flow Rate`
                Units: Kg/s
                Default value: 0.063
                value > 0.0
                value <= 10.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.rated_water_mass_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.rated_water_mass_flow_rate`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.rated_water_mass_flow_rate`')
        self._data["Rated Water Mass Flow Rate"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity. Required field when the heating design capacity method
        HeatingDesignCapacity. This input field is rated heating capacity. Users must multiply the
        actual finned length published in the literature to determine the rated capacity. Rated
        Capacity is for an inlet air dry-bulb temperature of 18.0C, the Rated Water Mass Flow Rate
        of 0.063kg/s or 0.252kg/s, and the Rated Average Water Temperature between 32.2C and 115.6C.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def maximum_water_flow_rate(self):
        """Get maximum_water_flow_rate

        Returns:
            float: the value of `maximum_water_flow_rate` or None if not set
        """
        return self._data["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Water Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Water Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.maximum_water_flow_rate`'.format(value))
                    self._data["Maximum Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.maximum_water_flow_rate`'.format(value))
        self._data["Maximum Water Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """  Corresponds to IDD Field `Fraction Radiant`

        Args:
            value (float): value for IDD Field `Fraction Radiant`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_radiant`')
        self._data["Fraction Radiant"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """Get fraction_of_radiant_energy_incident_on_people

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set
        """
        return self._data["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """  Corresponds to IDD Field `Fraction of Radiant Energy Incident on People`

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_radiant_energy_incident_on_people`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_radiant_energy_incident_on_people`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_radiant_energy_incident_on_people`')
        self._data["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
        vals.append(self._check_fraction_of_radiant_energy_to_surface_1(fraction_of_radiant_energy_to_surface_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.surface_1_name`')
        return value

    def _check_fraction_of_radiant_energy_to_surface_1(self, value):
        """ Validates falue of field `Fraction of Radiant Energy to Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_radiant_energy_to_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_radiant_energy_to_surface_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveWater.fraction_of_radiant_energy_to_surface_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacBaseboardRadiantConvectiveWater:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacBaseboardRadiantConvectiveWater:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacBaseboardRadiantConvectiveWater: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacBaseboardRadiantConvectiveWater: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacBaseboardRadiantConvectiveSteam(object):
    """ Corresponds to IDD object `ZoneHVAC:Baseboard:RadiantConvective:Steam`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    internal_name = "ZoneHVAC:Baseboard:RadiantConvective:Steam"
    field_count = 13
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Heating Design Capacity Method", "Maximum Steam Flow Rate", "Fraction Radiant"]
    extensible_fields = 2
    format = None
    min_fields = 11
    extensible_keys = ["Surface 1 Name", "Fraction of Radiant Energy to Surface 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:Baseboard:RadiantConvective:Steam`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Degree of SubCooling"] = None
        self._data["Maximum Steam Flow Rate"] = None
        self._data["Convergence Tolerance"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction of Radiant Energy Incident on People"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.degree_of_subcooling = None
        else:
            self.degree_of_subcooling = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_steam_flow_rate = None
        else:
            self.maximum_steam_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_radiant_energy_incident_on_people = None
        else:
            self.fraction_of_radiant_energy_incident_on_people = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.inlet_node_name`')
        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def degree_of_subcooling(self):
        """Get degree_of_subcooling

        Returns:
            float: the value of `degree_of_subcooling` or None if not set
        """
        return self._data["Degree of SubCooling"]

    @degree_of_subcooling.setter
    def degree_of_subcooling(self, value=5.0):
        """  Corresponds to IDD Field `Degree of SubCooling`

        Args:
            value (float): value for IDD Field `Degree of SubCooling`
                Units: deltaC
                Default value: 5.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.degree_of_subcooling`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.degree_of_subcooling`')
        self._data["Degree of SubCooling"] = value

    @property
    def maximum_steam_flow_rate(self):
        """Get maximum_steam_flow_rate

        Returns:
            float: the value of `maximum_steam_flow_rate` or None if not set
        """
        return self._data["Maximum Steam Flow Rate"]

    @maximum_steam_flow_rate.setter
    def maximum_steam_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Steam Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Steam Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Steam Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.maximum_steam_flow_rate`'.format(value))
                    self._data["Maximum Steam Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.maximum_steam_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.maximum_steam_flow_rate`')
        self._data["Maximum Steam Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """  Corresponds to IDD Field `Fraction Radiant`

        Args:
            value (float): value for IDD Field `Fraction Radiant`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_radiant`')
        self._data["Fraction Radiant"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """Get fraction_of_radiant_energy_incident_on_people

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set
        """
        return self._data["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """  Corresponds to IDD Field `Fraction of Radiant Energy Incident on People`

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_radiant_energy_incident_on_people`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_radiant_energy_incident_on_people`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_radiant_energy_incident_on_people`')
        self._data["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
        vals.append(self._check_fraction_of_radiant_energy_to_surface_1(fraction_of_radiant_energy_to_surface_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.surface_1_name`')
        return value

    def _check_fraction_of_radiant_energy_to_surface_1(self, value):
        """ Validates falue of field `Fraction of Radiant Energy to Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_radiant_energy_to_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_radiant_energy_to_surface_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveSteam.fraction_of_radiant_energy_to_surface_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacBaseboardRadiantConvectiveSteam:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacBaseboardRadiantConvectiveSteam:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacBaseboardRadiantConvectiveSteam: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacBaseboardRadiantConvectiveSteam: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacBaseboardRadiantConvectiveElectric(object):
    """ Corresponds to IDD object `ZoneHVAC:Baseboard:RadiantConvective:Electric`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    internal_name = "ZoneHVAC:Baseboard:RadiantConvective:Electric"
    field_count = 9
    required_fields = ["Name", "Heating Design Capacity Method", "Efficiency", "Fraction Radiant"]
    extensible_fields = 2
    format = None
    min_fields = 8
    extensible_keys = ["Surface 1 Name", "Fraction of Radiant Energy to Surface 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:Baseboard:RadiantConvective:Electric`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Efficiency"] = None
        self._data["Fraction Radiant"] = None
        self._data["Fraction of Radiant Energy Incident on People"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.efficiency = None
        else:
            self.efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_radiant = None
        else:
            self.fraction_radiant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_radiant_energy_incident_on_people = None
        else:
            self.fraction_of_radiant_energy_incident_on_people = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def efficiency(self):
        """Get efficiency

        Returns:
            float: the value of `efficiency` or None if not set
        """
        return self._data["Efficiency"]

    @efficiency.setter
    def efficiency(self, value=1.0):
        """  Corresponds to IDD Field `Efficiency`

        Args:
            value (float): value for IDD Field `Efficiency`
                Default value: 1.0
                value > 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.efficiency`')
        self._data["Efficiency"] = value

    @property
    def fraction_radiant(self):
        """Get fraction_radiant

        Returns:
            float: the value of `fraction_radiant` or None if not set
        """
        return self._data["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """  Corresponds to IDD Field `Fraction Radiant`

        Args:
            value (float): value for IDD Field `Fraction Radiant`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_radiant`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_radiant`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_radiant`')
        self._data["Fraction Radiant"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """Get fraction_of_radiant_energy_incident_on_people

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set
        """
        return self._data["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """  Corresponds to IDD Field `Fraction of Radiant Energy Incident on People`

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_radiant_energy_incident_on_people`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_radiant_energy_incident_on_people`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_radiant_energy_incident_on_people`')
        self._data["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
        vals.append(self._check_fraction_of_radiant_energy_to_surface_1(fraction_of_radiant_energy_to_surface_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.surface_1_name`')
        return value

    def _check_fraction_of_radiant_energy_to_surface_1(self, value):
        """ Validates falue of field `Fraction of Radiant Energy to Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_radiant_energy_to_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_radiant_energy_to_surface_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardRadiantConvectiveElectric.fraction_of_radiant_energy_to_surface_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacBaseboardRadiantConvectiveElectric:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacBaseboardRadiantConvectiveElectric:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacBaseboardRadiantConvectiveElectric: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacBaseboardRadiantConvectiveElectric: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacBaseboardConvectiveWater(object):
    """ Corresponds to IDD object `ZoneHVAC:Baseboard:Convective:Water`
        Hot water baseboard heater, convection-only. Natural convection hydronic heating unit.
    """
    internal_name = "ZoneHVAC:Baseboard:Convective:Water"
    field_count = 11
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Heating Design Capacity Method", "U-Factor Times Area Value", "Maximum Water Flow Rate"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:Baseboard:Convective:Water`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["U-Factor Times Area Value"] = None
        self._data["Maximum Water Flow Rate"] = None
        self._data["Convergence Tolerance"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ufactor_times_area_value = None
        else:
            self.ufactor_times_area_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate = None
        else:
            self.maximum_water_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_tolerance = None
        else:
            self.convergence_tolerance = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveWater.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveWater.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveWater.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveWater.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveWater.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveWater.inlet_node_name`')
        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveWater.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveWater.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveWater.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveWater.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def ufactor_times_area_value(self):
        """Get ufactor_times_area_value

        Returns:
            float: the value of `ufactor_times_area_value` or None if not set
        """
        return self._data["U-Factor Times Area Value"]

    @ufactor_times_area_value.setter
    def ufactor_times_area_value(self, value=None):
        """  Corresponds to IDD Field `U-Factor Times Area Value`

        Args:
            value (float or "Autosize"): value for IDD Field `U-Factor Times Area Value`
                Units: W/K
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["U-Factor Times Area Value"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardConvectiveWater.ufactor_times_area_value`'.format(value))
                    self._data["U-Factor Times Area Value"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.ufactor_times_area_value`'.format(value))
        self._data["U-Factor Times Area Value"] = value

    @property
    def maximum_water_flow_rate(self):
        """Get maximum_water_flow_rate

        Returns:
            float: the value of `maximum_water_flow_rate` or None if not set
        """
        return self._data["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Water Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Water Flow Rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Water Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardConvectiveWater.maximum_water_flow_rate`'.format(value))
                    self._data["Maximum Water Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.maximum_water_flow_rate`'.format(value))
        self._data["Maximum Water Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Tolerance`

        Args:
            value (float): value for IDD Field `Convergence Tolerance`
                Default value: 0.001
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardConvectiveWater.convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveWater.convergence_tolerance`')
        self._data["Convergence Tolerance"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacBaseboardConvectiveWater:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacBaseboardConvectiveWater:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacBaseboardConvectiveWater: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacBaseboardConvectiveWater: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacBaseboardConvectiveElectric(object):
    """ Corresponds to IDD object `ZoneHVAC:Baseboard:Convective:Electric`
        Electric baseboard heater, convection-only. Natural convection electric heating unit.
    """
    internal_name = "ZoneHVAC:Baseboard:Convective:Electric"
    field_count = 7
    required_fields = ["Name", "Heating Design Capacity Method", "Efficiency"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:Baseboard:Convective:Electric`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Efficiency"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.efficiency = None
        else:
            self.efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def efficiency(self):
        """Get efficiency

        Returns:
            float: the value of `efficiency` or None if not set
        """
        return self._data["Efficiency"]

    @efficiency.setter
    def efficiency(self, value=1.0):
        """  Corresponds to IDD Field `Efficiency`

        Args:
            value (float): value for IDD Field `Efficiency`
                Default value: 1.0
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacBaseboardConvectiveElectric.efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacBaseboardConvectiveElectric.efficiency`')
        self._data["Efficiency"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacBaseboardConvectiveElectric:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacBaseboardConvectiveElectric:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacBaseboardConvectiveElectric: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacBaseboardConvectiveElectric: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacLowTemperatureRadiantVariableFlow(object):
    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:VariableFlow`
        Low temperature hydronic radiant heating and/or cooling system embedded in a building
        surface (wall, ceiling, or floor). Controlled by varying the hot or chilled water
        flow to the unit.
    """
    internal_name = "ZoneHVAC:LowTemperatureRadiant:VariableFlow"
    field_count = 29
    required_fields = ["Name", "Heating Design Capacity Method"]
    extensible_fields = 0
    format = None
    min_fields = 29
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:LowTemperatureRadiant:VariableFlow`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Surface Name or Radiant Surface Group Name"] = None
        self._data["Hydronic Tubing Inside Diameter"] = None
        self._data["Hydronic Tubing Length"] = None
        self._data["Temperature Control Type"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Maximum Hot Water Flow"] = None
        self._data["Heating Water Inlet Node Name"] = None
        self._data["Heating Water Outlet Node Name"] = None
        self._data["Heating Control Throttling Range"] = None
        self._data["Heating Control Temperature Schedule Name"] = None
        self._data["Cooling Design Capacity Method"] = None
        self._data["Cooling Design Capacity"] = None
        self._data["Cooling Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Cooling Design Capacity"] = None
        self._data["Maximum Cold Water Flow"] = None
        self._data["Cooling Water Inlet Node Name"] = None
        self._data["Cooling Water Outlet Node Name"] = None
        self._data["Cooling Control Throttling Range"] = None
        self._data["Cooling Control Temperature Schedule Name"] = None
        self._data["Condensation Control Type"] = None
        self._data["Condensation Control Dewpoint Offset"] = None
        self._data["Number of Circuits"] = None
        self._data["Circuit Length"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_or_radiant_surface_group_name = None
        else:
            self.surface_name_or_radiant_surface_group_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_inside_diameter = None
        else:
            self.hydronic_tubing_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_length = None
        else:
            self.hydronic_tubing_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_control_type = None
        else:
            self.temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hot_water_flow = None
        else:
            self.maximum_hot_water_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_water_inlet_node_name = None
        else:
            self.heating_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_water_outlet_node_name = None
        else:
            self.heating_water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_control_throttling_range = None
        else:
            self.heating_control_throttling_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_control_temperature_schedule_name = None
        else:
            self.heating_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity_method = None
        else:
            self.cooling_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity = None
        else:
            self.cooling_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity_per_floor_area = None
        else:
            self.cooling_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_capacity = None
        else:
            self.fraction_of_autosized_cooling_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_cold_water_flow = None
        else:
            self.maximum_cold_water_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_water_inlet_node_name = None
        else:
            self.cooling_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_water_outlet_node_name = None
        else:
            self.cooling_water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_control_throttling_range = None
        else:
            self.cooling_control_throttling_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_control_temperature_schedule_name = None
        else:
            self.cooling_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensation_control_type = None
        else:
            self.condensation_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensation_control_dewpoint_offset = None
        else:
            self.condensation_control_dewpoint_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_circuits = None
        else:
            self.number_of_circuits = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circuit_length = None
        else:
            self.circuit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of zone system is serving

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.zone_name`')
        self._data["Zone Name"] = value

    @property
    def surface_name_or_radiant_surface_group_name(self):
        """Get surface_name_or_radiant_surface_group_name

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set
        """
        return self._data["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name or Radiant Surface Group Name`
        Identifies surfaces that radiant system is embedded in.
        For a system with multiple surfaces, enter the name of
        a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.surface_name_or_radiant_surface_group_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.surface_name_or_radiant_surface_group_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.surface_name_or_radiant_surface_group_name`')
        self._data["Surface Name or Radiant Surface Group Name"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """Get hydronic_tubing_inside_diameter

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=0.013):
        """  Corresponds to IDD Field `Hydronic Tubing Inside Diameter`

        Args:
            value (float): value for IDD Field `Hydronic Tubing Inside Diameter`
                Units: m
                IP-Units: in
                Default value: 0.013
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.hydronic_tubing_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.hydronic_tubing_inside_diameter`')
        self._data["Hydronic Tubing Inside Diameter"] = value

    @property
    def hydronic_tubing_length(self):
        """Get hydronic_tubing_length

        Returns:
            float: the value of `hydronic_tubing_length` or None if not set
        """
        return self._data["Hydronic Tubing Length"]

    @hydronic_tubing_length.setter
    def hydronic_tubing_length(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tubing Length`
        (total length of pipe embedded in surface)

        Args:
            value (float or "Autosize"): value for IDD Field `Hydronic Tubing Length`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Hydronic Tubing Length"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.hydronic_tubing_length`'.format(value))
                    self._data["Hydronic Tubing Length"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.hydronic_tubing_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.hydronic_tubing_length`')
        self._data["Hydronic Tubing Length"] = value

    @property
    def temperature_control_type(self):
        """Get temperature_control_type

        Returns:
            str: the value of `temperature_control_type` or None if not set
        """
        return self._data["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="MeanAirTemperature"):
        """  Corresponds to IDD Field `Temperature Control Type`
        (Temperature on which unit is controlled)

        Args:
            value (str): value for IDD Field `Temperature Control Type`
                Accepted values are:
                      - MeanAirTemperature
                      - MeanRadiantTemperature
                      - OperativeTemperature
                      - OutdoorDryBulbTemperature
                      - OutdoorWetBulbTemperature
                Default value: MeanAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.temperature_control_type`')
            vals = {}
            vals["meanairtemperature"] = "MeanAirTemperature"
            vals["meanradianttemperature"] = "MeanRadiantTemperature"
            vals["operativetemperature"] = "OperativeTemperature"
            vals["outdoordrybulbtemperature"] = "OutdoorDryBulbTemperature"
            vals["outdoorwetbulbtemperature"] = "OutdoorWetBulbTemperature"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantVariableFlow.temperature_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantVariableFlow.temperature_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Temperature Control Type"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def maximum_hot_water_flow(self):
        """Get maximum_hot_water_flow

        Returns:
            float: the value of `maximum_hot_water_flow` or None if not set
        """
        return self._data["Maximum Hot Water Flow"]

    @maximum_hot_water_flow.setter
    def maximum_hot_water_flow(self, value=None):
        """  Corresponds to IDD Field `Maximum Hot Water Flow`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water Flow`
                Units: m3/s
                IP-Units: gal/min
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Hot Water Flow"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.maximum_hot_water_flow`'.format(value))
                    self._data["Maximum Hot Water Flow"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.maximum_hot_water_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.maximum_hot_water_flow`')
        self._data["Maximum Hot Water Flow"] = value

    @property
    def heating_water_inlet_node_name(self):
        """Get heating_water_inlet_node_name

        Returns:
            str: the value of `heating_water_inlet_node_name` or None if not set
        """
        return self._data["Heating Water Inlet Node Name"]

    @heating_water_inlet_node_name.setter
    def heating_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Heating Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_water_inlet_node_name`')
        self._data["Heating Water Inlet Node Name"] = value

    @property
    def heating_water_outlet_node_name(self):
        """Get heating_water_outlet_node_name

        Returns:
            str: the value of `heating_water_outlet_node_name` or None if not set
        """
        return self._data["Heating Water Outlet Node Name"]

    @heating_water_outlet_node_name.setter
    def heating_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Heating Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_water_outlet_node_name`')
        self._data["Heating Water Outlet Node Name"] = value

    @property
    def heating_control_throttling_range(self):
        """Get heating_control_throttling_range

        Returns:
            float: the value of `heating_control_throttling_range` or None if not set
        """
        return self._data["Heating Control Throttling Range"]

    @heating_control_throttling_range.setter
    def heating_control_throttling_range(self, value=0.5):
        """  Corresponds to IDD Field `Heating Control Throttling Range`

        Args:
            value (float): value for IDD Field `Heating Control Throttling Range`
                Units: deltaC
                Default value: 0.5
                value >= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_control_throttling_range`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_control_throttling_range`')
        self._data["Heating Control Throttling Range"] = value

    @property
    def heating_control_temperature_schedule_name(self):
        """Get heating_control_temperature_schedule_name

        Returns:
            str: the value of `heating_control_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Control Temperature Schedule Name"]

    @heating_control_temperature_schedule_name.setter
    def heating_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.heating_control_temperature_schedule_name`')
        self._data["Heating Control Temperature Schedule Name"] = value

    @property
    def cooling_design_capacity_method(self):
        """Get cooling_design_capacity_method

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set
        """
        return self._data["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="CoolingDesignCapacity"):
        """  Corresponds to IDD Field `Cooling Design Capacity Method`
        Enter the method used to determine the cooling design capacity for scalable sizing.
        CoolingDesignCapacity => selected when the design cooling capacity value is specified or
        auto-sized. CapacityPerFloorArea => selected when the design cooling capacity is determined
        from user specified cooling capacity per floor area and total floor area of cooled zone
        served by the hydrolic unit. FractionOfAutosizedCoolingCapacity => is selected when the
        design cooling capacity is determined from a user specified fraction and the auto-sized
        design cooling capacity of the system.

        Args:
            value (str): value for IDD Field `Cooling Design Capacity Method`
                Accepted values are:
                      - None
                      - CoolingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedCoolingCapacity
                Default value: CoolingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_method`')
            vals = {}
            vals["none"] = "None"
            vals["coolingdesigncapacity"] = "CoolingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedcoolingcapacity"] = "FractionOfAutosizedCoolingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """Get cooling_design_capacity

        Returns:
            float: the value of `cooling_design_capacity` or None if not set
        """
        return self._data["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `Cooling Design Capacity`
        Enter the design cooling capacity. Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Cooling Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity`'.format(value))
                    self._data["Cooling Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity`')
        self._data["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """Get cooling_design_capacity_per_floor_area

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Cooling Design Capacity Per Floor Area`
        Enter the cooling design capacity per total floor area of cooled zones served by the unit.
        Required field when the cooling design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_design_capacity_per_floor_area`')
        self._data["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """Get fraction_of_autosized_cooling_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `Fraction of Autosized Cooling Design Capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Capacity`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.fraction_of_autosized_cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.fraction_of_autosized_cooling_design_capacity`')
        self._data["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def maximum_cold_water_flow(self):
        """Get maximum_cold_water_flow

        Returns:
            float: the value of `maximum_cold_water_flow` or None if not set
        """
        return self._data["Maximum Cold Water Flow"]

    @maximum_cold_water_flow.setter
    def maximum_cold_water_flow(self, value=None):
        """  Corresponds to IDD Field `Maximum Cold Water Flow`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cold Water Flow`
                Units: m3/s
                IP-Units: gal/min
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Cold Water Flow"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.maximum_cold_water_flow`'.format(value))
                    self._data["Maximum Cold Water Flow"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.maximum_cold_water_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.maximum_cold_water_flow`')
        self._data["Maximum Cold Water Flow"] = value

    @property
    def cooling_water_inlet_node_name(self):
        """Get cooling_water_inlet_node_name

        Returns:
            str: the value of `cooling_water_inlet_node_name` or None if not set
        """
        return self._data["Cooling Water Inlet Node Name"]

    @cooling_water_inlet_node_name.setter
    def cooling_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_water_inlet_node_name`')
        self._data["Cooling Water Inlet Node Name"] = value

    @property
    def cooling_water_outlet_node_name(self):
        """Get cooling_water_outlet_node_name

        Returns:
            str: the value of `cooling_water_outlet_node_name` or None if not set
        """
        return self._data["Cooling Water Outlet Node Name"]

    @cooling_water_outlet_node_name.setter
    def cooling_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_water_outlet_node_name`')
        self._data["Cooling Water Outlet Node Name"] = value

    @property
    def cooling_control_throttling_range(self):
        """Get cooling_control_throttling_range

        Returns:
            float: the value of `cooling_control_throttling_range` or None if not set
        """
        return self._data["Cooling Control Throttling Range"]

    @cooling_control_throttling_range.setter
    def cooling_control_throttling_range(self, value=0.5):
        """  Corresponds to IDD Field `Cooling Control Throttling Range`

        Args:
            value (float): value for IDD Field `Cooling Control Throttling Range`
                Units: deltaC
                Default value: 0.5
                value >= 0.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_control_throttling_range`'.format(value))
            if value < 0.5:
                raise ValueError('value need to be greater or equal 0.5 '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_control_throttling_range`')
        self._data["Cooling Control Throttling Range"] = value

    @property
    def cooling_control_temperature_schedule_name(self):
        """Get cooling_control_temperature_schedule_name

        Returns:
            str: the value of `cooling_control_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Control Temperature Schedule Name"]

    @cooling_control_temperature_schedule_name.setter
    def cooling_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.cooling_control_temperature_schedule_name`')
        self._data["Cooling Control Temperature Schedule Name"] = value

    @property
    def condensation_control_type(self):
        """Get condensation_control_type

        Returns:
            str: the value of `condensation_control_type` or None if not set
        """
        return self._data["Condensation Control Type"]

    @condensation_control_type.setter
    def condensation_control_type(self, value="SimpleOff"):
        """  Corresponds to IDD Field `Condensation Control Type`

        Args:
            value (str): value for IDD Field `Condensation Control Type`
                Accepted values are:
                      - Off
                      - SimpleOff
                      - VariableOff
                Default value: SimpleOff
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.condensation_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.condensation_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.condensation_control_type`')
            vals = {}
            vals["off"] = "Off"
            vals["simpleoff"] = "SimpleOff"
            vals["variableoff"] = "VariableOff"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantVariableFlow.condensation_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantVariableFlow.condensation_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Condensation Control Type"] = value

    @property
    def condensation_control_dewpoint_offset(self):
        """Get condensation_control_dewpoint_offset

        Returns:
            float: the value of `condensation_control_dewpoint_offset` or None if not set
        """
        return self._data["Condensation Control Dewpoint Offset"]

    @condensation_control_dewpoint_offset.setter
    def condensation_control_dewpoint_offset(self, value=1.0):
        """  Corresponds to IDD Field `Condensation Control Dewpoint Offset`

        Args:
            value (float): value for IDD Field `Condensation Control Dewpoint Offset`
                Units: C
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.condensation_control_dewpoint_offset`'.format(value))
        self._data["Condensation Control Dewpoint Offset"] = value

    @property
    def number_of_circuits(self):
        """Get number_of_circuits

        Returns:
            str: the value of `number_of_circuits` or None if not set
        """
        return self._data["Number of Circuits"]

    @number_of_circuits.setter
    def number_of_circuits(self, value="OnePerSurface"):
        """  Corresponds to IDD Field `Number of Circuits`

        Args:
            value (str): value for IDD Field `Number of Circuits`
                Accepted values are:
                      - OnePerSurface
                      - CalculateFromCircuitLength
                Default value: OnePerSurface
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.number_of_circuits`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.number_of_circuits`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantVariableFlow.number_of_circuits`')
            vals = {}
            vals["onepersurface"] = "OnePerSurface"
            vals["calculatefromcircuitlength"] = "CalculateFromCircuitLength"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantVariableFlow.number_of_circuits`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantVariableFlow.number_of_circuits`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Number of Circuits"] = value

    @property
    def circuit_length(self):
        """Get circuit_length

        Returns:
            float: the value of `circuit_length` or None if not set
        """
        return self._data["Circuit Length"]

    @circuit_length.setter
    def circuit_length(self, value=106.7):
        """  Corresponds to IDD Field `Circuit Length`

        Args:
            value (float): value for IDD Field `Circuit Length`
                Units: m
                Default value: 106.7
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantVariableFlow.circuit_length`'.format(value))
        self._data["Circuit Length"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacLowTemperatureRadiantVariableFlow:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacLowTemperatureRadiantVariableFlow:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacLowTemperatureRadiantVariableFlow: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacLowTemperatureRadiantVariableFlow: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacLowTemperatureRadiantConstantFlow(object):
    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:ConstantFlow`
        Low temperature hydronic radiant heating and/or cooling system embedded in a building
        surface (wall, ceiling, or floor). Controlled by varying the hot or chilled water
        temperature circulating through the unit.
    """
    internal_name = "ZoneHVAC:LowTemperatureRadiant:ConstantFlow"
    field_count = 29
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 29
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:LowTemperatureRadiant:ConstantFlow`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Surface Name or Radiant Surface Group Name"] = None
        self._data["Hydronic Tubing Inside Diameter"] = None
        self._data["Hydronic Tubing Length"] = None
        self._data["Temperature Control Type"] = None
        self._data["Rated Flow Rate"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Rated Pump Head"] = None
        self._data["Rated Power Consumption"] = None
        self._data["Motor Efficiency"] = None
        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = None
        self._data["Heating Water Inlet Node Name"] = None
        self._data["Heating Water Outlet Node Name"] = None
        self._data["Heating High Water Temperature Schedule Name"] = None
        self._data["Heating Low Water Temperature Schedule Name"] = None
        self._data["Heating High Control Temperature Schedule Name"] = None
        self._data["Heating Low Control Temperature Schedule Name"] = None
        self._data["Cooling Water Inlet Node Name"] = None
        self._data["Cooling Water Outlet Node Name"] = None
        self._data["Cooling High Water Temperature Schedule Name"] = None
        self._data["Cooling Low Water Temperature Schedule Name"] = None
        self._data["Cooling High Control Temperature Schedule Name"] = None
        self._data["Cooling Low Control Temperature Schedule Name"] = None
        self._data["Condensation Control Type"] = None
        self._data["Condensation Control Dewpoint Offset"] = None
        self._data["Number of Circuits"] = None
        self._data["Circuit Length"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_or_radiant_surface_group_name = None
        else:
            self.surface_name_or_radiant_surface_group_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_inside_diameter = None
        else:
            self.hydronic_tubing_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hydronic_tubing_length = None
        else:
            self.hydronic_tubing_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_control_type = None
        else:
            self.temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_flow_rate = None
        else:
            self.rated_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_pump_head = None
        else:
            self.rated_pump_head = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.motor_efficiency = None
        else:
            self.motor_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = None
        else:
            self.fraction_of_motor_inefficiencies_to_fluid_stream = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_water_inlet_node_name = None
        else:
            self.heating_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_water_outlet_node_name = None
        else:
            self.heating_water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_high_water_temperature_schedule_name = None
        else:
            self.heating_high_water_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_low_water_temperature_schedule_name = None
        else:
            self.heating_low_water_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_high_control_temperature_schedule_name = None
        else:
            self.heating_high_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_low_control_temperature_schedule_name = None
        else:
            self.heating_low_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_water_inlet_node_name = None
        else:
            self.cooling_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_water_outlet_node_name = None
        else:
            self.cooling_water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_high_water_temperature_schedule_name = None
        else:
            self.cooling_high_water_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_low_water_temperature_schedule_name = None
        else:
            self.cooling_low_water_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_high_control_temperature_schedule_name = None
        else:
            self.cooling_high_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_low_control_temperature_schedule_name = None
        else:
            self.cooling_low_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensation_control_type = None
        else:
            self.condensation_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condensation_control_dewpoint_offset = None
        else:
            self.condensation_control_dewpoint_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_circuits = None
        else:
            self.number_of_circuits = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circuit_length = None
        else:
            self.circuit_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of zone system is serving

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.zone_name`')
        self._data["Zone Name"] = value

    @property
    def surface_name_or_radiant_surface_group_name(self):
        """Get surface_name_or_radiant_surface_group_name

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set
        """
        return self._data["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name or Radiant Surface Group Name`
        Identifies surfaces that radiant system is embedded in.
        For a system with multiple surfaces, enter the name of
        a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.surface_name_or_radiant_surface_group_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.surface_name_or_radiant_surface_group_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.surface_name_or_radiant_surface_group_name`')
        self._data["Surface Name or Radiant Surface Group Name"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """Get hydronic_tubing_inside_diameter

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=0.013):
        """  Corresponds to IDD Field `Hydronic Tubing Inside Diameter`

        Args:
            value (float): value for IDD Field `Hydronic Tubing Inside Diameter`
                Units: m
                Default value: 0.013
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.hydronic_tubing_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.hydronic_tubing_inside_diameter`')
        self._data["Hydronic Tubing Inside Diameter"] = value

    @property
    def hydronic_tubing_length(self):
        """Get hydronic_tubing_length

        Returns:
            float: the value of `hydronic_tubing_length` or None if not set
        """
        return self._data["Hydronic Tubing Length"]

    @hydronic_tubing_length.setter
    def hydronic_tubing_length(self, value=None):
        """  Corresponds to IDD Field `Hydronic Tubing Length`
        Total length of pipe embedded in surface

        Args:
            value (float): value for IDD Field `Hydronic Tubing Length`
                Units: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.hydronic_tubing_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.hydronic_tubing_length`')
        self._data["Hydronic Tubing Length"] = value

    @property
    def temperature_control_type(self):
        """Get temperature_control_type

        Returns:
            str: the value of `temperature_control_type` or None if not set
        """
        return self._data["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="MeanAirTemperature"):
        """  Corresponds to IDD Field `Temperature Control Type`
        Temperature used to control system

        Args:
            value (str): value for IDD Field `Temperature Control Type`
                Accepted values are:
                      - MeanAirTemperature
                      - MeanRadiantTemperature
                      - OperativeTemperature
                      - OutdoorDryBulbTemperature
                      - OutdoorWetBulbTemperature
                Default value: MeanAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.temperature_control_type`')
            vals = {}
            vals["meanairtemperature"] = "MeanAirTemperature"
            vals["meanradianttemperature"] = "MeanRadiantTemperature"
            vals["operativetemperature"] = "OperativeTemperature"
            vals["outdoordrybulbtemperature"] = "OutdoorDryBulbTemperature"
            vals["outdoorwetbulbtemperature"] = "OutdoorWetBulbTemperature"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantConstantFlow.temperature_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantConstantFlow.temperature_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Temperature Control Type"] = value

    @property
    def rated_flow_rate(self):
        """Get rated_flow_rate

        Returns:
            float: the value of `rated_flow_rate` or None if not set
        """
        return self._data["Rated Flow Rate"]

    @rated_flow_rate.setter
    def rated_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Rated Flow Rate`

        Args:
            value (float): value for IDD Field `Rated Flow Rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.rated_flow_rate`'.format(value))
        self._data["Rated Flow Rate"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Pump Flow Rate Schedule Name`
        Modifies the Rated Flow Rate of the pump on a time basis
        the default is that the pump is ON and runs according to its other
        operational requirements specified above.  The schedule is for special
        pump operations. Values here are between 0 and 1 and are multipliers
        on the previous field (Rated Flow Rate).

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.pump_flow_rate_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.pump_flow_rate_schedule_name`')
        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def rated_pump_head(self):
        """Get rated_pump_head

        Returns:
            float: the value of `rated_pump_head` or None if not set
        """
        return self._data["Rated Pump Head"]

    @rated_pump_head.setter
    def rated_pump_head(self, value=179352.0):
        """  Corresponds to IDD Field `Rated Pump Head`
        default head is 60 feet

        Args:
            value (float): value for IDD Field `Rated Pump Head`
                Units: Pa
                Default value: 179352.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.rated_pump_head`'.format(value))
        self._data["Rated Pump Head"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `Rated Power Consumption`

        Args:
            value (float): value for IDD Field `Rated Power Consumption`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.rated_power_consumption`'.format(value))
        self._data["Rated Power Consumption"] = value

    @property
    def motor_efficiency(self):
        """Get motor_efficiency

        Returns:
            float: the value of `motor_efficiency` or None if not set
        """
        return self._data["Motor Efficiency"]

    @motor_efficiency.setter
    def motor_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Motor Efficiency`

        Args:
            value (float): value for IDD Field `Motor Efficiency`
                Default value: 0.9
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.motor_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.motor_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.motor_efficiency`')
        self._data["Motor Efficiency"] = value

    @property
    def fraction_of_motor_inefficiencies_to_fluid_stream(self):
        """Get fraction_of_motor_inefficiencies_to_fluid_stream

        Returns:
            float: the value of `fraction_of_motor_inefficiencies_to_fluid_stream` or None if not set
        """
        return self._data["Fraction of Motor Inefficiencies to Fluid Stream"]

    @fraction_of_motor_inefficiencies_to_fluid_stream.setter
    def fraction_of_motor_inefficiencies_to_fluid_stream(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`

        Args:
            value (float): value for IDD Field `Fraction of Motor Inefficiencies to Fluid Stream`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.fraction_of_motor_inefficiencies_to_fluid_stream`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.fraction_of_motor_inefficiencies_to_fluid_stream`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.fraction_of_motor_inefficiencies_to_fluid_stream`')
        self._data["Fraction of Motor Inefficiencies to Fluid Stream"] = value

    @property
    def heating_water_inlet_node_name(self):
        """Get heating_water_inlet_node_name

        Returns:
            str: the value of `heating_water_inlet_node_name` or None if not set
        """
        return self._data["Heating Water Inlet Node Name"]

    @heating_water_inlet_node_name.setter
    def heating_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Heating Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_water_inlet_node_name`')
        self._data["Heating Water Inlet Node Name"] = value

    @property
    def heating_water_outlet_node_name(self):
        """Get heating_water_outlet_node_name

        Returns:
            str: the value of `heating_water_outlet_node_name` or None if not set
        """
        return self._data["Heating Water Outlet Node Name"]

    @heating_water_outlet_node_name.setter
    def heating_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Heating Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Heating Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_water_outlet_node_name`')
        self._data["Heating Water Outlet Node Name"] = value

    @property
    def heating_high_water_temperature_schedule_name(self):
        """Get heating_high_water_temperature_schedule_name

        Returns:
            str: the value of `heating_high_water_temperature_schedule_name` or None if not set
        """
        return self._data["Heating High Water Temperature Schedule Name"]

    @heating_high_water_temperature_schedule_name.setter
    def heating_high_water_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating High Water Temperature Schedule Name`
        Water and control temperatures for heating work together to provide
        a linear function that determines the water temperature sent to the
        radiant system.  The current control temperature (see Temperature Control Type above) is
        compared to the high and low control temperatures at the current time.
        If the control temperature is above the high temperature, then the
        inlet water temperature is set to the low water temperature.  If the
        control temperature is below the low temperature, then the inlet
        water temperature is set to the high water temperature.  If the control
        temperature is between the high and low value, then the inlet water
        temperature is linearly interpolated between the low and high water
        temperature values.

        Args:
            value (str): value for IDD Field `Heating High Water Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_high_water_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_high_water_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_high_water_temperature_schedule_name`')
        self._data["Heating High Water Temperature Schedule Name"] = value

    @property
    def heating_low_water_temperature_schedule_name(self):
        """Get heating_low_water_temperature_schedule_name

        Returns:
            str: the value of `heating_low_water_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Low Water Temperature Schedule Name"]

    @heating_low_water_temperature_schedule_name.setter
    def heating_low_water_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Low Water Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Water Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_low_water_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_low_water_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_low_water_temperature_schedule_name`')
        self._data["Heating Low Water Temperature Schedule Name"] = value

    @property
    def heating_high_control_temperature_schedule_name(self):
        """Get heating_high_control_temperature_schedule_name

        Returns:
            str: the value of `heating_high_control_temperature_schedule_name` or None if not set
        """
        return self._data["Heating High Control Temperature Schedule Name"]

    @heating_high_control_temperature_schedule_name.setter
    def heating_high_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating High Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_high_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_high_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_high_control_temperature_schedule_name`')
        self._data["Heating High Control Temperature Schedule Name"] = value

    @property
    def heating_low_control_temperature_schedule_name(self):
        """Get heating_low_control_temperature_schedule_name

        Returns:
            str: the value of `heating_low_control_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Low Control Temperature Schedule Name"]

    @heating_low_control_temperature_schedule_name.setter
    def heating_low_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_low_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_low_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.heating_low_control_temperature_schedule_name`')
        self._data["Heating Low Control Temperature Schedule Name"] = value

    @property
    def cooling_water_inlet_node_name(self):
        """Get cooling_water_inlet_node_name

        Returns:
            str: the value of `cooling_water_inlet_node_name` or None if not set
        """
        return self._data["Cooling Water Inlet Node Name"]

    @cooling_water_inlet_node_name.setter
    def cooling_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_water_inlet_node_name`')
        self._data["Cooling Water Inlet Node Name"] = value

    @property
    def cooling_water_outlet_node_name(self):
        """Get cooling_water_outlet_node_name

        Returns:
            str: the value of `cooling_water_outlet_node_name` or None if not set
        """
        return self._data["Cooling Water Outlet Node Name"]

    @cooling_water_outlet_node_name.setter
    def cooling_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Cooling Water Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_water_outlet_node_name`')
        self._data["Cooling Water Outlet Node Name"] = value

    @property
    def cooling_high_water_temperature_schedule_name(self):
        """Get cooling_high_water_temperature_schedule_name

        Returns:
            str: the value of `cooling_high_water_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling High Water Temperature Schedule Name"]

    @cooling_high_water_temperature_schedule_name.setter
    def cooling_high_water_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling High Water Temperature Schedule Name`
        See note for Heating High Water Temperature Schedule above for
        interpretation information (or see the Input/Output Reference).

        Args:
            value (str): value for IDD Field `Cooling High Water Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_high_water_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_high_water_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_high_water_temperature_schedule_name`')
        self._data["Cooling High Water Temperature Schedule Name"] = value

    @property
    def cooling_low_water_temperature_schedule_name(self):
        """Get cooling_low_water_temperature_schedule_name

        Returns:
            str: the value of `cooling_low_water_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Low Water Temperature Schedule Name"]

    @cooling_low_water_temperature_schedule_name.setter
    def cooling_low_water_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Low Water Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Water Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_low_water_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_low_water_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_low_water_temperature_schedule_name`')
        self._data["Cooling Low Water Temperature Schedule Name"] = value

    @property
    def cooling_high_control_temperature_schedule_name(self):
        """Get cooling_high_control_temperature_schedule_name

        Returns:
            str: the value of `cooling_high_control_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling High Control Temperature Schedule Name"]

    @cooling_high_control_temperature_schedule_name.setter
    def cooling_high_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling High Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_high_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_high_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_high_control_temperature_schedule_name`')
        self._data["Cooling High Control Temperature Schedule Name"] = value

    @property
    def cooling_low_control_temperature_schedule_name(self):
        """Get cooling_low_control_temperature_schedule_name

        Returns:
            str: the value of `cooling_low_control_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Low Control Temperature Schedule Name"]

    @cooling_low_control_temperature_schedule_name.setter
    def cooling_low_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_low_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_low_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.cooling_low_control_temperature_schedule_name`')
        self._data["Cooling Low Control Temperature Schedule Name"] = value

    @property
    def condensation_control_type(self):
        """Get condensation_control_type

        Returns:
            str: the value of `condensation_control_type` or None if not set
        """
        return self._data["Condensation Control Type"]

    @condensation_control_type.setter
    def condensation_control_type(self, value="SimpleOff"):
        """  Corresponds to IDD Field `Condensation Control Type`

        Args:
            value (str): value for IDD Field `Condensation Control Type`
                Accepted values are:
                      - Off
                      - SimpleOff
                      - VariableOff
                Default value: SimpleOff
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.condensation_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.condensation_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.condensation_control_type`')
            vals = {}
            vals["off"] = "Off"
            vals["simpleoff"] = "SimpleOff"
            vals["variableoff"] = "VariableOff"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantConstantFlow.condensation_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantConstantFlow.condensation_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Condensation Control Type"] = value

    @property
    def condensation_control_dewpoint_offset(self):
        """Get condensation_control_dewpoint_offset

        Returns:
            float: the value of `condensation_control_dewpoint_offset` or None if not set
        """
        return self._data["Condensation Control Dewpoint Offset"]

    @condensation_control_dewpoint_offset.setter
    def condensation_control_dewpoint_offset(self, value=1.0):
        """  Corresponds to IDD Field `Condensation Control Dewpoint Offset`

        Args:
            value (float): value for IDD Field `Condensation Control Dewpoint Offset`
                Units: C
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.condensation_control_dewpoint_offset`'.format(value))
        self._data["Condensation Control Dewpoint Offset"] = value

    @property
    def number_of_circuits(self):
        """Get number_of_circuits

        Returns:
            str: the value of `number_of_circuits` or None if not set
        """
        return self._data["Number of Circuits"]

    @number_of_circuits.setter
    def number_of_circuits(self, value="OnePerSurface"):
        """  Corresponds to IDD Field `Number of Circuits`

        Args:
            value (str): value for IDD Field `Number of Circuits`
                Accepted values are:
                      - OnePerSurface
                      - CalculateFromCircuitLength
                Default value: OnePerSurface
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.number_of_circuits`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.number_of_circuits`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantConstantFlow.number_of_circuits`')
            vals = {}
            vals["onepersurface"] = "OnePerSurface"
            vals["calculatefromcircuitlength"] = "CalculateFromCircuitLength"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantConstantFlow.number_of_circuits`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantConstantFlow.number_of_circuits`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Number of Circuits"] = value

    @property
    def circuit_length(self):
        """Get circuit_length

        Returns:
            float: the value of `circuit_length` or None if not set
        """
        return self._data["Circuit Length"]

    @circuit_length.setter
    def circuit_length(self, value=106.7):
        """  Corresponds to IDD Field `Circuit Length`

        Args:
            value (float): value for IDD Field `Circuit Length`
                Units: m
                Default value: 106.7
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantConstantFlow.circuit_length`'.format(value))
        self._data["Circuit Length"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacLowTemperatureRadiantConstantFlow:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacLowTemperatureRadiantConstantFlow:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacLowTemperatureRadiantConstantFlow: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacLowTemperatureRadiantConstantFlow: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacLowTemperatureRadiantElectric(object):
    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:Electric`
        Electric resistance low temperature radiant system
    """
    internal_name = "ZoneHVAC:LowTemperatureRadiant:Electric"
    field_count = 11
    required_fields = ["Name", "Heating Design Capacity Method"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:LowTemperatureRadiant:Electric`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Surface Name or Radiant Surface Group Name"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Temperature Control Type"] = None
        self._data["Heating Throttling Range"] = None
        self._data["Heating Setpoint Temperature Schedule Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_or_radiant_surface_group_name = None
        else:
            self.surface_name_or_radiant_surface_group_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_control_type = None
        else:
            self.temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_throttling_range = None
        else:
            self.heating_throttling_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_setpoint_temperature_schedule_name = None
        else:
            self.heating_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of zone system is serving

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.zone_name`')
        self._data["Zone Name"] = value

    @property
    def surface_name_or_radiant_surface_group_name(self):
        """Get surface_name_or_radiant_surface_group_name

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set
        """
        return self._data["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name or Radiant Surface Group Name`
        Identifies surfaces that radiant system is embedded in.
        For a system with multiple surfaces, enter the name of
        a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.surface_name_or_radiant_surface_group_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.surface_name_or_radiant_surface_group_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.surface_name_or_radiant_surface_group_name`')
        self._data["Surface Name or Radiant Surface Group Name"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the maximum electrical heating design capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                IP-Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def temperature_control_type(self):
        """Get temperature_control_type

        Returns:
            str: the value of `temperature_control_type` or None if not set
        """
        return self._data["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="MeanAirTemperature"):
        """  Corresponds to IDD Field `Temperature Control Type`
        Temperature used to control unit

        Args:
            value (str): value for IDD Field `Temperature Control Type`
                Accepted values are:
                      - MeanAirTemperature
                      - MeanRadiantTemperature
                      - OperativeTemperature
                      - OutdoorDryBulbTemperature
                      - OutdoorWetBulbTemperature
                Default value: MeanAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.temperature_control_type`')
            vals = {}
            vals["meanairtemperature"] = "MeanAirTemperature"
            vals["meanradianttemperature"] = "MeanRadiantTemperature"
            vals["operativetemperature"] = "OperativeTemperature"
            vals["outdoordrybulbtemperature"] = "OutdoorDryBulbTemperature"
            vals["outdoorwetbulbtemperature"] = "OutdoorWetBulbTemperature"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacLowTemperatureRadiantElectric.temperature_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacLowTemperatureRadiantElectric.temperature_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Temperature Control Type"] = value

    @property
    def heating_throttling_range(self):
        """Get heating_throttling_range

        Returns:
            float: the value of `heating_throttling_range` or None if not set
        """
        return self._data["Heating Throttling Range"]

    @heating_throttling_range.setter
    def heating_throttling_range(self, value=0.0):
        """  Corresponds to IDD Field `Heating Throttling Range`

        Args:
            value (float): value for IDD Field `Heating Throttling Range`
                Units: deltaC
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.heating_throttling_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_throttling_range`')
        self._data["Heating Throttling Range"] = value

    @property
    def heating_setpoint_temperature_schedule_name(self):
        """Get heating_setpoint_temperature_schedule_name

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Setpoint Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantElectric.heating_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantElectric.heating_setpoint_temperature_schedule_name`')
        self._data["Heating Setpoint Temperature Schedule Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacLowTemperatureRadiantElectric:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacLowTemperatureRadiantElectric:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacLowTemperatureRadiantElectric: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacLowTemperatureRadiantElectric: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacLowTemperatureRadiantSurfaceGroup(object):
    """ Corresponds to IDD object `ZoneHVAC:LowTemperatureRadiant:SurfaceGroup`
        This is used to allow the coordinate control of several radiant system surfaces.
        Note that the following flow fractions must sum up to 1.0
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    internal_name = "ZoneHVAC:LowTemperatureRadiant:SurfaceGroup"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Surface 1 Name", "Flow Fraction for Surface 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:LowTemperatureRadiant:SurfaceGroup`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       flow_fraction_for_surface_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            flow_fraction_for_surface_1 (float): value for IDD Field `Flow Fraction for Surface 1`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
        vals.append(self._check_flow_fraction_for_surface_1(flow_fraction_for_surface_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.surface_1_name`')
        return value

    def _check_flow_fraction_for_surface_1(self, value):
        """ Validates falue of field `Flow Fraction for Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.flow_fraction_for_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacLowTemperatureRadiantSurfaceGroup.flow_fraction_for_surface_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacLowTemperatureRadiantSurfaceGroup:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacLowTemperatureRadiantSurfaceGroup:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacLowTemperatureRadiantSurfaceGroup: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacLowTemperatureRadiantSurfaceGroup: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacHighTemperatureRadiant(object):
    """ Corresponds to IDD object `ZoneHVAC:HighTemperatureRadiant`
        The number of surfaces can be expanded beyond 100, if necessary, by adding more
        groups to the end of the list
    """
    internal_name = "ZoneHVAC:HighTemperatureRadiant"
    field_count = 16
    required_fields = ["Name", "Zone Name", "Heating Design Capacity Method", "Fuel Type", "Combustion Efficiency", "Fraction of Input Converted to Radiant Energy", "Fraction of Input Converted to Latent Energy", "Fraction of Input that Is Lost", "Heating Throttling Range"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Surface 1 Name", "Fraction of Radiant Energy to Surface 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:HighTemperatureRadiant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self._data["Fuel Type"] = None
        self._data["Combustion Efficiency"] = None
        self._data["Fraction of Input Converted to Radiant Energy"] = None
        self._data["Fraction of Input Converted to Latent Energy"] = None
        self._data["Fraction of Input that Is Lost"] = None
        self._data["Temperature Control Type"] = None
        self._data["Heating Throttling Range"] = None
        self._data["Heating Setpoint Temperature Schedule Name"] = None
        self._data["Fraction of Radiant Energy Incident on People"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.combustion_efficiency = None
        else:
            self.combustion_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_input_converted_to_radiant_energy = None
        else:
            self.fraction_of_input_converted_to_radiant_energy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_input_converted_to_latent_energy = None
        else:
            self.fraction_of_input_converted_to_latent_energy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_input_that_is_lost = None
        else:
            self.fraction_of_input_that_is_lost = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_control_type = None
        else:
            self.temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_throttling_range = None
        else:
            self.heating_throttling_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_setpoint_temperature_schedule_name = None
        else:
            self.heating_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_radiant_energy_incident_on_people = None
        else:
            self.fraction_of_radiant_energy_incident_on_people = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of zone system is serving

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.zone_name`')
        self._data["Zone Name"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the maximum heating power input capacity.
        HeatingDesignCapacity = > selected when the design heating capacity value or autosize
        is specified. CapacityPerFloorArea = > selected when the design heating capacity is
        determine from user specified heating capacity per floor area and zone floor area.
        FractionOfAutosizedHeatingCapacity = > is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity.

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
                Accepted values are:
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_method`')
            vals = {}
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity.Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity`'.format(value))
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity`')
        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area.Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_design_capacity_per_floor_area`')
        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto - sized heating design capacity.Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                Default value: 1.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_autosized_heating_design_capacity`')
        self._data["Fraction of Autosized Heating Design Capacity"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """  Corresponds to IDD Field `Fuel Type`
        Natural gas or electricity

        Args:
            value (str): value for IDD Field `Fuel Type`
                Accepted values are:
                      - NaturalGas
                      - Electricity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.fuel_type`')
            vals = {}
            vals["naturalgas"] = "NaturalGas"
            vals["electricity"] = "Electricity"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacHighTemperatureRadiant.fuel_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacHighTemperatureRadiant.fuel_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fuel Type"] = value

    @property
    def combustion_efficiency(self):
        """Get combustion_efficiency

        Returns:
            float: the value of `combustion_efficiency` or None if not set
        """
        return self._data["Combustion Efficiency"]

    @combustion_efficiency.setter
    def combustion_efficiency(self, value=0.9):
        """  Corresponds to IDD Field `Combustion Efficiency`
        Not used for non-gas radiant heaters

        Args:
            value (float): value for IDD Field `Combustion Efficiency`
                Default value: 0.9
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.combustion_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.combustion_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.combustion_efficiency`')
        self._data["Combustion Efficiency"] = value

    @property
    def fraction_of_input_converted_to_radiant_energy(self):
        """Get fraction_of_input_converted_to_radiant_energy

        Returns:
            float: the value of `fraction_of_input_converted_to_radiant_energy` or None if not set
        """
        return self._data["Fraction of Input Converted to Radiant Energy"]

    @fraction_of_input_converted_to_radiant_energy.setter
    def fraction_of_input_converted_to_radiant_energy(self, value=0.7):
        """  Corresponds to IDD Field `Fraction of Input Converted to Radiant Energy`
        Radiant+latent+lost fractions must sum to 1 or less, remainder is considered convective heat

        Args:
            value (float): value for IDD Field `Fraction of Input Converted to Radiant Energy`
                Default value: 0.7
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_converted_to_radiant_energy`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_converted_to_radiant_energy`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_converted_to_radiant_energy`')
        self._data["Fraction of Input Converted to Radiant Energy"] = value

    @property
    def fraction_of_input_converted_to_latent_energy(self):
        """Get fraction_of_input_converted_to_latent_energy

        Returns:
            float: the value of `fraction_of_input_converted_to_latent_energy` or None if not set
        """
        return self._data["Fraction of Input Converted to Latent Energy"]

    @fraction_of_input_converted_to_latent_energy.setter
    def fraction_of_input_converted_to_latent_energy(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Input Converted to Latent Energy`

        Args:
            value (float): value for IDD Field `Fraction of Input Converted to Latent Energy`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_converted_to_latent_energy`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_converted_to_latent_energy`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_converted_to_latent_energy`')
        self._data["Fraction of Input Converted to Latent Energy"] = value

    @property
    def fraction_of_input_that_is_lost(self):
        """Get fraction_of_input_that_is_lost

        Returns:
            float: the value of `fraction_of_input_that_is_lost` or None if not set
        """
        return self._data["Fraction of Input that Is Lost"]

    @fraction_of_input_that_is_lost.setter
    def fraction_of_input_that_is_lost(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Input that Is Lost`
        Fraction of input vented to outdoor environment

        Args:
            value (float): value for IDD Field `Fraction of Input that Is Lost`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_that_is_lost`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_that_is_lost`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_input_that_is_lost`')
        self._data["Fraction of Input that Is Lost"] = value

    @property
    def temperature_control_type(self):
        """Get temperature_control_type

        Returns:
            str: the value of `temperature_control_type` or None if not set
        """
        return self._data["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="OperativeTemperature"):
        """  Corresponds to IDD Field `Temperature Control Type`
        Temperature type used to control unit

        Args:
            value (str): value for IDD Field `Temperature Control Type`
                Accepted values are:
                      - MeanAirTemperature
                      - MeanRadiantTemperature
                      - OperativeTemperature
                      - MeanAirTemperatureSetpoint
                      - MeanRadiantTemperatureSetpoint
                      - OperativeTemperatureSetpoint
                Default value: OperativeTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.temperature_control_type`')
            vals = {}
            vals["meanairtemperature"] = "MeanAirTemperature"
            vals["meanradianttemperature"] = "MeanRadiantTemperature"
            vals["operativetemperature"] = "OperativeTemperature"
            vals["meanairtemperaturesetpoint"] = "MeanAirTemperatureSetpoint"
            vals["meanradianttemperaturesetpoint"] = "MeanRadiantTemperatureSetpoint"
            vals["operativetemperaturesetpoint"] = "OperativeTemperatureSetpoint"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacHighTemperatureRadiant.temperature_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacHighTemperatureRadiant.temperature_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Temperature Control Type"] = value

    @property
    def heating_throttling_range(self):
        """Get heating_throttling_range

        Returns:
            float: the value of `heating_throttling_range` or None if not set
        """
        return self._data["Heating Throttling Range"]

    @heating_throttling_range.setter
    def heating_throttling_range(self, value=2.0):
        """  Corresponds to IDD Field `Heating Throttling Range`

        Args:
            value (float): value for IDD Field `Heating Throttling Range`
                Units: deltaC
                Default value: 2.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.heating_throttling_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_throttling_range`')
        self._data["Heating Throttling Range"] = value

    @property
    def heating_setpoint_temperature_schedule_name(self):
        """Get heating_setpoint_temperature_schedule_name

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Setpoint Temperature Schedule Name`
        This setpoint is an "operative temperature" setpoint

        Args:
            value (str): value for IDD Field `Heating Setpoint Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.heating_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.heating_setpoint_temperature_schedule_name`')
        self._data["Heating Setpoint Temperature Schedule Name"] = value

    @property
    def fraction_of_radiant_energy_incident_on_people(self):
        """Get fraction_of_radiant_energy_incident_on_people

        Returns:
            float: the value of `fraction_of_radiant_energy_incident_on_people` or None if not set
        """
        return self._data["Fraction of Radiant Energy Incident on People"]

    @fraction_of_radiant_energy_incident_on_people.setter
    def fraction_of_radiant_energy_incident_on_people(self, value=None):
        """  Corresponds to IDD Field `Fraction of Radiant Energy Incident on People`
        This will affect thermal comfort but from an energy balance standpoint this value
        gets added to the convective gains from the radiant heater

        Args:
            value (float): value for IDD Field `Fraction of Radiant Energy Incident on People`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fraction_of_radiant_energy_incident_on_people`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_radiant_energy_incident_on_people`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_radiant_energy_incident_on_people`')
        self._data["Fraction of Radiant Energy Incident on People"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       fraction_of_radiant_energy_to_surface_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            fraction_of_radiant_energy_to_surface_1 (float): value for IDD Field `Fraction of Radiant Energy to Surface 1`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
        vals.append(self._check_fraction_of_radiant_energy_to_surface_1(fraction_of_radiant_energy_to_surface_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacHighTemperatureRadiant.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacHighTemperatureRadiant.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacHighTemperatureRadiant.surface_1_name`')
        return value

    def _check_fraction_of_radiant_energy_to_surface_1(self, value):
        """ Validates falue of field `Fraction of Radiant Energy to Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacHighTemperatureRadiant.fraction_of_radiant_energy_to_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_radiant_energy_to_surface_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZoneHvacHighTemperatureRadiant.fraction_of_radiant_energy_to_surface_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacHighTemperatureRadiant:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacHighTemperatureRadiant:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacHighTemperatureRadiant: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacHighTemperatureRadiant: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacVentilatedSlab(object):
    """ Corresponds to IDD object `ZoneHVAC:VentilatedSlab`
        Ventilated slab system where outdoor air flows through hollow cores in a building
        surface (wall, ceiling, or floor).
    """
    internal_name = "ZoneHVAC:VentilatedSlab"
    field_count = 40
    required_fields = ["Name", "Zone Name", "Maximum Air Flow Rate", "Outdoor Air Control Type", "Minimum Outdoor Air Flow Rate", "Minimum Outdoor Air Schedule Name", "Maximum Outdoor Air Flow Rate", "Maximum Outdoor Air Fraction or Temperature Schedule Name", "System Configuration Type", "Temperature Control Type", "Heating High Air Temperature Schedule Name", "Heating Low Air Temperature Schedule Name", "Heating High Control Temperature Schedule Name", "Heating Low Control Temperature Schedule Name", "Cooling High Air Temperature Schedule Name", "Cooling Low Air Temperature Schedule Name", "Cooling High Control Temperature Schedule Name", "Cooling Low Control Temperature Schedule Name", "Return Air Node Name", "Slab In Node Name", "Outdoor Air Node Name", "Relief Air Node Name", "Outdoor Air Mixer Outlet Node Name", "Fan Outlet Node Name", "Fan Name", "Coil Option Type"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:VentilatedSlab`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Surface Name or Radiant Surface Group Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Outdoor Air Control Type"] = None
        self._data["Minimum Outdoor Air Flow Rate"] = None
        self._data["Minimum Outdoor Air Schedule Name"] = None
        self._data["Maximum Outdoor Air Flow Rate"] = None
        self._data["Maximum Outdoor Air Fraction or Temperature Schedule Name"] = None
        self._data["System Configuration Type"] = None
        self._data["Hollow Core Inside Diameter"] = None
        self._data["Hollow Core Length"] = None
        self._data["Number of Cores"] = None
        self._data["Temperature Control Type"] = None
        self._data["Heating High Air Temperature Schedule Name"] = None
        self._data["Heating Low Air Temperature Schedule Name"] = None
        self._data["Heating High Control Temperature Schedule Name"] = None
        self._data["Heating Low Control Temperature Schedule Name"] = None
        self._data["Cooling High Air Temperature Schedule Name"] = None
        self._data["Cooling Low Air Temperature Schedule Name"] = None
        self._data["Cooling High Control Temperature Schedule Name"] = None
        self._data["Cooling Low Control Temperature Schedule Name"] = None
        self._data["Return Air Node Name"] = None
        self._data["Slab In Node Name"] = None
        self._data["Zone Supply Air Node Name"] = None
        self._data["Outdoor Air Node Name"] = None
        self._data["Relief Air Node Name"] = None
        self._data["Outdoor Air Mixer Outlet Node Name"] = None
        self._data["Fan Outlet Node Name"] = None
        self._data["Fan Name"] = None
        self._data["Coil Option Type"] = None
        self._data["Heating Coil Object Type"] = None
        self._data["Heating Coil Name"] = None
        self._data["Hot Water or Steam Inlet Node Name"] = None
        self._data["Cooling Coil Object Type"] = None
        self._data["Cooling Coil Name"] = None
        self._data["Cold Water Inlet Node Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_or_radiant_surface_group_name = None
        else:
            self.surface_name_or_radiant_surface_group_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_control_type = None
        else:
            self.outdoor_air_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_flow_rate = None
        else:
            self.minimum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_air_schedule_name = None
        else:
            self.minimum_outdoor_air_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_flow_rate = None
        else:
            self.maximum_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_air_fraction_or_temperature_schedule_name = None
        else:
            self.maximum_outdoor_air_fraction_or_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.system_configuration_type = None
        else:
            self.system_configuration_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hollow_core_inside_diameter = None
        else:
            self.hollow_core_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hollow_core_length = None
        else:
            self.hollow_core_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cores = None
        else:
            self.number_of_cores = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_control_type = None
        else:
            self.temperature_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_high_air_temperature_schedule_name = None
        else:
            self.heating_high_air_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_low_air_temperature_schedule_name = None
        else:
            self.heating_low_air_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_high_control_temperature_schedule_name = None
        else:
            self.heating_high_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_low_control_temperature_schedule_name = None
        else:
            self.heating_low_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_high_air_temperature_schedule_name = None
        else:
            self.cooling_high_air_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_low_air_temperature_schedule_name = None
        else:
            self.cooling_low_air_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_high_control_temperature_schedule_name = None
        else:
            self.cooling_high_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_low_control_temperature_schedule_name = None
        else:
            self.cooling_low_control_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_node_name = None
        else:
            self.return_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slab_in_node_name = None
        else:
            self.slab_in_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_supply_air_node_name = None
        else:
            self.zone_supply_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_node_name = None
        else:
            self.outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relief_air_node_name = None
        else:
            self.relief_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_mixer_outlet_node_name = None
        else:
            self.outdoor_air_mixer_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_outlet_node_name = None
        else:
            self.fan_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fan_name = None
        else:
            self.fan_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coil_option_type = None
        else:
            self.coil_option_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_object_type = None
        else:
            self.heating_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_coil_name = None
        else:
            self.heating_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hot_water_or_steam_inlet_node_name = None
        else:
            self.hot_water_or_steam_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_object_type = None
        else:
            self.cooling_coil_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_coil_name = None
        else:
            self.cooling_coil_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cold_water_inlet_node_name = None
        else:
            self.cold_water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zonehvac_sizing_object_name = None
        else:
            self.design_specification_zonehvac_sizing_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.name`')
        self._data["Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        (name of zone system is serving)

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.zone_name`')
        self._data["Zone Name"] = value

    @property
    def surface_name_or_radiant_surface_group_name(self):
        """Get surface_name_or_radiant_surface_group_name

        Returns:
            str: the value of `surface_name_or_radiant_surface_group_name` or None if not set
        """
        return self._data["Surface Name or Radiant Surface Group Name"]

    @surface_name_or_radiant_surface_group_name.setter
    def surface_name_or_radiant_surface_group_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name or Radiant Surface Group Name`
        (name of surface system is embedded in) or list of surfaces

        Args:
            value (str): value for IDD Field `Surface Name or Radiant Surface Group Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.surface_name_or_radiant_surface_group_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.surface_name_or_radiant_surface_group_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.surface_name_or_radiant_surface_group_name`')
        self._data["Surface Name or Radiant Surface Group Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`
                Units: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacVentilatedSlab.maximum_air_flow_rate`'.format(value))
                    self._data["Maximum Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacVentilatedSlab.maximum_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneHvacVentilatedSlab.maximum_air_flow_rate`')
        self._data["Maximum Air Flow Rate"] = value

    @property
    def outdoor_air_control_type(self):
        """Get outdoor_air_control_type

        Returns:
            str: the value of `outdoor_air_control_type` or None if not set
        """
        return self._data["Outdoor Air Control Type"]

    @outdoor_air_control_type.setter
    def outdoor_air_control_type(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Control Type`

        Args:
            value (str): value for IDD Field `Outdoor Air Control Type`
                Accepted values are:
                      - VariablePercent
                      - FixedTemperature
                      - FixedAmount
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.outdoor_air_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.outdoor_air_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.outdoor_air_control_type`')
            vals = {}
            vals["variablepercent"] = "VariablePercent"
            vals["fixedtemperature"] = "FixedTemperature"
            vals["fixedamount"] = "FixedAmount"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacVentilatedSlab.outdoor_air_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacVentilatedSlab.outdoor_air_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Outdoor Air Control Type"] = value

    @property
    def minimum_outdoor_air_flow_rate(self):
        """Get minimum_outdoor_air_flow_rate

        Returns:
            float: the value of `minimum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Minimum Outdoor Air Flow Rate"]

    @minimum_outdoor_air_flow_rate.setter
    def minimum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Minimum Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Outdoor Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Minimum Outdoor Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacVentilatedSlab.minimum_outdoor_air_flow_rate`'.format(value))
                    self._data["Minimum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacVentilatedSlab.minimum_outdoor_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlab.minimum_outdoor_air_flow_rate`')
        self._data["Minimum Outdoor Air Flow Rate"] = value

    @property
    def minimum_outdoor_air_schedule_name(self):
        """Get minimum_outdoor_air_schedule_name

        Returns:
            str: the value of `minimum_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Air Schedule Name"]

    @minimum_outdoor_air_schedule_name.setter
    def minimum_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Minimum Outdoor Air Schedule Name`

        Args:
            value (str): value for IDD Field `Minimum Outdoor Air Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.minimum_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.minimum_outdoor_air_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.minimum_outdoor_air_schedule_name`')
        self._data["Minimum Outdoor Air Schedule Name"] = value

    @property
    def maximum_outdoor_air_flow_rate(self):
        """Get maximum_outdoor_air_flow_rate

        Returns:
            float: the value of `maximum_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Maximum Outdoor Air Flow Rate"]

    @maximum_outdoor_air_flow_rate.setter
    def maximum_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Flow Rate`
        schedule values multiply the minimum outdoor air flow rate

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Outdoor Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `ZoneHvacVentilatedSlab.maximum_outdoor_air_flow_rate`'.format(value))
                    self._data["Maximum Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `ZoneHvacVentilatedSlab.maximum_outdoor_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlab.maximum_outdoor_air_flow_rate`')
        self._data["Maximum Outdoor Air Flow Rate"] = value

    @property
    def maximum_outdoor_air_fraction_or_temperature_schedule_name(self):
        """Get maximum_outdoor_air_fraction_or_temperature_schedule_name

        Returns:
            str: the value of `maximum_outdoor_air_fraction_or_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Outdoor Air Fraction or Temperature Schedule Name"]

    @maximum_outdoor_air_fraction_or_temperature_schedule_name.setter
    def maximum_outdoor_air_fraction_or_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Maximum Outdoor Air Fraction or Temperature Schedule Name`
        Note that this depends on the control type as to whether schedule values are a fraction or temperature

        Args:
            value (str): value for IDD Field `Maximum Outdoor Air Fraction or Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.maximum_outdoor_air_fraction_or_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.maximum_outdoor_air_fraction_or_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.maximum_outdoor_air_fraction_or_temperature_schedule_name`')
        self._data["Maximum Outdoor Air Fraction or Temperature Schedule Name"] = value

    @property
    def system_configuration_type(self):
        """Get system_configuration_type

        Returns:
            str: the value of `system_configuration_type` or None if not set
        """
        return self._data["System Configuration Type"]

    @system_configuration_type.setter
    def system_configuration_type(self, value="SlabOnly"):
        """  Corresponds to IDD Field `System Configuration Type`

        Args:
            value (str): value for IDD Field `System Configuration Type`
                Accepted values are:
                      - SlabOnly
                      - SlabAndZone
                      - SeriesSlabs
                Default value: SlabOnly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.system_configuration_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.system_configuration_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.system_configuration_type`')
            vals = {}
            vals["slabonly"] = "SlabOnly"
            vals["slabandzone"] = "SlabAndZone"
            vals["seriesslabs"] = "SeriesSlabs"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacVentilatedSlab.system_configuration_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacVentilatedSlab.system_configuration_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["System Configuration Type"] = value

    @property
    def hollow_core_inside_diameter(self):
        """Get hollow_core_inside_diameter

        Returns:
            float: the value of `hollow_core_inside_diameter` or None if not set
        """
        return self._data["Hollow Core Inside Diameter"]

    @hollow_core_inside_diameter.setter
    def hollow_core_inside_diameter(self, value=0.05):
        """  Corresponds to IDD Field `Hollow Core Inside Diameter`

        Args:
            value (float): value for IDD Field `Hollow Core Inside Diameter`
                Units: m
                IP-Units: in
                Default value: 0.05
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacVentilatedSlab.hollow_core_inside_diameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlab.hollow_core_inside_diameter`')
        self._data["Hollow Core Inside Diameter"] = value

    @property
    def hollow_core_length(self):
        """Get hollow_core_length

        Returns:
            float: the value of `hollow_core_length` or None if not set
        """
        return self._data["Hollow Core Length"]

    @hollow_core_length.setter
    def hollow_core_length(self, value=None):
        """  Corresponds to IDD Field `Hollow Core Length`
        (length of core cavity embedded in surface)

        Args:
            value (float): value for IDD Field `Hollow Core Length`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacVentilatedSlab.hollow_core_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlab.hollow_core_length`')
        self._data["Hollow Core Length"] = value

    @property
    def number_of_cores(self):
        """Get number_of_cores

        Returns:
            float: the value of `number_of_cores` or None if not set
        """
        return self._data["Number of Cores"]

    @number_of_cores.setter
    def number_of_cores(self, value=None):
        """  Corresponds to IDD Field `Number of Cores`
        flow will be divided evenly among the cores

        Args:
            value (float): value for IDD Field `Number of Cores`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacVentilatedSlab.number_of_cores`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlab.number_of_cores`')
        self._data["Number of Cores"] = value

    @property
    def temperature_control_type(self):
        """Get temperature_control_type

        Returns:
            str: the value of `temperature_control_type` or None if not set
        """
        return self._data["Temperature Control Type"]

    @temperature_control_type.setter
    def temperature_control_type(self, value="OutdoorDryBulbTemperature"):
        """  Corresponds to IDD Field `Temperature Control Type`
        (temperature on which unit is controlled)

        Args:
            value (str): value for IDD Field `Temperature Control Type`
                Accepted values are:
                      - MeanAirTemperature
                      - MeanRadiantTemperature
                      - OperativeTemperature
                      - OutdoorDryBulbTemperature
                      - OutdoorWetBulbTemperature
                      - SurfaceTemperature
                      - ZoneAirDewPointTemperature
                Default value: OutdoorDryBulbTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.temperature_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.temperature_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.temperature_control_type`')
            vals = {}
            vals["meanairtemperature"] = "MeanAirTemperature"
            vals["meanradianttemperature"] = "MeanRadiantTemperature"
            vals["operativetemperature"] = "OperativeTemperature"
            vals["outdoordrybulbtemperature"] = "OutdoorDryBulbTemperature"
            vals["outdoorwetbulbtemperature"] = "OutdoorWetBulbTemperature"
            vals["surfacetemperature"] = "SurfaceTemperature"
            vals["zoneairdewpointtemperature"] = "ZoneAirDewPointTemperature"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacVentilatedSlab.temperature_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacVentilatedSlab.temperature_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Temperature Control Type"] = value

    @property
    def heating_high_air_temperature_schedule_name(self):
        """Get heating_high_air_temperature_schedule_name

        Returns:
            str: the value of `heating_high_air_temperature_schedule_name` or None if not set
        """
        return self._data["Heating High Air Temperature Schedule Name"]

    @heating_high_air_temperature_schedule_name.setter
    def heating_high_air_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating High Air Temperature Schedule Name`
        Air and control temperatures for heating work together to provide
        a linear function that determines the air temperature sent to the
        radiant system. The current control temperature (see A14) is
        compared to the high and low control temperatures at the current time.
        If the control temperature is above the high temperature, then the
        inlet air temperature is set to the low air temperature. If the
        control temperature is below the low temperature, then the inlet
        air temperature is set to the high air temperature. If the control
        temperature is between the high and low value, then the inlet air
        temperature is linearly interpolated between the low and high air
        temperature values.

        Args:
            value (str): value for IDD Field `Heating High Air Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.heating_high_air_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.heating_high_air_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.heating_high_air_temperature_schedule_name`')
        self._data["Heating High Air Temperature Schedule Name"] = value

    @property
    def heating_low_air_temperature_schedule_name(self):
        """Get heating_low_air_temperature_schedule_name

        Returns:
            str: the value of `heating_low_air_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Low Air Temperature Schedule Name"]

    @heating_low_air_temperature_schedule_name.setter
    def heating_low_air_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Low Air Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Air Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.heating_low_air_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.heating_low_air_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.heating_low_air_temperature_schedule_name`')
        self._data["Heating Low Air Temperature Schedule Name"] = value

    @property
    def heating_high_control_temperature_schedule_name(self):
        """Get heating_high_control_temperature_schedule_name

        Returns:
            str: the value of `heating_high_control_temperature_schedule_name` or None if not set
        """
        return self._data["Heating High Control Temperature Schedule Name"]

    @heating_high_control_temperature_schedule_name.setter
    def heating_high_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating High Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.heating_high_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.heating_high_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.heating_high_control_temperature_schedule_name`')
        self._data["Heating High Control Temperature Schedule Name"] = value

    @property
    def heating_low_control_temperature_schedule_name(self):
        """Get heating_low_control_temperature_schedule_name

        Returns:
            str: the value of `heating_low_control_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Low Control Temperature Schedule Name"]

    @heating_low_control_temperature_schedule_name.setter
    def heating_low_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Heating Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Low Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.heating_low_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.heating_low_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.heating_low_control_temperature_schedule_name`')
        self._data["Heating Low Control Temperature Schedule Name"] = value

    @property
    def cooling_high_air_temperature_schedule_name(self):
        """Get cooling_high_air_temperature_schedule_name

        Returns:
            str: the value of `cooling_high_air_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling High Air Temperature Schedule Name"]

    @cooling_high_air_temperature_schedule_name.setter
    def cooling_high_air_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling High Air Temperature Schedule Name`
        See note for heating high air temperature schedule above for
        interpretation information (or see the Input/Output Reference).

        Args:
            value (str): value for IDD Field `Cooling High Air Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cooling_high_air_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cooling_high_air_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cooling_high_air_temperature_schedule_name`')
        self._data["Cooling High Air Temperature Schedule Name"] = value

    @property
    def cooling_low_air_temperature_schedule_name(self):
        """Get cooling_low_air_temperature_schedule_name

        Returns:
            str: the value of `cooling_low_air_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Low Air Temperature Schedule Name"]

    @cooling_low_air_temperature_schedule_name.setter
    def cooling_low_air_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Low Air Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Air Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cooling_low_air_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cooling_low_air_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cooling_low_air_temperature_schedule_name`')
        self._data["Cooling Low Air Temperature Schedule Name"] = value

    @property
    def cooling_high_control_temperature_schedule_name(self):
        """Get cooling_high_control_temperature_schedule_name

        Returns:
            str: the value of `cooling_high_control_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling High Control Temperature Schedule Name"]

    @cooling_high_control_temperature_schedule_name.setter
    def cooling_high_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling High Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling High Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cooling_high_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cooling_high_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cooling_high_control_temperature_schedule_name`')
        self._data["Cooling High Control Temperature Schedule Name"] = value

    @property
    def cooling_low_control_temperature_schedule_name(self):
        """Get cooling_low_control_temperature_schedule_name

        Returns:
            str: the value of `cooling_low_control_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Low Control Temperature Schedule Name"]

    @cooling_low_control_temperature_schedule_name.setter
    def cooling_low_control_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Low Control Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Low Control Temperature Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cooling_low_control_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cooling_low_control_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cooling_low_control_temperature_schedule_name`')
        self._data["Cooling Low Control Temperature Schedule Name"] = value

    @property
    def return_air_node_name(self):
        """Get return_air_node_name

        Returns:
            str: the value of `return_air_node_name` or None if not set
        """
        return self._data["Return Air Node Name"]

    @return_air_node_name.setter
    def return_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Return Air Node Name`
        This is the zone return air inlet to the ventilated slab system outdoor air mixer.
        This node is typically a zone exhaust node (do not connect to "Zone Return Air Node").

        Args:
            value (str): value for IDD Field `Return Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.return_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.return_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.return_air_node_name`')
        self._data["Return Air Node Name"] = value

    @property
    def slab_in_node_name(self):
        """Get slab_in_node_name

        Returns:
            str: the value of `slab_in_node_name` or None if not set
        """
        return self._data["Slab In Node Name"]

    @slab_in_node_name.setter
    def slab_in_node_name(self, value=None):
        """  Corresponds to IDD Field `Slab In Node Name`
        This is the node entering the slab or series of slabs after the fan and coil(s).

        Args:
            value (str): value for IDD Field `Slab In Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.slab_in_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.slab_in_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.slab_in_node_name`')
        self._data["Slab In Node Name"] = value

    @property
    def zone_supply_air_node_name(self):
        """Get zone_supply_air_node_name

        Returns:
            str: the value of `zone_supply_air_node_name` or None if not set
        """
        return self._data["Zone Supply Air Node Name"]

    @zone_supply_air_node_name.setter
    def zone_supply_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Supply Air Node Name`
        This is the node name exiting the slab.
        This node is typically a zone inlet node.
        Leave blank when the system configuration is SlabOnly or SeriesSlabs.

        Args:
            value (str): value for IDD Field `Zone Supply Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.zone_supply_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.zone_supply_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.zone_supply_air_node_name`')
        self._data["Zone Supply Air Node Name"] = value

    @property
    def outdoor_air_node_name(self):
        """Get outdoor_air_node_name

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set
        """
        return self._data["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Node Name`
        This node is the outdoor air inlet to the ventilated slab oa mixer.
        This node should also be specified in an OutdoorAir:Node or OutdoorAir:NodeList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.outdoor_air_node_name`')
        self._data["Outdoor Air Node Name"] = value

    @property
    def relief_air_node_name(self):
        """Get relief_air_node_name

        Returns:
            str: the value of `relief_air_node_name` or None if not set
        """
        return self._data["Relief Air Node Name"]

    @relief_air_node_name.setter
    def relief_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Relief Air Node Name`
        This node is the relief air node from the ventilated slab outdoor air mixer.

        Args:
            value (str): value for IDD Field `Relief Air Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.relief_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.relief_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.relief_air_node_name`')
        self._data["Relief Air Node Name"] = value

    @property
    def outdoor_air_mixer_outlet_node_name(self):
        """Get outdoor_air_mixer_outlet_node_name

        Returns:
            str: the value of `outdoor_air_mixer_outlet_node_name` or None if not set
        """
        return self._data["Outdoor Air Mixer Outlet Node Name"]

    @outdoor_air_mixer_outlet_node_name.setter
    def outdoor_air_mixer_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Mixer Outlet Node Name`
        This is the node name leaving the outdoor air mixer and entering the fan and coil(s).

        Args:
            value (str): value for IDD Field `Outdoor Air Mixer Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.outdoor_air_mixer_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.outdoor_air_mixer_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.outdoor_air_mixer_outlet_node_name`')
        self._data["Outdoor Air Mixer Outlet Node Name"] = value

    @property
    def fan_outlet_node_name(self):
        """Get fan_outlet_node_name

        Returns:
            str: the value of `fan_outlet_node_name` or None if not set
        """
        return self._data["Fan Outlet Node Name"]

    @fan_outlet_node_name.setter
    def fan_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fan Outlet Node Name`
        This is the node name of the fan outlet.

        Args:
            value (str): value for IDD Field `Fan Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.fan_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.fan_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.fan_outlet_node_name`')
        self._data["Fan Outlet Node Name"] = value

    @property
    def fan_name(self):
        """Get fan_name

        Returns:
            str: the value of `fan_name` or None if not set
        """
        return self._data["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """  Corresponds to IDD Field `Fan Name`
        Allowable fan type is Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `Fan Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.fan_name`')
        self._data["Fan Name"] = value

    @property
    def coil_option_type(self):
        """Get coil_option_type

        Returns:
            str: the value of `coil_option_type` or None if not set
        """
        return self._data["Coil Option Type"]

    @coil_option_type.setter
    def coil_option_type(self, value=None):
        """  Corresponds to IDD Field `Coil Option Type`

        Args:
            value (str): value for IDD Field `Coil Option Type`
                Accepted values are:
                      - None
                      - Heating
                      - Cooling
                      - HeatingAndCooling
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.coil_option_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.coil_option_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.coil_option_type`')
            vals = {}
            vals["none"] = "None"
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["heatingandcooling"] = "HeatingAndCooling"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacVentilatedSlab.coil_option_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacVentilatedSlab.coil_option_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Coil Option Type"] = value

    @property
    def heating_coil_object_type(self):
        """Get heating_coil_object_type

        Returns:
            str: the value of `heating_coil_object_type` or None if not set
        """
        return self._data["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`
                Accepted values are:
                      - Coil:Heating:Water
                      - Coil:Heating:Electric
                      - Coil:Heating:Gas
                      - Coil:Heating:Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacVentilatedSlab.heating_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacVentilatedSlab.heating_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """Get heating_coil_name

        Returns:
            str: the value of `heating_coil_name` or None if not set
        """
        return self._data["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """  Corresponds to IDD Field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.heating_coil_name`')
        self._data["Heating Coil Name"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """Get hot_water_or_steam_inlet_node_name

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set
        """
        return self._data["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Hot Water or Steam Inlet Node Name`

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.hot_water_or_steam_inlet_node_name`')
        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def cooling_coil_object_type(self):
        """Get cooling_coil_object_type

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set
        """
        return self._data["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`
                Accepted values are:
                      - Coil:Cooling:Water
                      - Coil:Cooling:Water:DetailedGeometry
                      - CoilSystem:Cooling:Water:HeatExchangerAssisted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            vals["coilsystem:cooling:water:heatexchangerassisted"] = "CoilSystem:Cooling:Water:HeatExchangerAssisted"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `ZoneHvacVentilatedSlab.cooling_coil_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacVentilatedSlab.cooling_coil_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """Get cooling_coil_name

        Returns:
            str: the value of `cooling_coil_name` or None if not set
        """
        return self._data["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """  Corresponds to IDD Field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cooling_coil_name`')
        self._data["Cooling Coil Name"] = value

    @property
    def cold_water_inlet_node_name(self):
        """Get cold_water_inlet_node_name

        Returns:
            str: the value of `cold_water_inlet_node_name` or None if not set
        """
        return self._data["Cold Water Inlet Node Name"]

    @cold_water_inlet_node_name.setter
    def cold_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Cold Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cold Water Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.cold_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.cold_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.cold_water_inlet_node_name`')
        self._data["Cold Water Inlet Node Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_specification_zonehvac_sizing_object_name(self):
        """Get design_specification_zonehvac_sizing_object_name

        Returns:
            str: the value of `design_specification_zonehvac_sizing_object_name` or None if not set
        """
        return self._data["Design Specification ZoneHVAC Sizing Object Name"]

    @design_specification_zonehvac_sizing_object_name.setter
    def design_specification_zonehvac_sizing_object_name(self, value=None):
        """  Corresponds to IDD Field `Design Specification ZoneHVAC Sizing Object Name`
        Enter the name of a DesignSpecificationZoneHVACSizing object.

        Args:
            value (str): value for IDD Field `Design Specification ZoneHVAC Sizing Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlab.design_specification_zonehvac_sizing_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlab.design_specification_zonehvac_sizing_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlab.design_specification_zonehvac_sizing_object_name`')
        self._data["Design Specification ZoneHVAC Sizing Object Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacVentilatedSlab:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacVentilatedSlab:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacVentilatedSlab: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacVentilatedSlab: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneHvacVentilatedSlabSlabGroup(object):
    """ Corresponds to IDD object `ZoneHVAC:VentilatedSlab:SlabGroup`
        This is used to allow the coordinate control of several ventilad slab system
        surfaces. Note that the flow fractions must sum up to 1.0.
        The number of surfaces can be expanded beyond 10, if necessary, by adding more
        groups to the end of the list
    """
    internal_name = "ZoneHVAC:VentilatedSlab:SlabGroup"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 7
    format = None
    min_fields = 0
    extensible_keys = ["Zone 1 Name", "Surface 1 Name", "Core Diameter for Surface 1", "Core Length for Surface 1", "Core Numbers for Surface 1", "Slab Inlet Node Name for Surface 1", "Slab Outlet Node Name for Surface 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:VentilatedSlab:SlabGroup`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       zone_1_name=None,
                       surface_1_name=None,
                       core_diameter_for_surface_1=None,
                       core_length_for_surface_1=None,
                       core_numbers_for_surface_1=None,
                       slab_inlet_node_name_for_surface_1=None,
                       slab_outlet_node_name_for_surface_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            zone_1_name (str): value for IDD Field `Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            core_diameter_for_surface_1 (float): value for IDD Field `Core Diameter for Surface 1`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            core_length_for_surface_1 (float): value for IDD Field `Core Length for Surface 1`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            core_numbers_for_surface_1 (float): value for IDD Field `Core Numbers for Surface 1`
                value >= 0.0
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
        vals.append(self._check_zone_1_name(zone_1_name))
        vals.append(self._check_surface_1_name(surface_1_name))
        vals.append(self._check_core_diameter_for_surface_1(core_diameter_for_surface_1))
        vals.append(self._check_core_length_for_surface_1(core_length_for_surface_1))
        vals.append(self._check_core_numbers_for_surface_1(core_numbers_for_surface_1))
        vals.append(self._check_slab_inlet_node_name_for_surface_1(slab_inlet_node_name_for_surface_1))
        vals.append(self._check_slab_outlet_node_name_for_surface_1(slab_outlet_node_name_for_surface_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_zone_1_name(self, value):
        """ Validates falue of field `Zone 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.zone_1_name`')
        return value

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.surface_1_name`')
        return value

    def _check_core_diameter_for_surface_1(self, value):
        """ Validates falue of field `Core Diameter for Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.core_diameter_for_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.core_diameter_for_surface_1`')
        return value

    def _check_core_length_for_surface_1(self, value):
        """ Validates falue of field `Core Length for Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.core_length_for_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.core_length_for_surface_1`')
        return value

    def _check_core_numbers_for_surface_1(self, value):
        """ Validates falue of field `Core Numbers for Surface 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.core_numbers_for_surface_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.core_numbers_for_surface_1`')
        return value

    def _check_slab_inlet_node_name_for_surface_1(self, value):
        """ Validates falue of field `Slab Inlet Node Name for Surface 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.slab_inlet_node_name_for_surface_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.slab_inlet_node_name_for_surface_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.slab_inlet_node_name_for_surface_1`')
        return value

    def _check_slab_outlet_node_name_for_surface_1(self, value):
        """ Validates falue of field `Slab Outlet Node Name for Surface 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacVentilatedSlabSlabGroup.slab_outlet_node_name_for_surface_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.slab_outlet_node_name_for_surface_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacVentilatedSlabSlabGroup.slab_outlet_node_name_for_surface_1`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field ZoneHvacVentilatedSlabSlabGroup:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacVentilatedSlabSlabGroup:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacVentilatedSlabSlabGroup: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacVentilatedSlabSlabGroup: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

        return good

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def export(self):
        """ Export values of data object as list of strings"""
        out = []

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])