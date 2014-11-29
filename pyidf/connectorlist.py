from collections import OrderedDict

class ConnectorList(object):
    """ Corresponds to IDD object `ConnectorList`
        only two connectors allowed per loop
        if two entered, one must be Connector:Splitter and one must be Connector:Mixer
    """
    internal_name = "ConnectorList"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ConnectorList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Connector 1 Object Type"] = None
        self._data["Connector 1 Name"] = None
        self._data["Connector 2 Object Type"] = None
        self._data["Connector 2 Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.connector_1_object_type = None
        else:
            self.connector_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.connector_1_name = None
        else:
            self.connector_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.connector_2_object_type = None
        else:
            self.connector_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.connector_2_name = None
        else:
            self.connector_2_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `connector_1_object_type`

        Args:
            value (str): value for IDD Field `connector_1_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_1_object_type`')
            vals = set()
            vals.add("Connector:Splitter")
            vals.add("Connector:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `connector_1_object_type`'.format(value))

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
        """  Corresponds to IDD Field `connector_1_name`

        Args:
            value (str): value for IDD Field `connector_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_1_name`')

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
        """  Corresponds to IDD Field `connector_2_object_type`

        Args:
            value (str): value for IDD Field `connector_2_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_2_object_type`')
            vals = set()
            vals.add("Connector:Splitter")
            vals.add("Connector:Mixer")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `connector_2_object_type`'.format(value))

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
        """  Corresponds to IDD Field `connector_2_name`

        Args:
            value (str): value for IDD Field `connector_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `connector_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `connector_2_name`')

        self._data["Connector 2 Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.connector_1_object_type))
        out.append(self._to_str(self.connector_1_name))
        out.append(self._to_str(self.connector_2_object_type))
        out.append(self._to_str(self.connector_2_name))
        return ",".join(out)