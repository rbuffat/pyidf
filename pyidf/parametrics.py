""" Data objects in group "Parametrics"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ParametricSetValueForRun(DataObject):

    """ Corresponds to IDD object `Parametric:SetValueForRun`
        Parametric objects allow a set of multiple simulations to be defined in a single idf
        file. The parametric preprocessor scans the idf for Parametric:* objects then creates
        and runs multiple idf files, one for each defined simulation.
        The core parametric object is Parametric:SetValueForRun which defines the name
        of a parameters and sets the parameter to different values depending on which
        run is being simulated.
    """
    _schema = {'extensible-fields': OrderedDict([(u'value for run 1',
                                                  {'name': u'Value for Run 1',
                                                   'pyname': u'value_for_run_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Parametrics',
               'min-fields': 2,
               'name': u'Parametric:SetValueForRun',
               'pyname': u'ParametricSetValueForRun',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Parameter Name
        |  Must begin with the dollar sign character. The second character must be a letter.
        |  Remaining characters may only be letters or numbers. No spaces allowed.

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

    def add_extensible(self,
                       value_for_run_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            value_for_run_1 (str): value for IDD Field `Value for Run 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        value_for_run_1 = self.check_value("Value for Run 1", value_for_run_1)
        vals.append(value_for_run_1)
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




class ParametricLogic(DataObject):

    """ Corresponds to IDD object `Parametric:Logic`
        This object allows some types of objects to be included for some parametric cases and
        not for others. For example, you might want an overhang on a window in some
        parametric runs and not others. A single Parametric:Logic object is allowed per file.
        Consult the Input Output Reference for available commands and syntax.
    """
    _schema = {'extensible-fields': OrderedDict([(u'parametric logic line 1',
                                                  {'name': u'Parametric Logic Line 1',
                                                   'pyname': u'parametric_logic_line_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Parametrics',
               'min-fields': 2,
               'name': u'Parametric:Logic',
               'pyname': u'ParametricLogic',
               'required-object': False,
               'unique-object': True}

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

    def add_extensible(self,
                       parametric_logic_line_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            parametric_logic_line_1 (str): value for IDD Field `Parametric Logic Line 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        parametric_logic_line_1 = self.check_value(
            "Parametric Logic Line 1",
            parametric_logic_line_1)
        vals.append(parametric_logic_line_1)
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




class ParametricRunControl(DataObject):

    """ Corresponds to IDD object `Parametric:RunControl`
        Controls which parametric runs are simulated. This object is optional. If it is not
        included, then all parametric runs are performed.
    """
    _schema = {'extensible-fields': OrderedDict([(u'perform run 1',
                                                  {'name': u'Perform Run 1',
                                                   'pyname': u'perform_run_1',
                                                   'default': u'Yes',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'accepted-values': [u'Yes',
                                                                       u'No'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Parametrics',
               'min-fields': 2,
               'name': u'Parametric:RunControl',
               'pyname': u'ParametricRunControl',
               'required-object': False,
               'unique-object': True}

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

    def add_extensible(self,
                       perform_run_1="Yes",
                       ):
        """Add values for extensible fields.

        Args:

            perform_run_1 (str): value for IDD Field `Perform Run 1`
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        perform_run_1 = self.check_value("Perform Run 1", perform_run_1)
        vals.append(perform_run_1)
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




class ParametricFileNameSuffix(DataObject):

    """ Corresponds to IDD object `Parametric:FileNameSuffix`
        Defines the suffixes to be appended to the idf and output file names for each
        parametric run. If this object is omitted, the suffix will default to the run number.
    """
    _schema = {'extensible-fields': OrderedDict([(u'suffix for file name in run 1',
                                                  {'name': u'Suffix for File Name in Run 1',
                                                   'pyname': u'suffix_for_file_name_in_run_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Parametrics',
               'min-fields': 2,
               'name': u'Parametric:FileNameSuffix',
               'pyname': u'ParametricFileNameSuffix',
               'required-object': False,
               'unique-object': True}

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

    def add_extensible(self,
                       suffix_for_file_name_in_run_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            suffix_for_file_name_in_run_1 (str): value for IDD Field `Suffix for File Name in Run 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        suffix_for_file_name_in_run_1 = self.check_value(
            "Suffix for File Name in Run 1",
            suffix_for_file_name_in_run_1)
        vals.append(suffix_for_file_name_in_run_1)
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


