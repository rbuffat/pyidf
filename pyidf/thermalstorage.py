from collections import OrderedDict

class ThermalStorageIceSimple(object):
    """ Corresponds to IDD object `ThermalStorage:Ice:Simple`
        This ice storage model is a simplified model
        It requires a setpoint placed on the Chilled Water Side Outlet Node
        It should be placed in the chilled water supply side outlet branch
        followed by a pipe.
        Use the PlantEquipmentOperation:ComponentSetpoint plant operation scheme.
    """
    internal_name = "ThermalStorage:Ice:Simple"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermalStorage:Ice:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Ice Storage Type"] = None
        self._data["Capacity"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None

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
            self.ice_storage_type = None
        else:
            self.ice_storage_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.capacity = None
        else:
            self.capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
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
    def ice_storage_type(self):
        """Get ice_storage_type

        Returns:
            str: the value of `ice_storage_type` or None if not set
        """
        return self._data["Ice Storage Type"]

    @ice_storage_type.setter
    def ice_storage_type(self, value=None):
        """  Corresponds to IDD Field `ice_storage_type`
        IceOnCoilInternal = Ice-on-Coil, internal melt
        IceOnCoilExternal = Ice-on-Coil, external melt

        Args:
            value (str): value for IDD Field `ice_storage_type`
                Accepted values are:
                      - IceOnCoilInternal
                      - IceOnCoilExternal
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
                                 'for field `ice_storage_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ice_storage_type`')
            vals = set()
            vals.add("IceOnCoilInternal")
            vals.add("IceOnCoilExternal")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ice_storage_type`'.format(value))

        self._data["Ice Storage Type"] = value

    @property
    def capacity(self):
        """Get capacity

        Returns:
            float: the value of `capacity` or None if not set
        """
        return self._data["Capacity"]

    @capacity.setter
    def capacity(self, value=None):
        """  Corresponds to IDD Field `capacity`

        Args:
            value (float): value for IDD Field `capacity`
                Unit: GJ
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
                                 'for field `capacity`'.format(value))

        self._data["Capacity"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
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
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')

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
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
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
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

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
        out.append(self._to_str(self.ice_storage_type))
        out.append(self._to_str(self.capacity))
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        return ",".join(out)

class ThermalStorageIceDetailed(object):
    """ Corresponds to IDD object `ThermalStorage:Ice:Detailed`
        This input syntax is intended to describe a thermal storage system that
        includes smaller containers filled with water that are placed in a larger
        tank or series of tanks.
        The model uses polynomial equations to describe the system performance.
    """
    internal_name = "ThermalStorage:Ice:Detailed"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermalStorage:Ice:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Capacity"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Discharging Curve Object Type"] = None
        self._data["Discharging Curve Name"] = None
        self._data["Charging Curve Object Type"] = None
        self._data["Charging Curve Name"] = None
        self._data["Timestep of the Curve Data"] = None
        self._data["Parasitic Electric Load During Discharging"] = None
        self._data["Parasitic Electric Load During Charging"] = None
        self._data["Tank Loss Coefficient"] = None
        self._data["Freezing Temperature of Storage Medium"] = None
        self._data["Thaw Process Indicator"] = None

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
            self.capacity = None
        else:
            self.capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharging_curve_object_type = None
        else:
            self.discharging_curve_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharging_curve_name = None
        else:
            self.discharging_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.charging_curve_object_type = None
        else:
            self.charging_curve_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.charging_curve_name = None
        else:
            self.charging_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.timestep_of_the_curve_data = None
        else:
            self.timestep_of_the_curve_data = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.parasitic_electric_load_during_discharging = None
        else:
            self.parasitic_electric_load_during_discharging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.parasitic_electric_load_during_charging = None
        else:
            self.parasitic_electric_load_during_charging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tank_loss_coefficient = None
        else:
            self.tank_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.freezing_temperature_of_storage_medium = None
        else:
            self.freezing_temperature_of_storage_medium = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thaw_process_indicator = None
        else:
            self.thaw_process_indicator = vals[i]
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
    def capacity(self):
        """Get capacity

        Returns:
            float: the value of `capacity` or None if not set
        """
        return self._data["Capacity"]

    @capacity.setter
    def capacity(self, value=None):
        """  Corresponds to IDD Field `capacity`
        This includes only the latent storage capacity

        Args:
            value (float): value for IDD Field `capacity`
                Unit: GJ
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
                                 'for field `capacity`'.format(value))

        self._data["Capacity"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
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
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')

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
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
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
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def discharging_curve_object_type(self):
        """Get discharging_curve_object_type

        Returns:
            str: the value of `discharging_curve_object_type` or None if not set
        """
        return self._data["Discharging Curve Object Type"]

    @discharging_curve_object_type.setter
    def discharging_curve_object_type(self, value=None):
        """  Corresponds to IDD Field `discharging_curve_object_type`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `discharging_curve_object_type`
                Accepted values are:
                      - Curve:QuadraticLinear
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
                                 'for field `discharging_curve_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `discharging_curve_object_type`')
            vals = set()
            vals.add("Curve:QuadraticLinear")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `discharging_curve_object_type`'.format(value))

        self._data["Discharging Curve Object Type"] = value

    @property
    def discharging_curve_name(self):
        """Get discharging_curve_name

        Returns:
            str: the value of `discharging_curve_name` or None if not set
        """
        return self._data["Discharging Curve Name"]

    @discharging_curve_name.setter
    def discharging_curve_name(self, value=None):
        """  Corresponds to IDD Field `discharging_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `discharging_curve_name`
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
                                 'for field `discharging_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `discharging_curve_name`')

        self._data["Discharging Curve Name"] = value

    @property
    def charging_curve_object_type(self):
        """Get charging_curve_object_type

        Returns:
            str: the value of `charging_curve_object_type` or None if not set
        """
        return self._data["Charging Curve Object Type"]

    @charging_curve_object_type.setter
    def charging_curve_object_type(self, value=None):
        """  Corresponds to IDD Field `charging_curve_object_type`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `charging_curve_object_type`
                Accepted values are:
                      - Curve:QuadraticLinear
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
                                 'for field `charging_curve_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `charging_curve_object_type`')
            vals = set()
            vals.add("Curve:QuadraticLinear")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `charging_curve_object_type`'.format(value))

        self._data["Charging Curve Object Type"] = value

    @property
    def charging_curve_name(self):
        """Get charging_curve_name

        Returns:
            str: the value of `charging_curve_name` or None if not set
        """
        return self._data["Charging Curve Name"]

    @charging_curve_name.setter
    def charging_curve_name(self, value=None):
        """  Corresponds to IDD Field `charging_curve_name`
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `charging_curve_name`
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
                                 'for field `charging_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `charging_curve_name`')

        self._data["Charging Curve Name"] = value

    @property
    def timestep_of_the_curve_data(self):
        """Get timestep_of_the_curve_data

        Returns:
            float: the value of `timestep_of_the_curve_data` or None if not set
        """
        return self._data["Timestep of the Curve Data"]

    @timestep_of_the_curve_data.setter
    def timestep_of_the_curve_data(self, value=None):
        """  Corresponds to IDD Field `timestep_of_the_curve_data`

        Args:
            value (float): value for IDD Field `timestep_of_the_curve_data`
                Unit: hr
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
                                 'for field `timestep_of_the_curve_data`'.format(value))

        self._data["Timestep of the Curve Data"] = value

    @property
    def parasitic_electric_load_during_discharging(self):
        """Get parasitic_electric_load_during_discharging

        Returns:
            float: the value of `parasitic_electric_load_during_discharging` or None if not set
        """
        return self._data["Parasitic Electric Load During Discharging"]

    @parasitic_electric_load_during_discharging.setter
    def parasitic_electric_load_during_discharging(self, value=None):
        """  Corresponds to IDD Field `parasitic_electric_load_during_discharging`

        Args:
            value (float): value for IDD Field `parasitic_electric_load_during_discharging`
                Unit: dimensionless
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
                                 'for field `parasitic_electric_load_during_discharging`'.format(value))

        self._data["Parasitic Electric Load During Discharging"] = value

    @property
    def parasitic_electric_load_during_charging(self):
        """Get parasitic_electric_load_during_charging

        Returns:
            float: the value of `parasitic_electric_load_during_charging` or None if not set
        """
        return self._data["Parasitic Electric Load During Charging"]

    @parasitic_electric_load_during_charging.setter
    def parasitic_electric_load_during_charging(self, value=None):
        """  Corresponds to IDD Field `parasitic_electric_load_during_charging`

        Args:
            value (float): value for IDD Field `parasitic_electric_load_during_charging`
                Unit: dimensionless
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
                                 'for field `parasitic_electric_load_during_charging`'.format(value))

        self._data["Parasitic Electric Load During Charging"] = value

    @property
    def tank_loss_coefficient(self):
        """Get tank_loss_coefficient

        Returns:
            float: the value of `tank_loss_coefficient` or None if not set
        """
        return self._data["Tank Loss Coefficient"]

    @tank_loss_coefficient.setter
    def tank_loss_coefficient(self, value=None):
        """  Corresponds to IDD Field `tank_loss_coefficient`
        This is the fraction the total storage capacity that is lost or melts
        each hour

        Args:
            value (float): value for IDD Field `tank_loss_coefficient`
                Unit: dimensionless
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
                                 'for field `tank_loss_coefficient`'.format(value))

        self._data["Tank Loss Coefficient"] = value

    @property
    def freezing_temperature_of_storage_medium(self):
        """Get freezing_temperature_of_storage_medium

        Returns:
            float: the value of `freezing_temperature_of_storage_medium` or None if not set
        """
        return self._data["Freezing Temperature of Storage Medium"]

    @freezing_temperature_of_storage_medium.setter
    def freezing_temperature_of_storage_medium(self, value=0.0 ):
        """  Corresponds to IDD Field `freezing_temperature_of_storage_medium`
        This temperature is typically 0C for water.
        Simply changing this temperature without adjusting the performance
        parameters input above is inappropriate and not advised.

        Args:
            value (float): value for IDD Field `freezing_temperature_of_storage_medium`
                Unit: C
                Default value: 0.0
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
                                 'for field `freezing_temperature_of_storage_medium`'.format(value))

        self._data["Freezing Temperature of Storage Medium"] = value

    @property
    def thaw_process_indicator(self):
        """Get thaw_process_indicator

        Returns:
            str: the value of `thaw_process_indicator` or None if not set
        """
        return self._data["Thaw Process Indicator"]

    @thaw_process_indicator.setter
    def thaw_process_indicator(self, value="OutsideMelt"):
        """  Corresponds to IDD Field `thaw_process_indicator`
        This field determines whether the system uses internal or external melt
        during discharging.  This will then have an impact on charging performance.

        Args:
            value (str): value for IDD Field `thaw_process_indicator`
                Accepted values are:
                      - InsideMelt
                      - OutsideMelt
                Default value: OutsideMelt
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
                                 'for field `thaw_process_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thaw_process_indicator`')
            vals = set()
            vals.add("InsideMelt")
            vals.add("OutsideMelt")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thaw_process_indicator`'.format(value))

        self._data["Thaw Process Indicator"] = value

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
        out.append(self._to_str(self.capacity))
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.discharging_curve_object_type))
        out.append(self._to_str(self.discharging_curve_name))
        out.append(self._to_str(self.charging_curve_object_type))
        out.append(self._to_str(self.charging_curve_name))
        out.append(self._to_str(self.timestep_of_the_curve_data))
        out.append(self._to_str(self.parasitic_electric_load_during_discharging))
        out.append(self._to_str(self.parasitic_electric_load_during_charging))
        out.append(self._to_str(self.tank_loss_coefficient))
        out.append(self._to_str(self.freezing_temperature_of_storage_medium))
        out.append(self._to_str(self.thaw_process_indicator))
        return ",".join(out)

class ThermalStorageChilledWaterMixed(object):
    """ Corresponds to IDD object `ThermalStorage:ChilledWater:Mixed`
        Chilled water storage with a well-mixed, single-node tank. The chilled water is
        "used" by drawing from the "Use Side" of the water tank.  The tank is indirectly
        charged by circulating cold water through the "Source Side" of the water tank.
    """
    internal_name = "ThermalStorage:ChilledWater:Mixed"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermalStorage:ChilledWater:Mixed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tank Volume"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
        self._data["Deadband Temperature Difference"] = None
        self._data["Minimum Temperature Limit"] = None
        self._data["Nominal Cooling Capacity"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Heat Gain Coefficient from Ambient Temperature"] = None
        self._data["Use Side Inlet Node Name"] = None
        self._data["Use Side Outlet Node Name"] = None
        self._data["Use Side Heat Transfer Effectiveness"] = None
        self._data["Use Side Availability Schedule Name"] = None
        self._data["Use Side Design Flow Rate"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Source Side Heat Transfer Effectiveness"] = None
        self._data["Source Side Availability Schedule Name"] = None
        self._data["Source Side Design Flow Rate"] = None
        self._data["Tank Recovery Time"] = None

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
            self.tank_volume = None
        else:
            self.tank_volume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deadband_temperature_difference = None
        else:
            self.deadband_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_temperature_limit = None
        else:
            self.minimum_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cooling_capacity = None
        else:
            self.nominal_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_gain_coefficient_from_ambient_temperature = None
        else:
            self.heat_gain_coefficient_from_ambient_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_inlet_node_name = None
        else:
            self.use_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_outlet_node_name = None
        else:
            self.use_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_heat_transfer_effectiveness = None
        else:
            self.use_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_availability_schedule_name = None
        else:
            self.use_side_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_design_flow_rate = None
        else:
            self.use_side_design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_heat_transfer_effectiveness = None
        else:
            self.source_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_availability_schedule_name = None
        else:
            self.source_side_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_design_flow_rate = None
        else:
            self.source_side_design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tank_recovery_time = None
        else:
            self.tank_recovery_time = vals[i]
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
    def tank_volume(self):
        """Get tank_volume

        Returns:
            float: the value of `tank_volume` or None if not set
        """
        return self._data["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=0.1 ):
        """  Corresponds to IDD Field `tank_volume`

        Args:
            value (float): value for IDD Field `tank_volume`
                Unit: m3
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `tank_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_volume`')

        self._data["Tank Volume"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
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
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """Get deadband_temperature_difference

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set
        """
        return self._data["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=0.5 ):
        """  Corresponds to IDD Field `deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `deadband_temperature_difference`
                Unit: deltaC
                Default value: 0.5
                value > 0.0
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
                                 'for field `deadband_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `deadband_temperature_difference`')

        self._data["Deadband Temperature Difference"] = value

    @property
    def minimum_temperature_limit(self):
        """Get minimum_temperature_limit

        Returns:
            float: the value of `minimum_temperature_limit` or None if not set
        """
        return self._data["Minimum Temperature Limit"]

    @minimum_temperature_limit.setter
    def minimum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `minimum_temperature_limit`

        Args:
            value (float): value for IDD Field `minimum_temperature_limit`
                Unit: C
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
                                 'for field `minimum_temperature_limit`'.format(value))

        self._data["Minimum Temperature Limit"] = value

    @property
    def nominal_cooling_capacity(self):
        """Get nominal_cooling_capacity

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set
        """
        return self._data["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_cooling_capacity`

        Args:
            value (float): value for IDD Field `nominal_cooling_capacity`
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
                                 'for field `nominal_cooling_capacity`'.format(value))

        self._data["Nominal Cooling Capacity"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_indicator`

        Args:
            value (str): value for IDD Field `ambient_temperature_indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
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
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            vals = set()
            vals.add("Schedule")
            vals.add("Zone")
            vals.add("Outdoors")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ambient_temperature_indicator`'.format(value))

        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
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
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
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
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`
        required when field Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
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
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def heat_gain_coefficient_from_ambient_temperature(self):
        """Get heat_gain_coefficient_from_ambient_temperature

        Returns:
            float: the value of `heat_gain_coefficient_from_ambient_temperature` or None if not set
        """
        return self._data["Heat Gain Coefficient from Ambient Temperature"]

    @heat_gain_coefficient_from_ambient_temperature.setter
    def heat_gain_coefficient_from_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `heat_gain_coefficient_from_ambient_temperature`

        Args:
            value (float): value for IDD Field `heat_gain_coefficient_from_ambient_temperature`
                Unit: W/K
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
                                 'for field `heat_gain_coefficient_from_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heat_gain_coefficient_from_ambient_temperature`')

        self._data["Heat Gain Coefficient from Ambient Temperature"] = value

    @property
    def use_side_inlet_node_name(self):
        """Get use_side_inlet_node_name

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set
        """
        return self._data["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_inlet_node_name`
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
                                 'for field `use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_inlet_node_name`')

        self._data["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """Get use_side_outlet_node_name

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set
        """
        return self._data["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_outlet_node_name`
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
                                 'for field `use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_outlet_node_name`')

        self._data["Use Side Outlet Node Name"] = value

    @property
    def use_side_heat_transfer_effectiveness(self):
        """Get use_side_heat_transfer_effectiveness

        Returns:
            float: the value of `use_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Use Side Heat Transfer Effectiveness"]

    @use_side_heat_transfer_effectiveness.setter
    def use_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `use_side_heat_transfer_effectiveness`

        Args:
            value (float): value for IDD Field `use_side_heat_transfer_effectiveness`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `use_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')

        self._data["Use Side Heat Transfer Effectiveness"] = value

    @property
    def use_side_availability_schedule_name(self):
        """Get use_side_availability_schedule_name

        Returns:
            str: the value of `use_side_availability_schedule_name` or None if not set
        """
        return self._data["Use Side Availability Schedule Name"]

    @use_side_availability_schedule_name.setter
    def use_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `use_side_availability_schedule_name`
        Availability schedule name for use side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `use_side_availability_schedule_name`
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
                                 'for field `use_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_availability_schedule_name`')

        self._data["Use Side Availability Schedule Name"] = value

    @property
    def use_side_design_flow_rate(self):
        """Get use_side_design_flow_rate

        Returns:
            float: the value of `use_side_design_flow_rate` or None if not set
        """
        return self._data["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `use_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `use_side_design_flow_rate`
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
                                 'for field `use_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_design_flow_rate`')

        self._data["Use Side Design Flow Rate"] = value

    @property
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
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
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
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
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def source_side_heat_transfer_effectiveness(self):
        """Get source_side_heat_transfer_effectiveness

        Returns:
            float: the value of `source_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Source Side Heat Transfer Effectiveness"]

    @source_side_heat_transfer_effectiveness.setter
    def source_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `source_side_heat_transfer_effectiveness`

        Args:
            value (float): value for IDD Field `source_side_heat_transfer_effectiveness`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `source_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')

        self._data["Source Side Heat Transfer Effectiveness"] = value

    @property
    def source_side_availability_schedule_name(self):
        """Get source_side_availability_schedule_name

        Returns:
            str: the value of `source_side_availability_schedule_name` or None if not set
        """
        return self._data["Source Side Availability Schedule Name"]

    @source_side_availability_schedule_name.setter
    def source_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `source_side_availability_schedule_name`
        Availability schedule name for source side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `source_side_availability_schedule_name`
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
                                 'for field `source_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_availability_schedule_name`')

        self._data["Source Side Availability Schedule Name"] = value

    @property
    def source_side_design_flow_rate(self):
        """Get source_side_design_flow_rate

        Returns:
            float: the value of `source_side_design_flow_rate` or None if not set
        """
        return self._data["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_design_flow_rate`
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
                                 'for field `source_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_design_flow_rate`')

        self._data["Source Side Design Flow Rate"] = value

    @property
    def tank_recovery_time(self):
        """Get tank_recovery_time

        Returns:
            float: the value of `tank_recovery_time` or None if not set
        """
        return self._data["Tank Recovery Time"]

    @tank_recovery_time.setter
    def tank_recovery_time(self, value=4.0 ):
        """  Corresponds to IDD Field `tank_recovery_time`
        Parameter for autosizing design flow rates for indirectly cooled water tanks
        time required to lower temperature of entire tank from 14.4C to 9.0C

        Args:
            value (float): value for IDD Field `tank_recovery_time`
                Unit: hr
                Default value: 4.0
                value > 0.0
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
                                 'for field `tank_recovery_time`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_recovery_time`')

        self._data["Tank Recovery Time"] = value

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
        out.append(self._to_str(self.tank_volume))
        out.append(self._to_str(self.setpoint_temperature_schedule_name))
        out.append(self._to_str(self.deadband_temperature_difference))
        out.append(self._to_str(self.minimum_temperature_limit))
        out.append(self._to_str(self.nominal_cooling_capacity))
        out.append(self._to_str(self.ambient_temperature_indicator))
        out.append(self._to_str(self.ambient_temperature_schedule_name))
        out.append(self._to_str(self.ambient_temperature_zone_name))
        out.append(self._to_str(self.ambient_temperature_outdoor_air_node_name))
        out.append(self._to_str(self.heat_gain_coefficient_from_ambient_temperature))
        out.append(self._to_str(self.use_side_inlet_node_name))
        out.append(self._to_str(self.use_side_outlet_node_name))
        out.append(self._to_str(self.use_side_heat_transfer_effectiveness))
        out.append(self._to_str(self.use_side_availability_schedule_name))
        out.append(self._to_str(self.use_side_design_flow_rate))
        out.append(self._to_str(self.source_side_inlet_node_name))
        out.append(self._to_str(self.source_side_outlet_node_name))
        out.append(self._to_str(self.source_side_heat_transfer_effectiveness))
        out.append(self._to_str(self.source_side_availability_schedule_name))
        out.append(self._to_str(self.source_side_design_flow_rate))
        out.append(self._to_str(self.tank_recovery_time))
        return ",".join(out)

class ThermalStorageChilledWaterStratified(object):
    """ Corresponds to IDD object `ThermalStorage:ChilledWater:Stratified`
        Chilled water storage with astratified, multi-node tank. The chilled water is
        "used" by drawing from the "Use Side" of the water tank.  The tank is indirectly
        charged by circulating cold water through the "Source Side" of the water tank.
    """
    internal_name = "ThermalStorage:ChilledWater:Stratified"
    field_count = 43

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ThermalStorage:ChilledWater:Stratified`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Tank Volume"] = None
        self._data["Tank Height"] = None
        self._data["Tank Shape"] = None
        self._data["Tank Perimeter"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
        self._data["Deadband Temperature Difference"] = None
        self._data["Temperature Sensor Height"] = None
        self._data["Minimum Temperature Limit"] = None
        self._data["Nominal Cooling Capacity"] = None
        self._data["Ambient Temperature Indicator"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = None
        self._data["Use Side Inlet Node Name"] = None
        self._data["Use Side Outlet Node Name"] = None
        self._data["Use Side Heat Transfer Effectiveness"] = None
        self._data["Use Side Availability Schedule Name"] = None
        self._data["Use Side Inlet Height"] = None
        self._data["Use Side Outlet Height"] = None
        self._data["Use Side Design Flow Rate"] = None
        self._data["Source Side Inlet Node Name"] = None
        self._data["Source Side Outlet Node Name"] = None
        self._data["Source Side Heat Transfer Effectiveness"] = None
        self._data["Source Side Availability Schedule Name"] = None
        self._data["Source Side Inlet Height"] = None
        self._data["Source Side Outlet Height"] = None
        self._data["Source Side Design Flow Rate"] = None
        self._data["Tank Recovery Time"] = None
        self._data["Inlet Mode"] = None
        self._data["Number of Nodes"] = None
        self._data["Additional Destratification Conductivity"] = None
        self._data["Node 1 Additional Loss Coefficient"] = None
        self._data["Node 2 Additional Loss Coefficient"] = None
        self._data["Node 3 Additional Loss Coefficient"] = None
        self._data["Node 4 Additional Loss Coefficient"] = None
        self._data["Node 5 Additional Loss Coefficient"] = None
        self._data["Node 6 Additional Loss Coefficient"] = None
        self._data["Node 7 Additional Loss Coefficient"] = None
        self._data["Node 8 Additional Loss Coefficient"] = None
        self._data["Node 9 Additional Loss Coefficient"] = None
        self._data["Node 10 Additional Loss Coefficient"] = None

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
            self.tank_volume = None
        else:
            self.tank_volume = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tank_height = None
        else:
            self.tank_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tank_shape = None
        else:
            self.tank_shape = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tank_perimeter = None
        else:
            self.tank_perimeter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deadband_temperature_difference = None
        else:
            self.deadband_temperature_difference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_sensor_height = None
        else:
            self.temperature_sensor_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_temperature_limit = None
        else:
            self.minimum_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_cooling_capacity = None
        else:
            self.nominal_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_indicator = None
        else:
            self.ambient_temperature_indicator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = None
        else:
            self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_inlet_node_name = None
        else:
            self.use_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_outlet_node_name = None
        else:
            self.use_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_heat_transfer_effectiveness = None
        else:
            self.use_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_availability_schedule_name = None
        else:
            self.use_side_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_inlet_height = None
        else:
            self.use_side_inlet_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_outlet_height = None
        else:
            self.use_side_outlet_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.use_side_design_flow_rate = None
        else:
            self.use_side_design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_inlet_node_name = None
        else:
            self.source_side_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_node_name = None
        else:
            self.source_side_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_heat_transfer_effectiveness = None
        else:
            self.source_side_heat_transfer_effectiveness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_availability_schedule_name = None
        else:
            self.source_side_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_inlet_height = None
        else:
            self.source_side_inlet_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_outlet_height = None
        else:
            self.source_side_outlet_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_side_design_flow_rate = None
        else:
            self.source_side_design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tank_recovery_time = None
        else:
            self.tank_recovery_time = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_mode = None
        else:
            self.inlet_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_nodes = None
        else:
            self.number_of_nodes = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.additional_destratification_conductivity = None
        else:
            self.additional_destratification_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_1_additional_loss_coefficient = None
        else:
            self.node_1_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_2_additional_loss_coefficient = None
        else:
            self.node_2_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_3_additional_loss_coefficient = None
        else:
            self.node_3_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_4_additional_loss_coefficient = None
        else:
            self.node_4_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_5_additional_loss_coefficient = None
        else:
            self.node_5_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_6_additional_loss_coefficient = None
        else:
            self.node_6_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_7_additional_loss_coefficient = None
        else:
            self.node_7_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_8_additional_loss_coefficient = None
        else:
            self.node_8_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_9_additional_loss_coefficient = None
        else:
            self.node_9_additional_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_10_additional_loss_coefficient = None
        else:
            self.node_10_additional_loss_coefficient = vals[i]
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
    def tank_volume(self):
        """Get tank_volume

        Returns:
            float: the value of `tank_volume` or None if not set
        """
        return self._data["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=None):
        """  Corresponds to IDD Field `tank_volume`

        Args:
            value (float): value for IDD Field `tank_volume`
                Unit: m3
                value > 0.0
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
                                 'for field `tank_volume`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_volume`')

        self._data["Tank Volume"] = value

    @property
    def tank_height(self):
        """Get tank_height

        Returns:
            float: the value of `tank_height` or None if not set
        """
        return self._data["Tank Height"]

    @tank_height.setter
    def tank_height(self, value=None):
        """  Corresponds to IDD Field `tank_height`
        Height is measured in the axial direction for horizontal cylinders

        Args:
            value (float): value for IDD Field `tank_height`
                Unit: m
                value > 0.0
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
                                 'for field `tank_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_height`')

        self._data["Tank Height"] = value

    @property
    def tank_shape(self):
        """Get tank_shape

        Returns:
            str: the value of `tank_shape` or None if not set
        """
        return self._data["Tank Shape"]

    @tank_shape.setter
    def tank_shape(self, value="VerticalCylinder"):
        """  Corresponds to IDD Field `tank_shape`

        Args:
            value (str): value for IDD Field `tank_shape`
                Accepted values are:
                      - VerticalCylinder
                      - HorizontalCylinder
                      - Other
                Default value: VerticalCylinder
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
                                 'for field `tank_shape`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `tank_shape`')
            vals = set()
            vals.add("VerticalCylinder")
            vals.add("HorizontalCylinder")
            vals.add("Other")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `tank_shape`'.format(value))

        self._data["Tank Shape"] = value

    @property
    def tank_perimeter(self):
        """Get tank_perimeter

        Returns:
            float: the value of `tank_perimeter` or None if not set
        """
        return self._data["Tank Perimeter"]

    @tank_perimeter.setter
    def tank_perimeter(self, value=None):
        """  Corresponds to IDD Field `tank_perimeter`
        Only used if Tank Shape is Other

        Args:
            value (float): value for IDD Field `tank_perimeter`
                Unit: m
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
                                 'for field `tank_perimeter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tank_perimeter`')

        self._data["Tank Perimeter"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
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
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """Get deadband_temperature_difference

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set
        """
        return self._data["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=0.0 ):
        """  Corresponds to IDD Field `deadband_temperature_difference`

        Args:
            value (float): value for IDD Field `deadband_temperature_difference`
                Unit: deltaC
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `deadband_temperature_difference`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deadband_temperature_difference`')

        self._data["Deadband Temperature Difference"] = value

    @property
    def temperature_sensor_height(self):
        """Get temperature_sensor_height

        Returns:
            float: the value of `temperature_sensor_height` or None if not set
        """
        return self._data["Temperature Sensor Height"]

    @temperature_sensor_height.setter
    def temperature_sensor_height(self, value=None):
        """  Corresponds to IDD Field `temperature_sensor_height`

        Args:
            value (float): value for IDD Field `temperature_sensor_height`
                Unit: m
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
                                 'for field `temperature_sensor_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_sensor_height`')

        self._data["Temperature Sensor Height"] = value

    @property
    def minimum_temperature_limit(self):
        """Get minimum_temperature_limit

        Returns:
            float: the value of `minimum_temperature_limit` or None if not set
        """
        return self._data["Minimum Temperature Limit"]

    @minimum_temperature_limit.setter
    def minimum_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `minimum_temperature_limit`

        Args:
            value (float): value for IDD Field `minimum_temperature_limit`
                Unit: C
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
                                 'for field `minimum_temperature_limit`'.format(value))

        self._data["Minimum Temperature Limit"] = value

    @property
    def nominal_cooling_capacity(self):
        """Get nominal_cooling_capacity

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set
        """
        return self._data["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `nominal_cooling_capacity`

        Args:
            value (float): value for IDD Field `nominal_cooling_capacity`
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
                                 'for field `nominal_cooling_capacity`'.format(value))

        self._data["Nominal Cooling Capacity"] = value

    @property
    def ambient_temperature_indicator(self):
        """Get ambient_temperature_indicator

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set
        """
        return self._data["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_indicator`

        Args:
            value (str): value for IDD Field `ambient_temperature_indicator`
                Accepted values are:
                      - Schedule
                      - Zone
                      - Outdoors
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
                                 'for field `ambient_temperature_indicator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_indicator`')
            vals = set()
            vals.add("Schedule")
            vals.add("Zone")
            vals.add("Outdoors")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `ambient_temperature_indicator`'.format(value))

        self._data["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_schedule_name`
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
                                 'for field `ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_schedule_name`')

        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_zone_name`

        Args:
            value (str): value for IDD Field `ambient_temperature_zone_name`
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
                                 'for field `ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_zone_name`')

        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `ambient_temperature_outdoor_air_node_name`
        required for Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `ambient_temperature_outdoor_air_node_name`
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
                                 'for field `ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_temperature_outdoor_air_node_name`')

        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(self):
        """Get uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature

        Returns:
            float: the value of `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature` or None if not set
        """
        return self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"]

    @uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature.setter
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(self, value=None):
        """  Corresponds to IDD Field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`

        Args:
            value (float): value for IDD Field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`
                Unit: W/m2-K
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
                                 'for field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature`')

        self._data["Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = value

    @property
    def use_side_inlet_node_name(self):
        """Get use_side_inlet_node_name

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set
        """
        return self._data["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_inlet_node_name`
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
                                 'for field `use_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_inlet_node_name`')

        self._data["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """Get use_side_outlet_node_name

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set
        """
        return self._data["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `use_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `use_side_outlet_node_name`
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
                                 'for field `use_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_outlet_node_name`')

        self._data["Use Side Outlet Node Name"] = value

    @property
    def use_side_heat_transfer_effectiveness(self):
        """Get use_side_heat_transfer_effectiveness

        Returns:
            float: the value of `use_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Use Side Heat Transfer Effectiveness"]

    @use_side_heat_transfer_effectiveness.setter
    def use_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `use_side_heat_transfer_effectiveness`
        The use side effectiveness in the stratified tank model is a simplified analogy of
        a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        use mass flow rate that directly mixes with the tank fluid. And one minus the
        effectiveness is the fraction that bypasses the tank. The use side mass flow rate
        that bypasses the tank is mixed with the fluid or water leaving the stratified tank.

        Args:
            value (float): value for IDD Field `use_side_heat_transfer_effectiveness`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `use_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `use_side_heat_transfer_effectiveness`')

        self._data["Use Side Heat Transfer Effectiveness"] = value

    @property
    def use_side_availability_schedule_name(self):
        """Get use_side_availability_schedule_name

        Returns:
            str: the value of `use_side_availability_schedule_name` or None if not set
        """
        return self._data["Use Side Availability Schedule Name"]

    @use_side_availability_schedule_name.setter
    def use_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `use_side_availability_schedule_name`
        Availability schedule name for use side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `use_side_availability_schedule_name`
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
                                 'for field `use_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `use_side_availability_schedule_name`')

        self._data["Use Side Availability Schedule Name"] = value

    @property
    def use_side_inlet_height(self):
        """Get use_side_inlet_height

        Returns:
            float: the value of `use_side_inlet_height` or None if not set
        """
        return self._data["Use Side Inlet Height"]

    @use_side_inlet_height.setter
    def use_side_inlet_height(self, value=None):
        """  Corresponds to IDD Field `use_side_inlet_height`
        Defaults to top of tank

        Args:
            value (float): value for IDD Field `use_side_inlet_height`
                Unit: m
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
                                 'for field `use_side_inlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_inlet_height`')

        self._data["Use Side Inlet Height"] = value

    @property
    def use_side_outlet_height(self):
        """Get use_side_outlet_height

        Returns:
            float: the value of `use_side_outlet_height` or None if not set
        """
        return self._data["Use Side Outlet Height"]

    @use_side_outlet_height.setter
    def use_side_outlet_height(self, value=0.0 ):
        """  Corresponds to IDD Field `use_side_outlet_height`
        Defaults to bottom of tank

        Args:
            value (float): value for IDD Field `use_side_outlet_height`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `use_side_outlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_outlet_height`')

        self._data["Use Side Outlet Height"] = value

    @property
    def use_side_design_flow_rate(self):
        """Get use_side_design_flow_rate

        Returns:
            float: the value of `use_side_design_flow_rate` or None if not set
        """
        return self._data["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `use_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `use_side_design_flow_rate`
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
                                 'for field `use_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `use_side_design_flow_rate`')

        self._data["Use Side Design Flow Rate"] = value

    @property
    def source_side_inlet_node_name(self):
        """Get source_side_inlet_node_name

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set
        """
        return self._data["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_inlet_node_name`
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
                                 'for field `source_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_inlet_node_name`')

        self._data["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """Get source_side_outlet_node_name

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set
        """
        return self._data["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_side_outlet_node_name`
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
                                 'for field `source_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_outlet_node_name`')

        self._data["Source Side Outlet Node Name"] = value

    @property
    def source_side_heat_transfer_effectiveness(self):
        """Get source_side_heat_transfer_effectiveness

        Returns:
            float: the value of `source_side_heat_transfer_effectiveness` or None if not set
        """
        return self._data["Source Side Heat Transfer Effectiveness"]

    @source_side_heat_transfer_effectiveness.setter
    def source_side_heat_transfer_effectiveness(self, value=1.0 ):
        """  Corresponds to IDD Field `source_side_heat_transfer_effectiveness`
        The source side effectiveness in the stratified tank model is a simplified analogy of
        a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        source mass flow rate that directly mixes with the tank fluid. And one minus the
        effectiveness is the fraction that bypasses the tank. The source side mass flow rate
        that bypasses the tank is mixed with the fluid or water leaving the stratified tank.

        Args:
            value (float): value for IDD Field `source_side_heat_transfer_effectiveness`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `source_side_heat_transfer_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `source_side_heat_transfer_effectiveness`')

        self._data["Source Side Heat Transfer Effectiveness"] = value

    @property
    def source_side_availability_schedule_name(self):
        """Get source_side_availability_schedule_name

        Returns:
            str: the value of `source_side_availability_schedule_name` or None if not set
        """
        return self._data["Source Side Availability Schedule Name"]

    @source_side_availability_schedule_name.setter
    def source_side_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `source_side_availability_schedule_name`
        Availability schedule name for use side. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `source_side_availability_schedule_name`
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
                                 'for field `source_side_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_side_availability_schedule_name`')

        self._data["Source Side Availability Schedule Name"] = value

    @property
    def source_side_inlet_height(self):
        """Get source_side_inlet_height

        Returns:
            float: the value of `source_side_inlet_height` or None if not set
        """
        return self._data["Source Side Inlet Height"]

    @source_side_inlet_height.setter
    def source_side_inlet_height(self, value=0.0 ):
        """  Corresponds to IDD Field `source_side_inlet_height`
        Defaults to bottom of tank

        Args:
            value (float): value for IDD Field `source_side_inlet_height`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `source_side_inlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_inlet_height`')

        self._data["Source Side Inlet Height"] = value

    @property
    def source_side_outlet_height(self):
        """Get source_side_outlet_height

        Returns:
            float: the value of `source_side_outlet_height` or None if not set
        """
        return self._data["Source Side Outlet Height"]

    @source_side_outlet_height.setter
    def source_side_outlet_height(self, value=None):
        """  Corresponds to IDD Field `source_side_outlet_height`
        Defaults to top of tank

        Args:
            value (float): value for IDD Field `source_side_outlet_height`
                Unit: m
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
                                 'for field `source_side_outlet_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_outlet_height`')

        self._data["Source Side Outlet Height"] = value

    @property
    def source_side_design_flow_rate(self):
        """Get source_side_design_flow_rate

        Returns:
            float: the value of `source_side_design_flow_rate` or None if not set
        """
        return self._data["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `source_side_design_flow_rate`

        Args:
            value (float): value for IDD Field `source_side_design_flow_rate`
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
                                 'for field `source_side_design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `source_side_design_flow_rate`')

        self._data["Source Side Design Flow Rate"] = value

    @property
    def tank_recovery_time(self):
        """Get tank_recovery_time

        Returns:
            float: the value of `tank_recovery_time` or None if not set
        """
        return self._data["Tank Recovery Time"]

    @tank_recovery_time.setter
    def tank_recovery_time(self, value=4.0 ):
        """  Corresponds to IDD Field `tank_recovery_time`
        Parameter for autosizing design flow rates for indirectly cooled water tanks
        time required to lower temperature of entire tank from 14.4C to 9.0C

        Args:
            value (float): value for IDD Field `tank_recovery_time`
                Unit: hr
                Default value: 4.0
                value > 0.0
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
                                 'for field `tank_recovery_time`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `tank_recovery_time`')

        self._data["Tank Recovery Time"] = value

    @property
    def inlet_mode(self):
        """Get inlet_mode

        Returns:
            str: the value of `inlet_mode` or None if not set
        """
        return self._data["Inlet Mode"]

    @inlet_mode.setter
    def inlet_mode(self, value="Fixed"):
        """  Corresponds to IDD Field `inlet_mode`

        Args:
            value (str): value for IDD Field `inlet_mode`
                Accepted values are:
                      - Fixed
                      - Seeking
                Default value: Fixed
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
                                 'for field `inlet_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_mode`')
            vals = set()
            vals.add("Fixed")
            vals.add("Seeking")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `inlet_mode`'.format(value))

        self._data["Inlet Mode"] = value

    @property
    def number_of_nodes(self):
        """Get number_of_nodes

        Returns:
            int: the value of `number_of_nodes` or None if not set
        """
        return self._data["Number of Nodes"]

    @number_of_nodes.setter
    def number_of_nodes(self, value=1 ):
        """  Corresponds to IDD Field `number_of_nodes`

        Args:
            value (int): value for IDD Field `number_of_nodes`
                Default value: 1
                value >= 1
                value <= 10
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_nodes`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_nodes`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `number_of_nodes`')

        self._data["Number of Nodes"] = value

    @property
    def additional_destratification_conductivity(self):
        """Get additional_destratification_conductivity

        Returns:
            float: the value of `additional_destratification_conductivity` or None if not set
        """
        return self._data["Additional Destratification Conductivity"]

    @additional_destratification_conductivity.setter
    def additional_destratification_conductivity(self, value=0.0 ):
        """  Corresponds to IDD Field `additional_destratification_conductivity`

        Args:
            value (float): value for IDD Field `additional_destratification_conductivity`
                Unit: W/m-K
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `additional_destratification_conductivity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `additional_destratification_conductivity`')

        self._data["Additional Destratification Conductivity"] = value

    @property
    def node_1_additional_loss_coefficient(self):
        """Get node_1_additional_loss_coefficient

        Returns:
            float: the value of `node_1_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 1 Additional Loss Coefficient"]

    @node_1_additional_loss_coefficient.setter
    def node_1_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_1_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_1_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_1_additional_loss_coefficient`'.format(value))

        self._data["Node 1 Additional Loss Coefficient"] = value

    @property
    def node_2_additional_loss_coefficient(self):
        """Get node_2_additional_loss_coefficient

        Returns:
            float: the value of `node_2_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 2 Additional Loss Coefficient"]

    @node_2_additional_loss_coefficient.setter
    def node_2_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_2_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_2_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_2_additional_loss_coefficient`'.format(value))

        self._data["Node 2 Additional Loss Coefficient"] = value

    @property
    def node_3_additional_loss_coefficient(self):
        """Get node_3_additional_loss_coefficient

        Returns:
            float: the value of `node_3_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 3 Additional Loss Coefficient"]

    @node_3_additional_loss_coefficient.setter
    def node_3_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_3_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_3_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_3_additional_loss_coefficient`'.format(value))

        self._data["Node 3 Additional Loss Coefficient"] = value

    @property
    def node_4_additional_loss_coefficient(self):
        """Get node_4_additional_loss_coefficient

        Returns:
            float: the value of `node_4_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 4 Additional Loss Coefficient"]

    @node_4_additional_loss_coefficient.setter
    def node_4_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_4_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_4_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_4_additional_loss_coefficient`'.format(value))

        self._data["Node 4 Additional Loss Coefficient"] = value

    @property
    def node_5_additional_loss_coefficient(self):
        """Get node_5_additional_loss_coefficient

        Returns:
            float: the value of `node_5_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 5 Additional Loss Coefficient"]

    @node_5_additional_loss_coefficient.setter
    def node_5_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_5_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_5_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_5_additional_loss_coefficient`'.format(value))

        self._data["Node 5 Additional Loss Coefficient"] = value

    @property
    def node_6_additional_loss_coefficient(self):
        """Get node_6_additional_loss_coefficient

        Returns:
            float: the value of `node_6_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 6 Additional Loss Coefficient"]

    @node_6_additional_loss_coefficient.setter
    def node_6_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_6_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_6_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_6_additional_loss_coefficient`'.format(value))

        self._data["Node 6 Additional Loss Coefficient"] = value

    @property
    def node_7_additional_loss_coefficient(self):
        """Get node_7_additional_loss_coefficient

        Returns:
            float: the value of `node_7_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 7 Additional Loss Coefficient"]

    @node_7_additional_loss_coefficient.setter
    def node_7_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_7_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_7_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_7_additional_loss_coefficient`'.format(value))

        self._data["Node 7 Additional Loss Coefficient"] = value

    @property
    def node_8_additional_loss_coefficient(self):
        """Get node_8_additional_loss_coefficient

        Returns:
            float: the value of `node_8_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 8 Additional Loss Coefficient"]

    @node_8_additional_loss_coefficient.setter
    def node_8_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_8_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_8_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_8_additional_loss_coefficient`'.format(value))

        self._data["Node 8 Additional Loss Coefficient"] = value

    @property
    def node_9_additional_loss_coefficient(self):
        """Get node_9_additional_loss_coefficient

        Returns:
            float: the value of `node_9_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 9 Additional Loss Coefficient"]

    @node_9_additional_loss_coefficient.setter
    def node_9_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_9_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_9_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_9_additional_loss_coefficient`'.format(value))

        self._data["Node 9 Additional Loss Coefficient"] = value

    @property
    def node_10_additional_loss_coefficient(self):
        """Get node_10_additional_loss_coefficient

        Returns:
            float: the value of `node_10_additional_loss_coefficient` or None if not set
        """
        return self._data["Node 10 Additional Loss Coefficient"]

    @node_10_additional_loss_coefficient.setter
    def node_10_additional_loss_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `node_10_additional_loss_coefficient`

        Args:
            value (float): value for IDD Field `node_10_additional_loss_coefficient`
                Unit: W/m2-K
                Default value: 0.0
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
                                 'for field `node_10_additional_loss_coefficient`'.format(value))

        self._data["Node 10 Additional Loss Coefficient"] = value

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
        out.append(self._to_str(self.tank_volume))
        out.append(self._to_str(self.tank_height))
        out.append(self._to_str(self.tank_shape))
        out.append(self._to_str(self.tank_perimeter))
        out.append(self._to_str(self.setpoint_temperature_schedule_name))
        out.append(self._to_str(self.deadband_temperature_difference))
        out.append(self._to_str(self.temperature_sensor_height))
        out.append(self._to_str(self.minimum_temperature_limit))
        out.append(self._to_str(self.nominal_cooling_capacity))
        out.append(self._to_str(self.ambient_temperature_indicator))
        out.append(self._to_str(self.ambient_temperature_schedule_name))
        out.append(self._to_str(self.ambient_temperature_zone_name))
        out.append(self._to_str(self.ambient_temperature_outdoor_air_node_name))
        out.append(self._to_str(self.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature))
        out.append(self._to_str(self.use_side_inlet_node_name))
        out.append(self._to_str(self.use_side_outlet_node_name))
        out.append(self._to_str(self.use_side_heat_transfer_effectiveness))
        out.append(self._to_str(self.use_side_availability_schedule_name))
        out.append(self._to_str(self.use_side_inlet_height))
        out.append(self._to_str(self.use_side_outlet_height))
        out.append(self._to_str(self.use_side_design_flow_rate))
        out.append(self._to_str(self.source_side_inlet_node_name))
        out.append(self._to_str(self.source_side_outlet_node_name))
        out.append(self._to_str(self.source_side_heat_transfer_effectiveness))
        out.append(self._to_str(self.source_side_availability_schedule_name))
        out.append(self._to_str(self.source_side_inlet_height))
        out.append(self._to_str(self.source_side_outlet_height))
        out.append(self._to_str(self.source_side_design_flow_rate))
        out.append(self._to_str(self.tank_recovery_time))
        out.append(self._to_str(self.inlet_mode))
        out.append(self._to_str(self.number_of_nodes))
        out.append(self._to_str(self.additional_destratification_conductivity))
        out.append(self._to_str(self.node_1_additional_loss_coefficient))
        out.append(self._to_str(self.node_2_additional_loss_coefficient))
        out.append(self._to_str(self.node_3_additional_loss_coefficient))
        out.append(self._to_str(self.node_4_additional_loss_coefficient))
        out.append(self._to_str(self.node_5_additional_loss_coefficient))
        out.append(self._to_str(self.node_6_additional_loss_coefficient))
        out.append(self._to_str(self.node_7_additional_loss_coefficient))
        out.append(self._to_str(self.node_8_additional_loss_coefficient))
        out.append(self._to_str(self.node_9_additional_loss_coefficient))
        out.append(self._to_str(self.node_10_additional_loss_coefficient))
        return ",".join(out)