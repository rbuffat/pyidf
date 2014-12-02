from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class Branch(object):
    """ Corresponds to IDD object `Branch`
        List components on the branch in simulation and connection order
        Note: this should NOT include splitters or mixers which define
        endpoints of branches
    """
    internal_name = "Branch"
    field_count = 3
    required_fields = ["Name"]
    extensible_fields = 5
    format = None
    min_fields = 0
    extensible_keys = ["Component 1 Object Type", "Component 1 Name", "Component 1 Inlet Node Name", "Component 1 Outlet Node Name", "Component 1 Branch Control Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Branch`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Pressure Drop Curve Name"] = None
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
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pressure_drop_curve_name = None
        else:
            self.pressure_drop_curve_name = vals[i]
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
                                 ' for field `Branch.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.name`')
        self._data["Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Maximum Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Flow Rate`
                Units: m3/s
                Default value: 0.0
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `Branch.maximum_flow_rate`'.format(value))
                    self._data["Maximum Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `Branch.maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `Branch.maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def pressure_drop_curve_name(self):
        """Get pressure_drop_curve_name

        Returns:
            str: the value of `pressure_drop_curve_name` or None if not set
        """
        return self._data["Pressure Drop Curve Name"]

    @pressure_drop_curve_name.setter
    def pressure_drop_curve_name(self, value=None):
        """  Corresponds to IDD Field `Pressure Drop Curve Name`
        Optional field to include this branch in plant pressure drop calculations
        This field is only relevant for branches in PlantLoops and CondenserLoops
        Air loops do not account for pressure drop using this field
        Valid curve types are: Curve:Functional:PressureDrop or
        one of Curve:{Linear,Quadratic,Cubic,Exponent}')
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Pressure Drop Curve Name`
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
                                 ' for field `Branch.pressure_drop_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.pressure_drop_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.pressure_drop_curve_name`')
        self._data["Pressure Drop Curve Name"] = value

    def add_extensible(self,
                       component_1_object_type=None,
                       component_1_name=None,
                       component_1_inlet_node_name=None,
                       component_1_outlet_node_name=None,
                       component_1_branch_control_type=None,
                       ):
        """ Add values for extensible fields

        Args:

            component_1_object_type (str): value for IDD Field `Component 1 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_name (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_inlet_node_name (str): value for IDD Field `Component 1 Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_outlet_node_name (str): value for IDD Field `Component 1 Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_branch_control_type (str): value for IDD Field `Component 1 Branch Control Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_component_1_object_type(component_1_object_type))
        vals.append(self._check_component_1_name(component_1_name))
        vals.append(self._check_component_1_inlet_node_name(component_1_inlet_node_name))
        vals.append(self._check_component_1_outlet_node_name(component_1_outlet_node_name))
        vals.append(self._check_component_1_branch_control_type(component_1_branch_control_type))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_component_1_object_type(self, value):
        """ Validates falue of field `Component 1 Object Type`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `Branch.component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.component_1_object_type`')
        return value

    def _check_component_1_name(self, value):
        """ Validates falue of field `Component 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `Branch.component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.component_1_name`')
        return value

    def _check_component_1_inlet_node_name(self, value):
        """ Validates falue of field `Component 1 Inlet Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `Branch.component_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.component_1_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.component_1_inlet_node_name`')
        return value

    def _check_component_1_outlet_node_name(self, value):
        """ Validates falue of field `Component 1 Outlet Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `Branch.component_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.component_1_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.component_1_outlet_node_name`')
        return value

    def _check_component_1_branch_control_type(self, value):
        """ Validates falue of field `Component 1 Branch Control Type`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `Branch.component_1_branch_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Branch.component_1_branch_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Branch.component_1_branch_control_type`')
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
                    raise ValueError("Required field Branch:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Branch:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Branch: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Branch: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class ConnectorSplitter(object):
    """ Corresponds to IDD object `Connector:Splitter`
        Split one air/water stream into N outlet streams.  Branch names cannot be duplicated
        within a single Splitter list.
    """
    internal_name = "Connector:Splitter"
    field_count = 2
    required_fields = ["Name", "Inlet Branch Name"]
    extensible_fields = 1
    format = None
    min_fields = 3
    extensible_keys = ["Outlet Branch Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Connector:Splitter`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Branch Name"] = None
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
            self.inlet_branch_name = None
        else:
            self.inlet_branch_name = vals[i]
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
                                 ' for field `ConnectorSplitter.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorSplitter.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorSplitter.name`')
        self._data["Name"] = value

    @property
    def inlet_branch_name(self):
        """Get inlet_branch_name

        Returns:
            str: the value of `inlet_branch_name` or None if not set
        """
        return self._data["Inlet Branch Name"]

    @inlet_branch_name.setter
    def inlet_branch_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Branch Name`

        Args:
            value (str): value for IDD Field `Inlet Branch Name`
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
                                 ' for field `ConnectorSplitter.inlet_branch_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorSplitter.inlet_branch_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorSplitter.inlet_branch_name`')
        self._data["Inlet Branch Name"] = value

    def add_extensible(self,
                       outlet_branch_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            outlet_branch_name (str): value for IDD Field `Outlet Branch Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_outlet_branch_name(outlet_branch_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_outlet_branch_name(self, value):
        """ Validates falue of field `Outlet Branch Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ConnectorSplitter.outlet_branch_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorSplitter.outlet_branch_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorSplitter.outlet_branch_name`')
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
                    raise ValueError("Required field ConnectorSplitter:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ConnectorSplitter:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ConnectorSplitter: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ConnectorSplitter: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class ConnectorMixer(object):
    """ Corresponds to IDD object `Connector:Mixer`
        Mix N inlet air/water streams into one.  Branch names cannot be duplicated within
        a single mixer list.
    """
    internal_name = "Connector:Mixer"
    field_count = 2
    required_fields = ["Name", "Outlet Branch Name"]
    extensible_fields = 1
    format = None
    min_fields = 3
    extensible_keys = ["Inlet Branch Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Connector:Mixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outlet Branch Name"] = None
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
            self.outlet_branch_name = None
        else:
            self.outlet_branch_name = vals[i]
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
                                 ' for field `ConnectorMixer.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorMixer.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorMixer.name`')
        self._data["Name"] = value

    @property
    def outlet_branch_name(self):
        """Get outlet_branch_name

        Returns:
            str: the value of `outlet_branch_name` or None if not set
        """
        return self._data["Outlet Branch Name"]

    @outlet_branch_name.setter
    def outlet_branch_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Branch Name`

        Args:
            value (str): value for IDD Field `Outlet Branch Name`
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
                                 ' for field `ConnectorMixer.outlet_branch_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorMixer.outlet_branch_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorMixer.outlet_branch_name`')
        self._data["Outlet Branch Name"] = value

    def add_extensible(self,
                       inlet_branch_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            inlet_branch_name (str): value for IDD Field `Inlet Branch Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_inlet_branch_name(inlet_branch_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_inlet_branch_name(self, value):
        """ Validates falue of field `Inlet Branch Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ConnectorMixer.inlet_branch_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorMixer.inlet_branch_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorMixer.inlet_branch_name`')
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
                    raise ValueError("Required field ConnectorMixer:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ConnectorMixer:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ConnectorMixer: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ConnectorMixer: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class ConnectorList(object):
    """ Corresponds to IDD object `ConnectorList`
        only two connectors allowed per loop
        if two entered, one must be Connector:Splitter and one must be Connector:Mixer
    """
    internal_name = "ConnectorList"
    field_count = 5
    required_fields = ["Name", "Connector 1 Object Type", "Connector 1 Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ConnectorList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Connector 1 Object Type"] = None
        self._data["Connector 1 Name"] = None
        self._data["Connector 2 Object Type"] = None
        self._data["Connector 2 Name"] = None
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
            self.connector_1_object_type = None
        else:
            self.connector_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_1_name = None
        else:
            self.connector_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_2_object_type = None
        else:
            self.connector_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_2_name = None
        else:
            self.connector_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `ConnectorList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorList.name`')
        self._data["Name"] = value

    @property
    def connector_1_object_type(self):
        """Get connector_1_object_type

        Returns:
            str: the value of `connector_1_object_type` or None if not set
        """
        return self._data["Connector 1 Object Type"]

    @connector_1_object_type.setter
    def connector_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Connector 1 Object Type`

        Args:
            value (str): value for IDD Field `Connector 1 Object Type`
                Accepted values are:
                      - Connector:Splitter
                      - Connector:Mixer
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
                                 ' for field `ConnectorList.connector_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorList.connector_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorList.connector_1_object_type`')
            vals = {}
            vals["connector:splitter"] = "Connector:Splitter"
            vals["connector:mixer"] = "Connector:Mixer"
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
                                     'field `ConnectorList.connector_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ConnectorList.connector_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Connector 1 Object Type"] = value

    @property
    def connector_1_name(self):
        """Get connector_1_name

        Returns:
            str: the value of `connector_1_name` or None if not set
        """
        return self._data["Connector 1 Name"]

    @connector_1_name.setter
    def connector_1_name(self, value=None):
        """  Corresponds to IDD Field `Connector 1 Name`

        Args:
            value (str): value for IDD Field `Connector 1 Name`
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
                                 ' for field `ConnectorList.connector_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorList.connector_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorList.connector_1_name`')
        self._data["Connector 1 Name"] = value

    @property
    def connector_2_object_type(self):
        """Get connector_2_object_type

        Returns:
            str: the value of `connector_2_object_type` or None if not set
        """
        return self._data["Connector 2 Object Type"]

    @connector_2_object_type.setter
    def connector_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Connector 2 Object Type`

        Args:
            value (str): value for IDD Field `Connector 2 Object Type`
                Accepted values are:
                      - Connector:Splitter
                      - Connector:Mixer
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
                                 ' for field `ConnectorList.connector_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorList.connector_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorList.connector_2_object_type`')
            vals = {}
            vals["connector:splitter"] = "Connector:Splitter"
            vals["connector:mixer"] = "Connector:Mixer"
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
                                     'field `ConnectorList.connector_2_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ConnectorList.connector_2_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Connector 2 Object Type"] = value

    @property
    def connector_2_name(self):
        """Get connector_2_name

        Returns:
            str: the value of `connector_2_name` or None if not set
        """
        return self._data["Connector 2 Name"]

    @connector_2_name.setter
    def connector_2_name(self, value=None):
        """  Corresponds to IDD Field `Connector 2 Name`

        Args:
            value (str): value for IDD Field `Connector 2 Name`
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
                                 ' for field `ConnectorList.connector_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ConnectorList.connector_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ConnectorList.connector_2_name`')
        self._data["Connector 2 Name"] = value

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
                    raise ValueError("Required field ConnectorList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ConnectorList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ConnectorList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ConnectorList: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class NodeList(object):
    """ Corresponds to IDD object `NodeList`
        This object is used in places where lists of nodes may be
        needed, e.g. ZoneHVAC:EquipmentConnections field Zone Air Inlet Node or NodeList Name
    """
    internal_name = "NodeList"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `NodeList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
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
                                 ' for field `NodeList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `NodeList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `NodeList.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       node_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            node_name (str): value for IDD Field `Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_node_name(node_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_node_name(self, value):
        """ Validates falue of field `Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `NodeList.node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `NodeList.node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `NodeList.node_name`')
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
                    raise ValueError("Required field NodeList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field NodeList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for NodeList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for NodeList: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class OutdoorAirNode(object):
    """ Corresponds to IDD object `OutdoorAir:Node`
        This object sets the temperature and humidity conditions
        for an outdoor air node.  It allows the height above ground to be
        specified.  This object may be used more than once.
        The same node name may not appear in both an OutdoorAir:Node object and
        an OutdoorAir:NodeList object.
    """
    internal_name = "OutdoorAir:Node"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `OutdoorAir:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Height Above Ground"] = None
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
            self.height_above_ground = None
        else:
            self.height_above_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `OutdoorAirNode.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirNode.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirNode.name`')
        self._data["Name"] = value

    @property
    def height_above_ground(self):
        """Get height_above_ground

        Returns:
            float: the value of `height_above_ground` or None if not set
        """
        return self._data["Height Above Ground"]

    @height_above_ground.setter
    def height_above_ground(self, value=-1.0):
        """  Corresponds to IDD Field `Height Above Ground`
        A value less than zero indicates that the height will be ignored and the weather file conditions will be used.

        Args:
            value (float): value for IDD Field `Height Above Ground`
                Units: m
                Default value: -1.0
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
                                 ' for field `OutdoorAirNode.height_above_ground`'.format(value))
        self._data["Height Above Ground"] = value

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
                    raise ValueError("Required field OutdoorAirNode:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutdoorAirNode:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutdoorAirNode: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutdoorAirNode: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class OutdoorAirNodeList(object):
    """ Corresponds to IDD object `OutdoorAir:NodeList`
        This object sets the temperature and humidity conditions
        for an outdoor air node using the weather data values.
        to vary outdoor air node conditions with height above ground
        use OutdoorAir:Node instead of this object.
        This object may be used more than once.
        The same node name may not appear in both an OutdoorAir:Node object and
        an OutdoorAir:NodeList object.
    """
    internal_name = "OutdoorAir:NodeList"
    field_count = 0
    required_fields = []
    extensible_fields = 1
    format = None
    min_fields = 1
    extensible_keys = ["Node or NodeList Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `OutdoorAir:NodeList`
        """
        self._data = OrderedDict()
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
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

    def add_extensible(self,
                       node_or_nodelist_name_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            node_or_nodelist_name_1 (str): value for IDD Field `Node or NodeList Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_node_or_nodelist_name_1(node_or_nodelist_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_node_or_nodelist_name_1(self, value):
        """ Validates falue of field `Node or NodeList Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutdoorAirNodeList.node_or_nodelist_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirNodeList.node_or_nodelist_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirNodeList.node_or_nodelist_name_1`')
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
                    raise ValueError("Required field OutdoorAirNodeList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutdoorAirNodeList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutdoorAirNodeList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutdoorAirNodeList: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipeAdiabatic(object):
    """ Corresponds to IDD object `Pipe:Adiabatic`
        Passes Inlet Node state variables to Outlet Node state variables
    """
    internal_name = "Pipe:Adiabatic"
    field_count = 3
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Adiabatic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `PipeAdiabatic.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeAdiabatic.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeAdiabatic.name`')
        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
                                 ' for field `PipeAdiabatic.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeAdiabatic.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeAdiabatic.inlet_node_name`')
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `PipeAdiabatic.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeAdiabatic.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeAdiabatic.outlet_node_name`')
        self._data["Outlet Node Name"] = value

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
                    raise ValueError("Required field PipeAdiabatic:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipeAdiabatic:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipeAdiabatic: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipeAdiabatic: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipeAdiabaticSteam(object):
    """ Corresponds to IDD object `Pipe:Adiabatic:Steam`
        Passes Inlet Node state variables to Outlet Node state variables
    """
    internal_name = "Pipe:Adiabatic:Steam"
    field_count = 3
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Adiabatic:Steam`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `PipeAdiabaticSteam.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeAdiabaticSteam.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeAdiabaticSteam.name`')
        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
                                 ' for field `PipeAdiabaticSteam.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeAdiabaticSteam.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeAdiabaticSteam.inlet_node_name`')
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `PipeAdiabaticSteam.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeAdiabaticSteam.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeAdiabaticSteam.outlet_node_name`')
        self._data["Outlet Node Name"] = value

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
                    raise ValueError("Required field PipeAdiabaticSteam:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipeAdiabaticSteam:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipeAdiabaticSteam: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipeAdiabaticSteam: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipeIndoor(object):
    """ Corresponds to IDD object `Pipe:Indoor`
        Pipe model with transport delay and heat transfer to the environment.
    """
    internal_name = "Pipe:Indoor"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Indoor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Environment Type"] = None
        self._data["Ambient Temperature Zone Name"] = None
        self._data["Ambient Temperature Schedule Name"] = None
        self._data["Ambient Air Velocity Schedule Name"] = None
        self._data["Pipe Inside Diameter"] = None
        self._data["Pipe Length"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.environment_type = None
        else:
            self.environment_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_zone_name = None
        else:
            self.ambient_temperature_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_schedule_name = None
        else:
            self.ambient_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_air_velocity_schedule_name = None
        else:
            self.ambient_air_velocity_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inside_diameter = None
        else:
            self.pipe_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `PipeIndoor.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `PipeIndoor.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.construction_name`')
        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Inlet Node Name`
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
                                 ' for field `PipeIndoor.fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.fluid_inlet_node_name`')
        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Outlet Node Name`
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
                                 ' for field `PipeIndoor.fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.fluid_outlet_node_name`')
        self._data["Fluid Outlet Node Name"] = value

    @property
    def environment_type(self):
        """Get environment_type

        Returns:
            str: the value of `environment_type` or None if not set
        """
        return self._data["Environment Type"]

    @environment_type.setter
    def environment_type(self, value="Zone"):
        """  Corresponds to IDD Field `Environment Type`

        Args:
            value (str): value for IDD Field `Environment Type`
                Accepted values are:
                      - Zone
                      - Schedule
                Default value: Zone
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
                                 ' for field `PipeIndoor.environment_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.environment_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.environment_type`')
            vals = {}
            vals["zone"] = "Zone"
            vals["schedule"] = "Schedule"
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
                                     'field `PipeIndoor.environment_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipeIndoor.environment_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Environment Type"] = value

    @property
    def ambient_temperature_zone_name(self):
        """Get ambient_temperature_zone_name

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set
        """
        return self._data["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """  Corresponds to IDD Field `Ambient Temperature Zone Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Zone Name`
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
                                 ' for field `PipeIndoor.ambient_temperature_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.ambient_temperature_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.ambient_temperature_zone_name`')
        self._data["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """Get ambient_temperature_schedule_name

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set
        """
        return self._data["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`
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
                                 ' for field `PipeIndoor.ambient_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.ambient_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.ambient_temperature_schedule_name`')
        self._data["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_air_velocity_schedule_name(self):
        """Get ambient_air_velocity_schedule_name

        Returns:
            str: the value of `ambient_air_velocity_schedule_name` or None if not set
        """
        return self._data["Ambient Air Velocity Schedule Name"]

    @ambient_air_velocity_schedule_name.setter
    def ambient_air_velocity_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Ambient Air Velocity Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Air Velocity Schedule Name`
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
                                 ' for field `PipeIndoor.ambient_air_velocity_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeIndoor.ambient_air_velocity_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeIndoor.ambient_air_velocity_schedule_name`')
        self._data["Ambient Air Velocity Schedule Name"] = value

    @property
    def pipe_inside_diameter(self):
        """Get pipe_inside_diameter

        Returns:
            float: the value of `pipe_inside_diameter` or None if not set
        """
        return self._data["Pipe Inside Diameter"]

    @pipe_inside_diameter.setter
    def pipe_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `Pipe Inside Diameter`

        Args:
            value (float): value for IDD Field `Pipe Inside Diameter`
                Units: m
                IP-Units: in
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeIndoor.pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipeIndoor.pipe_inside_diameter`')
        self._data["Pipe Inside Diameter"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=None):
        """  Corresponds to IDD Field `Pipe Length`

        Args:
            value (float): value for IDD Field `Pipe Length`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeIndoor.pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipeIndoor.pipe_length`')
        self._data["Pipe Length"] = value

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
                    raise ValueError("Required field PipeIndoor:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipeIndoor:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipeIndoor: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipeIndoor: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipeOutdoor(object):
    """ Corresponds to IDD object `Pipe:Outdoor`
        Pipe model with transport delay and heat transfer to the environment.
    """
    internal_name = "Pipe:Outdoor"
    field_count = 7
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Outdoor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Ambient Temperature Outdoor Air Node Name"] = None
        self._data["Pipe Inside Diameter"] = None
        self._data["Pipe Length"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ambient_temperature_outdoor_air_node_name = None
        else:
            self.ambient_temperature_outdoor_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inside_diameter = None
        else:
            self.pipe_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `PipeOutdoor.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeOutdoor.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeOutdoor.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `PipeOutdoor.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeOutdoor.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeOutdoor.construction_name`')
        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Inlet Node Name`
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
                                 ' for field `PipeOutdoor.fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeOutdoor.fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeOutdoor.fluid_inlet_node_name`')
        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Outlet Node Name`
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
                                 ' for field `PipeOutdoor.fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeOutdoor.fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeOutdoor.fluid_outlet_node_name`')
        self._data["Fluid Outlet Node Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """Get ambient_temperature_outdoor_air_node_name

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set
        """
        return self._data["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Ambient Temperature Outdoor Air Node Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Outdoor Air Node Name`
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
                                 ' for field `PipeOutdoor.ambient_temperature_outdoor_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeOutdoor.ambient_temperature_outdoor_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeOutdoor.ambient_temperature_outdoor_air_node_name`')
        self._data["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def pipe_inside_diameter(self):
        """Get pipe_inside_diameter

        Returns:
            float: the value of `pipe_inside_diameter` or None if not set
        """
        return self._data["Pipe Inside Diameter"]

    @pipe_inside_diameter.setter
    def pipe_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `Pipe Inside Diameter`

        Args:
            value (float): value for IDD Field `Pipe Inside Diameter`
                Units: m
                IP-Units: in
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeOutdoor.pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipeOutdoor.pipe_inside_diameter`')
        self._data["Pipe Inside Diameter"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=None):
        """  Corresponds to IDD Field `Pipe Length`

        Args:
            value (float): value for IDD Field `Pipe Length`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeOutdoor.pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipeOutdoor.pipe_length`')
        self._data["Pipe Length"] = value

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
                    raise ValueError("Required field PipeOutdoor:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipeOutdoor:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipeOutdoor: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipeOutdoor: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipeUnderground(object):
    """ Corresponds to IDD object `Pipe:Underground`
        Buried Pipe model: For pipes buried at a depth less
        than one meter, this is an alternative object to:
        HeatExchanger:Surface
    """
    internal_name = "Pipe:Underground"
    field_count = 11
    required_fields = ["Name", "Construction Name", "Fluid Inlet Node Name", "Fluid Outlet Node Name", "Sun Exposure", "Soil Material Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Pipe:Underground`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Sun Exposure"] = None
        self._data["Pipe Inside Diameter"] = None
        self._data["Pipe Length"] = None
        self._data["Soil Material Name"] = None
        self._data["Average Soil Surface Temperature"] = None
        self._data["Amplitude of Soil Surface Temperature"] = None
        self._data["Phase Constant of Soil Surface Temperature"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inside_diameter = None
        else:
            self.pipe_inside_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_length = None
        else:
            self.pipe_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_material_name = None
        else:
            self.soil_material_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.average_soil_surface_temperature = None
        else:
            self.average_soil_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.amplitude_of_soil_surface_temperature = None
        else:
            self.amplitude_of_soil_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.phase_constant_of_soil_surface_temperature = None
        else:
            self.phase_constant_of_soil_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `PipeUnderground.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeUnderground.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeUnderground.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `PipeUnderground.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeUnderground.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeUnderground.construction_name`')
        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Inlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Inlet Node Name`
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
                                 ' for field `PipeUnderground.fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeUnderground.fluid_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeUnderground.fluid_inlet_node_name`')
        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Fluid Outlet Node Name`

        Args:
            value (str): value for IDD Field `Fluid Outlet Node Name`
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
                                 ' for field `PipeUnderground.fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeUnderground.fluid_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeUnderground.fluid_outlet_node_name`')
        self._data["Fluid Outlet Node Name"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value=None):
        """  Corresponds to IDD Field `Sun Exposure`

        Args:
            value (str): value for IDD Field `Sun Exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
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
                                 ' for field `PipeUnderground.sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeUnderground.sun_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeUnderground.sun_exposure`')
            vals = {}
            vals["sunexposed"] = "SunExposed"
            vals["nosun"] = "NoSun"
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
                                     'field `PipeUnderground.sun_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipeUnderground.sun_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sun Exposure"] = value

    @property
    def pipe_inside_diameter(self):
        """Get pipe_inside_diameter

        Returns:
            float: the value of `pipe_inside_diameter` or None if not set
        """
        return self._data["Pipe Inside Diameter"]

    @pipe_inside_diameter.setter
    def pipe_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `Pipe Inside Diameter`
        pipe thickness is defined in the Construction object

        Args:
            value (float): value for IDD Field `Pipe Inside Diameter`
                Units: m
                IP-Units: in
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeUnderground.pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipeUnderground.pipe_inside_diameter`')
        self._data["Pipe Inside Diameter"] = value

    @property
    def pipe_length(self):
        """Get pipe_length

        Returns:
            float: the value of `pipe_length` or None if not set
        """
        return self._data["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=None):
        """  Corresponds to IDD Field `Pipe Length`

        Args:
            value (float): value for IDD Field `Pipe Length`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeUnderground.pipe_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipeUnderground.pipe_length`')
        self._data["Pipe Length"] = value

    @property
    def soil_material_name(self):
        """Get soil_material_name

        Returns:
            str: the value of `soil_material_name` or None if not set
        """
        return self._data["Soil Material Name"]

    @soil_material_name.setter
    def soil_material_name(self, value=None):
        """  Corresponds to IDD Field `Soil Material Name`

        Args:
            value (str): value for IDD Field `Soil Material Name`
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
                                 ' for field `PipeUnderground.soil_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipeUnderground.soil_material_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipeUnderground.soil_material_name`')
        self._data["Soil Material Name"] = value

    @property
    def average_soil_surface_temperature(self):
        """Get average_soil_surface_temperature

        Returns:
            float: the value of `average_soil_surface_temperature` or None if not set
        """
        return self._data["Average Soil Surface Temperature"]

    @average_soil_surface_temperature.setter
    def average_soil_surface_temperature(self, value=0.0):
        """  Corresponds to IDD Field `Average Soil Surface Temperature`
        optional

        Args:
            value (float): value for IDD Field `Average Soil Surface Temperature`
                Units: C
                Default value: 0.0
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
                                 ' for field `PipeUnderground.average_soil_surface_temperature`'.format(value))
        self._data["Average Soil Surface Temperature"] = value

    @property
    def amplitude_of_soil_surface_temperature(self):
        """Get amplitude_of_soil_surface_temperature

        Returns:
            float: the value of `amplitude_of_soil_surface_temperature` or None if not set
        """
        return self._data["Amplitude of Soil Surface Temperature"]

    @amplitude_of_soil_surface_temperature.setter
    def amplitude_of_soil_surface_temperature(self, value=0.0):
        """  Corresponds to IDD Field `Amplitude of Soil Surface Temperature`
        optional

        Args:
            value (float): value for IDD Field `Amplitude of Soil Surface Temperature`
                Units: C
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeUnderground.amplitude_of_soil_surface_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `PipeUnderground.amplitude_of_soil_surface_temperature`')
        self._data["Amplitude of Soil Surface Temperature"] = value

    @property
    def phase_constant_of_soil_surface_temperature(self):
        """Get phase_constant_of_soil_surface_temperature

        Returns:
            float: the value of `phase_constant_of_soil_surface_temperature` or None if not set
        """
        return self._data["Phase Constant of Soil Surface Temperature"]

    @phase_constant_of_soil_surface_temperature.setter
    def phase_constant_of_soil_surface_temperature(self, value=0.0):
        """  Corresponds to IDD Field `Phase Constant of Soil Surface Temperature`
        optional

        Args:
            value (float): value for IDD Field `Phase Constant of Soil Surface Temperature`
                Units: days
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipeUnderground.phase_constant_of_soil_surface_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `PipeUnderground.phase_constant_of_soil_surface_temperature`')
        self._data["Phase Constant of Soil Surface Temperature"] = value

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
                    raise ValueError("Required field PipeUnderground:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipeUnderground:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipeUnderground: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipeUnderground: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipingSystemUndergroundDomain(object):
    """ Corresponds to IDD object `PipingSystem:Underground:Domain`
        The ground domain object for underground piping system simulation.
    """
    internal_name = "PipingSystem:Underground:Domain"
    field_count = 31
    required_fields = ["Name", "Xmax", "Ymax", "Zmax", "X-Direction Mesh Type", "Y-Direction Mesh Type", "Z-Direction Mesh Type", "Soil Thermal Conductivity", "Soil Density", "Soil Specific Heat", "Kusuda-Achenbach Average Surface Temperature", "Kusuda-Achenbach Average Amplitude of Surface Temperature", "Kusuda-Achenbach Phase Shift of Minimum Surface Temperature", "Number of Pipe Circuits Entered for this Domain"]
    extensible_fields = 1
    format = None
    min_fields = 31
    extensible_keys = ["Pipe Circuit 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PipingSystem:Underground:Domain`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Xmax"] = None
        self._data["Ymax"] = None
        self._data["Zmax"] = None
        self._data["X-Direction Mesh Density Parameter"] = None
        self._data["X-Direction Mesh Type"] = None
        self._data["X-Direction Geometric Coefficient"] = None
        self._data["Y-Direction Mesh Density Parameter"] = None
        self._data["Y-Direction Mesh Type"] = None
        self._data["Y-Direction Geometric Coefficient"] = None
        self._data["Z-Direction Mesh Density Parameter"] = None
        self._data["Z-Direction Mesh Type"] = None
        self._data["Z-Direction Geometric Coefficient"] = None
        self._data["Soil Thermal Conductivity"] = None
        self._data["Soil Density"] = None
        self._data["Soil Specific Heat"] = None
        self._data["Soil Moisture Content Volume Fraction"] = None
        self._data["Soil Moisture Content Volume Fraction at Saturation"] = None
        self._data["Kusuda-Achenbach Average Surface Temperature"] = None
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = None
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = None
        self._data["This Domain Includes Basement Surface Interaction"] = None
        self._data["Width of Basement Floor in Ground Domain"] = None
        self._data["Depth of Basement Wall In Ground Domain"] = None
        self._data["Shift Pipe X Coordinates By Basement Width"] = None
        self._data["Name of Basement Wall Boundary Condition Model"] = None
        self._data["Name of Basement Floor Boundary Condition Model"] = None
        self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"] = None
        self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"] = None
        self._data["Evapotranspiration Ground Cover Parameter"] = None
        self._data["Number of Pipe Circuits Entered for this Domain"] = None
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
            self.xmax = None
        else:
            self.xmax = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ymax = None
        else:
            self.ymax = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zmax = None
        else:
            self.zmax = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xdirection_mesh_density_parameter = None
        else:
            self.xdirection_mesh_density_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xdirection_mesh_type = None
        else:
            self.xdirection_mesh_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xdirection_geometric_coefficient = None
        else:
            self.xdirection_geometric_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ydirection_mesh_density_parameter = None
        else:
            self.ydirection_mesh_density_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ydirection_mesh_type = None
        else:
            self.ydirection_mesh_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ydirection_geometric_coefficient = None
        else:
            self.ydirection_geometric_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zdirection_mesh_density_parameter = None
        else:
            self.zdirection_mesh_density_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zdirection_mesh_type = None
        else:
            self.zdirection_mesh_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zdirection_geometric_coefficient = None
        else:
            self.zdirection_geometric_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction = None
        else:
            self.soil_moisture_content_volume_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.soil_moisture_content_volume_fraction_at_saturation = None
        else:
            self.soil_moisture_content_volume_fraction_at_saturation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.this_domain_includes_basement_surface_interaction = None
        else:
            self.this_domain_includes_basement_surface_interaction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width_of_basement_floor_in_ground_domain = None
        else:
            self.width_of_basement_floor_in_ground_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.depth_of_basement_wall_in_ground_domain = None
        else:
            self.depth_of_basement_wall_in_ground_domain = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shift_pipe_x_coordinates_by_basement_width = None
        else:
            self.shift_pipe_x_coordinates_by_basement_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.name_of_basement_wall_boundary_condition_model = None
        else:
            self.name_of_basement_wall_boundary_condition_model = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.name_of_basement_floor_boundary_condition_model = None
        else:
            self.name_of_basement_floor_boundary_condition_model = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = None
        else:
            self.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = None
        else:
            self.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_pipe_circuits_entered_for_this_domain = None
        else:
            self.number_of_pipe_circuits_entered_for_this_domain = vals[i]
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
                                 ' for field `PipingSystemUndergroundDomain.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.name`')
        self._data["Name"] = value

    @property
    def xmax(self):
        """Get xmax

        Returns:
            float: the value of `xmax` or None if not set
        """
        return self._data["Xmax"]

    @xmax.setter
    def xmax(self, value=None):
        """  Corresponds to IDD Field `Xmax`
        Domain extent in the local 'X' direction

        Args:
            value (float): value for IDD Field `Xmax`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.xmax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundDomain.xmax`')
        self._data["Xmax"] = value

    @property
    def ymax(self):
        """Get ymax

        Returns:
            float: the value of `ymax` or None if not set
        """
        return self._data["Ymax"]

    @ymax.setter
    def ymax(self, value=None):
        """  Corresponds to IDD Field `Ymax`
        Domain extent in the local 'Y' direction

        Args:
            value (float): value for IDD Field `Ymax`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.ymax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundDomain.ymax`')
        self._data["Ymax"] = value

    @property
    def zmax(self):
        """Get zmax

        Returns:
            float: the value of `zmax` or None if not set
        """
        return self._data["Zmax"]

    @zmax.setter
    def zmax(self, value=None):
        """  Corresponds to IDD Field `Zmax`
        Domain extent in the local 'Y' direction

        Args:
            value (float): value for IDD Field `Zmax`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.zmax`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundDomain.zmax`')
        self._data["Zmax"] = value

    @property
    def xdirection_mesh_density_parameter(self):
        """Get xdirection_mesh_density_parameter

        Returns:
            int: the value of `xdirection_mesh_density_parameter` or None if not set
        """
        return self._data["X-Direction Mesh Density Parameter"]

    @xdirection_mesh_density_parameter.setter
    def xdirection_mesh_density_parameter(self, value=4):
        """  Corresponds to IDD Field `X-Direction Mesh Density Parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `X-Direction Mesh Density Parameter`
                Default value: 4
                value > 0
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
                                     'for field `PipingSystemUndergroundDomain.xdirection_mesh_density_parameter`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundDomain.xdirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `PipingSystemUndergroundDomain.xdirection_mesh_density_parameter`')
        self._data["X-Direction Mesh Density Parameter"] = value

    @property
    def xdirection_mesh_type(self):
        """Get xdirection_mesh_type

        Returns:
            str: the value of `xdirection_mesh_type` or None if not set
        """
        return self._data["X-Direction Mesh Type"]

    @xdirection_mesh_type.setter
    def xdirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `X-Direction Mesh Type`

        Args:
            value (str): value for IDD Field `X-Direction Mesh Type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
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
                                 ' for field `PipingSystemUndergroundDomain.xdirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.xdirection_mesh_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.xdirection_mesh_type`')
            vals = {}
            vals["uniform"] = "Uniform"
            vals["symmetricgeometric"] = "SymmetricGeometric"
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
                                     'field `PipingSystemUndergroundDomain.xdirection_mesh_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipingSystemUndergroundDomain.xdirection_mesh_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["X-Direction Mesh Type"] = value

    @property
    def xdirection_geometric_coefficient(self):
        """Get xdirection_geometric_coefficient

        Returns:
            float: the value of `xdirection_geometric_coefficient` or None if not set
        """
        return self._data["X-Direction Geometric Coefficient"]

    @xdirection_geometric_coefficient.setter
    def xdirection_geometric_coefficient(self, value=1.3):
        """  Corresponds to IDD Field `X-Direction Geometric Coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `X-Direction Geometric Coefficient`
                Default value: 1.3
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.xdirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `PipingSystemUndergroundDomain.xdirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `PipingSystemUndergroundDomain.xdirection_geometric_coefficient`')
        self._data["X-Direction Geometric Coefficient"] = value

    @property
    def ydirection_mesh_density_parameter(self):
        """Get ydirection_mesh_density_parameter

        Returns:
            int: the value of `ydirection_mesh_density_parameter` or None if not set
        """
        return self._data["Y-Direction Mesh Density Parameter"]

    @ydirection_mesh_density_parameter.setter
    def ydirection_mesh_density_parameter(self, value=4):
        """  Corresponds to IDD Field `Y-Direction Mesh Density Parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `Y-Direction Mesh Density Parameter`
                Default value: 4
                value > 0
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
                                     'for field `PipingSystemUndergroundDomain.ydirection_mesh_density_parameter`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundDomain.ydirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `PipingSystemUndergroundDomain.ydirection_mesh_density_parameter`')
        self._data["Y-Direction Mesh Density Parameter"] = value

    @property
    def ydirection_mesh_type(self):
        """Get ydirection_mesh_type

        Returns:
            str: the value of `ydirection_mesh_type` or None if not set
        """
        return self._data["Y-Direction Mesh Type"]

    @ydirection_mesh_type.setter
    def ydirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `Y-Direction Mesh Type`

        Args:
            value (str): value for IDD Field `Y-Direction Mesh Type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
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
                                 ' for field `PipingSystemUndergroundDomain.ydirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.ydirection_mesh_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.ydirection_mesh_type`')
            vals = {}
            vals["uniform"] = "Uniform"
            vals["symmetricgeometric"] = "SymmetricGeometric"
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
                                     'field `PipingSystemUndergroundDomain.ydirection_mesh_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipingSystemUndergroundDomain.ydirection_mesh_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Y-Direction Mesh Type"] = value

    @property
    def ydirection_geometric_coefficient(self):
        """Get ydirection_geometric_coefficient

        Returns:
            float: the value of `ydirection_geometric_coefficient` or None if not set
        """
        return self._data["Y-Direction Geometric Coefficient"]

    @ydirection_geometric_coefficient.setter
    def ydirection_geometric_coefficient(self, value=1.3):
        """  Corresponds to IDD Field `Y-Direction Geometric Coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `Y-Direction Geometric Coefficient`
                Default value: 1.3
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.ydirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `PipingSystemUndergroundDomain.ydirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `PipingSystemUndergroundDomain.ydirection_geometric_coefficient`')
        self._data["Y-Direction Geometric Coefficient"] = value

    @property
    def zdirection_mesh_density_parameter(self):
        """Get zdirection_mesh_density_parameter

        Returns:
            int: the value of `zdirection_mesh_density_parameter` or None if not set
        """
        return self._data["Z-Direction Mesh Density Parameter"]

    @zdirection_mesh_density_parameter.setter
    def zdirection_mesh_density_parameter(self, value=4):
        """  Corresponds to IDD Field `Z-Direction Mesh Density Parameter`
        If mesh type is symmetric geometric, this should be an even number.

        Args:
            value (int): value for IDD Field `Z-Direction Mesh Density Parameter`
                Default value: 4
                value > 0
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
                                     'for field `PipingSystemUndergroundDomain.zdirection_mesh_density_parameter`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundDomain.zdirection_mesh_density_parameter`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `PipingSystemUndergroundDomain.zdirection_mesh_density_parameter`')
        self._data["Z-Direction Mesh Density Parameter"] = value

    @property
    def zdirection_mesh_type(self):
        """Get zdirection_mesh_type

        Returns:
            str: the value of `zdirection_mesh_type` or None if not set
        """
        return self._data["Z-Direction Mesh Type"]

    @zdirection_mesh_type.setter
    def zdirection_mesh_type(self, value=None):
        """  Corresponds to IDD Field `Z-Direction Mesh Type`

        Args:
            value (str): value for IDD Field `Z-Direction Mesh Type`
                Accepted values are:
                      - Uniform
                      - SymmetricGeometric
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
                                 ' for field `PipingSystemUndergroundDomain.zdirection_mesh_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.zdirection_mesh_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.zdirection_mesh_type`')
            vals = {}
            vals["uniform"] = "Uniform"
            vals["symmetricgeometric"] = "SymmetricGeometric"
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
                                     'field `PipingSystemUndergroundDomain.zdirection_mesh_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipingSystemUndergroundDomain.zdirection_mesh_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Z-Direction Mesh Type"] = value

    @property
    def zdirection_geometric_coefficient(self):
        """Get zdirection_geometric_coefficient

        Returns:
            float: the value of `zdirection_geometric_coefficient` or None if not set
        """
        return self._data["Z-Direction Geometric Coefficient"]

    @zdirection_geometric_coefficient.setter
    def zdirection_geometric_coefficient(self, value=1.3):
        """  Corresponds to IDD Field `Z-Direction Geometric Coefficient`
        optional
        Only used if mesh type is symmetric geometric

        Args:
            value (float): value for IDD Field `Z-Direction Geometric Coefficient`
                Default value: 1.3
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.zdirection_geometric_coefficient`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `PipingSystemUndergroundDomain.zdirection_geometric_coefficient`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `PipingSystemUndergroundDomain.zdirection_geometric_coefficient`')
        self._data["Z-Direction Geometric Coefficient"] = value

    @property
    def soil_thermal_conductivity(self):
        """Get soil_thermal_conductivity

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set
        """
        return self._data["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Soil Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`
                Units: W/m-K
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.soil_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_thermal_conductivity`')
        self._data["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """Get soil_density

        Returns:
            float: the value of `soil_density` or None if not set
        """
        return self._data["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """  Corresponds to IDD Field `Soil Density`

        Args:
            value (float): value for IDD Field `Soil Density`
                Units: kg/m3
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_density`')
        self._data["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """Get soil_specific_heat

        Returns:
            float: the value of `soil_specific_heat` or None if not set
        """
        return self._data["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """  Corresponds to IDD Field `Soil Specific Heat`
        This is a dry soil property, which is adjusted for freezing effects
        by the simulation algorithm.

        Args:
            value (float): value for IDD Field `Soil Specific Heat`
                Units: J/kg-K
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundDomain.soil_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_specific_heat`')
        self._data["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """Get soil_moisture_content_volume_fraction

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0):
        """  Corresponds to IDD Field `Soil Moisture Content Volume Fraction`

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction`
                Units: percent
                Default value: 30.0
                value >= 0.0
                value <= 100.0
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
                                 ' for field `PipingSystemUndergroundDomain.soil_moisture_content_volume_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_moisture_content_volume_fraction`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_moisture_content_volume_fraction`')
        self._data["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """Get soil_moisture_content_volume_fraction_at_saturation

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set
        """
        return self._data["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0):
        """  Corresponds to IDD Field `Soil Moisture Content Volume Fraction at Saturation`

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction at Saturation`
                Units: percent
                Default value: 50.0
                value >= 0.0
                value <= 100.0
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
                                 ' for field `PipingSystemUndergroundDomain.soil_moisture_content_volume_fraction_at_saturation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_moisture_content_volume_fraction_at_saturation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `PipingSystemUndergroundDomain.soil_moisture_content_volume_fraction_at_saturation`')
        self._data["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def kusudaachenbach_average_surface_temperature(self):
        """Get kusudaachenbach_average_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `Kusuda-Achenbach Average Surface Temperature`

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Average Surface Temperature`
                Units: C
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
                                 ' for field `PipingSystemUndergroundDomain.kusudaachenbach_average_surface_temperature`'.format(value))
        self._data["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """Get kusudaachenbach_average_amplitude_of_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `Kusuda-Achenbach Average Amplitude of Surface Temperature`

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Average Amplitude of Surface Temperature`
                Units: C
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
                                 ' for field `PipingSystemUndergroundDomain.kusudaachenbach_average_amplitude_of_surface_temperature`'.format(value))
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """Get kusudaachenbach_phase_shift_of_minimum_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`
                Units: days
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
                                 ' for field `PipingSystemUndergroundDomain.kusudaachenbach_phase_shift_of_minimum_surface_temperature`'.format(value))
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def this_domain_includes_basement_surface_interaction(self):
        """Get this_domain_includes_basement_surface_interaction

        Returns:
            str: the value of `this_domain_includes_basement_surface_interaction` or None if not set
        """
        return self._data["This Domain Includes Basement Surface Interaction"]

    @this_domain_includes_basement_surface_interaction.setter
    def this_domain_includes_basement_surface_interaction(self, value="No"):
        """  Corresponds to IDD Field `This Domain Includes Basement Surface Interaction`
        if Yes, then the following basement inputs are used
        if No, then the following basement inputs are *ignored*

        Args:
            value (str): value for IDD Field `This Domain Includes Basement Surface Interaction`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `PipingSystemUndergroundDomain.this_domain_includes_basement_surface_interaction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.this_domain_includes_basement_surface_interaction`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.this_domain_includes_basement_surface_interaction`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `PipingSystemUndergroundDomain.this_domain_includes_basement_surface_interaction`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipingSystemUndergroundDomain.this_domain_includes_basement_surface_interaction`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["This Domain Includes Basement Surface Interaction"] = value

    @property
    def width_of_basement_floor_in_ground_domain(self):
        """Get width_of_basement_floor_in_ground_domain

        Returns:
            float: the value of `width_of_basement_floor_in_ground_domain` or None if not set
        """
        return self._data["Width of Basement Floor in Ground Domain"]

    @width_of_basement_floor_in_ground_domain.setter
    def width_of_basement_floor_in_ground_domain(self, value=None):
        """  Corresponds to IDD Field `Width of Basement Floor in Ground Domain`
        Required only if Domain Has Basement Interaction

        Args:
            value (float): value for IDD Field `Width of Basement Floor in Ground Domain`
                Units: m
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
                                 ' for field `PipingSystemUndergroundDomain.width_of_basement_floor_in_ground_domain`'.format(value))
        self._data["Width of Basement Floor in Ground Domain"] = value

    @property
    def depth_of_basement_wall_in_ground_domain(self):
        """Get depth_of_basement_wall_in_ground_domain

        Returns:
            float: the value of `depth_of_basement_wall_in_ground_domain` or None if not set
        """
        return self._data["Depth of Basement Wall In Ground Domain"]

    @depth_of_basement_wall_in_ground_domain.setter
    def depth_of_basement_wall_in_ground_domain(self, value=None):
        """  Corresponds to IDD Field `Depth of Basement Wall In Ground Domain`
        Required only if Domain Has Basement Interaction

        Args:
            value (float): value for IDD Field `Depth of Basement Wall In Ground Domain`
                Units: m
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
                                 ' for field `PipingSystemUndergroundDomain.depth_of_basement_wall_in_ground_domain`'.format(value))
        self._data["Depth of Basement Wall In Ground Domain"] = value

    @property
    def shift_pipe_x_coordinates_by_basement_width(self):
        """Get shift_pipe_x_coordinates_by_basement_width

        Returns:
            str: the value of `shift_pipe_x_coordinates_by_basement_width` or None if not set
        """
        return self._data["Shift Pipe X Coordinates By Basement Width"]

    @shift_pipe_x_coordinates_by_basement_width.setter
    def shift_pipe_x_coordinates_by_basement_width(self, value=None):
        """  Corresponds to IDD Field `Shift Pipe X Coordinates By Basement Width`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `Shift Pipe X Coordinates By Basement Width`
                Accepted values are:
                      - Yes
                      - No
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
                                 ' for field `PipingSystemUndergroundDomain.shift_pipe_x_coordinates_by_basement_width`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.shift_pipe_x_coordinates_by_basement_width`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.shift_pipe_x_coordinates_by_basement_width`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
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
                                     'field `PipingSystemUndergroundDomain.shift_pipe_x_coordinates_by_basement_width`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipingSystemUndergroundDomain.shift_pipe_x_coordinates_by_basement_width`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Shift Pipe X Coordinates By Basement Width"] = value

    @property
    def name_of_basement_wall_boundary_condition_model(self):
        """Get name_of_basement_wall_boundary_condition_model

        Returns:
            str: the value of `name_of_basement_wall_boundary_condition_model` or None if not set
        """
        return self._data["Name of Basement Wall Boundary Condition Model"]

    @name_of_basement_wall_boundary_condition_model.setter
    def name_of_basement_wall_boundary_condition_model(self, value=None):
        """  Corresponds to IDD Field `Name of Basement Wall Boundary Condition Model`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `Name of Basement Wall Boundary Condition Model`
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
                                 ' for field `PipingSystemUndergroundDomain.name_of_basement_wall_boundary_condition_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.name_of_basement_wall_boundary_condition_model`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.name_of_basement_wall_boundary_condition_model`')
        self._data["Name of Basement Wall Boundary Condition Model"] = value

    @property
    def name_of_basement_floor_boundary_condition_model(self):
        """Get name_of_basement_floor_boundary_condition_model

        Returns:
            str: the value of `name_of_basement_floor_boundary_condition_model` or None if not set
        """
        return self._data["Name of Basement Floor Boundary Condition Model"]

    @name_of_basement_floor_boundary_condition_model.setter
    def name_of_basement_floor_boundary_condition_model(self, value=None):
        """  Corresponds to IDD Field `Name of Basement Floor Boundary Condition Model`
        Required only if Domain Has Basement Interaction

        Args:
            value (str): value for IDD Field `Name of Basement Floor Boundary Condition Model`
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
                                 ' for field `PipingSystemUndergroundDomain.name_of_basement_floor_boundary_condition_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.name_of_basement_floor_boundary_condition_model`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.name_of_basement_floor_boundary_condition_model`')
        self._data["Name of Basement Floor Boundary Condition Model"] = value

    @property
    def convergence_criterion_for_the_outer_cartesian_domain_iteration_loop(self):
        """Get convergence_criterion_for_the_outer_cartesian_domain_iteration_loop

        Returns:
            float: the value of `convergence_criterion_for_the_outer_cartesian_domain_iteration_loop` or None if not set
        """
        return self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"]

    @convergence_criterion_for_the_outer_cartesian_domain_iteration_loop.setter
    def convergence_criterion_for_the_outer_cartesian_domain_iteration_loop(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Criterion for the Outer Cartesian Domain Iteration Loop`

        Args:
            value (float): value for IDD Field `Convergence Criterion for the Outer Cartesian Domain Iteration Loop`
                Units: deltaC
                Default value: 0.001
                value >= 1e-06
                value <= 0.5
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
                                 ' for field `PipingSystemUndergroundDomain.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`'.format(value))
            if value < 1e-06:
                raise ValueError('value need to be greater or equal 1e-06 '
                                 'for field `PipingSystemUndergroundDomain.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `PipingSystemUndergroundDomain.convergence_criterion_for_the_outer_cartesian_domain_iteration_loop`')
        self._data["Convergence Criterion for the Outer Cartesian Domain Iteration Loop"] = value

    @property
    def maximum_iterations_in_the_outer_cartesian_domain_iteration_loop(self):
        """Get maximum_iterations_in_the_outer_cartesian_domain_iteration_loop

        Returns:
            int: the value of `maximum_iterations_in_the_outer_cartesian_domain_iteration_loop` or None if not set
        """
        return self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"]

    @maximum_iterations_in_the_outer_cartesian_domain_iteration_loop.setter
    def maximum_iterations_in_the_outer_cartesian_domain_iteration_loop(self, value=500):
        """  Corresponds to IDD Field `Maximum Iterations in the Outer Cartesian Domain Iteration Loop`

        Args:
            value (int): value for IDD Field `Maximum Iterations in the Outer Cartesian Domain Iteration Loop`
                Default value: 500
                value >= 3
                value <= 10000
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
                                     'for field `PipingSystemUndergroundDomain.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundDomain.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`'.format(value))
            if value < 3:
                raise ValueError('value need to be greater or equal 3 '
                                 'for field `PipingSystemUndergroundDomain.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`')
            if value > 10000:
                raise ValueError('value need to be smaller 10000 '
                                 'for field `PipingSystemUndergroundDomain.maximum_iterations_in_the_outer_cartesian_domain_iteration_loop`')
        self._data["Maximum Iterations in the Outer Cartesian Domain Iteration Loop"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """Get evapotranspiration_ground_cover_parameter

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set
        """
        return self._data["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4):
        """  Corresponds to IDD Field `Evapotranspiration Ground Cover Parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `Evapotranspiration Ground Cover Parameter`
                Default value: 0.4
                value >= 0.0
                value <= 1.5
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
                                 ' for field `PipingSystemUndergroundDomain.evapotranspiration_ground_cover_parameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `PipingSystemUndergroundDomain.evapotranspiration_ground_cover_parameter`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `PipingSystemUndergroundDomain.evapotranspiration_ground_cover_parameter`')
        self._data["Evapotranspiration Ground Cover Parameter"] = value

    @property
    def number_of_pipe_circuits_entered_for_this_domain(self):
        """Get number_of_pipe_circuits_entered_for_this_domain

        Returns:
            int: the value of `number_of_pipe_circuits_entered_for_this_domain` or None if not set
        """
        return self._data["Number of Pipe Circuits Entered for this Domain"]

    @number_of_pipe_circuits_entered_for_this_domain.setter
    def number_of_pipe_circuits_entered_for_this_domain(self, value=None):
        """  Corresponds to IDD Field `Number of Pipe Circuits Entered for this Domain`

        Args:
            value (int): value for IDD Field `Number of Pipe Circuits Entered for this Domain`
                value >= 1
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
                                     'for field `PipingSystemUndergroundDomain.number_of_pipe_circuits_entered_for_this_domain`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundDomain.number_of_pipe_circuits_entered_for_this_domain`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `PipingSystemUndergroundDomain.number_of_pipe_circuits_entered_for_this_domain`')
        self._data["Number of Pipe Circuits Entered for this Domain"] = value

    def add_extensible(self,
                       pipe_circuit_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            pipe_circuit_1 (str): value for IDD Field `Pipe Circuit 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_pipe_circuit_1(pipe_circuit_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_pipe_circuit_1(self, value):
        """ Validates falue of field `Pipe Circuit 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `PipingSystemUndergroundDomain.pipe_circuit_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundDomain.pipe_circuit_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundDomain.pipe_circuit_1`')
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
                    raise ValueError("Required field PipingSystemUndergroundDomain:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipingSystemUndergroundDomain:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipingSystemUndergroundDomain: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipingSystemUndergroundDomain: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipingSystemUndergroundPipeCircuit(object):
    """ Corresponds to IDD object `PipingSystem:Underground:PipeCircuit`
        The pipe circuit object in an underground piping system.
        This object is simulated within an underground piping domain object
        and connected on a branch on a plant loop.
    """
    internal_name = "PipingSystem:Underground:PipeCircuit"
    field_count = 14
    required_fields = ["Name", "Pipe Thermal Conductivity", "Pipe Density", "Pipe Specific Heat", "Pipe Inner Diameter", "Pipe Outer Diameter", "Design Flow Rate", "Circuit Inlet Node", "Circuit Outlet Node", "Radial Thickness of Inner Radial Near Pipe Mesh Region", "Number of Pipe Segments Entered for this Pipe Circuit"]
    extensible_fields = 1
    format = None
    min_fields = 15
    extensible_keys = ["Pipe Segment 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `PipingSystem:Underground:PipeCircuit`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Density"] = None
        self._data["Pipe Specific Heat"] = None
        self._data["Pipe Inner Diameter"] = None
        self._data["Pipe Outer Diameter"] = None
        self._data["Design Flow Rate"] = None
        self._data["Circuit Inlet Node"] = None
        self._data["Circuit Outlet Node"] = None
        self._data["Convergence Criterion for the Inner Radial Iteration Loop"] = None
        self._data["Maximum Iterations in the Inner Radial Iteration Loop"] = None
        self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"] = None
        self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"] = None
        self._data["Number of Pipe Segments Entered for this Pipe Circuit"] = None
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
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_density = None
        else:
            self.pipe_density = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_specific_heat = None
        else:
            self.pipe_specific_heat = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_inner_diameter = None
        else:
            self.pipe_inner_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pipe_outer_diameter = None
        else:
            self.pipe_outer_diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circuit_inlet_node = None
        else:
            self.circuit_inlet_node = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.circuit_outlet_node = None
        else:
            self.circuit_outlet_node = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convergence_criterion_for_the_inner_radial_iteration_loop = None
        else:
            self.convergence_criterion_for_the_inner_radial_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_iterations_in_the_inner_radial_iteration_loop = None
        else:
            self.maximum_iterations_in_the_inner_radial_iteration_loop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = None
        else:
            self.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.radial_thickness_of_inner_radial_near_pipe_mesh_region = None
        else:
            self.radial_thickness_of_inner_radial_near_pipe_mesh_region = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_pipe_segments_entered_for_this_pipe_circuit = None
        else:
            self.number_of_pipe_segments_entered_for_this_pipe_circuit = vals[i]
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
                                 ' for field `PipingSystemUndergroundPipeCircuit.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundPipeCircuit.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundPipeCircuit.name`')
        self._data["Name"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `Pipe Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Pipe Thermal Conductivity`
                Units: W/m-K
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_thermal_conductivity`')
        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_density(self):
        """Get pipe_density

        Returns:
            float: the value of `pipe_density` or None if not set
        """
        return self._data["Pipe Density"]

    @pipe_density.setter
    def pipe_density(self, value=None):
        """  Corresponds to IDD Field `Pipe Density`

        Args:
            value (float): value for IDD Field `Pipe Density`
                Units: kg/m3
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.pipe_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_density`')
        self._data["Pipe Density"] = value

    @property
    def pipe_specific_heat(self):
        """Get pipe_specific_heat

        Returns:
            float: the value of `pipe_specific_heat` or None if not set
        """
        return self._data["Pipe Specific Heat"]

    @pipe_specific_heat.setter
    def pipe_specific_heat(self, value=None):
        """  Corresponds to IDD Field `Pipe Specific Heat`

        Args:
            value (float): value for IDD Field `Pipe Specific Heat`
                Units: J/kg-K
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.pipe_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_specific_heat`')
        self._data["Pipe Specific Heat"] = value

    @property
    def pipe_inner_diameter(self):
        """Get pipe_inner_diameter

        Returns:
            float: the value of `pipe_inner_diameter` or None if not set
        """
        return self._data["Pipe Inner Diameter"]

    @pipe_inner_diameter.setter
    def pipe_inner_diameter(self, value=None):
        """  Corresponds to IDD Field `Pipe Inner Diameter`

        Args:
            value (float): value for IDD Field `Pipe Inner Diameter`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.pipe_inner_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_inner_diameter`')
        self._data["Pipe Inner Diameter"] = value

    @property
    def pipe_outer_diameter(self):
        """Get pipe_outer_diameter

        Returns:
            float: the value of `pipe_outer_diameter` or None if not set
        """
        return self._data["Pipe Outer Diameter"]

    @pipe_outer_diameter.setter
    def pipe_outer_diameter(self, value=None):
        """  Corresponds to IDD Field `Pipe Outer Diameter`

        Args:
            value (float): value for IDD Field `Pipe Outer Diameter`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.pipe_outer_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_outer_diameter`')
        self._data["Pipe Outer Diameter"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Design Flow Rate`

        Args:
            value (float): value for IDD Field `Design Flow Rate`
                Units: m3/s
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.design_flow_rate`')
        self._data["Design Flow Rate"] = value

    @property
    def circuit_inlet_node(self):
        """Get circuit_inlet_node

        Returns:
            str: the value of `circuit_inlet_node` or None if not set
        """
        return self._data["Circuit Inlet Node"]

    @circuit_inlet_node.setter
    def circuit_inlet_node(self, value=None):
        """  Corresponds to IDD Field `Circuit Inlet Node`

        Args:
            value (str): value for IDD Field `Circuit Inlet Node`
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
                                 ' for field `PipingSystemUndergroundPipeCircuit.circuit_inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundPipeCircuit.circuit_inlet_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundPipeCircuit.circuit_inlet_node`')
        self._data["Circuit Inlet Node"] = value

    @property
    def circuit_outlet_node(self):
        """Get circuit_outlet_node

        Returns:
            str: the value of `circuit_outlet_node` or None if not set
        """
        return self._data["Circuit Outlet Node"]

    @circuit_outlet_node.setter
    def circuit_outlet_node(self, value=None):
        """  Corresponds to IDD Field `Circuit Outlet Node`

        Args:
            value (str): value for IDD Field `Circuit Outlet Node`
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
                                 ' for field `PipingSystemUndergroundPipeCircuit.circuit_outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundPipeCircuit.circuit_outlet_node`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundPipeCircuit.circuit_outlet_node`')
        self._data["Circuit Outlet Node"] = value

    @property
    def convergence_criterion_for_the_inner_radial_iteration_loop(self):
        """Get convergence_criterion_for_the_inner_radial_iteration_loop

        Returns:
            float: the value of `convergence_criterion_for_the_inner_radial_iteration_loop` or None if not set
        """
        return self._data["Convergence Criterion for the Inner Radial Iteration Loop"]

    @convergence_criterion_for_the_inner_radial_iteration_loop.setter
    def convergence_criterion_for_the_inner_radial_iteration_loop(self, value=0.001):
        """  Corresponds to IDD Field `Convergence Criterion for the Inner Radial Iteration Loop`

        Args:
            value (float): value for IDD Field `Convergence Criterion for the Inner Radial Iteration Loop`
                Units: deltaC
                Default value: 0.001
                value >= 1e-06
                value <= 0.5
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
                                 ' for field `PipingSystemUndergroundPipeCircuit.convergence_criterion_for_the_inner_radial_iteration_loop`'.format(value))
            if value < 1e-06:
                raise ValueError('value need to be greater or equal 1e-06 '
                                 'for field `PipingSystemUndergroundPipeCircuit.convergence_criterion_for_the_inner_radial_iteration_loop`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `PipingSystemUndergroundPipeCircuit.convergence_criterion_for_the_inner_radial_iteration_loop`')
        self._data["Convergence Criterion for the Inner Radial Iteration Loop"] = value

    @property
    def maximum_iterations_in_the_inner_radial_iteration_loop(self):
        """Get maximum_iterations_in_the_inner_radial_iteration_loop

        Returns:
            int: the value of `maximum_iterations_in_the_inner_radial_iteration_loop` or None if not set
        """
        return self._data["Maximum Iterations in the Inner Radial Iteration Loop"]

    @maximum_iterations_in_the_inner_radial_iteration_loop.setter
    def maximum_iterations_in_the_inner_radial_iteration_loop(self, value=500):
        """  Corresponds to IDD Field `Maximum Iterations in the Inner Radial Iteration Loop`

        Args:
            value (int): value for IDD Field `Maximum Iterations in the Inner Radial Iteration Loop`
                Default value: 500
                value >= 3
                value <= 10000
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
                                     'for field `PipingSystemUndergroundPipeCircuit.maximum_iterations_in_the_inner_radial_iteration_loop`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundPipeCircuit.maximum_iterations_in_the_inner_radial_iteration_loop`'.format(value))
            if value < 3:
                raise ValueError('value need to be greater or equal 3 '
                                 'for field `PipingSystemUndergroundPipeCircuit.maximum_iterations_in_the_inner_radial_iteration_loop`')
            if value > 10000:
                raise ValueError('value need to be smaller 10000 '
                                 'for field `PipingSystemUndergroundPipeCircuit.maximum_iterations_in_the_inner_radial_iteration_loop`')
        self._data["Maximum Iterations in the Inner Radial Iteration Loop"] = value

    @property
    def number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region(self):
        """Get number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region

        Returns:
            int: the value of `number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region` or None if not set
        """
        return self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"]

    @number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region.setter
    def number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region(self, value=3):
        """  Corresponds to IDD Field `Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region`

        Args:
            value (int): value for IDD Field `Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region`
                Default value: 3
                value >= 1
                value <= 15
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
                                     'for field `PipingSystemUndergroundPipeCircuit.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundPipeCircuit.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `PipingSystemUndergroundPipeCircuit.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`')
            if value > 15:
                raise ValueError('value need to be smaller 15 '
                                 'for field `PipingSystemUndergroundPipeCircuit.number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region`')
        self._data["Number of Soil Nodes in the Inner Radial Near Pipe Mesh Region"] = value

    @property
    def radial_thickness_of_inner_radial_near_pipe_mesh_region(self):
        """Get radial_thickness_of_inner_radial_near_pipe_mesh_region

        Returns:
            float: the value of `radial_thickness_of_inner_radial_near_pipe_mesh_region` or None if not set
        """
        return self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"]

    @radial_thickness_of_inner_radial_near_pipe_mesh_region.setter
    def radial_thickness_of_inner_radial_near_pipe_mesh_region(self, value=None):
        """  Corresponds to IDD Field `Radial Thickness of Inner Radial Near Pipe Mesh Region`
        Required because it must be selected by user instead of being
        inferred from circuit/domain object inputs.

        Args:
            value (float): value for IDD Field `Radial Thickness of Inner Radial Near Pipe Mesh Region`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeCircuit.radial_thickness_of_inner_radial_near_pipe_mesh_region`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeCircuit.radial_thickness_of_inner_radial_near_pipe_mesh_region`')
        self._data["Radial Thickness of Inner Radial Near Pipe Mesh Region"] = value

    @property
    def number_of_pipe_segments_entered_for_this_pipe_circuit(self):
        """Get number_of_pipe_segments_entered_for_this_pipe_circuit

        Returns:
            int: the value of `number_of_pipe_segments_entered_for_this_pipe_circuit` or None if not set
        """
        return self._data["Number of Pipe Segments Entered for this Pipe Circuit"]

    @number_of_pipe_segments_entered_for_this_pipe_circuit.setter
    def number_of_pipe_segments_entered_for_this_pipe_circuit(self, value=None):
        """  Corresponds to IDD Field `Number of Pipe Segments Entered for this Pipe Circuit`

        Args:
            value (int): value for IDD Field `Number of Pipe Segments Entered for this Pipe Circuit`
                value >= 1
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
                                     'for field `PipingSystemUndergroundPipeCircuit.number_of_pipe_segments_entered_for_this_pipe_circuit`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `PipingSystemUndergroundPipeCircuit.number_of_pipe_segments_entered_for_this_pipe_circuit`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `PipingSystemUndergroundPipeCircuit.number_of_pipe_segments_entered_for_this_pipe_circuit`')
        self._data["Number of Pipe Segments Entered for this Pipe Circuit"] = value

    def add_extensible(self,
                       pipe_segment_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            pipe_segment_1 (str): value for IDD Field `Pipe Segment 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_pipe_segment_1(pipe_segment_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_pipe_segment_1(self, value):
        """ Validates falue of field `Pipe Segment 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `PipingSystemUndergroundPipeCircuit.pipe_segment_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_segment_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundPipeCircuit.pipe_segment_1`')
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
                    raise ValueError("Required field PipingSystemUndergroundPipeCircuit:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipingSystemUndergroundPipeCircuit:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipingSystemUndergroundPipeCircuit: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipingSystemUndergroundPipeCircuit: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class PipingSystemUndergroundPipeSegment(object):
    """ Corresponds to IDD object `PipingSystem:Underground:PipeSegment`
        The pipe segment to be used in an underground piping system
        This object represents a single pipe leg positioned axially
        in the local z-direction, at a given x, y location in the domain
    """
    internal_name = "PipingSystem:Underground:PipeSegment"
    field_count = 4
    required_fields = ["Name", "X Position", "Y Position", "Flow Direction"]
    extensible_fields = 0
    format = None
    min_fields = 4
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `PipingSystem:Underground:PipeSegment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["X Position"] = None
        self._data["Y Position"] = None
        self._data["Flow Direction"] = None
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
            self.x_position = None
        else:
            self.x_position = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.y_position = None
        else:
            self.y_position = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_direction = None
        else:
            self.flow_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `PipingSystemUndergroundPipeSegment.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundPipeSegment.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundPipeSegment.name`')
        self._data["Name"] = value

    @property
    def x_position(self):
        """Get x_position

        Returns:
            float: the value of `x_position` or None if not set
        """
        return self._data["X Position"]

    @x_position.setter
    def x_position(self, value=None):
        """  Corresponds to IDD Field `X Position`
        This segment will be centered at this distance from the x=0
        domain surface or the basement wall surface, based on whether
        a basement exists in this domain and the selection of the
        shift input field found in the domain object.

        Args:
            value (float): value for IDD Field `X Position`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeSegment.x_position`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeSegment.x_position`')
        self._data["X Position"] = value

    @property
    def y_position(self):
        """Get y_position

        Returns:
            float: the value of `y_position` or None if not set
        """
        return self._data["Y Position"]

    @y_position.setter
    def y_position(self, value=None):
        """  Corresponds to IDD Field `Y Position`
        This segment will be centered at this distance away from the
        ground surface; thus this value represents the burial depth
        of this pipe segment.

        Args:
            value (float): value for IDD Field `Y Position`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `PipingSystemUndergroundPipeSegment.y_position`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `PipingSystemUndergroundPipeSegment.y_position`')
        self._data["Y Position"] = value

    @property
    def flow_direction(self):
        """Get flow_direction

        Returns:
            str: the value of `flow_direction` or None if not set
        """
        return self._data["Flow Direction"]

    @flow_direction.setter
    def flow_direction(self, value=None):
        """  Corresponds to IDD Field `Flow Direction`
        This segment will be simulated such that the flow is in the
        selected direction.  This can allow for detailed analysis
        of circuiting effects in a single domain.

        Args:
            value (str): value for IDD Field `Flow Direction`
                Accepted values are:
                      - IncreasingZ
                      - DecreasingZ
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
                                 ' for field `PipingSystemUndergroundPipeSegment.flow_direction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `PipingSystemUndergroundPipeSegment.flow_direction`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `PipingSystemUndergroundPipeSegment.flow_direction`')
            vals = {}
            vals["increasingz"] = "IncreasingZ"
            vals["decreasingz"] = "DecreasingZ"
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
                                     'field `PipingSystemUndergroundPipeSegment.flow_direction`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `PipingSystemUndergroundPipeSegment.flow_direction`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Flow Direction"] = value

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
                    raise ValueError("Required field PipingSystemUndergroundPipeSegment:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field PipingSystemUndergroundPipeSegment:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for PipingSystemUndergroundPipeSegment: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for PipingSystemUndergroundPipeSegment: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class Duct(object):
    """ Corresponds to IDD object `Duct`
        Passes inlet node state variables to outlet node state variables
    """
    internal_name = "Duct"
    field_count = 3
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Duct`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
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
                                 ' for field `Duct.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Duct.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Duct.name`')
        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
                                 ' for field `Duct.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Duct.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Duct.inlet_node_name`')
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `Duct.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Duct.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Duct.outlet_node_name`')
        self._data["Outlet Node Name"] = value

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
                    raise ValueError("Required field Duct:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Duct:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Duct: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Duct: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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