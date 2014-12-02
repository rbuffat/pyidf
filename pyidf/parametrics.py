from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ParametricSetValueForRun(object):
    """ Corresponds to IDD object `Parametric:SetValueForRun`
        Parametric objects allow a set of multiple simulations to be defined in a single idf
        file. The parametric preprocessor scans the idf for Parametric:* objects then creates
        and runs multiple idf files, one for each defined simulation.
        The core parametric object is Parametric:SetValueForRun which defines the name
        of a parameters and sets the parameter to different values depending on which
        run is being simulated.
    """
    internal_name = "Parametric:SetValueForRun"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Value for Run 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:SetValueForRun`
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
        Parameter Name
        Must begin with the dollar sign character. The second character must be a letter.
        Remaining characters may only be letters or numbers. No spaces allowed.

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
                                 ' for field `ParametricSetValueForRun.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricSetValueForRun.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricSetValueForRun.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       value_for_run_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            value_for_run_1 (str): value for IDD Field `Value for Run 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_value_for_run_1(value_for_run_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_value_for_run_1(self, value):
        """ Validates falue of field `Value for Run 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ParametricSetValueForRun.value_for_run_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricSetValueForRun.value_for_run_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricSetValueForRun.value_for_run_1`')
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
                    raise ValueError("Required field ParametricSetValueForRun:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ParametricSetValueForRun:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ParametricSetValueForRun: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ParametricSetValueForRun: {} / {}".format(out_fields,
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

class ParametricLogic(object):
    """ Corresponds to IDD object `Parametric:Logic`
        This object allows some types of objects to be included for some parametric cases and
        not for others. For example, you might want an overhang on a window in some
        parametric runs and not others. A single Parametric:Logic object is allowed per file.
        Consult the Input Output Reference for available commands and syntax.
    """
    internal_name = "Parametric:Logic"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Parametric Logic Line 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:Logic`
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
                                 ' for field `ParametricLogic.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricLogic.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricLogic.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       parametric_logic_line_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            parametric_logic_line_1 (str): value for IDD Field `Parametric Logic Line 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_parametric_logic_line_1(parametric_logic_line_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_parametric_logic_line_1(self, value):
        """ Validates falue of field `Parametric Logic Line 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ParametricLogic.parametric_logic_line_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricLogic.parametric_logic_line_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricLogic.parametric_logic_line_1`')
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
                    raise ValueError("Required field ParametricLogic:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ParametricLogic:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ParametricLogic: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ParametricLogic: {} / {}".format(out_fields,
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

class ParametricRunControl(object):
    """ Corresponds to IDD object `Parametric:RunControl`
        Controls which parametric runs are simulated. This object is optional. If it is not
        included, then all parametric runs are performed.
    """
    internal_name = "Parametric:RunControl"
    field_count = 1
    required_fields = []
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Perform Run 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:RunControl`
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
                                 ' for field `ParametricRunControl.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricRunControl.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricRunControl.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       perform_run_1="Yes",
                       ):
        """ Add values for extensible fields

        Args:

            perform_run_1 (str): value for IDD Field `Perform Run 1`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_perform_run_1(perform_run_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_perform_run_1(self, value):
        """ Validates falue of field `Perform Run 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ParametricRunControl.perform_run_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricRunControl.perform_run_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricRunControl.perform_run_1`')
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
                                     'field `ParametricRunControl.perform_run_1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ParametricRunControl.perform_run_1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
                    raise ValueError("Required field ParametricRunControl:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ParametricRunControl:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ParametricRunControl: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ParametricRunControl: {} / {}".format(out_fields,
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

class ParametricFileNameSuffix(object):
    """ Corresponds to IDD object `Parametric:FileNameSuffix`
        Defines the suffixes to be appended to the idf and output file names for each
        parametric run. If this object is omitted, the suffix will default to the run number.
    """
    internal_name = "Parametric:FileNameSuffix"
    field_count = 1
    required_fields = []
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Suffix for File Name in Run 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:FileNameSuffix`
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
                                 ' for field `ParametricFileNameSuffix.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricFileNameSuffix.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricFileNameSuffix.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       suffix_for_file_name_in_run_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            suffix_for_file_name_in_run_1 (str): value for IDD Field `Suffix for File Name in Run 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_suffix_for_file_name_in_run_1(suffix_for_file_name_in_run_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_suffix_for_file_name_in_run_1(self, value):
        """ Validates falue of field `Suffix for File Name in Run 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ParametricFileNameSuffix.suffix_for_file_name_in_run_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ParametricFileNameSuffix.suffix_for_file_name_in_run_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ParametricFileNameSuffix.suffix_for_file_name_in_run_1`')
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
                    raise ValueError("Required field ParametricFileNameSuffix:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ParametricFileNameSuffix:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ParametricFileNameSuffix: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ParametricFileNameSuffix: {} / {}".format(out_fields,
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