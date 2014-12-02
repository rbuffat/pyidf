from collections import OrderedDict
import logging
import re

class MatrixTwoDimension(object):
    """ Corresponds to IDD object `Matrix:TwoDimension`
        matrix data in row-major order
        list each row keeping the columns in order
        number of values must equal N1 x N2
    """
    internal_name = "Matrix:TwoDimension"
    field_count = 3
    required_fields = ["Name", "Number of Rows", "Number of Columns"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Matrix:TwoDimension`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Number of Rows"] = None
        self._data["Number of Columns"] = None
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
            self.number_of_rows = None
        else:
            self.number_of_rows = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_columns = None
        else:
            self.number_of_columns = vals[i]
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def number_of_rows(self):
        """Get number_of_rows

        Returns:
            int: the value of `number_of_rows` or None if not set
        """
        return self._data["Number of Rows"]

    @number_of_rows.setter
    def number_of_rows(self, value=None):
        """  Corresponds to IDD Field `Number of Rows`

        Args:
            value (int): value for IDD Field `Number of Rows`
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
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `number_of_rows`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `number_of_rows`'.format(value))
        self._data["Number of Rows"] = value

    @property
    def number_of_columns(self):
        """Get number_of_columns

        Returns:
            int: the value of `number_of_columns` or None if not set
        """
        return self._data["Number of Columns"]

    @number_of_columns.setter
    def number_of_columns(self, value=None):
        """  Corresponds to IDD Field `Number of Columns`

        Args:
            value (int): value for IDD Field `Number of Columns`
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
                        logging.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `number_of_columns`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `number_of_columns`'.format(value))
        self._data["Number of Columns"] = value

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