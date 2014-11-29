from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SimulationControl`
        """
        self._data = OrderedDict()
        self._data["Do Zone Sizing Calculation"] = None
        self._data["Do System Sizing Calculation"] = None
        self._data["Do Plant Sizing Calculation"] = None
        self._data["Run Simulation for Sizing Periods"] = None
        self._data["Run Simulation for Weather File Run Periods"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.do_zone_sizing_calculation = None
        else:
            self.do_zone_sizing_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.do_system_sizing_calculation = None
        else:
            self.do_system_sizing_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.do_plant_sizing_calculation = None
        else:
            self.do_plant_sizing_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.run_simulation_for_sizing_periods = None
        else:
            self.run_simulation_for_sizing_periods = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.run_simulation_for_weather_file_run_periods = None
        else:
            self.run_simulation_for_weather_file_run_periods = vals[i]
        i += 1

    @property
    def do_zone_sizing_calculation(self):
        """Get do_zone_sizing_calculation

        Returns:
            str: the value of `do_zone_sizing_calculation` or None if not set
        """
        return self._data["Do Zone Sizing Calculation"]

    @do_zone_sizing_calculation.setter
    def do_zone_sizing_calculation(self, value="No"):
        """  Corresponds to IDD Field `do_zone_sizing_calculation`
        If Yes, Zone sizing is accomplished from corresponding Sizing:Zone objects
        and autosize fields.

        Args:
            value (str): value for IDD Field `do_zone_sizing_calculation`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `do_zone_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `do_zone_sizing_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `do_zone_sizing_calculation`'.format(value))

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
        """  Corresponds to IDD Field `do_system_sizing_calculation`
        If Yes, System sizing is accomplished from corresponding Sizing:System objects
        and autosize fields.
        If Yes, Zone sizing (previous field) must also be Yes.

        Args:
            value (str): value for IDD Field `do_system_sizing_calculation`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `do_system_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `do_system_sizing_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `do_system_sizing_calculation`'.format(value))

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
        """  Corresponds to IDD Field `do_plant_sizing_calculation`
        If Yes, Plant sizing is accomplished from corresponding Sizing:Plant objects
        and autosize fields.

        Args:
            value (str): value for IDD Field `do_plant_sizing_calculation`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `do_plant_sizing_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `do_plant_sizing_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `do_plant_sizing_calculation`'.format(value))

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
        """  Corresponds to IDD Field `run_simulation_for_sizing_periods`
        If Yes, SizingPeriod:* objects are executed and results from those may be displayed..

        Args:
            value (str): value for IDD Field `run_simulation_for_sizing_periods`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `run_simulation_for_sizing_periods`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_simulation_for_sizing_periods`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `run_simulation_for_sizing_periods`'.format(value))

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
        """  Corresponds to IDD Field `run_simulation_for_weather_file_run_periods`
        If Yes, RunPeriod:* objects are executed and results from those may be displayed..

        Args:
            value (str): value for IDD Field `run_simulation_for_weather_file_run_periods`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `run_simulation_for_weather_file_run_periods`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `run_simulation_for_weather_file_run_periods`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `run_simulation_for_weather_file_run_periods`'.format(value))

        self._data["Run Simulation for Weather File Run Periods"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.do_zone_sizing_calculation))
        out.append(self._to_str(self.do_system_sizing_calculation))
        out.append(self._to_str(self.do_plant_sizing_calculation))
        out.append(self._to_str(self.run_simulation_for_sizing_periods))
        out.append(self._to_str(self.run_simulation_for_weather_file_run_periods))
        return ",".join(out)