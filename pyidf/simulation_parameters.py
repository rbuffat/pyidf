from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class Version(object):
    """ Corresponds to IDD object `Version`
        Specifies the EnergyPlus version of the IDF file.
    """
    internal_name = "Version"
    field_count = 1
    required_fields = ["Version Identifier"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Version`
        """
        self._data = OrderedDict()
        self._data["Version Identifier"] = None
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
            self.version_identifier = None
        else:
            self.version_identifier = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def version_identifier(self):
        """Get version_identifier

        Returns:
            str: the value of `version_identifier` or None if not set
        """
        return self._data["Version Identifier"]

    @version_identifier.setter
    def version_identifier(self, value="7.0"):
        """  Corresponds to IDD Field `Version Identifier`

        Args:
            value (str): value for IDD Field `Version Identifier`
                Default value: 7.0
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
                                 ' for field `Version.version_identifier`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Version.version_identifier`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Version.version_identifier`')
        self._data["Version Identifier"] = value

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
                    raise ValueError("Required field Version:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Version:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Version: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Version: {} / {}".format(out_fields,
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

class SimulationControl(object):
    """ Corresponds to IDD object `SimulationControl`
        Note that the following 3 fields are related to the Sizing:Zone, Sizing:System,
        and Sizing:Plant objects.  Having these fields set to Yes but no corresponding
        Sizing object will not cause the sizing to be done. However, having any of these
        fields set to No, the corresponding Sizing object is ignored.
        Note also, if you want to do system sizing, you must also do zone sizing in the same
        run or an error will result.
    """
    internal_name = "SimulationControl"
    field_count = 5
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SimulationControl`
        """
        self._data = OrderedDict()
        self._data["Do Zone Sizing Calculation"] = None
        self._data["Do System Sizing Calculation"] = None
        self._data["Do Plant Sizing Calculation"] = None
        self._data["Run Simulation for Sizing Periods"] = None
        self._data["Run Simulation for Weather File Run Periods"] = None
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
            self.do_zone_sizing_calculation = None
        else:
            self.do_zone_sizing_calculation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.do_system_sizing_calculation = None
        else:
            self.do_system_sizing_calculation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.do_plant_sizing_calculation = None
        else:
            self.do_plant_sizing_calculation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.run_simulation_for_sizing_periods = None
        else:
            self.run_simulation_for_sizing_periods = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.run_simulation_for_weather_file_run_periods = None
        else:
            self.run_simulation_for_weather_file_run_periods = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def do_zone_sizing_calculation(self):
        """Get do_zone_sizing_calculation

        Returns:
            str: the value of `do_zone_sizing_calculation` or None if not set
        """
        return self._data["Do Zone Sizing Calculation"]

    @do_zone_sizing_calculation.setter
    def do_zone_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `Do Zone Sizing Calculation`
        If Yes, Zone sizing is accomplished from corresponding Sizing:Zone objects
        and autosize fields.

        Args:
            value (str): value for IDD Field `Do Zone Sizing Calculation`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `SimulationControl.do_zone_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SimulationControl.do_zone_sizing_calculation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SimulationControl.do_zone_sizing_calculation`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `SimulationControl.do_zone_sizing_calculation`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SimulationControl.do_zone_sizing_calculation`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Do Zone Sizing Calculation"] = value

    @property
    def do_system_sizing_calculation(self):
        """Get do_system_sizing_calculation

        Returns:
            str: the value of `do_system_sizing_calculation` or None if not set
        """
        return self._data["Do System Sizing Calculation"]

    @do_system_sizing_calculation.setter
    def do_system_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `Do System Sizing Calculation`
        If Yes, System sizing is accomplished from corresponding Sizing:System objects
        and autosize fields.
        If Yes, Zone sizing (previous field) must also be Yes.

        Args:
            value (str): value for IDD Field `Do System Sizing Calculation`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `SimulationControl.do_system_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SimulationControl.do_system_sizing_calculation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SimulationControl.do_system_sizing_calculation`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `SimulationControl.do_system_sizing_calculation`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SimulationControl.do_system_sizing_calculation`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Do System Sizing Calculation"] = value

    @property
    def do_plant_sizing_calculation(self):
        """Get do_plant_sizing_calculation

        Returns:
            str: the value of `do_plant_sizing_calculation` or None if not set
        """
        return self._data["Do Plant Sizing Calculation"]

    @do_plant_sizing_calculation.setter
    def do_plant_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `Do Plant Sizing Calculation`
        If Yes, Plant sizing is accomplished from corresponding Sizing:Plant objects
        and autosize fields.

        Args:
            value (str): value for IDD Field `Do Plant Sizing Calculation`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `SimulationControl.do_plant_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SimulationControl.do_plant_sizing_calculation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SimulationControl.do_plant_sizing_calculation`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `SimulationControl.do_plant_sizing_calculation`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SimulationControl.do_plant_sizing_calculation`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Do Plant Sizing Calculation"] = value

    @property
    def run_simulation_for_sizing_periods(self):
        """Get run_simulation_for_sizing_periods

        Returns:
            str: the value of `run_simulation_for_sizing_periods` or None if not set
        """
        return self._data["Run Simulation for Sizing Periods"]

    @run_simulation_for_sizing_periods.setter
    def run_simulation_for_sizing_periods(self, value="Yes"):
        """  Corresponds to IDD Field `Run Simulation for Sizing Periods`
        If Yes, SizingPeriod:* objects are executed and results from those may be displayed..

        Args:
            value (str): value for IDD Field `Run Simulation for Sizing Periods`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 ' for field `SimulationControl.run_simulation_for_sizing_periods`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SimulationControl.run_simulation_for_sizing_periods`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SimulationControl.run_simulation_for_sizing_periods`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `SimulationControl.run_simulation_for_sizing_periods`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SimulationControl.run_simulation_for_sizing_periods`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Run Simulation for Sizing Periods"] = value

    @property
    def run_simulation_for_weather_file_run_periods(self):
        """Get run_simulation_for_weather_file_run_periods

        Returns:
            str: the value of `run_simulation_for_weather_file_run_periods` or None if not set
        """
        return self._data["Run Simulation for Weather File Run Periods"]

    @run_simulation_for_weather_file_run_periods.setter
    def run_simulation_for_weather_file_run_periods(self, value="Yes"):
        """  Corresponds to IDD Field `Run Simulation for Weather File Run Periods`
        If Yes, RunPeriod:* objects are executed and results from those may be displayed..

        Args:
            value (str): value for IDD Field `Run Simulation for Weather File Run Periods`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 ' for field `SimulationControl.run_simulation_for_weather_file_run_periods`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SimulationControl.run_simulation_for_weather_file_run_periods`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SimulationControl.run_simulation_for_weather_file_run_periods`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `SimulationControl.run_simulation_for_weather_file_run_periods`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SimulationControl.run_simulation_for_weather_file_run_periods`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Run Simulation for Weather File Run Periods"] = value

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
                    raise ValueError("Required field SimulationControl:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SimulationControl:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SimulationControl: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SimulationControl: {} / {}".format(out_fields,
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

class Building(object):
    """ Corresponds to IDD object `Building`
        Describes parameters that are used during the simulation
        of the building. There are necessary correlations between the entries for
        this object and some entries in the Site:WeatherStation and
        Site:HeightVariation objects, specifically the Terrain field.
    """
    internal_name = "Building"
    field_count = 8
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 8
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Building`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["North Axis"] = None
        self._data["Terrain"] = None
        self._data["Loads Convergence Tolerance Value"] = None
        self._data["Temperature Convergence Tolerance Value"] = None
        self._data["Solar Distribution"] = None
        self._data["Maximum Number of Warmup Days"] = None
        self._data["Minimum Number of Warmup Days"] = None
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
            self.north_axis = None
        else:
            self.north_axis = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.terrain = None
        else:
            self.terrain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loads_convergence_tolerance_value = None
        else:
            self.loads_convergence_tolerance_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_convergence_tolerance_value = None
        else:
            self.temperature_convergence_tolerance_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.solar_distribution = None
        else:
            self.solar_distribution = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_number_of_warmup_days = None
        else:
            self.maximum_number_of_warmup_days = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_number_of_warmup_days = None
        else:
            self.minimum_number_of_warmup_days = vals[i]
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
    def name(self, value="NONE"):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                Default value: NONE
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
                                 ' for field `Building.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Building.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Building.name`')
        self._data["Name"] = value

    @property
    def north_axis(self):
        """Get north_axis

        Returns:
            float: the value of `north_axis` or None if not set
        """
        return self._data["North Axis"]

    @north_axis.setter
    def north_axis(self, value=0.0):
        """  Corresponds to IDD Field `North Axis`
        degrees from true North

        Args:
            value (float): value for IDD Field `North Axis`
                Units: deg
                Default value: 0.0
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
                                 ' for field `Building.north_axis`'.format(value))
        self._data["North Axis"] = value

    @property
    def terrain(self):
        """Get terrain

        Returns:
            str: the value of `terrain` or None if not set
        """
        return self._data["Terrain"]

    @terrain.setter
    def terrain(self, value="Suburbs"):
        """  Corresponds to IDD Field `Terrain`
        Country=FlatOpenCountry | Suburbs=CountryTownsSuburbs | City=CityCenter | Ocean=body of water (5km) | Urban=Urban-Industrial-Forest

        Args:
            value (str): value for IDD Field `Terrain`
                Accepted values are:
                      - Country
                      - Suburbs
                      - City
                      - Ocean
                      - Urban
                Default value: Suburbs
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
                                 ' for field `Building.terrain`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Building.terrain`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Building.terrain`')
            vals = {}
            vals["country"] = "Country"
            vals["suburbs"] = "Suburbs"
            vals["city"] = "City"
            vals["ocean"] = "Ocean"
            vals["urban"] = "Urban"
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
                                     'field `Building.terrain`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `Building.terrain`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Terrain"] = value

    @property
    def loads_convergence_tolerance_value(self):
        """Get loads_convergence_tolerance_value

        Returns:
            float: the value of `loads_convergence_tolerance_value` or None if not set
        """
        return self._data["Loads Convergence Tolerance Value"]

    @loads_convergence_tolerance_value.setter
    def loads_convergence_tolerance_value(self, value=0.04):
        """  Corresponds to IDD Field `Loads Convergence Tolerance Value`
        Loads Convergence Tolerance Value is a fraction of load

        Args:
            value (float): value for IDD Field `Loads Convergence Tolerance Value`
                Default value: 0.04
                value > 0.0
                value <= 0.5
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
                                 ' for field `Building.loads_convergence_tolerance_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `Building.loads_convergence_tolerance_value`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `Building.loads_convergence_tolerance_value`')
        self._data["Loads Convergence Tolerance Value"] = value

    @property
    def temperature_convergence_tolerance_value(self):
        """Get temperature_convergence_tolerance_value

        Returns:
            float: the value of `temperature_convergence_tolerance_value` or None if not set
        """
        return self._data["Temperature Convergence Tolerance Value"]

    @temperature_convergence_tolerance_value.setter
    def temperature_convergence_tolerance_value(self, value=0.4):
        """  Corresponds to IDD Field `Temperature Convergence Tolerance Value`

        Args:
            value (float): value for IDD Field `Temperature Convergence Tolerance Value`
                Units: deltaC
                Default value: 0.4
                value > 0.0
                value <= 0.5
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
                                 ' for field `Building.temperature_convergence_tolerance_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `Building.temperature_convergence_tolerance_value`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `Building.temperature_convergence_tolerance_value`')
        self._data["Temperature Convergence Tolerance Value"] = value

    @property
    def solar_distribution(self):
        """Get solar_distribution

        Returns:
            str: the value of `solar_distribution` or None if not set
        """
        return self._data["Solar Distribution"]

    @solar_distribution.setter
    def solar_distribution(self, value="FullExterior"):
        """  Corresponds to IDD Field `Solar Distribution`
        MinimalShadowing | FullExterior | FullInteriorAndExterior | FullExteriorWithReflections | FullInteriorAndExteriorWithReflections

        Args:
            value (str): value for IDD Field `Solar Distribution`
                Accepted values are:
                      - MinimalShadowing
                      - FullExterior
                      - FullInteriorAndExterior
                      - FullExteriorWithReflections
                      - FullInteriorAndExteriorWithReflections
                Default value: FullExterior
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
                                 ' for field `Building.solar_distribution`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Building.solar_distribution`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Building.solar_distribution`')
            vals = {}
            vals["minimalshadowing"] = "MinimalShadowing"
            vals["fullexterior"] = "FullExterior"
            vals["fullinteriorandexterior"] = "FullInteriorAndExterior"
            vals["fullexteriorwithreflections"] = "FullExteriorWithReflections"
            vals["fullinteriorandexteriorwithreflections"] = "FullInteriorAndExteriorWithReflections"
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
                                     'field `Building.solar_distribution`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `Building.solar_distribution`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Solar Distribution"] = value

    @property
    def maximum_number_of_warmup_days(self):
        """Get maximum_number_of_warmup_days

        Returns:
            int: the value of `maximum_number_of_warmup_days` or None if not set
        """
        return self._data["Maximum Number of Warmup Days"]

    @maximum_number_of_warmup_days.setter
    def maximum_number_of_warmup_days(self, value=25):
        """  Corresponds to IDD Field `Maximum Number of Warmup Days`
        EnergyPlus will only use as many warmup days as needed to reach convergence tolerance.
        This field's value should NOT be set less than 25.

        Args:
            value (int): value for IDD Field `Maximum Number of Warmup Days`
                Default value: 25
                value > 0
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
                                     'for field `Building.maximum_number_of_warmup_days`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `Building.maximum_number_of_warmup_days`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `Building.maximum_number_of_warmup_days`')
        self._data["Maximum Number of Warmup Days"] = value

    @property
    def minimum_number_of_warmup_days(self):
        """Get minimum_number_of_warmup_days

        Returns:
            int: the value of `minimum_number_of_warmup_days` or None if not set
        """
        return self._data["Minimum Number of Warmup Days"]

    @minimum_number_of_warmup_days.setter
    def minimum_number_of_warmup_days(self, value=6):
        """  Corresponds to IDD Field `Minimum Number of Warmup Days`
        The minimum number of warmup days that produce enough temperature and flux history
        to start EnergyPlus simulation for all reference buildings was suggested to be 6.
        When this field is greater than the maximum warmup days defined previous field
        the maximum number of warmup days will be reset to the minimum value entered here.
        Warmup days will be set to be the value you entered when it is less than the default 6.

        Args:
            value (int): value for IDD Field `Minimum Number of Warmup Days`
                Default value: 6
                value > 0
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
                                     'for field `Building.minimum_number_of_warmup_days`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `Building.minimum_number_of_warmup_days`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `Building.minimum_number_of_warmup_days`')
        self._data["Minimum Number of Warmup Days"] = value

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
                    raise ValueError("Required field Building:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Building:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Building: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Building: {} / {}".format(out_fields,
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

class ShadowCalculation(object):
    """ Corresponds to IDD object `ShadowCalculation`
        This object is used to control details of the solar, shading, and daylighting models
    """
    internal_name = "ShadowCalculation"
    field_count = 5
    required_fields = ["Calculation Frequency"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ShadowCalculation`
        """
        self._data = OrderedDict()
        self._data["Calculation Method"] = None
        self._data["Calculation Frequency"] = None
        self._data["Maximum Figures in Shadow Overlap Calculations"] = None
        self._data["Polygon Clipping Algorithm"] = None
        self._data["Sky Diffuse Modeling Algorithm"] = None
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
            self.calculation_method = None
        else:
            self.calculation_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.calculation_frequency = None
        else:
            self.calculation_frequency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_figures_in_shadow_overlap_calculations = None
        else:
            self.maximum_figures_in_shadow_overlap_calculations = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.polygon_clipping_algorithm = None
        else:
            self.polygon_clipping_algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sky_diffuse_modeling_algorithm = None
        else:
            self.sky_diffuse_modeling_algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def calculation_method(self):
        """Get calculation_method

        Returns:
            str: the value of `calculation_method` or None if not set
        """
        return self._data["Calculation Method"]

    @calculation_method.setter
    def calculation_method(self, value="AverageOverDaysInFrequency"):
        """  Corresponds to IDD Field `Calculation Method`
        choose calculation method. note that TimestepFrequency is only needed for certain cases
        and can increase execution time significantly.

        Args:
            value (str): value for IDD Field `Calculation Method`
                Accepted values are:
                      - AverageOverDaysInFrequency
                      - TimestepFrequency
                Default value: AverageOverDaysInFrequency
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
                                 ' for field `ShadowCalculation.calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadowCalculation.calculation_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadowCalculation.calculation_method`')
            vals = {}
            vals["averageoverdaysinfrequency"] = "AverageOverDaysInFrequency"
            vals["timestepfrequency"] = "TimestepFrequency"
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
                                     'field `ShadowCalculation.calculation_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ShadowCalculation.calculation_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Calculation Method"] = value

    @property
    def calculation_frequency(self):
        """Get calculation_frequency

        Returns:
            int: the value of `calculation_frequency` or None if not set
        """
        return self._data["Calculation Frequency"]

    @calculation_frequency.setter
    def calculation_frequency(self, value=20):
        """  Corresponds to IDD Field `Calculation Frequency`
        enter number of days
        this field is only used if the previous field is set to AverageOverDaysInFrequency
        0=Use Default Periodic Calculation|<else> calculate every <value> day
        only really applicable to RunPeriods
        warning issued if >31

        Args:
            value (int): value for IDD Field `Calculation Frequency`
                Default value: 20
                value >= 1
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
                                     'for field `ShadowCalculation.calculation_frequency`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ShadowCalculation.calculation_frequency`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ShadowCalculation.calculation_frequency`')
        self._data["Calculation Frequency"] = value

    @property
    def maximum_figures_in_shadow_overlap_calculations(self):
        """Get maximum_figures_in_shadow_overlap_calculations

        Returns:
            int: the value of `maximum_figures_in_shadow_overlap_calculations` or None if not set
        """
        return self._data["Maximum Figures in Shadow Overlap Calculations"]

    @maximum_figures_in_shadow_overlap_calculations.setter
    def maximum_figures_in_shadow_overlap_calculations(self, value=15000):
        """  Corresponds to IDD Field `Maximum Figures in Shadow Overlap Calculations`
        Number of allowable figures in shadow overlap calculations

        Args:
            value (int): value for IDD Field `Maximum Figures in Shadow Overlap Calculations`
                Default value: 15000
                value >= 200
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
                                     'for field `ShadowCalculation.maximum_figures_in_shadow_overlap_calculations`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ShadowCalculation.maximum_figures_in_shadow_overlap_calculations`'.format(value))
            if value < 200:
                raise ValueError('value need to be greater or equal 200 '
                                 'for field `ShadowCalculation.maximum_figures_in_shadow_overlap_calculations`')
        self._data["Maximum Figures in Shadow Overlap Calculations"] = value

    @property
    def polygon_clipping_algorithm(self):
        """Get polygon_clipping_algorithm

        Returns:
            str: the value of `polygon_clipping_algorithm` or None if not set
        """
        return self._data["Polygon Clipping Algorithm"]

    @polygon_clipping_algorithm.setter
    def polygon_clipping_algorithm(self, value=None):
        """  Corresponds to IDD Field `Polygon Clipping Algorithm`
        Advanced Feature.  Internal default is SutherlandHodgman
        Refer to InputOutput Reference and Engineering Reference for more information

        Args:
            value (str): value for IDD Field `Polygon Clipping Algorithm`
                Accepted values are:
                      - ConvexWeilerAtherton
                      - SutherlandHodgman
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
                                 ' for field `ShadowCalculation.polygon_clipping_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadowCalculation.polygon_clipping_algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadowCalculation.polygon_clipping_algorithm`')
            vals = {}
            vals["convexweileratherton"] = "ConvexWeilerAtherton"
            vals["sutherlandhodgman"] = "SutherlandHodgman"
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
                                     'field `ShadowCalculation.polygon_clipping_algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ShadowCalculation.polygon_clipping_algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Polygon Clipping Algorithm"] = value

    @property
    def sky_diffuse_modeling_algorithm(self):
        """Get sky_diffuse_modeling_algorithm

        Returns:
            str: the value of `sky_diffuse_modeling_algorithm` or None if not set
        """
        return self._data["Sky Diffuse Modeling Algorithm"]

    @sky_diffuse_modeling_algorithm.setter
    def sky_diffuse_modeling_algorithm(self, value=None):
        """  Corresponds to IDD Field `Sky Diffuse Modeling Algorithm`
        Advanced Feature.  Internal default is SimpleSkyDiffuseModeling
        If you have shading elements that change transmittance over the
        year, you may wish to choose the detailed method.
        Refer to InputOutput Reference and Engineering Reference for more information

        Args:
            value (str): value for IDD Field `Sky Diffuse Modeling Algorithm`
                Accepted values are:
                      - SimpleSkyDiffuseModeling
                      - DetailedSkyDiffuseModeling
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
                                 ' for field `ShadowCalculation.sky_diffuse_modeling_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadowCalculation.sky_diffuse_modeling_algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadowCalculation.sky_diffuse_modeling_algorithm`')
            vals = {}
            vals["simpleskydiffusemodeling"] = "SimpleSkyDiffuseModeling"
            vals["detailedskydiffusemodeling"] = "DetailedSkyDiffuseModeling"
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
                                     'field `ShadowCalculation.sky_diffuse_modeling_algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ShadowCalculation.sky_diffuse_modeling_algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sky Diffuse Modeling Algorithm"] = value

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
                    raise ValueError("Required field ShadowCalculation:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadowCalculation:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadowCalculation: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadowCalculation: {} / {}".format(out_fields,
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

class SurfaceConvectionAlgorithmInside(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside`
        Default indoor surface heat transfer convection algorithm to be used for all zones
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside"
    field_count = 1
    required_fields = ["Algorithm"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Inside`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="TARP"):
        """  Corresponds to IDD Field `Algorithm`
        Simple = constant value natural convection (ASHRAE)
        TARP = variable natural convection based on temperature difference (ASHRAE, Walton)
        CeilingDiffuser = ACH-based forced and mixed convection correlations
        for ceiling diffuser configuration with simple natural convection limit
        AdaptiveConvectionAlgorithm = dynamic selection of convection models based on conditions

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - Simple
                      - TARP
                      - CeilingDiffuser
                      - AdaptiveConvectionAlgorithm
                Default value: TARP
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
                                 ' for field `SurfaceConvectionAlgorithmInside.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInside.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInside.algorithm`')
            vals = {}
            vals["simple"] = "Simple"
            vals["tarp"] = "TARP"
            vals["ceilingdiffuser"] = "CeilingDiffuser"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
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
                                     'field `SurfaceConvectionAlgorithmInside.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInside.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

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
                    raise ValueError("Required field SurfaceConvectionAlgorithmInside:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceConvectionAlgorithmInside:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceConvectionAlgorithmInside: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceConvectionAlgorithmInside: {} / {}".format(out_fields,
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

class SurfaceConvectionAlgorithmOutside(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside`
        Default outside surface heat transfer convection algorithm to be used for all zones
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside"
    field_count = 1
    required_fields = ["Algorithm"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Outside`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="DOE-2"):
        """  Corresponds to IDD Field `Algorithm`
        SimpleCombined = Combined radiation and convection coefficient using simple ASHRAE model
        TARP = correlation from models developed by ASHRAE, Walton, and Sparrow et. al.
        MoWiTT = correlation from measurements by Klems and Yazdanian for smooth surfaces
        DOE-2 = correlation from measurements by Klems and Yazdanian for rough surfaces
        AdaptiveConvectionAlgorithm = dynamic selection of correlations based on conditions

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - SimpleCombined
                      - TARP
                      - MoWiTT
                      - DOE-2
                      - AdaptiveConvectionAlgorithm
                Default value: DOE-2
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
                                 ' for field `SurfaceConvectionAlgorithmOutside.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutside.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutside.algorithm`')
            vals = {}
            vals["simplecombined"] = "SimpleCombined"
            vals["tarp"] = "TARP"
            vals["mowitt"] = "MoWiTT"
            vals["doe-2"] = "DOE-2"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
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
                                     'field `SurfaceConvectionAlgorithmOutside.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutside.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

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
                    raise ValueError("Required field SurfaceConvectionAlgorithmOutside:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceConvectionAlgorithmOutside:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceConvectionAlgorithmOutside: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceConvectionAlgorithmOutside: {} / {}".format(out_fields,
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

class HeatBalanceAlgorithm(object):
    """ Corresponds to IDD object `HeatBalanceAlgorithm`
        Determines which Heat Balance Algorithm will be used ie.
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: ConductionFiniteDifferenceSimplified
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    internal_name = "HeatBalanceAlgorithm"
    field_count = 4
    required_fields = ["Algorithm"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatBalanceAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None
        self._data["Surface Temperature Upper Limit"] = None
        self._data["Minimum Surface Convection Heat Transfer Coefficient Value"] = None
        self._data["Maximum Surface Convection Heat Transfer Coefficient Value"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_temperature_upper_limit = None
        else:
            self.surface_temperature_upper_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_surface_convection_heat_transfer_coefficient_value = None
        else:
            self.minimum_surface_convection_heat_transfer_coefficient_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_surface_convection_heat_transfer_coefficient_value = None
        else:
            self.maximum_surface_convection_heat_transfer_coefficient_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `Algorithm`

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
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
                                 ' for field `HeatBalanceAlgorithm.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatBalanceAlgorithm.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatBalanceAlgorithm.algorithm`')
            vals = {}
            vals["conductiontransferfunction"] = "ConductionTransferFunction"
            vals["moisturepenetrationdepthconductiontransferfunction"] = "MoisturePenetrationDepthConductionTransferFunction"
            vals["conductionfinitedifference"] = "ConductionFiniteDifference"
            vals["combinedheatandmoisturefiniteelement"] = "CombinedHeatAndMoistureFiniteElement"
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
                                     'field `HeatBalanceAlgorithm.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatBalanceAlgorithm.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

    @property
    def surface_temperature_upper_limit(self):
        """Get surface_temperature_upper_limit

        Returns:
            float: the value of `surface_temperature_upper_limit` or None if not set
        """
        return self._data["Surface Temperature Upper Limit"]

    @surface_temperature_upper_limit.setter
    def surface_temperature_upper_limit(self, value=200.0):
        """  Corresponds to IDD Field `Surface Temperature Upper Limit`

        Args:
            value (float): value for IDD Field `Surface Temperature Upper Limit`
                Units: C
                Default value: 200.0
                value >= 200.0
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
                                 ' for field `HeatBalanceAlgorithm.surface_temperature_upper_limit`'.format(value))
            if value < 200.0:
                raise ValueError('value need to be greater or equal 200.0 '
                                 'for field `HeatBalanceAlgorithm.surface_temperature_upper_limit`')
        self._data["Surface Temperature Upper Limit"] = value

    @property
    def minimum_surface_convection_heat_transfer_coefficient_value(self):
        """Get minimum_surface_convection_heat_transfer_coefficient_value

        Returns:
            float: the value of `minimum_surface_convection_heat_transfer_coefficient_value` or None if not set
        """
        return self._data["Minimum Surface Convection Heat Transfer Coefficient Value"]

    @minimum_surface_convection_heat_transfer_coefficient_value.setter
    def minimum_surface_convection_heat_transfer_coefficient_value(self, value=0.1):
        """  Corresponds to IDD Field `Minimum Surface Convection Heat Transfer Coefficient Value`

        Args:
            value (float): value for IDD Field `Minimum Surface Convection Heat Transfer Coefficient Value`
                Units: W/m2-K
                Default value: 0.1
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
                                 ' for field `HeatBalanceAlgorithm.minimum_surface_convection_heat_transfer_coefficient_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `HeatBalanceAlgorithm.minimum_surface_convection_heat_transfer_coefficient_value`')
        self._data["Minimum Surface Convection Heat Transfer Coefficient Value"] = value

    @property
    def maximum_surface_convection_heat_transfer_coefficient_value(self):
        """Get maximum_surface_convection_heat_transfer_coefficient_value

        Returns:
            float: the value of `maximum_surface_convection_heat_transfer_coefficient_value` or None if not set
        """
        return self._data["Maximum Surface Convection Heat Transfer Coefficient Value"]

    @maximum_surface_convection_heat_transfer_coefficient_value.setter
    def maximum_surface_convection_heat_transfer_coefficient_value(self, value=1000.0):
        """  Corresponds to IDD Field `Maximum Surface Convection Heat Transfer Coefficient Value`

        Args:
            value (float): value for IDD Field `Maximum Surface Convection Heat Transfer Coefficient Value`
                Units: W/m2-K
                Default value: 1000.0
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
                                 ' for field `HeatBalanceAlgorithm.maximum_surface_convection_heat_transfer_coefficient_value`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `HeatBalanceAlgorithm.maximum_surface_convection_heat_transfer_coefficient_value`')
        self._data["Maximum Surface Convection Heat Transfer Coefficient Value"] = value

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
                    raise ValueError("Required field HeatBalanceAlgorithm:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field HeatBalanceAlgorithm:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for HeatBalanceAlgorithm: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for HeatBalanceAlgorithm: {} / {}".format(out_fields,
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

class HeatBalanceSettingsConductionFiniteDifference(object):
    """ Corresponds to IDD object `HeatBalanceSettings:ConductionFiniteDifference`
        Determines settings for the Conduction Finite Difference
        algorithm for surface heat transfer modeling.
    """
    internal_name = "HeatBalanceSettings:ConductionFiniteDifference"
    field_count = 4
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `HeatBalanceSettings:ConductionFiniteDifference`
        """
        self._data = OrderedDict()
        self._data["Difference Scheme"] = None
        self._data["Space Discretization Constant"] = None
        self._data["Relaxation Factor"] = None
        self._data["Inside Face Surface Temperature Convergence Criteria"] = None
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
            self.difference_scheme = None
        else:
            self.difference_scheme = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.space_discretization_constant = None
        else:
            self.space_discretization_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relaxation_factor = None
        else:
            self.relaxation_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_face_surface_temperature_convergence_criteria = None
        else:
            self.inside_face_surface_temperature_convergence_criteria = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def difference_scheme(self):
        """Get difference_scheme

        Returns:
            str: the value of `difference_scheme` or None if not set
        """
        return self._data["Difference Scheme"]

    @difference_scheme.setter
    def difference_scheme(self, value="FullyImplicitFirstOrder"):
        """  Corresponds to IDD Field `Difference Scheme`

        Args:
            value (str): value for IDD Field `Difference Scheme`
                Accepted values are:
                      - CrankNicholsonSecondOrder
                      - FullyImplicitFirstOrder
                Default value: FullyImplicitFirstOrder
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
                                 ' for field `HeatBalanceSettingsConductionFiniteDifference.difference_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `HeatBalanceSettingsConductionFiniteDifference.difference_scheme`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `HeatBalanceSettingsConductionFiniteDifference.difference_scheme`')
            vals = {}
            vals["cranknicholsonsecondorder"] = "CrankNicholsonSecondOrder"
            vals["fullyimplicitfirstorder"] = "FullyImplicitFirstOrder"
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
                                     'field `HeatBalanceSettingsConductionFiniteDifference.difference_scheme`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `HeatBalanceSettingsConductionFiniteDifference.difference_scheme`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Difference Scheme"] = value

    @property
    def space_discretization_constant(self):
        """Get space_discretization_constant

        Returns:
            float: the value of `space_discretization_constant` or None if not set
        """
        return self._data["Space Discretization Constant"]

    @space_discretization_constant.setter
    def space_discretization_constant(self, value=3.0):
        """  Corresponds to IDD Field `Space Discretization Constant`
        increase or decrease number of nodes

        Args:
            value (float): value for IDD Field `Space Discretization Constant`
                Default value: 3.0
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
                                 ' for field `HeatBalanceSettingsConductionFiniteDifference.space_discretization_constant`'.format(value))
        self._data["Space Discretization Constant"] = value

    @property
    def relaxation_factor(self):
        """Get relaxation_factor

        Returns:
            float: the value of `relaxation_factor` or None if not set
        """
        return self._data["Relaxation Factor"]

    @relaxation_factor.setter
    def relaxation_factor(self, value=1.0):
        """  Corresponds to IDD Field `Relaxation Factor`

        Args:
            value (float): value for IDD Field `Relaxation Factor`
                Default value: 1.0
                value >= 0.01
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
                                 ' for field `HeatBalanceSettingsConductionFiniteDifference.relaxation_factor`'.format(value))
            if value < 0.01:
                raise ValueError('value need to be greater or equal 0.01 '
                                 'for field `HeatBalanceSettingsConductionFiniteDifference.relaxation_factor`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `HeatBalanceSettingsConductionFiniteDifference.relaxation_factor`')
        self._data["Relaxation Factor"] = value

    @property
    def inside_face_surface_temperature_convergence_criteria(self):
        """Get inside_face_surface_temperature_convergence_criteria

        Returns:
            float: the value of `inside_face_surface_temperature_convergence_criteria` or None if not set
        """
        return self._data["Inside Face Surface Temperature Convergence Criteria"]

    @inside_face_surface_temperature_convergence_criteria.setter
    def inside_face_surface_temperature_convergence_criteria(self, value=0.002):
        """  Corresponds to IDD Field `Inside Face Surface Temperature Convergence Criteria`

        Args:
            value (float): value for IDD Field `Inside Face Surface Temperature Convergence Criteria`
                Default value: 0.002
                value >= 1e-07
                value <= 0.01
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
                                 ' for field `HeatBalanceSettingsConductionFiniteDifference.inside_face_surface_temperature_convergence_criteria`'.format(value))
            if value < 1e-07:
                raise ValueError('value need to be greater or equal 1e-07 '
                                 'for field `HeatBalanceSettingsConductionFiniteDifference.inside_face_surface_temperature_convergence_criteria`')
            if value > 0.01:
                raise ValueError('value need to be smaller 0.01 '
                                 'for field `HeatBalanceSettingsConductionFiniteDifference.inside_face_surface_temperature_convergence_criteria`')
        self._data["Inside Face Surface Temperature Convergence Criteria"] = value

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
                    raise ValueError("Required field HeatBalanceSettingsConductionFiniteDifference:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field HeatBalanceSettingsConductionFiniteDifference:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for HeatBalanceSettingsConductionFiniteDifference: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for HeatBalanceSettingsConductionFiniteDifference: {} / {}".format(out_fields,
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

class ZoneAirHeatBalanceAlgorithm(object):
    """ Corresponds to IDD object `ZoneAirHeatBalanceAlgorithm`
        Determines which algorithm will be used to solve the zone air heat balance.
    """
    internal_name = "ZoneAirHeatBalanceAlgorithm"
    field_count = 1
    required_fields = []
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirHeatBalanceAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ThirdOrderBackwardDifference"):
        """  Corresponds to IDD Field `Algorithm`

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - ThirdOrderBackwardDifference
                      - AnalyticalSolution
                      - EulerMethod
                Default value: ThirdOrderBackwardDifference
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
                                 ' for field `ZoneAirHeatBalanceAlgorithm.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirHeatBalanceAlgorithm.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirHeatBalanceAlgorithm.algorithm`')
            vals = {}
            vals["thirdorderbackwarddifference"] = "ThirdOrderBackwardDifference"
            vals["analyticalsolution"] = "AnalyticalSolution"
            vals["eulermethod"] = "EulerMethod"
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
                                     'field `ZoneAirHeatBalanceAlgorithm.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneAirHeatBalanceAlgorithm.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

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
                    raise ValueError("Required field ZoneAirHeatBalanceAlgorithm:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneAirHeatBalanceAlgorithm:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneAirHeatBalanceAlgorithm: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneAirHeatBalanceAlgorithm: {} / {}".format(out_fields,
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

class ZoneAirContaminantBalance(object):
    """ Corresponds to IDD object `ZoneAirContaminantBalance`
        Determines which contaminant concentration will be simulates.
    """
    internal_name = "ZoneAirContaminantBalance"
    field_count = 4
    required_fields = []
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirContaminantBalance`
        """
        self._data = OrderedDict()
        self._data["Carbon Dioxide Concentration"] = None
        self._data["Outdoor Carbon Dioxide Schedule Name"] = None
        self._data["Generic Contaminant Concentration"] = None
        self._data["Outdoor Generic Contaminant Schedule Name"] = None
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
            self.carbon_dioxide_concentration = None
        else:
            self.carbon_dioxide_concentration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_carbon_dioxide_schedule_name = None
        else:
            self.outdoor_carbon_dioxide_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.generic_contaminant_concentration = None
        else:
            self.generic_contaminant_concentration = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_generic_contaminant_schedule_name = None
        else:
            self.outdoor_generic_contaminant_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def carbon_dioxide_concentration(self):
        """Get carbon_dioxide_concentration

        Returns:
            str: the value of `carbon_dioxide_concentration` or None if not set
        """
        return self._data["Carbon Dioxide Concentration"]

    @carbon_dioxide_concentration.setter
    def carbon_dioxide_concentration(self, value="No"):
        """  Corresponds to IDD Field `Carbon Dioxide Concentration`
        If Yes, CO2 simulation will be performed.

        Args:
            value (str): value for IDD Field `Carbon Dioxide Concentration`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `ZoneAirContaminantBalance.carbon_dioxide_concentration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirContaminantBalance.carbon_dioxide_concentration`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirContaminantBalance.carbon_dioxide_concentration`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `ZoneAirContaminantBalance.carbon_dioxide_concentration`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneAirContaminantBalance.carbon_dioxide_concentration`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Carbon Dioxide Concentration"] = value

    @property
    def outdoor_carbon_dioxide_schedule_name(self):
        """Get outdoor_carbon_dioxide_schedule_name

        Returns:
            str: the value of `outdoor_carbon_dioxide_schedule_name` or None if not set
        """
        return self._data["Outdoor Carbon Dioxide Schedule Name"]

    @outdoor_carbon_dioxide_schedule_name.setter
    def outdoor_carbon_dioxide_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Carbon Dioxide Schedule Name`
        Schedule values should be in parts per million (ppm)

        Args:
            value (str): value for IDD Field `Outdoor Carbon Dioxide Schedule Name`
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
                                 ' for field `ZoneAirContaminantBalance.outdoor_carbon_dioxide_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirContaminantBalance.outdoor_carbon_dioxide_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirContaminantBalance.outdoor_carbon_dioxide_schedule_name`')
        self._data["Outdoor Carbon Dioxide Schedule Name"] = value

    @property
    def generic_contaminant_concentration(self):
        """Get generic_contaminant_concentration

        Returns:
            str: the value of `generic_contaminant_concentration` or None if not set
        """
        return self._data["Generic Contaminant Concentration"]

    @generic_contaminant_concentration.setter
    def generic_contaminant_concentration(self, value="No"):
        """  Corresponds to IDD Field `Generic Contaminant Concentration`
        If Yes, generic contaminant simulation will be performed.

        Args:
            value (str): value for IDD Field `Generic Contaminant Concentration`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `ZoneAirContaminantBalance.generic_contaminant_concentration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirContaminantBalance.generic_contaminant_concentration`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirContaminantBalance.generic_contaminant_concentration`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `ZoneAirContaminantBalance.generic_contaminant_concentration`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneAirContaminantBalance.generic_contaminant_concentration`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Generic Contaminant Concentration"] = value

    @property
    def outdoor_generic_contaminant_schedule_name(self):
        """Get outdoor_generic_contaminant_schedule_name

        Returns:
            str: the value of `outdoor_generic_contaminant_schedule_name` or None if not set
        """
        return self._data["Outdoor Generic Contaminant Schedule Name"]

    @outdoor_generic_contaminant_schedule_name.setter
    def outdoor_generic_contaminant_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Generic Contaminant Schedule Name`
        Schedule values should be generic contaminant concentration in parts per
        million (ppm)

        Args:
            value (str): value for IDD Field `Outdoor Generic Contaminant Schedule Name`
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
                                 ' for field `ZoneAirContaminantBalance.outdoor_generic_contaminant_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirContaminantBalance.outdoor_generic_contaminant_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirContaminantBalance.outdoor_generic_contaminant_schedule_name`')
        self._data["Outdoor Generic Contaminant Schedule Name"] = value

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
                    raise ValueError("Required field ZoneAirContaminantBalance:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneAirContaminantBalance:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneAirContaminantBalance: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneAirContaminantBalance: {} / {}".format(out_fields,
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

class ZoneAirMassFlowConservation(object):
    """ Corresponds to IDD object `ZoneAirMassFlowConservation`
        Enforces the zone air mass flow balance by adjusting zone mixing object flow rates.
        The infiltration object mass flow rate may also be adjusted or may add infiltration
        air flow to the base infiltration air flow for source zones only.
    """
    internal_name = "ZoneAirMassFlowConservation"
    field_count = 2
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneAirMassFlowConservation`
        """
        self._data = OrderedDict()
        self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"] = None
        self._data["Source Zone Infiltration Treatment"] = None
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
            self.adjust_zone_mixing_for_zone_air_mass_flow_balance = None
        else:
            self.adjust_zone_mixing_for_zone_air_mass_flow_balance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_zone_infiltration_treatment = None
        else:
            self.source_zone_infiltration_treatment = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def adjust_zone_mixing_for_zone_air_mass_flow_balance(self):
        """Get adjust_zone_mixing_for_zone_air_mass_flow_balance

        Returns:
            str: the value of `adjust_zone_mixing_for_zone_air_mass_flow_balance` or None if not set
        """
        return self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"]

    @adjust_zone_mixing_for_zone_air_mass_flow_balance.setter
    def adjust_zone_mixing_for_zone_air_mass_flow_balance(self, value="No"):
        """  Corresponds to IDD Field `Adjust Zone Mixing For Zone Air Mass Flow Balance`
        If Yes, Zone mixing object flow rates are adjusted to balance the zone air mass flow
        and additional infiltration air flow may be added if required in order to balance the
        zone air mass flow.
        This optional choice input field allows users triggering the zone air mass flow
        balance calculation when desired. This global object has two choice KEYs: Yes and
        No. If this input field is specified as Yes, then EnergyPlus attempts to enforce
        the zone air mass flow conservation, or else if it is specified as No, then EnergyPlus
        calculation defaults to zone air mass flow balance that does not include zone mixing
        objects and that assumes self-balanced simple flow objects per the default procedure,
        which may not necessarily enforce zone mass conservation unless the user specified
        a balanced flow to begin with. Mass conservation is enforced both for the receiving
        and source zones if there is at least one mixing object defined. The default input
        is No. (Note that No input may also results in balanced flow depending on the
        system specified).

        Args:
            value (str): value for IDD Field `Adjust Zone Mixing For Zone Air Mass Flow Balance`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `ZoneAirMassFlowConservation.adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirMassFlowConservation.adjust_zone_mixing_for_zone_air_mass_flow_balance`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirMassFlowConservation.adjust_zone_mixing_for_zone_air_mass_flow_balance`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `ZoneAirMassFlowConservation.adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneAirMassFlowConservation.adjust_zone_mixing_for_zone_air_mass_flow_balance`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Adjust Zone Mixing For Zone Air Mass Flow Balance"] = value

    @property
    def source_zone_infiltration_treatment(self):
        """Get source_zone_infiltration_treatment

        Returns:
            str: the value of `source_zone_infiltration_treatment` or None if not set
        """
        return self._data["Source Zone Infiltration Treatment"]

    @source_zone_infiltration_treatment.setter
    def source_zone_infiltration_treatment(self, value="AddInfiltrationFlow"):
        """  Corresponds to IDD Field `Source Zone Infiltration Treatment`
        This input field allows user to choose how zone infiltration flow is treated during
        the zone air mass flow balance calculation.
        It has two choice KEYs: AddInfiltrationFlow and AdjustInfiltrationFlow.  If this
        input is specified as AddInfiltrationFlow, then energy plus adds infiltration air
        mass flow on top of the base flow, which is calculated using the infiltration object
        user inputs, in order to balance the zone air mass flow.  The additional infiltration
        air mass flow is not self-balanced.  If this input is specified as
        AdjustInfiltrationFlow, then energy plus may adjust the base flow calculated using
        the infiltration object user inputs in order to balance the zone air mass flow. If it
        is not required to adjust the base infiltration air flow calculated from the user
        specified infiltration object inputs, then the base infiltration air mass flow
        is assumed self-balanced. If the above input field specified as "No", then this input
        field has no impact on the simulation.

        Args:
            value (str): value for IDD Field `Source Zone Infiltration Treatment`
                Accepted values are:
                      - AddInfiltrationFlow
                      - AdjustInfiltrationFlow
                Default value: AddInfiltrationFlow
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
                                 ' for field `ZoneAirMassFlowConservation.source_zone_infiltration_treatment`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneAirMassFlowConservation.source_zone_infiltration_treatment`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneAirMassFlowConservation.source_zone_infiltration_treatment`')
            vals = {}
            vals["addinfiltrationflow"] = "AddInfiltrationFlow"
            vals["adjustinfiltrationflow"] = "AdjustInfiltrationFlow"
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
                                     'field `ZoneAirMassFlowConservation.source_zone_infiltration_treatment`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneAirMassFlowConservation.source_zone_infiltration_treatment`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Source Zone Infiltration Treatment"] = value

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
                    raise ValueError("Required field ZoneAirMassFlowConservation:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneAirMassFlowConservation:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneAirMassFlowConservation: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneAirMassFlowConservation: {} / {}".format(out_fields,
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

class ZoneCapacitanceMultiplierResearchSpecial(object):
    """ Corresponds to IDD object `ZoneCapacitanceMultiplier:ResearchSpecial`
        Multiplier altering the relative capacitance of the air compared to an empty zone
    """
    internal_name = "ZoneCapacitanceMultiplier:ResearchSpecial"
    field_count = 4
    required_fields = []
    extensible_fields = 0
    format = "singleline"
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneCapacitanceMultiplier:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Temperature Capacity Multiplier"] = None
        self._data["Humidity Capacity Multiplier"] = None
        self._data["Carbon Dioxide Capacity Multiplier"] = None
        self._data["Generic Contaminant Capacity Multiplier"] = None
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
            self.temperature_capacity_multiplier = None
        else:
            self.temperature_capacity_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidity_capacity_multiplier = None
        else:
            self.humidity_capacity_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.carbon_dioxide_capacity_multiplier = None
        else:
            self.carbon_dioxide_capacity_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.generic_contaminant_capacity_multiplier = None
        else:
            self.generic_contaminant_capacity_multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def temperature_capacity_multiplier(self):
        """Get temperature_capacity_multiplier

        Returns:
            float: the value of `temperature_capacity_multiplier` or None if not set
        """
        return self._data["Temperature Capacity Multiplier"]

    @temperature_capacity_multiplier.setter
    def temperature_capacity_multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Temperature Capacity Multiplier`
        Used to alter the capacitance of zone air with respect to heat or temperature

        Args:
            value (float): value for IDD Field `Temperature Capacity Multiplier`
                Default value: 1.0
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
                                 ' for field `ZoneCapacitanceMultiplierResearchSpecial.temperature_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneCapacitanceMultiplierResearchSpecial.temperature_capacity_multiplier`')
        self._data["Temperature Capacity Multiplier"] = value

    @property
    def humidity_capacity_multiplier(self):
        """Get humidity_capacity_multiplier

        Returns:
            float: the value of `humidity_capacity_multiplier` or None if not set
        """
        return self._data["Humidity Capacity Multiplier"]

    @humidity_capacity_multiplier.setter
    def humidity_capacity_multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Humidity Capacity Multiplier`
        Used to alter the capacitance of zone air with respect to moisture or humidity ratio

        Args:
            value (float): value for IDD Field `Humidity Capacity Multiplier`
                Default value: 1.0
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
                                 ' for field `ZoneCapacitanceMultiplierResearchSpecial.humidity_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneCapacitanceMultiplierResearchSpecial.humidity_capacity_multiplier`')
        self._data["Humidity Capacity Multiplier"] = value

    @property
    def carbon_dioxide_capacity_multiplier(self):
        """Get carbon_dioxide_capacity_multiplier

        Returns:
            float: the value of `carbon_dioxide_capacity_multiplier` or None if not set
        """
        return self._data["Carbon Dioxide Capacity Multiplier"]

    @carbon_dioxide_capacity_multiplier.setter
    def carbon_dioxide_capacity_multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Carbon Dioxide Capacity Multiplier`
        Used to alter the capacitance of zone air with respect to zone air carbob dioxide concentration

        Args:
            value (float): value for IDD Field `Carbon Dioxide Capacity Multiplier`
                Default value: 1.0
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
                                 ' for field `ZoneCapacitanceMultiplierResearchSpecial.carbon_dioxide_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneCapacitanceMultiplierResearchSpecial.carbon_dioxide_capacity_multiplier`')
        self._data["Carbon Dioxide Capacity Multiplier"] = value

    @property
    def generic_contaminant_capacity_multiplier(self):
        """Get generic_contaminant_capacity_multiplier

        Returns:
            float: the value of `generic_contaminant_capacity_multiplier` or None if not set
        """
        return self._data["Generic Contaminant Capacity Multiplier"]

    @generic_contaminant_capacity_multiplier.setter
    def generic_contaminant_capacity_multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Generic Contaminant Capacity Multiplier`
        Used to alter the capacitance of zone air with respect to zone air generic contaminant concentration

        Args:
            value (float): value for IDD Field `Generic Contaminant Capacity Multiplier`
                Default value: 1.0
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
                                 ' for field `ZoneCapacitanceMultiplierResearchSpecial.generic_contaminant_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ZoneCapacitanceMultiplierResearchSpecial.generic_contaminant_capacity_multiplier`')
        self._data["Generic Contaminant Capacity Multiplier"] = value

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
                    raise ValueError("Required field ZoneCapacitanceMultiplierResearchSpecial:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneCapacitanceMultiplierResearchSpecial:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneCapacitanceMultiplierResearchSpecial: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneCapacitanceMultiplierResearchSpecial: {} / {}".format(out_fields,
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

class Timestep(object):
    """ Corresponds to IDD object `Timestep`
        Specifies the "basic" timestep for the simulation. The
        value entered here is also known as the Zone Timestep.  This is used in
        the Zone Heat Balance Model calculation as the driving timestep for heat
        transfer and load calculations.
    """
    internal_name = "Timestep"
    field_count = 1
    required_fields = ["Number of Timesteps per Hour"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Timestep`
        """
        self._data = OrderedDict()
        self._data["Number of Timesteps per Hour"] = None
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
            self.number_of_timesteps_per_hour = None
        else:
            self.number_of_timesteps_per_hour = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def number_of_timesteps_per_hour(self):
        """Get number_of_timesteps_per_hour

        Returns:
            int: the value of `number_of_timesteps_per_hour` or None if not set
        """
        return self._data["Number of Timesteps per Hour"]

    @number_of_timesteps_per_hour.setter
    def number_of_timesteps_per_hour(self, value=6):
        """  Corresponds to IDD Field `Number of Timesteps per Hour`
        Number in hour: normal validity 4 to 60: 6 suggested
        Must be evenly divisible into 60
        Allowable values include 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60
        Normal 6 is mimimum as lower values may cause inaccuracies
        A minimum value of 20 is suggested for both ConductionFiniteDifference
        and CombinedHeatAndMoistureFiniteElement surface heat balance alogorithms
        A minimum of 12 is suggested for simulations involving a Vegetated Roof (Material:RoofVegetation).

        Args:
            value (int): value for IDD Field `Number of Timesteps per Hour`
                Default value: 6
                value >= 1
                value <= 60
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
                                     'for field `Timestep.number_of_timesteps_per_hour`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `Timestep.number_of_timesteps_per_hour`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `Timestep.number_of_timesteps_per_hour`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `Timestep.number_of_timesteps_per_hour`')
        self._data["Number of Timesteps per Hour"] = value

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
                    raise ValueError("Required field Timestep:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Timestep:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Timestep: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Timestep: {} / {}".format(out_fields,
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

class ConvergenceLimits(object):
    """ Corresponds to IDD object `ConvergenceLimits`
        Specifies limits on HVAC system simulation timesteps and iterations.
        This item is an advanced feature that should be used only with caution.
    """
    internal_name = "ConvergenceLimits"
    field_count = 4
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ConvergenceLimits`
        """
        self._data = OrderedDict()
        self._data["Minimum System Timestep"] = None
        self._data["Maximum HVAC Iterations"] = None
        self._data["Minimum Plant Iterations"] = None
        self._data["Maximum Plant Iterations"] = None
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
            self.minimum_system_timestep = None
        else:
            self.minimum_system_timestep = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_hvac_iterations = None
        else:
            self.maximum_hvac_iterations = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_plant_iterations = None
        else:
            self.minimum_plant_iterations = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_plant_iterations = None
        else:
            self.maximum_plant_iterations = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def minimum_system_timestep(self):
        """Get minimum_system_timestep

        Returns:
            int: the value of `minimum_system_timestep` or None if not set
        """
        return self._data["Minimum System Timestep"]

    @minimum_system_timestep.setter
    def minimum_system_timestep(self, value=None):
        """  Corresponds to IDD Field `Minimum System Timestep`
        0 sets the minimum to the zone timestep (ref: Timestep)
        1 is normal (ratchet down to 1 minute)
        setting greater than zone timestep (in minutes) will effectively set to zone timestep

        Args:
            value (int): value for IDD Field `Minimum System Timestep`
                Units: minutes
                value >= 0
                value <= 60
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
                                     'for field `ConvergenceLimits.minimum_system_timestep`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ConvergenceLimits.minimum_system_timestep`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `ConvergenceLimits.minimum_system_timestep`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `ConvergenceLimits.minimum_system_timestep`')
        self._data["Minimum System Timestep"] = value

    @property
    def maximum_hvac_iterations(self):
        """Get maximum_hvac_iterations

        Returns:
            int: the value of `maximum_hvac_iterations` or None if not set
        """
        return self._data["Maximum HVAC Iterations"]

    @maximum_hvac_iterations.setter
    def maximum_hvac_iterations(self, value=20):
        """  Corresponds to IDD Field `Maximum HVAC Iterations`

        Args:
            value (int): value for IDD Field `Maximum HVAC Iterations`
                Default value: 20
                value >= 1
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
                                     'for field `ConvergenceLimits.maximum_hvac_iterations`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ConvergenceLimits.maximum_hvac_iterations`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ConvergenceLimits.maximum_hvac_iterations`')
        self._data["Maximum HVAC Iterations"] = value

    @property
    def minimum_plant_iterations(self):
        """Get minimum_plant_iterations

        Returns:
            int: the value of `minimum_plant_iterations` or None if not set
        """
        return self._data["Minimum Plant Iterations"]

    @minimum_plant_iterations.setter
    def minimum_plant_iterations(self, value=2):
        """  Corresponds to IDD Field `Minimum Plant Iterations`
        Controls the minimum number of plant system solver iterations within a single HVAC iteration
        Larger values will increase runtime but might improve solution accuracy for complicated plant systems
        Complex plants include: several interconnected loops, heat recovery, thermal load following generators, etc.

        Args:
            value (int): value for IDD Field `Minimum Plant Iterations`
                Default value: 2
                value >= 1
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
                                     'for field `ConvergenceLimits.minimum_plant_iterations`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ConvergenceLimits.minimum_plant_iterations`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ConvergenceLimits.minimum_plant_iterations`')
        self._data["Minimum Plant Iterations"] = value

    @property
    def maximum_plant_iterations(self):
        """Get maximum_plant_iterations

        Returns:
            int: the value of `maximum_plant_iterations` or None if not set
        """
        return self._data["Maximum Plant Iterations"]

    @maximum_plant_iterations.setter
    def maximum_plant_iterations(self, value=8):
        """  Corresponds to IDD Field `Maximum Plant Iterations`
        Controls the maximum number of plant system solver iterations within a single HVAC iteration
        Smaller values might decrease runtime but could decrease solution accuracy for complicated plant systems

        Args:
            value (int): value for IDD Field `Maximum Plant Iterations`
                Default value: 8
                value >= 2
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
                                     'for field `ConvergenceLimits.maximum_plant_iterations`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ConvergenceLimits.maximum_plant_iterations`'.format(value))
            if value < 2:
                raise ValueError('value need to be greater or equal 2 '
                                 'for field `ConvergenceLimits.maximum_plant_iterations`')
        self._data["Maximum Plant Iterations"] = value

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
                    raise ValueError("Required field ConvergenceLimits:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ConvergenceLimits:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ConvergenceLimits: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ConvergenceLimits: {} / {}".format(out_fields,
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

class ProgramControl(object):
    """ Corresponds to IDD object `ProgramControl`
        used to support various efforts in time reduction for simulation including threading
    """
    internal_name = "ProgramControl"
    field_count = 1
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ProgramControl`
        """
        self._data = OrderedDict()
        self._data["Number of Threads Allowed"] = None
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
            self.number_of_threads_allowed = None
        else:
            self.number_of_threads_allowed = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def number_of_threads_allowed(self):
        """Get number_of_threads_allowed

        Returns:
            int: the value of `number_of_threads_allowed` or None if not set
        """
        return self._data["Number of Threads Allowed"]

    @number_of_threads_allowed.setter
    def number_of_threads_allowed(self, value=None):
        """  Corresponds to IDD Field `Number of Threads Allowed`
        This is currently used only in the Interior Radiant Exchange module -- view factors on # surfaces
        if value is 0, then maximum number allowed will be used.

        Args:
            value (int): value for IDD Field `Number of Threads Allowed`
                value >= 0
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
                                     'for field `ProgramControl.number_of_threads_allowed`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ProgramControl.number_of_threads_allowed`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `ProgramControl.number_of_threads_allowed`')
        self._data["Number of Threads Allowed"] = value

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
                    raise ValueError("Required field ProgramControl:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ProgramControl:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ProgramControl: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ProgramControl: {} / {}".format(out_fields,
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