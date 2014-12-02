from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

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
    field_count = 10
    required_fields = ["Name", "Curve Type"]
    extensible_fields = 2
    format = None
    min_fields = 14
    extensible_keys = ["X Value", "Output Value"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Table:OneIndependentVariable`
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
            self.curve_type = None
        else:
            self.curve_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interpolation_method = None
        else:
            self.interpolation_method = vals[i]
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
            self.minimum_table_output = None
        else:
            self.minimum_table_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_table_output = None
        else:
            self.maximum_table_output = vals[i]
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
        if len(vals[i]) == 0:
            self.normalization_reference = None
        else:
            self.normalization_reference = vals[i]
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
                                 ' for field `TableOneIndependentVariable.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableOneIndependentVariable.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableOneIndependentVariable.name`')
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
        """  Corresponds to IDD Field `Curve Type`

        Args:
            value (str): value for IDD Field `Curve Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableOneIndependentVariable.curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableOneIndependentVariable.curve_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableOneIndependentVariable.curve_type`')
            vals = {}
            vals["linear"] = "Linear"
            vals["quadratic"] = "Quadratic"
            vals["cubic"] = "Cubic"
            vals["quartic"] = "Quartic"
            vals["exponent"] = "Exponent"
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
                                     'field `TableOneIndependentVariable.curve_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableOneIndependentVariable.curve_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Interpolation Method`

        Args:
            value (str): value for IDD Field `Interpolation Method`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableOneIndependentVariable.interpolation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableOneIndependentVariable.interpolation_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableOneIndependentVariable.interpolation_method`')
            vals = {}
            vals["linearinterpolationoftable"] = "LinearInterpolationOfTable"
            vals["evaluatecurvetolimits"] = "EvaluateCurveToLimits"
            vals["lagrangeinterpolationlinearextrapolation"] = "LagrangeInterpolationLinearExtrapolation"
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
                                     'field `TableOneIndependentVariable.interpolation_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableOneIndependentVariable.interpolation_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Minimum Value of X`
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `Minimum Value of X`
                Units are based on field `A4`
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
                                 ' for field `TableOneIndependentVariable.minimum_value_of_x`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X`
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `Maximum Value of X`
                Units are based on field `A4`
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
                                 ' for field `TableOneIndependentVariable.maximum_value_of_x`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Table Output`
        Specify the minimum value calculated by this table
        lookup object
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `Minimum Table Output`
                Units are based on field `A5`
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
                                 ' for field `TableOneIndependentVariable.minimum_table_output`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Table Output`
        Specify the maximum value calculated by this table
        lookup object
        used only when Interpolation Type is Evaluate Curve
        to Limits

        Args:
            value (float): value for IDD Field `Maximum Table Output`
                Units are based on field `A5`
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
                                 ' for field `TableOneIndependentVariable.maximum_table_output`'.format(value))
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableOneIndependentVariable.input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableOneIndependentVariable.input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableOneIndependentVariable.input_unit_type_for_x`')
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
                                     'field `TableOneIndependentVariable.input_unit_type_for_x`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableOneIndependentVariable.input_unit_type_for_x`'.format(value, vals[value_lower]))
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableOneIndependentVariable.output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableOneIndependentVariable.output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableOneIndependentVariable.output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
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
                                     'field `TableOneIndependentVariable.output_unit_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableOneIndependentVariable.output_unit_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Normalization Reference`
        This field is used to normalize the following ouput data.
        The minimum and maximum table output fields are also normalized.
        If this field is blank or 1, the table data presented
        in the following fields will be used with normalization
        reference set to 1.

        Args:
            value (float): value for IDD Field `Normalization Reference`
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
                                 ' for field `TableOneIndependentVariable.normalization_reference`'.format(value))
        self._data["Normalization Reference"] = value

    def add_extensible(self,
                       x_value=None,
                       output_value=None,
                       ):
        """ Add values for extensible fields

        Args:

            x_value (float): value for IDD Field `X Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_value (float): value for IDD Field `Output Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_x_value(x_value))
        vals.append(self._check_output_value(output_value))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_x_value(self, value):
        """ Validates falue of field `X Value`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableOneIndependentVariable.x_value`'.format(value))
        return value

    def _check_output_value(self, value):
        """ Validates falue of field `Output Value`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableOneIndependentVariable.output_value`'.format(value))
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
                    raise ValueError("Required field TableOneIndependentVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field TableOneIndependentVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for TableOneIndependentVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for TableOneIndependentVariable: {} / {}".format(out_fields,
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
    field_count = 13
    required_fields = ["Name", "Curve Type"]
    extensible_fields = 3
    format = None
    min_fields = 22
    extensible_keys = ["X Value", "Y Value", "Output Value"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Table:TwoIndependentVariables`
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
            self.curve_type = None
        else:
            self.curve_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interpolation_method = None
        else:
            self.interpolation_method = vals[i]
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
            self.minimum_table_output = None
        else:
            self.minimum_table_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_table_output = None
        else:
            self.maximum_table_output = vals[i]
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
        if len(vals[i]) == 0:
            self.normalization_reference = None
        else:
            self.normalization_reference = vals[i]
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
                                 ' for field `TableTwoIndependentVariables.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableTwoIndependentVariables.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableTwoIndependentVariables.name`')
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
        """  Corresponds to IDD Field `Curve Type`

        Args:
            value (str): value for IDD Field `Curve Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableTwoIndependentVariables.curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableTwoIndependentVariables.curve_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableTwoIndependentVariables.curve_type`')
            vals = {}
            vals["biquadratic"] = "BiQuadratic"
            vals["quadraticlinear"] = "QuadraticLinear"
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
                                     'field `TableTwoIndependentVariables.curve_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableTwoIndependentVariables.curve_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Interpolation Method`

        Args:
            value (str): value for IDD Field `Interpolation Method`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableTwoIndependentVariables.interpolation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableTwoIndependentVariables.interpolation_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableTwoIndependentVariables.interpolation_method`')
            vals = {}
            vals["linearinterpolationoftable"] = "LinearInterpolationOfTable"
            vals["evaluatecurvetolimits"] = "EvaluateCurveToLimits"
            vals["lagrangeinterpolationlinearextrapolation"] = "LagrangeInterpolationLinearExtrapolation"
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
                                     'field `TableTwoIndependentVariables.interpolation_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableTwoIndependentVariables.interpolation_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Minimum Value of X`

        Args:
            value (float): value for IDD Field `Minimum Value of X`
                Units are based on field `A4`
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
                                 ' for field `TableTwoIndependentVariables.minimum_value_of_x`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X`

        Args:
            value (float): value for IDD Field `Maximum Value of X`
                Units are based on field `A4`
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
                                 ' for field `TableTwoIndependentVariables.maximum_value_of_x`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Value of Y`

        Args:
            value (float): value for IDD Field `Minimum Value of Y`
                Units are based on field `A5`
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
                                 ' for field `TableTwoIndependentVariables.minimum_value_of_y`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of Y`

        Args:
            value (float): value for IDD Field `Maximum Value of Y`
                Units are based on field `A5`
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
                                 ' for field `TableTwoIndependentVariables.maximum_value_of_y`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Table Output`
        Specify the minimum value calculated by this table lookup object

        Args:
            value (float): value for IDD Field `Minimum Table Output`
                Units are based on field `A6`
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
                                 ' for field `TableTwoIndependentVariables.minimum_table_output`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Table Output`
        Specify the maximum value calculated by this table lookup object

        Args:
            value (float): value for IDD Field `Maximum Table Output`
                Units are based on field `A6`
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
                                 ' for field `TableTwoIndependentVariables.maximum_table_output`'.format(value))
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableTwoIndependentVariables.input_unit_type_for_x`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableTwoIndependentVariables.input_unit_type_for_x`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableTwoIndependentVariables.input_unit_type_for_x`')
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
                                     'field `TableTwoIndependentVariables.input_unit_type_for_x`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableTwoIndependentVariables.input_unit_type_for_x`'.format(value, vals[value_lower]))
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableTwoIndependentVariables.input_unit_type_for_y`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableTwoIndependentVariables.input_unit_type_for_y`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableTwoIndependentVariables.input_unit_type_for_y`')
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
                                     'field `TableTwoIndependentVariables.input_unit_type_for_y`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableTwoIndependentVariables.input_unit_type_for_y`'.format(value, vals[value_lower]))
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableTwoIndependentVariables.output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableTwoIndependentVariables.output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableTwoIndependentVariables.output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
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
                                     'field `TableTwoIndependentVariables.output_unit_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableTwoIndependentVariables.output_unit_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Normalization Reference`
        This field is used to normalize the following output data.
        The minimum and maximum table output fields are also normalized.
        If this field is blank or 1, the table data presented below will be used.

        Args:
            value (float): value for IDD Field `Normalization Reference`
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
                                 ' for field `TableTwoIndependentVariables.normalization_reference`'.format(value))
        self._data["Normalization Reference"] = value

    def add_extensible(self,
                       x_value=None,
                       y_value=None,
                       output_value=None,
                       ):
        """ Add values for extensible fields

        Args:

            x_value (float): value for IDD Field `X Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            y_value (float): value for IDD Field `Y Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_value (float): value for IDD Field `Output Value`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_x_value(x_value))
        vals.append(self._check_y_value(y_value))
        vals.append(self._check_output_value(output_value))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_x_value(self, value):
        """ Validates falue of field `X Value`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableTwoIndependentVariables.x_value`'.format(value))
        return value

    def _check_y_value(self, value):
        """ Validates falue of field `Y Value`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableTwoIndependentVariables.y_value`'.format(value))
        return value

    def _check_output_value(self, value):
        """ Validates falue of field `Output Value`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableTwoIndependentVariables.output_value`'.format(value))
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
                    raise ValueError("Required field TableTwoIndependentVariables:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field TableTwoIndependentVariables:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for TableTwoIndependentVariables: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for TableTwoIndependentVariables: {} / {}".format(out_fields,
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
    field_count = 31
    required_fields = ["Name"]
    extensible_fields = 20
    format = None
    min_fields = 27
    extensible_keys = ["Field 3 Determined by the Number of Independent Variables", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Table:MultiVariableLookup`
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
            self.interpolation_method = None
        else:
            self.interpolation_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_interpolation_points = None
        else:
            self.number_of_interpolation_points = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.curve_type = None
        else:
            self.curve_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.table_data_format = None
        else:
            self.table_data_format = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.external_file_name = None
        else:
            self.external_file_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.x1_sort_order = None
        else:
            self.x1_sort_order = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.x2_sort_order = None
        else:
            self.x2_sort_order = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.normalization_reference = None
        else:
            self.normalization_reference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x1 = None
        else:
            self.minimum_value_of_x1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x1 = None
        else:
            self.maximum_value_of_x1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x2 = None
        else:
            self.minimum_value_of_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x2 = None
        else:
            self.maximum_value_of_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x3 = None
        else:
            self.minimum_value_of_x3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x3 = None
        else:
            self.maximum_value_of_x3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x4 = None
        else:
            self.minimum_value_of_x4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x4 = None
        else:
            self.maximum_value_of_x4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_value_of_x5 = None
        else:
            self.minimum_value_of_x5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_value_of_x5 = None
        else:
            self.maximum_value_of_x5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_table_output = None
        else:
            self.minimum_table_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_table_output = None
        else:
            self.maximum_table_output = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x1 = None
        else:
            self.input_unit_type_for_x1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x2 = None
        else:
            self.input_unit_type_for_x2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x3 = None
        else:
            self.input_unit_type_for_x3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x4 = None
        else:
            self.input_unit_type_for_x4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.input_unit_type_for_x5 = None
        else:
            self.input_unit_type_for_x5 = vals[i]
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
        if len(vals[i]) == 0:
            self.number_of_independent_variables = None
        else:
            self.number_of_independent_variables = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_values_for_independent_variable_x1 = None
        else:
            self.number_of_values_for_independent_variable_x1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.field_1_determined_by_the_number_of_independent_variables = None
        else:
            self.field_1_determined_by_the_number_of_independent_variables = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.field_2_determined_by_the_number_of_independent_variables = None
        else:
            self.field_2_determined_by_the_number_of_independent_variables = vals[i]
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
                                 ' for field `TableMultiVariableLookup.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.name`')
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
        """  Corresponds to IDD Field `Interpolation Method`

        Args:
            value (str): value for IDD Field `Interpolation Method`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.interpolation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.interpolation_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.interpolation_method`')
            vals = {}
            vals["linearinterpolationoftable"] = "LinearInterpolationOfTable"
            vals["evaluatecurvetolimits"] = "EvaluateCurveToLimits"
            vals["lagrangeinterpolationlinearextrapolation"] = "LagrangeInterpolationLinearExtrapolation"
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
                                     'field `TableMultiVariableLookup.interpolation_method`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.interpolation_method`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Interpolation Method"] = value

    @property
    def number_of_interpolation_points(self):
        """Get number_of_interpolation_points

        Returns:
            int: the value of `number_of_interpolation_points` or None if not set
        """
        return self._data["Number of Interpolation Points"]

    @number_of_interpolation_points.setter
    def number_of_interpolation_points(self, value=3):
        """  Corresponds to IDD Field `Number of Interpolation Points`

        Args:
            value (int): value for IDD Field `Number of Interpolation Points`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `TableMultiVariableLookup.number_of_interpolation_points`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `TableMultiVariableLookup.number_of_interpolation_points`'.format(value))
            if value <= 1:
                raise ValueError('value need to be greater 1 '
                                 'for field `TableMultiVariableLookup.number_of_interpolation_points`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `TableMultiVariableLookup.number_of_interpolation_points`')
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
        """  Corresponds to IDD Field `Curve Type`
        The curve types BiCubic and TriQuadratic may not
        be used with Interpolation Method = EvaluateCurveToLimits

        Args:
            value (str): value for IDD Field `Curve Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.curve_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.curve_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.curve_type`')
            vals = {}
            vals["linear"] = "Linear"
            vals["quadratic"] = "Quadratic"
            vals["cubic"] = "Cubic"
            vals["quartic"] = "Quartic"
            vals["exponent"] = "Exponent"
            vals["biquadratic"] = "BiQuadratic"
            vals["quadraticlinear"] = "QuadraticLinear"
            vals["bicubic"] = "BiCubic"
            vals["triquadratic"] = "TriQuadratic"
            vals["other"] = "Other"
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
                                     'field `TableMultiVariableLookup.curve_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.curve_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Table Data Format`

        Args:
            value (str): value for IDD Field `Table Data Format`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.table_data_format`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.table_data_format`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.table_data_format`')
            vals = {}
            vals["singlelineindependentvariablewithmatrix"] = "SingleLineIndependentVariableWithMatrix"
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
                                     'field `TableMultiVariableLookup.table_data_format`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.table_data_format`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `External File Name`

        Args:
            value (str): value for IDD Field `External File Name`
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
                                 ' for field `TableMultiVariableLookup.external_file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.external_file_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.external_file_name`')
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
        """  Corresponds to IDD Field `X1 Sort Order`

        Args:
            value (str): value for IDD Field `X1 Sort Order`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.x1_sort_order`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.x1_sort_order`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.x1_sort_order`')
            vals = {}
            vals["ascending"] = "Ascending"
            vals["descending"] = "Descending"
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
                                     'field `TableMultiVariableLookup.x1_sort_order`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.x1_sort_order`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `X2 Sort Order`

        Args:
            value (str): value for IDD Field `X2 Sort Order`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.x2_sort_order`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.x2_sort_order`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.x2_sort_order`')
            vals = {}
            vals["ascending"] = "Ascending"
            vals["descending"] = "Descending"
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
                                     'field `TableMultiVariableLookup.x2_sort_order`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.x2_sort_order`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Normalization Reference`
        This field is used to normalize the table output data.
        The minimum and maximum table output fields are also normalized.
        If this field is blank or 1, the table data will be directly used.
        This field is not allowed to be set equal to 0.

        Args:
            value (float): value for IDD Field `Normalization Reference`
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
                                 ' for field `TableMultiVariableLookup.normalization_reference`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Value of X1`

        Args:
            value (float): value for IDD Field `Minimum Value of X1`
                Units are based on field `A8`
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
                                 ' for field `TableMultiVariableLookup.minimum_value_of_x1`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X1`

        Args:
            value (float): value for IDD Field `Maximum Value of X1`
                Units are based on field `A8`
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
                                 ' for field `TableMultiVariableLookup.maximum_value_of_x1`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Value of X2`

        Args:
            value (float): value for IDD Field `Minimum Value of X2`
                Units are based on field `A9`
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
                                 ' for field `TableMultiVariableLookup.minimum_value_of_x2`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X2`

        Args:
            value (float): value for IDD Field `Maximum Value of X2`
                Units are based on field `A9`
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
                                 ' for field `TableMultiVariableLookup.maximum_value_of_x2`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Value of X3`

        Args:
            value (float): value for IDD Field `Minimum Value of X3`
                Units are based on field `A10`
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
                                 ' for field `TableMultiVariableLookup.minimum_value_of_x3`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X3`

        Args:
            value (float): value for IDD Field `Maximum Value of X3`
                Units are based on field `A10`
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
                                 ' for field `TableMultiVariableLookup.maximum_value_of_x3`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Value of X4`

        Args:
            value (float): value for IDD Field `Minimum Value of X4`
                Units are based on field `A11`
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
                                 ' for field `TableMultiVariableLookup.minimum_value_of_x4`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X4`

        Args:
            value (float): value for IDD Field `Maximum Value of X4`
                Units are based on field `A11`
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
                                 ' for field `TableMultiVariableLookup.maximum_value_of_x4`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Value of X5`

        Args:
            value (float): value for IDD Field `Minimum Value of X5`
                Units are based on field `A12`
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
                                 ' for field `TableMultiVariableLookup.minimum_value_of_x5`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Value of X5`

        Args:
            value (float): value for IDD Field `Maximum Value of X5`
                Units are based on field `A12`
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
                                 ' for field `TableMultiVariableLookup.maximum_value_of_x5`'.format(value))
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
        """  Corresponds to IDD Field `Minimum Table Output`
        Specify the minimum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Minimum Table Output`
                Units are based on field `A13`
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
                                 ' for field `TableMultiVariableLookup.minimum_table_output`'.format(value))
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
        """  Corresponds to IDD Field `Maximum Table Output`
        Specify the maximum value calculated by this curve object

        Args:
            value (float): value for IDD Field `Maximum Table Output`
                Units are based on field `A13`
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
                                 ' for field `TableMultiVariableLookup.maximum_table_output`'.format(value))
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
        """  Corresponds to IDD Field `Input Unit Type for X1`

        Args:
            value (str): value for IDD Field `Input Unit Type for X1`
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.input_unit_type_for_x1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x1`')
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
                                     'field `TableMultiVariableLookup.input_unit_type_for_x1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.input_unit_type_for_x1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for X2`

        Args:
            value (str): value for IDD Field `Input Unit Type for X2`
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.input_unit_type_for_x2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x2`')
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
                                     'field `TableMultiVariableLookup.input_unit_type_for_x2`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.input_unit_type_for_x2`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for X3`

        Args:
            value (str): value for IDD Field `Input Unit Type for X3`
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.input_unit_type_for_x3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x3`')
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
                                     'field `TableMultiVariableLookup.input_unit_type_for_x3`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.input_unit_type_for_x3`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for X4`

        Args:
            value (str): value for IDD Field `Input Unit Type for X4`
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.input_unit_type_for_x4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x4`')
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
                                     'field `TableMultiVariableLookup.input_unit_type_for_x4`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.input_unit_type_for_x4`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Input Unit Type for X5`

        Args:
            value (str): value for IDD Field `Input Unit Type for X5`
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.input_unit_type_for_x5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.input_unit_type_for_x5`')
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
                                     'field `TableMultiVariableLookup.input_unit_type_for_x5`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.input_unit_type_for_x5`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
                raise ValueError('value {} need to be of type str'
                                 ' for field `TableMultiVariableLookup.output_unit_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `TableMultiVariableLookup.output_unit_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `TableMultiVariableLookup.output_unit_type`')
            vals = {}
            vals["dimensionless"] = "Dimensionless"
            vals["capacity"] = "Capacity"
            vals["power"] = "Power"
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
                                     'field `TableMultiVariableLookup.output_unit_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `TableMultiVariableLookup.output_unit_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Number of Independent Variables`

        Args:
            value (int): value for IDD Field `Number of Independent Variables`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `TableMultiVariableLookup.number_of_independent_variables`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `TableMultiVariableLookup.number_of_independent_variables`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `TableMultiVariableLookup.number_of_independent_variables`')
            if value > 5:
                raise ValueError('value need to be smaller 5 '
                                 'for field `TableMultiVariableLookup.number_of_independent_variables`')
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
        """  Corresponds to IDD Field `Number of Values for Independent Variable X1`

        Args:
            value (int): value for IDD Field `Number of Values for Independent Variable X1`
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
                                     'for field `TableMultiVariableLookup.number_of_values_for_independent_variable_x1`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `TableMultiVariableLookup.number_of_values_for_independent_variable_x1`'.format(value))
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
        """  Corresponds to IDD Field `Field 1 Determined by the Number of Independent Variables`

        Args:
            value (float): value for IDD Field `Field 1 Determined by the Number of Independent Variables`
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
                                 ' for field `TableMultiVariableLookup.field_1_determined_by_the_number_of_independent_variables`'.format(value))
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
        """  Corresponds to IDD Field `Field 2 Determined by the Number of Independent Variables`

        Args:
            value (float): value for IDD Field `Field 2 Determined by the Number of Independent Variables`
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
                                 ' for field `TableMultiVariableLookup.field_2_determined_by_the_number_of_independent_variables`'.format(value))
        self._data["Field 2 Determined by the Number of Independent Variables"] = value

    def add_extensible(self,
                       field_3_determined_by_the_number_of_independent_variables=None,
                       v1=None,
                       v2=None,
                       v3=None,
                       v4=None,
                       v5=None,
                       v6=None,
                       v7=None,
                       v8=None,
                       v9=None,
                       v10=None,
                       v11=None,
                       v12=None,
                       v13=None,
                       v14=None,
                       v15=None,
                       v16=None,
                       v17=None,
                       v18=None,
                       v19=None,
                       ):
        """ Add values for extensible fields

        Args:

            field_3_determined_by_the_number_of_independent_variables (float): value for IDD Field `Field 3 Determined by the Number of Independent Variables`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v1 (float): value for IDD Field `V1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v2 (float): value for IDD Field `V2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v3 (float): value for IDD Field `V3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v4 (float): value for IDD Field `V4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v5 (float): value for IDD Field `V5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v6 (float): value for IDD Field `V6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v7 (float): value for IDD Field `V7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v8 (float): value for IDD Field `V8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v9 (float): value for IDD Field `V9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v10 (float): value for IDD Field `V10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v11 (float): value for IDD Field `V11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v12 (float): value for IDD Field `V12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v13 (float): value for IDD Field `V13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v14 (float): value for IDD Field `V14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v15 (float): value for IDD Field `V15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v16 (float): value for IDD Field `V16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v17 (float): value for IDD Field `V17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v18 (float): value for IDD Field `V18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            v19 (float): value for IDD Field `V19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_field_3_determined_by_the_number_of_independent_variables(field_3_determined_by_the_number_of_independent_variables))
        vals.append(self._check_v1(v1))
        vals.append(self._check_v2(v2))
        vals.append(self._check_v3(v3))
        vals.append(self._check_v4(v4))
        vals.append(self._check_v5(v5))
        vals.append(self._check_v6(v6))
        vals.append(self._check_v7(v7))
        vals.append(self._check_v8(v8))
        vals.append(self._check_v9(v9))
        vals.append(self._check_v10(v10))
        vals.append(self._check_v11(v11))
        vals.append(self._check_v12(v12))
        vals.append(self._check_v13(v13))
        vals.append(self._check_v14(v14))
        vals.append(self._check_v15(v15))
        vals.append(self._check_v16(v16))
        vals.append(self._check_v17(v17))
        vals.append(self._check_v18(v18))
        vals.append(self._check_v19(v19))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_field_3_determined_by_the_number_of_independent_variables(self, value):
        """ Validates falue of field `Field 3 Determined by the Number of Independent Variables`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.field_3_determined_by_the_number_of_independent_variables`'.format(value))
        return value

    def _check_v1(self, value):
        """ Validates falue of field `V1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v1`'.format(value))
        return value

    def _check_v2(self, value):
        """ Validates falue of field `V2`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v2`'.format(value))
        return value

    def _check_v3(self, value):
        """ Validates falue of field `V3`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v3`'.format(value))
        return value

    def _check_v4(self, value):
        """ Validates falue of field `V4`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v4`'.format(value))
        return value

    def _check_v5(self, value):
        """ Validates falue of field `V5`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v5`'.format(value))
        return value

    def _check_v6(self, value):
        """ Validates falue of field `V6`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v6`'.format(value))
        return value

    def _check_v7(self, value):
        """ Validates falue of field `V7`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v7`'.format(value))
        return value

    def _check_v8(self, value):
        """ Validates falue of field `V8`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v8`'.format(value))
        return value

    def _check_v9(self, value):
        """ Validates falue of field `V9`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v9`'.format(value))
        return value

    def _check_v10(self, value):
        """ Validates falue of field `V10`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v10`'.format(value))
        return value

    def _check_v11(self, value):
        """ Validates falue of field `V11`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v11`'.format(value))
        return value

    def _check_v12(self, value):
        """ Validates falue of field `V12`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v12`'.format(value))
        return value

    def _check_v13(self, value):
        """ Validates falue of field `V13`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v13`'.format(value))
        return value

    def _check_v14(self, value):
        """ Validates falue of field `V14`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v14`'.format(value))
        return value

    def _check_v15(self, value):
        """ Validates falue of field `V15`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v15`'.format(value))
        return value

    def _check_v16(self, value):
        """ Validates falue of field `V16`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v16`'.format(value))
        return value

    def _check_v17(self, value):
        """ Validates falue of field `V17`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v17`'.format(value))
        return value

    def _check_v18(self, value):
        """ Validates falue of field `V18`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v18`'.format(value))
        return value

    def _check_v19(self, value):
        """ Validates falue of field `V19`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `TableMultiVariableLookup.v19`'.format(value))
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
                    raise ValueError("Required field TableMultiVariableLookup:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field TableMultiVariableLookup:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for TableMultiVariableLookup: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for TableMultiVariableLookup: {} / {}".format(out_fields,
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