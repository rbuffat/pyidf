""" Data objects in group "Performance Tables"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class TableOneIndependentVariable(DataObject):

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
    _schema = {'extensible-fields': OrderedDict([(u'x value #1',
                                                  {'name': u'X Value #1',
                                                   'pyname': u'x_value_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'}),
                                                 (u'output value #1',
                                                  {'name': u'Output Value #1',
                                                   'pyname': u'output_value_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'curve type',
                                       {'name': u'Curve Type',
                                        'pyname': u'curve_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Linear',
                                                            u'Quadratic',
                                                            u'Cubic',
                                                            u'Quartic',
                                                            u'Exponent'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'interpolation method',
                                       {'name': u'Interpolation Method',
                                        'pyname': u'interpolation_method',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LinearInterpolationOfTable',
                                                            u'EvaluateCurveToLimits',
                                                            u'LagrangeInterpolationLinearExtrapolation'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of X',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of X',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum table output',
                                       {'name': u'Minimum Table Output',
                                        'pyname': u'minimum_table_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum table output',
                                       {'name': u'Maximum Table Output',
                                        'pyname': u'maximum_table_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for X',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Capacity',
                                                            u'Power'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'normalization reference',
                                       {'name': u'Normalization Reference',
                                        'pyname': u'normalization_reference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Performance Tables',
               'min-fields': 14,
               'name': u'Table:OneIndependentVariable',
               'pyname': u'TableOneIndependentVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def curve_type(self):
        """field `Curve Type`

        Args:
            value (str): value for IDD Field `Curve Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `curve_type` or None if not set

        """
        return self["Curve Type"]

    @curve_type.setter
    def curve_type(self, value=None):
        """Corresponds to IDD field `Curve Type`"""
        self["Curve Type"] = value

    @property
    def interpolation_method(self):
        """field `Interpolation Method`

        Args:
            value (str): value for IDD Field `Interpolation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `interpolation_method` or None if not set

        """
        return self["Interpolation Method"]

    @interpolation_method.setter
    def interpolation_method(self, value=None):
        """Corresponds to IDD field `Interpolation Method`"""
        self["Interpolation Method"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of X`

        |  used only when Interpolation Type is Evaluate Curve
        |  to Limits
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Value of X`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of X"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of X`"""
        self["Minimum Value of X"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of X`

        |  used only when Interpolation Type is Evaluate Curve
        |  to Limits
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Value of X`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of X"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of X`"""
        self["Maximum Value of X"] = value

    @property
    def minimum_table_output(self):
        """field `Minimum Table Output`

        |  Specify the minimum value calculated by this table
        |  lookup object
        |  used only when Interpolation Type is Evaluate Curve
        |  to Limits
        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Minimum Table Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_table_output` or None if not set

        """
        return self["Minimum Table Output"]

    @minimum_table_output.setter
    def minimum_table_output(self, value=None):
        """Corresponds to IDD field `Minimum Table Output`"""
        self["Minimum Table Output"] = value

    @property
    def maximum_table_output(self):
        """field `Maximum Table Output`

        |  Specify the maximum value calculated by this table
        |  lookup object
        |  used only when Interpolation Type is Evaluate Curve
        |  to Limits
        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Maximum Table Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_table_output` or None if not set

        """
        return self["Maximum Table Output"]

    @maximum_table_output.setter
    def maximum_table_output(self, value=None):
        """Corresponds to IDD field `Maximum Table Output`"""
        self["Maximum Table Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for X`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X`"""
        self["Input Unit Type for X"] = value

    @property
    def output_unit_type(self):
        """field `Output Unit Type`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Output Unit Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `output_unit_type` or None if not set

        """
        return self["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """Corresponds to IDD field `Output Unit Type`"""
        self["Output Unit Type"] = value

    @property
    def normalization_reference(self):
        """field `Normalization Reference`

        |  This field is used to normalize the following ouput data.
        |  The minimum and maximum table output fields are also normalized.
        |  If this field is blank or 1, the table data presented
        |  in the following fields will be used with normalization
        |  reference set to 1.

        Args:
            value (float): value for IDD Field `Normalization Reference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `normalization_reference` or None if not set

        """
        return self["Normalization Reference"]

    @normalization_reference.setter
    def normalization_reference(self, value=None):
        """Corresponds to IDD field `Normalization Reference`"""
        self["Normalization Reference"] = value

    def add_extensible(self,
                       x_value_1=None,
                       output_value_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            x_value_1 (float): value for IDD Field `X Value #1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_value_1 (float): value for IDD Field `Output Value #1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        x_value_1 = self.check_value("X Value #1", x_value_1)
        vals.append(x_value_1)
        output_value_1 = self.check_value("Output Value #1", output_value_1)
        vals.append(output_value_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class TableTwoIndependentVariables(DataObject):

    """ Corresponds to IDD object `Table:TwoIndependentVariables`
        Allows entry of tabular data pairs as alternate input
        for performance curve objects.
        Performance curve objects can be created using these inputs.
        BiQuadratic Table Equation: Output = a + bX + cX**2 + dY + eY**2 + fXY
        BiQuadratic solution requires a minimum of 6 data pairs
        QuadraticLinear Table Equation: Output = a + bX + cX**2 + dY + eXY + fX**2Y
        QuadraticLinear solution requires a minimum of 6 data pairs
    """
    _schema = {'extensible-fields': OrderedDict([(u'x value #1',
                                                  {'name': u'X Value #1',
                                                   'pyname': u'x_value_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'}),
                                                 (u'y value #1',
                                                  {'name': u'Y Value #1',
                                                   'pyname': u'y_value_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'}),
                                                 (u'output value #1',
                                                  {'name': u'Output Value #1',
                                                   'pyname': u'output_value_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'real'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'curve type',
                                       {'name': u'Curve Type',
                                        'pyname': u'curve_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'BiQuadratic',
                                                            u'QuadraticLinear'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'interpolation method',
                                       {'name': u'Interpolation Method',
                                        'pyname': u'interpolation_method',
                                        'default': u'LagrangeInterpolationLinearExtrapolation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LinearInterpolationOfTable',
                                                            u'EvaluateCurveToLimits',
                                                            u'LagrangeInterpolationLinearExtrapolation'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of X',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of X',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of Y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of Y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum table output',
                                       {'name': u'Minimum Table Output',
                                        'pyname': u'minimum_table_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum table output',
                                       {'name': u'Maximum Table Output',
                                        'pyname': u'maximum_table_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for X',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for y',
                                       {'name': u'Input Unit Type for Y',
                                        'pyname': u'input_unit_type_for_y',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Capacity',
                                                            u'Power'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'normalization reference',
                                       {'name': u'Normalization Reference',
                                        'pyname': u'normalization_reference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Performance Tables',
               'min-fields': 22,
               'name': u'Table:TwoIndependentVariables',
               'pyname': u'TableTwoIndependentVariables',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def curve_type(self):
        """field `Curve Type`

        Args:
            value (str): value for IDD Field `Curve Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `curve_type` or None if not set

        """
        return self["Curve Type"]

    @curve_type.setter
    def curve_type(self, value=None):
        """Corresponds to IDD field `Curve Type`"""
        self["Curve Type"] = value

    @property
    def interpolation_method(self):
        """field `Interpolation Method`

        |  Default value: LagrangeInterpolationLinearExtrapolation

        Args:
            value (str): value for IDD Field `Interpolation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `interpolation_method` or None if not set

        """
        return self["Interpolation Method"]

    @interpolation_method.setter
    def interpolation_method(
            self,
            value="LagrangeInterpolationLinearExtrapolation"):
        """Corresponds to IDD field `Interpolation Method`"""
        self["Interpolation Method"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of X`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Value of X`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of X"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of X`"""
        self["Minimum Value of X"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of X`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Value of X`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of X"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of X`"""
        self["Maximum Value of X"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of Y`

        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Minimum Value of Y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of Y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of Y`"""
        self["Minimum Value of Y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of Y`

        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Maximum Value of Y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of Y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of Y`"""
        self["Maximum Value of Y"] = value

    @property
    def minimum_table_output(self):
        """field `Minimum Table Output`

        |  Specify the minimum value calculated by this table lookup object
        |  Units are based on field `A6`

        Args:
            value (float): value for IDD Field `Minimum Table Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_table_output` or None if not set

        """
        return self["Minimum Table Output"]

    @minimum_table_output.setter
    def minimum_table_output(self, value=None):
        """Corresponds to IDD field `Minimum Table Output`"""
        self["Minimum Table Output"] = value

    @property
    def maximum_table_output(self):
        """field `Maximum Table Output`

        |  Specify the maximum value calculated by this table lookup object
        |  Units are based on field `A6`

        Args:
            value (float): value for IDD Field `Maximum Table Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_table_output` or None if not set

        """
        return self["Maximum Table Output"]

    @maximum_table_output.setter
    def maximum_table_output(self, value=None):
        """Corresponds to IDD field `Maximum Table Output`"""
        self["Maximum Table Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for X`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for X"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X`"""
        self["Input Unit Type for X"] = value

    @property
    def input_unit_type_for_y(self):
        """field `Input Unit Type for Y`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for Y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_y` or None if not set

        """
        return self["Input Unit Type for Y"]

    @input_unit_type_for_y.setter
    def input_unit_type_for_y(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for Y`"""
        self["Input Unit Type for Y"] = value

    @property
    def output_unit_type(self):
        """field `Output Unit Type`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Output Unit Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `output_unit_type` or None if not set

        """
        return self["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """Corresponds to IDD field `Output Unit Type`"""
        self["Output Unit Type"] = value

    @property
    def normalization_reference(self):
        """field `Normalization Reference`

        |  This field is used to normalize the following output data.
        |  The minimum and maximum table output fields are also normalized.
        |  If this field is blank or 1, the table data presented below will be used.

        Args:
            value (float): value for IDD Field `Normalization Reference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `normalization_reference` or None if not set

        """
        return self["Normalization Reference"]

    @normalization_reference.setter
    def normalization_reference(self, value=None):
        """Corresponds to IDD field `Normalization Reference`"""
        self["Normalization Reference"] = value

    def add_extensible(self,
                       x_value_1=None,
                       y_value_1=None,
                       output_value_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            x_value_1 (float): value for IDD Field `X Value #1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            y_value_1 (float): value for IDD Field `Y Value #1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_value_1 (float): value for IDD Field `Output Value #1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        x_value_1 = self.check_value("X Value #1", x_value_1)
        vals.append(x_value_1)
        y_value_1 = self.check_value("Y Value #1", y_value_1)
        vals.append(y_value_1)
        output_value_1 = self.check_value("Output Value #1", output_value_1)
        vals.append(output_value_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class TableMultiVariableLookup(DataObject):

    """ Corresponds to IDD object `Table:MultiVariableLookup`
        The multi-variable lookup table can represent from 1 to 5 independent variables and
        can interpolate these independent variables up to a 4th order polynomial. The
        polynomial order is assumed to be the number of interpolation points (n) minus 1.
        When any independent variable value is outside the table limits, linear extrapolation
        is used to predict the table result and is based on the two nearest data points in the
        table for that particular independent variable.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'interpolation method',
                                       {'name': u'Interpolation Method',
                                        'pyname': u'interpolation_method',
                                        'default': u'LagrangeInterpolationLinearExtrapolation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LinearInterpolationOfTable',
                                                            u'EvaluateCurveToLimits',
                                                            u'LagrangeInterpolationLinearExtrapolation'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'number of interpolation points',
                                       {'name': u'Number of Interpolation Points',
                                        'pyname': u'number_of_interpolation_points',
                                        'default': 3,
                                        'minimum>': 1,
                                        'maximum': 4,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'curve type',
                                       {'name': u'Curve Type',
                                        'pyname': u'curve_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Linear',
                                                            u'Quadratic',
                                                            u'Cubic',
                                                            u'Quartic',
                                                            u'Exponent',
                                                            u'BiQuadratic',
                                                            u'QuadraticLinear',
                                                            u'BiCubic',
                                                            u'TriQuadratic',
                                                            u'Other'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'table data format',
                                       {'name': u'Table Data Format',
                                        'pyname': u'table_data_format',
                                        'default': u'SingleLineIndependentVariableWithMatrix',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SingleLineIndependentVariableWithMatrix'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'external file name',
                                       {'name': u'External File Name',
                                        'pyname': u'external_file_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'x1 sort order',
                                       {'name': u'X1 Sort Order',
                                        'pyname': u'x1_sort_order',
                                        'default': u'Ascending',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Ascending',
                                                            u'Descending'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'x2 sort order',
                                       {'name': u'X2 Sort Order',
                                        'pyname': u'x2_sort_order',
                                        'default': u'Ascending',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Ascending',
                                                            u'Descending'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'normalization reference',
                                       {'name': u'Normalization Reference',
                                        'pyname': u'normalization_reference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x1',
                                       {'name': u'Minimum Value of X1',
                                        'pyname': u'minimum_value_of_x1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x1',
                                       {'name': u'Maximum Value of X1',
                                        'pyname': u'maximum_value_of_x1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x2',
                                       {'name': u'Minimum Value of X2',
                                        'pyname': u'minimum_value_of_x2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x2',
                                       {'name': u'Maximum Value of X2',
                                        'pyname': u'maximum_value_of_x2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x3',
                                       {'name': u'Minimum Value of X3',
                                        'pyname': u'minimum_value_of_x3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x3',
                                       {'name': u'Maximum Value of X3',
                                        'pyname': u'maximum_value_of_x3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x4',
                                       {'name': u'Minimum Value of X4',
                                        'pyname': u'minimum_value_of_x4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x4',
                                       {'name': u'Maximum Value of X4',
                                        'pyname': u'maximum_value_of_x4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x5',
                                       {'name': u'Minimum Value of X5',
                                        'pyname': u'minimum_value_of_x5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x5',
                                       {'name': u'Maximum Value of X5',
                                        'pyname': u'maximum_value_of_x5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum table output',
                                       {'name': u'Minimum Table Output',
                                        'pyname': u'minimum_table_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum table output',
                                       {'name': u'Maximum Table Output',
                                        'pyname': u'maximum_table_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x1',
                                       {'name': u'Input Unit Type for X1',
                                        'pyname': u'input_unit_type_for_x1',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for x2',
                                       {'name': u'Input Unit Type for X2',
                                        'pyname': u'input_unit_type_for_x2',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for x3',
                                       {'name': u'Input Unit Type for X3',
                                        'pyname': u'input_unit_type_for_x3',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for x4',
                                       {'name': u'Input Unit Type for X4',
                                        'pyname': u'input_unit_type_for_x4',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for x5',
                                       {'name': u'Input Unit Type for X5',
                                        'pyname': u'input_unit_type_for_x5',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Capacity',
                                                            u'Power'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'number of independent variables',
                                       {'name': u'Number of Independent Variables',
                                        'pyname': u'number_of_independent_variables',
                                        'minimum>': 0,
                                        'maximum': 5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of values for independent variable x1',
                                       {'name': u'Number of Values for Independent Variable X1',
                                        'pyname': u'number_of_values_for_independent_variable_x1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'field 1 determined by the number of independent variables',
                                       {'name': u'Field 1 Determined by the Number of Independent Variables',
                                        'pyname': u'field_1_determined_by_the_number_of_independent_variables',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'field 2 determined by the number of independent variables',
                                       {'name': u'Field 2 Determined by the Number of Independent Variables',
                                        'pyname': u'field_2_determined_by_the_number_of_independent_variables',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Performance Tables',
               'min-fields': 27,
               'name': u'Table:MultiVariableLookup',
               'pyname': u'TableMultiVariableLookup',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def interpolation_method(self):
        """field `Interpolation Method`

        |  Default value: LagrangeInterpolationLinearExtrapolation

        Args:
            value (str): value for IDD Field `Interpolation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `interpolation_method` or None if not set

        """
        return self["Interpolation Method"]

    @interpolation_method.setter
    def interpolation_method(
            self,
            value="LagrangeInterpolationLinearExtrapolation"):
        """Corresponds to IDD field `Interpolation Method`"""
        self["Interpolation Method"] = value

    @property
    def number_of_interpolation_points(self):
        """field `Number of Interpolation Points`

        |  Default value: 3
        |  value > 1
        |  value <= 4

        Args:
            value (int): value for IDD Field `Number of Interpolation Points`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_interpolation_points` or None if not set

        """
        return self["Number of Interpolation Points"]

    @number_of_interpolation_points.setter
    def number_of_interpolation_points(self, value=3):
        """Corresponds to IDD field `Number of Interpolation Points`"""
        self["Number of Interpolation Points"] = value

    @property
    def curve_type(self):
        """field `Curve Type`

        |  The curve types BiCubic and TriQuadratic may not
        |  be used with Interpolation Method = EvaluateCurveToLimits

        Args:
            value (str): value for IDD Field `Curve Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `curve_type` or None if not set

        """
        return self["Curve Type"]

    @curve_type.setter
    def curve_type(self, value=None):
        """Corresponds to IDD field `Curve Type`"""
        self["Curve Type"] = value

    @property
    def table_data_format(self):
        """field `Table Data Format`

        |  Default value: SingleLineIndependentVariableWithMatrix

        Args:
            value (str): value for IDD Field `Table Data Format`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `table_data_format` or None if not set

        """
        return self["Table Data Format"]

    @table_data_format.setter
    def table_data_format(
            self,
            value="SingleLineIndependentVariableWithMatrix"):
        """Corresponds to IDD field `Table Data Format`"""
        self["Table Data Format"] = value

    @property
    def external_file_name(self):
        """field `External File Name`

        Args:
            value (str): value for IDD Field `External File Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `external_file_name` or None if not set

        """
        return self["External File Name"]

    @external_file_name.setter
    def external_file_name(self, value=None):
        """Corresponds to IDD field `External File Name`"""
        self["External File Name"] = value

    @property
    def x1_sort_order(self):
        """field `X1 Sort Order`

        |  Default value: Ascending

        Args:
            value (str): value for IDD Field `X1 Sort Order`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `x1_sort_order` or None if not set

        """
        return self["X1 Sort Order"]

    @x1_sort_order.setter
    def x1_sort_order(self, value="Ascending"):
        """Corresponds to IDD field `X1 Sort Order`"""
        self["X1 Sort Order"] = value

    @property
    def x2_sort_order(self):
        """field `X2 Sort Order`

        |  Default value: Ascending

        Args:
            value (str): value for IDD Field `X2 Sort Order`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `x2_sort_order` or None if not set

        """
        return self["X2 Sort Order"]

    @x2_sort_order.setter
    def x2_sort_order(self, value="Ascending"):
        """Corresponds to IDD field `X2 Sort Order`"""
        self["X2 Sort Order"] = value

    @property
    def normalization_reference(self):
        """field `Normalization Reference`

        |  This field is used to normalize the table output data.
        |  The minimum and maximum table output fields are also normalized.
        |  If this field is blank or 1, the table data will be directly used.
        |  This field is not allowed to be set equal to 0.

        Args:
            value (float): value for IDD Field `Normalization Reference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `normalization_reference` or None if not set

        """
        return self["Normalization Reference"]

    @normalization_reference.setter
    def normalization_reference(self, value=None):
        """Corresponds to IDD field `Normalization Reference`"""
        self["Normalization Reference"] = value

    @property
    def minimum_value_of_x1(self):
        """field `Minimum Value of X1`

        |  Units are based on field `A8`

        Args:
            value (float): value for IDD Field `Minimum Value of X1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x1` or None if not set

        """
        return self["Minimum Value of X1"]

    @minimum_value_of_x1.setter
    def minimum_value_of_x1(self, value=None):
        """Corresponds to IDD field `Minimum Value of X1`"""
        self["Minimum Value of X1"] = value

    @property
    def maximum_value_of_x1(self):
        """field `Maximum Value of X1`

        |  Units are based on field `A8`

        Args:
            value (float): value for IDD Field `Maximum Value of X1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x1` or None if not set

        """
        return self["Maximum Value of X1"]

    @maximum_value_of_x1.setter
    def maximum_value_of_x1(self, value=None):
        """Corresponds to IDD field `Maximum Value of X1`"""
        self["Maximum Value of X1"] = value

    @property
    def minimum_value_of_x2(self):
        """field `Minimum Value of X2`

        |  Units are based on field `A9`

        Args:
            value (float): value for IDD Field `Minimum Value of X2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x2` or None if not set

        """
        return self["Minimum Value of X2"]

    @minimum_value_of_x2.setter
    def minimum_value_of_x2(self, value=None):
        """Corresponds to IDD field `Minimum Value of X2`"""
        self["Minimum Value of X2"] = value

    @property
    def maximum_value_of_x2(self):
        """field `Maximum Value of X2`

        |  Units are based on field `A9`

        Args:
            value (float): value for IDD Field `Maximum Value of X2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x2` or None if not set

        """
        return self["Maximum Value of X2"]

    @maximum_value_of_x2.setter
    def maximum_value_of_x2(self, value=None):
        """Corresponds to IDD field `Maximum Value of X2`"""
        self["Maximum Value of X2"] = value

    @property
    def minimum_value_of_x3(self):
        """field `Minimum Value of X3`

        |  Units are based on field `A10`

        Args:
            value (float): value for IDD Field `Minimum Value of X3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x3` or None if not set

        """
        return self["Minimum Value of X3"]

    @minimum_value_of_x3.setter
    def minimum_value_of_x3(self, value=None):
        """Corresponds to IDD field `Minimum Value of X3`"""
        self["Minimum Value of X3"] = value

    @property
    def maximum_value_of_x3(self):
        """field `Maximum Value of X3`

        |  Units are based on field `A10`

        Args:
            value (float): value for IDD Field `Maximum Value of X3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x3` or None if not set

        """
        return self["Maximum Value of X3"]

    @maximum_value_of_x3.setter
    def maximum_value_of_x3(self, value=None):
        """Corresponds to IDD field `Maximum Value of X3`"""
        self["Maximum Value of X3"] = value

    @property
    def minimum_value_of_x4(self):
        """field `Minimum Value of X4`

        |  Units are based on field `A11`

        Args:
            value (float): value for IDD Field `Minimum Value of X4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x4` or None if not set

        """
        return self["Minimum Value of X4"]

    @minimum_value_of_x4.setter
    def minimum_value_of_x4(self, value=None):
        """Corresponds to IDD field `Minimum Value of X4`"""
        self["Minimum Value of X4"] = value

    @property
    def maximum_value_of_x4(self):
        """field `Maximum Value of X4`

        |  Units are based on field `A11`

        Args:
            value (float): value for IDD Field `Maximum Value of X4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x4` or None if not set

        """
        return self["Maximum Value of X4"]

    @maximum_value_of_x4.setter
    def maximum_value_of_x4(self, value=None):
        """Corresponds to IDD field `Maximum Value of X4`"""
        self["Maximum Value of X4"] = value

    @property
    def minimum_value_of_x5(self):
        """field `Minimum Value of X5`

        |  Units are based on field `A12`

        Args:
            value (float): value for IDD Field `Minimum Value of X5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x5` or None if not set

        """
        return self["Minimum Value of X5"]

    @minimum_value_of_x5.setter
    def minimum_value_of_x5(self, value=None):
        """Corresponds to IDD field `Minimum Value of X5`"""
        self["Minimum Value of X5"] = value

    @property
    def maximum_value_of_x5(self):
        """field `Maximum Value of X5`

        |  Units are based on field `A12`

        Args:
            value (float): value for IDD Field `Maximum Value of X5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x5` or None if not set

        """
        return self["Maximum Value of X5"]

    @maximum_value_of_x5.setter
    def maximum_value_of_x5(self, value=None):
        """Corresponds to IDD field `Maximum Value of X5`"""
        self["Maximum Value of X5"] = value

    @property
    def minimum_table_output(self):
        """field `Minimum Table Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A13`

        Args:
            value (float): value for IDD Field `Minimum Table Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_table_output` or None if not set

        """
        return self["Minimum Table Output"]

    @minimum_table_output.setter
    def minimum_table_output(self, value=None):
        """Corresponds to IDD field `Minimum Table Output`"""
        self["Minimum Table Output"] = value

    @property
    def maximum_table_output(self):
        """field `Maximum Table Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A13`

        Args:
            value (float): value for IDD Field `Maximum Table Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_table_output` or None if not set

        """
        return self["Maximum Table Output"]

    @maximum_table_output.setter
    def maximum_table_output(self, value=None):
        """Corresponds to IDD field `Maximum Table Output`"""
        self["Maximum Table Output"] = value

    @property
    def input_unit_type_for_x1(self):
        """field `Input Unit Type for X1`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x1` or None if not set

        """
        return self["Input Unit Type for X1"]

    @input_unit_type_for_x1.setter
    def input_unit_type_for_x1(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X1`"""
        self["Input Unit Type for X1"] = value

    @property
    def input_unit_type_for_x2(self):
        """field `Input Unit Type for X2`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x2` or None if not set

        """
        return self["Input Unit Type for X2"]

    @input_unit_type_for_x2.setter
    def input_unit_type_for_x2(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X2`"""
        self["Input Unit Type for X2"] = value

    @property
    def input_unit_type_for_x3(self):
        """field `Input Unit Type for X3`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x3` or None if not set

        """
        return self["Input Unit Type for X3"]

    @input_unit_type_for_x3.setter
    def input_unit_type_for_x3(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X3`"""
        self["Input Unit Type for X3"] = value

    @property
    def input_unit_type_for_x4(self):
        """field `Input Unit Type for X4`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x4` or None if not set

        """
        return self["Input Unit Type for X4"]

    @input_unit_type_for_x4.setter
    def input_unit_type_for_x4(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X4`"""
        self["Input Unit Type for X4"] = value

    @property
    def input_unit_type_for_x5(self):
        """field `Input Unit Type for X5`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for X5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x5` or None if not set

        """
        return self["Input Unit Type for X5"]

    @input_unit_type_for_x5.setter
    def input_unit_type_for_x5(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for X5`"""
        self["Input Unit Type for X5"] = value

    @property
    def output_unit_type(self):
        """field `Output Unit Type`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Output Unit Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `output_unit_type` or None if not set

        """
        return self["Output Unit Type"]

    @output_unit_type.setter
    def output_unit_type(self, value="Dimensionless"):
        """Corresponds to IDD field `Output Unit Type`"""
        self["Output Unit Type"] = value

    @property
    def number_of_independent_variables(self):
        """field `Number of Independent Variables`

        |  value <= 5

        Args:
            value (int): value for IDD Field `Number of Independent Variables`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_independent_variables` or None if not set

        """
        return self["Number of Independent Variables"]

    @number_of_independent_variables.setter
    def number_of_independent_variables(self, value=None):
        """Corresponds to IDD field `Number of Independent Variables`"""
        self["Number of Independent Variables"] = value

    @property
    def number_of_values_for_independent_variable_x1(self):
        """field `Number of Values for Independent Variable X1`

        Args:
            value (int): value for IDD Field `Number of Values for Independent Variable X1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_values_for_independent_variable_x1` or None if not set

        """
        return self["Number of Values for Independent Variable X1"]

    @number_of_values_for_independent_variable_x1.setter
    def number_of_values_for_independent_variable_x1(self, value=None):
        """Corresponds to IDD field `Number of Values for Independent Variable
        X1`"""
        self["Number of Values for Independent Variable X1"] = value

    @property
    def field_1_determined_by_the_number_of_independent_variables(self):
        """field `Field 1 Determined by the Number of Independent Variables`

        Args:
            value (float): value for IDD Field `Field 1 Determined by the Number of Independent Variables`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `field_1_determined_by_the_number_of_independent_variables` or None if not set

        """
        return self[
            "Field 1 Determined by the Number of Independent Variables"]

    @field_1_determined_by_the_number_of_independent_variables.setter
    def field_1_determined_by_the_number_of_independent_variables(
            self,
            value=None):
        """Corresponds to IDD field `Field 1 Determined by the Number of
        Independent Variables`"""
        self[
            "Field 1 Determined by the Number of Independent Variables"] = value

    @property
    def field_2_determined_by_the_number_of_independent_variables(self):
        """field `Field 2 Determined by the Number of Independent Variables`

        Args:
            value (float): value for IDD Field `Field 2 Determined by the Number of Independent Variables`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `field_2_determined_by_the_number_of_independent_variables` or None if not set

        """
        return self[
            "Field 2 Determined by the Number of Independent Variables"]

    @field_2_determined_by_the_number_of_independent_variables.setter
    def field_2_determined_by_the_number_of_independent_variables(
            self,
            value=None):
        """Corresponds to IDD field `Field 2 Determined by the Number of
        Independent Variables`"""
        self[
            "Field 2 Determined by the Number of Independent Variables"] = value


