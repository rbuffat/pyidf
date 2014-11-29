from collections import OrderedDict

class DistrictHeating(object):
    """ Corresponds to IDD object `DistrictHeating`
        Centralized source of hot water, such as a district heating system.
    """
    internal_name = "DistrictHeating"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DistrictHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Hot Water Inlet Node Name"] = None
        self._data["Hot Water Outlet Node Name"] = None
        self._data["Nominal Capacity"] = None
        self._data["Capacity Fraction Schedule Name"] = None

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
            self.hot_water_inlet_node_name = None
        else:
            self.hot_water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hot_water_outlet_node_name = None
        else:
            self.hot_water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_capacity = None
        else:
            self.nominal_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity_fraction_schedule_name = None
        else:
            self.capacity_fraction_schedule_name = vals[i]
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
    def hot_water_inlet_node_name(self):
        """Get hot_water_inlet_node_name

        Returns:
            str: the value of `hot_water_inlet_node_name` or None if not set
        """
        return self._data["Hot Water Inlet Node Name"]

    @hot_water_inlet_node_name.setter
    def hot_water_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_inlet_node_name`
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
                                 'for field `hot_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_inlet_node_name`')

        self._data["Hot Water Inlet Node Name"] = value

    @property
    def hot_water_outlet_node_name(self):
        """Get hot_water_outlet_node_name

        Returns:
            str: the value of `hot_water_outlet_node_name` or None if not set
        """
        return self._data["Hot Water Outlet Node Name"]

    @hot_water_outlet_node_name.setter
    def hot_water_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `hot_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_outlet_node_name`
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
                                 'for field `hot_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_outlet_node_name`')

        self._data["Hot Water Outlet Node Name"] = value

    @property
    def nominal_capacity(self):
        """Get nominal_capacity

        Returns:
            float: the value of `nominal_capacity` or None if not set
        """
        return self._data["Nominal Capacity"]

    @nominal_capacity.setter
    def nominal_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_capacity`

        Args:
            value (float): value for IDD Field `nominal_capacity`
                Unit: W
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
                                 'for field `nominal_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_capacity`')

        self._data["Nominal Capacity"] = value

    @property
    def capacity_fraction_schedule_name(self):
        """Get capacity_fraction_schedule_name

        Returns:
            str: the value of `capacity_fraction_schedule_name` or None if not set
        """
        return self._data["Capacity Fraction Schedule Name"]

    @capacity_fraction_schedule_name.setter
    def capacity_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `capacity_fraction_schedule_name`
        Schedule values are multiplied by Nominal Capacity for current capacity

        Args:
            value (str): value for IDD Field `capacity_fraction_schedule_name`
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
                                 'for field `capacity_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `capacity_fraction_schedule_name`')

        self._data["Capacity Fraction Schedule Name"] = value

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
        out.append(self._to_str(self.hot_water_inlet_node_name))
        out.append(self._to_str(self.hot_water_outlet_node_name))
        out.append(self._to_str(self.nominal_capacity))
        out.append(self._to_str(self.capacity_fraction_schedule_name))
        return ",".join(out)