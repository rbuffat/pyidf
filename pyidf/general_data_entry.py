""" Data objects in group "General Data Entry"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class MatrixTwoDimension(DataObject):

    """ Corresponds to IDD object `Matrix:TwoDimension`
        matrix data in row-major order
        list each row keeping the columns in order
        number of values must equal N1 x N2
    """
    _schema = {'extensible-fields': OrderedDict([(u'value 1',
                                                  {'name': u'Value 1',
                                                   'pyname': u'value_1',
                                                   'required-field': False,
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
                                      (u'number of rows',
                                       {'name': u'Number of Rows',
                                        'pyname': u'number_of_rows',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of columns',
                                       {'name': u'Number of Columns',
                                        'pyname': u'number_of_columns',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'General Data Entry',
               'min-fields': 0,
               'name': u'Matrix:TwoDimension',
               'pyname': u'MatrixTwoDimension',
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
    def number_of_rows(self):
        """field `Number of Rows`

        Args:
            value (int): value for IDD Field `Number of Rows`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_rows` or None if not set

        """
        return self["Number of Rows"]

    @number_of_rows.setter
    def number_of_rows(self, value=None):
        """Corresponds to IDD field `Number of Rows`"""
        self["Number of Rows"] = value

    @property
    def number_of_columns(self):
        """field `Number of Columns`

        Args:
            value (int): value for IDD Field `Number of Columns`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_columns` or None if not set

        """
        return self["Number of Columns"]

    @number_of_columns.setter
    def number_of_columns(self, value=None):
        """Corresponds to IDD field `Number of Columns`"""
        self["Number of Columns"] = value

    def add_extensible(self,
                       value_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            value_1 (float): value for IDD Field `Value 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        value_1 = self.check_value("Value 1", value_1)
        vals.append(value_1)
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


