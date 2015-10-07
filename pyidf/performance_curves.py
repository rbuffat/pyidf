""" Data objects in group "Performance Curves"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class CurveLinear(DataObject):

    """ Corresponds to IDD object `Curve:Linear`
        Linear curve with one independent variable.
        Input for the linear curve consists of a curve name, the two coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for
        curve minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                                            u'Pressure',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Linear',
               'pyname': u'CurveLinear',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveQuadLinear(DataObject):

    """ Corresponds to IDD object `Curve:QuadLinear`
        Linear curve with four independent variables.
        Input for the linear curve consists of a curve name, the two coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*w + C3*x + C4*y + C5*z
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 w',
                                       {'name': u'Coefficient2 w',
                                        'pyname': u'coefficient2_w',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x',
                                       {'name': u'Coefficient3 x',
                                        'pyname': u'coefficient3_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 y',
                                       {'name': u'Coefficient4 y',
                                        'pyname': u'coefficient4_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 z',
                                       {'name': u'Coefficient5 z',
                                        'pyname': u'coefficient5_z',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of w',
                                       {'name': u'Minimum Value of w',
                                        'pyname': u'minimum_value_of_w',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of w',
                                       {'name': u'Maximum Value of w',
                                        'pyname': u'maximum_value_of_w',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of z',
                                       {'name': u'Minimum Value of z',
                                        'pyname': u'minimum_value_of_z',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of z',
                                       {'name': u'Maximum Value of z',
                                        'pyname': u'maximum_value_of_z',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for w',
                                       {'name': u'Input Unit Type for w',
                                        'pyname': u'input_unit_type_for_w',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance',
                                                            u'VolumetricFlowPerPower'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance',
                                                            u'VolumetricFlowPerPower'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for y',
                                       {'name': u'Input Unit Type for y',
                                        'pyname': u'input_unit_type_for_y',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance',
                                                            u'VolumetricFlowPerPower'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for z',
                                       {'name': u'Input Unit Type for z',
                                        'pyname': u'input_unit_type_for_z',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'MassFlow',
                                                            u'Power',
                                                            u'Distance',
                                                            u'VolumetricFlowPerPower'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:QuadLinear',
               'pyname': u'CurveQuadLinear',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_w(self):
        """field `Coefficient2 w`

        Args:
            value (float): value for IDD Field `Coefficient2 w`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_w` or None if not set

        """
        return self["Coefficient2 w"]

    @coefficient2_w.setter
    def coefficient2_w(self, value=None):
        """Corresponds to IDD field `Coefficient2 w`"""
        self["Coefficient2 w"] = value

    @property
    def coefficient3_x(self):
        """field `Coefficient3 x`

        Args:
            value (float): value for IDD Field `Coefficient3 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x` or None if not set

        """
        return self["Coefficient3 x"]

    @coefficient3_x.setter
    def coefficient3_x(self, value=None):
        """Corresponds to IDD field `Coefficient3 x`"""
        self["Coefficient3 x"] = value

    @property
    def coefficient4_y(self):
        """field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_y` or None if not set

        """
        return self["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """Corresponds to IDD field `Coefficient4 y`"""
        self["Coefficient4 y"] = value

    @property
    def coefficient5_z(self):
        """field `Coefficient5 z`

        Args:
            value (float): value for IDD Field `Coefficient5 z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_z` or None if not set

        """
        return self["Coefficient5 z"]

    @coefficient5_z.setter
    def coefficient5_z(self, value=None):
        """Corresponds to IDD field `Coefficient5 z`"""
        self["Coefficient5 z"] = value

    @property
    def minimum_value_of_w(self):
        """field `Minimum Value of w`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of w`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_w` or None if not set

        """
        return self["Minimum Value of w"]

    @minimum_value_of_w.setter
    def minimum_value_of_w(self, value=None):
        """Corresponds to IDD field `Minimum Value of w`"""
        self["Minimum Value of w"] = value

    @property
    def maximum_value_of_w(self):
        """field `Maximum Value of w`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of w`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_w` or None if not set

        """
        return self["Maximum Value of w"]

    @maximum_value_of_w.setter
    def maximum_value_of_w(self, value=None):
        """Corresponds to IDD field `Maximum Value of w`"""
        self["Maximum Value of w"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_value_of_z(self):
        """field `Minimum Value of z`

        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Minimum Value of z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_z` or None if not set

        """
        return self["Minimum Value of z"]

    @minimum_value_of_z.setter
    def minimum_value_of_z(self, value=None):
        """Corresponds to IDD field `Minimum Value of z`"""
        self["Minimum Value of z"] = value

    @property
    def maximum_value_of_z(self):
        """field `Maximum Value of z`

        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Maximum Value of z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_z` or None if not set

        """
        return self["Maximum Value of z"]

    @maximum_value_of_z.setter
    def maximum_value_of_z(self, value=None):
        """Corresponds to IDD field `Maximum Value of z`"""
        self["Maximum Value of z"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_w(self):
        """field `Input Unit Type for w`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for w`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_w` or None if not set

        """
        return self["Input Unit Type for w"]

    @input_unit_type_for_w.setter
    def input_unit_type_for_w(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for w`"""
        self["Input Unit Type for w"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

    @property
    def input_unit_type_for_y(self):
        """field `Input Unit Type for y`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_y` or None if not set

        """
        return self["Input Unit Type for y"]

    @input_unit_type_for_y.setter
    def input_unit_type_for_y(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for y`"""
        self["Input Unit Type for y"] = value

    @property
    def input_unit_type_for_z(self):
        """field `Input Unit Type for z`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_z` or None if not set

        """
        return self["Input Unit Type for z"]

    @input_unit_type_for_z.setter
    def input_unit_type_for_z(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for z`"""
        self["Input Unit Type for z"] = value




class CurveQuadratic(DataObject):

    """ Corresponds to IDD object `Curve:Quadratic`
        Quadratic curve with one independent variable.
        Input for a quadratic curve consists of the curve name, the three coefficients, and
        the maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Quadratic',
               'pyname': u'CurveQuadratic',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveCubic(DataObject):

    """ Corresponds to IDD object `Curve:Cubic`
        Cubic curve with one independent variable.
        Input for a cubic curve consists of the curve name, the 4 coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*x**3
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 x**3',
                                       {'name': u'Coefficient4 x**3',
                                        'pyname': u'coefficient4_x3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Cubic',
               'pyname': u'CurveCubic',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def coefficient4_x3(self):
        """field `Coefficient4 x**3`


        Args:
            value (float): value for IDD Field `Coefficient4 x**3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_x3` or None if not set
        """
        return self["Coefficient4 x**3"]

    @coefficient4_x3.setter
    def coefficient4_x3(self, value=None):
        """  Corresponds to IDD field `Coefficient4 x**3`

        """
        self["Coefficient4 x**3"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveQuartic(DataObject):

    """ Corresponds to IDD object `Curve:Quartic`
        Quartic (fourth order polynomial) curve with one independent variable.
        Input for a Quartic curve consists of the curve name, the
        five coefficients, and the maximum and minimum valid independent variable values.
        Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*x**3 + C5*x**4
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 x**3',
                                       {'name': u'Coefficient4 x**3',
                                        'pyname': u'coefficient4_x3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 x**4',
                                       {'name': u'Coefficient5 x**4',
                                        'pyname': u'coefficient5_x4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Quartic',
               'pyname': u'CurveQuartic',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def coefficient4_x3(self):
        """field `Coefficient4 x**3`


        Args:
            value (float): value for IDD Field `Coefficient4 x**3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_x3` or None if not set
        """
        return self["Coefficient4 x**3"]

    @coefficient4_x3.setter
    def coefficient4_x3(self, value=None):
        """  Corresponds to IDD field `Coefficient4 x**3`

        """
        self["Coefficient4 x**3"] = value

    @property
    def coefficient5_x4(self):
        """field `Coefficient5 x**4`


        Args:
            value (float): value for IDD Field `Coefficient5 x**4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_x4` or None if not set
        """
        return self["Coefficient5 x**4"]

    @coefficient5_x4.setter
    def coefficient5_x4(self, value=None):
        """  Corresponds to IDD field `Coefficient5 x**4`

        """
        self["Coefficient5 x**4"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveExponent(DataObject):

    """ Corresponds to IDD object `Curve:Exponent`
        Exponent curve with one independent variable.
        Input for a exponent curve consists of the curve name, the 3 coefficients, and the
        maximum and minimum valid independent variable values. Optional inputs for curve
        minimum and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x**C3
        The independent variable x is raised to the C3 power, multiplied by C2, and C1 is added to the result.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 constant',
                                       {'name': u'Coefficient2 Constant',
                                        'pyname': u'coefficient2_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 constant',
                                       {'name': u'Coefficient3 Constant',
                                        'pyname': u'coefficient3_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 6,
               'name': u'Curve:Exponent',
               'pyname': u'CurveExponent',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_constant(self):
        """field `Coefficient2 Constant`

        Args:
            value (float): value for IDD Field `Coefficient2 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_constant` or None if not set

        """
        return self["Coefficient2 Constant"]

    @coefficient2_constant.setter
    def coefficient2_constant(self, value=None):
        """Corresponds to IDD field `Coefficient2 Constant`"""
        self["Coefficient2 Constant"] = value

    @property
    def coefficient3_constant(self):
        """field `Coefficient3 Constant`

        Args:
            value (float): value for IDD Field `Coefficient3 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_constant` or None if not set

        """
        return self["Coefficient3 Constant"]

    @coefficient3_constant.setter
    def coefficient3_constant(self, value=None):
        """Corresponds to IDD field `Coefficient3 Constant`"""
        self["Coefficient3 Constant"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Specify the minimum value of the independent variable x allowed
        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Specify the maximum value of the independent variable x allowed
        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveBicubic(DataObject):

    """ Corresponds to IDD object `Curve:Bicubic`
        Cubic curve with two independent variables. Input consists of the
        curve name, the ten coefficients, and the minimum and maximum values for each of
        the independent variables. Optional inputs for curve minimum and maximum may
        be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3 + C8*y**3 + C9*x**2*y
        + C10*x*y**2
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 y',
                                       {'name': u'Coefficient4 y',
                                        'pyname': u'coefficient4_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 y**2',
                                       {'name': u'Coefficient5 y**2',
                                        'pyname': u'coefficient5_y2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient6 x*y',
                                       {'name': u'Coefficient6 x*y',
                                        'pyname': u'coefficient6_xy',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient7 x**3',
                                       {'name': u'Coefficient7 x**3',
                                        'pyname': u'coefficient7_x3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient8 y**3',
                                       {'name': u'Coefficient8 y**3',
                                        'pyname': u'coefficient8_y3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient9 x**2*y',
                                       {'name': u'Coefficient9 x**2*y',
                                        'pyname': u'coefficient9_x2y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient10 x*y**2',
                                       {'name': u'Coefficient10 x*y**2',
                                        'pyname': u'coefficient10_xy2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Bicubic',
               'pyname': u'CurveBicubic',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def coefficient4_y(self):
        """field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_y` or None if not set

        """
        return self["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """Corresponds to IDD field `Coefficient4 y`"""
        self["Coefficient4 y"] = value

    @property
    def coefficient5_y2(self):
        """field `Coefficient5 y**2`


        Args:
            value (float): value for IDD Field `Coefficient5 y**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_y2` or None if not set
        """
        return self["Coefficient5 y**2"]

    @coefficient5_y2.setter
    def coefficient5_y2(self, value=None):
        """  Corresponds to IDD field `Coefficient5 y**2`

        """
        self["Coefficient5 y**2"] = value

    @property
    def coefficient6_xy(self):
        """field `Coefficient6 x*y`


        Args:
            value (float): value for IDD Field `Coefficient6 x*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient6_xy` or None if not set
        """
        return self["Coefficient6 x*y"]

    @coefficient6_xy.setter
    def coefficient6_xy(self, value=None):
        """  Corresponds to IDD field `Coefficient6 x*y`

        """
        self["Coefficient6 x*y"] = value

    @property
    def coefficient7_x3(self):
        """field `Coefficient7 x**3`


        Args:
            value (float): value for IDD Field `Coefficient7 x**3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient7_x3` or None if not set
        """
        return self["Coefficient7 x**3"]

    @coefficient7_x3.setter
    def coefficient7_x3(self, value=None):
        """  Corresponds to IDD field `Coefficient7 x**3`

        """
        self["Coefficient7 x**3"] = value

    @property
    def coefficient8_y3(self):
        """field `Coefficient8 y**3`


        Args:
            value (float): value for IDD Field `Coefficient8 y**3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient8_y3` or None if not set
        """
        return self["Coefficient8 y**3"]

    @coefficient8_y3.setter
    def coefficient8_y3(self, value=None):
        """  Corresponds to IDD field `Coefficient8 y**3`

        """
        self["Coefficient8 y**3"] = value

    @property
    def coefficient9_x2y(self):
        """field `Coefficient9 x**2*y`


        Args:
            value (float): value for IDD Field `Coefficient9 x**2*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient9_x2y` or None if not set
        """
        return self["Coefficient9 x**2*y"]

    @coefficient9_x2y.setter
    def coefficient9_x2y(self, value=None):
        """  Corresponds to IDD field `Coefficient9 x**2*y`

        """
        self["Coefficient9 x**2*y"] = value

    @property
    def coefficient10_xy2(self):
        """field `Coefficient10 x*y**2`


        Args:
            value (float): value for IDD Field `Coefficient10 x*y**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient10_xy2` or None if not set
        """
        return self["Coefficient10 x*y**2"]

    @coefficient10_xy2.setter
    def coefficient10_xy2(self, value=None):
        """  Corresponds to IDD field `Coefficient10 x*y**2`

        """
        self["Coefficient10 x*y**2"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveBiquadratic(DataObject):

    """ Corresponds to IDD object `Curve:Biquadratic`
        Quadratic curve with two independent variables. Input consists of the curve name, the
        six coefficients, and min and max values for each of the independent variables.
        Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 y',
                                       {'name': u'Coefficient4 y',
                                        'pyname': u'coefficient4_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 y**2',
                                       {'name': u'Coefficient5 y**2',
                                        'pyname': u'coefficient5_y2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient6 x*y',
                                       {'name': u'Coefficient6 x*y',
                                        'pyname': u'coefficient6_xy',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Biquadratic',
               'pyname': u'CurveBiquadratic',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def coefficient4_y(self):
        """field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_y` or None if not set

        """
        return self["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """Corresponds to IDD field `Coefficient4 y`"""
        self["Coefficient4 y"] = value

    @property
    def coefficient5_y2(self):
        """field `Coefficient5 y**2`


        Args:
            value (float): value for IDD Field `Coefficient5 y**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_y2` or None if not set
        """
        return self["Coefficient5 y**2"]

    @coefficient5_y2.setter
    def coefficient5_y2(self, value=None):
        """  Corresponds to IDD field `Coefficient5 y**2`

        """
        self["Coefficient5 y**2"] = value

    @property
    def coefficient6_xy(self):
        """field `Coefficient6 x*y`


        Args:
            value (float): value for IDD Field `Coefficient6 x*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient6_xy` or None if not set
        """
        return self["Coefficient6 x*y"]

    @coefficient6_xy.setter
    def coefficient6_xy(self, value=None):
        """  Corresponds to IDD field `Coefficient6 x*y`

        """
        self["Coefficient6 x*y"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveQuadraticLinear(DataObject):

    """ Corresponds to IDD object `Curve:QuadraticLinear`
        Quadratic-linear curve with two independent variables. Input consists of the curve
        name, the six coefficients, and min and max values for each of the independent
        variables. Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = (C1 + C2*x + C3*x**2) + (C4 + C5*x + C6*x**2)*y
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 y',
                                       {'name': u'Coefficient4 y',
                                        'pyname': u'coefficient4_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 x*y',
                                       {'name': u'Coefficient5 x*y',
                                        'pyname': u'coefficient5_xy',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient6 x**2*y',
                                       {'name': u'Coefficient6 x**2*y',
                                        'pyname': u'coefficient6_x2y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:QuadraticLinear',
               'pyname': u'CurveQuadraticLinear',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def coefficient4_y(self):
        """field `Coefficient4 y`

        Args:
            value (float): value for IDD Field `Coefficient4 y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_y` or None if not set

        """
        return self["Coefficient4 y"]

    @coefficient4_y.setter
    def coefficient4_y(self, value=None):
        """Corresponds to IDD field `Coefficient4 y`"""
        self["Coefficient4 y"] = value

    @property
    def coefficient5_xy(self):
        """field `Coefficient5 x*y`


        Args:
            value (float): value for IDD Field `Coefficient5 x*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_xy` or None if not set
        """
        return self["Coefficient5 x*y"]

    @coefficient5_xy.setter
    def coefficient5_xy(self, value=None):
        """  Corresponds to IDD field `Coefficient5 x*y`

        """
        self["Coefficient5 x*y"] = value

    @property
    def coefficient6_x2y(self):
        """field `Coefficient6 x**2*y`


        Args:
            value (float): value for IDD Field `Coefficient6 x**2*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient6_x2y` or None if not set
        """
        return self["Coefficient6 x**2*y"]

    @coefficient6_x2y.setter
    def coefficient6_x2y(self, value=None):
        """  Corresponds to IDD field `Coefficient6 x**2*y`

        """
        self["Coefficient6 x**2*y"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveCubicLinear(DataObject):

    """ Corresponds to IDD object `Curve:CubicLinear`
        Cubic-linear curve with two independent variables. Input consists of the curve
        name, the six coefficients, and min and max values for each of the independent
        variables. Optional inputs for curve minimum and maximum may be used to limit the
        output of the performance curve.
        curve = (C1 + C2*x + C3*x**2 + C4*x**3) + (C5 + C6*x)*y
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x',
                                       {'name': u'Coefficient2 x',
                                        'pyname': u'coefficient2_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x**2',
                                       {'name': u'Coefficient3 x**2',
                                        'pyname': u'coefficient3_x2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 x**3',
                                       {'name': u'Coefficient4 x**3',
                                        'pyname': u'coefficient4_x3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 y',
                                       {'name': u'Coefficient5 y',
                                        'pyname': u'coefficient5_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient6 x*y',
                                       {'name': u'Coefficient6 x*y',
                                        'pyname': u'coefficient6_xy',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for y',
                                       {'name': u'Input Unit Type for Y',
                                        'pyname': u'input_unit_type_for_y',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:CubicLinear',
               'pyname': u'CurveCubicLinear',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x(self):
        """field `Coefficient2 x`

        Args:
            value (float): value for IDD Field `Coefficient2 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x` or None if not set

        """
        return self["Coefficient2 x"]

    @coefficient2_x.setter
    def coefficient2_x(self, value=None):
        """Corresponds to IDD field `Coefficient2 x`"""
        self["Coefficient2 x"] = value

    @property
    def coefficient3_x2(self):
        """field `Coefficient3 x**2`


        Args:
            value (float): value for IDD Field `Coefficient3 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x2` or None if not set
        """
        return self["Coefficient3 x**2"]

    @coefficient3_x2.setter
    def coefficient3_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient3 x**2`

        """
        self["Coefficient3 x**2"] = value

    @property
    def coefficient4_x3(self):
        """field `Coefficient4 x**3`


        Args:
            value (float): value for IDD Field `Coefficient4 x**3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_x3` or None if not set
        """
        return self["Coefficient4 x**3"]

    @coefficient4_x3.setter
    def coefficient4_x3(self, value=None):
        """  Corresponds to IDD field `Coefficient4 x**3`

        """
        self["Coefficient4 x**3"] = value

    @property
    def coefficient5_y(self):
        """field `Coefficient5 y`

        Args:
            value (float): value for IDD Field `Coefficient5 y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_y` or None if not set

        """
        return self["Coefficient5 y"]

    @coefficient5_y.setter
    def coefficient5_y(self, value=None):
        """Corresponds to IDD field `Coefficient5 y`"""
        self["Coefficient5 y"] = value

    @property
    def coefficient6_xy(self):
        """field `Coefficient6 x*y`


        Args:
            value (float): value for IDD Field `Coefficient6 x*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient6_xy` or None if not set
        """
        return self["Coefficient6 x*y"]

    @coefficient6_xy.setter
    def coefficient6_xy(self, value=None):
        """  Corresponds to IDD field `Coefficient6 x*y`

        """
        self["Coefficient6 x*y"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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




class CurveTriquadratic(DataObject):

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
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 constant',
                                       {'name': u'Coefficient1 Constant',
                                        'pyname': u'coefficient1_constant',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 x**2',
                                       {'name': u'Coefficient2 x**2',
                                        'pyname': u'coefficient2_x2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 x',
                                       {'name': u'Coefficient3 x',
                                        'pyname': u'coefficient3_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 y**2',
                                       {'name': u'Coefficient4 y**2',
                                        'pyname': u'coefficient4_y2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 y',
                                       {'name': u'Coefficient5 y',
                                        'pyname': u'coefficient5_y',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient6 z**2',
                                       {'name': u'Coefficient6 z**2',
                                        'pyname': u'coefficient6_z2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient7 z',
                                       {'name': u'Coefficient7 z',
                                        'pyname': u'coefficient7_z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient8 x**2*y**2',
                                       {'name': u'Coefficient8 x**2*y**2',
                                        'pyname': u'coefficient8_x2y2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient9 x*y',
                                       {'name': u'Coefficient9 x*y',
                                        'pyname': u'coefficient9_xy',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient10 x*y**2',
                                       {'name': u'Coefficient10 x*y**2',
                                        'pyname': u'coefficient10_xy2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient11 x**2*y',
                                       {'name': u'Coefficient11 x**2*y',
                                        'pyname': u'coefficient11_x2y',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient12 x**2*z**2',
                                       {'name': u'Coefficient12 x**2*z**2',
                                        'pyname': u'coefficient12_x2z2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient13 x*z',
                                       {'name': u'Coefficient13 x*z',
                                        'pyname': u'coefficient13_xz',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient14 x*z**2',
                                       {'name': u'Coefficient14 x*z**2',
                                        'pyname': u'coefficient14_xz2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient15 x**2*z',
                                       {'name': u'Coefficient15 x**2*z',
                                        'pyname': u'coefficient15_x2z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient16 y**2*z**2',
                                       {'name': u'Coefficient16 y**2*z**2',
                                        'pyname': u'coefficient16_y2z2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient17 y*z',
                                       {'name': u'Coefficient17 y*z',
                                        'pyname': u'coefficient17_yz',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient18 y*z**2',
                                       {'name': u'Coefficient18 y*z**2',
                                        'pyname': u'coefficient18_yz2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient19 y**2*z',
                                       {'name': u'Coefficient19 y**2*z',
                                        'pyname': u'coefficient19_y2z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient20 x**2*y**2*z**2',
                                       {'name': u'Coefficient20 x**2*y**2*z**2',
                                        'pyname': u'coefficient20_x2y2z2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient21 x**2*y**2*z',
                                       {'name': u'Coefficient21 x**2*y**2*z',
                                        'pyname': u'coefficient21_x2y2z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient22 x**2*y*z**2',
                                       {'name': u'Coefficient22 x**2*y*z**2',
                                        'pyname': u'coefficient22_x2yz2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient23 x*y**2*z**2',
                                       {'name': u'Coefficient23 x*y**2*z**2',
                                        'pyname': u'coefficient23_xy2z2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient24 x**2*y*z',
                                       {'name': u'Coefficient24 x**2*y*z',
                                        'pyname': u'coefficient24_x2yz',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient25 x*y**2*z',
                                       {'name': u'Coefficient25 x*y**2*z',
                                        'pyname': u'coefficient25_xy2z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient26 x*y*z**2',
                                       {'name': u'Coefficient26 x*y*z**2',
                                        'pyname': u'coefficient26_xyz2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient27 x*y*z',
                                       {'name': u'Coefficient27 x*y*z',
                                        'pyname': u'coefficient27_xyz',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of z',
                                       {'name': u'Minimum Value of z',
                                        'pyname': u'minimum_value_of_z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of z',
                                       {'name': u'Maximum Value of z',
                                        'pyname': u'maximum_value_of_z',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
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
                                      (u'input unit type for z',
                                       {'name': u'Input Unit Type for Z',
                                        'pyname': u'input_unit_type_for_z',
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
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Triquadratic',
               'pyname': u'CurveTriquadratic',
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
    def coefficient1_constant(self):
        """field `Coefficient1 Constant`

        Args:
            value (float): value for IDD Field `Coefficient1 Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_constant` or None if not set

        """
        return self["Coefficient1 Constant"]

    @coefficient1_constant.setter
    def coefficient1_constant(self, value=None):
        """Corresponds to IDD field `Coefficient1 Constant`"""
        self["Coefficient1 Constant"] = value

    @property
    def coefficient2_x2(self):
        """field `Coefficient2 x**2`


        Args:
            value (float): value for IDD Field `Coefficient2 x**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_x2` or None if not set
        """
        return self["Coefficient2 x**2"]

    @coefficient2_x2.setter
    def coefficient2_x2(self, value=None):
        """  Corresponds to IDD field `Coefficient2 x**2`

        """
        self["Coefficient2 x**2"] = value

    @property
    def coefficient3_x(self):
        """field `Coefficient3 x`

        Args:
            value (float): value for IDD Field `Coefficient3 x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_x` or None if not set

        """
        return self["Coefficient3 x"]

    @coefficient3_x.setter
    def coefficient3_x(self, value=None):
        """Corresponds to IDD field `Coefficient3 x`"""
        self["Coefficient3 x"] = value

    @property
    def coefficient4_y2(self):
        """field `Coefficient4 y**2`


        Args:
            value (float): value for IDD Field `Coefficient4 y**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_y2` or None if not set
        """
        return self["Coefficient4 y**2"]

    @coefficient4_y2.setter
    def coefficient4_y2(self, value=None):
        """  Corresponds to IDD field `Coefficient4 y**2`

        """
        self["Coefficient4 y**2"] = value

    @property
    def coefficient5_y(self):
        """field `Coefficient5 y`

        Args:
            value (float): value for IDD Field `Coefficient5 y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_y` or None if not set

        """
        return self["Coefficient5 y"]

    @coefficient5_y.setter
    def coefficient5_y(self, value=None):
        """Corresponds to IDD field `Coefficient5 y`"""
        self["Coefficient5 y"] = value

    @property
    def coefficient6_z2(self):
        """field `Coefficient6 z**2`


        Args:
            value (float): value for IDD Field `Coefficient6 z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient6_z2` or None if not set
        """
        return self["Coefficient6 z**2"]

    @coefficient6_z2.setter
    def coefficient6_z2(self, value=None):
        """  Corresponds to IDD field `Coefficient6 z**2`

        """
        self["Coefficient6 z**2"] = value

    @property
    def coefficient7_z(self):
        """field `Coefficient7 z`

        Args:
            value (float): value for IDD Field `Coefficient7 z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient7_z` or None if not set

        """
        return self["Coefficient7 z"]

    @coefficient7_z.setter
    def coefficient7_z(self, value=None):
        """Corresponds to IDD field `Coefficient7 z`"""
        self["Coefficient7 z"] = value

    @property
    def coefficient8_x2y2(self):
        """field `Coefficient8 x**2*y**2`


        Args:
            value (float): value for IDD Field `Coefficient8 x**2*y**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient8_x2y2` or None if not set
        """
        return self["Coefficient8 x**2*y**2"]

    @coefficient8_x2y2.setter
    def coefficient8_x2y2(self, value=None):
        """  Corresponds to IDD field `Coefficient8 x**2*y**2`

        """
        self["Coefficient8 x**2*y**2"] = value

    @property
    def coefficient9_xy(self):
        """field `Coefficient9 x*y`


        Args:
            value (float): value for IDD Field `Coefficient9 x*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient9_xy` or None if not set
        """
        return self["Coefficient9 x*y"]

    @coefficient9_xy.setter
    def coefficient9_xy(self, value=None):
        """  Corresponds to IDD field `Coefficient9 x*y`

        """
        self["Coefficient9 x*y"] = value

    @property
    def coefficient10_xy2(self):
        """field `Coefficient10 x*y**2`


        Args:
            value (float): value for IDD Field `Coefficient10 x*y**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient10_xy2` or None if not set
        """
        return self["Coefficient10 x*y**2"]

    @coefficient10_xy2.setter
    def coefficient10_xy2(self, value=None):
        """  Corresponds to IDD field `Coefficient10 x*y**2`

        """
        self["Coefficient10 x*y**2"] = value

    @property
    def coefficient11_x2y(self):
        """field `Coefficient11 x**2*y`


        Args:
            value (float): value for IDD Field `Coefficient11 x**2*y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient11_x2y` or None if not set
        """
        return self["Coefficient11 x**2*y"]

    @coefficient11_x2y.setter
    def coefficient11_x2y(self, value=None):
        """  Corresponds to IDD field `Coefficient11 x**2*y`

        """
        self["Coefficient11 x**2*y"] = value

    @property
    def coefficient12_x2z2(self):
        """field `Coefficient12 x**2*z**2`


        Args:
            value (float): value for IDD Field `Coefficient12 x**2*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient12_x2z2` or None if not set
        """
        return self["Coefficient12 x**2*z**2"]

    @coefficient12_x2z2.setter
    def coefficient12_x2z2(self, value=None):
        """  Corresponds to IDD field `Coefficient12 x**2*z**2`

        """
        self["Coefficient12 x**2*z**2"] = value

    @property
    def coefficient13_xz(self):
        """field `Coefficient13 x*z`


        Args:
            value (float): value for IDD Field `Coefficient13 x*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient13_xz` or None if not set
        """
        return self["Coefficient13 x*z"]

    @coefficient13_xz.setter
    def coefficient13_xz(self, value=None):
        """  Corresponds to IDD field `Coefficient13 x*z`

        """
        self["Coefficient13 x*z"] = value

    @property
    def coefficient14_xz2(self):
        """field `Coefficient14 x*z**2`


        Args:
            value (float): value for IDD Field `Coefficient14 x*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient14_xz2` or None if not set
        """
        return self["Coefficient14 x*z**2"]

    @coefficient14_xz2.setter
    def coefficient14_xz2(self, value=None):
        """  Corresponds to IDD field `Coefficient14 x*z**2`

        """
        self["Coefficient14 x*z**2"] = value

    @property
    def coefficient15_x2z(self):
        """field `Coefficient15 x**2*z`


        Args:
            value (float): value for IDD Field `Coefficient15 x**2*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient15_x2z` or None if not set
        """
        return self["Coefficient15 x**2*z"]

    @coefficient15_x2z.setter
    def coefficient15_x2z(self, value=None):
        """  Corresponds to IDD field `Coefficient15 x**2*z`

        """
        self["Coefficient15 x**2*z"] = value

    @property
    def coefficient16_y2z2(self):
        """field `Coefficient16 y**2*z**2`


        Args:
            value (float): value for IDD Field `Coefficient16 y**2*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient16_y2z2` or None if not set
        """
        return self["Coefficient16 y**2*z**2"]

    @coefficient16_y2z2.setter
    def coefficient16_y2z2(self, value=None):
        """  Corresponds to IDD field `Coefficient16 y**2*z**2`

        """
        self["Coefficient16 y**2*z**2"] = value

    @property
    def coefficient17_yz(self):
        """field `Coefficient17 y*z`


        Args:
            value (float): value for IDD Field `Coefficient17 y*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient17_yz` or None if not set
        """
        return self["Coefficient17 y*z"]

    @coefficient17_yz.setter
    def coefficient17_yz(self, value=None):
        """  Corresponds to IDD field `Coefficient17 y*z`

        """
        self["Coefficient17 y*z"] = value

    @property
    def coefficient18_yz2(self):
        """field `Coefficient18 y*z**2`


        Args:
            value (float): value for IDD Field `Coefficient18 y*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient18_yz2` or None if not set
        """
        return self["Coefficient18 y*z**2"]

    @coefficient18_yz2.setter
    def coefficient18_yz2(self, value=None):
        """  Corresponds to IDD field `Coefficient18 y*z**2`

        """
        self["Coefficient18 y*z**2"] = value

    @property
    def coefficient19_y2z(self):
        """field `Coefficient19 y**2*z`


        Args:
            value (float): value for IDD Field `Coefficient19 y**2*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient19_y2z` or None if not set
        """
        return self["Coefficient19 y**2*z"]

    @coefficient19_y2z.setter
    def coefficient19_y2z(self, value=None):
        """  Corresponds to IDD field `Coefficient19 y**2*z`

        """
        self["Coefficient19 y**2*z"] = value

    @property
    def coefficient20_x2y2z2(self):
        """field `Coefficient20 x**2*y**2*z**2`


        Args:
            value (float): value for IDD Field `Coefficient20 x**2*y**2*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient20_x2y2z2` or None if not set
        """
        return self["Coefficient20 x**2*y**2*z**2"]

    @coefficient20_x2y2z2.setter
    def coefficient20_x2y2z2(self, value=None):
        """  Corresponds to IDD field `Coefficient20 x**2*y**2*z**2`

        """
        self["Coefficient20 x**2*y**2*z**2"] = value

    @property
    def coefficient21_x2y2z(self):
        """field `Coefficient21 x**2*y**2*z`


        Args:
            value (float): value for IDD Field `Coefficient21 x**2*y**2*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient21_x2y2z` or None if not set
        """
        return self["Coefficient21 x**2*y**2*z"]

    @coefficient21_x2y2z.setter
    def coefficient21_x2y2z(self, value=None):
        """  Corresponds to IDD field `Coefficient21 x**2*y**2*z`

        """
        self["Coefficient21 x**2*y**2*z"] = value

    @property
    def coefficient22_x2yz2(self):
        """field `Coefficient22 x**2*y*z**2`


        Args:
            value (float): value for IDD Field `Coefficient22 x**2*y*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient22_x2yz2` or None if not set
        """
        return self["Coefficient22 x**2*y*z**2"]

    @coefficient22_x2yz2.setter
    def coefficient22_x2yz2(self, value=None):
        """  Corresponds to IDD field `Coefficient22 x**2*y*z**2`

        """
        self["Coefficient22 x**2*y*z**2"] = value

    @property
    def coefficient23_xy2z2(self):
        """field `Coefficient23 x*y**2*z**2`


        Args:
            value (float): value for IDD Field `Coefficient23 x*y**2*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient23_xy2z2` or None if not set
        """
        return self["Coefficient23 x*y**2*z**2"]

    @coefficient23_xy2z2.setter
    def coefficient23_xy2z2(self, value=None):
        """  Corresponds to IDD field `Coefficient23 x*y**2*z**2`

        """
        self["Coefficient23 x*y**2*z**2"] = value

    @property
    def coefficient24_x2yz(self):
        """field `Coefficient24 x**2*y*z`


        Args:
            value (float): value for IDD Field `Coefficient24 x**2*y*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient24_x2yz` or None if not set
        """
        return self["Coefficient24 x**2*y*z"]

    @coefficient24_x2yz.setter
    def coefficient24_x2yz(self, value=None):
        """  Corresponds to IDD field `Coefficient24 x**2*y*z`

        """
        self["Coefficient24 x**2*y*z"] = value

    @property
    def coefficient25_xy2z(self):
        """field `Coefficient25 x*y**2*z`


        Args:
            value (float): value for IDD Field `Coefficient25 x*y**2*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient25_xy2z` or None if not set
        """
        return self["Coefficient25 x*y**2*z"]

    @coefficient25_xy2z.setter
    def coefficient25_xy2z(self, value=None):
        """  Corresponds to IDD field `Coefficient25 x*y**2*z`

        """
        self["Coefficient25 x*y**2*z"] = value

    @property
    def coefficient26_xyz2(self):
        """field `Coefficient26 x*y*z**2`


        Args:
            value (float): value for IDD Field `Coefficient26 x*y*z**2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient26_xyz2` or None if not set
        """
        return self["Coefficient26 x*y*z**2"]

    @coefficient26_xyz2.setter
    def coefficient26_xyz2(self, value=None):
        """  Corresponds to IDD field `Coefficient26 x*y*z**2`

        """
        self["Coefficient26 x*y*z**2"] = value

    @property
    def coefficient27_xyz(self):
        """field `Coefficient27 x*y*z`


        Args:
            value (float): value for IDD Field `Coefficient27 x*y*z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient27_xyz` or None if not set
        """
        return self["Coefficient27 x*y*z"]

    @coefficient27_xyz.setter
    def coefficient27_xyz(self, value=None):
        """  Corresponds to IDD field `Coefficient27 x*y*z`

        """
        self["Coefficient27 x*y*z"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_value_of_z(self):
        """field `Minimum Value of z`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Value of z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_z` or None if not set

        """
        return self["Minimum Value of z"]

    @minimum_value_of_z.setter
    def minimum_value_of_z(self, value=None):
        """Corresponds to IDD field `Minimum Value of z`"""
        self["Minimum Value of z"] = value

    @property
    def maximum_value_of_z(self):
        """field `Maximum Value of z`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Value of z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_z` or None if not set

        """
        return self["Maximum Value of z"]

    @maximum_value_of_z.setter
    def maximum_value_of_z(self, value=None):
        """Corresponds to IDD field `Maximum Value of z`"""
        self["Maximum Value of z"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

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
    def input_unit_type_for_z(self):
        """field `Input Unit Type for Z`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for Z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_z` or None if not set

        """
        return self["Input Unit Type for Z"]

    @input_unit_type_for_z.setter
    def input_unit_type_for_z(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for Z`"""
        self["Input Unit Type for Z"] = value

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




class CurveFunctionalPressureDrop(DataObject):

    """ Corresponds to IDD object `Curve:Functional:PressureDrop`
        Sets up curve information for minor loss and/or friction
        calculations in plant pressure simulations
        Expression: DeltaP = {K + f*(L/D)} * (rho * V^2) / 2
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'diameter',
                                       {'name': u'Diameter',
                                        'pyname': u'diameter',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'minor loss coefficient',
                                       {'name': u'Minor Loss Coefficient',
                                        'pyname': u'minor_loss_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'length',
                                       {'name': u'Length',
                                        'pyname': u'length',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'roughness',
                                       {'name': u'Roughness',
                                        'pyname': u'roughness',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'fixed friction factor',
                                       {'name': u'Fixed Friction Factor',
                                        'pyname': u'fixed_friction_factor',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 5,
               'name': u'Curve:Functional:PressureDrop',
               'pyname': u'CurveFunctionalPressureDrop',
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
    def diameter(self):
        """field `Diameter`

        |  "D" in above expression, used to also calculate local velocity
        |  Units: m

        Args:
            value (float): value for IDD Field `Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `diameter` or None if not set

        """
        return self["Diameter"]

    @diameter.setter
    def diameter(self, value=None):
        """Corresponds to IDD field `Diameter`"""
        self["Diameter"] = value

    @property
    def minor_loss_coefficient(self):
        """field `Minor Loss Coefficient`

        |  "K" in above expression
        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Minor Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minor_loss_coefficient` or None if not set

        """
        return self["Minor Loss Coefficient"]

    @minor_loss_coefficient.setter
    def minor_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Minor Loss Coefficient`"""
        self["Minor Loss Coefficient"] = value

    @property
    def length(self):
        """field `Length`

        |  "L" in above expression
        |  Units: m

        Args:
            value (float): value for IDD Field `Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `length` or None if not set

        """
        return self["Length"]

    @length.setter
    def length(self, value=None):
        """Corresponds to IDD field `Length`"""
        self["Length"] = value

    @property
    def roughness(self):
        """field `Roughness`

        |  This will be used to calculate "f" from Moody-chart approximations
        |  Units: m

        Args:
            value (float): value for IDD Field `Roughness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `roughness` or None if not set

        """
        return self["Roughness"]

    @roughness.setter
    def roughness(self, value=None):
        """Corresponds to IDD field `Roughness`"""
        self["Roughness"] = value

    @property
    def fixed_friction_factor(self):
        """field `Fixed Friction Factor`

        |  Optional way to set a constant value for "f", instead of using
        |  internal Moody-chart approximations

        Args:
            value (float): value for IDD Field `Fixed Friction Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fixed_friction_factor` or None if not set

        """
        return self["Fixed Friction Factor"]

    @fixed_friction_factor.setter
    def fixed_friction_factor(self, value=None):
        """Corresponds to IDD field `Fixed Friction Factor`"""
        self["Fixed Friction Factor"] = value




class CurveFanPressureRise(DataObject):

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
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 c4',
                                       {'name': u'Coefficient4 C4',
                                        'pyname': u'coefficient4_c4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of qfan',
                                       {'name': u'Minimum Value of Qfan',
                                        'pyname': u'minimum_value_of_qfan',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum value of qfan',
                                       {'name': u'Maximum Value of Qfan',
                                        'pyname': u'maximum_value_of_qfan',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum value of psm',
                                       {'name': u'Minimum Value of Psm',
                                        'pyname': u'minimum_value_of_psm',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'maximum value of psm',
                                       {'name': u'Maximum Value of Psm',
                                        'pyname': u'maximum_value_of_psm',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:FanPressureRise',
               'pyname': u'CurveFanPressureRise',
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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_c4` or None if not set

        """
        return self["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """Corresponds to IDD field `Coefficient4 C4`"""
        self["Coefficient4 C4"] = value

    @property
    def minimum_value_of_qfan(self):
        """field `Minimum Value of Qfan`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Minimum Value of Qfan`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_qfan` or None if not set

        """
        return self["Minimum Value of Qfan"]

    @minimum_value_of_qfan.setter
    def minimum_value_of_qfan(self, value=None):
        """Corresponds to IDD field `Minimum Value of Qfan`"""
        self["Minimum Value of Qfan"] = value

    @property
    def maximum_value_of_qfan(self):
        """field `Maximum Value of Qfan`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Maximum Value of Qfan`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_qfan` or None if not set

        """
        return self["Maximum Value of Qfan"]

    @maximum_value_of_qfan.setter
    def maximum_value_of_qfan(self, value=None):
        """Corresponds to IDD field `Maximum Value of Qfan`"""
        self["Maximum Value of Qfan"] = value

    @property
    def minimum_value_of_psm(self):
        """field `Minimum Value of Psm`

        |  Units: Pa
        |  IP-Units: Pa

        Args:
            value (float): value for IDD Field `Minimum Value of Psm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_psm` or None if not set

        """
        return self["Minimum Value of Psm"]

    @minimum_value_of_psm.setter
    def minimum_value_of_psm(self, value=None):
        """Corresponds to IDD field `Minimum Value of Psm`"""
        self["Minimum Value of Psm"] = value

    @property
    def maximum_value_of_psm(self):
        """field `Maximum Value of Psm`

        |  Units: Pa
        |  IP-Units: Pa

        Args:
            value (float): value for IDD Field `Maximum Value of Psm`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_psm` or None if not set

        """
        return self["Maximum Value of Psm"]

    @maximum_value_of_psm.setter
    def maximum_value_of_psm(self, value=None):
        """Corresponds to IDD field `Maximum Value of Psm`"""
        self["Maximum Value of Psm"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units: Pa
        |  IP-Units: Pa

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units: Pa
        |  IP-Units: Pa

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value




class CurveExponentialSkewNormal(DataObject):

    """ Corresponds to IDD object `Curve:ExponentialSkewNormal`
        Exponential-modified skew normal curve with one independent variable.
        Input consists of the curve name, the four coefficients, and the maximum
        and minimum valid independent variable values. Optional inputs for the curve minimum
        and maximum may be used to limit the output of the performance curve.
        curve = see Input Output Reference
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 c4',
                                       {'name': u'Coefficient4 C4',
                                        'pyname': u'coefficient4_c4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:ExponentialSkewNormal',
               'pyname': u'CurveExponentialSkewNormal',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  See InputOut Reference for curve description

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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_c4` or None if not set

        """
        return self["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """Corresponds to IDD field `Coefficient4 C4`"""
        self["Coefficient4 C4"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

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




class CurveSigmoid(DataObject):

    """ Corresponds to IDD object `Curve:Sigmoid`
        Sigmoid curve with one independent variable.
        Input consists of the curve name, the five coefficients, and the maximum and minimum
        valid independent variable values. Optional inputs for the curve minimum and maximum
        may be used to limit the output of the performance curve.
        curve = C1+C2/[1+exp((C3-x)/C4)]**C5
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 c4',
                                       {'name': u'Coefficient4 C4',
                                        'pyname': u'coefficient4_c4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 c5',
                                       {'name': u'Coefficient5 C5',
                                        'pyname': u'coefficient5_c5',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:Sigmoid',
               'pyname': u'CurveSigmoid',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  See InputOut Reference for curve description

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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_c4` or None if not set

        """
        return self["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """Corresponds to IDD field `Coefficient4 C4`"""
        self["Coefficient4 C4"] = value

    @property
    def coefficient5_c5(self):
        """field `Coefficient5 C5`

        Args:
            value (float): value for IDD Field `Coefficient5 C5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_c5` or None if not set

        """
        return self["Coefficient5 C5"]

    @coefficient5_c5.setter
    def coefficient5_c5(self, value=None):
        """Corresponds to IDD field `Coefficient5 C5`"""
        self["Coefficient5 C5"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

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




class CurveRectangularHyperbola1(DataObject):

    """ Corresponds to IDD object `Curve:RectangularHyperbola1`
        Rectangular hyperbola type 1 curve with one independent variable.
        Input consists of the curve name, the three coefficients, and the maximum and
        minimum valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = ((C1*x)/(C2+x))+C3
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:RectangularHyperbola1',
               'pyname': u'CurveRectangularHyperbola1',
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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

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




class CurveRectangularHyperbola2(DataObject):

    """ Corresponds to IDD object `Curve:RectangularHyperbola2`
        Rectangular hyperbola type 2 curve with one independent variable.
        Input consists of the curve name, the three coefficients, and the maximum and
        minimum valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = ((C1*x)/(C2+x))+(C3*x)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:RectangularHyperbola2',
               'pyname': u'CurveRectangularHyperbola2',
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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

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




class CurveExponentialDecay(DataObject):

    """ Corresponds to IDD object `Curve:ExponentialDecay`
        Exponential decay curve with one independent variable.
        Input consists of the curve name, the three coefficients, and the maximum and minimum
        valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = C1+C2*exp(C3*x)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:ExponentialDecay',
               'pyname': u'CurveExponentialDecay',
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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

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




class CurveDoubleExponentialDecay(DataObject):

    """ Corresponds to IDD object `Curve:DoubleExponentialDecay`
        Double exponential decay curve with one independent variable.
        Input consists of the curve name, the five coefficients, and the maximum and minimum
        valid independent variable values. Optional inputs for the curve minimum and
        maximum may be used to limit the output of the performance curve.
        curve = C1+C2*exp(C3*x)+C4*exp(C5*x)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c4',
                                       {'name': u'Coefficient3 C4',
                                        'pyname': u'coefficient3_c4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c5',
                                       {'name': u'Coefficient3 C5',
                                        'pyname': u'coefficient3_c5',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:DoubleExponentialDecay',
               'pyname': u'CurveDoubleExponentialDecay',
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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def coefficient3_c4(self):
        """field `Coefficient3 C4`

        Args:
            value (float): value for IDD Field `Coefficient3 C4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c4` or None if not set

        """
        return self["Coefficient3 C4"]

    @coefficient3_c4.setter
    def coefficient3_c4(self, value=None):
        """Corresponds to IDD field `Coefficient3 C4`"""
        self["Coefficient3 C4"] = value

    @property
    def coefficient3_c5(self):
        """field `Coefficient3 C5`

        Args:
            value (float): value for IDD Field `Coefficient3 C5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c5` or None if not set

        """
        return self["Coefficient3 C5"]

    @coefficient3_c5.setter
    def coefficient3_c5(self, value=None):
        """Corresponds to IDD field `Coefficient3 C5`"""
        self["Coefficient3 C5"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

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




class CurveChillerPartLoadWithLift(DataObject):

    """ Corresponds to IDD object `Curve:ChillerPartLoadWithLift`
        This chiller part-load performance curve has three independent variables.
        Input consists of the curve name, the twelve coefficients, and the maximum
        and minimum valid independent variable values. Optional inputs for the curve minimum
        and maximum may be used to limit the output of the performance curve.
        curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3
        + C8*y**3 + C9*x**2*y + C10*x*y**2 + C11*x**2*y**2 + C12*z*y**3
        x = dT* = normalized fractional Lift = dT / dTref
        y = PLR = part load ratio (cooling load/steady state capacity)
        z = Tdev* = normalized Tdev = Tdev / dTref
        Where:
        dT = Lift = Leaving Condenser Water Temperature - Leaving Chilled Water Temperature
        dTref = dT at the reference condition
        Tdev = Leaving Chilled Water Temperature - Reference Chilled Water Temperature
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'coefficient1 c1',
                                       {'name': u'Coefficient1 C1',
                                        'pyname': u'coefficient1_c1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient2 c2',
                                       {'name': u'Coefficient2 C2',
                                        'pyname': u'coefficient2_c2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient3 c3',
                                       {'name': u'Coefficient3 C3',
                                        'pyname': u'coefficient3_c3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient4 c4',
                                       {'name': u'Coefficient4 C4',
                                        'pyname': u'coefficient4_c4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient5 c5',
                                       {'name': u'Coefficient5 C5',
                                        'pyname': u'coefficient5_c5',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient6 c6',
                                       {'name': u'Coefficient6 C6',
                                        'pyname': u'coefficient6_c6',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient7 c7',
                                       {'name': u'Coefficient7 C7',
                                        'pyname': u'coefficient7_c7',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient8 c8',
                                       {'name': u'Coefficient8 C8',
                                        'pyname': u'coefficient8_c8',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient9 c9',
                                       {'name': u'Coefficient9 C9',
                                        'pyname': u'coefficient9_c9',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient10 c10',
                                       {'name': u'Coefficient10 C10',
                                        'pyname': u'coefficient10_c10',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient11 c11',
                                       {'name': u'Coefficient11 C11',
                                        'pyname': u'coefficient11_c11',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient12 c12',
                                       {'name': u'Coefficient12 C12',
                                        'pyname': u'coefficient12_c12',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of x',
                                       {'name': u'Minimum Value of x',
                                        'pyname': u'minimum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of x',
                                       {'name': u'Maximum Value of x',
                                        'pyname': u'maximum_value_of_x',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of y',
                                       {'name': u'Minimum Value of y',
                                        'pyname': u'minimum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of y',
                                       {'name': u'Maximum Value of y',
                                        'pyname': u'maximum_value_of_y',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum value of z',
                                       {'name': u'Minimum Value of z',
                                        'pyname': u'minimum_value_of_z',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum value of z',
                                       {'name': u'Maximum Value of z',
                                        'pyname': u'maximum_value_of_z',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum curve output',
                                       {'name': u'Minimum Curve Output',
                                        'pyname': u'minimum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum curve output',
                                       {'name': u'Maximum Curve Output',
                                        'pyname': u'maximum_curve_output',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'input unit type for x',
                                       {'name': u'Input Unit Type for x',
                                        'pyname': u'input_unit_type_for_x',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for y',
                                       {'name': u'Input Unit Type for y',
                                        'pyname': u'input_unit_type_for_y',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'input unit type for z',
                                       {'name': u'Input Unit Type for z',
                                        'pyname': u'input_unit_type_for_z',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'output unit type',
                                       {'name': u'Output Unit Type',
                                        'pyname': u'output_unit_type',
                                        'default': u'Dimensionless',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Dimensionless'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Performance Curves',
               'min-fields': 0,
               'name': u'Curve:ChillerPartLoadWithLift',
               'pyname': u'CurveChillerPartLoadWithLift',
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
    def coefficient1_c1(self):
        """field `Coefficient1 C1`

        Args:
            value (float): value for IDD Field `Coefficient1 C1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient1_c1` or None if not set

        """
        return self["Coefficient1 C1"]

    @coefficient1_c1.setter
    def coefficient1_c1(self, value=None):
        """Corresponds to IDD field `Coefficient1 C1`"""
        self["Coefficient1 C1"] = value

    @property
    def coefficient2_c2(self):
        """field `Coefficient2 C2`

        Args:
            value (float): value for IDD Field `Coefficient2 C2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient2_c2` or None if not set

        """
        return self["Coefficient2 C2"]

    @coefficient2_c2.setter
    def coefficient2_c2(self, value=None):
        """Corresponds to IDD field `Coefficient2 C2`"""
        self["Coefficient2 C2"] = value

    @property
    def coefficient3_c3(self):
        """field `Coefficient3 C3`

        Args:
            value (float): value for IDD Field `Coefficient3 C3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient3_c3` or None if not set

        """
        return self["Coefficient3 C3"]

    @coefficient3_c3.setter
    def coefficient3_c3(self, value=None):
        """Corresponds to IDD field `Coefficient3 C3`"""
        self["Coefficient3 C3"] = value

    @property
    def coefficient4_c4(self):
        """field `Coefficient4 C4`

        Args:
            value (float): value for IDD Field `Coefficient4 C4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient4_c4` or None if not set

        """
        return self["Coefficient4 C4"]

    @coefficient4_c4.setter
    def coefficient4_c4(self, value=None):
        """Corresponds to IDD field `Coefficient4 C4`"""
        self["Coefficient4 C4"] = value

    @property
    def coefficient5_c5(self):
        """field `Coefficient5 C5`

        Args:
            value (float): value for IDD Field `Coefficient5 C5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient5_c5` or None if not set

        """
        return self["Coefficient5 C5"]

    @coefficient5_c5.setter
    def coefficient5_c5(self, value=None):
        """Corresponds to IDD field `Coefficient5 C5`"""
        self["Coefficient5 C5"] = value

    @property
    def coefficient6_c6(self):
        """field `Coefficient6 C6`

        Args:
            value (float): value for IDD Field `Coefficient6 C6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient6_c6` or None if not set

        """
        return self["Coefficient6 C6"]

    @coefficient6_c6.setter
    def coefficient6_c6(self, value=None):
        """Corresponds to IDD field `Coefficient6 C6`"""
        self["Coefficient6 C6"] = value

    @property
    def coefficient7_c7(self):
        """field `Coefficient7 C7`

        Args:
            value (float): value for IDD Field `Coefficient7 C7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient7_c7` or None if not set

        """
        return self["Coefficient7 C7"]

    @coefficient7_c7.setter
    def coefficient7_c7(self, value=None):
        """Corresponds to IDD field `Coefficient7 C7`"""
        self["Coefficient7 C7"] = value

    @property
    def coefficient8_c8(self):
        """field `Coefficient8 C8`

        Args:
            value (float): value for IDD Field `Coefficient8 C8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient8_c8` or None if not set

        """
        return self["Coefficient8 C8"]

    @coefficient8_c8.setter
    def coefficient8_c8(self, value=None):
        """Corresponds to IDD field `Coefficient8 C8`"""
        self["Coefficient8 C8"] = value

    @property
    def coefficient9_c9(self):
        """field `Coefficient9 C9`

        Args:
            value (float): value for IDD Field `Coefficient9 C9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient9_c9` or None if not set

        """
        return self["Coefficient9 C9"]

    @coefficient9_c9.setter
    def coefficient9_c9(self, value=None):
        """Corresponds to IDD field `Coefficient9 C9`"""
        self["Coefficient9 C9"] = value

    @property
    def coefficient10_c10(self):
        """field `Coefficient10 C10`

        Args:
            value (float): value for IDD Field `Coefficient10 C10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient10_c10` or None if not set

        """
        return self["Coefficient10 C10"]

    @coefficient10_c10.setter
    def coefficient10_c10(self, value=None):
        """Corresponds to IDD field `Coefficient10 C10`"""
        self["Coefficient10 C10"] = value

    @property
    def coefficient11_c11(self):
        """field `Coefficient11 C11`

        Args:
            value (float): value for IDD Field `Coefficient11 C11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient11_c11` or None if not set

        """
        return self["Coefficient11 C11"]

    @coefficient11_c11.setter
    def coefficient11_c11(self, value=None):
        """Corresponds to IDD field `Coefficient11 C11`"""
        self["Coefficient11 C11"] = value

    @property
    def coefficient12_c12(self):
        """field `Coefficient12 C12`

        Args:
            value (float): value for IDD Field `Coefficient12 C12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coefficient12_c12` or None if not set

        """
        return self["Coefficient12 C12"]

    @coefficient12_c12.setter
    def coefficient12_c12(self, value=None):
        """Corresponds to IDD field `Coefficient12 C12`"""
        self["Coefficient12 C12"] = value

    @property
    def minimum_value_of_x(self):
        """field `Minimum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Minimum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_x` or None if not set

        """
        return self["Minimum Value of x"]

    @minimum_value_of_x.setter
    def minimum_value_of_x(self, value=None):
        """Corresponds to IDD field `Minimum Value of x`"""
        self["Minimum Value of x"] = value

    @property
    def maximum_value_of_x(self):
        """field `Maximum Value of x`

        |  Units are based on field `A2`

        Args:
            value (float): value for IDD Field `Maximum Value of x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_x` or None if not set

        """
        return self["Maximum Value of x"]

    @maximum_value_of_x.setter
    def maximum_value_of_x(self, value=None):
        """Corresponds to IDD field `Maximum Value of x`"""
        self["Maximum Value of x"] = value

    @property
    def minimum_value_of_y(self):
        """field `Minimum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Minimum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_y` or None if not set

        """
        return self["Minimum Value of y"]

    @minimum_value_of_y.setter
    def minimum_value_of_y(self, value=None):
        """Corresponds to IDD field `Minimum Value of y`"""
        self["Minimum Value of y"] = value

    @property
    def maximum_value_of_y(self):
        """field `Maximum Value of y`

        |  Units are based on field `A3`

        Args:
            value (float): value for IDD Field `Maximum Value of y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_y` or None if not set

        """
        return self["Maximum Value of y"]

    @maximum_value_of_y.setter
    def maximum_value_of_y(self, value=None):
        """Corresponds to IDD field `Maximum Value of y`"""
        self["Maximum Value of y"] = value

    @property
    def minimum_value_of_z(self):
        """field `Minimum Value of z`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Minimum Value of z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_value_of_z` or None if not set

        """
        return self["Minimum Value of z"]

    @minimum_value_of_z.setter
    def minimum_value_of_z(self, value=None):
        """Corresponds to IDD field `Minimum Value of z`"""
        self["Minimum Value of z"] = value

    @property
    def maximum_value_of_z(self):
        """field `Maximum Value of z`

        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Maximum Value of z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_value_of_z` or None if not set

        """
        return self["Maximum Value of z"]

    @maximum_value_of_z.setter
    def maximum_value_of_z(self, value=None):
        """Corresponds to IDD field `Maximum Value of z`"""
        self["Maximum Value of z"] = value

    @property
    def minimum_curve_output(self):
        """field `Minimum Curve Output`

        |  Specify the minimum value calculated by this curve object
        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Minimum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_curve_output` or None if not set

        """
        return self["Minimum Curve Output"]

    @minimum_curve_output.setter
    def minimum_curve_output(self, value=None):
        """Corresponds to IDD field `Minimum Curve Output`"""
        self["Minimum Curve Output"] = value

    @property
    def maximum_curve_output(self):
        """field `Maximum Curve Output`

        |  Specify the maximum value calculated by this curve object
        |  Units are based on field `A5`

        Args:
            value (float): value for IDD Field `Maximum Curve Output`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_curve_output` or None if not set

        """
        return self["Maximum Curve Output"]

    @maximum_curve_output.setter
    def maximum_curve_output(self, value=None):
        """Corresponds to IDD field `Maximum Curve Output`"""
        self["Maximum Curve Output"] = value

    @property
    def input_unit_type_for_x(self):
        """field `Input Unit Type for x`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for x`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_x` or None if not set

        """
        return self["Input Unit Type for x"]

    @input_unit_type_for_x.setter
    def input_unit_type_for_x(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for x`"""
        self["Input Unit Type for x"] = value

    @property
    def input_unit_type_for_y(self):
        """field `Input Unit Type for y`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for y`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_y` or None if not set

        """
        return self["Input Unit Type for y"]

    @input_unit_type_for_y.setter
    def input_unit_type_for_y(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for y`"""
        self["Input Unit Type for y"] = value

    @property
    def input_unit_type_for_z(self):
        """field `Input Unit Type for z`

        |  Default value: Dimensionless

        Args:
            value (str): value for IDD Field `Input Unit Type for z`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `input_unit_type_for_z` or None if not set

        """
        return self["Input Unit Type for z"]

    @input_unit_type_for_z.setter
    def input_unit_type_for_z(self, value="Dimensionless"):
        """Corresponds to IDD field `Input Unit Type for z`"""
        self["Input Unit Type for z"] = value

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


