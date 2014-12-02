from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class LoadProfilePlant(object):
    """ Corresponds to IDD object `LoadProfile:Plant`
        Used to simulate a scheduled plant loop demand profile.  Load and flow rate are
        specified using schedules. Positive values are heating loads, and negative values are
        cooling loads. The actual load met is dependent on the performance of the supply
        loop components.
    """
    internal_name = "LoadProfile:Plant"
    field_count = 6
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Load Schedule Name", "Peak Flow Rate", "Flow Rate Fraction Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `LoadProfile:Plant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Load Schedule Name"] = None
        self._data["Peak Flow Rate"] = None
        self._data["Flow Rate Fraction Schedule Name"] = None
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
        if len(vals[i]) == 0:
            self.load_schedule_name = None
        else:
            self.load_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.peak_flow_rate = None
        else:
            self.peak_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_rate_fraction_schedule_name = None
        else:
            self.flow_rate_fraction_schedule_name = vals[i]
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
                                 ' for field `LoadProfilePlant.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `LoadProfilePlant.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `LoadProfilePlant.name`')
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
                                 ' for field `LoadProfilePlant.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `LoadProfilePlant.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `LoadProfilePlant.inlet_node_name`')
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
                                 ' for field `LoadProfilePlant.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `LoadProfilePlant.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `LoadProfilePlant.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def load_schedule_name(self):
        """Get load_schedule_name

        Returns:
            str: the value of `load_schedule_name` or None if not set
        """
        return self._data["Load Schedule Name"]

    @load_schedule_name.setter
    def load_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Load Schedule Name`
        Schedule values are load in [W]

        Args:
            value (str): value for IDD Field `Load Schedule Name`
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
                                 ' for field `LoadProfilePlant.load_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `LoadProfilePlant.load_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `LoadProfilePlant.load_schedule_name`')
        self._data["Load Schedule Name"] = value

    @property
    def peak_flow_rate(self):
        """Get peak_flow_rate

        Returns:
            float: the value of `peak_flow_rate` or None if not set
        """
        return self._data["Peak Flow Rate"]

    @peak_flow_rate.setter
    def peak_flow_rate(self, value=None):
        """  Corresponds to IDD Field `Peak Flow Rate`

        Args:
            value (float): value for IDD Field `Peak Flow Rate`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `LoadProfilePlant.peak_flow_rate`'.format(value))
        self._data["Peak Flow Rate"] = value

    @property
    def flow_rate_fraction_schedule_name(self):
        """Get flow_rate_fraction_schedule_name

        Returns:
            str: the value of `flow_rate_fraction_schedule_name` or None if not set
        """
        return self._data["Flow Rate Fraction Schedule Name"]

    @flow_rate_fraction_schedule_name.setter
    def flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Flow Rate Fraction Schedule Name`

        Args:
            value (str): value for IDD Field `Flow Rate Fraction Schedule Name`
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
                                 ' for field `LoadProfilePlant.flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `LoadProfilePlant.flow_rate_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `LoadProfilePlant.flow_rate_fraction_schedule_name`')
        self._data["Flow Rate Fraction Schedule Name"] = value

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
                    raise ValueError("Required field LoadProfilePlant:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field LoadProfilePlant:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for LoadProfilePlant: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for LoadProfilePlant: {} / {}".format(out_fields,
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