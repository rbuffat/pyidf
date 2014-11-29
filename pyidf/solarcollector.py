from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollector:FlatPlate:Water`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["SolarCollectorPerformance Name"] = None
        self._data["Surface Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Maximum Flow Rate"] = None

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
            self.solarcollectorperformance_name = None
        else:
            self.solarcollectorperformance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
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
    def solarcollectorperformance_name(self):
        """Get solarcollectorperformance_name

        Returns:
            str: the value of `solarcollectorperformance_name` or None if not set
        """
        return self._data["SolarCollectorPerformance Name"]

    @solarcollectorperformance_name.setter
    def solarcollectorperformance_name(self, value=None):
        """  Corresponds to IDD Field `solarcollectorperformance_name`

        Args:
            value (str): value for IDD Field `solarcollectorperformance_name`
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
                                 'for field `solarcollectorperformance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solarcollectorperformance_name`')

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
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

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
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
                Unit: m3/s
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
                                 'for field `maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_flow_rate`')

        self._data["Maximum Flow Rate"] = value

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
        out.append(self._to_str(self.solarcollectorperformance_name))
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.maximum_flow_rate))
        return ",".join(out)

class SolarCollectorFlatPlatePhotovoltaicThermal(object):
    """ Corresponds to IDD object `SolarCollector:FlatPlate:PhotovoltaicThermal`
        Models hybrid photovoltaic-thermal (PVT) solar collectors that convert incident solar
        energy into both electricity and useful thermal energy by heating air or water.
    """
    internal_name = "SolarCollector:FlatPlate:PhotovoltaicThermal"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollector:FlatPlate:PhotovoltaicThermal`
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
        self._data["Air Outlet Node Name"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.photovoltaicthermal_model_performance_name = None
        else:
            self.photovoltaicthermal_model_performance_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.photovoltaic_name = None
        else:
            self.photovoltaic_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_working_fluid_type = None
        else:
            self.thermal_working_fluid_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_inlet_node_name = None
        else:
            self.water_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.water_outlet_node_name = None
        else:
            self.water_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_inlet_node_name = None
        else:
            self.air_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_outlet_node_name = None
        else:
            self.air_outlet_node_name = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

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
        """  Corresponds to IDD Field `photovoltaicthermal_model_performance_name`

        Args:
            value (str): value for IDD Field `photovoltaicthermal_model_performance_name`
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
                                 'for field `photovoltaicthermal_model_performance_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `photovoltaicthermal_model_performance_name`')

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
        """  Corresponds to IDD Field `photovoltaic_name`
        Enter the name of a Generator:Photovoltaic object.

        Args:
            value (str): value for IDD Field `photovoltaic_name`
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
                                 'for field `photovoltaic_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `photovoltaic_name`')

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
        """  Corresponds to IDD Field `thermal_working_fluid_type`

        Args:
            value (str): value for IDD Field `thermal_working_fluid_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_working_fluid_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_working_fluid_type`')
            vals = set()
            vals.add("Water")
            vals.add("Air")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `thermal_working_fluid_type`'.format(value))

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
        """  Corresponds to IDD Field `water_inlet_node_name`

        Args:
            value (str): value for IDD Field `water_inlet_node_name`
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
                                 'for field `water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_inlet_node_name`')

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
        """  Corresponds to IDD Field `water_outlet_node_name`

        Args:
            value (str): value for IDD Field `water_outlet_node_name`
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
                                 'for field `water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `water_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
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
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                Unit: m3/s
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
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """Get air_outlet_node_name

        Returns:
            str: the value of `air_outlet_node_name` or None if not set
        """
        return self._data["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                Unit: m3/s
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
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.photovoltaicthermal_model_performance_name))
        out.append(self._to_str(self.photovoltaic_name))
        out.append(self._to_str(self.thermal_working_fluid_type))
        out.append(self._to_str(self.water_inlet_node_name))
        out.append(self._to_str(self.water_outlet_node_name))
        out.append(self._to_str(self.air_inlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        out.append(self._to_str(self.air_outlet_node_name))
        return ",".join(out)

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollector:IntegralCollectorStorage`
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
            self.integralcollectorstorageparameters_name = None
        else:
            self.integralcollectorstorageparameters_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bottom_surface_boundary_conditions_type = None
        else:
            self.bottom_surface_boundary_conditions_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.boundary_condition_model_name = None
        else:
            self.boundary_condition_model_name = vals[i]
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
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
    def integralcollectorstorageparameters_name(self):
        """Get integralcollectorstorageparameters_name

        Returns:
            str: the value of `integralcollectorstorageparameters_name` or None if not set
        """
        return self._data["IntegralCollectorStorageParameters Name"]

    @integralcollectorstorageparameters_name.setter
    def integralcollectorstorageparameters_name(self, value=None):
        """  Corresponds to IDD Field `integralcollectorstorageparameters_name`

        Args:
            value (str): value for IDD Field `integralcollectorstorageparameters_name`
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
                                 'for field `integralcollectorstorageparameters_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `integralcollectorstorageparameters_name`')

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
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def bottom_surface_boundary_conditions_type(self):
        """Get bottom_surface_boundary_conditions_type

        Returns:
            str: the value of `bottom_surface_boundary_conditions_type` or None if not set
        """
        return self._data["Bottom Surface Boundary Conditions Type"]

    @bottom_surface_boundary_conditions_type.setter
    def bottom_surface_boundary_conditions_type(self, value=None):
        """  Corresponds to IDD Field `bottom_surface_boundary_conditions_type`

        Args:
            value (str): value for IDD Field `bottom_surface_boundary_conditions_type`
                Accepted values are:
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
                                 'for field `bottom_surface_boundary_conditions_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `bottom_surface_boundary_conditions_type`')
            vals = set()
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `bottom_surface_boundary_conditions_type`'.format(value))

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
        """  Corresponds to IDD Field `boundary_condition_model_name`
        Enter the name of a SurfaceProperty:OtherSideConditionsModel
        object. Specified only if the boundary condition type is
        OtherSideConditionsModel, otherwise leave it blank

        Args:
            value (str): value for IDD Field `boundary_condition_model_name`
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
                                 'for field `boundary_condition_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `boundary_condition_model_name`')

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
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
                Unit: m3/s
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
                                 'for field `maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_flow_rate`')

        self._data["Maximum Flow Rate"] = value

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
        out.append(self._to_str(self.integralcollectorstorageparameters_name))
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.bottom_surface_boundary_conditions_type))
        out.append(self._to_str(self.boundary_condition_model_name))
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.maximum_flow_rate))
        return ",".join(out)

class SolarCollectorUnglazedTranspired(object):
    """ Corresponds to IDD object `SolarCollector:UnglazedTranspired`
        Unglazed transpired solar collector (UTSC) used to condition outdoor air. This type of
        collector is generally used to heat air drawn through perforated absorbers and also
        recover heat conducted out through the underlying surfae. This object represents a
        single collector attached to one or more building or shading surfaces and to one or
        more outdoor air systems.
    """
    internal_name = "SolarCollector:UnglazedTranspired"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollector:UnglazedTranspired`
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
        self._data["Surface 1 Name"] = None
        self._data["Surface 2 Name"] = None
        self._data["Surface 3 Name"] = None
        self._data["Surface 4 Name"] = None
        self._data["Surface 5 Name"] = None
        self._data["Surface 6 Name"] = None
        self._data["Surface 7 Name"] = None
        self._data["Surface 8 Name"] = None
        self._data["Surface 9 Name"] = None
        self._data["Surface 10 Name"] = None

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
            self.boundary_conditions_model_name = None
        else:
            self.boundary_conditions_model_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
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
            self.setpoint_node_name = None
        else:
            self.setpoint_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.free_heating_setpoint_schedule_name = None
        else:
            self.free_heating_setpoint_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diameter_of_perforations_in_collector = None
        else:
            self.diameter_of_perforations_in_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_between_perforations_in_collector = None
        else:
            self.distance_between_perforations_in_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_emissivity_of_collector_surface = None
        else:
            self.thermal_emissivity_of_collector_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_absorbtivity_of_collector_surface = None
        else:
            self.solar_absorbtivity_of_collector_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_overall_height_of_collector = None
        else:
            self.effective_overall_height_of_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_gap_thickness_of_plenum_behind_collector = None
        else:
            self.effective_gap_thickness_of_plenum_behind_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_cross_section_area_of_plenum_behind_collector = None
        else:
            self.effective_cross_section_area_of_plenum_behind_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hole_layout_pattern_for_pitch = None
        else:
            self.hole_layout_pattern_for_pitch = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heat_exchange_effectiveness_correlation = None
        else:
            self.heat_exchange_effectiveness_correlation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_actual_collector_surface_area_to_projected_surface_area = None
        else:
            self.ratio_of_actual_collector_surface_area_to_projected_surface_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.roughness_of_collector = None
        else:
            self.roughness_of_collector = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collector_thickness = None
        else:
            self.collector_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effectiveness_for_perforations_with_respect_to_wind = None
        else:
            self.effectiveness_for_perforations_with_respect_to_wind = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = None
        else:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_1_name = None
        else:
            self.surface_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_2_name = None
        else:
            self.surface_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_3_name = None
        else:
            self.surface_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_4_name = None
        else:
            self.surface_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_5_name = None
        else:
            self.surface_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_6_name = None
        else:
            self.surface_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_7_name = None
        else:
            self.surface_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_8_name = None
        else:
            self.surface_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_9_name = None
        else:
            self.surface_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_10_name = None
        else:
            self.surface_10_name = vals[i]
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
    def boundary_conditions_model_name(self):
        """Get boundary_conditions_model_name

        Returns:
            str: the value of `boundary_conditions_model_name` or None if not set
        """
        return self._data["Boundary Conditions Model Name"]

    @boundary_conditions_model_name.setter
    def boundary_conditions_model_name(self, value=None):
        """  Corresponds to IDD Field `boundary_conditions_model_name`
        Enter the name of a SurfaceProperty:OtherSideConditionsModel object

        Args:
            value (str): value for IDD Field `boundary_conditions_model_name`
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
                                 'for field `boundary_conditions_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `boundary_conditions_model_name`')

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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this collector. Schedule value > 0 means it is available.
        If this field is blank, the collector is always available.

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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`
        required field if no SolarCollector:UnglazedTranspired:Multisystem

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
        required field if no SolarCollector:UnglazedTranspired:Multisystem

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
    def setpoint_node_name(self):
        """Get setpoint_node_name

        Returns:
            str: the value of `setpoint_node_name` or None if not set
        """
        return self._data["Setpoint Node Name"]

    @setpoint_node_name.setter
    def setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_node_name`
        This node is where the mixed air setpoint is determined.
        required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `setpoint_node_name`
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
                                 'for field `setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_node_name`')

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
        """  Corresponds to IDD Field `zone_node_name`
        This node is used to indentify the affected zone
        required field if no SolarCollector:UnglazedTranspired:Multisystem

        Args:
            value (str): value for IDD Field `zone_node_name`
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
                                 'for field `zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_node_name`')

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
        """  Corresponds to IDD Field `free_heating_setpoint_schedule_name`

        Args:
            value (str): value for IDD Field `free_heating_setpoint_schedule_name`
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
                                 'for field `free_heating_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `free_heating_setpoint_schedule_name`')

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
        """  Corresponds to IDD Field `diameter_of_perforations_in_collector`

        Args:
            value (float): value for IDD Field `diameter_of_perforations_in_collector`
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
                                 'for field `diameter_of_perforations_in_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `diameter_of_perforations_in_collector`')

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
        """  Corresponds to IDD Field `distance_between_perforations_in_collector`

        Args:
            value (float): value for IDD Field `distance_between_perforations_in_collector`
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
                                 'for field `distance_between_perforations_in_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `distance_between_perforations_in_collector`')

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
        """  Corresponds to IDD Field `thermal_emissivity_of_collector_surface`

        Args:
            value (float): value for IDD Field `thermal_emissivity_of_collector_surface`
                Unit: dimensionless
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
                                 'for field `thermal_emissivity_of_collector_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `thermal_emissivity_of_collector_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `thermal_emissivity_of_collector_surface`')

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
        """  Corresponds to IDD Field `solar_absorbtivity_of_collector_surface`

        Args:
            value (float): value for IDD Field `solar_absorbtivity_of_collector_surface`
                Unit: dimensionless
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
                                 'for field `solar_absorbtivity_of_collector_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_absorbtivity_of_collector_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_absorbtivity_of_collector_surface`')

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
        """  Corresponds to IDD Field `effective_overall_height_of_collector`

        Args:
            value (float): value for IDD Field `effective_overall_height_of_collector`
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
                                 'for field `effective_overall_height_of_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_overall_height_of_collector`')

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
        """  Corresponds to IDD Field `effective_gap_thickness_of_plenum_behind_collector`
        if corrugated, use average depth

        Args:
            value (float): value for IDD Field `effective_gap_thickness_of_plenum_behind_collector`
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
                                 'for field `effective_gap_thickness_of_plenum_behind_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_gap_thickness_of_plenum_behind_collector`')

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
        """  Corresponds to IDD Field `effective_cross_section_area_of_plenum_behind_collector`
        if corrugated, use average depth

        Args:
            value (float): value for IDD Field `effective_cross_section_area_of_plenum_behind_collector`
                Unit: m2
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
                                 'for field `effective_cross_section_area_of_plenum_behind_collector`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_cross_section_area_of_plenum_behind_collector`')

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
        """  Corresponds to IDD Field `hole_layout_pattern_for_pitch`

        Args:
            value (str): value for IDD Field `hole_layout_pattern_for_pitch`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hole_layout_pattern_for_pitch`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hole_layout_pattern_for_pitch`')
            vals = set()
            vals.add("Triangle")
            vals.add("Square")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `hole_layout_pattern_for_pitch`'.format(value))

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
        """  Corresponds to IDD Field `heat_exchange_effectiveness_correlation`

        Args:
            value (str): value for IDD Field `heat_exchange_effectiveness_correlation`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heat_exchange_effectiveness_correlation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_exchange_effectiveness_correlation`')
            vals = set()
            vals.add("Kutscher1994")
            vals.add("VanDeckerHollandsBrunger2001")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heat_exchange_effectiveness_correlation`'.format(value))

        self._data["Heat Exchange Effectiveness Correlation"] = value

    @property
    def ratio_of_actual_collector_surface_area_to_projected_surface_area(self):
        """Get ratio_of_actual_collector_surface_area_to_projected_surface_area

        Returns:
            float: the value of `ratio_of_actual_collector_surface_area_to_projected_surface_area` or None if not set
        """
        return self._data["Ratio of Actual Collector Surface Area to Projected Surface Area"]

    @ratio_of_actual_collector_surface_area_to_projected_surface_area.setter
    def ratio_of_actual_collector_surface_area_to_projected_surface_area(self, value=1.0 ):
        """  Corresponds to IDD Field `ratio_of_actual_collector_surface_area_to_projected_surface_area`
        This parameter is used to help account for corrugations in the collector

        Args:
            value (float): value for IDD Field `ratio_of_actual_collector_surface_area_to_projected_surface_area`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ratio_of_actual_collector_surface_area_to_projected_surface_area`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `ratio_of_actual_collector_surface_area_to_projected_surface_area`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `ratio_of_actual_collector_surface_area_to_projected_surface_area`')

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
        """  Corresponds to IDD Field `roughness_of_collector`

        Args:
            value (str): value for IDD Field `roughness_of_collector`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `roughness_of_collector`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roughness_of_collector`')
            vals = set()
            vals.add("VeryRough")
            vals.add("Rough")
            vals.add("MediumRough")
            vals.add("MediumSmooth")
            vals.add("Smooth")
            vals.add("VerySmooth")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `roughness_of_collector`'.format(value))

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
        """  Corresponds to IDD Field `collector_thickness`
        Collector thickness is not required for Kutscher correlation
        Collector thickness is required for Van Decker et al. correlation

        Args:
            value (float): value for IDD Field `collector_thickness`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `collector_thickness`'.format(value))
            if value < 0.0005:
                raise ValueError('value need to be greater or equal 0.0005 '
                                 'for field `collector_thickness`')
            if value > 0.007:
                raise ValueError('value need to be smaller 0.007 '
                                 'for field `collector_thickness`')

        self._data["Collector Thickness"] = value

    @property
    def effectiveness_for_perforations_with_respect_to_wind(self):
        """Get effectiveness_for_perforations_with_respect_to_wind

        Returns:
            float: the value of `effectiveness_for_perforations_with_respect_to_wind` or None if not set
        """
        return self._data["Effectiveness for Perforations with Respect to Wind"]

    @effectiveness_for_perforations_with_respect_to_wind.setter
    def effectiveness_for_perforations_with_respect_to_wind(self, value=0.25 ):
        """  Corresponds to IDD Field `effectiveness_for_perforations_with_respect_to_wind`
        Cv

        Args:
            value (float): value for IDD Field `effectiveness_for_perforations_with_respect_to_wind`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `effectiveness_for_perforations_with_respect_to_wind`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effectiveness_for_perforations_with_respect_to_wind`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `effectiveness_for_perforations_with_respect_to_wind`')

        self._data["Effectiveness for Perforations with Respect to Wind"] = value

    @property
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self):
        """Get discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow

        Returns:
            float: the value of `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow` or None if not set
        """
        return self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"]

    @discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow.setter
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self, value=0.65 ):
        """  Corresponds to IDD Field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`
        Cd

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')

        self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = value

    @property
    def surface_1_name(self):
        """Get surface_1_name

        Returns:
            str: the value of `surface_1_name` or None if not set
        """
        return self._data["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """  Corresponds to IDD Field `surface_1_name`

        Args:
            value (str): value for IDD Field `surface_1_name`
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
                                 'for field `surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_1_name`')

        self._data["Surface 1 Name"] = value

    @property
    def surface_2_name(self):
        """Get surface_2_name

        Returns:
            str: the value of `surface_2_name` or None if not set
        """
        return self._data["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """  Corresponds to IDD Field `surface_2_name`

        Args:
            value (str): value for IDD Field `surface_2_name`
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
                                 'for field `surface_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_2_name`')

        self._data["Surface 2 Name"] = value

    @property
    def surface_3_name(self):
        """Get surface_3_name

        Returns:
            str: the value of `surface_3_name` or None if not set
        """
        return self._data["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """  Corresponds to IDD Field `surface_3_name`

        Args:
            value (str): value for IDD Field `surface_3_name`
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
                                 'for field `surface_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_3_name`')

        self._data["Surface 3 Name"] = value

    @property
    def surface_4_name(self):
        """Get surface_4_name

        Returns:
            str: the value of `surface_4_name` or None if not set
        """
        return self._data["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """  Corresponds to IDD Field `surface_4_name`

        Args:
            value (str): value for IDD Field `surface_4_name`
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
                                 'for field `surface_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_4_name`')

        self._data["Surface 4 Name"] = value

    @property
    def surface_5_name(self):
        """Get surface_5_name

        Returns:
            str: the value of `surface_5_name` or None if not set
        """
        return self._data["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """  Corresponds to IDD Field `surface_5_name`

        Args:
            value (str): value for IDD Field `surface_5_name`
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
                                 'for field `surface_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_5_name`')

        self._data["Surface 5 Name"] = value

    @property
    def surface_6_name(self):
        """Get surface_6_name

        Returns:
            str: the value of `surface_6_name` or None if not set
        """
        return self._data["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """  Corresponds to IDD Field `surface_6_name`

        Args:
            value (str): value for IDD Field `surface_6_name`
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
                                 'for field `surface_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_6_name`')

        self._data["Surface 6 Name"] = value

    @property
    def surface_7_name(self):
        """Get surface_7_name

        Returns:
            str: the value of `surface_7_name` or None if not set
        """
        return self._data["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """  Corresponds to IDD Field `surface_7_name`

        Args:
            value (str): value for IDD Field `surface_7_name`
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
                                 'for field `surface_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_7_name`')

        self._data["Surface 7 Name"] = value

    @property
    def surface_8_name(self):
        """Get surface_8_name

        Returns:
            str: the value of `surface_8_name` or None if not set
        """
        return self._data["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """  Corresponds to IDD Field `surface_8_name`

        Args:
            value (str): value for IDD Field `surface_8_name`
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
                                 'for field `surface_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_8_name`')

        self._data["Surface 8 Name"] = value

    @property
    def surface_9_name(self):
        """Get surface_9_name

        Returns:
            str: the value of `surface_9_name` or None if not set
        """
        return self._data["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """  Corresponds to IDD Field `surface_9_name`

        Args:
            value (str): value for IDD Field `surface_9_name`
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
                                 'for field `surface_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_9_name`')

        self._data["Surface 9 Name"] = value

    @property
    def surface_10_name(self):
        """Get surface_10_name

        Returns:
            str: the value of `surface_10_name` or None if not set
        """
        return self._data["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """  Corresponds to IDD Field `surface_10_name`

        Args:
            value (str): value for IDD Field `surface_10_name`
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
                                 'for field `surface_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_10_name`')

        self._data["Surface 10 Name"] = value

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
        out.append(self._to_str(self.boundary_conditions_model_name))
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.setpoint_node_name))
        out.append(self._to_str(self.zone_node_name))
        out.append(self._to_str(self.free_heating_setpoint_schedule_name))
        out.append(self._to_str(self.diameter_of_perforations_in_collector))
        out.append(self._to_str(self.distance_between_perforations_in_collector))
        out.append(self._to_str(self.thermal_emissivity_of_collector_surface))
        out.append(self._to_str(self.solar_absorbtivity_of_collector_surface))
        out.append(self._to_str(self.effective_overall_height_of_collector))
        out.append(self._to_str(self.effective_gap_thickness_of_plenum_behind_collector))
        out.append(self._to_str(self.effective_cross_section_area_of_plenum_behind_collector))
        out.append(self._to_str(self.hole_layout_pattern_for_pitch))
        out.append(self._to_str(self.heat_exchange_effectiveness_correlation))
        out.append(self._to_str(self.ratio_of_actual_collector_surface_area_to_projected_surface_area))
        out.append(self._to_str(self.roughness_of_collector))
        out.append(self._to_str(self.collector_thickness))
        out.append(self._to_str(self.effectiveness_for_perforations_with_respect_to_wind))
        out.append(self._to_str(self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow))
        out.append(self._to_str(self.surface_1_name))
        out.append(self._to_str(self.surface_2_name))
        out.append(self._to_str(self.surface_3_name))
        out.append(self._to_str(self.surface_4_name))
        out.append(self._to_str(self.surface_5_name))
        out.append(self._to_str(self.surface_6_name))
        out.append(self._to_str(self.surface_7_name))
        out.append(self._to_str(self.surface_8_name))
        out.append(self._to_str(self.surface_9_name))
        out.append(self._to_str(self.surface_10_name))
        return ",".join(out)

class SolarCollectorUnglazedTranspiredMultisystem(object):
    """ Corresponds to IDD object `SolarCollector:UnglazedTranspired:Multisystem`
        quad-tuples of inlet, outlet, control, and zone nodes
        for multiple different outdoor air systems attached to same collector
    """
    internal_name = "SolarCollector:UnglazedTranspired:Multisystem"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SolarCollector:UnglazedTranspired:Multisystem`
        """
        self._data = OrderedDict()
        self._data["Solar Collector Name"] = None
        self._data["Outdoor Air System 1 Collector Inlet Node"] = None
        self._data["Outdoor Air System 1 Collector Outlet Node"] = None
        self._data["Outdoor Air System 1 Mixed Air Node"] = None
        self._data["Outdoor Air System 1 Zone Node"] = None
        self._data["Outdoor Air System 2 Collector Inlet Node"] = None
        self._data["Outdoor Air System 2 Collector Outlet Node"] = None
        self._data["Outdoor Air System 2 Mixed Air Node"] = None
        self._data["Outdoor Air System 2 Zone Node"] = None
        self._data["Outdoor Air System 3 Collector Inlet Node"] = None
        self._data["Outdoor Air System 3 Collector Outlet Node"] = None
        self._data["Outdoor Air System 3 Mixed Air Node"] = None
        self._data["Outdoor Air System 3 Zone Node"] = None
        self._data["Outdoor Air System 4 Collector Inlet Node"] = None
        self._data["Outdoor Air System 4 Collector Outlet Node"] = None
        self._data["Outdoor Air System 4 Mixed Air Node"] = None
        self._data["Outdoor Air System 4 Zone Node"] = None
        self._data["Outdoor Air System 5 Collector Inlet Node"] = None
        self._data["Outdoor Air System 5 Collector Outlet Node"] = None
        self._data["Outdoor Air System 5 Mixed Air Node"] = None
        self._data["Outdoor Air System 5 Zone Node"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.solar_collector_name = None
        else:
            self.solar_collector_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_1_collector_inlet_node = None
        else:
            self.outdoor_air_system_1_collector_inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_1_collector_outlet_node = None
        else:
            self.outdoor_air_system_1_collector_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_1_mixed_air_node = None
        else:
            self.outdoor_air_system_1_mixed_air_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_1_zone_node = None
        else:
            self.outdoor_air_system_1_zone_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_2_collector_inlet_node = None
        else:
            self.outdoor_air_system_2_collector_inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_2_collector_outlet_node = None
        else:
            self.outdoor_air_system_2_collector_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_2_mixed_air_node = None
        else:
            self.outdoor_air_system_2_mixed_air_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_2_zone_node = None
        else:
            self.outdoor_air_system_2_zone_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_3_collector_inlet_node = None
        else:
            self.outdoor_air_system_3_collector_inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_3_collector_outlet_node = None
        else:
            self.outdoor_air_system_3_collector_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_3_mixed_air_node = None
        else:
            self.outdoor_air_system_3_mixed_air_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_3_zone_node = None
        else:
            self.outdoor_air_system_3_zone_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_4_collector_inlet_node = None
        else:
            self.outdoor_air_system_4_collector_inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_4_collector_outlet_node = None
        else:
            self.outdoor_air_system_4_collector_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_4_mixed_air_node = None
        else:
            self.outdoor_air_system_4_mixed_air_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_4_zone_node = None
        else:
            self.outdoor_air_system_4_zone_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_5_collector_inlet_node = None
        else:
            self.outdoor_air_system_5_collector_inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_5_collector_outlet_node = None
        else:
            self.outdoor_air_system_5_collector_outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_5_mixed_air_node = None
        else:
            self.outdoor_air_system_5_mixed_air_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_system_5_zone_node = None
        else:
            self.outdoor_air_system_5_zone_node = vals[i]
        i += 1

    @property
    def solar_collector_name(self):
        """Get solar_collector_name

        Returns:
            str: the value of `solar_collector_name` or None if not set
        """
        return self._data["Solar Collector Name"]

    @solar_collector_name.setter
    def solar_collector_name(self, value=None):
        """  Corresponds to IDD Field `solar_collector_name`
        Enter the name of a SolarCollector:UnglazedTranspired object.

        Args:
            value (str): value for IDD Field `solar_collector_name`
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
                                 'for field `solar_collector_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_collector_name`')

        self._data["Solar Collector Name"] = value

    @property
    def outdoor_air_system_1_collector_inlet_node(self):
        """Get outdoor_air_system_1_collector_inlet_node

        Returns:
            str: the value of `outdoor_air_system_1_collector_inlet_node` or None if not set
        """
        return self._data["Outdoor Air System 1 Collector Inlet Node"]

    @outdoor_air_system_1_collector_inlet_node.setter
    def outdoor_air_system_1_collector_inlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_1_collector_inlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_1_collector_inlet_node`
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
                                 'for field `outdoor_air_system_1_collector_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_1_collector_inlet_node`')

        self._data["Outdoor Air System 1 Collector Inlet Node"] = value

    @property
    def outdoor_air_system_1_collector_outlet_node(self):
        """Get outdoor_air_system_1_collector_outlet_node

        Returns:
            str: the value of `outdoor_air_system_1_collector_outlet_node` or None if not set
        """
        return self._data["Outdoor Air System 1 Collector Outlet Node"]

    @outdoor_air_system_1_collector_outlet_node.setter
    def outdoor_air_system_1_collector_outlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_1_collector_outlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_1_collector_outlet_node`
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
                                 'for field `outdoor_air_system_1_collector_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_1_collector_outlet_node`')

        self._data["Outdoor Air System 1 Collector Outlet Node"] = value

    @property
    def outdoor_air_system_1_mixed_air_node(self):
        """Get outdoor_air_system_1_mixed_air_node

        Returns:
            str: the value of `outdoor_air_system_1_mixed_air_node` or None if not set
        """
        return self._data["Outdoor Air System 1 Mixed Air Node"]

    @outdoor_air_system_1_mixed_air_node.setter
    def outdoor_air_system_1_mixed_air_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_1_mixed_air_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_1_mixed_air_node`
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
                                 'for field `outdoor_air_system_1_mixed_air_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_1_mixed_air_node`')

        self._data["Outdoor Air System 1 Mixed Air Node"] = value

    @property
    def outdoor_air_system_1_zone_node(self):
        """Get outdoor_air_system_1_zone_node

        Returns:
            str: the value of `outdoor_air_system_1_zone_node` or None if not set
        """
        return self._data["Outdoor Air System 1 Zone Node"]

    @outdoor_air_system_1_zone_node.setter
    def outdoor_air_system_1_zone_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_1_zone_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_1_zone_node`
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
                                 'for field `outdoor_air_system_1_zone_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_1_zone_node`')

        self._data["Outdoor Air System 1 Zone Node"] = value

    @property
    def outdoor_air_system_2_collector_inlet_node(self):
        """Get outdoor_air_system_2_collector_inlet_node

        Returns:
            str: the value of `outdoor_air_system_2_collector_inlet_node` or None if not set
        """
        return self._data["Outdoor Air System 2 Collector Inlet Node"]

    @outdoor_air_system_2_collector_inlet_node.setter
    def outdoor_air_system_2_collector_inlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_2_collector_inlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_2_collector_inlet_node`
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
                                 'for field `outdoor_air_system_2_collector_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_2_collector_inlet_node`')

        self._data["Outdoor Air System 2 Collector Inlet Node"] = value

    @property
    def outdoor_air_system_2_collector_outlet_node(self):
        """Get outdoor_air_system_2_collector_outlet_node

        Returns:
            str: the value of `outdoor_air_system_2_collector_outlet_node` or None if not set
        """
        return self._data["Outdoor Air System 2 Collector Outlet Node"]

    @outdoor_air_system_2_collector_outlet_node.setter
    def outdoor_air_system_2_collector_outlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_2_collector_outlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_2_collector_outlet_node`
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
                                 'for field `outdoor_air_system_2_collector_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_2_collector_outlet_node`')

        self._data["Outdoor Air System 2 Collector Outlet Node"] = value

    @property
    def outdoor_air_system_2_mixed_air_node(self):
        """Get outdoor_air_system_2_mixed_air_node

        Returns:
            str: the value of `outdoor_air_system_2_mixed_air_node` or None if not set
        """
        return self._data["Outdoor Air System 2 Mixed Air Node"]

    @outdoor_air_system_2_mixed_air_node.setter
    def outdoor_air_system_2_mixed_air_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_2_mixed_air_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_2_mixed_air_node`
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
                                 'for field `outdoor_air_system_2_mixed_air_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_2_mixed_air_node`')

        self._data["Outdoor Air System 2 Mixed Air Node"] = value

    @property
    def outdoor_air_system_2_zone_node(self):
        """Get outdoor_air_system_2_zone_node

        Returns:
            str: the value of `outdoor_air_system_2_zone_node` or None if not set
        """
        return self._data["Outdoor Air System 2 Zone Node"]

    @outdoor_air_system_2_zone_node.setter
    def outdoor_air_system_2_zone_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_2_zone_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_2_zone_node`
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
                                 'for field `outdoor_air_system_2_zone_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_2_zone_node`')

        self._data["Outdoor Air System 2 Zone Node"] = value

    @property
    def outdoor_air_system_3_collector_inlet_node(self):
        """Get outdoor_air_system_3_collector_inlet_node

        Returns:
            str: the value of `outdoor_air_system_3_collector_inlet_node` or None if not set
        """
        return self._data["Outdoor Air System 3 Collector Inlet Node"]

    @outdoor_air_system_3_collector_inlet_node.setter
    def outdoor_air_system_3_collector_inlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_3_collector_inlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_3_collector_inlet_node`
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
                                 'for field `outdoor_air_system_3_collector_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_3_collector_inlet_node`')

        self._data["Outdoor Air System 3 Collector Inlet Node"] = value

    @property
    def outdoor_air_system_3_collector_outlet_node(self):
        """Get outdoor_air_system_3_collector_outlet_node

        Returns:
            str: the value of `outdoor_air_system_3_collector_outlet_node` or None if not set
        """
        return self._data["Outdoor Air System 3 Collector Outlet Node"]

    @outdoor_air_system_3_collector_outlet_node.setter
    def outdoor_air_system_3_collector_outlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_3_collector_outlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_3_collector_outlet_node`
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
                                 'for field `outdoor_air_system_3_collector_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_3_collector_outlet_node`')

        self._data["Outdoor Air System 3 Collector Outlet Node"] = value

    @property
    def outdoor_air_system_3_mixed_air_node(self):
        """Get outdoor_air_system_3_mixed_air_node

        Returns:
            str: the value of `outdoor_air_system_3_mixed_air_node` or None if not set
        """
        return self._data["Outdoor Air System 3 Mixed Air Node"]

    @outdoor_air_system_3_mixed_air_node.setter
    def outdoor_air_system_3_mixed_air_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_3_mixed_air_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_3_mixed_air_node`
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
                                 'for field `outdoor_air_system_3_mixed_air_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_3_mixed_air_node`')

        self._data["Outdoor Air System 3 Mixed Air Node"] = value

    @property
    def outdoor_air_system_3_zone_node(self):
        """Get outdoor_air_system_3_zone_node

        Returns:
            str: the value of `outdoor_air_system_3_zone_node` or None if not set
        """
        return self._data["Outdoor Air System 3 Zone Node"]

    @outdoor_air_system_3_zone_node.setter
    def outdoor_air_system_3_zone_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_3_zone_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_3_zone_node`
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
                                 'for field `outdoor_air_system_3_zone_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_3_zone_node`')

        self._data["Outdoor Air System 3 Zone Node"] = value

    @property
    def outdoor_air_system_4_collector_inlet_node(self):
        """Get outdoor_air_system_4_collector_inlet_node

        Returns:
            str: the value of `outdoor_air_system_4_collector_inlet_node` or None if not set
        """
        return self._data["Outdoor Air System 4 Collector Inlet Node"]

    @outdoor_air_system_4_collector_inlet_node.setter
    def outdoor_air_system_4_collector_inlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_4_collector_inlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_4_collector_inlet_node`
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
                                 'for field `outdoor_air_system_4_collector_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_4_collector_inlet_node`')

        self._data["Outdoor Air System 4 Collector Inlet Node"] = value

    @property
    def outdoor_air_system_4_collector_outlet_node(self):
        """Get outdoor_air_system_4_collector_outlet_node

        Returns:
            str: the value of `outdoor_air_system_4_collector_outlet_node` or None if not set
        """
        return self._data["Outdoor Air System 4 Collector Outlet Node"]

    @outdoor_air_system_4_collector_outlet_node.setter
    def outdoor_air_system_4_collector_outlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_4_collector_outlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_4_collector_outlet_node`
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
                                 'for field `outdoor_air_system_4_collector_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_4_collector_outlet_node`')

        self._data["Outdoor Air System 4 Collector Outlet Node"] = value

    @property
    def outdoor_air_system_4_mixed_air_node(self):
        """Get outdoor_air_system_4_mixed_air_node

        Returns:
            str: the value of `outdoor_air_system_4_mixed_air_node` or None if not set
        """
        return self._data["Outdoor Air System 4 Mixed Air Node"]

    @outdoor_air_system_4_mixed_air_node.setter
    def outdoor_air_system_4_mixed_air_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_4_mixed_air_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_4_mixed_air_node`
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
                                 'for field `outdoor_air_system_4_mixed_air_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_4_mixed_air_node`')

        self._data["Outdoor Air System 4 Mixed Air Node"] = value

    @property
    def outdoor_air_system_4_zone_node(self):
        """Get outdoor_air_system_4_zone_node

        Returns:
            str: the value of `outdoor_air_system_4_zone_node` or None if not set
        """
        return self._data["Outdoor Air System 4 Zone Node"]

    @outdoor_air_system_4_zone_node.setter
    def outdoor_air_system_4_zone_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_4_zone_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_4_zone_node`
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
                                 'for field `outdoor_air_system_4_zone_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_4_zone_node`')

        self._data["Outdoor Air System 4 Zone Node"] = value

    @property
    def outdoor_air_system_5_collector_inlet_node(self):
        """Get outdoor_air_system_5_collector_inlet_node

        Returns:
            str: the value of `outdoor_air_system_5_collector_inlet_node` or None if not set
        """
        return self._data["Outdoor Air System 5 Collector Inlet Node"]

    @outdoor_air_system_5_collector_inlet_node.setter
    def outdoor_air_system_5_collector_inlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_5_collector_inlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_5_collector_inlet_node`
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
                                 'for field `outdoor_air_system_5_collector_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_5_collector_inlet_node`')

        self._data["Outdoor Air System 5 Collector Inlet Node"] = value

    @property
    def outdoor_air_system_5_collector_outlet_node(self):
        """Get outdoor_air_system_5_collector_outlet_node

        Returns:
            str: the value of `outdoor_air_system_5_collector_outlet_node` or None if not set
        """
        return self._data["Outdoor Air System 5 Collector Outlet Node"]

    @outdoor_air_system_5_collector_outlet_node.setter
    def outdoor_air_system_5_collector_outlet_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_5_collector_outlet_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_5_collector_outlet_node`
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
                                 'for field `outdoor_air_system_5_collector_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_5_collector_outlet_node`')

        self._data["Outdoor Air System 5 Collector Outlet Node"] = value

    @property
    def outdoor_air_system_5_mixed_air_node(self):
        """Get outdoor_air_system_5_mixed_air_node

        Returns:
            str: the value of `outdoor_air_system_5_mixed_air_node` or None if not set
        """
        return self._data["Outdoor Air System 5 Mixed Air Node"]

    @outdoor_air_system_5_mixed_air_node.setter
    def outdoor_air_system_5_mixed_air_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_5_mixed_air_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_5_mixed_air_node`
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
                                 'for field `outdoor_air_system_5_mixed_air_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_5_mixed_air_node`')

        self._data["Outdoor Air System 5 Mixed Air Node"] = value

    @property
    def outdoor_air_system_5_zone_node(self):
        """Get outdoor_air_system_5_zone_node

        Returns:
            str: the value of `outdoor_air_system_5_zone_node` or None if not set
        """
        return self._data["Outdoor Air System 5 Zone Node"]

    @outdoor_air_system_5_zone_node.setter
    def outdoor_air_system_5_zone_node(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_system_5_zone_node`

        Args:
            value (str): value for IDD Field `outdoor_air_system_5_zone_node`
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
                                 'for field `outdoor_air_system_5_zone_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_system_5_zone_node`')

        self._data["Outdoor Air System 5 Zone Node"] = value

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
        out.append(self._to_str(self.solar_collector_name))
        out.append(self._to_str(self.outdoor_air_system_1_collector_inlet_node))
        out.append(self._to_str(self.outdoor_air_system_1_collector_outlet_node))
        out.append(self._to_str(self.outdoor_air_system_1_mixed_air_node))
        out.append(self._to_str(self.outdoor_air_system_1_zone_node))
        out.append(self._to_str(self.outdoor_air_system_2_collector_inlet_node))
        out.append(self._to_str(self.outdoor_air_system_2_collector_outlet_node))
        out.append(self._to_str(self.outdoor_air_system_2_mixed_air_node))
        out.append(self._to_str(self.outdoor_air_system_2_zone_node))
        out.append(self._to_str(self.outdoor_air_system_3_collector_inlet_node))
        out.append(self._to_str(self.outdoor_air_system_3_collector_outlet_node))
        out.append(self._to_str(self.outdoor_air_system_3_mixed_air_node))
        out.append(self._to_str(self.outdoor_air_system_3_zone_node))
        out.append(self._to_str(self.outdoor_air_system_4_collector_inlet_node))
        out.append(self._to_str(self.outdoor_air_system_4_collector_outlet_node))
        out.append(self._to_str(self.outdoor_air_system_4_mixed_air_node))
        out.append(self._to_str(self.outdoor_air_system_4_zone_node))
        out.append(self._to_str(self.outdoor_air_system_5_collector_inlet_node))
        out.append(self._to_str(self.outdoor_air_system_5_collector_outlet_node))
        out.append(self._to_str(self.outdoor_air_system_5_mixed_air_node))
        out.append(self._to_str(self.outdoor_air_system_5_zone_node))
        return ",".join(out)