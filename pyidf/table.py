from collections import OrderedDict

class TableOneIndependentVariable(object):
    """ Corresponds to IDD object `Table:OneIndependentVariable`
        Allows entry of tabular data pairs as alternate input
        for performance curve objects.
        Performance curve objects can be created using these inputs.
        Linear Table Equation: Output = a + bX
        Linear solution requires a minimum of 2 data pairs
        Quadratic Table Equation: Output = a + b*X + c*X**2
        Quadratic solution requires a minimum of 3 data pairs
        Cubic Table Equation: Output = a + b*X + c* X**2 + d*X**3
        Cubic solution requires a minimum of 4 data pairs
        Quartic Table Equation: Output = a + b*X + c* X**2 + d*X**3 + e*X**4
        Quartic solution requires a minimum of 5 data pairs
        Exponent Table Equation: Output = a + b*X**c
        Exponent solution requires a minimum of 4 data pairs
    """
    internal_name = "Table:OneIndependentVariable"
    field_count = 29

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Table:OneIndependentVariable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Curve Type"] = None
        self._data["Interpolation Method"] = None
        self._data["Minimum Value of X"] = None
        self._data["Maximum Value of X"] = None
        self._data["Minimum Table Output"] = None
        self._data["Maximum Table Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Output Unit Type"] = None
        self._data["Normalization Reference"] = None
        self._data["X Value #1"] = None
        self._data["Output Value #1"] = None
        self._data["X Value #2"] = None
        self._data["Output Value #2"] = None
        self._data["X Value #3"] = None
        self._data["Output Value #3"] = None
        self._data["X Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["X Value #5"] = None
        self._data["Output Value #5"] = None
        self._data["X Value #6"] = None
        self._data["Output Value #6"] = None
        self._data["X Value #7"] = None
        self._data["Output Value #7"] = None
        self._data["Output Value #7"] = None
        self._data["Output Value #7"] = None
        self._data["Output Value #7"] = None
        self._data["Output Value #7"] = None
        self._data["Output Value #7"] = None

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
            self.curve_type = None
        else:
            self.curve_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.interpolation_method = None
        else:
            self.interpolation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_table_output = None
        else:
            self.minimum_table_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_table_output = None
        else:
            self.maximum_table_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.normalization_reference = None
        else:
            self.normalization_reference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_1 = None
        else:
            self.x_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_1 = None
        else:
            self.output_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_2 = None
        else:
            self.x_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_2 = None
        else:
            self.output_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_3 = None
        else:
            self.x_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_3 = None
        else:
            self.output_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_4 = None
        else:
            self.x_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_5 = None
        else:
            self.x_value_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_5 = None
        else:
            self.output_value_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_6 = None
        else:
            self.x_value_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_6 = None
        else:
            self.output_value_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_7 = None
        else:
            self.x_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_7 = None
        else:
            self.output_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_7 = None
        else:
            self.output_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_7 = None
        else:
            self.output_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_7 = None
        else:
            self.output_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_7 = None
        else:
            self.output_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_7 = None
        else:
            self.output_value_7 = vals[i]
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
    def curve_type(self):
        """Get curve_type

        Returns:
            str: the value of `curve_type` or None if not set
        """
        return self._data["Curve Type"]

    @curve_type.setter
    def curve_type(self, value=None):
        """  Corresponds to IDD Field `curve_type`

        Args:
            value (str): value for IDD Field `curve_type`
                Accepted values are:
                      - Linear
                      - Quadratic
                      - Cubic
                      - Quartic
                      - Exponent
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
                                 'for field `curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `curve_type`')
            vals = set()
            vals.add("Linear")
            vals.add("Quadratic")
            vals.add("Cubic")
            vals.add("Quartic")
            vals.add("Exponent")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `curve_type`'.format(value))

        self._data["Curve Type"] = value

    @property
    def interpolation_method(self):
        """Get interpolation_method

        Returns:
            str: the value of `interpolation_method` or None if not set
        """
        return self._data["Interpolation Method"]

    @interpolation_method.setter
    def interpolation_method(self, value=None):
        """  Corresponds to IDD Field `interpolation_method`

        Args:
            value (str): value for IDD Field `interpolation_method`
                Accepted values are:
                      - LinearInterpolationOfTable
                      - EvaluateCurveToLimits
                      - LagrangeInterpolationLinearExtrapolation
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
                                 'for field `interpolation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `interpolation_method`')
            vals = set()
            vals.add("LinearInterpolationOfTable")
            vals.add("EvaluateCurveToLimits")
            vals.add("LagrangeInterpolationLinearExtrapolation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `interpolation_method`'.format(value))

        self._data["Interpolation Method"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of X"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x`
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `minimum_value_of_x`
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
                                 'for field `minimum_value_of_x`'.format(value))

        self._data["Minimum Value of X"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of X"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x`
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `maximum_value_of_x`
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
                                 'for field `maximum_value_of_x`'.format(value))

        self._data["Maximum Value of X"] = value

    @property
    def minimum_table_output(self):
        """Get minimum_table_output

        Returns:
            float: the value of `minimum_table_output` or None if not set
        """
        return self._data["Minimum Table Output"]

    @minimum_table_output.setter
    def minimum_table_output(self, value=None):
        """  Corresponds to IDD Field `minimum_table_output`
        Specify the minimum value calculated by this table
        lookup object
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `minimum_table_output`
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
                                 'for field `minimum_table_output`'.format(value))

        self._data["Minimum Table Output"] = value

    @property
    def maximum_table_output(self):
        """Get maximum_table_output

        Returns:
            float: the value of `maximum_table_output` or None if not set
        """
        return self._data["Maximum Table Output"]

    @maximum_table_output.setter
    def maximum_table_output(self, value=None):
        """  Corresponds to IDD Field `maximum_table_output`
        Specify the maximum value calculated by this table
        lookup object
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `maximum_table_output`
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
                                 'for field `maximum_table_output`'.format(value))

        self._data["Maximum Table Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x`'.format(value))

        self._data["Input Unit Type for X"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `output_unit_type`

        Args:
            value (str): value for IDD Field `output_unit_type`
                Accepted values are:
                      - Dimensionless
                      - Capacity
                      - Power
                Default value: Dimensionless
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
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Capacity")
            vals.add("Power")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `output_unit_type`'.format(value))

        self._data["Output Unit Type"] = value

    @property
    def normalization_reference(self):
        """Get normalization_reference

        Returns:
            float: the value of `normalization_reference` or None if not set
        """
        return self._data["Normalization Reference"]

    @normalization_reference.setter
    def normalization_reference(self, value=None):
        """  Corresponds to IDD Field `normalization_reference`
        This field is used to normalize the following ouput data.
        The minimum and maximum table output fields are also normalized.
        If this field is blank or 1, the table data presented
        in the following fields will be used with normalization
        reference set to 1.

        Args:
            value (float): value for IDD Field `normalization_reference`
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
                                 'for field `normalization_reference`'.format(value))

        self._data["Normalization Reference"] = value

    @property
    def x_value_1(self):
        """Get x_value_1

        Returns:
            float: the value of `x_value_1` or None if not set
        """
        return self._data["X Value #1"]

    @x_value_1.setter
    def x_value_1(self, value=None):
        """  Corresponds to IDD Field `x_value_1`

        Args:
            value (float): value for IDD Field `x_value_1`
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
                                 'for field `x_value_1`'.format(value))

        self._data["X Value #1"] = value

    @property
    def output_value_1(self):
        """Get output_value_1

        Returns:
            float: the value of `output_value_1` or None if not set
        """
        return self._data["Output Value #1"]

    @output_value_1.setter
    def output_value_1(self, value=None):
        """  Corresponds to IDD Field `output_value_1`

        Args:
            value (float): value for IDD Field `output_value_1`
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
                                 'for field `output_value_1`'.format(value))

        self._data["Output Value #1"] = value

    @property
    def x_value_2(self):
        """Get x_value_2

        Returns:
            float: the value of `x_value_2` or None if not set
        """
        return self._data["X Value #2"]

    @x_value_2.setter
    def x_value_2(self, value=None):
        """  Corresponds to IDD Field `x_value_2`

        Args:
            value (float): value for IDD Field `x_value_2`
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
                                 'for field `x_value_2`'.format(value))

        self._data["X Value #2"] = value

    @property
    def output_value_2(self):
        """Get output_value_2

        Returns:
            float: the value of `output_value_2` or None if not set
        """
        return self._data["Output Value #2"]

    @output_value_2.setter
    def output_value_2(self, value=None):
        """  Corresponds to IDD Field `output_value_2`

        Args:
            value (float): value for IDD Field `output_value_2`
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
                                 'for field `output_value_2`'.format(value))

        self._data["Output Value #2"] = value

    @property
    def x_value_3(self):
        """Get x_value_3

        Returns:
            float: the value of `x_value_3` or None if not set
        """
        return self._data["X Value #3"]

    @x_value_3.setter
    def x_value_3(self, value=None):
        """  Corresponds to IDD Field `x_value_3`

        Args:
            value (float): value for IDD Field `x_value_3`
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
                                 'for field `x_value_3`'.format(value))

        self._data["X Value #3"] = value

    @property
    def output_value_3(self):
        """Get output_value_3

        Returns:
            float: the value of `output_value_3` or None if not set
        """
        return self._data["Output Value #3"]

    @output_value_3.setter
    def output_value_3(self, value=None):
        """  Corresponds to IDD Field `output_value_3`

        Args:
            value (float): value for IDD Field `output_value_3`
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
                                 'for field `output_value_3`'.format(value))

        self._data["Output Value #3"] = value

    @property
    def x_value_4(self):
        """Get x_value_4

        Returns:
            float: the value of `x_value_4` or None if not set
        """
        return self._data["X Value #4"]

    @x_value_4.setter
    def x_value_4(self, value=None):
        """  Corresponds to IDD Field `x_value_4`

        Args:
            value (float): value for IDD Field `x_value_4`
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
                                 'for field `x_value_4`'.format(value))

        self._data["X Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def x_value_5(self):
        """Get x_value_5

        Returns:
            float: the value of `x_value_5` or None if not set
        """
        return self._data["X Value #5"]

    @x_value_5.setter
    def x_value_5(self, value=None):
        """  Corresponds to IDD Field `x_value_5`

        Args:
            value (float): value for IDD Field `x_value_5`
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
                                 'for field `x_value_5`'.format(value))

        self._data["X Value #5"] = value

    @property
    def output_value_5(self):
        """Get output_value_5

        Returns:
            float: the value of `output_value_5` or None if not set
        """
        return self._data["Output Value #5"]

    @output_value_5.setter
    def output_value_5(self, value=None):
        """  Corresponds to IDD Field `output_value_5`

        Args:
            value (float): value for IDD Field `output_value_5`
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
                                 'for field `output_value_5`'.format(value))

        self._data["Output Value #5"] = value

    @property
    def x_value_6(self):
        """Get x_value_6

        Returns:
            float: the value of `x_value_6` or None if not set
        """
        return self._data["X Value #6"]

    @x_value_6.setter
    def x_value_6(self, value=None):
        """  Corresponds to IDD Field `x_value_6`

        Args:
            value (float): value for IDD Field `x_value_6`
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
                                 'for field `x_value_6`'.format(value))

        self._data["X Value #6"] = value

    @property
    def output_value_6(self):
        """Get output_value_6

        Returns:
            float: the value of `output_value_6` or None if not set
        """
        return self._data["Output Value #6"]

    @output_value_6.setter
    def output_value_6(self, value=None):
        """  Corresponds to IDD Field `output_value_6`

        Args:
            value (float): value for IDD Field `output_value_6`
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
                                 'for field `output_value_6`'.format(value))

        self._data["Output Value #6"] = value

    @property
    def x_value_7(self):
        """Get x_value_7

        Returns:
            float: the value of `x_value_7` or None if not set
        """
        return self._data["X Value #7"]

    @x_value_7.setter
    def x_value_7(self, value=None):
        """  Corresponds to IDD Field `x_value_7`

        Args:
            value (float): value for IDD Field `x_value_7`
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
                                 'for field `x_value_7`'.format(value))

        self._data["X Value #7"] = value

    @property
    def output_value_7(self):
        """Get output_value_7

        Returns:
            float: the value of `output_value_7` or None if not set
        """
        return self._data["Output Value #7"]

    @output_value_7.setter
    def output_value_7(self, value=None):
        """  Corresponds to IDD Field `output_value_7`

        Args:
            value (float): value for IDD Field `output_value_7`
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
                                 'for field `output_value_7`'.format(value))

        self._data["Output Value #7"] = value

    @property
    def output_value_7(self):
        """Get output_value_7

        Returns:
            float: the value of `output_value_7` or None if not set
        """
        return self._data["Output Value #7"]

    @output_value_7.setter
    def output_value_7(self, value=None):
        """  Corresponds to IDD Field `output_value_7`

        Args:
            value (float): value for IDD Field `output_value_7`
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
                                 'for field `output_value_7`'.format(value))

        self._data["Output Value #7"] = value

    @property
    def output_value_7(self):
        """Get output_value_7

        Returns:
            float: the value of `output_value_7` or None if not set
        """
        return self._data["Output Value #7"]

    @output_value_7.setter
    def output_value_7(self, value=None):
        """  Corresponds to IDD Field `output_value_7`

        Args:
            value (float): value for IDD Field `output_value_7`
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
                                 'for field `output_value_7`'.format(value))

        self._data["Output Value #7"] = value

    @property
    def output_value_7(self):
        """Get output_value_7

        Returns:
            float: the value of `output_value_7` or None if not set
        """
        return self._data["Output Value #7"]

    @output_value_7.setter
    def output_value_7(self, value=None):
        """  Corresponds to IDD Field `output_value_7`

        Args:
            value (float): value for IDD Field `output_value_7`
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
                                 'for field `output_value_7`'.format(value))

        self._data["Output Value #7"] = value

    @property
    def output_value_7(self):
        """Get output_value_7

        Returns:
            float: the value of `output_value_7` or None if not set
        """
        return self._data["Output Value #7"]

    @output_value_7.setter
    def output_value_7(self, value=None):
        """  Corresponds to IDD Field `output_value_7`

        Args:
            value (float): value for IDD Field `output_value_7`
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
                                 'for field `output_value_7`'.format(value))

        self._data["Output Value #7"] = value

    @property
    def output_value_7(self):
        """Get output_value_7

        Returns:
            float: the value of `output_value_7` or None if not set
        """
        return self._data["Output Value #7"]

    @output_value_7.setter
    def output_value_7(self, value=None):
        """  Corresponds to IDD Field `output_value_7`

        Args:
            value (float): value for IDD Field `output_value_7`
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
                                 'for field `output_value_7`'.format(value))

        self._data["Output Value #7"] = value

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
        out.append(self._to_str(self.curve_type))
        out.append(self._to_str(self.interpolation_method))
        out.append(self._to_str(self.minimum_value_of_x))
        out.append(self._to_str(self.maximum_value_of_x))
        out.append(self._to_str(self.minimum_table_output))
        out.append(self._to_str(self.maximum_table_output))
        out.append(self._to_str(self.input_unit_type_for_x))
        out.append(self._to_str(self.output_unit_type))
        out.append(self._to_str(self.normalization_reference))
        out.append(self._to_str(self.x_value_1))
        out.append(self._to_str(self.output_value_1))
        out.append(self._to_str(self.x_value_2))
        out.append(self._to_str(self.output_value_2))
        out.append(self._to_str(self.x_value_3))
        out.append(self._to_str(self.output_value_3))
        out.append(self._to_str(self.x_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.x_value_5))
        out.append(self._to_str(self.output_value_5))
        out.append(self._to_str(self.x_value_6))
        out.append(self._to_str(self.output_value_6))
        out.append(self._to_str(self.x_value_7))
        out.append(self._to_str(self.output_value_7))
        out.append(self._to_str(self.output_value_7))
        out.append(self._to_str(self.output_value_7))
        out.append(self._to_str(self.output_value_7))
        out.append(self._to_str(self.output_value_7))
        out.append(self._to_str(self.output_value_7))
        return ",".join(out)

class TableTwoIndependentVariables(object):
    """ Corresponds to IDD object `Table:TwoIndependentVariables`
        Allows entry of tabular data pairs as alternate input
        for performance curve objects.
        Performance curve objects can be created using these inputs.
        BiQuadratic Table Equation: Output = a + bX + cX**2 + dY + eY**2 + fXY
        BiQuadratic solution requires a minimum of 6 data pairs
        QuadraticLinear Table Equation: Output = a + bX + cX**2 + dY + eXY + fX**2Y
        QuadraticLinear solution requires a minimum of 6 data pairs
    """
    internal_name = "Table:TwoIndependentVariables"
    field_count = 64

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Table:TwoIndependentVariables`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Curve Type"] = None
        self._data["Interpolation Method"] = None
        self._data["Minimum Value of X"] = None
        self._data["Maximum Value of X"] = None
        self._data["Minimum Value of Y"] = None
        self._data["Maximum Value of Y"] = None
        self._data["Minimum Table Output"] = None
        self._data["Maximum Table Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Input Unit Type for Y"] = None
        self._data["Output Unit Type"] = None
        self._data["Normalization Reference"] = None
        self._data["X Value #1"] = None
        self._data["Y Value #1"] = None
        self._data["Output Value #1"] = None
        self._data["X Value #2"] = None
        self._data["Y Value #2"] = None
        self._data["Output Value #2"] = None
        self._data["X Value #3"] = None
        self._data["Y Value #3"] = None
        self._data["Output Value #3"] = None
        self._data["X Value #4"] = None
        self._data["Y Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None
        self._data["Output Value #4"] = None

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
            self.curve_type = None
        else:
            self.curve_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.interpolation_method = None
        else:
            self.interpolation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_y = None
        else:
            self.minimum_value_of_y = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_y = None
        else:
            self.maximum_value_of_y = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_table_output = None
        else:
            self.minimum_table_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_table_output = None
        else:
            self.maximum_table_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_y = None
        else:
            self.input_unit_type_for_y = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.normalization_reference = None
        else:
            self.normalization_reference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_1 = None
        else:
            self.x_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.y_value_1 = None
        else:
            self.y_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_1 = None
        else:
            self.output_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_2 = None
        else:
            self.x_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.y_value_2 = None
        else:
            self.y_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_2 = None
        else:
            self.output_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_3 = None
        else:
            self.x_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.y_value_3 = None
        else:
            self.y_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_3 = None
        else:
            self.output_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x_value_4 = None
        else:
            self.x_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.y_value_4 = None
        else:
            self.y_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_value_4 = None
        else:
            self.output_value_4 = vals[i]
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
    def curve_type(self):
        """Get curve_type

        Returns:
            str: the value of `curve_type` or None if not set
        """
        return self._data["Curve Type"]

    @curve_type.setter
    def curve_type(self, value=None):
        """  Corresponds to IDD Field `curve_type`

        Args:
            value (str): value for IDD Field `curve_type`
                Accepted values are:
                      - BiQuadratic
                      - QuadraticLinear
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
                                 'for field `curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `curve_type`')
            vals = set()
            vals.add("BiQuadratic")
            vals.add("QuadraticLinear")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `curve_type`'.format(value))

        self._data["Curve Type"] = value

    @property
    def interpolation_method(self):
        """Get interpolation_method

        Returns:
            str: the value of `interpolation_method` or None if not set
        """
        return self._data["Interpolation Method"]

    @interpolation_method.setter
    def interpolation_method(self, value="LagrangeInterpolationLinearExtrapolation"):
        """  Corresponds to IDD Field `interpolation_method`

        Args:
            value (str): value for IDD Field `interpolation_method`
                Accepted values are:
                      - LinearInterpolationOfTable
                      - EvaluateCurveToLimits
                      - LagrangeInterpolationLinearExtrapolation
                Default value: LagrangeInterpolationLinearExtrapolation
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
                                 'for field `interpolation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `interpolation_method`')
            vals = set()
            vals.add("LinearInterpolationOfTable")
            vals.add("EvaluateCurveToLimits")
            vals.add("LagrangeInterpolationLinearExtrapolation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `interpolation_method`'.format(value))

        self._data["Interpolation Method"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of X"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x`

        Args:
            value (float): value for IDD Field `minimum_value_of_x`
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
                                 'for field `minimum_value_of_x`'.format(value))

        self._data["Minimum Value of X"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of X"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x`

        Args:
            value (float): value for IDD Field `maximum_value_of_x`
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
                                 'for field `maximum_value_of_x`'.format(value))

        self._data["Maximum Value of X"] = value

    @property
    def minimum_value_of_y(self):
        """Get minimum_value_of_y

        Returns:
            float: the value of `minimum_value_of_y` or None if not set
        """
        return self._data["Minimum Value of Y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_y`

        Args:
            value (float): value for IDD Field `minimum_value_of_y`
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
                                 'for field `minimum_value_of_y`'.format(value))

        self._data["Minimum Value of Y"] = value

    @property
    def maximum_value_of_y(self):
        """Get maximum_value_of_y

        Returns:
            float: the value of `maximum_value_of_y` or None if not set
        """
        return self._data["Maximum Value of Y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_y`

        Args:
            value (float): value for IDD Field `maximum_value_of_y`
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
                                 'for field `maximum_value_of_y`'.format(value))

        self._data["Maximum Value of Y"] = value

    @property
    def minimum_table_output(self):
        """Get minimum_table_output

        Returns:
            float: the value of `minimum_table_output` or None if not set
        """
        return self._data["Minimum Table Output"]

    @minimum_table_output.setter
    def minimum_table_output(self, value=None):
        """  Corresponds to IDD Field `minimum_table_output`
        Specify the minimum value calculated by this table lookup object

        Args:
            value (float): value for IDD Field `minimum_table_output`
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
                                 'for field `minimum_table_output`'.format(value))

        self._data["Minimum Table Output"] = value

    @property
    def maximum_table_output(self):
        """Get maximum_table_output

        Returns:
            float: the value of `maximum_table_output` or None if not set
        """
        return self._data["Maximum Table Output"]

    @maximum_table_output.setter
    def maximum_table_output(self, value=None):
        """  Corresponds to IDD Field `maximum_table_output`
        Specify the maximum value calculated by this table lookup object

        Args:
            value (float): value for IDD Field `maximum_table_output`
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
                                 'for field `maximum_table_output`'.format(value))

        self._data["Maximum Table Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x`'.format(value))

        self._data["Input Unit Type for X"] = value

    @property
    def input_unit_type_for_y(self):
        """Get input_unit_type_for_y

        Returns:
            str: the value of `input_unit_type_for_y` or None if not set
        """
        return self._data["Input Unit Type for Y"]

    @input_unit_type_for_y.setter
    def input_unit_type_for_y(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_y`

        Args:
            value (str): value for IDD Field `input_unit_type_for_y`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_y`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_y`'.format(value))

        self._data["Input Unit Type for Y"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `output_unit_type`

        Args:
            value (str): value for IDD Field `output_unit_type`
                Accepted values are:
                      - Dimensionless
                      - Capacity
                      - Power
                Default value: Dimensionless
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
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Capacity")
            vals.add("Power")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `output_unit_type`'.format(value))

        self._data["Output Unit Type"] = value

    @property
    def normalization_reference(self):
        """Get normalization_reference

        Returns:
            float: the value of `normalization_reference` or None if not set
        """
        return self._data["Normalization Reference"]

    @normalization_reference.setter
    def normalization_reference(self, value=None):
        """  Corresponds to IDD Field `normalization_reference`
        This field is used to normalize the following output data.
        The minimum and maximum table output fields are also normalized.
        If this field is blank or 1, the table data presented below will be used.

        Args:
            value (float): value for IDD Field `normalization_reference`
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
                                 'for field `normalization_reference`'.format(value))

        self._data["Normalization Reference"] = value

    @property
    def x_value_1(self):
        """Get x_value_1

        Returns:
            float: the value of `x_value_1` or None if not set
        """
        return self._data["X Value #1"]

    @x_value_1.setter
    def x_value_1(self, value=None):
        """  Corresponds to IDD Field `x_value_1`

        Args:
            value (float): value for IDD Field `x_value_1`
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
                                 'for field `x_value_1`'.format(value))

        self._data["X Value #1"] = value

    @property
    def y_value_1(self):
        """Get y_value_1

        Returns:
            float: the value of `y_value_1` or None if not set
        """
        return self._data["Y Value #1"]

    @y_value_1.setter
    def y_value_1(self, value=None):
        """  Corresponds to IDD Field `y_value_1`

        Args:
            value (float): value for IDD Field `y_value_1`
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
                                 'for field `y_value_1`'.format(value))

        self._data["Y Value #1"] = value

    @property
    def output_value_1(self):
        """Get output_value_1

        Returns:
            float: the value of `output_value_1` or None if not set
        """
        return self._data["Output Value #1"]

    @output_value_1.setter
    def output_value_1(self, value=None):
        """  Corresponds to IDD Field `output_value_1`

        Args:
            value (float): value for IDD Field `output_value_1`
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
                                 'for field `output_value_1`'.format(value))

        self._data["Output Value #1"] = value

    @property
    def x_value_2(self):
        """Get x_value_2

        Returns:
            float: the value of `x_value_2` or None if not set
        """
        return self._data["X Value #2"]

    @x_value_2.setter
    def x_value_2(self, value=None):
        """  Corresponds to IDD Field `x_value_2`

        Args:
            value (float): value for IDD Field `x_value_2`
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
                                 'for field `x_value_2`'.format(value))

        self._data["X Value #2"] = value

    @property
    def y_value_2(self):
        """Get y_value_2

        Returns:
            float: the value of `y_value_2` or None if not set
        """
        return self._data["Y Value #2"]

    @y_value_2.setter
    def y_value_2(self, value=None):
        """  Corresponds to IDD Field `y_value_2`

        Args:
            value (float): value for IDD Field `y_value_2`
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
                                 'for field `y_value_2`'.format(value))

        self._data["Y Value #2"] = value

    @property
    def output_value_2(self):
        """Get output_value_2

        Returns:
            float: the value of `output_value_2` or None if not set
        """
        return self._data["Output Value #2"]

    @output_value_2.setter
    def output_value_2(self, value=None):
        """  Corresponds to IDD Field `output_value_2`

        Args:
            value (float): value for IDD Field `output_value_2`
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
                                 'for field `output_value_2`'.format(value))

        self._data["Output Value #2"] = value

    @property
    def x_value_3(self):
        """Get x_value_3

        Returns:
            float: the value of `x_value_3` or None if not set
        """
        return self._data["X Value #3"]

    @x_value_3.setter
    def x_value_3(self, value=None):
        """  Corresponds to IDD Field `x_value_3`

        Args:
            value (float): value for IDD Field `x_value_3`
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
                                 'for field `x_value_3`'.format(value))

        self._data["X Value #3"] = value

    @property
    def y_value_3(self):
        """Get y_value_3

        Returns:
            float: the value of `y_value_3` or None if not set
        """
        return self._data["Y Value #3"]

    @y_value_3.setter
    def y_value_3(self, value=None):
        """  Corresponds to IDD Field `y_value_3`

        Args:
            value (float): value for IDD Field `y_value_3`
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
                                 'for field `y_value_3`'.format(value))

        self._data["Y Value #3"] = value

    @property
    def output_value_3(self):
        """Get output_value_3

        Returns:
            float: the value of `output_value_3` or None if not set
        """
        return self._data["Output Value #3"]

    @output_value_3.setter
    def output_value_3(self, value=None):
        """  Corresponds to IDD Field `output_value_3`

        Args:
            value (float): value for IDD Field `output_value_3`
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
                                 'for field `output_value_3`'.format(value))

        self._data["Output Value #3"] = value

    @property
    def x_value_4(self):
        """Get x_value_4

        Returns:
            float: the value of `x_value_4` or None if not set
        """
        return self._data["X Value #4"]

    @x_value_4.setter
    def x_value_4(self, value=None):
        """  Corresponds to IDD Field `x_value_4`

        Args:
            value (float): value for IDD Field `x_value_4`
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
                                 'for field `x_value_4`'.format(value))

        self._data["X Value #4"] = value

    @property
    def y_value_4(self):
        """Get y_value_4

        Returns:
            float: the value of `y_value_4` or None if not set
        """
        return self._data["Y Value #4"]

    @y_value_4.setter
    def y_value_4(self, value=None):
        """  Corresponds to IDD Field `y_value_4`

        Args:
            value (float): value for IDD Field `y_value_4`
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
                                 'for field `y_value_4`'.format(value))

        self._data["Y Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

    @property
    def output_value_4(self):
        """Get output_value_4

        Returns:
            float: the value of `output_value_4` or None if not set
        """
        return self._data["Output Value #4"]

    @output_value_4.setter
    def output_value_4(self, value=None):
        """  Corresponds to IDD Field `output_value_4`

        Args:
            value (float): value for IDD Field `output_value_4`
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
                                 'for field `output_value_4`'.format(value))

        self._data["Output Value #4"] = value

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
        out.append(self._to_str(self.curve_type))
        out.append(self._to_str(self.interpolation_method))
        out.append(self._to_str(self.minimum_value_of_x))
        out.append(self._to_str(self.maximum_value_of_x))
        out.append(self._to_str(self.minimum_value_of_y))
        out.append(self._to_str(self.maximum_value_of_y))
        out.append(self._to_str(self.minimum_table_output))
        out.append(self._to_str(self.maximum_table_output))
        out.append(self._to_str(self.input_unit_type_for_x))
        out.append(self._to_str(self.input_unit_type_for_y))
        out.append(self._to_str(self.output_unit_type))
        out.append(self._to_str(self.normalization_reference))
        out.append(self._to_str(self.x_value_1))
        out.append(self._to_str(self.y_value_1))
        out.append(self._to_str(self.output_value_1))
        out.append(self._to_str(self.x_value_2))
        out.append(self._to_str(self.y_value_2))
        out.append(self._to_str(self.output_value_2))
        out.append(self._to_str(self.x_value_3))
        out.append(self._to_str(self.y_value_3))
        out.append(self._to_str(self.output_value_3))
        out.append(self._to_str(self.x_value_4))
        out.append(self._to_str(self.y_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        out.append(self._to_str(self.output_value_4))
        return ",".join(out)

class TableMultiVariableLookup(object):
    """ Corresponds to IDD object `Table:MultiVariableLookup`
        The multi-variable lookup table can represent from 1 to 5 independent variables and
        can interpolate these independent variables up to a 4th order polynomial. The
        polynomial order is assumed to be the number of interpolation points (n) minus 1.
        When any independent variable value is outside the table limits, linear extrapolation
        is used to predict the table result and is based on the two nearest data points in the
        table for that particularindependent variable.
    """
    internal_name = "Table:MultiVariableLookup"
    field_count = 186

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Table:MultiVariableLookup`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Interpolation Method"] = None
        self._data["Number of Interpolation Points"] = None
        self._data["Curve Type"] = None
        self._data["Table Data Format"] = None
        self._data["External File Name"] = None
        self._data["X1 Sort Order"] = None
        self._data["X2 Sort Order"] = None
        self._data["Normalization Reference"] = None
        self._data["Minimum Value of X1"] = None
        self._data["Maximum Value of X1"] = None
        self._data["Minimum Value of X2"] = None
        self._data["Maximum Value of X2"] = None
        self._data["Minimum Value of X3"] = None
        self._data["Maximum Value of X3"] = None
        self._data["Minimum Value of X4"] = None
        self._data["Maximum Value of X4"] = None
        self._data["Minimum Value of X5"] = None
        self._data["Maximum Value of X5"] = None
        self._data["Minimum Table Output"] = None
        self._data["Maximum Table Output"] = None
        self._data["Input Unit Type for X1"] = None
        self._data["Input Unit Type for X2"] = None
        self._data["Input Unit Type for X3"] = None
        self._data["Input Unit Type for X4"] = None
        self._data["Input Unit Type for X5"] = None
        self._data["Output Unit Type"] = None
        self._data["Number of Independent Variables"] = None
        self._data["Number of Values for Independent Variable X1"] = None
        self._data["Field 1 Determined by the Number of Independent Variables"] = None
        self._data["Field 2 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None
        self._data["Field 3 Determined by the Number of Independent Variables"] = None

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
            self.interpolation_method = None
        else:
            self.interpolation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_interpolation_points = None
        else:
            self.number_of_interpolation_points = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.curve_type = None
        else:
            self.curve_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.table_data_format = None
        else:
            self.table_data_format = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.external_file_name = None
        else:
            self.external_file_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x1_sort_order = None
        else:
            self.x1_sort_order = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.x2_sort_order = None
        else:
            self.x2_sort_order = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.normalization_reference = None
        else:
            self.normalization_reference = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x1 = None
        else:
            self.minimum_value_of_x1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x1 = None
        else:
            self.maximum_value_of_x1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x2 = None
        else:
            self.minimum_value_of_x2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x2 = None
        else:
            self.maximum_value_of_x2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x3 = None
        else:
            self.minimum_value_of_x3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x3 = None
        else:
            self.maximum_value_of_x3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x4 = None
        else:
            self.minimum_value_of_x4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x4 = None
        else:
            self.maximum_value_of_x4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_value_of_x5 = None
        else:
            self.minimum_value_of_x5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_value_of_x5 = None
        else:
            self.maximum_value_of_x5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_table_output = None
        else:
            self.minimum_table_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_table_output = None
        else:
            self.maximum_table_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x1 = None
        else:
            self.input_unit_type_for_x1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x2 = None
        else:
            self.input_unit_type_for_x2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x3 = None
        else:
            self.input_unit_type_for_x3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x4 = None
        else:
            self.input_unit_type_for_x4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.input_unit_type_for_x5 = None
        else:
            self.input_unit_type_for_x5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_independent_variables = None
        else:
            self.number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_values_for_independent_variable_x1 = None
        else:
            self.number_of_values_for_independent_variable_x1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_1_determined_by_the_number_of_independent_variables = None
        else:
            self.field_1_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_2_determined_by_the_number_of_independent_variables = None
        else:
            self.field_2_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.field_3_determined_by_the_number_of_independent_variables = None
        else:
            self.field_3_determined_by_the_number_of_independent_variables = vals[i]
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
    def interpolation_method(self):
        """Get interpolation_method

        Returns:
            str: the value of `interpolation_method` or None if not set
        """
        return self._data["Interpolation Method"]

    @interpolation_method.setter
    def interpolation_method(self, value="LagrangeInterpolationLinearExtrapolation"):
        """  Corresponds to IDD Field `interpolation_method`

        Args:
            value (str): value for IDD Field `interpolation_method`
                Accepted values are:
                      - LinearInterpolationOfTable
                      - EvaluateCurveToLimits
                      - LagrangeInterpolationLinearExtrapolation
                Default value: LagrangeInterpolationLinearExtrapolation
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
                                 'for field `interpolation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `interpolation_method`')
            vals = set()
            vals.add("LinearInterpolationOfTable")
            vals.add("EvaluateCurveToLimits")
            vals.add("LagrangeInterpolationLinearExtrapolation")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `interpolation_method`'.format(value))

        self._data["Interpolation Method"] = value

    @property
    def number_of_interpolation_points(self):
        """Get number_of_interpolation_points

        Returns:
            int: the value of `number_of_interpolation_points` or None if not set
        """
        return self._data["Number of Interpolation Points"]

    @number_of_interpolation_points.setter
    def number_of_interpolation_points(self, value=3 ):
        """  Corresponds to IDD Field `number_of_interpolation_points`

        Args:
            value (int): value for IDD Field `number_of_interpolation_points`
                Default value: 3
                value > 1
                value <= 4
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
                                 'for field `number_of_interpolation_points`'.format(value))
            if value <= 1:
                raise ValueError('value need to be greater 1 '
                                 'for field `number_of_interpolation_points`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_interpolation_points`')

        self._data["Number of Interpolation Points"] = value

    @property
    def curve_type(self):
        """Get curve_type

        Returns:
            str: the value of `curve_type` or None if not set
        """
        return self._data["Curve Type"]

    @curve_type.setter
    def curve_type(self, value=None):
        """  Corresponds to IDD Field `curve_type`
        The curve types BiCubic and TriQuadratic may not
        be used with Interpolation Method = EvaluateCurveToLimits

        Args:
            value (str): value for IDD Field `curve_type`
                Accepted values are:
                      - Linear
                      - Quadratic
                      - Cubic
                      - Quartic
                      - Exponent
                      - BiQuadratic
                      - QuadraticLinear
                      - BiCubic
                      - TriQuadratic
                      - Other
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
                                 'for field `curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `curve_type`')
            vals = set()
            vals.add("Linear")
            vals.add("Quadratic")
            vals.add("Cubic")
            vals.add("Quartic")
            vals.add("Exponent")
            vals.add("BiQuadratic")
            vals.add("QuadraticLinear")
            vals.add("BiCubic")
            vals.add("TriQuadratic")
            vals.add("Other")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `curve_type`'.format(value))

        self._data["Curve Type"] = value

    @property
    def table_data_format(self):
        """Get table_data_format

        Returns:
            str: the value of `table_data_format` or None if not set
        """
        return self._data["Table Data Format"]

    @table_data_format.setter
    def table_data_format(self, value="SingleLineIndependentVariableWithMatrix"):
        """  Corresponds to IDD Field `table_data_format`

        Args:
            value (str): value for IDD Field `table_data_format`
                Accepted values are:
                      - SingleLineIndependentVariableWithMatrix
                Default value: SingleLineIndependentVariableWithMatrix
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
                                 'for field `table_data_format`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `table_data_format`')
            vals = set()
            vals.add("SingleLineIndependentVariableWithMatrix")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `table_data_format`'.format(value))

        self._data["Table Data Format"] = value

    @property
    def external_file_name(self):
        """Get external_file_name

        Returns:
            str: the value of `external_file_name` or None if not set
        """
        return self._data["External File Name"]

    @external_file_name.setter
    def external_file_name(self, value=None):
        """  Corresponds to IDD Field `external_file_name`

        Args:
            value (str): value for IDD Field `external_file_name`
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
                                 'for field `external_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `external_file_name`')

        self._data["External File Name"] = value

    @property
    def x1_sort_order(self):
        """Get x1_sort_order

        Returns:
            str: the value of `x1_sort_order` or None if not set
        """
        return self._data["X1 Sort Order"]

    @x1_sort_order.setter
    def x1_sort_order(self, value="Ascending"):
        """  Corresponds to IDD Field `x1_sort_order`

        Args:
            value (str): value for IDD Field `x1_sort_order`
                Accepted values are:
                      - Ascending
                      - Descending
                Default value: Ascending
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
                                 'for field `x1_sort_order`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `x1_sort_order`')
            vals = set()
            vals.add("Ascending")
            vals.add("Descending")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `x1_sort_order`'.format(value))

        self._data["X1 Sort Order"] = value

    @property
    def x2_sort_order(self):
        """Get x2_sort_order

        Returns:
            str: the value of `x2_sort_order` or None if not set
        """
        return self._data["X2 Sort Order"]

    @x2_sort_order.setter
    def x2_sort_order(self, value="Ascending"):
        """  Corresponds to IDD Field `x2_sort_order`

        Args:
            value (str): value for IDD Field `x2_sort_order`
                Accepted values are:
                      - Ascending
                      - Descending
                Default value: Ascending
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
                                 'for field `x2_sort_order`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `x2_sort_order`')
            vals = set()
            vals.add("Ascending")
            vals.add("Descending")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `x2_sort_order`'.format(value))

        self._data["X2 Sort Order"] = value

    @property
    def normalization_reference(self):
        """Get normalization_reference

        Returns:
            float: the value of `normalization_reference` or None if not set
        """
        return self._data["Normalization Reference"]

    @normalization_reference.setter
    def normalization_reference(self, value=None):
        """  Corresponds to IDD Field `normalization_reference`
        This field is used to normalize the table output data.
        The minimum and maximum table output fields are also normalized.
        If this field is blank or 1, the table data will be directly used.
        This field is not allowed to be set equal to 0.

        Args:
            value (float): value for IDD Field `normalization_reference`
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
                                 'for field `normalization_reference`'.format(value))

        self._data["Normalization Reference"] = value

    @property
    def minimum_value_of_x1(self):
        """Get minimum_value_of_x1

        Returns:
            float: the value of `minimum_value_of_x1` or None if not set
        """
        return self._data["Minimum Value of X1"]

    @minimum_value_of_x1.setter
    def minimum_value_of_x1(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x1`

        Args:
            value (float): value for IDD Field `minimum_value_of_x1`
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
                                 'for field `minimum_value_of_x1`'.format(value))

        self._data["Minimum Value of X1"] = value

    @property
    def maximum_value_of_x1(self):
        """Get maximum_value_of_x1

        Returns:
            float: the value of `maximum_value_of_x1` or None if not set
        """
        return self._data["Maximum Value of X1"]

    @maximum_value_of_x1.setter
    def maximum_value_of_x1(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x1`

        Args:
            value (float): value for IDD Field `maximum_value_of_x1`
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
                                 'for field `maximum_value_of_x1`'.format(value))

        self._data["Maximum Value of X1"] = value

    @property
    def minimum_value_of_x2(self):
        """Get minimum_value_of_x2

        Returns:
            float: the value of `minimum_value_of_x2` or None if not set
        """
        return self._data["Minimum Value of X2"]

    @minimum_value_of_x2.setter
    def minimum_value_of_x2(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x2`

        Args:
            value (float): value for IDD Field `minimum_value_of_x2`
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
                                 'for field `minimum_value_of_x2`'.format(value))

        self._data["Minimum Value of X2"] = value

    @property
    def maximum_value_of_x2(self):
        """Get maximum_value_of_x2

        Returns:
            float: the value of `maximum_value_of_x2` or None if not set
        """
        return self._data["Maximum Value of X2"]

    @maximum_value_of_x2.setter
    def maximum_value_of_x2(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x2`

        Args:
            value (float): value for IDD Field `maximum_value_of_x2`
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
                                 'for field `maximum_value_of_x2`'.format(value))

        self._data["Maximum Value of X2"] = value

    @property
    def minimum_value_of_x3(self):
        """Get minimum_value_of_x3

        Returns:
            float: the value of `minimum_value_of_x3` or None if not set
        """
        return self._data["Minimum Value of X3"]

    @minimum_value_of_x3.setter
    def minimum_value_of_x3(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x3`

        Args:
            value (float): value for IDD Field `minimum_value_of_x3`
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
                                 'for field `minimum_value_of_x3`'.format(value))

        self._data["Minimum Value of X3"] = value

    @property
    def maximum_value_of_x3(self):
        """Get maximum_value_of_x3

        Returns:
            float: the value of `maximum_value_of_x3` or None if not set
        """
        return self._data["Maximum Value of X3"]

    @maximum_value_of_x3.setter
    def maximum_value_of_x3(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x3`

        Args:
            value (float): value for IDD Field `maximum_value_of_x3`
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
                                 'for field `maximum_value_of_x3`'.format(value))

        self._data["Maximum Value of X3"] = value

    @property
    def minimum_value_of_x4(self):
        """Get minimum_value_of_x4

        Returns:
            float: the value of `minimum_value_of_x4` or None if not set
        """
        return self._data["Minimum Value of X4"]

    @minimum_value_of_x4.setter
    def minimum_value_of_x4(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x4`

        Args:
            value (float): value for IDD Field `minimum_value_of_x4`
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
                                 'for field `minimum_value_of_x4`'.format(value))

        self._data["Minimum Value of X4"] = value

    @property
    def maximum_value_of_x4(self):
        """Get maximum_value_of_x4

        Returns:
            float: the value of `maximum_value_of_x4` or None if not set
        """
        return self._data["Maximum Value of X4"]

    @maximum_value_of_x4.setter
    def maximum_value_of_x4(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x4`

        Args:
            value (float): value for IDD Field `maximum_value_of_x4`
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
                                 'for field `maximum_value_of_x4`'.format(value))

        self._data["Maximum Value of X4"] = value

    @property
    def minimum_value_of_x5(self):
        """Get minimum_value_of_x5

        Returns:
            float: the value of `minimum_value_of_x5` or None if not set
        """
        return self._data["Minimum Value of X5"]

    @minimum_value_of_x5.setter
    def minimum_value_of_x5(self, value=None):
        """  Corresponds to IDD Field `minimum_value_of_x5`

        Args:
            value (float): value for IDD Field `minimum_value_of_x5`
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
                                 'for field `minimum_value_of_x5`'.format(value))

        self._data["Minimum Value of X5"] = value

    @property
    def maximum_value_of_x5(self):
        """Get maximum_value_of_x5

        Returns:
            float: the value of `maximum_value_of_x5` or None if not set
        """
        return self._data["Maximum Value of X5"]

    @maximum_value_of_x5.setter
    def maximum_value_of_x5(self, value=None):
        """  Corresponds to IDD Field `maximum_value_of_x5`

        Args:
            value (float): value for IDD Field `maximum_value_of_x5`
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
                                 'for field `maximum_value_of_x5`'.format(value))

        self._data["Maximum Value of X5"] = value

    @property
    def minimum_table_output(self):
        """Get minimum_table_output

        Returns:
            float: the value of `minimum_table_output` or None if not set
        """
        return self._data["Minimum Table Output"]

    @minimum_table_output.setter
    def minimum_table_output(self, value=None):
        """  Corresponds to IDD Field `minimum_table_output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `minimum_table_output`
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
                                 'for field `minimum_table_output`'.format(value))

        self._data["Minimum Table Output"] = value

    @property
    def maximum_table_output(self):
        """Get maximum_table_output

        Returns:
            float: the value of `maximum_table_output` or None if not set
        """
        return self._data["Maximum Table Output"]

    @maximum_table_output.setter
    def maximum_table_output(self, value=None):
        """  Corresponds to IDD Field `maximum_table_output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `maximum_table_output`
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
                                 'for field `maximum_table_output`'.format(value))

        self._data["Maximum Table Output"] = value

    @property
    def input_unit_type_for_x1(self):
        """Get input_unit_type_for_x1

        Returns:
            str: the value of `input_unit_type_for_x1` or None if not set
        """
        return self._data["Input Unit Type for X1"]

    @input_unit_type_for_x1.setter
    def input_unit_type_for_x1(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x1`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x1`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x1`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x1`'.format(value))

        self._data["Input Unit Type for X1"] = value

    @property
    def input_unit_type_for_x2(self):
        """Get input_unit_type_for_x2

        Returns:
            str: the value of `input_unit_type_for_x2` or None if not set
        """
        return self._data["Input Unit Type for X2"]

    @input_unit_type_for_x2.setter
    def input_unit_type_for_x2(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x2`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x2`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x2`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x2`'.format(value))

        self._data["Input Unit Type for X2"] = value

    @property
    def input_unit_type_for_x3(self):
        """Get input_unit_type_for_x3

        Returns:
            str: the value of `input_unit_type_for_x3` or None if not set
        """
        return self._data["Input Unit Type for X3"]

    @input_unit_type_for_x3.setter
    def input_unit_type_for_x3(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x3`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x3`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x3`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x3`'.format(value))

        self._data["Input Unit Type for X3"] = value

    @property
    def input_unit_type_for_x4(self):
        """Get input_unit_type_for_x4

        Returns:
            str: the value of `input_unit_type_for_x4` or None if not set
        """
        return self._data["Input Unit Type for X4"]

    @input_unit_type_for_x4.setter
    def input_unit_type_for_x4(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x4`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x4`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x4`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x4`'.format(value))

        self._data["Input Unit Type for X4"] = value

    @property
    def input_unit_type_for_x5(self):
        """Get input_unit_type_for_x5

        Returns:
            str: the value of `input_unit_type_for_x5` or None if not set
        """
        return self._data["Input Unit Type for X5"]

    @input_unit_type_for_x5.setter
    def input_unit_type_for_x5(self, value="Dimensionless"):
        """  Corresponds to IDD Field `input_unit_type_for_x5`

        Args:
            value (str): value for IDD Field `input_unit_type_for_x5`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                Default value: Dimensionless
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
                                 'for field `input_unit_type_for_x5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x5`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Temperature")
            vals.add("VolumetricFlow")
            vals.add("MassFlow")
            vals.add("Power")
            vals.add("Distance")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `input_unit_type_for_x5`'.format(value))

        self._data["Input Unit Type for X5"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `output_unit_type`

        Args:
            value (str): value for IDD Field `output_unit_type`
                Accepted values are:
                      - Dimensionless
                      - Capacity
                      - Power
                Default value: Dimensionless
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
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            vals = set()
            vals.add("Dimensionless")
            vals.add("Capacity")
            vals.add("Power")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `output_unit_type`'.format(value))

        self._data["Output Unit Type"] = value

    @property
    def number_of_independent_variables(self):
        """Get number_of_independent_variables

        Returns:
            int: the value of `number_of_independent_variables` or None if not set
        """
        return self._data["Number of Independent Variables"]

    @number_of_independent_variables.setter
    def number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `number_of_independent_variables`

        Args:
            value (int): value for IDD Field `number_of_independent_variables`
                value > 0
                value <= 5
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
                                 'for field `number_of_independent_variables`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `number_of_independent_variables`')
            if value > 5:
                raise ValueError('value need to be smaller 5 '
                                 'for field `number_of_independent_variables`')

        self._data["Number of Independent Variables"] = value

    @property
    def number_of_values_for_independent_variable_x1(self):
        """Get number_of_values_for_independent_variable_x1

        Returns:
            int: the value of `number_of_values_for_independent_variable_x1` or None if not set
        """
        return self._data["Number of Values for Independent Variable X1"]

    @number_of_values_for_independent_variable_x1.setter
    def number_of_values_for_independent_variable_x1(self, value=None):
        """  Corresponds to IDD Field `number_of_values_for_independent_variable_x1`

        Args:
            value (int): value for IDD Field `number_of_values_for_independent_variable_x1`
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
                                 'for field `number_of_values_for_independent_variable_x1`'.format(value))

        self._data["Number of Values for Independent Variable X1"] = value

    @property
    def field_1_determined_by_the_number_of_independent_variables(self):
        """Get field_1_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_1_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 1 Determined by the Number of Independent Variables"]

    @field_1_determined_by_the_number_of_independent_variables.setter
    def field_1_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_1_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_1_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_1_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 1 Determined by the Number of Independent Variables"] = value

    @property
    def field_2_determined_by_the_number_of_independent_variables(self):
        """Get field_2_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_2_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 2 Determined by the Number of Independent Variables"]

    @field_2_determined_by_the_number_of_independent_variables.setter
    def field_2_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_2_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_2_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_2_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 2 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

    @property
    def field_3_determined_by_the_number_of_independent_variables(self):
        """Get field_3_determined_by_the_number_of_independent_variables

        Returns:
            float: the value of `field_3_determined_by_the_number_of_independent_variables` or None if not set
        """
        return self._data["Field 3 Determined by the Number of Independent Variables"]

    @field_3_determined_by_the_number_of_independent_variables.setter
    def field_3_determined_by_the_number_of_independent_variables(self, value=None):
        """  Corresponds to IDD Field `field_3_determined_by_the_number_of_independent_variables`

        Args:
            value (float): value for IDD Field `field_3_determined_by_the_number_of_independent_variables`
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
                                 'for field `field_3_determined_by_the_number_of_independent_variables`'.format(value))

        self._data["Field 3 Determined by the Number of Independent Variables"] = value

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
        out.append(self._to_str(self.interpolation_method))
        out.append(self._to_str(self.number_of_interpolation_points))
        out.append(self._to_str(self.curve_type))
        out.append(self._to_str(self.table_data_format))
        out.append(self._to_str(self.external_file_name))
        out.append(self._to_str(self.x1_sort_order))
        out.append(self._to_str(self.x2_sort_order))
        out.append(self._to_str(self.normalization_reference))
        out.append(self._to_str(self.minimum_value_of_x1))
        out.append(self._to_str(self.maximum_value_of_x1))
        out.append(self._to_str(self.minimum_value_of_x2))
        out.append(self._to_str(self.maximum_value_of_x2))
        out.append(self._to_str(self.minimum_value_of_x3))
        out.append(self._to_str(self.maximum_value_of_x3))
        out.append(self._to_str(self.minimum_value_of_x4))
        out.append(self._to_str(self.maximum_value_of_x4))
        out.append(self._to_str(self.minimum_value_of_x5))
        out.append(self._to_str(self.maximum_value_of_x5))
        out.append(self._to_str(self.minimum_table_output))
        out.append(self._to_str(self.maximum_table_output))
        out.append(self._to_str(self.input_unit_type_for_x1))
        out.append(self._to_str(self.input_unit_type_for_x2))
        out.append(self._to_str(self.input_unit_type_for_x3))
        out.append(self._to_str(self.input_unit_type_for_x4))
        out.append(self._to_str(self.input_unit_type_for_x5))
        out.append(self._to_str(self.output_unit_type))
        out.append(self._to_str(self.number_of_independent_variables))
        out.append(self._to_str(self.number_of_values_for_independent_variable_x1))
        out.append(self._to_str(self.field_1_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_2_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        out.append(self._to_str(self.field_3_determined_by_the_number_of_independent_variables))
        return ",".join(out)