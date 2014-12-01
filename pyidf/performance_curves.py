from collections import OrderedDict

class CurveLinear(object):
    """ Corresponds to IDD object `Curve:Linear`
        Linear curve with one independent variable.
        Input for the linear curve consists of a curve name, the two coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for
        curve minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x
    
    """
    internal_name = "Curve:Linear"
    field_count = 9
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Linear`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - Pressure
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["pressure"] = "Pressure"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveQuadLinear(object):
    """ Corresponds to IDD object `Curve:QuadLinear`
        Linear curve with four independent variables.
        Input for the linear curve consists of a curve name, the two coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*w + C3*x + C4*y + C5*z
    
    """
    internal_name = "Curve:QuadLinear"
    field_count = 20
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 w", "Coefficient3 x", "Coefficient4 y", "Coefficient5 z", "Minimum Value of w", "Maximum Value of w", "Minimum Value of x", "Maximum Value of x", "Minimum Value of y", "Maximum Value of y", "Minimum Value of z", "Maximum Value of z"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:QuadLinear`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 w"] = None
        self._data["Coefficient3 x"] = None
        self._data["Coefficient4 y"] = None
        self._data["Coefficient5 z"] = None
        self._data["Minimum Value of w"] = None
        self._data["Maximum Value of w"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Value of y"] = None
        self._data["Maximum Value of y"] = None
        self._data["Minimum Value of z"] = None
        self._data["Maximum Value of z"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for w"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Input Unit Type for y"] = None
        self._data["Input Unit Type for z"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_w = None
        else:
            self.coefficient2_w = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x = None
        else:
            self.coefficient3_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_y = None
        else:
            self.coefficient4_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_z = None
        else:
            self.coefficient5_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_w = None
        else:
            self.minimum_value_of_w = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_w = None
        else:
            self.maximum_value_of_w = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_y = None
        else:
            self.minimum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_y = None
        else:
            self.maximum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_z = None
        else:
            self.minimum_value_of_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_z = None
        else:
            self.maximum_value_of_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_w = None
        else:
            self.input_unit_type_for_w = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_y = None
        else:
            self.input_unit_type_for_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_z = None
        else:
            self.input_unit_type_for_z = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_w(self):
        """Get coefficient2_w

        Returns:
            float: the value of `coefficient2_w` or None if not set
        """
        return self._data["Coefficient2 w"]

    @coefficient2_w.setter
    def coefficient2_w(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 w`

        Args:
            value (float): value for IDD Field `Coefficient2 w`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_w`'.format(value))
        self._data["Coefficient2 w"] = value

    @property
    def coefficient3_x(self):
        """Get coefficient3_x

        Returns:
            float: the value of `coefficient3_x` or None if not set
        """
        return self._data["Coefficient3 x"]

    @coefficient3_x.setter
    def coefficient3_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x`

        Args:
            value (float): value for IDD Field `Coefficient3 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x`'.format(value))
        self._data["Coefficient3 x"] = value

    @property
    def coefficient4_y(self):
        """Get coefficient4_y

        Returns:
            float: the value of `coefficient4_y` or None if not set
        """
        return self._data["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_y`'.format(value))
        self._data["Coefficient4 y"] = value

    @property
    def coefficient5_z(self):
        """Get coefficient5_z

        Returns:
            float: the value of `coefficient5_z` or None if not set
        """
        return self._data["Coefficient5 z"]

    @coefficient5_z.setter
    def coefficient5_z(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 z`

        Args:
            value (float): value for IDD Field `Coefficient5 z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_z`'.format(value))
        self._data["Coefficient5 z"] = value

    @property
    def minimum_value_of_w(self):
        """Get minimum_value_of_w

        Returns:
            float: the value of `minimum_value_of_w` or None if not set
        """
        return self._data["Minimum Value of w"]

    @minimum_value_of_w.setter
    def minimum_value_of_w(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of w`

        Args:
            value (float): value for IDD Field `Minimum Value of w`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_w`'.format(value))
        self._data["Minimum Value of w"] = value

    @property
    def maximum_value_of_w(self):
        """Get maximum_value_of_w

        Returns:
            float: the value of `maximum_value_of_w` or None if not set
        """
        return self._data["Maximum Value of w"]

    @maximum_value_of_w.setter
    def maximum_value_of_w(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of w`

        Args:
            value (float): value for IDD Field `Maximum Value of w`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_w`'.format(value))
        self._data["Maximum Value of w"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """Get minimum_value_of_y

        Returns:
            float: the value of `minimum_value_of_y` or None if not set
        """
        return self._data["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of y`

        Args:
            value (float): value for IDD Field `Minimum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_y`'.format(value))
        self._data["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """Get maximum_value_of_y

        Returns:
            float: the value of `maximum_value_of_y` or None if not set
        """
        return self._data["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of y`

        Args:
            value (float): value for IDD Field `Maximum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_y`'.format(value))
        self._data["Maximum Value of y"] = value

    @property
    def minimum_value_of_z(self):
        """Get minimum_value_of_z

        Returns:
            float: the value of `minimum_value_of_z` or None if not set
        """
        return self._data["Minimum Value of z"]

    @minimum_value_of_z.setter
    def minimum_value_of_z(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of z`

        Args:
            value (float): value for IDD Field `Minimum Value of z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_z`'.format(value))
        self._data["Minimum Value of z"] = value

    @property
    def maximum_value_of_z(self):
        """Get maximum_value_of_z

        Returns:
            float: the value of `maximum_value_of_z` or None if not set
        """
        return self._data["Maximum Value of z"]

    @maximum_value_of_z.setter
    def maximum_value_of_z(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of z`

        Args:
            value (float): value for IDD Field `Maximum Value of z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_z`'.format(value))
        self._data["Maximum Value of z"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_w(self):
        """Get input_unit_type_for_w

        Returns:
            str: the value of `input_unit_type_for_w` or None if not set
        """
        return self._data["Input Unit Type for w"]

    @input_unit_type_for_w.setter
    def input_unit_type_for_w(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for w`

        Args:
            value (str): value for IDD Field `Input Unit Type for w`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                      - VolumetricFlowPerPower
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_w`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_w`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_w`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            vals["volumetricflowperpower"] = "VolumetricFlowPerPower"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_w`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for w"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                      - VolumetricFlowPerPower
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            vals["volumetricflowperpower"] = "VolumetricFlowPerPower"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def input_unit_type_for_y(self):
        """Get input_unit_type_for_y

        Returns:
            str: the value of `input_unit_type_for_y` or None if not set
        """
        return self._data["Input Unit Type for y"]

    @input_unit_type_for_y.setter
    def input_unit_type_for_y(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for y`

        Args:
            value (str): value for IDD Field `Input Unit Type for y`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                      - VolumetricFlowPerPower
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_y`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_y`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            vals["volumetricflowperpower"] = "VolumetricFlowPerPower"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_y`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for y"] = value

    @property
    def input_unit_type_for_z(self):
        """Get input_unit_type_for_z

        Returns:
            str: the value of `input_unit_type_for_z` or None if not set
        """
        return self._data["Input Unit Type for z"]

    @input_unit_type_for_z.setter
    def input_unit_type_for_z(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for z`

        Args:
            value (str): value for IDD Field `Input Unit Type for z`
                Accepted values are:
                      - Dimensionless
                      - Temperature
                      - VolumetricFlow
                      - MassFlow
                      - Power
                      - Distance
                      - VolumetricFlowPerPower
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_z`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_z`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_z`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            vals["volumetricflowperpower"] = "VolumetricFlowPerPower"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_z`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for z"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveQuadratic(object):
    """ Corresponds to IDD object `Curve:Quadratic`
        Quadratic curve with one independent variable.
        Input for a quadratic curve consists of the curve name, the three coefficients, and
        the maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2
    
    """
    internal_name = "Curve:Quadratic"
    field_count = 10
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Coefficient3 x**2", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Quadratic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Coefficient3 x**2"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x2 = None
        else:
            self.coefficient3_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """Get coefficient3_x2

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self._data["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x**2`

        Args:
            value (float): value for IDD Field `Coefficient3 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x2`'.format(value))
        self._data["Coefficient3 x**2"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveCubic(object):
    """ Corresponds to IDD object `Curve:Cubic`
        Cubic curve with one independent variable.
        Input for a cubic curve consists of the curve name, the 4 coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*x**3
    
    """
    internal_name = "Curve:Cubic"
    field_count = 11
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Coefficient3 x**2", "Coefficient4 x**3", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Cubic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Coefficient3 x**2"] = None
        self._data["Coefficient4 x**3"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x2 = None
        else:
            self.coefficient3_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_x3 = None
        else:
            self.coefficient4_x3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """Get coefficient3_x2

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self._data["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x**2`

        Args:
            value (float): value for IDD Field `Coefficient3 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x2`'.format(value))
        self._data["Coefficient3 x**2"] = value

    @property
    def coefficient4_x3(self):
        """Get coefficient4_x3

        Returns:
            float: the value of `coefficient4_x3` or None if not set
        """
        return self._data["Coefficient4 x**3"]

    @coefficient4_x3.setter
    def coefficient4_x3(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 x**3`

        Args:
            value (float): value for IDD Field `Coefficient4 x**3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_x3`'.format(value))
        self._data["Coefficient4 x**3"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveQuartic(object):
    """ Corresponds to IDD object `Curve:Quartic`
        Quartic (fourth order polynomial) curve with one independent variable.
        Input for a Quartic curve consists of the curve name, the
        five coefficients, and the maximum and minimum valid independent variable values.
        Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*x**3 + C5*x**4
    
    """
    internal_name = "Curve:Quartic"
    field_count = 12
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Coefficient3 x**2", "Coefficient4 x**3", "Coefficient5 x**4", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Quartic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Coefficient3 x**2"] = None
        self._data["Coefficient4 x**3"] = None
        self._data["Coefficient5 x**4"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x2 = None
        else:
            self.coefficient3_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_x3 = None
        else:
            self.coefficient4_x3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_x4 = None
        else:
            self.coefficient5_x4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """Get coefficient3_x2

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self._data["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x**2`

        Args:
            value (float): value for IDD Field `Coefficient3 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x2`'.format(value))
        self._data["Coefficient3 x**2"] = value

    @property
    def coefficient4_x3(self):
        """Get coefficient4_x3

        Returns:
            float: the value of `coefficient4_x3` or None if not set
        """
        return self._data["Coefficient4 x**3"]

    @coefficient4_x3.setter
    def coefficient4_x3(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 x**3`

        Args:
            value (float): value for IDD Field `Coefficient4 x**3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_x3`'.format(value))
        self._data["Coefficient4 x**3"] = value

    @property
    def coefficient5_x4(self):
        """Get coefficient5_x4

        Returns:
            float: the value of `coefficient5_x4` or None if not set
        """
        return self._data["Coefficient5 x**4"]

    @coefficient5_x4.setter
    def coefficient5_x4(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 x**4`

        Args:
            value (float): value for IDD Field `Coefficient5 x**4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_x4`'.format(value))
        self._data["Coefficient5 x**4"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveExponent(object):
    """ Corresponds to IDD object `Curve:Exponent`
        Exponent curve with one independent variable.
        Input for a exponent curve consists of the curve name, the 3 coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x**C3
        The independent variable x is raised to the C3 power, multiplied by C2, and C1 is added to the result.
    
    """
    internal_name = "Curve:Exponent"
    field_count = 10
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 Constant", "Coefficient3 Constant", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Exponent`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 Constant"] = None
        self._data["Coefficient3 Constant"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_constant = None
        else:
            self.coefficient2_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_constant = None
        else:
            self.coefficient3_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_constant(self):
        """Get coefficient2_constant

        Returns:
            float: the value of `coefficient2_constant` or None if not set
        """
        return self._data["Coefficient2 Constant"]

    @coefficient2_constant.setter
    def coefficient2_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 Constant`

        Args:
            value (float): value for IDD Field `Coefficient2 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_constant`'.format(value))
        self._data["Coefficient2 Constant"] = value

    @property
    def coefficient3_constant(self):
        """Get coefficient3_constant

        Returns:
            float: the value of `coefficient3_constant` or None if not set
        """
        return self._data["Coefficient3 Constant"]

    @coefficient3_constant.setter
    def coefficient3_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 Constant`

        Args:
            value (float): value for IDD Field `Coefficient3 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_constant`'.format(value))
        self._data["Coefficient3 Constant"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`
        Specify the minimum value of the independent variable x allowed

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`
        Specify the maximum value of the independent variable x allowed

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveBicubic(object):
    """ Corresponds to IDD object `Curve:Bicubic`
        Cubic curve with two independent variables. Input consists of the
        curve name, the ten coefficients, and the minimum and maximum values for each of
        the independent variables. Optional inputs for curve minimum and maximum may
        be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3 + C8*y**3 + C9*x**2*y
        + C10*x*y**2
    
    """
    internal_name = "Curve:Bicubic"
    field_count = 20
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Coefficient3 x**2", "Coefficient4 y", "Coefficient5 y**2", "Coefficient6 x*y", "Coefficient7 x**3", "Coefficient8 y**3", "Coefficient9 x**2*y", "Coefficient10 x*y**2", "Minimum Value of x", "Maximum Value of x", "Minimum Value of y", "Maximum Value of y"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Bicubic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Coefficient3 x**2"] = None
        self._data["Coefficient4 y"] = None
        self._data["Coefficient5 y**2"] = None
        self._data["Coefficient6 x*y"] = None
        self._data["Coefficient7 x**3"] = None
        self._data["Coefficient8 y**3"] = None
        self._data["Coefficient9 x**2*y"] = None
        self._data["Coefficient10 x*y**2"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Value of y"] = None
        self._data["Maximum Value of y"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Input Unit Type for Y"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x2 = None
        else:
            self.coefficient3_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_y = None
        else:
            self.coefficient4_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_y2 = None
        else:
            self.coefficient5_y2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient6_xy = None
        else:
            self.coefficient6_xy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient7_x3 = None
        else:
            self.coefficient7_x3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient8_y3 = None
        else:
            self.coefficient8_y3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient9_x2y = None
        else:
            self.coefficient9_x2y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient10_xy2 = None
        else:
            self.coefficient10_xy2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_y = None
        else:
            self.minimum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_y = None
        else:
            self.maximum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_y = None
        else:
            self.input_unit_type_for_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """Get coefficient3_x2

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self._data["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x**2`

        Args:
            value (float): value for IDD Field `Coefficient3 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x2`'.format(value))
        self._data["Coefficient3 x**2"] = value

    @property
    def coefficient4_y(self):
        """Get coefficient4_y

        Returns:
            float: the value of `coefficient4_y` or None if not set
        """
        return self._data["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_y`'.format(value))
        self._data["Coefficient4 y"] = value

    @property
    def coefficient5_y2(self):
        """Get coefficient5_y2

        Returns:
            float: the value of `coefficient5_y2` or None if not set
        """
        return self._data["Coefficient5 y**2"]

    @coefficient5_y2.setter
    def coefficient5_y2(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 y**2`

        Args:
            value (float): value for IDD Field `Coefficient5 y**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_y2`'.format(value))
        self._data["Coefficient5 y**2"] = value

    @property
    def coefficient6_xy(self):
        """Get coefficient6_xy

        Returns:
            float: the value of `coefficient6_xy` or None if not set
        """
        return self._data["Coefficient6 x*y"]

    @coefficient6_xy.setter
    def coefficient6_xy(self, value=None):
        """  Corresponds to IDD Field `Coefficient6 x*y`

        Args:
            value (float): value for IDD Field `Coefficient6 x*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient6_xy`'.format(value))
        self._data["Coefficient6 x*y"] = value

    @property
    def coefficient7_x3(self):
        """Get coefficient7_x3

        Returns:
            float: the value of `coefficient7_x3` or None if not set
        """
        return self._data["Coefficient7 x**3"]

    @coefficient7_x3.setter
    def coefficient7_x3(self, value=None):
        """  Corresponds to IDD Field `Coefficient7 x**3`

        Args:
            value (float): value for IDD Field `Coefficient7 x**3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient7_x3`'.format(value))
        self._data["Coefficient7 x**3"] = value

    @property
    def coefficient8_y3(self):
        """Get coefficient8_y3

        Returns:
            float: the value of `coefficient8_y3` or None if not set
        """
        return self._data["Coefficient8 y**3"]

    @coefficient8_y3.setter
    def coefficient8_y3(self, value=None):
        """  Corresponds to IDD Field `Coefficient8 y**3`

        Args:
            value (float): value for IDD Field `Coefficient8 y**3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient8_y3`'.format(value))
        self._data["Coefficient8 y**3"] = value

    @property
    def coefficient9_x2y(self):
        """Get coefficient9_x2y

        Returns:
            float: the value of `coefficient9_x2y` or None if not set
        """
        return self._data["Coefficient9 x**2*y"]

    @coefficient9_x2y.setter
    def coefficient9_x2y(self, value=None):
        """  Corresponds to IDD Field `Coefficient9 x**2*y`

        Args:
            value (float): value for IDD Field `Coefficient9 x**2*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient9_x2y`'.format(value))
        self._data["Coefficient9 x**2*y"] = value

    @property
    def coefficient10_xy2(self):
        """Get coefficient10_xy2

        Returns:
            float: the value of `coefficient10_xy2` or None if not set
        """
        return self._data["Coefficient10 x*y**2"]

    @coefficient10_xy2.setter
    def coefficient10_xy2(self, value=None):
        """  Corresponds to IDD Field `Coefficient10 x*y**2`

        Args:
            value (float): value for IDD Field `Coefficient10 x*y**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient10_xy2`'.format(value))
        self._data["Coefficient10 x*y**2"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """Get minimum_value_of_y

        Returns:
            float: the value of `minimum_value_of_y` or None if not set
        """
        return self._data["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of y`

        Args:
            value (float): value for IDD Field `Minimum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_y`'.format(value))
        self._data["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """Get maximum_value_of_y

        Returns:
            float: the value of `maximum_value_of_y` or None if not set
        """
        return self._data["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of y`

        Args:
            value (float): value for IDD Field `Maximum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_y`'.format(value))
        self._data["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for Y`

        Args:
            value (str): value for IDD Field `Input Unit Type for Y`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_y`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_y`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_y`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveBiquadratic(object):
    """ Corresponds to IDD object `Curve:Biquadratic`
        Quadratic curve with two independent variables. Input consists of the curve name, the
        six coefficients, and min and max values for each of the independent variables.
        Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y
    
    """
    internal_name = "Curve:Biquadratic"
    field_count = 16
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Coefficient3 x**2", "Coefficient4 y", "Coefficient5 y**2", "Coefficient6 x*y", "Minimum Value of x", "Maximum Value of x", "Minimum Value of y", "Maximum Value of y"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Biquadratic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Coefficient3 x**2"] = None
        self._data["Coefficient4 y"] = None
        self._data["Coefficient5 y**2"] = None
        self._data["Coefficient6 x*y"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Value of y"] = None
        self._data["Maximum Value of y"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Input Unit Type for Y"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x2 = None
        else:
            self.coefficient3_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_y = None
        else:
            self.coefficient4_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_y2 = None
        else:
            self.coefficient5_y2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient6_xy = None
        else:
            self.coefficient6_xy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_y = None
        else:
            self.minimum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_y = None
        else:
            self.maximum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_y = None
        else:
            self.input_unit_type_for_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """Get coefficient3_x2

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self._data["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x**2`

        Args:
            value (float): value for IDD Field `Coefficient3 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x2`'.format(value))
        self._data["Coefficient3 x**2"] = value

    @property
    def coefficient4_y(self):
        """Get coefficient4_y

        Returns:
            float: the value of `coefficient4_y` or None if not set
        """
        return self._data["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_y`'.format(value))
        self._data["Coefficient4 y"] = value

    @property
    def coefficient5_y2(self):
        """Get coefficient5_y2

        Returns:
            float: the value of `coefficient5_y2` or None if not set
        """
        return self._data["Coefficient5 y**2"]

    @coefficient5_y2.setter
    def coefficient5_y2(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 y**2`

        Args:
            value (float): value for IDD Field `Coefficient5 y**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_y2`'.format(value))
        self._data["Coefficient5 y**2"] = value

    @property
    def coefficient6_xy(self):
        """Get coefficient6_xy

        Returns:
            float: the value of `coefficient6_xy` or None if not set
        """
        return self._data["Coefficient6 x*y"]

    @coefficient6_xy.setter
    def coefficient6_xy(self, value=None):
        """  Corresponds to IDD Field `Coefficient6 x*y`

        Args:
            value (float): value for IDD Field `Coefficient6 x*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient6_xy`'.format(value))
        self._data["Coefficient6 x*y"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """Get minimum_value_of_y

        Returns:
            float: the value of `minimum_value_of_y` or None if not set
        """
        return self._data["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of y`

        Args:
            value (float): value for IDD Field `Minimum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_y`'.format(value))
        self._data["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """Get maximum_value_of_y

        Returns:
            float: the value of `maximum_value_of_y` or None if not set
        """
        return self._data["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of y`

        Args:
            value (float): value for IDD Field `Maximum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_y`'.format(value))
        self._data["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for Y`

        Args:
            value (str): value for IDD Field `Input Unit Type for Y`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_y`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_y`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_y`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveQuadraticLinear(object):
    """ Corresponds to IDD object `Curve:QuadraticLinear`
        Quadratic-linear curve with two independent variables. Input consists of the curve
        name, the six coefficients, and min and max values for each of the independent
        variables. Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = (C1 + C2*x + C3*x**2) + (C4 + C5*x + C6*x**2)*y
    
    """
    internal_name = "Curve:QuadraticLinear"
    field_count = 16
    required_fields = ["Name", "Coefficient1 Constant", "Coefficient2 x", "Coefficient3 x**2", "Coefficient4 y", "Coefficient5 x*y", "Coefficient6 x**2*y", "Minimum Value of x", "Maximum Value of x", "Minimum Value of y", "Maximum Value of y"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:QuadraticLinear`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x"] = None
        self._data["Coefficient3 x**2"] = None
        self._data["Coefficient4 y"] = None
        self._data["Coefficient5 x*y"] = None
        self._data["Coefficient6 x**2*y"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Value of y"] = None
        self._data["Maximum Value of y"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Input Unit Type for Y"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x = None
        else:
            self.coefficient2_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x2 = None
        else:
            self.coefficient3_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_y = None
        else:
            self.coefficient4_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_xy = None
        else:
            self.coefficient5_xy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient6_x2y = None
        else:
            self.coefficient6_x2y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_y = None
        else:
            self.minimum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_y = None
        else:
            self.maximum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_y = None
        else:
            self.input_unit_type_for_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """Get coefficient2_x

        Returns:
            float: the value of `coefficient2_x` or None if not set
        """
        return self._data["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x`'.format(value))
        self._data["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """Get coefficient3_x2

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self._data["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x**2`

        Args:
            value (float): value for IDD Field `Coefficient3 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x2`'.format(value))
        self._data["Coefficient3 x**2"] = value

    @property
    def coefficient4_y(self):
        """Get coefficient4_y

        Returns:
            float: the value of `coefficient4_y` or None if not set
        """
        return self._data["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_y`'.format(value))
        self._data["Coefficient4 y"] = value

    @property
    def coefficient5_xy(self):
        """Get coefficient5_xy

        Returns:
            float: the value of `coefficient5_xy` or None if not set
        """
        return self._data["Coefficient5 x*y"]

    @coefficient5_xy.setter
    def coefficient5_xy(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 x*y`

        Args:
            value (float): value for IDD Field `Coefficient5 x*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_xy`'.format(value))
        self._data["Coefficient5 x*y"] = value

    @property
    def coefficient6_x2y(self):
        """Get coefficient6_x2y

        Returns:
            float: the value of `coefficient6_x2y` or None if not set
        """
        return self._data["Coefficient6 x**2*y"]

    @coefficient6_x2y.setter
    def coefficient6_x2y(self, value=None):
        """  Corresponds to IDD Field `Coefficient6 x**2*y`

        Args:
            value (float): value for IDD Field `Coefficient6 x**2*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient6_x2y`'.format(value))
        self._data["Coefficient6 x**2*y"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """Get minimum_value_of_y

        Returns:
            float: the value of `minimum_value_of_y` or None if not set
        """
        return self._data["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of y`

        Args:
            value (float): value for IDD Field `Minimum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_y`'.format(value))
        self._data["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """Get maximum_value_of_y

        Returns:
            float: the value of `maximum_value_of_y` or None if not set
        """
        return self._data["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of y`

        Args:
            value (float): value for IDD Field `Maximum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_y`'.format(value))
        self._data["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for Y`

        Args:
            value (str): value for IDD Field `Input Unit Type for Y`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_y`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_y`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_y`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveTriquadratic(object):
    """ Corresponds to IDD object `Curve:Triquadratic`
        Quadratic curve with three independent variables. Input consists of the curve name,
        the twenty seven coefficients, and min and max values for each of the independent
        variables. Optional inputs for curve minimum and maximum may be used to
        limit the output of the performance curve.
        curve = a0 + a1*x**2 + a2*x + a3*y**2 + a4*y
        + a5*z**2 + a6*z + a7*x**2*y**2 + a8*x*y
        + a9*x*y**2 + a10*x**2*y + a11*x**2*z**2
        + a12*x*z + a13*x*z**2 + a14*x**2*z + a15*y**2*z**2
        + a16*y*z + a17*y*z**2 + a18*y**2*z + a19*x**2*y**2*z**2
        + a20*x**2*y**2*z + a21*x**2*y*z**2 + a22*x*y**2*z**2
        + a23*x**2*y*z + a24*x*y**2*z + a25*x*y*z**2 +a26*x*y*z
    
    """
    internal_name = "Curve:Triquadratic"
    field_count = 40
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Triquadratic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 Constant"] = None
        self._data["Coefficient2 x**2"] = None
        self._data["Coefficient3 x"] = None
        self._data["Coefficient4 y**2"] = None
        self._data["Coefficient5 y"] = None
        self._data["Coefficient6 z**2"] = None
        self._data["Coefficient7 z"] = None
        self._data["Coefficient8 x**2*y**2"] = None
        self._data["Coefficient9 x*y"] = None
        self._data["Coefficient10 x*y**2"] = None
        self._data["Coefficient11 x**2*y"] = None
        self._data["Coefficient12 x**2*z**2"] = None
        self._data["Coefficient13 x*z"] = None
        self._data["Coefficient14 x*z**2"] = None
        self._data["Coefficient15 x**2*z"] = None
        self._data["Coefficient16 y**2*z**2"] = None
        self._data["Coefficient17 y*z"] = None
        self._data["Coefficient18 y*z**2"] = None
        self._data["Coefficient19 y**2*z"] = None
        self._data["Coefficient20 x**2*y**2*z**2"] = None
        self._data["Coefficient21 x**2*y**2*z"] = None
        self._data["Coefficient22 x**2*y*z**2"] = None
        self._data["Coefficient23 x*y**2*z**2"] = None
        self._data["Coefficient24 x**2*y*z"] = None
        self._data["Coefficient25 x*y**2*z"] = None
        self._data["Coefficient26 x*y*z**2"] = None
        self._data["Coefficient27 x*y*z"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Value of y"] = None
        self._data["Maximum Value of y"] = None
        self._data["Minimum Value of z"] = None
        self._data["Maximum Value of z"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for X"] = None
        self._data["Input Unit Type for Y"] = None
        self._data["Input Unit Type for Z"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_constant = None
        else:
            self.coefficient1_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_x2 = None
        else:
            self.coefficient2_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_x = None
        else:
            self.coefficient3_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_y2 = None
        else:
            self.coefficient4_y2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_y = None
        else:
            self.coefficient5_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient6_z2 = None
        else:
            self.coefficient6_z2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient7_z = None
        else:
            self.coefficient7_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient8_x2y2 = None
        else:
            self.coefficient8_x2y2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient9_xy = None
        else:
            self.coefficient9_xy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient10_xy2 = None
        else:
            self.coefficient10_xy2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient11_x2y = None
        else:
            self.coefficient11_x2y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient12_x2z2 = None
        else:
            self.coefficient12_x2z2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient13_xz = None
        else:
            self.coefficient13_xz = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient14_xz2 = None
        else:
            self.coefficient14_xz2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient15_x2z = None
        else:
            self.coefficient15_x2z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient16_y2z2 = None
        else:
            self.coefficient16_y2z2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient17_yz = None
        else:
            self.coefficient17_yz = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient18_yz2 = None
        else:
            self.coefficient18_yz2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient19_y2z = None
        else:
            self.coefficient19_y2z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient20_x2y2z2 = None
        else:
            self.coefficient20_x2y2z2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient21_x2y2z = None
        else:
            self.coefficient21_x2y2z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient22_x2yz2 = None
        else:
            self.coefficient22_x2yz2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient23_xy2z2 = None
        else:
            self.coefficient23_xy2z2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient24_x2yz = None
        else:
            self.coefficient24_x2yz = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient25_xy2z = None
        else:
            self.coefficient25_xy2z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient26_xyz2 = None
        else:
            self.coefficient26_xyz2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient27_xyz = None
        else:
            self.coefficient27_xyz = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_y = None
        else:
            self.minimum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_y = None
        else:
            self.maximum_value_of_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_z = None
        else:
            self.minimum_value_of_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_z = None
        else:
            self.maximum_value_of_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_y = None
        else:
            self.input_unit_type_for_y = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_z = None
        else:
            self.input_unit_type_for_z = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_constant(self):
        """Get coefficient1_constant

        Returns:
            float: the value of `coefficient1_constant` or None if not set
        """
        return self._data["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_constant`'.format(value))
        self._data["Coefficient1 Constant"] = value

    @property
    def coefficient2_x2(self):
        """Get coefficient2_x2

        Returns:
            float: the value of `coefficient2_x2` or None if not set
        """
        return self._data["Coefficient2 x**2"]

    @coefficient2_x2.setter
    def coefficient2_x2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 x**2`

        Args:
            value (float): value for IDD Field `Coefficient2 x**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_x2`'.format(value))
        self._data["Coefficient2 x**2"] = value

    @property
    def coefficient3_x(self):
        """Get coefficient3_x

        Returns:
            float: the value of `coefficient3_x` or None if not set
        """
        return self._data["Coefficient3 x"]

    @coefficient3_x.setter
    def coefficient3_x(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 x`

        Args:
            value (float): value for IDD Field `Coefficient3 x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_x`'.format(value))
        self._data["Coefficient3 x"] = value

    @property
    def coefficient4_y2(self):
        """Get coefficient4_y2

        Returns:
            float: the value of `coefficient4_y2` or None if not set
        """
        return self._data["Coefficient4 y**2"]

    @coefficient4_y2.setter
    def coefficient4_y2(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 y**2`

        Args:
            value (float): value for IDD Field `Coefficient4 y**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_y2`'.format(value))
        self._data["Coefficient4 y**2"] = value

    @property
    def coefficient5_y(self):
        """Get coefficient5_y

        Returns:
            float: the value of `coefficient5_y` or None if not set
        """
        return self._data["Coefficient5 y"]

    @coefficient5_y.setter
    def coefficient5_y(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 y`

        Args:
            value (float): value for IDD Field `Coefficient5 y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_y`'.format(value))
        self._data["Coefficient5 y"] = value

    @property
    def coefficient6_z2(self):
        """Get coefficient6_z2

        Returns:
            float: the value of `coefficient6_z2` or None if not set
        """
        return self._data["Coefficient6 z**2"]

    @coefficient6_z2.setter
    def coefficient6_z2(self, value=None):
        """  Corresponds to IDD Field `Coefficient6 z**2`

        Args:
            value (float): value for IDD Field `Coefficient6 z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient6_z2`'.format(value))
        self._data["Coefficient6 z**2"] = value

    @property
    def coefficient7_z(self):
        """Get coefficient7_z

        Returns:
            float: the value of `coefficient7_z` or None if not set
        """
        return self._data["Coefficient7 z"]

    @coefficient7_z.setter
    def coefficient7_z(self, value=None):
        """  Corresponds to IDD Field `Coefficient7 z`

        Args:
            value (float): value for IDD Field `Coefficient7 z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient7_z`'.format(value))
        self._data["Coefficient7 z"] = value

    @property
    def coefficient8_x2y2(self):
        """Get coefficient8_x2y2

        Returns:
            float: the value of `coefficient8_x2y2` or None if not set
        """
        return self._data["Coefficient8 x**2*y**2"]

    @coefficient8_x2y2.setter
    def coefficient8_x2y2(self, value=None):
        """  Corresponds to IDD Field `Coefficient8 x**2*y**2`

        Args:
            value (float): value for IDD Field `Coefficient8 x**2*y**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient8_x2y2`'.format(value))
        self._data["Coefficient8 x**2*y**2"] = value

    @property
    def coefficient9_xy(self):
        """Get coefficient9_xy

        Returns:
            float: the value of `coefficient9_xy` or None if not set
        """
        return self._data["Coefficient9 x*y"]

    @coefficient9_xy.setter
    def coefficient9_xy(self, value=None):
        """  Corresponds to IDD Field `Coefficient9 x*y`

        Args:
            value (float): value for IDD Field `Coefficient9 x*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient9_xy`'.format(value))
        self._data["Coefficient9 x*y"] = value

    @property
    def coefficient10_xy2(self):
        """Get coefficient10_xy2

        Returns:
            float: the value of `coefficient10_xy2` or None if not set
        """
        return self._data["Coefficient10 x*y**2"]

    @coefficient10_xy2.setter
    def coefficient10_xy2(self, value=None):
        """  Corresponds to IDD Field `Coefficient10 x*y**2`

        Args:
            value (float): value for IDD Field `Coefficient10 x*y**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient10_xy2`'.format(value))
        self._data["Coefficient10 x*y**2"] = value

    @property
    def coefficient11_x2y(self):
        """Get coefficient11_x2y

        Returns:
            float: the value of `coefficient11_x2y` or None if not set
        """
        return self._data["Coefficient11 x**2*y"]

    @coefficient11_x2y.setter
    def coefficient11_x2y(self, value=None):
        """  Corresponds to IDD Field `Coefficient11 x**2*y`

        Args:
            value (float): value for IDD Field `Coefficient11 x**2*y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient11_x2y`'.format(value))
        self._data["Coefficient11 x**2*y"] = value

    @property
    def coefficient12_x2z2(self):
        """Get coefficient12_x2z2

        Returns:
            float: the value of `coefficient12_x2z2` or None if not set
        """
        return self._data["Coefficient12 x**2*z**2"]

    @coefficient12_x2z2.setter
    def coefficient12_x2z2(self, value=None):
        """  Corresponds to IDD Field `Coefficient12 x**2*z**2`

        Args:
            value (float): value for IDD Field `Coefficient12 x**2*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient12_x2z2`'.format(value))
        self._data["Coefficient12 x**2*z**2"] = value

    @property
    def coefficient13_xz(self):
        """Get coefficient13_xz

        Returns:
            float: the value of `coefficient13_xz` or None if not set
        """
        return self._data["Coefficient13 x*z"]

    @coefficient13_xz.setter
    def coefficient13_xz(self, value=None):
        """  Corresponds to IDD Field `Coefficient13 x*z`

        Args:
            value (float): value for IDD Field `Coefficient13 x*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient13_xz`'.format(value))
        self._data["Coefficient13 x*z"] = value

    @property
    def coefficient14_xz2(self):
        """Get coefficient14_xz2

        Returns:
            float: the value of `coefficient14_xz2` or None if not set
        """
        return self._data["Coefficient14 x*z**2"]

    @coefficient14_xz2.setter
    def coefficient14_xz2(self, value=None):
        """  Corresponds to IDD Field `Coefficient14 x*z**2`

        Args:
            value (float): value for IDD Field `Coefficient14 x*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient14_xz2`'.format(value))
        self._data["Coefficient14 x*z**2"] = value

    @property
    def coefficient15_x2z(self):
        """Get coefficient15_x2z

        Returns:
            float: the value of `coefficient15_x2z` or None if not set
        """
        return self._data["Coefficient15 x**2*z"]

    @coefficient15_x2z.setter
    def coefficient15_x2z(self, value=None):
        """  Corresponds to IDD Field `Coefficient15 x**2*z`

        Args:
            value (float): value for IDD Field `Coefficient15 x**2*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient15_x2z`'.format(value))
        self._data["Coefficient15 x**2*z"] = value

    @property
    def coefficient16_y2z2(self):
        """Get coefficient16_y2z2

        Returns:
            float: the value of `coefficient16_y2z2` or None if not set
        """
        return self._data["Coefficient16 y**2*z**2"]

    @coefficient16_y2z2.setter
    def coefficient16_y2z2(self, value=None):
        """  Corresponds to IDD Field `Coefficient16 y**2*z**2`

        Args:
            value (float): value for IDD Field `Coefficient16 y**2*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient16_y2z2`'.format(value))
        self._data["Coefficient16 y**2*z**2"] = value

    @property
    def coefficient17_yz(self):
        """Get coefficient17_yz

        Returns:
            float: the value of `coefficient17_yz` or None if not set
        """
        return self._data["Coefficient17 y*z"]

    @coefficient17_yz.setter
    def coefficient17_yz(self, value=None):
        """  Corresponds to IDD Field `Coefficient17 y*z`

        Args:
            value (float): value for IDD Field `Coefficient17 y*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient17_yz`'.format(value))
        self._data["Coefficient17 y*z"] = value

    @property
    def coefficient18_yz2(self):
        """Get coefficient18_yz2

        Returns:
            float: the value of `coefficient18_yz2` or None if not set
        """
        return self._data["Coefficient18 y*z**2"]

    @coefficient18_yz2.setter
    def coefficient18_yz2(self, value=None):
        """  Corresponds to IDD Field `Coefficient18 y*z**2`

        Args:
            value (float): value for IDD Field `Coefficient18 y*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient18_yz2`'.format(value))
        self._data["Coefficient18 y*z**2"] = value

    @property
    def coefficient19_y2z(self):
        """Get coefficient19_y2z

        Returns:
            float: the value of `coefficient19_y2z` or None if not set
        """
        return self._data["Coefficient19 y**2*z"]

    @coefficient19_y2z.setter
    def coefficient19_y2z(self, value=None):
        """  Corresponds to IDD Field `Coefficient19 y**2*z`

        Args:
            value (float): value for IDD Field `Coefficient19 y**2*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient19_y2z`'.format(value))
        self._data["Coefficient19 y**2*z"] = value

    @property
    def coefficient20_x2y2z2(self):
        """Get coefficient20_x2y2z2

        Returns:
            float: the value of `coefficient20_x2y2z2` or None if not set
        """
        return self._data["Coefficient20 x**2*y**2*z**2"]

    @coefficient20_x2y2z2.setter
    def coefficient20_x2y2z2(self, value=None):
        """  Corresponds to IDD Field `Coefficient20 x**2*y**2*z**2`

        Args:
            value (float): value for IDD Field `Coefficient20 x**2*y**2*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient20_x2y2z2`'.format(value))
        self._data["Coefficient20 x**2*y**2*z**2"] = value

    @property
    def coefficient21_x2y2z(self):
        """Get coefficient21_x2y2z

        Returns:
            float: the value of `coefficient21_x2y2z` or None if not set
        """
        return self._data["Coefficient21 x**2*y**2*z"]

    @coefficient21_x2y2z.setter
    def coefficient21_x2y2z(self, value=None):
        """  Corresponds to IDD Field `Coefficient21 x**2*y**2*z`

        Args:
            value (float): value for IDD Field `Coefficient21 x**2*y**2*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient21_x2y2z`'.format(value))
        self._data["Coefficient21 x**2*y**2*z"] = value

    @property
    def coefficient22_x2yz2(self):
        """Get coefficient22_x2yz2

        Returns:
            float: the value of `coefficient22_x2yz2` or None if not set
        """
        return self._data["Coefficient22 x**2*y*z**2"]

    @coefficient22_x2yz2.setter
    def coefficient22_x2yz2(self, value=None):
        """  Corresponds to IDD Field `Coefficient22 x**2*y*z**2`

        Args:
            value (float): value for IDD Field `Coefficient22 x**2*y*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient22_x2yz2`'.format(value))
        self._data["Coefficient22 x**2*y*z**2"] = value

    @property
    def coefficient23_xy2z2(self):
        """Get coefficient23_xy2z2

        Returns:
            float: the value of `coefficient23_xy2z2` or None if not set
        """
        return self._data["Coefficient23 x*y**2*z**2"]

    @coefficient23_xy2z2.setter
    def coefficient23_xy2z2(self, value=None):
        """  Corresponds to IDD Field `Coefficient23 x*y**2*z**2`

        Args:
            value (float): value for IDD Field `Coefficient23 x*y**2*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient23_xy2z2`'.format(value))
        self._data["Coefficient23 x*y**2*z**2"] = value

    @property
    def coefficient24_x2yz(self):
        """Get coefficient24_x2yz

        Returns:
            float: the value of `coefficient24_x2yz` or None if not set
        """
        return self._data["Coefficient24 x**2*y*z"]

    @coefficient24_x2yz.setter
    def coefficient24_x2yz(self, value=None):
        """  Corresponds to IDD Field `Coefficient24 x**2*y*z`

        Args:
            value (float): value for IDD Field `Coefficient24 x**2*y*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient24_x2yz`'.format(value))
        self._data["Coefficient24 x**2*y*z"] = value

    @property
    def coefficient25_xy2z(self):
        """Get coefficient25_xy2z

        Returns:
            float: the value of `coefficient25_xy2z` or None if not set
        """
        return self._data["Coefficient25 x*y**2*z"]

    @coefficient25_xy2z.setter
    def coefficient25_xy2z(self, value=None):
        """  Corresponds to IDD Field `Coefficient25 x*y**2*z`

        Args:
            value (float): value for IDD Field `Coefficient25 x*y**2*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient25_xy2z`'.format(value))
        self._data["Coefficient25 x*y**2*z"] = value

    @property
    def coefficient26_xyz2(self):
        """Get coefficient26_xyz2

        Returns:
            float: the value of `coefficient26_xyz2` or None if not set
        """
        return self._data["Coefficient26 x*y*z**2"]

    @coefficient26_xyz2.setter
    def coefficient26_xyz2(self, value=None):
        """  Corresponds to IDD Field `Coefficient26 x*y*z**2`

        Args:
            value (float): value for IDD Field `Coefficient26 x*y*z**2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient26_xyz2`'.format(value))
        self._data["Coefficient26 x*y*z**2"] = value

    @property
    def coefficient27_xyz(self):
        """Get coefficient27_xyz

        Returns:
            float: the value of `coefficient27_xyz` or None if not set
        """
        return self._data["Coefficient27 x*y*z"]

    @coefficient27_xyz.setter
    def coefficient27_xyz(self, value=None):
        """  Corresponds to IDD Field `Coefficient27 x*y*z`

        Args:
            value (float): value for IDD Field `Coefficient27 x*y*z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient27_xyz`'.format(value))
        self._data["Coefficient27 x*y*z"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """Get minimum_value_of_y

        Returns:
            float: the value of `minimum_value_of_y` or None if not set
        """
        return self._data["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of y`

        Args:
            value (float): value for IDD Field `Minimum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_y`'.format(value))
        self._data["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """Get maximum_value_of_y

        Returns:
            float: the value of `maximum_value_of_y` or None if not set
        """
        return self._data["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of y`

        Args:
            value (float): value for IDD Field `Maximum Value of y`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_y`'.format(value))
        self._data["Maximum Value of y"] = value

    @property
    def minimum_value_of_z(self):
        """Get minimum_value_of_z

        Returns:
            float: the value of `minimum_value_of_z` or None if not set
        """
        return self._data["Minimum Value of z"]

    @minimum_value_of_z.setter
    def minimum_value_of_z(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of z`

        Args:
            value (float): value for IDD Field `Minimum Value of z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_z`'.format(value))
        self._data["Minimum Value of z"] = value

    @property
    def maximum_value_of_z(self):
        """Get maximum_value_of_z

        Returns:
            float: the value of `maximum_value_of_z` or None if not set
        """
        return self._data["Maximum Value of z"]

    @maximum_value_of_z.setter
    def maximum_value_of_z(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of z`

        Args:
            value (float): value for IDD Field `Maximum Value of z`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_z`'.format(value))
        self._data["Maximum Value of z"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for X`

        Args:
            value (str): value for IDD Field `Input Unit Type for X`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for Y`

        Args:
            value (str): value for IDD Field `Input Unit Type for Y`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_y`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_y`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_y`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for Y"] = value

    @property
    def input_unit_type_for_z(self):
        """Get input_unit_type_for_z

        Returns:
            str: the value of `input_unit_type_for_z` or None if not set
        """
        return self._data["Input Unit Type for Z"]

    @input_unit_type_for_z.setter
    def input_unit_type_for_z(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for Z`

        Args:
            value (str): value for IDD Field `Input Unit Type for Z`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_z`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_z`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_z`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["massflow"] = "MassFlow"
            vals["power"] = "Power"
            vals["distance"] = "Distance"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_z`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for Z"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveFunctionalPressureDrop(object):
    """ Corresponds to IDD object `Curve:Functional:PressureDrop`
        Sets up curve information for minor loss and/or friction
        calculations in plant pressure simulations
        Expression: DeltaP = {K + f*(L/D)} * (rho * V^2) / 2
    
    """
    internal_name = "Curve:Functional:PressureDrop"
    field_count = 6
    required_fields = ["Name", "Diameter"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Functional:PressureDrop`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Diameter"] = None
        self._data["Minor Loss Coefficient"] = None
        self._data["Length"] = None
        self._data["Roughness"] = None
        self._data["Fixed Friction Factor"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diameter = None
        else:
            self.diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minor_loss_coefficient = None
        else:
            self.minor_loss_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.roughness = None
        else:
            self.roughness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fixed_friction_factor = None
        else:
            self.fixed_friction_factor = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def diameter(self):
        """Get diameter

        Returns:
            float: the value of `diameter` or None if not set
        """
        return self._data["Diameter"]

    @diameter.setter
    def diameter(self, value=None):
        """  Corresponds to IDD Field `Diameter`
        "D" in above expression, used to also calculate local velocity

        Args:
            value (float): value for IDD Field `Diameter`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `diameter`')
        self._data["Diameter"] = value

    @property
    def minor_loss_coefficient(self):
        """Get minor_loss_coefficient

        Returns:
            float: the value of `minor_loss_coefficient` or None if not set
        """
        return self._data["Minor Loss Coefficient"]

    @minor_loss_coefficient.setter
    def minor_loss_coefficient(self, value=None):
        """  Corresponds to IDD Field `Minor Loss Coefficient`
        "K" in above expression

        Args:
            value (float): value for IDD Field `Minor Loss Coefficient`
                Units: dimensionless
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
                raise ValueError('value {} need to be of type float '
                                 'for field `minor_loss_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minor_loss_coefficient`')
        self._data["Minor Loss Coefficient"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        "L" in above expression

        Args:
            value (float): value for IDD Field `Length`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `length`')
        self._data["Length"] = value

    @property
    def roughness(self):
        """Get roughness

        Returns:
            float: the value of `roughness` or None if not set
        """
        return self._data["Roughness"]

    @roughness.setter
    def roughness(self, value=None):
        """  Corresponds to IDD Field `Roughness`
        This will be used to calculate "f" from Moody-chart approximations

        Args:
            value (float): value for IDD Field `Roughness`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `roughness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `roughness`')
        self._data["Roughness"] = value

    @property
    def fixed_friction_factor(self):
        """Get fixed_friction_factor

        Returns:
            float: the value of `fixed_friction_factor` or None if not set
        """
        return self._data["Fixed Friction Factor"]

    @fixed_friction_factor.setter
    def fixed_friction_factor(self, value=None):
        """  Corresponds to IDD Field `Fixed Friction Factor`
        Optional way to set a constant value for "f", instead of using
        internal Moody-chart approximations

        Args:
            value (float): value for IDD Field `Fixed Friction Factor`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `fixed_friction_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `fixed_friction_factor`')
        self._data["Fixed Friction Factor"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveFanPressureRise(object):
    """ Corresponds to IDD object `Curve:FanPressureRise`
        Special curve type with two independent variables.
        Input for the fan total pressure rise curve consists of the curve name, the four
        coefficients, and the maximum and minimum valid independent variable values. Optional
        inputs for the curve minimum and maximum may be used to limit the output of the
        performance curve.
        curve = C1*Qfan**2+C2*Qfan+C3*Qfan*(Psm-Po)**0.5+C4*(Psm-Po)
        Po assumed to be zero
        See InputOut Reference for curve details
    
    """
    internal_name = "Curve:FanPressureRise"
    field_count = 11
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Coefficient4 C4", "Minimum Value of Qfan", "Maximum Value of Qfan", "Minimum Value of Psm", "Maximum Value of Psm"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:FanPressureRise`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Coefficient4 C4"] = None
        self._data["Minimum Value of Qfan"] = None
        self._data["Maximum Value of Qfan"] = None
        self._data["Minimum Value of Psm"] = None
        self._data["Maximum Value of Psm"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_c4 = None
        else:
            self.coefficient4_c4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_qfan = None
        else:
            self.minimum_value_of_qfan = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_qfan = None
        else:
            self.maximum_value_of_qfan = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_psm = None
        else:
            self.minimum_value_of_psm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_psm = None
        else:
            self.maximum_value_of_psm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """Get coefficient4_c4

        Returns:
            float: the value of `coefficient4_c4` or None if not set
        """
        return self._data["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_c4`'.format(value))
        self._data["Coefficient4 C4"] = value

    @property
    def minimum_value_of_qfan(self):
        """Get minimum_value_of_qfan

        Returns:
            float: the value of `minimum_value_of_qfan` or None if not set
        """
        return self._data["Minimum Value of Qfan"]

    @minimum_value_of_qfan.setter
    def minimum_value_of_qfan(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of Qfan`

        Args:
            value (float): value for IDD Field `Minimum Value of Qfan`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_qfan`'.format(value))
        self._data["Minimum Value of Qfan"] = value

    @property
    def maximum_value_of_qfan(self):
        """Get maximum_value_of_qfan

        Returns:
            float: the value of `maximum_value_of_qfan` or None if not set
        """
        return self._data["Maximum Value of Qfan"]

    @maximum_value_of_qfan.setter
    def maximum_value_of_qfan(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of Qfan`

        Args:
            value (float): value for IDD Field `Maximum Value of Qfan`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_qfan`'.format(value))
        self._data["Maximum Value of Qfan"] = value

    @property
    def minimum_value_of_psm(self):
        """Get minimum_value_of_psm

        Returns:
            float: the value of `minimum_value_of_psm` or None if not set
        """
        return self._data["Minimum Value of Psm"]

    @minimum_value_of_psm.setter
    def minimum_value_of_psm(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of Psm`

        Args:
            value (float): value for IDD Field `Minimum Value of Psm`
                Units: Pa
                IP-Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_psm`'.format(value))
        self._data["Minimum Value of Psm"] = value

    @property
    def maximum_value_of_psm(self):
        """Get maximum_value_of_psm

        Returns:
            float: the value of `maximum_value_of_psm` or None if not set
        """
        return self._data["Maximum Value of Psm"]

    @maximum_value_of_psm.setter
    def maximum_value_of_psm(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of Psm`

        Args:
            value (float): value for IDD Field `Maximum Value of Psm`
                Units: Pa
                IP-Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_psm`'.format(value))
        self._data["Maximum Value of Psm"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                Units: Pa
                IP-Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                Units: Pa
                IP-Units: Pa
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveExponentialSkewNormal(object):
    """ Corresponds to IDD object `Curve:ExponentialSkewNormal`
        Exponential-modified skew normal curve with one independent variable.
        Input consists of the curve name, the four coefficients, and the maximum
        and minimum valid independent variable values. Optional inputs for the curve minimum
        and maximum may be used to limit the output of the performance curve.
        curve = see Input Output Reference
    
    """
    internal_name = "Curve:ExponentialSkewNormal"
    field_count = 11
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Coefficient4 C4", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:ExponentialSkewNormal`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Coefficient4 C4"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_c4 = None
        else:
            self.coefficient4_c4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
        See InputOut Reference for curve description

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """Get coefficient4_c4

        Returns:
            float: the value of `coefficient4_c4` or None if not set
        """
        return self._data["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_c4`'.format(value))
        self._data["Coefficient4 C4"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveSigmoid(object):
    """ Corresponds to IDD object `Curve:Sigmoid`
        Sigmoid curve with one independent variable.
        Input consists of the curve name, the five coefficients, and the maximum and minimum
        valid independent variable values. Optional inputs for the curve minimum and maximum
        may be used to limit the output of the performance curve.
        curve = C1+C2/[1+exp((C3-x)/C4)]**C5
    
    """
    internal_name = "Curve:Sigmoid"
    field_count = 12
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Coefficient4 C4", "Coefficient5 C5", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:Sigmoid`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Coefficient4 C4"] = None
        self._data["Coefficient5 C5"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient4_c4 = None
        else:
            self.coefficient4_c4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient5_c5 = None
        else:
            self.coefficient5_c5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
        See InputOut Reference for curve description

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """Get coefficient4_c4

        Returns:
            float: the value of `coefficient4_c4` or None if not set
        """
        return self._data["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """  Corresponds to IDD Field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient4_c4`'.format(value))
        self._data["Coefficient4 C4"] = value

    @property
    def coefficient5_c5(self):
        """Get coefficient5_c5

        Returns:
            float: the value of `coefficient5_c5` or None if not set
        """
        return self._data["Coefficient5 C5"]

    @coefficient5_c5.setter
    def coefficient5_c5(self, value=None):
        """  Corresponds to IDD Field `Coefficient5 C5`

        Args:
            value (float): value for IDD Field `Coefficient5 C5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient5_c5`'.format(value))
        self._data["Coefficient5 C5"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveRectangularHyperbola1(object):
    """ Corresponds to IDD object `Curve:RectangularHyperbola1`
        Rectangular hyperbola type 1 curve with one independent variable.
        Input consists of the curve name, the three coefficients, and the maximum and
        minimum valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = ((C1*x)/(C2+x))+C3
    
    """
    internal_name = "Curve:RectangularHyperbola1"
    field_count = 10
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:RectangularHyperbola1`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveRectangularHyperbola2(object):
    """ Corresponds to IDD object `Curve:RectangularHyperbola2`
        Rectangular hyperbola type 2 curve with one independent variable.
        Input consists of the curve name, the three coefficients, and the maximum and
        minimum valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = ((C1*x)/(C2+x))+(C3*x)
    
    """
    internal_name = "Curve:RectangularHyperbola2"
    field_count = 10
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:RectangularHyperbola2`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveExponentialDecay(object):
    """ Corresponds to IDD object `Curve:ExponentialDecay`
        Exponential decay curve with one independent variable.
        Input consists of the curve name, the three coefficients, and the maximum and minimum
        valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = C1+C2*exp(C3*x)
    
    """
    internal_name = "Curve:ExponentialDecay"
    field_count = 10
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:ExponentialDecay`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class CurveDoubleExponentialDecay(object):
    """ Corresponds to IDD object `Curve:DoubleExponentialDecay`
        Double exponential decay curve with one independent variable.
        Input consists of the curve name, the five coefficients, and the maximum and minimum
        valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = C1+C2*exp(C3*x)+C4*exp(C5*x)
    
    """
    internal_name = "Curve:DoubleExponentialDecay"
    field_count = 12
    required_fields = ["Name", "Coefficient1 C1", "Coefficient2 C2", "Coefficient3 C3", "Coefficient3 C4", "Coefficient3 C5", "Minimum Value of x", "Maximum Value of x"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Curve:DoubleExponentialDecay`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Coefficient1 C1"] = None
        self._data["Coefficient2 C2"] = None
        self._data["Coefficient3 C3"] = None
        self._data["Coefficient3 C4"] = None
        self._data["Coefficient3 C5"] = None
        self._data["Minimum Value of x"] = None
        self._data["Maximum Value of x"] = None
        self._data["Minimum Curve Output"] = None
        self._data["Maximum Curve Output"] = None
        self._data["Input Unit Type for x"] = None
        self._data["Output Unit Type"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient1_c1 = None
        else:
            self.coefficient1_c1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient2_c2 = None
        else:
            self.coefficient2_c2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c3 = None
        else:
            self.coefficient3_c3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c4 = None
        else:
            self.coefficient3_c4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient3_c5 = None
        else:
            self.coefficient3_c5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x = None
        else:
            self.minimum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x = None
        else:
            self.maximum_value_of_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_curve_output = None
        else:
            self.minimum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_curve_output = None
        else:
            self.maximum_curve_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x = None
        else:
            self.input_unit_type_for_x = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.output_unit_type = None
        else:
            self.output_unit_type = vals[i]
        i += 1
        if i >= len(vals):
            return

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
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def coefficient1_c1(self):
        """Get coefficient1_c1

        Returns:
            float: the value of `coefficient1_c1` or None if not set
        """
        return self._data["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """  Corresponds to IDD Field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient1_c1`'.format(value))
        self._data["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """Get coefficient2_c2

        Returns:
            float: the value of `coefficient2_c2` or None if not set
        """
        return self._data["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """  Corresponds to IDD Field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient2_c2`'.format(value))
        self._data["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """Get coefficient3_c3

        Returns:
            float: the value of `coefficient3_c3` or None if not set
        """
        return self._data["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c3`'.format(value))
        self._data["Coefficient3 C3"] = value

    @property
    def coefficient3_c4(self):
        """Get coefficient3_c4

        Returns:
            float: the value of `coefficient3_c4` or None if not set
        """
        return self._data["Coefficient3 C4"]

    @coefficient3_c4.setter
    def coefficient3_c4(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C4`

        Args:
            value (float): value for IDD Field `Coefficient3 C4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c4`'.format(value))
        self._data["Coefficient3 C4"] = value

    @property
    def coefficient3_c5(self):
        """Get coefficient3_c5

        Returns:
            float: the value of `coefficient3_c5` or None if not set
        """
        return self._data["Coefficient3 C5"]

    @coefficient3_c5.setter
    def coefficient3_c5(self, value=None):
        """  Corresponds to IDD Field `Coefficient3 C5`

        Args:
            value (float): value for IDD Field `Coefficient3 C5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient3_c5`'.format(value))
        self._data["Coefficient3 C5"] = value

    @property
    def minimum_value_of_x(self):
        """Get minimum_value_of_x

        Returns:
            float: the value of `minimum_value_of_x` or None if not set
        """
        return self._data["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Minimum Value of x`

        Args:
            value (float): value for IDD Field `Minimum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_value_of_x`'.format(value))
        self._data["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """Get maximum_value_of_x

        Returns:
            float: the value of `maximum_value_of_x` or None if not set
        """
        return self._data["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """  Corresponds to IDD Field `Maximum Value of x`

        Args:
            value (float): value for IDD Field `Maximum Value of x`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_value_of_x`'.format(value))
        self._data["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """Get minimum_curve_output

        Returns:
            float: the value of `minimum_curve_output` or None if not set
        """
        return self._data["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Minimum Curve Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_curve_output`'.format(value))
        self._data["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """Get maximum_curve_output

        Returns:
            float: the value of `maximum_curve_output` or None if not set
        """
        return self._data["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """  Corresponds to IDD Field `Maximum Curve Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Curve Output`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_curve_output`'.format(value))
        self._data["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """Get input_unit_type_for_x

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set
        """
        return self._data["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Input Unit Type for x`

        Args:
            value (str): value for IDD Field `Input Unit Type for x`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `input_unit_type_for_x`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `input_unit_type_for_x`'.format(value))
            value = vals[value_lower]
        self._data["Input Unit Type for x"] = value

    @property
    def output_unit_type(self):
        """Get output_unit_type

        Returns:
            str: the value of `output_unit_type` or None if not set
        """
        return self._data["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """  Corresponds to IDD Field `Output Unit Type`

        Args:
            value (str): value for IDD Field `Output Unit Type`
                Accepted values are:
                      - Dimensionless
                Default value: Dimensionless
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `output_unit_type`'.format(value))
            value = vals[value_lower]
        self._data["Output Unit Type"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])