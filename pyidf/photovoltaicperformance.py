from collections import OrderedDict

class PhotovoltaicPerformanceSimple(object):
    """ Corresponds to IDD object `PhotovoltaicPerformance:Simple`
        Describes a simple model of photovoltaics that may be useful for early phase
        design analysis. In this model the user has direct access to the efficiency with
        which surfaces convert incident solar radiation to electricity and need not specify
        arrays of specific modules.
    """
    internal_name = "PhotovoltaicPerformance:Simple"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PhotovoltaicPerformance:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fraction of Surface Area with Active Solar Cells"] = None
        self._data["Conversion Efficiency Input Mode"] = None
        self._data["Value for Cell Efficiency if Fixed"] = None
        self._data["Efficiency Schedule Name"] = None

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
            self.fraction_of_surface_area_with_active_solar_cells = None
        else:
            self.fraction_of_surface_area_with_active_solar_cells = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conversion_efficiency_input_mode = None
        else:
            self.conversion_efficiency_input_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.value_for_cell_efficiency_if_fixed = None
        else:
            self.value_for_cell_efficiency_if_fixed = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_schedule_name = None
        else:
            self.efficiency_schedule_name = vals[i]
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
    def fraction_of_surface_area_with_active_solar_cells(self):
        """Get fraction_of_surface_area_with_active_solar_cells

        Returns:
            float: the value of `fraction_of_surface_area_with_active_solar_cells` or None if not set
        """
        return self._data["Fraction of Surface Area with Active Solar Cells"]

    @fraction_of_surface_area_with_active_solar_cells.setter
    def fraction_of_surface_area_with_active_solar_cells(self, value=None):
        """  Corresponds to IDD Field `fraction_of_surface_area_with_active_solar_cells`

        Args:
            value (float): value for IDD Field `fraction_of_surface_area_with_active_solar_cells`
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
                                 'for field `fraction_of_surface_area_with_active_solar_cells`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_surface_area_with_active_solar_cells`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_surface_area_with_active_solar_cells`')

        self._data["Fraction of Surface Area with Active Solar Cells"] = value

    @property
    def conversion_efficiency_input_mode(self):
        """Get conversion_efficiency_input_mode

        Returns:
            str: the value of `conversion_efficiency_input_mode` or None if not set
        """
        return self._data["Conversion Efficiency Input Mode"]

    @conversion_efficiency_input_mode.setter
    def conversion_efficiency_input_mode(self, value=None):
        """  Corresponds to IDD Field `conversion_efficiency_input_mode`

        Args:
            value (str): value for IDD Field `conversion_efficiency_input_mode`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `conversion_efficiency_input_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `conversion_efficiency_input_mode`')
            vals = set()
            vals.add("Fixed")
            vals.add("Scheduled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `conversion_efficiency_input_mode`'.format(value))

        self._data["Conversion Efficiency Input Mode"] = value

    @property
    def value_for_cell_efficiency_if_fixed(self):
        """Get value_for_cell_efficiency_if_fixed

        Returns:
            float: the value of `value_for_cell_efficiency_if_fixed` or None if not set
        """
        return self._data["Value for Cell Efficiency if Fixed"]

    @value_for_cell_efficiency_if_fixed.setter
    def value_for_cell_efficiency_if_fixed(self, value=None):
        """  Corresponds to IDD Field `value_for_cell_efficiency_if_fixed`
        Efficiency = (power generated [W])/(incident solar[W])

        Args:
            value (float): value for IDD Field `value_for_cell_efficiency_if_fixed`
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
                                 'for field `value_for_cell_efficiency_if_fixed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `value_for_cell_efficiency_if_fixed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `value_for_cell_efficiency_if_fixed`')

        self._data["Value for Cell Efficiency if Fixed"] = value

    @property
    def efficiency_schedule_name(self):
        """Get efficiency_schedule_name

        Returns:
            str: the value of `efficiency_schedule_name` or None if not set
        """
        return self._data["Efficiency Schedule Name"]

    @efficiency_schedule_name.setter
    def efficiency_schedule_name(self, value=None):
        """  Corresponds to IDD Field `efficiency_schedule_name`

        Args:
            value (str): value for IDD Field `efficiency_schedule_name`
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
                                 'for field `efficiency_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `efficiency_schedule_name`')

        self._data["Efficiency Schedule Name"] = value

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
        out.append(self._to_str(self.fraction_of_surface_area_with_active_solar_cells))
        out.append(self._to_str(self.conversion_efficiency_input_mode))
        out.append(self._to_str(self.value_for_cell_efficiency_if_fixed))
        out.append(self._to_str(self.efficiency_schedule_name))
        return ",".join(out)

class PhotovoltaicPerformanceEquivalentOneDiode(object):
    """ Corresponds to IDD object `PhotovoltaicPerformance:EquivalentOne-Diode`
        Describes the performance characteristics of Photovoltaic (PV) modules to be modeled
        using an equivalent one-diode circuit.  This model is also known as
        the 4- or 5-parameter TRNSYS model for photovoltaics.
    """
    internal_name = "PhotovoltaicPerformance:EquivalentOne-Diode"
    field_count = 20

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PhotovoltaicPerformance:EquivalentOne-Diode`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Cell type"] = None
        self._data["Number of Cells in Series"] = None
        self._data["Active Area"] = None
        self._data["Transmittance Absorptance Product"] = None
        self._data["Semiconductor Bandgap"] = None
        self._data["Shunt Resistance"] = None
        self._data["Short Circuit Current"] = None
        self._data["Open Circuit Voltage"] = None
        self._data["Reference Temperature"] = None
        self._data["Reference Insolation"] = None
        self._data["Module Current at Maximum Power"] = None
        self._data["Module Voltage at Maximum Power"] = None
        self._data["Temperature Coefficient of Short Circuit Current"] = None
        self._data["Temperature Coefficient of Open Circuit Voltage"] = None
        self._data["Nominal Operating Cell Temperature Test Ambient Temperature"] = None
        self._data["Nominal Operating Cell Temperature Test Cell Temperature"] = None
        self._data["Nominal Operating Cell Temperature Test Insolation"] = None
        self._data["Module Heat Loss Coefficient"] = None
        self._data["Total Heat Capacity"] = None

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
            self.cell_type = None
        else:
            self.cell_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells_in_series = None
        else:
            self.number_of_cells_in_series = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.active_area = None
        else:
            self.active_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transmittance_absorptance_product = None
        else:
            self.transmittance_absorptance_product = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.semiconductor_bandgap = None
        else:
            self.semiconductor_bandgap = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shunt_resistance = None
        else:
            self.shunt_resistance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.short_circuit_current = None
        else:
            self.short_circuit_current = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.open_circuit_voltage = None
        else:
            self.open_circuit_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_temperature = None
        else:
            self.reference_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_insolation = None
        else:
            self.reference_insolation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.module_current_at_maximum_power = None
        else:
            self.module_current_at_maximum_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.module_voltage_at_maximum_power = None
        else:
            self.module_voltage_at_maximum_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_coefficient_of_short_circuit_current = None
        else:
            self.temperature_coefficient_of_short_circuit_current = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_coefficient_of_open_circuit_voltage = None
        else:
            self.temperature_coefficient_of_open_circuit_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_operating_cell_temperature_test_ambient_temperature = None
        else:
            self.nominal_operating_cell_temperature_test_ambient_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_operating_cell_temperature_test_cell_temperature = None
        else:
            self.nominal_operating_cell_temperature_test_cell_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_operating_cell_temperature_test_insolation = None
        else:
            self.nominal_operating_cell_temperature_test_insolation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.module_heat_loss_coefficient = None
        else:
            self.module_heat_loss_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_heat_capacity = None
        else:
            self.total_heat_capacity = vals[i]
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
    def cell_type(self):
        """Get cell_type

        Returns:
            str: the value of `cell_type` or None if not set
        """
        return self._data["Cell type"]

    @cell_type.setter
    def cell_type(self, value=None):
        """  Corresponds to IDD Field `cell_type`

        Args:
            value (str): value for IDD Field `cell_type`
                Accepted values are:
                      - CrystallineSilicon
                      - AmorphousSilicon
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
                                 'for field `cell_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cell_type`')
            vals = set()
            vals.add("CrystallineSilicon")
            vals.add("AmorphousSilicon")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cell_type`'.format(value))

        self._data["Cell type"] = value

    @property
    def number_of_cells_in_series(self):
        """Get number_of_cells_in_series

        Returns:
            int: the value of `number_of_cells_in_series` or None if not set
        """
        return self._data["Number of Cells in Series"]

    @number_of_cells_in_series.setter
    def number_of_cells_in_series(self, value=36 ):
        """  Corresponds to IDD Field `number_of_cells_in_series`

        Args:
            value (int): value for IDD Field `number_of_cells_in_series`
                Unit: dimensionless
                Default value: 36
                value >= 0
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
                                 'for field `number_of_cells_in_series`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_cells_in_series`')

        self._data["Number of Cells in Series"] = value

    @property
    def active_area(self):
        """Get active_area

        Returns:
            float: the value of `active_area` or None if not set
        """
        return self._data["Active Area"]

    @active_area.setter
    def active_area(self, value=0.89 ):
        """  Corresponds to IDD Field `active_area`
        The total power output of the array is determined by the
        number of modules (see above).  The Active Area is only
        used to calculate the PV Array Efficiency output variable.

        Args:
            value (float): value for IDD Field `active_area`
                Unit: m2
                Default value: 0.89
                value >= 0.1
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
                                 'for field `active_area`'.format(value))
            if value < 0.1:
                raise ValueError('value need to be greater or equal 0.1 '
                                 'for field `active_area`')

        self._data["Active Area"] = value

    @property
    def transmittance_absorptance_product(self):
        """Get transmittance_absorptance_product

        Returns:
            float: the value of `transmittance_absorptance_product` or None if not set
        """
        return self._data["Transmittance Absorptance Product"]

    @transmittance_absorptance_product.setter
    def transmittance_absorptance_product(self, value=0.95 ):
        """  Corresponds to IDD Field `transmittance_absorptance_product`

        Args:
            value (float): value for IDD Field `transmittance_absorptance_product`
                Unit: dimensionless
                Default value: 0.95
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
                                 'for field `transmittance_absorptance_product`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `transmittance_absorptance_product`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `transmittance_absorptance_product`')

        self._data["Transmittance Absorptance Product"] = value

    @property
    def semiconductor_bandgap(self):
        """Get semiconductor_bandgap

        Returns:
            float: the value of `semiconductor_bandgap` or None if not set
        """
        return self._data["Semiconductor Bandgap"]

    @semiconductor_bandgap.setter
    def semiconductor_bandgap(self, value=1.12 ):
        """  Corresponds to IDD Field `semiconductor_bandgap`

        Args:
            value (float): value for IDD Field `semiconductor_bandgap`
                Unit: eV
                Default value: 1.12
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
                                 'for field `semiconductor_bandgap`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `semiconductor_bandgap`')

        self._data["Semiconductor Bandgap"] = value

    @property
    def shunt_resistance(self):
        """Get shunt_resistance

        Returns:
            float: the value of `shunt_resistance` or None if not set
        """
        return self._data["Shunt Resistance"]

    @shunt_resistance.setter
    def shunt_resistance(self, value=1000000.0 ):
        """  Corresponds to IDD Field `shunt_resistance`

        Args:
            value (float): value for IDD Field `shunt_resistance`
                Unit: ohms
                Default value: 1000000.0
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
                                 'for field `shunt_resistance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `shunt_resistance`')

        self._data["Shunt Resistance"] = value

    @property
    def short_circuit_current(self):
        """Get short_circuit_current

        Returns:
            float: the value of `short_circuit_current` or None if not set
        """
        return self._data["Short Circuit Current"]

    @short_circuit_current.setter
    def short_circuit_current(self, value=6.5 ):
        """  Corresponds to IDD Field `short_circuit_current`

        Args:
            value (float): value for IDD Field `short_circuit_current`
                Unit: A
                Default value: 6.5
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
                                 'for field `short_circuit_current`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `short_circuit_current`')

        self._data["Short Circuit Current"] = value

    @property
    def open_circuit_voltage(self):
        """Get open_circuit_voltage

        Returns:
            float: the value of `open_circuit_voltage` or None if not set
        """
        return self._data["Open Circuit Voltage"]

    @open_circuit_voltage.setter
    def open_circuit_voltage(self, value=21.6 ):
        """  Corresponds to IDD Field `open_circuit_voltage`

        Args:
            value (float): value for IDD Field `open_circuit_voltage`
                Unit: V
                Default value: 21.6
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
                                 'for field `open_circuit_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `open_circuit_voltage`')

        self._data["Open Circuit Voltage"] = value

    @property
    def reference_temperature(self):
        """Get reference_temperature

        Returns:
            float: the value of `reference_temperature` or None if not set
        """
        return self._data["Reference Temperature"]

    @reference_temperature.setter
    def reference_temperature(self, value=25.0 ):
        """  Corresponds to IDD Field `reference_temperature`

        Args:
            value (float): value for IDD Field `reference_temperature`
                Unit: C
                Default value: 25.0
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
                                 'for field `reference_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `reference_temperature`')

        self._data["Reference Temperature"] = value

    @property
    def reference_insolation(self):
        """Get reference_insolation

        Returns:
            float: the value of `reference_insolation` or None if not set
        """
        return self._data["Reference Insolation"]

    @reference_insolation.setter
    def reference_insolation(self, value=1000.0 ):
        """  Corresponds to IDD Field `reference_insolation`

        Args:
            value (float): value for IDD Field `reference_insolation`
                Unit: W/m2
                Default value: 1000.0
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
                                 'for field `reference_insolation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `reference_insolation`')

        self._data["Reference Insolation"] = value

    @property
    def module_current_at_maximum_power(self):
        """Get module_current_at_maximum_power

        Returns:
            float: the value of `module_current_at_maximum_power` or None if not set
        """
        return self._data["Module Current at Maximum Power"]

    @module_current_at_maximum_power.setter
    def module_current_at_maximum_power(self, value=5.9 ):
        """  Corresponds to IDD Field `module_current_at_maximum_power`
        Single module current at the maximum power point
        and reference conditions.  Module Current, Module Voltage,
        Number of Modules in Parallel and Number of Modules in Series
        determine the maximum power output of the array.

        Args:
            value (float): value for IDD Field `module_current_at_maximum_power`
                Unit: A
                Default value: 5.9
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
                                 'for field `module_current_at_maximum_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `module_current_at_maximum_power`')

        self._data["Module Current at Maximum Power"] = value

    @property
    def module_voltage_at_maximum_power(self):
        """Get module_voltage_at_maximum_power

        Returns:
            float: the value of `module_voltage_at_maximum_power` or None if not set
        """
        return self._data["Module Voltage at Maximum Power"]

    @module_voltage_at_maximum_power.setter
    def module_voltage_at_maximum_power(self, value=17.0 ):
        """  Corresponds to IDD Field `module_voltage_at_maximum_power`
        Single module voltage at the maximum power point
        and reference conditions.  Module Current, Module Voltage,
        Number of Modules in Parallel and Number of Modules in Series
        determine the maximum power output of the array.

        Args:
            value (float): value for IDD Field `module_voltage_at_maximum_power`
                Unit: V
                Default value: 17.0
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
                                 'for field `module_voltage_at_maximum_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `module_voltage_at_maximum_power`')

        self._data["Module Voltage at Maximum Power"] = value

    @property
    def temperature_coefficient_of_short_circuit_current(self):
        """Get temperature_coefficient_of_short_circuit_current

        Returns:
            float: the value of `temperature_coefficient_of_short_circuit_current` or None if not set
        """
        return self._data["Temperature Coefficient of Short Circuit Current"]

    @temperature_coefficient_of_short_circuit_current.setter
    def temperature_coefficient_of_short_circuit_current(self, value=0.02 ):
        """  Corresponds to IDD Field `temperature_coefficient_of_short_circuit_current`

        Args:
            value (float): value for IDD Field `temperature_coefficient_of_short_circuit_current`
                Unit: A/K
                Default value: 0.02
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
                                 'for field `temperature_coefficient_of_short_circuit_current`'.format(value))

        self._data["Temperature Coefficient of Short Circuit Current"] = value

    @property
    def temperature_coefficient_of_open_circuit_voltage(self):
        """Get temperature_coefficient_of_open_circuit_voltage

        Returns:
            float: the value of `temperature_coefficient_of_open_circuit_voltage` or None if not set
        """
        return self._data["Temperature Coefficient of Open Circuit Voltage"]

    @temperature_coefficient_of_open_circuit_voltage.setter
    def temperature_coefficient_of_open_circuit_voltage(self, value=-0.079 ):
        """  Corresponds to IDD Field `temperature_coefficient_of_open_circuit_voltage`

        Args:
            value (float): value for IDD Field `temperature_coefficient_of_open_circuit_voltage`
                Unit: V/K
                Default value: -0.079
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
                                 'for field `temperature_coefficient_of_open_circuit_voltage`'.format(value))

        self._data["Temperature Coefficient of Open Circuit Voltage"] = value

    @property
    def nominal_operating_cell_temperature_test_ambient_temperature(self):
        """Get nominal_operating_cell_temperature_test_ambient_temperature

        Returns:
            float: the value of `nominal_operating_cell_temperature_test_ambient_temperature` or None if not set
        """
        return self._data["Nominal Operating Cell Temperature Test Ambient Temperature"]

    @nominal_operating_cell_temperature_test_ambient_temperature.setter
    def nominal_operating_cell_temperature_test_ambient_temperature(self, value=20.0 ):
        """  Corresponds to IDD Field `nominal_operating_cell_temperature_test_ambient_temperature`

        Args:
            value (float): value for IDD Field `nominal_operating_cell_temperature_test_ambient_temperature`
                Unit: C
                Default value: 20.0
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
                                 'for field `nominal_operating_cell_temperature_test_ambient_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_operating_cell_temperature_test_ambient_temperature`')

        self._data["Nominal Operating Cell Temperature Test Ambient Temperature"] = value

    @property
    def nominal_operating_cell_temperature_test_cell_temperature(self):
        """Get nominal_operating_cell_temperature_test_cell_temperature

        Returns:
            float: the value of `nominal_operating_cell_temperature_test_cell_temperature` or None if not set
        """
        return self._data["Nominal Operating Cell Temperature Test Cell Temperature"]

    @nominal_operating_cell_temperature_test_cell_temperature.setter
    def nominal_operating_cell_temperature_test_cell_temperature(self, value=40.0 ):
        """  Corresponds to IDD Field `nominal_operating_cell_temperature_test_cell_temperature`

        Args:
            value (float): value for IDD Field `nominal_operating_cell_temperature_test_cell_temperature`
                Unit: C
                Default value: 40.0
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
                                 'for field `nominal_operating_cell_temperature_test_cell_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_operating_cell_temperature_test_cell_temperature`')

        self._data["Nominal Operating Cell Temperature Test Cell Temperature"] = value

    @property
    def nominal_operating_cell_temperature_test_insolation(self):
        """Get nominal_operating_cell_temperature_test_insolation

        Returns:
            float: the value of `nominal_operating_cell_temperature_test_insolation` or None if not set
        """
        return self._data["Nominal Operating Cell Temperature Test Insolation"]

    @nominal_operating_cell_temperature_test_insolation.setter
    def nominal_operating_cell_temperature_test_insolation(self, value=800.0 ):
        """  Corresponds to IDD Field `nominal_operating_cell_temperature_test_insolation`

        Args:
            value (float): value for IDD Field `nominal_operating_cell_temperature_test_insolation`
                Unit: W/m2
                Default value: 800.0
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
                                 'for field `nominal_operating_cell_temperature_test_insolation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_operating_cell_temperature_test_insolation`')

        self._data["Nominal Operating Cell Temperature Test Insolation"] = value

    @property
    def module_heat_loss_coefficient(self):
        """Get module_heat_loss_coefficient

        Returns:
            float: the value of `module_heat_loss_coefficient` or None if not set
        """
        return self._data["Module Heat Loss Coefficient"]

    @module_heat_loss_coefficient.setter
    def module_heat_loss_coefficient(self, value=30.0 ):
        """  Corresponds to IDD Field `module_heat_loss_coefficient`

        Args:
            value (float): value for IDD Field `module_heat_loss_coefficient`
                Unit: W/m2-K
                Default value: 30.0
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
                                 'for field `module_heat_loss_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `module_heat_loss_coefficient`')

        self._data["Module Heat Loss Coefficient"] = value

    @property
    def total_heat_capacity(self):
        """Get total_heat_capacity

        Returns:
            float: the value of `total_heat_capacity` or None if not set
        """
        return self._data["Total Heat Capacity"]

    @total_heat_capacity.setter
    def total_heat_capacity(self, value=50000.0 ):
        """  Corresponds to IDD Field `total_heat_capacity`

        Args:
            value (float): value for IDD Field `total_heat_capacity`
                Unit: J/m2-K
                Default value: 50000.0
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
                                 'for field `total_heat_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `total_heat_capacity`')

        self._data["Total Heat Capacity"] = value

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
        out.append(self._to_str(self.cell_type))
        out.append(self._to_str(self.number_of_cells_in_series))
        out.append(self._to_str(self.active_area))
        out.append(self._to_str(self.transmittance_absorptance_product))
        out.append(self._to_str(self.semiconductor_bandgap))
        out.append(self._to_str(self.shunt_resistance))
        out.append(self._to_str(self.short_circuit_current))
        out.append(self._to_str(self.open_circuit_voltage))
        out.append(self._to_str(self.reference_temperature))
        out.append(self._to_str(self.reference_insolation))
        out.append(self._to_str(self.module_current_at_maximum_power))
        out.append(self._to_str(self.module_voltage_at_maximum_power))
        out.append(self._to_str(self.temperature_coefficient_of_short_circuit_current))
        out.append(self._to_str(self.temperature_coefficient_of_open_circuit_voltage))
        out.append(self._to_str(self.nominal_operating_cell_temperature_test_ambient_temperature))
        out.append(self._to_str(self.nominal_operating_cell_temperature_test_cell_temperature))
        out.append(self._to_str(self.nominal_operating_cell_temperature_test_insolation))
        out.append(self._to_str(self.module_heat_loss_coefficient))
        out.append(self._to_str(self.total_heat_capacity))
        return ",".join(out)

class PhotovoltaicPerformanceSandia(object):
    """ Corresponds to IDD object `PhotovoltaicPerformance:Sandia`
        Describes performance input data needed for specific makes and models of production
        PV panels using the empirical coefficients assembled by Sandia National Laboratory.
    """
    internal_name = "PhotovoltaicPerformance:Sandia"
    field_count = 40

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PhotovoltaicPerformance:Sandia`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Active Area"] = None
        self._data["Number of Cells in Series"] = None
        self._data["Number of Cells in Parallel"] = None
        self._data["Short Circuit Current"] = None
        self._data["Open Circuit Voltage"] = None
        self._data["Current at Maximum Power Point"] = None
        self._data["Voltage at Maximum Power Point"] = None
        self._data["Sandia Database Parameter aIsc"] = None
        self._data["Sandia Database Parameter aImp"] = None
        self._data["Sandia Database Parameter c0"] = None
        self._data["Sandia Database Parameter c1"] = None
        self._data["Sandia Database Parameter BVoc0"] = None
        self._data["Sandia Database Parameter mBVoc"] = None
        self._data["Sandia Database Parameter BVmp0"] = None
        self._data["Sandia Database Parameter mBVmp"] = None
        self._data["Diode Factor"] = None
        self._data["Sandia Database Parameter c2"] = None
        self._data["Sandia Database Parameter c3"] = None
        self._data["Sandia Database Parameter a0"] = None
        self._data["Sandia Database Parameter a1"] = None
        self._data["Sandia Database Parameter a2"] = None
        self._data["Sandia Database Parameter a3"] = None
        self._data["Sandia Database Parameter a4"] = None
        self._data["Sandia Database Parameter b0"] = None
        self._data["Sandia Database Parameter b1"] = None
        self._data["Sandia Database Parameter b2"] = None
        self._data["Sandia Database Parameter b3"] = None
        self._data["Sandia Database Parameter b4"] = None
        self._data["Sandia Database Parameter b5"] = None
        self._data["Sandia Database Parameter Delta(Tc)"] = None
        self._data["Sandia Database Parameter fd"] = None
        self._data["Sandia Database Parameter a"] = None
        self._data["Sandia Database Parameter b"] = None
        self._data["Sandia Database Parameter c4"] = None
        self._data["Sandia Database Parameter c5"] = None
        self._data["Sandia Database Parameter Ix0"] = None
        self._data["Sandia Database Parameter Ixx0"] = None
        self._data["Sandia Database Parameter c6"] = None
        self._data["Sandia Database Parameter c7"] = None

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
            self.active_area = None
        else:
            self.active_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells_in_series = None
        else:
            self.number_of_cells_in_series = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cells_in_parallel = None
        else:
            self.number_of_cells_in_parallel = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.short_circuit_current = None
        else:
            self.short_circuit_current = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.open_circuit_voltage = None
        else:
            self.open_circuit_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.current_at_maximum_power_point = None
        else:
            self.current_at_maximum_power_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.voltage_at_maximum_power_point = None
        else:
            self.voltage_at_maximum_power_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_aisc = None
        else:
            self.sandia_database_parameter_aisc = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_aimp = None
        else:
            self.sandia_database_parameter_aimp = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c0 = None
        else:
            self.sandia_database_parameter_c0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c1 = None
        else:
            self.sandia_database_parameter_c1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_bvoc0 = None
        else:
            self.sandia_database_parameter_bvoc0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_mbvoc = None
        else:
            self.sandia_database_parameter_mbvoc = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_bvmp0 = None
        else:
            self.sandia_database_parameter_bvmp0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_mbvmp = None
        else:
            self.sandia_database_parameter_mbvmp = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diode_factor = None
        else:
            self.diode_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c2 = None
        else:
            self.sandia_database_parameter_c2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c3 = None
        else:
            self.sandia_database_parameter_c3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_a0 = None
        else:
            self.sandia_database_parameter_a0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_a1 = None
        else:
            self.sandia_database_parameter_a1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_a2 = None
        else:
            self.sandia_database_parameter_a2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_a3 = None
        else:
            self.sandia_database_parameter_a3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_a4 = None
        else:
            self.sandia_database_parameter_a4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b0 = None
        else:
            self.sandia_database_parameter_b0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b1 = None
        else:
            self.sandia_database_parameter_b1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b2 = None
        else:
            self.sandia_database_parameter_b2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b3 = None
        else:
            self.sandia_database_parameter_b3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b4 = None
        else:
            self.sandia_database_parameter_b4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b5 = None
        else:
            self.sandia_database_parameter_b5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_deltatc = None
        else:
            self.sandia_database_parameter_deltatc = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_fd = None
        else:
            self.sandia_database_parameter_fd = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_a = None
        else:
            self.sandia_database_parameter_a = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_b = None
        else:
            self.sandia_database_parameter_b = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c4 = None
        else:
            self.sandia_database_parameter_c4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c5 = None
        else:
            self.sandia_database_parameter_c5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_ix0 = None
        else:
            self.sandia_database_parameter_ix0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_ixx0 = None
        else:
            self.sandia_database_parameter_ixx0 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c6 = None
        else:
            self.sandia_database_parameter_c6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sandia_database_parameter_c7 = None
        else:
            self.sandia_database_parameter_c7 = vals[i]
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
    def active_area(self):
        """Get active_area

        Returns:
            float: the value of `active_area` or None if not set
        """
        return self._data["Active Area"]

    @active_area.setter
    def active_area(self, value=1.0 ):
        """  Corresponds to IDD Field `active_area`
        (m2, single module)

        Args:
            value (float): value for IDD Field `active_area`
                Unit: m2
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `active_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `active_area`')

        self._data["Active Area"] = value

    @property
    def number_of_cells_in_series(self):
        """Get number_of_cells_in_series

        Returns:
            int: the value of `number_of_cells_in_series` or None if not set
        """
        return self._data["Number of Cells in Series"]

    @number_of_cells_in_series.setter
    def number_of_cells_in_series(self, value=1 ):
        """  Corresponds to IDD Field `number_of_cells_in_series`

        Args:
            value (int): value for IDD Field `number_of_cells_in_series`
                Unit: dimensionless
                Default value: 1
                value >= 1
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
                                 'for field `number_of_cells_in_series`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells_in_series`')

        self._data["Number of Cells in Series"] = value

    @property
    def number_of_cells_in_parallel(self):
        """Get number_of_cells_in_parallel

        Returns:
            int: the value of `number_of_cells_in_parallel` or None if not set
        """
        return self._data["Number of Cells in Parallel"]

    @number_of_cells_in_parallel.setter
    def number_of_cells_in_parallel(self, value=1 ):
        """  Corresponds to IDD Field `number_of_cells_in_parallel`

        Args:
            value (int): value for IDD Field `number_of_cells_in_parallel`
                Unit: dimensionless
                Default value: 1
                value >= 1
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
                                 'for field `number_of_cells_in_parallel`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cells_in_parallel`')

        self._data["Number of Cells in Parallel"] = value

    @property
    def short_circuit_current(self):
        """Get short_circuit_current

        Returns:
            float: the value of `short_circuit_current` or None if not set
        """
        return self._data["Short Circuit Current"]

    @short_circuit_current.setter
    def short_circuit_current(self, value=None):
        """  Corresponds to IDD Field `short_circuit_current`
        (Amps)

        Args:
            value (float): value for IDD Field `short_circuit_current`
                Unit: A
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
                                 'for field `short_circuit_current`'.format(value))

        self._data["Short Circuit Current"] = value

    @property
    def open_circuit_voltage(self):
        """Get open_circuit_voltage

        Returns:
            float: the value of `open_circuit_voltage` or None if not set
        """
        return self._data["Open Circuit Voltage"]

    @open_circuit_voltage.setter
    def open_circuit_voltage(self, value=None):
        """  Corresponds to IDD Field `open_circuit_voltage`
        (Volts)

        Args:
            value (float): value for IDD Field `open_circuit_voltage`
                Unit: V
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
                                 'for field `open_circuit_voltage`'.format(value))

        self._data["Open Circuit Voltage"] = value

    @property
    def current_at_maximum_power_point(self):
        """Get current_at_maximum_power_point

        Returns:
            float: the value of `current_at_maximum_power_point` or None if not set
        """
        return self._data["Current at Maximum Power Point"]

    @current_at_maximum_power_point.setter
    def current_at_maximum_power_point(self, value=None):
        """  Corresponds to IDD Field `current_at_maximum_power_point`
        (Amps)

        Args:
            value (float): value for IDD Field `current_at_maximum_power_point`
                Unit: A
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
                                 'for field `current_at_maximum_power_point`'.format(value))

        self._data["Current at Maximum Power Point"] = value

    @property
    def voltage_at_maximum_power_point(self):
        """Get voltage_at_maximum_power_point

        Returns:
            float: the value of `voltage_at_maximum_power_point` or None if not set
        """
        return self._data["Voltage at Maximum Power Point"]

    @voltage_at_maximum_power_point.setter
    def voltage_at_maximum_power_point(self, value=None):
        """  Corresponds to IDD Field `voltage_at_maximum_power_point`
        (Volts)

        Args:
            value (float): value for IDD Field `voltage_at_maximum_power_point`
                Unit: V
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
                                 'for field `voltage_at_maximum_power_point`'.format(value))

        self._data["Voltage at Maximum Power Point"] = value

    @property
    def sandia_database_parameter_aisc(self):
        """Get sandia_database_parameter_aisc

        Returns:
            float: the value of `sandia_database_parameter_aisc` or None if not set
        """
        return self._data["Sandia Database Parameter aIsc"]

    @sandia_database_parameter_aisc.setter
    def sandia_database_parameter_aisc(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_aisc`
        (1/degC)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_aisc`
                Unit: 1/K
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
                                 'for field `sandia_database_parameter_aisc`'.format(value))

        self._data["Sandia Database Parameter aIsc"] = value

    @property
    def sandia_database_parameter_aimp(self):
        """Get sandia_database_parameter_aimp

        Returns:
            float: the value of `sandia_database_parameter_aimp` or None if not set
        """
        return self._data["Sandia Database Parameter aImp"]

    @sandia_database_parameter_aimp.setter
    def sandia_database_parameter_aimp(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_aimp`
        (1/degC)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_aimp`
                Unit: 1/K
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
                                 'for field `sandia_database_parameter_aimp`'.format(value))

        self._data["Sandia Database Parameter aImp"] = value

    @property
    def sandia_database_parameter_c0(self):
        """Get sandia_database_parameter_c0

        Returns:
            float: the value of `sandia_database_parameter_c0` or None if not set
        """
        return self._data["Sandia Database Parameter c0"]

    @sandia_database_parameter_c0.setter
    def sandia_database_parameter_c0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c0`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c0`
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
                                 'for field `sandia_database_parameter_c0`'.format(value))

        self._data["Sandia Database Parameter c0"] = value

    @property
    def sandia_database_parameter_c1(self):
        """Get sandia_database_parameter_c1

        Returns:
            float: the value of `sandia_database_parameter_c1` or None if not set
        """
        return self._data["Sandia Database Parameter c1"]

    @sandia_database_parameter_c1.setter
    def sandia_database_parameter_c1(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c1`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c1`
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
                                 'for field `sandia_database_parameter_c1`'.format(value))

        self._data["Sandia Database Parameter c1"] = value

    @property
    def sandia_database_parameter_bvoc0(self):
        """Get sandia_database_parameter_bvoc0

        Returns:
            float: the value of `sandia_database_parameter_bvoc0` or None if not set
        """
        return self._data["Sandia Database Parameter BVoc0"]

    @sandia_database_parameter_bvoc0.setter
    def sandia_database_parameter_bvoc0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_bvoc0`
        (Volts/degC)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_bvoc0`
                Unit: V/K
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
                                 'for field `sandia_database_parameter_bvoc0`'.format(value))

        self._data["Sandia Database Parameter BVoc0"] = value

    @property
    def sandia_database_parameter_mbvoc(self):
        """Get sandia_database_parameter_mbvoc

        Returns:
            float: the value of `sandia_database_parameter_mbvoc` or None if not set
        """
        return self._data["Sandia Database Parameter mBVoc"]

    @sandia_database_parameter_mbvoc.setter
    def sandia_database_parameter_mbvoc(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_mbvoc`
        (Volts/degC)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_mbvoc`
                Unit: V/K
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
                                 'for field `sandia_database_parameter_mbvoc`'.format(value))

        self._data["Sandia Database Parameter mBVoc"] = value

    @property
    def sandia_database_parameter_bvmp0(self):
        """Get sandia_database_parameter_bvmp0

        Returns:
            float: the value of `sandia_database_parameter_bvmp0` or None if not set
        """
        return self._data["Sandia Database Parameter BVmp0"]

    @sandia_database_parameter_bvmp0.setter
    def sandia_database_parameter_bvmp0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_bvmp0`
        (Volts/degC)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_bvmp0`
                Unit: V/K
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
                                 'for field `sandia_database_parameter_bvmp0`'.format(value))

        self._data["Sandia Database Parameter BVmp0"] = value

    @property
    def sandia_database_parameter_mbvmp(self):
        """Get sandia_database_parameter_mbvmp

        Returns:
            float: the value of `sandia_database_parameter_mbvmp` or None if not set
        """
        return self._data["Sandia Database Parameter mBVmp"]

    @sandia_database_parameter_mbvmp.setter
    def sandia_database_parameter_mbvmp(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_mbvmp`
        (Volts/degC)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_mbvmp`
                Unit: V/K
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
                                 'for field `sandia_database_parameter_mbvmp`'.format(value))

        self._data["Sandia Database Parameter mBVmp"] = value

    @property
    def diode_factor(self):
        """Get diode_factor

        Returns:
            float: the value of `diode_factor` or None if not set
        """
        return self._data["Diode Factor"]

    @diode_factor.setter
    def diode_factor(self, value=None):
        """  Corresponds to IDD Field `diode_factor`
        (nondimensional)

        Args:
            value (float): value for IDD Field `diode_factor`
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
                                 'for field `diode_factor`'.format(value))

        self._data["Diode Factor"] = value

    @property
    def sandia_database_parameter_c2(self):
        """Get sandia_database_parameter_c2

        Returns:
            float: the value of `sandia_database_parameter_c2` or None if not set
        """
        return self._data["Sandia Database Parameter c2"]

    @sandia_database_parameter_c2.setter
    def sandia_database_parameter_c2(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c2`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c2`
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
                                 'for field `sandia_database_parameter_c2`'.format(value))

        self._data["Sandia Database Parameter c2"] = value

    @property
    def sandia_database_parameter_c3(self):
        """Get sandia_database_parameter_c3

        Returns:
            float: the value of `sandia_database_parameter_c3` or None if not set
        """
        return self._data["Sandia Database Parameter c3"]

    @sandia_database_parameter_c3.setter
    def sandia_database_parameter_c3(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c3`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c3`
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
                                 'for field `sandia_database_parameter_c3`'.format(value))

        self._data["Sandia Database Parameter c3"] = value

    @property
    def sandia_database_parameter_a0(self):
        """Get sandia_database_parameter_a0

        Returns:
            float: the value of `sandia_database_parameter_a0` or None if not set
        """
        return self._data["Sandia Database Parameter a0"]

    @sandia_database_parameter_a0.setter
    def sandia_database_parameter_a0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_a0`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_a0`
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
                                 'for field `sandia_database_parameter_a0`'.format(value))

        self._data["Sandia Database Parameter a0"] = value

    @property
    def sandia_database_parameter_a1(self):
        """Get sandia_database_parameter_a1

        Returns:
            float: the value of `sandia_database_parameter_a1` or None if not set
        """
        return self._data["Sandia Database Parameter a1"]

    @sandia_database_parameter_a1.setter
    def sandia_database_parameter_a1(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_a1`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_a1`
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
                                 'for field `sandia_database_parameter_a1`'.format(value))

        self._data["Sandia Database Parameter a1"] = value

    @property
    def sandia_database_parameter_a2(self):
        """Get sandia_database_parameter_a2

        Returns:
            float: the value of `sandia_database_parameter_a2` or None if not set
        """
        return self._data["Sandia Database Parameter a2"]

    @sandia_database_parameter_a2.setter
    def sandia_database_parameter_a2(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_a2`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_a2`
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
                                 'for field `sandia_database_parameter_a2`'.format(value))

        self._data["Sandia Database Parameter a2"] = value

    @property
    def sandia_database_parameter_a3(self):
        """Get sandia_database_parameter_a3

        Returns:
            float: the value of `sandia_database_parameter_a3` or None if not set
        """
        return self._data["Sandia Database Parameter a3"]

    @sandia_database_parameter_a3.setter
    def sandia_database_parameter_a3(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_a3`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_a3`
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
                                 'for field `sandia_database_parameter_a3`'.format(value))

        self._data["Sandia Database Parameter a3"] = value

    @property
    def sandia_database_parameter_a4(self):
        """Get sandia_database_parameter_a4

        Returns:
            float: the value of `sandia_database_parameter_a4` or None if not set
        """
        return self._data["Sandia Database Parameter a4"]

    @sandia_database_parameter_a4.setter
    def sandia_database_parameter_a4(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_a4`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_a4`
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
                                 'for field `sandia_database_parameter_a4`'.format(value))

        self._data["Sandia Database Parameter a4"] = value

    @property
    def sandia_database_parameter_b0(self):
        """Get sandia_database_parameter_b0

        Returns:
            float: the value of `sandia_database_parameter_b0` or None if not set
        """
        return self._data["Sandia Database Parameter b0"]

    @sandia_database_parameter_b0.setter
    def sandia_database_parameter_b0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b0`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b0`
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
                                 'for field `sandia_database_parameter_b0`'.format(value))

        self._data["Sandia Database Parameter b0"] = value

    @property
    def sandia_database_parameter_b1(self):
        """Get sandia_database_parameter_b1

        Returns:
            float: the value of `sandia_database_parameter_b1` or None if not set
        """
        return self._data["Sandia Database Parameter b1"]

    @sandia_database_parameter_b1.setter
    def sandia_database_parameter_b1(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b1`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b1`
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
                                 'for field `sandia_database_parameter_b1`'.format(value))

        self._data["Sandia Database Parameter b1"] = value

    @property
    def sandia_database_parameter_b2(self):
        """Get sandia_database_parameter_b2

        Returns:
            float: the value of `sandia_database_parameter_b2` or None if not set
        """
        return self._data["Sandia Database Parameter b2"]

    @sandia_database_parameter_b2.setter
    def sandia_database_parameter_b2(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b2`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b2`
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
                                 'for field `sandia_database_parameter_b2`'.format(value))

        self._data["Sandia Database Parameter b2"] = value

    @property
    def sandia_database_parameter_b3(self):
        """Get sandia_database_parameter_b3

        Returns:
            float: the value of `sandia_database_parameter_b3` or None if not set
        """
        return self._data["Sandia Database Parameter b3"]

    @sandia_database_parameter_b3.setter
    def sandia_database_parameter_b3(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b3`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b3`
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
                                 'for field `sandia_database_parameter_b3`'.format(value))

        self._data["Sandia Database Parameter b3"] = value

    @property
    def sandia_database_parameter_b4(self):
        """Get sandia_database_parameter_b4

        Returns:
            float: the value of `sandia_database_parameter_b4` or None if not set
        """
        return self._data["Sandia Database Parameter b4"]

    @sandia_database_parameter_b4.setter
    def sandia_database_parameter_b4(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b4`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b4`
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
                                 'for field `sandia_database_parameter_b4`'.format(value))

        self._data["Sandia Database Parameter b4"] = value

    @property
    def sandia_database_parameter_b5(self):
        """Get sandia_database_parameter_b5

        Returns:
            float: the value of `sandia_database_parameter_b5` or None if not set
        """
        return self._data["Sandia Database Parameter b5"]

    @sandia_database_parameter_b5.setter
    def sandia_database_parameter_b5(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b5`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b5`
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
                                 'for field `sandia_database_parameter_b5`'.format(value))

        self._data["Sandia Database Parameter b5"] = value

    @property
    def sandia_database_parameter_deltatc(self):
        """Get sandia_database_parameter_deltatc

        Returns:
            float: the value of `sandia_database_parameter_deltatc` or None if not set
        """
        return self._data["Sandia Database Parameter Delta(Tc)"]

    @sandia_database_parameter_deltatc.setter
    def sandia_database_parameter_deltatc(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_deltatc`
        (deg C)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_deltatc`
                Unit: deltaC
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
                                 'for field `sandia_database_parameter_deltatc`'.format(value))

        self._data["Sandia Database Parameter Delta(Tc)"] = value

    @property
    def sandia_database_parameter_fd(self):
        """Get sandia_database_parameter_fd

        Returns:
            float: the value of `sandia_database_parameter_fd` or None if not set
        """
        return self._data["Sandia Database Parameter fd"]

    @sandia_database_parameter_fd.setter
    def sandia_database_parameter_fd(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_fd`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_fd`
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
                                 'for field `sandia_database_parameter_fd`'.format(value))

        self._data["Sandia Database Parameter fd"] = value

    @property
    def sandia_database_parameter_a(self):
        """Get sandia_database_parameter_a

        Returns:
            float: the value of `sandia_database_parameter_a` or None if not set
        """
        return self._data["Sandia Database Parameter a"]

    @sandia_database_parameter_a.setter
    def sandia_database_parameter_a(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_a`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_a`
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
                                 'for field `sandia_database_parameter_a`'.format(value))

        self._data["Sandia Database Parameter a"] = value

    @property
    def sandia_database_parameter_b(self):
        """Get sandia_database_parameter_b

        Returns:
            float: the value of `sandia_database_parameter_b` or None if not set
        """
        return self._data["Sandia Database Parameter b"]

    @sandia_database_parameter_b.setter
    def sandia_database_parameter_b(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_b`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_b`
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
                                 'for field `sandia_database_parameter_b`'.format(value))

        self._data["Sandia Database Parameter b"] = value

    @property
    def sandia_database_parameter_c4(self):
        """Get sandia_database_parameter_c4

        Returns:
            float: the value of `sandia_database_parameter_c4` or None if not set
        """
        return self._data["Sandia Database Parameter c4"]

    @sandia_database_parameter_c4.setter
    def sandia_database_parameter_c4(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c4`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c4`
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
                                 'for field `sandia_database_parameter_c4`'.format(value))

        self._data["Sandia Database Parameter c4"] = value

    @property
    def sandia_database_parameter_c5(self):
        """Get sandia_database_parameter_c5

        Returns:
            float: the value of `sandia_database_parameter_c5` or None if not set
        """
        return self._data["Sandia Database Parameter c5"]

    @sandia_database_parameter_c5.setter
    def sandia_database_parameter_c5(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c5`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c5`
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
                                 'for field `sandia_database_parameter_c5`'.format(value))

        self._data["Sandia Database Parameter c5"] = value

    @property
    def sandia_database_parameter_ix0(self):
        """Get sandia_database_parameter_ix0

        Returns:
            float: the value of `sandia_database_parameter_ix0` or None if not set
        """
        return self._data["Sandia Database Parameter Ix0"]

    @sandia_database_parameter_ix0.setter
    def sandia_database_parameter_ix0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_ix0`
        (Amps)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_ix0`
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
                                 'for field `sandia_database_parameter_ix0`'.format(value))

        self._data["Sandia Database Parameter Ix0"] = value

    @property
    def sandia_database_parameter_ixx0(self):
        """Get sandia_database_parameter_ixx0

        Returns:
            float: the value of `sandia_database_parameter_ixx0` or None if not set
        """
        return self._data["Sandia Database Parameter Ixx0"]

    @sandia_database_parameter_ixx0.setter
    def sandia_database_parameter_ixx0(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_ixx0`
        (Amps)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_ixx0`
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
                                 'for field `sandia_database_parameter_ixx0`'.format(value))

        self._data["Sandia Database Parameter Ixx0"] = value

    @property
    def sandia_database_parameter_c6(self):
        """Get sandia_database_parameter_c6

        Returns:
            float: the value of `sandia_database_parameter_c6` or None if not set
        """
        return self._data["Sandia Database Parameter c6"]

    @sandia_database_parameter_c6.setter
    def sandia_database_parameter_c6(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c6`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c6`
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
                                 'for field `sandia_database_parameter_c6`'.format(value))

        self._data["Sandia Database Parameter c6"] = value

    @property
    def sandia_database_parameter_c7(self):
        """Get sandia_database_parameter_c7

        Returns:
            float: the value of `sandia_database_parameter_c7` or None if not set
        """
        return self._data["Sandia Database Parameter c7"]

    @sandia_database_parameter_c7.setter
    def sandia_database_parameter_c7(self, value=None):
        """  Corresponds to IDD Field `sandia_database_parameter_c7`
        (nondimensional)

        Args:
            value (float): value for IDD Field `sandia_database_parameter_c7`
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
                                 'for field `sandia_database_parameter_c7`'.format(value))

        self._data["Sandia Database Parameter c7"] = value

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
        out.append(self._to_str(self.active_area))
        out.append(self._to_str(self.number_of_cells_in_series))
        out.append(self._to_str(self.number_of_cells_in_parallel))
        out.append(self._to_str(self.short_circuit_current))
        out.append(self._to_str(self.open_circuit_voltage))
        out.append(self._to_str(self.current_at_maximum_power_point))
        out.append(self._to_str(self.voltage_at_maximum_power_point))
        out.append(self._to_str(self.sandia_database_parameter_aisc))
        out.append(self._to_str(self.sandia_database_parameter_aimp))
        out.append(self._to_str(self.sandia_database_parameter_c0))
        out.append(self._to_str(self.sandia_database_parameter_c1))
        out.append(self._to_str(self.sandia_database_parameter_bvoc0))
        out.append(self._to_str(self.sandia_database_parameter_mbvoc))
        out.append(self._to_str(self.sandia_database_parameter_bvmp0))
        out.append(self._to_str(self.sandia_database_parameter_mbvmp))
        out.append(self._to_str(self.diode_factor))
        out.append(self._to_str(self.sandia_database_parameter_c2))
        out.append(self._to_str(self.sandia_database_parameter_c3))
        out.append(self._to_str(self.sandia_database_parameter_a0))
        out.append(self._to_str(self.sandia_database_parameter_a1))
        out.append(self._to_str(self.sandia_database_parameter_a2))
        out.append(self._to_str(self.sandia_database_parameter_a3))
        out.append(self._to_str(self.sandia_database_parameter_a4))
        out.append(self._to_str(self.sandia_database_parameter_b0))
        out.append(self._to_str(self.sandia_database_parameter_b1))
        out.append(self._to_str(self.sandia_database_parameter_b2))
        out.append(self._to_str(self.sandia_database_parameter_b3))
        out.append(self._to_str(self.sandia_database_parameter_b4))
        out.append(self._to_str(self.sandia_database_parameter_b5))
        out.append(self._to_str(self.sandia_database_parameter_deltatc))
        out.append(self._to_str(self.sandia_database_parameter_fd))
        out.append(self._to_str(self.sandia_database_parameter_a))
        out.append(self._to_str(self.sandia_database_parameter_b))
        out.append(self._to_str(self.sandia_database_parameter_c4))
        out.append(self._to_str(self.sandia_database_parameter_c5))
        out.append(self._to_str(self.sandia_database_parameter_ix0))
        out.append(self._to_str(self.sandia_database_parameter_ixx0))
        out.append(self._to_str(self.sandia_database_parameter_c6))
        out.append(self._to_str(self.sandia_database_parameter_c7))
        return ",".join(out)