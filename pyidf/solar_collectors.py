from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class SolarCollectorPerformanceFlatPlate(object):
    """ Corresponds to IDD object `SolarCollectorPerformance:FlatPlate`
        Thermal and optical performance parameters for a single flat plate solar collector
        module. These parameters are based on the testing methodologies described in ASHRAE
        Standards 93 and 96 which are used Solar Rating and Certification Corporation (SRCC)
        Directory of SRCC Certified Solar Collector Ratings. See EnergyPlus DataSets file
        SolarCollectors.idf.
    """
    internal_name = "SolarCollectorPerformance:FlatPlate"
    field_count = 10
    required_fields = ["Name", "Gross Area", "Test Fluid", "Test Flow Rate", "Test Correlation Type", "Coefficient 1 of Efficiency Equation", "Coefficient 2 of Efficiency Equation"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollectorPerformance:FlatPlate`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Gross Area"] = None
        self._data["Test Fluid"] = None
        self._data["Test Flow Rate"] = None
        self._data["Test Correlation Type"] = None
        self._data["Coefficient 1 of Efficiency Equation"] = None
        self._data["Coefficient 2 of Efficiency Equation"] = None
        self._data["Coefficient 3 of Efficiency Equation"] = None
        self._data["Coefficient 2 of Incident Angle Modifier"] = None
        self._data["Coefficient 3 of Incident Angle Modifier"] = None
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
            self.gross_area = None
        else:
            self.gross_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.test_fluid = None
        else:
            self.test_fluid = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.test_flow_rate = None
        else:
            self.test_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.test_correlation_type = None
        else:
            self.test_correlation_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_1_of_efficiency_equation = None
        else:
            self.coefficient_1_of_efficiency_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_2_of_efficiency_equation = None
        else:
            self.coefficient_2_of_efficiency_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_3_of_efficiency_equation = None
        else:
            self.coefficient_3_of_efficiency_equation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_2_of_incident_angle_modifier = None
        else:
            self.coefficient_2_of_incident_angle_modifier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_3_of_incident_angle_modifier = None
        else:
            self.coefficient_3_of_incident_angle_modifier = vals[i]
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformanceFlatPlate.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformanceFlatPlate.name`')
        self._data["Name"] = value

    @property
    def gross_area(self):
        """Get gross_area

        Returns:
            float: the value of `gross_area` or None if not set
        """
        return self._data["Gross Area"]

    @gross_area.setter
    def gross_area(self, value=None):
        """  Corresponds to IDD Field `Gross Area`

        Args:
            value (float): value for IDD Field `Gross Area`
                Units: m2
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.gross_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceFlatPlate.gross_area`')
        self._data["Gross Area"] = value

    @property
    def test_fluid(self):
        """Get test_fluid

        Returns:
            str: the value of `test_fluid` or None if not set
        """
        return self._data["Test Fluid"]

    @test_fluid.setter
    def test_fluid(self, value="Water"):
        """  Corresponds to IDD Field `Test Fluid`

        Args:
            value (str): value for IDD Field `Test Fluid`
                Accepted values are:
                      - Water
                Default value: Water
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.test_fluid`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformanceFlatPlate.test_fluid`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformanceFlatPlate.test_fluid`')
            vals = {}
            vals["water"] = "Water"
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
                                     'field `SolarCollectorPerformanceFlatPlate.test_fluid`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorPerformanceFlatPlate.test_fluid`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Test Fluid"] = value

    @property
    def test_flow_rate(self):
        """Get test_flow_rate

        Returns:
            float: the value of `test_flow_rate` or None if not set
        """
        return self._data["Test Flow Rate"]

    @test_flow_rate.setter
    def test_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Test Flow Rate`

        Args:
            value (float): value for IDD Field `Test Flow Rate`
                Units: m3/s
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.test_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceFlatPlate.test_flow_rate`')
        self._data["Test Flow Rate"] = value

    @property
    def test_correlation_type(self):
        """Get test_correlation_type

        Returns:
            str: the value of `test_correlation_type` or None if not set
        """
        return self._data["Test Correlation Type"]

    @test_correlation_type.setter
    def test_correlation_type(self, value=None):
        """  Corresponds to IDD Field `Test Correlation Type`

        Args:
            value (str): value for IDD Field `Test Correlation Type`
                Accepted values are:
                      - Inlet
                      - Average
                      - Outlet
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.test_correlation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformanceFlatPlate.test_correlation_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformanceFlatPlate.test_correlation_type`')
            vals = {}
            vals["inlet"] = "Inlet"
            vals["average"] = "Average"
            vals["outlet"] = "Outlet"
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
                                     'field `SolarCollectorPerformanceFlatPlate.test_correlation_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorPerformanceFlatPlate.test_correlation_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Test Correlation Type"] = value

    @property
    def coefficient_1_of_efficiency_equation(self):
        """Get coefficient_1_of_efficiency_equation

        Returns:
            float: the value of `coefficient_1_of_efficiency_equation` or None if not set
        """
        return self._data["Coefficient 1 of Efficiency Equation"]

    @coefficient_1_of_efficiency_equation.setter
    def coefficient_1_of_efficiency_equation(self, value=None):
        """  Corresponds to IDD Field `Coefficient 1 of Efficiency Equation`
        Y-intercept term

        Args:
            value (float): value for IDD Field `Coefficient 1 of Efficiency Equation`
                Units: dimensionless
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.coefficient_1_of_efficiency_equation`'.format(value))
        self._data["Coefficient 1 of Efficiency Equation"] = value

    @property
    def coefficient_2_of_efficiency_equation(self):
        """Get coefficient_2_of_efficiency_equation

        Returns:
            float: the value of `coefficient_2_of_efficiency_equation` or None if not set
        """
        return self._data["Coefficient 2 of Efficiency Equation"]

    @coefficient_2_of_efficiency_equation.setter
    def coefficient_2_of_efficiency_equation(self, value=None):
        """  Corresponds to IDD Field `Coefficient 2 of Efficiency Equation`
        1st Order term

        Args:
            value (float): value for IDD Field `Coefficient 2 of Efficiency Equation`
                Units: W/m2-K
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.coefficient_2_of_efficiency_equation`'.format(value))
        self._data["Coefficient 2 of Efficiency Equation"] = value

    @property
    def coefficient_3_of_efficiency_equation(self):
        """Get coefficient_3_of_efficiency_equation

        Returns:
            float: the value of `coefficient_3_of_efficiency_equation` or None if not set
        """
        return self._data["Coefficient 3 of Efficiency Equation"]

    @coefficient_3_of_efficiency_equation.setter
    def coefficient_3_of_efficiency_equation(self, value=None):
        """  Corresponds to IDD Field `Coefficient 3 of Efficiency Equation`
        2nd order term

        Args:
            value (float): value for IDD Field `Coefficient 3 of Efficiency Equation`
                Units: W/m2-K2
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.coefficient_3_of_efficiency_equation`'.format(value))
        self._data["Coefficient 3 of Efficiency Equation"] = value

    @property
    def coefficient_2_of_incident_angle_modifier(self):
        """Get coefficient_2_of_incident_angle_modifier

        Returns:
            float: the value of `coefficient_2_of_incident_angle_modifier` or None if not set
        """
        return self._data["Coefficient 2 of Incident Angle Modifier"]

    @coefficient_2_of_incident_angle_modifier.setter
    def coefficient_2_of_incident_angle_modifier(self, value=None):
        """  Corresponds to IDD Field `Coefficient 2 of Incident Angle Modifier`
        1st order term

        Args:
            value (float): value for IDD Field `Coefficient 2 of Incident Angle Modifier`
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.coefficient_2_of_incident_angle_modifier`'.format(value))
        self._data["Coefficient 2 of Incident Angle Modifier"] = value

    @property
    def coefficient_3_of_incident_angle_modifier(self):
        """Get coefficient_3_of_incident_angle_modifier

        Returns:
            float: the value of `coefficient_3_of_incident_angle_modifier` or None if not set
        """
        return self._data["Coefficient 3 of Incident Angle Modifier"]

    @coefficient_3_of_incident_angle_modifier.setter
    def coefficient_3_of_incident_angle_modifier(self, value=None):
        """  Corresponds to IDD Field `Coefficient 3 of Incident Angle Modifier`
        2nd order term

        Args:
            value (float): value for IDD Field `Coefficient 3 of Incident Angle Modifier`
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
                                 ' for field `SolarCollectorPerformanceFlatPlate.coefficient_3_of_incident_angle_modifier`'.format(value))
        self._data["Coefficient 3 of Incident Angle Modifier"] = value

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
                    raise ValueError("Required field SolarCollectorPerformanceFlatPlate:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorPerformanceFlatPlate:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorPerformanceFlatPlate: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorPerformanceFlatPlate: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorFlatPlateWater(object):
    """ Corresponds to IDD object `SolarCollector:FlatPlate:Water`
        Flat plate water solar collector (single glazed, unglazed, or evacuated tube).
        Thermal and optical properties are taken from the referenced
        SolarCollectorPerformance:FlatPlate object. Collector tilt, azimuth, and gross area
        are taken from the referenced building surface or shading surface. The collector
        surface participates normally in all shading calculations.
    """
    internal_name = "SolarCollector:FlatPlate:Water"
    field_count = 6
    required_fields = ["Name", "SolarCollectorPerformance Name", "Surface Name", "Inlet Node Name", "Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollector:FlatPlate:Water`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["SolarCollectorPerformance Name"] = None
        self._data["Surface Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Maximum Flow Rate"] = None
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
            self.solarcollectorperformance_name = None
        else:
            self.solarcollectorperformance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
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
                                 ' for field `SolarCollectorFlatPlateWater.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlateWater.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlateWater.name`')
        self._data["Name"] = value

    @property
    def solarcollectorperformance_name(self):
        """Get solarcollectorperformance_name

        Returns:
            str: the value of `solarcollectorperformance_name` or None if not set
        """
        return self._data["SolarCollectorPerformance Name"]

    @solarcollectorperformance_name.setter
    def solarcollectorperformance_name(self, value=None):
        """  Corresponds to IDD Field `SolarCollectorPerformance Name`

        Args:
            value (str): value for IDD Field `SolarCollectorPerformance Name`
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
                                 ' for field `SolarCollectorFlatPlateWater.solarcollectorperformance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlateWater.solarcollectorperformance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlateWater.solarcollectorperformance_name`')
        self._data["SolarCollectorPerformance Name"] = value

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SolarCollectorFlatPlateWater.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlateWater.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlateWater.surface_name`')
        self._data["Surface Name"] = value

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
                                 ' for field `SolarCollectorFlatPlateWater.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlateWater.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlateWater.inlet_node_name`')
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
                                 ' for field `SolarCollectorFlatPlateWater.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlateWater.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlateWater.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
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
                                 ' for field `SolarCollectorFlatPlateWater.maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorFlatPlateWater.maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

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
                    raise ValueError("Required field SolarCollectorFlatPlateWater:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorFlatPlateWater:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorFlatPlateWater: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorFlatPlateWater: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorFlatPlatePhotovoltaicThermal(object):
    """ Corresponds to IDD object `SolarCollector:FlatPlate:PhotovoltaicThermal`
        Models hybrid photovoltaic-thermal (PVT) solar collectors that convert incident solar
        energy into both electricity and useful thermal energy by heating air or water.
    """
    internal_name = "SolarCollector:FlatPlate:PhotovoltaicThermal"
    field_count = 10
    required_fields = ["Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollector:FlatPlate:PhotovoltaicThermal`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Photovoltaic-Thermal Model Performance Name"] = None
        self._data["Photovoltaic Name"] = None
        self._data["Thermal Working Fluid Type"] = None
        self._data["Water Inlet Node Name"] = None
        self._data["Water Outlet Node Name"] = None
        self._data["Air Inlet Node Name"] = None
        self._data["Air Outlet Node Name"] = None
        self._data["Design Flow Rate"] = None
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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.photovoltaicthermal_model_performance_name = None
        else:
            self.photovoltaicthermal_model_performance_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.photovoltaic_name = None
        else:
            self.photovoltaic_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_working_fluid_type = None
        else:
            self.thermal_working_fluid_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.name`')
        self._data["Name"] = value

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.surface_name`')
        self._data["Surface Name"] = value

    @property
    def photovoltaicthermal_model_performance_name(self):
        """Get photovoltaicthermal_model_performance_name

        Returns:
            str: the value of `photovoltaicthermal_model_performance_name` or None if not set
        """
        return self._data["Photovoltaic-Thermal Model Performance Name"]

    @photovoltaicthermal_model_performance_name.setter
    def photovoltaicthermal_model_performance_name(self, value=None):
        """  Corresponds to IDD Field `Photovoltaic-Thermal Model Performance Name`

        Args:
            value (str): value for IDD Field `Photovoltaic-Thermal Model Performance Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.photovoltaicthermal_model_performance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.photovoltaicthermal_model_performance_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.photovoltaicthermal_model_performance_name`')
        self._data["Photovoltaic-Thermal Model Performance Name"] = value

    @property
    def photovoltaic_name(self):
        """Get photovoltaic_name

        Returns:
            str: the value of `photovoltaic_name` or None if not set
        """
        return self._data["Photovoltaic Name"]

    @photovoltaic_name.setter
    def photovoltaic_name(self, value=None):
        """  Corresponds to IDD Field `Photovoltaic Name`
        Enter the name of a Generator:Photovoltaic object.

        Args:
            value (str): value for IDD Field `Photovoltaic Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.photovoltaic_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.photovoltaic_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.photovoltaic_name`')
        self._data["Photovoltaic Name"] = value

    @property
    def thermal_working_fluid_type(self):
        """Get thermal_working_fluid_type

        Returns:
            str: the value of `thermal_working_fluid_type` or None if not set
        """
        return self._data["Thermal Working Fluid Type"]

    @thermal_working_fluid_type.setter
    def thermal_working_fluid_type(self, value=None):
        """  Corresponds to IDD Field `Thermal Working Fluid Type`

        Args:
            value (str): value for IDD Field `Thermal Working Fluid Type`
                Accepted values are:
                      - Water
                      - Air
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.thermal_working_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.thermal_working_fluid_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.thermal_working_fluid_type`')
            vals = {}
            vals["water"] = "Water"
            vals["air"] = "Air"
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
                                     'field `SolarCollectorFlatPlatePhotovoltaicThermal.thermal_working_fluid_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorFlatPlatePhotovoltaicThermal.thermal_working_fluid_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Thermal Working Fluid Type"] = value

    @property
    def water_inlet_node_name(self):
        """Get water_inlet_node_name

        Returns:
            str: the value of `water_inlet_node_name` or None if not set
        """
        return self._data["Water Inlet Node Name"]

    @water_inlet_node_name.setter
    def water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Water Inlet Node Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.water_inlet_node_name`')
        self._data["Water Inlet Node Name"] = value

    @property
    def water_outlet_node_name(self):
        """Get water_outlet_node_name

        Returns:
            str: the value of `water_outlet_node_name` or None if not set
        """
        return self._data["Water Outlet Node Name"]

    @water_outlet_node_name.setter
    def water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Water Outlet Node Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.water_outlet_node_name`')
        self._data["Water Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """Get air_inlet_node_name

        Returns:
            str: the value of `air_inlet_node_name` or None if not set
        """
        return self._data["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.air_inlet_node_name`')
        self._data["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`
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
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.air_outlet_node_name`')
        self._data["Air Outlet Node Name"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Flow Rate`
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
                    self._data["Design Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `SolarCollectorFlatPlatePhotovoltaicThermal.design_flow_rate`'.format(value))
                    self._data["Design Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `SolarCollectorFlatPlatePhotovoltaicThermal.design_flow_rate`'.format(value))
        self._data["Design Flow Rate"] = value

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
                    raise ValueError("Required field SolarCollectorFlatPlatePhotovoltaicThermal:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorFlatPlatePhotovoltaicThermal:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorFlatPlatePhotovoltaicThermal: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorFlatPlatePhotovoltaicThermal: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorPerformancePhotovoltaicThermalSimple(object):
    """ Corresponds to IDD object `SolarCollectorPerformance:PhotovoltaicThermal:Simple`
        Thermal performance parameters for a hybrid photovoltaic-thermal (PVT) solar collector.
    """
    internal_name = "SolarCollectorPerformance:PhotovoltaicThermal:Simple"
    field_count = 6
    required_fields = ["Fraction of Surface Area with Active Thermal Collector"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollectorPerformance:PhotovoltaicThermal:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fraction of Surface Area with Active Thermal Collector"] = None
        self._data["Thermal Conversion Efficiency Input Mode Type"] = None
        self._data["Value for Thermal Conversion Efficiency if Fixed"] = None
        self._data["Thermal Conversion Efficiency Schedule Name"] = None
        self._data["Front Surface Emittance"] = None
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
            self.fraction_of_surface_area_with_active_thermal_collector = None
        else:
            self.fraction_of_surface_area_with_active_thermal_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conversion_efficiency_input_mode_type = None
        else:
            self.thermal_conversion_efficiency_input_mode_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_thermal_conversion_efficiency_if_fixed = None
        else:
            self.value_for_thermal_conversion_efficiency_if_fixed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_conversion_efficiency_schedule_name = None
        else:
            self.thermal_conversion_efficiency_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.front_surface_emittance = None
        else:
            self.front_surface_emittance = vals[i]
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
                                 ' for field `SolarCollectorPerformancePhotovoltaicThermalSimple.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.name`')
        self._data["Name"] = value

    @property
    def fraction_of_surface_area_with_active_thermal_collector(self):
        """Get fraction_of_surface_area_with_active_thermal_collector

        Returns:
            float: the value of `fraction_of_surface_area_with_active_thermal_collector` or None if not set
        """
        return self._data["Fraction of Surface Area with Active Thermal Collector"]

    @fraction_of_surface_area_with_active_thermal_collector.setter
    def fraction_of_surface_area_with_active_thermal_collector(self, value=None):
        """  Corresponds to IDD Field `Fraction of Surface Area with Active Thermal Collector`

        Args:
            value (float): value for IDD Field `Fraction of Surface Area with Active Thermal Collector`
                Units: dimensionless
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
                                 ' for field `SolarCollectorPerformancePhotovoltaicThermalSimple.fraction_of_surface_area_with_active_thermal_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.fraction_of_surface_area_with_active_thermal_collector`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.fraction_of_surface_area_with_active_thermal_collector`')
        self._data["Fraction of Surface Area with Active Thermal Collector"] = value

    @property
    def thermal_conversion_efficiency_input_mode_type(self):
        """Get thermal_conversion_efficiency_input_mode_type

        Returns:
            str: the value of `thermal_conversion_efficiency_input_mode_type` or None if not set
        """
        return self._data["Thermal Conversion Efficiency Input Mode Type"]

    @thermal_conversion_efficiency_input_mode_type.setter
    def thermal_conversion_efficiency_input_mode_type(self, value=None):
        """  Corresponds to IDD Field `Thermal Conversion Efficiency Input Mode Type`

        Args:
            value (str): value for IDD Field `Thermal Conversion Efficiency Input Mode Type`
                Accepted values are:
                      - Fixed
                      - Scheduled
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
                                 ' for field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_input_mode_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_input_mode_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_input_mode_type`')
            vals = {}
            vals["fixed"] = "Fixed"
            vals["scheduled"] = "Scheduled"
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
                                     'field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_input_mode_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_input_mode_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Thermal Conversion Efficiency Input Mode Type"] = value

    @property
    def value_for_thermal_conversion_efficiency_if_fixed(self):
        """Get value_for_thermal_conversion_efficiency_if_fixed

        Returns:
            float: the value of `value_for_thermal_conversion_efficiency_if_fixed` or None if not set
        """
        return self._data["Value for Thermal Conversion Efficiency if Fixed"]

    @value_for_thermal_conversion_efficiency_if_fixed.setter
    def value_for_thermal_conversion_efficiency_if_fixed(self, value=None):
        """  Corresponds to IDD Field `Value for Thermal Conversion Efficiency if Fixed`
        Efficiency = (thermal power generated [W])/(incident solar[W])

        Args:
            value (float): value for IDD Field `Value for Thermal Conversion Efficiency if Fixed`
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
                                 ' for field `SolarCollectorPerformancePhotovoltaicThermalSimple.value_for_thermal_conversion_efficiency_if_fixed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.value_for_thermal_conversion_efficiency_if_fixed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.value_for_thermal_conversion_efficiency_if_fixed`')
        self._data["Value for Thermal Conversion Efficiency if Fixed"] = value

    @property
    def thermal_conversion_efficiency_schedule_name(self):
        """Get thermal_conversion_efficiency_schedule_name

        Returns:
            str: the value of `thermal_conversion_efficiency_schedule_name` or None if not set
        """
        return self._data["Thermal Conversion Efficiency Schedule Name"]

    @thermal_conversion_efficiency_schedule_name.setter
    def thermal_conversion_efficiency_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Thermal Conversion Efficiency Schedule Name`

        Args:
            value (str): value for IDD Field `Thermal Conversion Efficiency Schedule Name`
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
                                 ' for field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.thermal_conversion_efficiency_schedule_name`')
        self._data["Thermal Conversion Efficiency Schedule Name"] = value

    @property
    def front_surface_emittance(self):
        """Get front_surface_emittance

        Returns:
            float: the value of `front_surface_emittance` or None if not set
        """
        return self._data["Front Surface Emittance"]

    @front_surface_emittance.setter
    def front_surface_emittance(self, value=0.84):
        """  Corresponds to IDD Field `Front Surface Emittance`

        Args:
            value (float): value for IDD Field `Front Surface Emittance`
                Default value: 0.84
                value > 0.0
                value < 1.0
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
                                 ' for field `SolarCollectorPerformancePhotovoltaicThermalSimple.front_surface_emittance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.front_surface_emittance`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformancePhotovoltaicThermalSimple.front_surface_emittance`')
        self._data["Front Surface Emittance"] = value

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
                    raise ValueError("Required field SolarCollectorPerformancePhotovoltaicThermalSimple:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorPerformancePhotovoltaicThermalSimple:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorPerformancePhotovoltaicThermalSimple: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorPerformancePhotovoltaicThermalSimple: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorIntegralCollectorStorage(object):
    """ Corresponds to IDD object `SolarCollector:IntegralCollectorStorage`
        Glazed solar collector with integral storage unit. Thermal and optical properties are
        taken from the referenced SolarCollectorPerformance:IntegralCollectorStorage object.
        Collector tilt, azimuth, and gross area are taken from the referenced building surface
        or shading surface. The collector surface participates normally in all shading
        calculations.
    """
    internal_name = "SolarCollector:IntegralCollectorStorage"
    field_count = 8
    required_fields = ["Name", "IntegralCollectorStorageParameters Name", "Surface Name", "Bottom Surface Boundary Conditions Type", "Inlet Node Name", "Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollector:IntegralCollectorStorage`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["IntegralCollectorStorageParameters Name"] = None
        self._data["Surface Name"] = None
        self._data["Bottom Surface Boundary Conditions Type"] = None
        self._data["Boundary Condition Model Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Maximum Flow Rate"] = None
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
            self.integralcollectorstorageparameters_name = None
        else:
            self.integralcollectorstorageparameters_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.bottom_surface_boundary_conditions_type = None
        else:
            self.bottom_surface_boundary_conditions_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.boundary_condition_model_name = None
        else:
            self.boundary_condition_model_name = vals[i]
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.name`')
        self._data["Name"] = value

    @property
    def integralcollectorstorageparameters_name(self):
        """Get integralcollectorstorageparameters_name

        Returns:
            str: the value of `integralcollectorstorageparameters_name` or None if not set
        """
        return self._data["IntegralCollectorStorageParameters Name"]

    @integralcollectorstorageparameters_name.setter
    def integralcollectorstorageparameters_name(self, value=None):
        """  Corresponds to IDD Field `IntegralCollectorStorageParameters Name`

        Args:
            value (str): value for IDD Field `IntegralCollectorStorageParameters Name`
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.integralcollectorstorageparameters_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.integralcollectorstorageparameters_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.integralcollectorstorageparameters_name`')
        self._data["IntegralCollectorStorageParameters Name"] = value

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.surface_name`')
        self._data["Surface Name"] = value

    @property
    def bottom_surface_boundary_conditions_type(self):
        """Get bottom_surface_boundary_conditions_type

        Returns:
            str: the value of `bottom_surface_boundary_conditions_type` or None if not set
        """
        return self._data["Bottom Surface Boundary Conditions Type"]

    @bottom_surface_boundary_conditions_type.setter
    def bottom_surface_boundary_conditions_type(self, value="AmbientAir"):
        """  Corresponds to IDD Field `Bottom Surface Boundary Conditions Type`

        Args:
            value (str): value for IDD Field `Bottom Surface Boundary Conditions Type`
                Accepted values are:
                      - OtherSideConditionsModel
                      - AmbientAir
                Default value: AmbientAir
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.bottom_surface_boundary_conditions_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.bottom_surface_boundary_conditions_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.bottom_surface_boundary_conditions_type`')
            vals = {}
            vals["othersideconditionsmodel"] = "OtherSideConditionsModel"
            vals["ambientair"] = "AmbientAir"
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
                                     'field `SolarCollectorIntegralCollectorStorage.bottom_surface_boundary_conditions_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorIntegralCollectorStorage.bottom_surface_boundary_conditions_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Bottom Surface Boundary Conditions Type"] = value

    @property
    def boundary_condition_model_name(self):
        """Get boundary_condition_model_name

        Returns:
            str: the value of `boundary_condition_model_name` or None if not set
        """
        return self._data["Boundary Condition Model Name"]

    @boundary_condition_model_name.setter
    def boundary_condition_model_name(self, value=None):
        """  Corresponds to IDD Field `Boundary Condition Model Name`
        Enter the name of a SurfaceProperty:OtherSideConditionsModel
        object. Specified only if the boundary condition type is
        OtherSideConditionsModel, otherwise leave it blank

        Args:
            value (str): value for IDD Field `Boundary Condition Model Name`
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.boundary_condition_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.boundary_condition_model_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.boundary_condition_model_name`')
        self._data["Boundary Condition Model Name"] = value

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
                                 ' for field `SolarCollectorIntegralCollectorStorage.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.inlet_node_name`')
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorIntegralCollectorStorage.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorIntegralCollectorStorage.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
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
                                 ' for field `SolarCollectorIntegralCollectorStorage.maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorIntegralCollectorStorage.maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

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
                    raise ValueError("Required field SolarCollectorIntegralCollectorStorage:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorIntegralCollectorStorage:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorIntegralCollectorStorage: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorIntegralCollectorStorage: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorPerformanceIntegralCollectorStorage(object):
    """ Corresponds to IDD object `SolarCollectorPerformance:IntegralCollectorStorage`
        Thermal and optical performance parameters for a single glazed solar collector with
        integral storage unit.
    """
    internal_name = "SolarCollectorPerformance:IntegralCollectorStorage"
    field_count = 19
    required_fields = ["Name", "ICS Collector Type", "Bottom Heat Loss Conductance", "Side Heat Loss Conductance", "Aspect Ratio", "Collector Side Height", "Thermal Mass of Absorber Plate", "Number of Covers", "Cover Spacing", "Refractive Index of Outer Cover", "Extinction Coefficient Times Thickness of Outer Cover", "Emissivity of Outer Cover", "Refractive Index of Inner Cover", "Extinction Coefficient Times Thickness of the inner Cover", "Emmissivity of Inner Cover", "Absorptance of Absorber Plate", "Emissivity of Absorber Plate"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollectorPerformance:IntegralCollectorStorage`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["ICS Collector Type"] = None
        self._data["Gross Area"] = None
        self._data["Collector Water Volume"] = None
        self._data["Bottom Heat Loss Conductance"] = None
        self._data["Side Heat Loss Conductance"] = None
        self._data["Aspect Ratio"] = None
        self._data["Collector Side Height"] = None
        self._data["Thermal Mass of Absorber Plate"] = None
        self._data["Number of Covers"] = None
        self._data["Cover Spacing"] = None
        self._data["Refractive Index of Outer Cover"] = None
        self._data["Extinction Coefficient Times Thickness of Outer Cover"] = None
        self._data["Emissivity of Outer Cover"] = None
        self._data["Refractive Index of Inner Cover"] = None
        self._data["Extinction Coefficient Times Thickness of the inner Cover"] = None
        self._data["Emmissivity of Inner Cover"] = None
        self._data["Absorptance of Absorber Plate"] = None
        self._data["Emissivity of Absorber Plate"] = None
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
            self.ics_collector_type = None
        else:
            self.ics_collector_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gross_area = None
        else:
            self.gross_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collector_water_volume = None
        else:
            self.collector_water_volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.bottom_heat_loss_conductance = None
        else:
            self.bottom_heat_loss_conductance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.side_heat_loss_conductance = None
        else:
            self.side_heat_loss_conductance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.aspect_ratio = None
        else:
            self.aspect_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collector_side_height = None
        else:
            self.collector_side_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_mass_of_absorber_plate = None
        else:
            self.thermal_mass_of_absorber_plate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_covers = None
        else:
            self.number_of_covers = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cover_spacing = None
        else:
            self.cover_spacing = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refractive_index_of_outer_cover = None
        else:
            self.refractive_index_of_outer_cover = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.extinction_coefficient_times_thickness_of_outer_cover = None
        else:
            self.extinction_coefficient_times_thickness_of_outer_cover = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.emissivity_of_outer_cover = None
        else:
            self.emissivity_of_outer_cover = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.refractive_index_of_inner_cover = None
        else:
            self.refractive_index_of_inner_cover = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.extinction_coefficient_times_thickness_of_the_inner_cover = None
        else:
            self.extinction_coefficient_times_thickness_of_the_inner_cover = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.emmissivity_of_inner_cover = None
        else:
            self.emmissivity_of_inner_cover = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.absorptance_of_absorber_plate = None
        else:
            self.absorptance_of_absorber_plate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.emissivity_of_absorber_plate = None
        else:
            self.emissivity_of_absorber_plate = vals[i]
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.name`')
        self._data["Name"] = value

    @property
    def ics_collector_type(self):
        """Get ics_collector_type

        Returns:
            str: the value of `ics_collector_type` or None if not set
        """
        return self._data["ICS Collector Type"]

    @ics_collector_type.setter
    def ics_collector_type(self, value=None):
        """  Corresponds to IDD Field `ICS Collector Type`
        Currently only RectangularTank ICS collector type is available.

        Args:
            value (str): value for IDD Field `ICS Collector Type`
                Accepted values are:
                      - RectangularTank
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.ics_collector_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.ics_collector_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.ics_collector_type`')
            vals = {}
            vals["rectangulartank"] = "RectangularTank"
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
                                     'field `SolarCollectorPerformanceIntegralCollectorStorage.ics_collector_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorPerformanceIntegralCollectorStorage.ics_collector_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["ICS Collector Type"] = value

    @property
    def gross_area(self):
        """Get gross_area

        Returns:
            float: the value of `gross_area` or None if not set
        """
        return self._data["Gross Area"]

    @gross_area.setter
    def gross_area(self, value=None):
        """  Corresponds to IDD Field `Gross Area`

        Args:
            value (float): value for IDD Field `Gross Area`
                Units: m2
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.gross_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.gross_area`')
        self._data["Gross Area"] = value

    @property
    def collector_water_volume(self):
        """Get collector_water_volume

        Returns:
            float: the value of `collector_water_volume` or None if not set
        """
        return self._data["Collector Water Volume"]

    @collector_water_volume.setter
    def collector_water_volume(self, value=None):
        """  Corresponds to IDD Field `Collector Water Volume`

        Args:
            value (float): value for IDD Field `Collector Water Volume`
                Units: m3
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.collector_water_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.collector_water_volume`')
        self._data["Collector Water Volume"] = value

    @property
    def bottom_heat_loss_conductance(self):
        """Get bottom_heat_loss_conductance

        Returns:
            float: the value of `bottom_heat_loss_conductance` or None if not set
        """
        return self._data["Bottom Heat Loss Conductance"]

    @bottom_heat_loss_conductance.setter
    def bottom_heat_loss_conductance(self, value=0.4):
        """  Corresponds to IDD Field `Bottom Heat Loss Conductance`
        Heat loss conductance of the collector bottom insulation

        Args:
            value (float): value for IDD Field `Bottom Heat Loss Conductance`
                Units: W/m2-K
                Default value: 0.4
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.bottom_heat_loss_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.bottom_heat_loss_conductance`')
        self._data["Bottom Heat Loss Conductance"] = value

    @property
    def side_heat_loss_conductance(self):
        """Get side_heat_loss_conductance

        Returns:
            float: the value of `side_heat_loss_conductance` or None if not set
        """
        return self._data["Side Heat Loss Conductance"]

    @side_heat_loss_conductance.setter
    def side_heat_loss_conductance(self, value=0.6):
        """  Corresponds to IDD Field `Side Heat Loss Conductance`
        heat loss conductance of the collector side insulation

        Args:
            value (float): value for IDD Field `Side Heat Loss Conductance`
                Units: W/m2-K
                Default value: 0.6
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.side_heat_loss_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.side_heat_loss_conductance`')
        self._data["Side Heat Loss Conductance"] = value

    @property
    def aspect_ratio(self):
        """Get aspect_ratio

        Returns:
            float: the value of `aspect_ratio` or None if not set
        """
        return self._data["Aspect Ratio"]

    @aspect_ratio.setter
    def aspect_ratio(self, value=0.8):
        """  Corresponds to IDD Field `Aspect Ratio`
        This value is ratio of the width (short side) to length
        (long side of) of the collector.  Used to calculate the
        perimeter of the collector

        Args:
            value (float): value for IDD Field `Aspect Ratio`
                Units: m
                Default value: 0.8
                value > 0.5
                value < 1.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.aspect_ratio`'.format(value))
            if value <= 0.5:
                raise ValueError('value need to be greater 0.5 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.aspect_ratio`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.aspect_ratio`')
        self._data["Aspect Ratio"] = value

    @property
    def collector_side_height(self):
        """Get collector_side_height

        Returns:
            float: the value of `collector_side_height` or None if not set
        """
        return self._data["Collector Side Height"]

    @collector_side_height.setter
    def collector_side_height(self, value=0.2):
        """  Corresponds to IDD Field `Collector Side Height`
        This value is used to estimate collector side area for the heat
        loss calculation through the collector side

        Args:
            value (float): value for IDD Field `Collector Side Height`
                Units: m
                Default value: 0.2
                value > 0.0
                value < 0.3
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.collector_side_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.collector_side_height`')
            if value >= 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.collector_side_height`')
        self._data["Collector Side Height"] = value

    @property
    def thermal_mass_of_absorber_plate(self):
        """Get thermal_mass_of_absorber_plate

        Returns:
            float: the value of `thermal_mass_of_absorber_plate` or None if not set
        """
        return self._data["Thermal Mass of Absorber Plate"]

    @thermal_mass_of_absorber_plate.setter
    def thermal_mass_of_absorber_plate(self, value=0.0):
        """  Corresponds to IDD Field `Thermal Mass of Absorber Plate`
        Calculated from the specific heat, density and thickness
        of the absorber plate.

        Args:
            value (float): value for IDD Field `Thermal Mass of Absorber Plate`
                Units: J/m2-K
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.thermal_mass_of_absorber_plate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.thermal_mass_of_absorber_plate`')
        self._data["Thermal Mass of Absorber Plate"] = value

    @property
    def number_of_covers(self):
        """Get number_of_covers

        Returns:
            int: the value of `number_of_covers` or None if not set
        """
        return self._data["Number of Covers"]

    @number_of_covers.setter
    def number_of_covers(self, value=2):
        """  Corresponds to IDD Field `Number of Covers`
        Number of transparent covers. Common practice is to use low-iron
        glass as the outer cover and very thin transparent sheet such as
        Teflon as the inner cover.

        Args:
            value (int): value for IDD Field `Number of Covers`
                Default value: 2
                value >= 1
                value <= 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `SolarCollectorPerformanceIntegralCollectorStorage.number_of_covers`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `SolarCollectorPerformanceIntegralCollectorStorage.number_of_covers`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.number_of_covers`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.number_of_covers`')
        self._data["Number of Covers"] = value

    @property
    def cover_spacing(self):
        """Get cover_spacing

        Returns:
            float: the value of `cover_spacing` or None if not set
        """
        return self._data["Cover Spacing"]

    @cover_spacing.setter
    def cover_spacing(self, value=0.05):
        """  Corresponds to IDD Field `Cover Spacing`
        The gap between the transparent covers and between the inner cover
        and the absorber plate

        Args:
            value (float): value for IDD Field `Cover Spacing`
                Units: m
                Default value: 0.05
                value > 0.0
                value <= 0.2
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.cover_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.cover_spacing`')
            if value > 0.2:
                raise ValueError('value need to be smaller 0.2 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.cover_spacing`')
        self._data["Cover Spacing"] = value

    @property
    def refractive_index_of_outer_cover(self):
        """Get refractive_index_of_outer_cover

        Returns:
            float: the value of `refractive_index_of_outer_cover` or None if not set
        """
        return self._data["Refractive Index of Outer Cover"]

    @refractive_index_of_outer_cover.setter
    def refractive_index_of_outer_cover(self, value=1.526):
        """  Corresponds to IDD Field `Refractive Index of Outer Cover`
        Refractive index of outer cover. Typically low-iron glass is used
        as the outer cover material, and used as the default outer cover
        with a vallue of 1.526.

        Args:
            value (float): value for IDD Field `Refractive Index of Outer Cover`
                Units: dimensionless
                Default value: 1.526
                value >= 1.0
                value <= 2.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.refractive_index_of_outer_cover`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.refractive_index_of_outer_cover`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.refractive_index_of_outer_cover`')
        self._data["Refractive Index of Outer Cover"] = value

    @property
    def extinction_coefficient_times_thickness_of_outer_cover(self):
        """Get extinction_coefficient_times_thickness_of_outer_cover

        Returns:
            float: the value of `extinction_coefficient_times_thickness_of_outer_cover` or None if not set
        """
        return self._data["Extinction Coefficient Times Thickness of Outer Cover"]

    @extinction_coefficient_times_thickness_of_outer_cover.setter
    def extinction_coefficient_times_thickness_of_outer_cover(self, value=0.045):
        """  Corresponds to IDD Field `Extinction Coefficient Times Thickness of Outer Cover`
        Clear glass has extinction coefficient of about 15 [1/m]
        and with thickness of 3.0mm, the product of the extinction
        coefficient and thickness becomes 0.045 (=15 * 0.003)

        Args:
            value (float): value for IDD Field `Extinction Coefficient Times Thickness of Outer Cover`
                Units: dimensionless
                Default value: 0.045
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.extinction_coefficient_times_thickness_of_outer_cover`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.extinction_coefficient_times_thickness_of_outer_cover`')
        self._data["Extinction Coefficient Times Thickness of Outer Cover"] = value

    @property
    def emissivity_of_outer_cover(self):
        """Get emissivity_of_outer_cover

        Returns:
            float: the value of `emissivity_of_outer_cover` or None if not set
        """
        return self._data["Emissivity of Outer Cover"]

    @emissivity_of_outer_cover.setter
    def emissivity_of_outer_cover(self, value=0.88):
        """  Corresponds to IDD Field `Emissivity of Outer Cover`
        Thermal emissivity of the outer cover, commonly glass is used as
        the out collector cover material.

        Args:
            value (float): value for IDD Field `Emissivity of Outer Cover`
                Units: dimensionless
                Default value: 0.88
                value > 0.0
                value < 1.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.emissivity_of_outer_cover`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.emissivity_of_outer_cover`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.emissivity_of_outer_cover`')
        self._data["Emissivity of Outer Cover"] = value

    @property
    def refractive_index_of_inner_cover(self):
        """Get refractive_index_of_inner_cover

        Returns:
            float: the value of `refractive_index_of_inner_cover` or None if not set
        """
        return self._data["Refractive Index of Inner Cover"]

    @refractive_index_of_inner_cover.setter
    def refractive_index_of_inner_cover(self, value=1.37):
        """  Corresponds to IDD Field `Refractive Index of Inner Cover`
        Typical material is very thin sheet of Teflon (PTFE). The default
        value is refractive index of Teflon.

        Args:
            value (float): value for IDD Field `Refractive Index of Inner Cover`
                Units: dimensionless
                Default value: 1.37
                value >= 1.0
                value <= 2.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.refractive_index_of_inner_cover`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.refractive_index_of_inner_cover`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.refractive_index_of_inner_cover`')
        self._data["Refractive Index of Inner Cover"] = value

    @property
    def extinction_coefficient_times_thickness_of_the_inner_cover(self):
        """Get extinction_coefficient_times_thickness_of_the_inner_cover

        Returns:
            float: the value of `extinction_coefficient_times_thickness_of_the_inner_cover` or None if not set
        """
        return self._data["Extinction Coefficient Times Thickness of the inner Cover"]

    @extinction_coefficient_times_thickness_of_the_inner_cover.setter
    def extinction_coefficient_times_thickness_of_the_inner_cover(self, value=0.008):
        """  Corresponds to IDD Field `Extinction Coefficient Times Thickness of the inner Cover`
        Default inner cover is very thin sheet of Teflon with
        extinction coefficient of approximately 40.0 and a thickness
        0.2mm yields a default value of 0.008.

        Args:
            value (float): value for IDD Field `Extinction Coefficient Times Thickness of the inner Cover`
                Units: dimensionless
                Default value: 0.008
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.extinction_coefficient_times_thickness_of_the_inner_cover`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.extinction_coefficient_times_thickness_of_the_inner_cover`')
        self._data["Extinction Coefficient Times Thickness of the inner Cover"] = value

    @property
    def emmissivity_of_inner_cover(self):
        """Get emmissivity_of_inner_cover

        Returns:
            float: the value of `emmissivity_of_inner_cover` or None if not set
        """
        return self._data["Emmissivity of Inner Cover"]

    @emmissivity_of_inner_cover.setter
    def emmissivity_of_inner_cover(self, value=0.88):
        """  Corresponds to IDD Field `Emmissivity of Inner Cover`
        Thermal emissivity of the inner cover matrial

        Args:
            value (float): value for IDD Field `Emmissivity of Inner Cover`
                Units: dimensionless
                Default value: 0.88
                value > 0.0
                value < 1.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.emmissivity_of_inner_cover`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.emmissivity_of_inner_cover`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.emmissivity_of_inner_cover`')
        self._data["Emmissivity of Inner Cover"] = value

    @property
    def absorptance_of_absorber_plate(self):
        """Get absorptance_of_absorber_plate

        Returns:
            float: the value of `absorptance_of_absorber_plate` or None if not set
        """
        return self._data["Absorptance of Absorber Plate"]

    @absorptance_of_absorber_plate.setter
    def absorptance_of_absorber_plate(self, value=0.96):
        """  Corresponds to IDD Field `Absorptance of Absorber Plate`
        The absober plate solar absorptance.  Copper is assumed as
        the default absorber plate.

        Args:
            value (float): value for IDD Field `Absorptance of Absorber Plate`
                Units: dimensionless
                Default value: 0.96
                value > 0.0
                value < 1.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.absorptance_of_absorber_plate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.absorptance_of_absorber_plate`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.absorptance_of_absorber_plate`')
        self._data["Absorptance of Absorber Plate"] = value

    @property
    def emissivity_of_absorber_plate(self):
        """Get emissivity_of_absorber_plate

        Returns:
            float: the value of `emissivity_of_absorber_plate` or None if not set
        """
        return self._data["Emissivity of Absorber Plate"]

    @emissivity_of_absorber_plate.setter
    def emissivity_of_absorber_plate(self, value=0.3):
        """  Corresponds to IDD Field `Emissivity of Absorber Plate`
        Thermal emissivity of the absorber plate

        Args:
            value (float): value for IDD Field `Emissivity of Absorber Plate`
                Units: dimensionless
                Default value: 0.3
                value > 0.0
                value < 1.0
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
                                 ' for field `SolarCollectorPerformanceIntegralCollectorStorage.emissivity_of_absorber_plate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.emissivity_of_absorber_plate`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorPerformanceIntegralCollectorStorage.emissivity_of_absorber_plate`')
        self._data["Emissivity of Absorber Plate"] = value

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
                    raise ValueError("Required field SolarCollectorPerformanceIntegralCollectorStorage:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorPerformanceIntegralCollectorStorage:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorPerformanceIntegralCollectorStorage: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorPerformanceIntegralCollectorStorage: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorUnglazedTranspired(object):
    """ Corresponds to IDD object `SolarCollector:UnglazedTranspired`
        Unglazed transpired solar collector (UTSC) used to condition outdoor air. This type of
        collector is generally used to heat air drawn through perforated absorbers and also
        recover heat conducted out through the underlying surfae. This object represents a
        single collector attached to one or more building or shading surfaces and to one or
        more outdoor air systems.
    """
    internal_name = "SolarCollector:UnglazedTranspired"
    field_count = 22
    required_fields = ["Name", "Boundary Conditions Model Name", "Diameter of Perforations in Collector", "Distance Between Perforations in Collector", "Thermal Emissivity of Collector Surface", "Solar Absorbtivity of Collector Surface", "Effective Overall Height of Collector", "Effective Gap Thickness of Plenum Behind Collector", "Effective Cross Section Area of Plenum Behind Collector", "Roughness of Collector"]
    extensible_fields = 1
    format = None
    min_fields = 23
    extensible_keys = ["Surface 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollector:UnglazedTranspired`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Boundary Conditions Model Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Setpoint Node Name"] = None
        self._data["Zone Node Name"] = None
        self._data["Free Heating Setpoint Schedule Name"] = None
        self._data["Diameter of Perforations in Collector"] = None
        self._data["Distance Between Perforations in Collector"] = None
        self._data["Thermal Emissivity of Collector Surface"] = None
        self._data["Solar Absorbtivity of Collector Surface"] = None
        self._data["Effective Overall Height of Collector"] = None
        self._data["Effective Gap Thickness of Plenum Behind Collector"] = None
        self._data["Effective Cross Section Area of Plenum Behind Collector"] = None
        self._data["Hole Layout Pattern for Pitch"] = None
        self._data["Heat Exchange Effectiveness Correlation"] = None
        self._data["Ratio of Actual Collector Surface Area to Projected Surface Area"] = None
        self._data["Roughness of Collector"] = None
        self._data["Collector Thickness"] = None
        self._data["Effectiveness for Perforations with Respect to Wind"] = None
        self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = None
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
            self.boundary_conditions_model_name = None
        else:
            self.boundary_conditions_model_name = vals[i]
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
            self.setpoint_node_name = None
        else:
            self.setpoint_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.free_heating_setpoint_schedule_name = None
        else:
            self.free_heating_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diameter_of_perforations_in_collector = None
        else:
            self.diameter_of_perforations_in_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.distance_between_perforations_in_collector = None
        else:
            self.distance_between_perforations_in_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_emissivity_of_collector_surface = None
        else:
            self.thermal_emissivity_of_collector_surface = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.solar_absorbtivity_of_collector_surface = None
        else:
            self.solar_absorbtivity_of_collector_surface = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effective_overall_height_of_collector = None
        else:
            self.effective_overall_height_of_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effective_gap_thickness_of_plenum_behind_collector = None
        else:
            self.effective_gap_thickness_of_plenum_behind_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effective_cross_section_area_of_plenum_behind_collector = None
        else:
            self.effective_cross_section_area_of_plenum_behind_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hole_layout_pattern_for_pitch = None
        else:
            self.hole_layout_pattern_for_pitch = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_exchange_effectiveness_correlation = None
        else:
            self.heat_exchange_effectiveness_correlation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_actual_collector_surface_area_to_projected_surface_area = None
        else:
            self.ratio_of_actual_collector_surface_area_to_projected_surface_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.roughness_of_collector = None
        else:
            self.roughness_of_collector = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.collector_thickness = None
        else:
            self.collector_thickness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effectiveness_for_perforations_with_respect_to_wind = None
        else:
            self.effectiveness_for_perforations_with_respect_to_wind = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = None
        else:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = vals[i]
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
                                 ' for field `SolarCollectorUnglazedTranspired.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.name`')
        self._data["Name"] = value

    @property
    def boundary_conditions_model_name(self):
        """Get boundary_conditions_model_name

        Returns:
            str: the value of `boundary_conditions_model_name` or None if not set
        """
        return self._data["Boundary Conditions Model Name"]

    @boundary_conditions_model_name.setter
    def boundary_conditions_model_name(self, value=None):
        """  Corresponds to IDD Field `Boundary Conditions Model Name`
        Enter the name of a SurfaceProperty:OtherSideConditionsModel object

        Args:
            value (str): value for IDD Field `Boundary Conditions Model Name`
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
                                 ' for field `SolarCollectorUnglazedTranspired.boundary_conditions_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.boundary_conditions_model_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.boundary_conditions_model_name`')
        self._data["Boundary Conditions Model Name"] = value

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
        Availability schedule name for this collector. Schedule value > 0 means it is available.
        If this field is blank, the collector is always available.

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
                                 ' for field `SolarCollectorUnglazedTranspired.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.availability_schedule_name`')
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
        required field if no SolarCollector:UnglazedTranspired:Multisystem

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
                                 ' for field `SolarCollectorUnglazedTranspired.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.inlet_node_name`')
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
        required field if no SolarCollector:UnglazedTranspired:Multisystem

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
                                 ' for field `SolarCollectorUnglazedTranspired.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def setpoint_node_name(self):
        """Get setpoint_node_name

        Returns:
            str: the value of `setpoint_node_name` or None if not set
        """
        return self._data["Setpoint Node Name"]

    @setpoint_node_name.setter
    def setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `Setpoint Node Name`
        This node is where the mixed air setpoint is determined.
        required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `Setpoint Node Name`
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
                                 ' for field `SolarCollectorUnglazedTranspired.setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.setpoint_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.setpoint_node_name`')
        self._data["Setpoint Node Name"] = value

    @property
    def zone_node_name(self):
        """Get zone_node_name

        Returns:
            str: the value of `zone_node_name` or None if not set
        """
        return self._data["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Node Name`
        This node is used to indentify the affected zone
        required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `Zone Node Name`
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
                                 ' for field `SolarCollectorUnglazedTranspired.zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.zone_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.zone_node_name`')
        self._data["Zone Node Name"] = value

    @property
    def free_heating_setpoint_schedule_name(self):
        """Get free_heating_setpoint_schedule_name

        Returns:
            str: the value of `free_heating_setpoint_schedule_name` or None if not set
        """
        return self._data["Free Heating Setpoint Schedule Name"]

    @free_heating_setpoint_schedule_name.setter
    def free_heating_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Free Heating Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Free Heating Setpoint Schedule Name`
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
                                 ' for field `SolarCollectorUnglazedTranspired.free_heating_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.free_heating_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.free_heating_setpoint_schedule_name`')
        self._data["Free Heating Setpoint Schedule Name"] = value

    @property
    def diameter_of_perforations_in_collector(self):
        """Get diameter_of_perforations_in_collector

        Returns:
            float: the value of `diameter_of_perforations_in_collector` or None if not set
        """
        return self._data["Diameter of Perforations in Collector"]

    @diameter_of_perforations_in_collector.setter
    def diameter_of_perforations_in_collector(self, value=None):
        """  Corresponds to IDD Field `Diameter of Perforations in Collector`

        Args:
            value (float): value for IDD Field `Diameter of Perforations in Collector`
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
                                 ' for field `SolarCollectorUnglazedTranspired.diameter_of_perforations_in_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.diameter_of_perforations_in_collector`')
        self._data["Diameter of Perforations in Collector"] = value

    @property
    def distance_between_perforations_in_collector(self):
        """Get distance_between_perforations_in_collector

        Returns:
            float: the value of `distance_between_perforations_in_collector` or None if not set
        """
        return self._data["Distance Between Perforations in Collector"]

    @distance_between_perforations_in_collector.setter
    def distance_between_perforations_in_collector(self, value=None):
        """  Corresponds to IDD Field `Distance Between Perforations in Collector`

        Args:
            value (float): value for IDD Field `Distance Between Perforations in Collector`
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
                                 ' for field `SolarCollectorUnglazedTranspired.distance_between_perforations_in_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.distance_between_perforations_in_collector`')
        self._data["Distance Between Perforations in Collector"] = value

    @property
    def thermal_emissivity_of_collector_surface(self):
        """Get thermal_emissivity_of_collector_surface

        Returns:
            float: the value of `thermal_emissivity_of_collector_surface` or None if not set
        """
        return self._data["Thermal Emissivity of Collector Surface"]

    @thermal_emissivity_of_collector_surface.setter
    def thermal_emissivity_of_collector_surface(self, value=None):
        """  Corresponds to IDD Field `Thermal Emissivity of Collector Surface`

        Args:
            value (float): value for IDD Field `Thermal Emissivity of Collector Surface`
                Units: dimensionless
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
                                 ' for field `SolarCollectorUnglazedTranspired.thermal_emissivity_of_collector_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.thermal_emissivity_of_collector_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorUnglazedTranspired.thermal_emissivity_of_collector_surface`')
        self._data["Thermal Emissivity of Collector Surface"] = value

    @property
    def solar_absorbtivity_of_collector_surface(self):
        """Get solar_absorbtivity_of_collector_surface

        Returns:
            float: the value of `solar_absorbtivity_of_collector_surface` or None if not set
        """
        return self._data["Solar Absorbtivity of Collector Surface"]

    @solar_absorbtivity_of_collector_surface.setter
    def solar_absorbtivity_of_collector_surface(self, value=None):
        """  Corresponds to IDD Field `Solar Absorbtivity of Collector Surface`

        Args:
            value (float): value for IDD Field `Solar Absorbtivity of Collector Surface`
                Units: dimensionless
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
                                 ' for field `SolarCollectorUnglazedTranspired.solar_absorbtivity_of_collector_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.solar_absorbtivity_of_collector_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SolarCollectorUnglazedTranspired.solar_absorbtivity_of_collector_surface`')
        self._data["Solar Absorbtivity of Collector Surface"] = value

    @property
    def effective_overall_height_of_collector(self):
        """Get effective_overall_height_of_collector

        Returns:
            float: the value of `effective_overall_height_of_collector` or None if not set
        """
        return self._data["Effective Overall Height of Collector"]

    @effective_overall_height_of_collector.setter
    def effective_overall_height_of_collector(self, value=None):
        """  Corresponds to IDD Field `Effective Overall Height of Collector`

        Args:
            value (float): value for IDD Field `Effective Overall Height of Collector`
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
                                 ' for field `SolarCollectorUnglazedTranspired.effective_overall_height_of_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.effective_overall_height_of_collector`')
        self._data["Effective Overall Height of Collector"] = value

    @property
    def effective_gap_thickness_of_plenum_behind_collector(self):
        """Get effective_gap_thickness_of_plenum_behind_collector

        Returns:
            float: the value of `effective_gap_thickness_of_plenum_behind_collector` or None if not set
        """
        return self._data["Effective Gap Thickness of Plenum Behind Collector"]

    @effective_gap_thickness_of_plenum_behind_collector.setter
    def effective_gap_thickness_of_plenum_behind_collector(self, value=None):
        """  Corresponds to IDD Field `Effective Gap Thickness of Plenum Behind Collector`
        if corrugated, use average depth

        Args:
            value (float): value for IDD Field `Effective Gap Thickness of Plenum Behind Collector`
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
                                 ' for field `SolarCollectorUnglazedTranspired.effective_gap_thickness_of_plenum_behind_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.effective_gap_thickness_of_plenum_behind_collector`')
        self._data["Effective Gap Thickness of Plenum Behind Collector"] = value

    @property
    def effective_cross_section_area_of_plenum_behind_collector(self):
        """Get effective_cross_section_area_of_plenum_behind_collector

        Returns:
            float: the value of `effective_cross_section_area_of_plenum_behind_collector` or None if not set
        """
        return self._data["Effective Cross Section Area of Plenum Behind Collector"]

    @effective_cross_section_area_of_plenum_behind_collector.setter
    def effective_cross_section_area_of_plenum_behind_collector(self, value=None):
        """  Corresponds to IDD Field `Effective Cross Section Area of Plenum Behind Collector`
        if corrugated, use average depth

        Args:
            value (float): value for IDD Field `Effective Cross Section Area of Plenum Behind Collector`
                Units: m2
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
                                 ' for field `SolarCollectorUnglazedTranspired.effective_cross_section_area_of_plenum_behind_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.effective_cross_section_area_of_plenum_behind_collector`')
        self._data["Effective Cross Section Area of Plenum Behind Collector"] = value

    @property
    def hole_layout_pattern_for_pitch(self):
        """Get hole_layout_pattern_for_pitch

        Returns:
            str: the value of `hole_layout_pattern_for_pitch` or None if not set
        """
        return self._data["Hole Layout Pattern for Pitch"]

    @hole_layout_pattern_for_pitch.setter
    def hole_layout_pattern_for_pitch(self, value="Square"):
        """  Corresponds to IDD Field `Hole Layout Pattern for Pitch`

        Args:
            value (str): value for IDD Field `Hole Layout Pattern for Pitch`
                Accepted values are:
                      - Triangle
                      - Square
                Default value: Square
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
                                 ' for field `SolarCollectorUnglazedTranspired.hole_layout_pattern_for_pitch`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.hole_layout_pattern_for_pitch`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.hole_layout_pattern_for_pitch`')
            vals = {}
            vals["triangle"] = "Triangle"
            vals["square"] = "Square"
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
                                     'field `SolarCollectorUnglazedTranspired.hole_layout_pattern_for_pitch`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorUnglazedTranspired.hole_layout_pattern_for_pitch`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Hole Layout Pattern for Pitch"] = value

    @property
    def heat_exchange_effectiveness_correlation(self):
        """Get heat_exchange_effectiveness_correlation

        Returns:
            str: the value of `heat_exchange_effectiveness_correlation` or None if not set
        """
        return self._data["Heat Exchange Effectiveness Correlation"]

    @heat_exchange_effectiveness_correlation.setter
    def heat_exchange_effectiveness_correlation(self, value="Kutscher1994"):
        """  Corresponds to IDD Field `Heat Exchange Effectiveness Correlation`

        Args:
            value (str): value for IDD Field `Heat Exchange Effectiveness Correlation`
                Accepted values are:
                      - Kutscher1994
                      - VanDeckerHollandsBrunger2001
                Default value: Kutscher1994
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
                                 ' for field `SolarCollectorUnglazedTranspired.heat_exchange_effectiveness_correlation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.heat_exchange_effectiveness_correlation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.heat_exchange_effectiveness_correlation`')
            vals = {}
            vals["kutscher1994"] = "Kutscher1994"
            vals["vandeckerhollandsbrunger2001"] = "VanDeckerHollandsBrunger2001"
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
                                     'field `SolarCollectorUnglazedTranspired.heat_exchange_effectiveness_correlation`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorUnglazedTranspired.heat_exchange_effectiveness_correlation`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Heat Exchange Effectiveness Correlation"] = value

    @property
    def ratio_of_actual_collector_surface_area_to_projected_surface_area(self):
        """Get ratio_of_actual_collector_surface_area_to_projected_surface_area

        Returns:
            float: the value of `ratio_of_actual_collector_surface_area_to_projected_surface_area` or None if not set
        """
        return self._data["Ratio of Actual Collector Surface Area to Projected Surface Area"]

    @ratio_of_actual_collector_surface_area_to_projected_surface_area.setter
    def ratio_of_actual_collector_surface_area_to_projected_surface_area(self, value=1.0):
        """  Corresponds to IDD Field `Ratio of Actual Collector Surface Area to Projected Surface Area`
        This parameter is used to help account for corrugations in the collector

        Args:
            value (float): value for IDD Field `Ratio of Actual Collector Surface Area to Projected Surface Area`
                Units: dimensionless
                Default value: 1.0
                value >= 1.0
                value <= 2.0
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
                                 ' for field `SolarCollectorUnglazedTranspired.ratio_of_actual_collector_surface_area_to_projected_surface_area`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `SolarCollectorUnglazedTranspired.ratio_of_actual_collector_surface_area_to_projected_surface_area`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `SolarCollectorUnglazedTranspired.ratio_of_actual_collector_surface_area_to_projected_surface_area`')
        self._data["Ratio of Actual Collector Surface Area to Projected Surface Area"] = value

    @property
    def roughness_of_collector(self):
        """Get roughness_of_collector

        Returns:
            str: the value of `roughness_of_collector` or None if not set
        """
        return self._data["Roughness of Collector"]

    @roughness_of_collector.setter
    def roughness_of_collector(self, value=None):
        """  Corresponds to IDD Field `Roughness of Collector`

        Args:
            value (str): value for IDD Field `Roughness of Collector`
                Accepted values are:
                      - VeryRough
                      - Rough
                      - MediumRough
                      - MediumSmooth
                      - Smooth
                      - VerySmooth
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
                                 ' for field `SolarCollectorUnglazedTranspired.roughness_of_collector`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.roughness_of_collector`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.roughness_of_collector`')
            vals = {}
            vals["veryrough"] = "VeryRough"
            vals["rough"] = "Rough"
            vals["mediumrough"] = "MediumRough"
            vals["mediumsmooth"] = "MediumSmooth"
            vals["smooth"] = "Smooth"
            vals["verysmooth"] = "VerySmooth"
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
                                     'field `SolarCollectorUnglazedTranspired.roughness_of_collector`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SolarCollectorUnglazedTranspired.roughness_of_collector`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Roughness of Collector"] = value

    @property
    def collector_thickness(self):
        """Get collector_thickness

        Returns:
            float: the value of `collector_thickness` or None if not set
        """
        return self._data["Collector Thickness"]

    @collector_thickness.setter
    def collector_thickness(self, value=None):
        """  Corresponds to IDD Field `Collector Thickness`
        Collector thickness is not required for Kutscher correlation
        Collector thickness is required for Van Decker et al. correlation

        Args:
            value (float): value for IDD Field `Collector Thickness`
                Units: m
                value >= 0.0005
                value <= 0.007
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
                                 ' for field `SolarCollectorUnglazedTranspired.collector_thickness`'.format(value))
            if value < 0.0005:
                raise ValueError('value need to be greater or equal 0.0005 '
                                 'for field `SolarCollectorUnglazedTranspired.collector_thickness`')
            if value > 0.007:
                raise ValueError('value need to be smaller 0.007 '
                                 'for field `SolarCollectorUnglazedTranspired.collector_thickness`')
        self._data["Collector Thickness"] = value

    @property
    def effectiveness_for_perforations_with_respect_to_wind(self):
        """Get effectiveness_for_perforations_with_respect_to_wind

        Returns:
            float: the value of `effectiveness_for_perforations_with_respect_to_wind` or None if not set
        """
        return self._data["Effectiveness for Perforations with Respect to Wind"]

    @effectiveness_for_perforations_with_respect_to_wind.setter
    def effectiveness_for_perforations_with_respect_to_wind(self, value=0.25):
        """  Corresponds to IDD Field `Effectiveness for Perforations with Respect to Wind`
        Cv

        Args:
            value (float): value for IDD Field `Effectiveness for Perforations with Respect to Wind`
                Units: dimensionless
                Default value: 0.25
                value > 0.0
                value <= 1.5
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
                                 ' for field `SolarCollectorUnglazedTranspired.effectiveness_for_perforations_with_respect_to_wind`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.effectiveness_for_perforations_with_respect_to_wind`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `SolarCollectorUnglazedTranspired.effectiveness_for_perforations_with_respect_to_wind`')
        self._data["Effectiveness for Perforations with Respect to Wind"] = value

    @property
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self):
        """Get discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow

        Returns:
            float: the value of `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow` or None if not set
        """
        return self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"]

    @discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow.setter
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self, value=0.65):
        """  Corresponds to IDD Field `Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow`
        Cd

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow`
                Units: dimensionless
                Default value: 0.65
                value > 0.0
                value <= 1.5
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
                                 ' for field `SolarCollectorUnglazedTranspired.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SolarCollectorUnglazedTranspired.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `SolarCollectorUnglazedTranspired.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')
        self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
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
                                 ' for field `SolarCollectorUnglazedTranspired.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspired.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspired.surface_1_name`')
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
                    raise ValueError("Required field SolarCollectorUnglazedTranspired:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorUnglazedTranspired:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorUnglazedTranspired: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorUnglazedTranspired: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SolarCollectorUnglazedTranspiredMultisystem(object):
    """ Corresponds to IDD object `SolarCollector:UnglazedTranspired:Multisystem`
        quad-tuples of inlet, outlet, control, and zone nodes
        for multiple different outdoor air systems attached to same collector
    """
    internal_name = "SolarCollector:UnglazedTranspired:Multisystem"
    field_count = 1
    required_fields = ["Solar Collector Name"]
    extensible_fields = 4
    format = None
    min_fields = 0
    extensible_keys = ["Outdoor Air System 1 Collector Inlet Node", "Outdoor Air System 1 Collector Outlet Node", "Outdoor Air System 1 Mixed Air Node", "Outdoor Air System 1 Zone Node"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SolarCollector:UnglazedTranspired:Multisystem`
        """
        self._data = OrderedDict()
        self._data["Solar Collector Name"] = None
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
            self.solar_collector_name = None
        else:
            self.solar_collector_name = vals[i]
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
    def solar_collector_name(self):
        """Get solar_collector_name

        Returns:
            str: the value of `solar_collector_name` or None if not set
        """
        return self._data["Solar Collector Name"]

    @solar_collector_name.setter
    def solar_collector_name(self, value=None):
        """  Corresponds to IDD Field `Solar Collector Name`
        Enter the name of a SolarCollector:UnglazedTranspired object.

        Args:
            value (str): value for IDD Field `Solar Collector Name`
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
                                 ' for field `SolarCollectorUnglazedTranspiredMultisystem.solar_collector_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.solar_collector_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.solar_collector_name`')
        self._data["Solar Collector Name"] = value

    def add_extensible(self,
                       outdoor_air_system_1_collector_inlet_node=None,
                       outdoor_air_system_1_collector_outlet_node=None,
                       outdoor_air_system_1_mixed_air_node=None,
                       outdoor_air_system_1_zone_node=None,
                       ):
        """ Add values for extensible fields

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
        vals.append(self._check_outdoor_air_system_1_collector_inlet_node(outdoor_air_system_1_collector_inlet_node))
        vals.append(self._check_outdoor_air_system_1_collector_outlet_node(outdoor_air_system_1_collector_outlet_node))
        vals.append(self._check_outdoor_air_system_1_mixed_air_node(outdoor_air_system_1_mixed_air_node))
        vals.append(self._check_outdoor_air_system_1_zone_node(outdoor_air_system_1_zone_node))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_outdoor_air_system_1_collector_inlet_node(self, value):
        """ Validates falue of field `Outdoor Air System 1 Collector Inlet Node`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_collector_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_collector_inlet_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_collector_inlet_node`')
        return value

    def _check_outdoor_air_system_1_collector_outlet_node(self, value):
        """ Validates falue of field `Outdoor Air System 1 Collector Outlet Node`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_collector_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_collector_outlet_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_collector_outlet_node`')
        return value

    def _check_outdoor_air_system_1_mixed_air_node(self, value):
        """ Validates falue of field `Outdoor Air System 1 Mixed Air Node`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_mixed_air_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_mixed_air_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_mixed_air_node`')
        return value

    def _check_outdoor_air_system_1_zone_node(self, value):
        """ Validates falue of field `Outdoor Air System 1 Zone Node`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_zone_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_zone_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SolarCollectorUnglazedTranspiredMultisystem.outdoor_air_system_1_zone_node`')
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
                    raise ValueError("Required field SolarCollectorUnglazedTranspiredMultisystem:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SolarCollectorUnglazedTranspiredMultisystem:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SolarCollectorUnglazedTranspiredMultisystem: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SolarCollectorUnglazedTranspiredMultisystem: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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