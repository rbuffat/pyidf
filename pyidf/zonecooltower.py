from collections import OrderedDict

class ZoneCoolTowerShower(object):
    """ Corresponds to IDD object `ZoneCoolTower:Shower`
        A cooltower (sometimes referred to as a wind tower or a shower cooling tower)
        models passive downdraught evaporative cooling (PDEC) that is designed to capture the
        wind at the top of a tower and cool the outdoor air using water evaporation before
        delivering it to a space.
    """
    internal_name = "ZoneCoolTower:Shower"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneCoolTower:Shower`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Water Supply Storage Tank Name"] = None
        self._data["Flow Control Type"] = None
        self._data["Pump Flow Rate Schedule Name"] = None
        self._data["Maximum Water Flow Rate"] = None
        self._data["Effective Tower Height"] = None
        self._data["Airflow Outlet Area"] = None
        self._data["Maximum Air Flow Rate"] = None
        self._data["Minimum Indoor Temperature"] = None
        self._data["Fraction of Water Loss"] = None
        self._data["Fraction of Flow Schedule"] = None
        self._data["Rated Power Consumption"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_supply_storage_tank_name = None
        else:
            self.water_supply_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_control_type = None
        else:
            self.flow_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_flow_rate_schedule_name = None
        else:
            self.pump_flow_rate_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_water_flow_rate = None
        else:
            self.maximum_water_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_tower_height = None
        else:
            self.effective_tower_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_outlet_area = None
        else:
            self.airflow_outlet_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_air_flow_rate = None
        else:
            self.maximum_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_indoor_temperature = None
        else:
            self.minimum_indoor_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_water_loss = None
        else:
            self.fraction_of_water_loss = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_flow_schedule = None
        else:
            self.fraction_of_flow_schedule = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_power_consumption = None
        else:
            self.rated_power_consumption = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def water_supply_storage_tank_name(self):
        """Get water_supply_storage_tank_name

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set
        """
        return self._data["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `water_supply_storage_tank_name`
        In case of stand alone tank or underground water, leave this input blank

        Args:
            value (str): value for IDD Field `water_supply_storage_tank_name`
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
                                 'for field `water_supply_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_supply_storage_tank_name`')

        self._data["Water Supply Storage Tank Name"] = value

    @property
    def flow_control_type(self):
        """Get flow_control_type

        Returns:
            str: the value of `flow_control_type` or None if not set
        """
        return self._data["Flow Control Type"]

    @flow_control_type.setter
    def flow_control_type(self, value="WindDrivenFlow"):
        """  Corresponds to IDD Field `flow_control_type`
        Water flow schedule should be selected when the water flow rate is known.
        Wind-driven flow should be selected when the water flow rate is unknown.

        Args:
            value (str): value for IDD Field `flow_control_type`
                Accepted values are:
                      - WaterFlowSchedule
                      - WindDrivenFlow
                Default value: WindDrivenFlow
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
                                 'for field `flow_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_control_type`')
            vals = set()
            vals.add("WaterFlowSchedule")
            vals.add("WindDrivenFlow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `flow_control_type`'.format(value))

        self._data["Flow Control Type"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """Get pump_flow_rate_schedule_name

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set
        """
        return self._data["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `pump_flow_rate_schedule_name`

        Args:
            value (str): value for IDD Field `pump_flow_rate_schedule_name`
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
                                 'for field `pump_flow_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_flow_rate_schedule_name`')

        self._data["Pump Flow Rate Schedule Name"] = value

    @property
    def maximum_water_flow_rate(self):
        """Get maximum_water_flow_rate

        Returns:
            float: the value of `maximum_water_flow_rate` or None if not set
        """
        return self._data["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_water_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_water_flow_rate`
                Unit: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_water_flow_rate`'.format(value))

        self._data["Maximum Water Flow Rate"] = value

    @property
    def effective_tower_height(self):
        """Get effective_tower_height

        Returns:
            float: the value of `effective_tower_height` or None if not set
        """
        return self._data["Effective Tower Height"]

    @effective_tower_height.setter
    def effective_tower_height(self, value=None):
        """  Corresponds to IDD Field `effective_tower_height`
        This field is from either the spray or the wet pad to the top of the outlet.

        Args:
            value (float): value for IDD Field `effective_tower_height`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `effective_tower_height`'.format(value))

        self._data["Effective Tower Height"] = value

    @property
    def airflow_outlet_area(self):
        """Get airflow_outlet_area

        Returns:
            float: the value of `airflow_outlet_area` or None if not set
        """
        return self._data["Airflow Outlet Area"]

    @airflow_outlet_area.setter
    def airflow_outlet_area(self, value=None):
        """  Corresponds to IDD Field `airflow_outlet_area`
        User have to specify effective area when outlet area is relatively bigger than the cross sectional area
        of cooltower. If the number of outlet is more than one, assume the air passes through only one.

        Args:
            value (float): value for IDD Field `airflow_outlet_area`
                Unit: m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `airflow_outlet_area`'.format(value))

        self._data["Airflow Outlet Area"] = value

    @property
    def maximum_air_flow_rate(self):
        """Get maximum_air_flow_rate

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set
        """
        return self._data["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Unit: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

        self._data["Maximum Air Flow Rate"] = value

    @property
    def minimum_indoor_temperature(self):
        """Get minimum_indoor_temperature

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set
        """
        return self._data["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=None):
        """  Corresponds to IDD Field `minimum_indoor_temperature`
        This field is to specify the indoor temperature below which cooltower is shutoff.

        Args:
            value (float): value for IDD Field `minimum_indoor_temperature`
                Unit: C
                value >= -100.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_indoor_temperature`'.format(value))
            if value < -100.0:
                raise ValueError('value need to be greater or equal -100.0 '
                                 'for field `minimum_indoor_temperature`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `minimum_indoor_temperature`')

        self._data["Minimum Indoor Temperature"] = value

    @property
    def fraction_of_water_loss(self):
        """Get fraction_of_water_loss

        Returns:
            float: the value of `fraction_of_water_loss` or None if not set
        """
        return self._data["Fraction of Water Loss"]

    @fraction_of_water_loss.setter
    def fraction_of_water_loss(self, value=None):
        """  Corresponds to IDD Field `fraction_of_water_loss`

        Args:
            value (float): value for IDD Field `fraction_of_water_loss`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_water_loss`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_water_loss`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_water_loss`')

        self._data["Fraction of Water Loss"] = value

    @property
    def fraction_of_flow_schedule(self):
        """Get fraction_of_flow_schedule

        Returns:
            float: the value of `fraction_of_flow_schedule` or None if not set
        """
        return self._data["Fraction of Flow Schedule"]

    @fraction_of_flow_schedule.setter
    def fraction_of_flow_schedule(self, value=None):
        """  Corresponds to IDD Field `fraction_of_flow_schedule`

        Args:
            value (float): value for IDD Field `fraction_of_flow_schedule`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_flow_schedule`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_flow_schedule`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_flow_schedule`')

        self._data["Fraction of Flow Schedule"] = value

    @property
    def rated_power_consumption(self):
        """Get rated_power_consumption

        Returns:
            float: the value of `rated_power_consumption` or None if not set
        """
        return self._data["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """  Corresponds to IDD Field `rated_power_consumption`

        Args:
            value (float): value for IDD Field `rated_power_consumption`
                Unit: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `rated_power_consumption`'.format(value))

        self._data["Rated Power Consumption"] = value

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
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.water_supply_storage_tank_name))
        out.append(self._to_str(self.flow_control_type))
        out.append(self._to_str(self.pump_flow_rate_schedule_name))
        out.append(self._to_str(self.maximum_water_flow_rate))
        out.append(self._to_str(self.effective_tower_height))
        out.append(self._to_str(self.airflow_outlet_area))
        out.append(self._to_str(self.maximum_air_flow_rate))
        out.append(self._to_str(self.minimum_indoor_temperature))
        out.append(self._to_str(self.fraction_of_water_loss))
        out.append(self._to_str(self.fraction_of_flow_schedule))
        out.append(self._to_str(self.rated_power_consumption))
        return ",".join(out)