from collections import OrderedDict

class ConstructionWindowEquivalentLayer(object):
    """ Corresponds to IDD object `Construction:WindowEquivalentLayer`
        Start with outside layer and work your way to the inside Layer
        Up to 11 layers total. Up to six solid layers and up to five gaps.
        Enter the material name for each layer
    """
    internal_name = "Construction:WindowEquivalentLayer"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction:WindowEquivalentLayer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outside Layer"] = None
        self._data["Layer 2"] = None
        self._data["Layer 3"] = None
        self._data["Layer 4"] = None
        self._data["Layer 5"] = None
        self._data["Layer 6"] = None
        self._data["Layer 7"] = None
        self._data["Layer 8"] = None
        self._data["Layer 9"] = None
        self._data["Layer 10"] = None
        self._data["Layer 11"] = None

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
            self.outside_layer = None
        else:
            self.outside_layer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2 = None
        else:
            self.layer_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3 = None
        else:
            self.layer_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4 = None
        else:
            self.layer_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5 = None
        else:
            self.layer_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_6 = None
        else:
            self.layer_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_7 = None
        else:
            self.layer_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_8 = None
        else:
            self.layer_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_9 = None
        else:
            self.layer_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_10 = None
        else:
            self.layer_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_11 = None
        else:
            self.layer_11 = vals[i]
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
    def outside_layer(self):
        """Get outside_layer

        Returns:
            str: the value of `outside_layer` or None if not set
        """
        return self._data["Outside Layer"]

    @outside_layer.setter
    def outside_layer(self, value=None):
        """  Corresponds to IDD Field `outside_layer`

        Args:
            value (str): value for IDD Field `outside_layer`
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
                                 'for field `outside_layer`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_layer`')

        self._data["Outside Layer"] = value

    @property
    def layer_2(self):
        """Get layer_2

        Returns:
            str: the value of `layer_2` or None if not set
        """
        return self._data["Layer 2"]

    @layer_2.setter
    def layer_2(self, value=None):
        """  Corresponds to IDD Field `layer_2`

        Args:
            value (str): value for IDD Field `layer_2`
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
                                 'for field `layer_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2`')

        self._data["Layer 2"] = value

    @property
    def layer_3(self):
        """Get layer_3

        Returns:
            str: the value of `layer_3` or None if not set
        """
        return self._data["Layer 3"]

    @layer_3.setter
    def layer_3(self, value=None):
        """  Corresponds to IDD Field `layer_3`

        Args:
            value (str): value for IDD Field `layer_3`
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
                                 'for field `layer_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3`')

        self._data["Layer 3"] = value

    @property
    def layer_4(self):
        """Get layer_4

        Returns:
            str: the value of `layer_4` or None if not set
        """
        return self._data["Layer 4"]

    @layer_4.setter
    def layer_4(self, value=None):
        """  Corresponds to IDD Field `layer_4`

        Args:
            value (str): value for IDD Field `layer_4`
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
                                 'for field `layer_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4`')

        self._data["Layer 4"] = value

    @property
    def layer_5(self):
        """Get layer_5

        Returns:
            str: the value of `layer_5` or None if not set
        """
        return self._data["Layer 5"]

    @layer_5.setter
    def layer_5(self, value=None):
        """  Corresponds to IDD Field `layer_5`

        Args:
            value (str): value for IDD Field `layer_5`
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
                                 'for field `layer_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5`')

        self._data["Layer 5"] = value

    @property
    def layer_6(self):
        """Get layer_6

        Returns:
            str: the value of `layer_6` or None if not set
        """
        return self._data["Layer 6"]

    @layer_6.setter
    def layer_6(self, value=None):
        """  Corresponds to IDD Field `layer_6`

        Args:
            value (str): value for IDD Field `layer_6`
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
                                 'for field `layer_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_6`')

        self._data["Layer 6"] = value

    @property
    def layer_7(self):
        """Get layer_7

        Returns:
            str: the value of `layer_7` or None if not set
        """
        return self._data["Layer 7"]

    @layer_7.setter
    def layer_7(self, value=None):
        """  Corresponds to IDD Field `layer_7`

        Args:
            value (str): value for IDD Field `layer_7`
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
                                 'for field `layer_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_7`')

        self._data["Layer 7"] = value

    @property
    def layer_8(self):
        """Get layer_8

        Returns:
            str: the value of `layer_8` or None if not set
        """
        return self._data["Layer 8"]

    @layer_8.setter
    def layer_8(self, value=None):
        """  Corresponds to IDD Field `layer_8`

        Args:
            value (str): value for IDD Field `layer_8`
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
                                 'for field `layer_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_8`')

        self._data["Layer 8"] = value

    @property
    def layer_9(self):
        """Get layer_9

        Returns:
            str: the value of `layer_9` or None if not set
        """
        return self._data["Layer 9"]

    @layer_9.setter
    def layer_9(self, value=None):
        """  Corresponds to IDD Field `layer_9`

        Args:
            value (str): value for IDD Field `layer_9`
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
                                 'for field `layer_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_9`')

        self._data["Layer 9"] = value

    @property
    def layer_10(self):
        """Get layer_10

        Returns:
            str: the value of `layer_10` or None if not set
        """
        return self._data["Layer 10"]

    @layer_10.setter
    def layer_10(self, value=None):
        """  Corresponds to IDD Field `layer_10`

        Args:
            value (str): value for IDD Field `layer_10`
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
                                 'for field `layer_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_10`')

        self._data["Layer 10"] = value

    @property
    def layer_11(self):
        """Get layer_11

        Returns:
            str: the value of `layer_11` or None if not set
        """
        return self._data["Layer 11"]

    @layer_11.setter
    def layer_11(self, value=None):
        """  Corresponds to IDD Field `layer_11`

        Args:
            value (str): value for IDD Field `layer_11`
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
                                 'for field `layer_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_11`')

        self._data["Layer 11"] = value

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
        out.append(self._to_str(self.outside_layer))
        out.append(self._to_str(self.layer_2))
        out.append(self._to_str(self.layer_3))
        out.append(self._to_str(self.layer_4))
        out.append(self._to_str(self.layer_5))
        out.append(self._to_str(self.layer_6))
        out.append(self._to_str(self.layer_7))
        out.append(self._to_str(self.layer_8))
        out.append(self._to_str(self.layer_9))
        out.append(self._to_str(self.layer_10))
        out.append(self._to_str(self.layer_11))
        return ",".join(out)

class Construction(object):
    """ Corresponds to IDD object `Construction`
        Start with outside layer and work your way to the inside layer
        Up to 10 layers total, 8 for windows
        Enter the material name for each layer
    """
    internal_name = "Construction"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outside Layer"] = None
        self._data["Layer 2"] = None
        self._data["Layer 3"] = None
        self._data["Layer 4"] = None
        self._data["Layer 5"] = None
        self._data["Layer 6"] = None
        self._data["Layer 7"] = None
        self._data["Layer 8"] = None
        self._data["Layer 9"] = None
        self._data["Layer 10"] = None

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
            self.outside_layer = None
        else:
            self.outside_layer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2 = None
        else:
            self.layer_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3 = None
        else:
            self.layer_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4 = None
        else:
            self.layer_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5 = None
        else:
            self.layer_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_6 = None
        else:
            self.layer_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_7 = None
        else:
            self.layer_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_8 = None
        else:
            self.layer_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_9 = None
        else:
            self.layer_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_10 = None
        else:
            self.layer_10 = vals[i]
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
    def outside_layer(self):
        """Get outside_layer

        Returns:
            str: the value of `outside_layer` or None if not set
        """
        return self._data["Outside Layer"]

    @outside_layer.setter
    def outside_layer(self, value=None):
        """  Corresponds to IDD Field `outside_layer`

        Args:
            value (str): value for IDD Field `outside_layer`
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
                                 'for field `outside_layer`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_layer`')

        self._data["Outside Layer"] = value

    @property
    def layer_2(self):
        """Get layer_2

        Returns:
            str: the value of `layer_2` or None if not set
        """
        return self._data["Layer 2"]

    @layer_2.setter
    def layer_2(self, value=None):
        """  Corresponds to IDD Field `layer_2`

        Args:
            value (str): value for IDD Field `layer_2`
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
                                 'for field `layer_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2`')

        self._data["Layer 2"] = value

    @property
    def layer_3(self):
        """Get layer_3

        Returns:
            str: the value of `layer_3` or None if not set
        """
        return self._data["Layer 3"]

    @layer_3.setter
    def layer_3(self, value=None):
        """  Corresponds to IDD Field `layer_3`

        Args:
            value (str): value for IDD Field `layer_3`
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
                                 'for field `layer_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3`')

        self._data["Layer 3"] = value

    @property
    def layer_4(self):
        """Get layer_4

        Returns:
            str: the value of `layer_4` or None if not set
        """
        return self._data["Layer 4"]

    @layer_4.setter
    def layer_4(self, value=None):
        """  Corresponds to IDD Field `layer_4`

        Args:
            value (str): value for IDD Field `layer_4`
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
                                 'for field `layer_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4`')

        self._data["Layer 4"] = value

    @property
    def layer_5(self):
        """Get layer_5

        Returns:
            str: the value of `layer_5` or None if not set
        """
        return self._data["Layer 5"]

    @layer_5.setter
    def layer_5(self, value=None):
        """  Corresponds to IDD Field `layer_5`

        Args:
            value (str): value for IDD Field `layer_5`
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
                                 'for field `layer_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5`')

        self._data["Layer 5"] = value

    @property
    def layer_6(self):
        """Get layer_6

        Returns:
            str: the value of `layer_6` or None if not set
        """
        return self._data["Layer 6"]

    @layer_6.setter
    def layer_6(self, value=None):
        """  Corresponds to IDD Field `layer_6`

        Args:
            value (str): value for IDD Field `layer_6`
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
                                 'for field `layer_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_6`')

        self._data["Layer 6"] = value

    @property
    def layer_7(self):
        """Get layer_7

        Returns:
            str: the value of `layer_7` or None if not set
        """
        return self._data["Layer 7"]

    @layer_7.setter
    def layer_7(self, value=None):
        """  Corresponds to IDD Field `layer_7`

        Args:
            value (str): value for IDD Field `layer_7`
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
                                 'for field `layer_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_7`')

        self._data["Layer 7"] = value

    @property
    def layer_8(self):
        """Get layer_8

        Returns:
            str: the value of `layer_8` or None if not set
        """
        return self._data["Layer 8"]

    @layer_8.setter
    def layer_8(self, value=None):
        """  Corresponds to IDD Field `layer_8`

        Args:
            value (str): value for IDD Field `layer_8`
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
                                 'for field `layer_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_8`')

        self._data["Layer 8"] = value

    @property
    def layer_9(self):
        """Get layer_9

        Returns:
            str: the value of `layer_9` or None if not set
        """
        return self._data["Layer 9"]

    @layer_9.setter
    def layer_9(self, value=None):
        """  Corresponds to IDD Field `layer_9`

        Args:
            value (str): value for IDD Field `layer_9`
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
                                 'for field `layer_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_9`')

        self._data["Layer 9"] = value

    @property
    def layer_10(self):
        """Get layer_10

        Returns:
            str: the value of `layer_10` or None if not set
        """
        return self._data["Layer 10"]

    @layer_10.setter
    def layer_10(self, value=None):
        """  Corresponds to IDD Field `layer_10`

        Args:
            value (str): value for IDD Field `layer_10`
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
                                 'for field `layer_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_10`')

        self._data["Layer 10"] = value

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
        out.append(self._to_str(self.outside_layer))
        out.append(self._to_str(self.layer_2))
        out.append(self._to_str(self.layer_3))
        out.append(self._to_str(self.layer_4))
        out.append(self._to_str(self.layer_5))
        out.append(self._to_str(self.layer_6))
        out.append(self._to_str(self.layer_7))
        out.append(self._to_str(self.layer_8))
        out.append(self._to_str(self.layer_9))
        out.append(self._to_str(self.layer_10))
        return ",".join(out)

class ConstructionCfactorUndergroundWall(object):
    """ Corresponds to IDD object `Construction:CfactorUndergroundWall`
        Alternate method of describing underground wall constructions
    """
    internal_name = "Construction:CfactorUndergroundWall"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction:CfactorUndergroundWall`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["C-Factor"] = None
        self._data["Height"] = None

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
            self.cfactor = None
        else:
            self.cfactor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
    def cfactor(self):
        """Get cfactor

        Returns:
            float: the value of `cfactor` or None if not set
        """
        return self._data["C-Factor"]

    @cfactor.setter
    def cfactor(self, value=None):
        """  Corresponds to IDD Field `cfactor`
        Enter C-Factor without film coefficients or soil

        Args:
            value (float): value for IDD Field `cfactor`
                Unit: W/m2-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cfactor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cfactor`')

        self._data["C-Factor"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `height`
        Enter height of the underground wall

        Args:
            value (float): value for IDD Field `height`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `height`')

        self._data["Height"] = value

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
        out.append(self._to_str(self.cfactor))
        out.append(self._to_str(self.height))
        return ",".join(out)

class ConstructionFfactorGroundFloor(object):
    """ Corresponds to IDD object `Construction:FfactorGroundFloor`
        Alternate method of describing slab-on-grade or underground floor constructions
    """
    internal_name = "Construction:FfactorGroundFloor"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction:FfactorGroundFloor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["F-Factor"] = None
        self._data["Area"] = None
        self._data["PerimeterExposed"] = None

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
            self.ffactor = None
        else:
            self.ffactor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.area = None
        else:
            self.area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.perimeterexposed = None
        else:
            self.perimeterexposed = vals[i]
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
    def ffactor(self):
        """Get ffactor

        Returns:
            float: the value of `ffactor` or None if not set
        """
        return self._data["F-Factor"]

    @ffactor.setter
    def ffactor(self, value=None):
        """  Corresponds to IDD Field `ffactor`

        Args:
            value (float): value for IDD Field `ffactor`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ffactor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ffactor`')

        self._data["F-Factor"] = value

    @property
    def area(self):
        """Get area

        Returns:
            float: the value of `area` or None if not set
        """
        return self._data["Area"]

    @area.setter
    def area(self, value=None):
        """  Corresponds to IDD Field `area`
        Enter area of the floor

        Args:
            value (float): value for IDD Field `area`
                Unit: m2
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `area`')

        self._data["Area"] = value

    @property
    def perimeterexposed(self):
        """Get perimeterexposed

        Returns:
            float: the value of `perimeterexposed` or None if not set
        """
        return self._data["PerimeterExposed"]

    @perimeterexposed.setter
    def perimeterexposed(self, value=None):
        """  Corresponds to IDD Field `perimeterexposed`
        Enter exposed perimeter of the floor

        Args:
            value (float): value for IDD Field `perimeterexposed`
                Unit: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `perimeterexposed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `perimeterexposed`')

        self._data["PerimeterExposed"] = value

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
        out.append(self._to_str(self.ffactor))
        out.append(self._to_str(self.area))
        out.append(self._to_str(self.perimeterexposed))
        return ",".join(out)

class ConstructionInternalSource(object):
    """ Corresponds to IDD object `Construction:InternalSource`
        Start with outside layer and work your way to the inside Layer
        Up to 10 layers total, 8 for windows
        Enter the material name for each layer
    """
    internal_name = "Construction:InternalSource"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction:InternalSource`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Source Present After Layer Number"] = None
        self._data["Temperature Calculation Requested After Layer Number"] = None
        self._data["Dimensions for the CTF Calculation"] = None
        self._data["Tube Spacing"] = None
        self._data["Outside Layer"] = None
        self._data["Layer 2"] = None
        self._data["Layer 3"] = None
        self._data["Layer 4"] = None
        self._data["Layer 5"] = None
        self._data["Layer 6"] = None
        self._data["Layer 7"] = None
        self._data["Layer 8"] = None
        self._data["Layer 9"] = None
        self._data["Layer 10"] = None

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
            self.source_present_after_layer_number = None
        else:
            self.source_present_after_layer_number = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_calculation_requested_after_layer_number = None
        else:
            self.temperature_calculation_requested_after_layer_number = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.dimensions_for_the_ctf_calculation = None
        else:
            self.dimensions_for_the_ctf_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tube_spacing = None
        else:
            self.tube_spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_layer = None
        else:
            self.outside_layer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2 = None
        else:
            self.layer_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3 = None
        else:
            self.layer_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4 = None
        else:
            self.layer_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5 = None
        else:
            self.layer_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_6 = None
        else:
            self.layer_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_7 = None
        else:
            self.layer_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_8 = None
        else:
            self.layer_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_9 = None
        else:
            self.layer_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_10 = None
        else:
            self.layer_10 = vals[i]
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
    def source_present_after_layer_number(self):
        """Get source_present_after_layer_number

        Returns:
            int: the value of `source_present_after_layer_number` or None if not set
        """
        return self._data["Source Present After Layer Number"]

    @source_present_after_layer_number.setter
    def source_present_after_layer_number(self, value=None):
        """  Corresponds to IDD Field `source_present_after_layer_number`
        refers to the list of materials which follows

        Args:
            value (int): value for IDD Field `source_present_after_layer_number`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `source_present_after_layer_number`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `source_present_after_layer_number`')

        self._data["Source Present After Layer Number"] = value

    @property
    def temperature_calculation_requested_after_layer_number(self):
        """Get temperature_calculation_requested_after_layer_number

        Returns:
            int: the value of `temperature_calculation_requested_after_layer_number` or None if not set
        """
        return self._data["Temperature Calculation Requested After Layer Number"]

    @temperature_calculation_requested_after_layer_number.setter
    def temperature_calculation_requested_after_layer_number(self, value=None):
        """  Corresponds to IDD Field `temperature_calculation_requested_after_layer_number`
        refers to the list of materials which follows

        Args:
            value (int): value for IDD Field `temperature_calculation_requested_after_layer_number`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `temperature_calculation_requested_after_layer_number`'.format(value))

        self._data["Temperature Calculation Requested After Layer Number"] = value

    @property
    def dimensions_for_the_ctf_calculation(self):
        """Get dimensions_for_the_ctf_calculation

        Returns:
            int: the value of `dimensions_for_the_ctf_calculation` or None if not set
        """
        return self._data["Dimensions for the CTF Calculation"]

    @dimensions_for_the_ctf_calculation.setter
    def dimensions_for_the_ctf_calculation(self, value=None):
        """  Corresponds to IDD Field `dimensions_for_the_ctf_calculation`
        1 = 1-dimensional calculation, 2 = 2-dimensional calculation

        Args:
            value (int): value for IDD Field `dimensions_for_the_ctf_calculation`
                value >= 1
                value <= 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `dimensions_for_the_ctf_calculation`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `dimensions_for_the_ctf_calculation`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `dimensions_for_the_ctf_calculation`')

        self._data["Dimensions for the CTF Calculation"] = value

    @property
    def tube_spacing(self):
        """Get tube_spacing

        Returns:
            float: the value of `tube_spacing` or None if not set
        """
        return self._data["Tube Spacing"]

    @tube_spacing.setter
    def tube_spacing(self, value=None):
        """  Corresponds to IDD Field `tube_spacing`
        uniform spacing between tubes or resistance wires in direction
        perpendicular to main intended direction of heat transfer

        Args:
            value (float): value for IDD Field `tube_spacing`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `tube_spacing`'.format(value))

        self._data["Tube Spacing"] = value

    @property
    def outside_layer(self):
        """Get outside_layer

        Returns:
            str: the value of `outside_layer` or None if not set
        """
        return self._data["Outside Layer"]

    @outside_layer.setter
    def outside_layer(self, value=None):
        """  Corresponds to IDD Field `outside_layer`

        Args:
            value (str): value for IDD Field `outside_layer`
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
                                 'for field `outside_layer`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_layer`')

        self._data["Outside Layer"] = value

    @property
    def layer_2(self):
        """Get layer_2

        Returns:
            str: the value of `layer_2` or None if not set
        """
        return self._data["Layer 2"]

    @layer_2.setter
    def layer_2(self, value=None):
        """  Corresponds to IDD Field `layer_2`

        Args:
            value (str): value for IDD Field `layer_2`
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
                                 'for field `layer_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2`')

        self._data["Layer 2"] = value

    @property
    def layer_3(self):
        """Get layer_3

        Returns:
            str: the value of `layer_3` or None if not set
        """
        return self._data["Layer 3"]

    @layer_3.setter
    def layer_3(self, value=None):
        """  Corresponds to IDD Field `layer_3`

        Args:
            value (str): value for IDD Field `layer_3`
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
                                 'for field `layer_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3`')

        self._data["Layer 3"] = value

    @property
    def layer_4(self):
        """Get layer_4

        Returns:
            str: the value of `layer_4` or None if not set
        """
        return self._data["Layer 4"]

    @layer_4.setter
    def layer_4(self, value=None):
        """  Corresponds to IDD Field `layer_4`

        Args:
            value (str): value for IDD Field `layer_4`
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
                                 'for field `layer_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4`')

        self._data["Layer 4"] = value

    @property
    def layer_5(self):
        """Get layer_5

        Returns:
            str: the value of `layer_5` or None if not set
        """
        return self._data["Layer 5"]

    @layer_5.setter
    def layer_5(self, value=None):
        """  Corresponds to IDD Field `layer_5`

        Args:
            value (str): value for IDD Field `layer_5`
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
                                 'for field `layer_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5`')

        self._data["Layer 5"] = value

    @property
    def layer_6(self):
        """Get layer_6

        Returns:
            str: the value of `layer_6` or None if not set
        """
        return self._data["Layer 6"]

    @layer_6.setter
    def layer_6(self, value=None):
        """  Corresponds to IDD Field `layer_6`

        Args:
            value (str): value for IDD Field `layer_6`
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
                                 'for field `layer_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_6`')

        self._data["Layer 6"] = value

    @property
    def layer_7(self):
        """Get layer_7

        Returns:
            str: the value of `layer_7` or None if not set
        """
        return self._data["Layer 7"]

    @layer_7.setter
    def layer_7(self, value=None):
        """  Corresponds to IDD Field `layer_7`

        Args:
            value (str): value for IDD Field `layer_7`
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
                                 'for field `layer_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_7`')

        self._data["Layer 7"] = value

    @property
    def layer_8(self):
        """Get layer_8

        Returns:
            str: the value of `layer_8` or None if not set
        """
        return self._data["Layer 8"]

    @layer_8.setter
    def layer_8(self, value=None):
        """  Corresponds to IDD Field `layer_8`

        Args:
            value (str): value for IDD Field `layer_8`
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
                                 'for field `layer_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_8`')

        self._data["Layer 8"] = value

    @property
    def layer_9(self):
        """Get layer_9

        Returns:
            str: the value of `layer_9` or None if not set
        """
        return self._data["Layer 9"]

    @layer_9.setter
    def layer_9(self, value=None):
        """  Corresponds to IDD Field `layer_9`

        Args:
            value (str): value for IDD Field `layer_9`
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
                                 'for field `layer_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_9`')

        self._data["Layer 9"] = value

    @property
    def layer_10(self):
        """Get layer_10

        Returns:
            str: the value of `layer_10` or None if not set
        """
        return self._data["Layer 10"]

    @layer_10.setter
    def layer_10(self, value=None):
        """  Corresponds to IDD Field `layer_10`

        Args:
            value (str): value for IDD Field `layer_10`
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
                                 'for field `layer_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_10`')

        self._data["Layer 10"] = value

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
        out.append(self._to_str(self.source_present_after_layer_number))
        out.append(self._to_str(self.temperature_calculation_requested_after_layer_number))
        out.append(self._to_str(self.dimensions_for_the_ctf_calculation))
        out.append(self._to_str(self.tube_spacing))
        out.append(self._to_str(self.outside_layer))
        out.append(self._to_str(self.layer_2))
        out.append(self._to_str(self.layer_3))
        out.append(self._to_str(self.layer_4))
        out.append(self._to_str(self.layer_5))
        out.append(self._to_str(self.layer_6))
        out.append(self._to_str(self.layer_7))
        out.append(self._to_str(self.layer_8))
        out.append(self._to_str(self.layer_9))
        out.append(self._to_str(self.layer_10))
        return ",".join(out)

class ConstructionComplexFenestrationState(object):
    """ Corresponds to IDD object `Construction:ComplexFenestrationState`
        Describes one state for a complex glazing system
        These input objects are typically generated by using WINDOW software and export to IDF syntax
    """
    internal_name = "Construction:ComplexFenestrationState"
    field_count = 36

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction:ComplexFenestrationState`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Basis Type"] = None
        self._data["Basis Symmetry Type"] = None
        self._data["Window Thermal Model"] = None
        self._data["Basis Matrix Name"] = None
        self._data["Solar Optical Complex Front Transmittance Matrix Name"] = None
        self._data["Solar Optical Complex Back Reflectance Matrix Name"] = None
        self._data["Visible Optical Complex Front Transmittance Matrix Name"] = None
        self._data["Visible Optical Complex Back Transmittance Matrix Name"] = None
        self._data["Outside Layer Name"] = None
        self._data["Outside Layer Directional Front Absoptance Matrix Name"] = None
        self._data["Outside Layer Directional Back Absoptance Matrix Name"] = None
        self._data["Gap 1 Name"] = None
        self._data["CFS Gap 1 Directional Front Absoptance Matrix Name"] = None
        self._data["CFS Gap 1 Directional Back Absoptance Matrix Name"] = None
        self._data["Layer 2 Name"] = None
        self._data["Layer 2 Directional Front Absoptance Matrix Name"] = None
        self._data["Layer 2 Directional Back Absoptance Matrix Name"] = None
        self._data["Gap 2 Name"] = None
        self._data["Gap 2 Directional Front Absoptance Matrix Name"] = None
        self._data["Gap 2 Directional Back Absoptance Matrix Name"] = None
        self._data["Layer 3 Material"] = None
        self._data["Layer 3 Directional Front Absoptance Matrix Name"] = None
        self._data["Layer 3 Directional Back Absoptance Matrix Name"] = None
        self._data["Gap 3 Name"] = None
        self._data["Gap 3 Directional Front Absoptance Matrix Name"] = None
        self._data["Gap 3 Directional Back Absoptance Matrix Name"] = None
        self._data["Layer 4 Name"] = None
        self._data["Layer 4 Directional Front Absoptance Matrix Name"] = None
        self._data["Layer 4 Directional Back Absoptance Matrix Name"] = None
        self._data["Gap 4 Name"] = None
        self._data["Gap 4 Directional Front Absoptance Matrix Name"] = None
        self._data["Gap 4 Directional Back Absoptance Matrix Name"] = None
        self._data["Layer 5 Name"] = None
        self._data["Layer 5 Directional Front Absoptance Matrix Name"] = None
        self._data["Layer 5 Directional Back Absoptance Matrix Name"] = None

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
            self.basis_type = None
        else:
            self.basis_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basis_symmetry_type = None
        else:
            self.basis_symmetry_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_thermal_model = None
        else:
            self.window_thermal_model = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.basis_matrix_name = None
        else:
            self.basis_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_optical_complex_front_transmittance_matrix_name = None
        else:
            self.solar_optical_complex_front_transmittance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_optical_complex_back_reflectance_matrix_name = None
        else:
            self.solar_optical_complex_back_reflectance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_optical_complex_front_transmittance_matrix_name = None
        else:
            self.visible_optical_complex_front_transmittance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_optical_complex_back_transmittance_matrix_name = None
        else:
            self.visible_optical_complex_back_transmittance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_layer_name = None
        else:
            self.outside_layer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_layer_directional_front_absoptance_matrix_name = None
        else:
            self.outside_layer_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_layer_directional_back_absoptance_matrix_name = None
        else:
            self.outside_layer_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_1_name = None
        else:
            self.gap_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cfs_gap_1_directional_front_absoptance_matrix_name = None
        else:
            self.cfs_gap_1_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cfs_gap_1_directional_back_absoptance_matrix_name = None
        else:
            self.cfs_gap_1_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2_name = None
        else:
            self.layer_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2_directional_front_absoptance_matrix_name = None
        else:
            self.layer_2_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2_directional_back_absoptance_matrix_name = None
        else:
            self.layer_2_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_2_name = None
        else:
            self.gap_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_2_directional_front_absoptance_matrix_name = None
        else:
            self.gap_2_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_2_directional_back_absoptance_matrix_name = None
        else:
            self.gap_2_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3_material = None
        else:
            self.layer_3_material = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3_directional_front_absoptance_matrix_name = None
        else:
            self.layer_3_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3_directional_back_absoptance_matrix_name = None
        else:
            self.layer_3_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_3_name = None
        else:
            self.gap_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_3_directional_front_absoptance_matrix_name = None
        else:
            self.gap_3_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_3_directional_back_absoptance_matrix_name = None
        else:
            self.gap_3_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4_name = None
        else:
            self.layer_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4_directional_front_absoptance_matrix_name = None
        else:
            self.layer_4_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4_directional_back_absoptance_matrix_name = None
        else:
            self.layer_4_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_4_name = None
        else:
            self.gap_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_4_directional_front_absoptance_matrix_name = None
        else:
            self.gap_4_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gap_4_directional_back_absoptance_matrix_name = None
        else:
            self.gap_4_directional_back_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5_name = None
        else:
            self.layer_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5_directional_front_absoptance_matrix_name = None
        else:
            self.layer_5_directional_front_absoptance_matrix_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5_directional_back_absoptance_matrix_name = None
        else:
            self.layer_5_directional_back_absoptance_matrix_name = vals[i]
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
    def basis_type(self):
        """Get basis_type

        Returns:
            str: the value of `basis_type` or None if not set
        """
        return self._data["Basis Type"]

    @basis_type.setter
    def basis_type(self, value="LBNLWINDOW"):
        """  Corresponds to IDD Field `basis_type`

        Args:
            value (str): value for IDD Field `basis_type`
                Accepted values are:
                      - LBNLWINDOW
                      - UserDefined
                Default value: LBNLWINDOW
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
                                 'for field `basis_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basis_type`')
            vals = set()
            vals.add("LBNLWINDOW")
            vals.add("UserDefined")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `basis_type`'.format(value))

        self._data["Basis Type"] = value

    @property
    def basis_symmetry_type(self):
        """Get basis_symmetry_type

        Returns:
            str: the value of `basis_symmetry_type` or None if not set
        """
        return self._data["Basis Symmetry Type"]

    @basis_symmetry_type.setter
    def basis_symmetry_type(self, value="None"):
        """  Corresponds to IDD Field `basis_symmetry_type`

        Args:
            value (str): value for IDD Field `basis_symmetry_type`
                Accepted values are:
                      - Axisymmetric
                      - None
                Default value: None
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
                                 'for field `basis_symmetry_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basis_symmetry_type`')
            vals = set()
            vals.add("Axisymmetric")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `basis_symmetry_type`'.format(value))

        self._data["Basis Symmetry Type"] = value

    @property
    def window_thermal_model(self):
        """Get window_thermal_model

        Returns:
            str: the value of `window_thermal_model` or None if not set
        """
        return self._data["Window Thermal Model"]

    @window_thermal_model.setter
    def window_thermal_model(self, value=None):
        """  Corresponds to IDD Field `window_thermal_model`

        Args:
            value (str): value for IDD Field `window_thermal_model`
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
                                 'for field `window_thermal_model`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_thermal_model`')

        self._data["Window Thermal Model"] = value

    @property
    def basis_matrix_name(self):
        """Get basis_matrix_name

        Returns:
            str: the value of `basis_matrix_name` or None if not set
        """
        return self._data["Basis Matrix Name"]

    @basis_matrix_name.setter
    def basis_matrix_name(self, value=None):
        """  Corresponds to IDD Field `basis_matrix_name`

        Args:
            value (str): value for IDD Field `basis_matrix_name`
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
                                 'for field `basis_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basis_matrix_name`')

        self._data["Basis Matrix Name"] = value

    @property
    def solar_optical_complex_front_transmittance_matrix_name(self):
        """Get solar_optical_complex_front_transmittance_matrix_name

        Returns:
            str: the value of `solar_optical_complex_front_transmittance_matrix_name` or None if not set
        """
        return self._data["Solar Optical Complex Front Transmittance Matrix Name"]

    @solar_optical_complex_front_transmittance_matrix_name.setter
    def solar_optical_complex_front_transmittance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `solar_optical_complex_front_transmittance_matrix_name`

        Args:
            value (str): value for IDD Field `solar_optical_complex_front_transmittance_matrix_name`
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
                                 'for field `solar_optical_complex_front_transmittance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_optical_complex_front_transmittance_matrix_name`')

        self._data["Solar Optical Complex Front Transmittance Matrix Name"] = value

    @property
    def solar_optical_complex_back_reflectance_matrix_name(self):
        """Get solar_optical_complex_back_reflectance_matrix_name

        Returns:
            str: the value of `solar_optical_complex_back_reflectance_matrix_name` or None if not set
        """
        return self._data["Solar Optical Complex Back Reflectance Matrix Name"]

    @solar_optical_complex_back_reflectance_matrix_name.setter
    def solar_optical_complex_back_reflectance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `solar_optical_complex_back_reflectance_matrix_name`

        Args:
            value (str): value for IDD Field `solar_optical_complex_back_reflectance_matrix_name`
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
                                 'for field `solar_optical_complex_back_reflectance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `solar_optical_complex_back_reflectance_matrix_name`')

        self._data["Solar Optical Complex Back Reflectance Matrix Name"] = value

    @property
    def visible_optical_complex_front_transmittance_matrix_name(self):
        """Get visible_optical_complex_front_transmittance_matrix_name

        Returns:
            str: the value of `visible_optical_complex_front_transmittance_matrix_name` or None if not set
        """
        return self._data["Visible Optical Complex Front Transmittance Matrix Name"]

    @visible_optical_complex_front_transmittance_matrix_name.setter
    def visible_optical_complex_front_transmittance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `visible_optical_complex_front_transmittance_matrix_name`

        Args:
            value (str): value for IDD Field `visible_optical_complex_front_transmittance_matrix_name`
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
                                 'for field `visible_optical_complex_front_transmittance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `visible_optical_complex_front_transmittance_matrix_name`')

        self._data["Visible Optical Complex Front Transmittance Matrix Name"] = value

    @property
    def visible_optical_complex_back_transmittance_matrix_name(self):
        """Get visible_optical_complex_back_transmittance_matrix_name

        Returns:
            str: the value of `visible_optical_complex_back_transmittance_matrix_name` or None if not set
        """
        return self._data["Visible Optical Complex Back Transmittance Matrix Name"]

    @visible_optical_complex_back_transmittance_matrix_name.setter
    def visible_optical_complex_back_transmittance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `visible_optical_complex_back_transmittance_matrix_name`

        Args:
            value (str): value for IDD Field `visible_optical_complex_back_transmittance_matrix_name`
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
                                 'for field `visible_optical_complex_back_transmittance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `visible_optical_complex_back_transmittance_matrix_name`')

        self._data["Visible Optical Complex Back Transmittance Matrix Name"] = value

    @property
    def outside_layer_name(self):
        """Get outside_layer_name

        Returns:
            str: the value of `outside_layer_name` or None if not set
        """
        return self._data["Outside Layer Name"]

    @outside_layer_name.setter
    def outside_layer_name(self, value=None):
        """  Corresponds to IDD Field `outside_layer_name`

        Args:
            value (str): value for IDD Field `outside_layer_name`
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
                                 'for field `outside_layer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_layer_name`')

        self._data["Outside Layer Name"] = value

    @property
    def outside_layer_directional_front_absoptance_matrix_name(self):
        """Get outside_layer_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `outside_layer_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Outside Layer Directional Front Absoptance Matrix Name"]

    @outside_layer_directional_front_absoptance_matrix_name.setter
    def outside_layer_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `outside_layer_directional_front_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `outside_layer_directional_front_absoptance_matrix_name`
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
                                 'for field `outside_layer_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_layer_directional_front_absoptance_matrix_name`')

        self._data["Outside Layer Directional Front Absoptance Matrix Name"] = value

    @property
    def outside_layer_directional_back_absoptance_matrix_name(self):
        """Get outside_layer_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `outside_layer_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Outside Layer Directional Back Absoptance Matrix Name"]

    @outside_layer_directional_back_absoptance_matrix_name.setter
    def outside_layer_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `outside_layer_directional_back_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `outside_layer_directional_back_absoptance_matrix_name`
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
                                 'for field `outside_layer_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_layer_directional_back_absoptance_matrix_name`')

        self._data["Outside Layer Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_1_name(self):
        """Get gap_1_name

        Returns:
            str: the value of `gap_1_name` or None if not set
        """
        return self._data["Gap 1 Name"]

    @gap_1_name.setter
    def gap_1_name(self, value=None):
        """  Corresponds to IDD Field `gap_1_name`

        Args:
            value (str): value for IDD Field `gap_1_name`
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
                                 'for field `gap_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_1_name`')

        self._data["Gap 1 Name"] = value

    @property
    def cfs_gap_1_directional_front_absoptance_matrix_name(self):
        """Get cfs_gap_1_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `cfs_gap_1_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["CFS Gap 1 Directional Front Absoptance Matrix Name"]

    @cfs_gap_1_directional_front_absoptance_matrix_name.setter
    def cfs_gap_1_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `cfs_gap_1_directional_front_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `cfs_gap_1_directional_front_absoptance_matrix_name`
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
                                 'for field `cfs_gap_1_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cfs_gap_1_directional_front_absoptance_matrix_name`')

        self._data["CFS Gap 1 Directional Front Absoptance Matrix Name"] = value

    @property
    def cfs_gap_1_directional_back_absoptance_matrix_name(self):
        """Get cfs_gap_1_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `cfs_gap_1_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["CFS Gap 1 Directional Back Absoptance Matrix Name"]

    @cfs_gap_1_directional_back_absoptance_matrix_name.setter
    def cfs_gap_1_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `cfs_gap_1_directional_back_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `cfs_gap_1_directional_back_absoptance_matrix_name`
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
                                 'for field `cfs_gap_1_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cfs_gap_1_directional_back_absoptance_matrix_name`')

        self._data["CFS Gap 1 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_2_name(self):
        """Get layer_2_name

        Returns:
            str: the value of `layer_2_name` or None if not set
        """
        return self._data["Layer 2 Name"]

    @layer_2_name.setter
    def layer_2_name(self, value=None):
        """  Corresponds to IDD Field `layer_2_name`

        Args:
            value (str): value for IDD Field `layer_2_name`
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
                                 'for field `layer_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2_name`')

        self._data["Layer 2 Name"] = value

    @property
    def layer_2_directional_front_absoptance_matrix_name(self):
        """Get layer_2_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `layer_2_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 2 Directional Front Absoptance Matrix Name"]

    @layer_2_directional_front_absoptance_matrix_name.setter
    def layer_2_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_2_directional_front_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_2_directional_front_absoptance_matrix_name`
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
                                 'for field `layer_2_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2_directional_front_absoptance_matrix_name`')

        self._data["Layer 2 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_2_directional_back_absoptance_matrix_name(self):
        """Get layer_2_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `layer_2_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 2 Directional Back Absoptance Matrix Name"]

    @layer_2_directional_back_absoptance_matrix_name.setter
    def layer_2_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_2_directional_back_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_2_directional_back_absoptance_matrix_name`
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
                                 'for field `layer_2_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2_directional_back_absoptance_matrix_name`')

        self._data["Layer 2 Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_2_name(self):
        """Get gap_2_name

        Returns:
            str: the value of `gap_2_name` or None if not set
        """
        return self._data["Gap 2 Name"]

    @gap_2_name.setter
    def gap_2_name(self, value=None):
        """  Corresponds to IDD Field `gap_2_name`

        Args:
            value (str): value for IDD Field `gap_2_name`
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
                                 'for field `gap_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_2_name`')

        self._data["Gap 2 Name"] = value

    @property
    def gap_2_directional_front_absoptance_matrix_name(self):
        """Get gap_2_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `gap_2_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Gap 2 Directional Front Absoptance Matrix Name"]

    @gap_2_directional_front_absoptance_matrix_name.setter
    def gap_2_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `gap_2_directional_front_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `gap_2_directional_front_absoptance_matrix_name`
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
                                 'for field `gap_2_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_2_directional_front_absoptance_matrix_name`')

        self._data["Gap 2 Directional Front Absoptance Matrix Name"] = value

    @property
    def gap_2_directional_back_absoptance_matrix_name(self):
        """Get gap_2_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `gap_2_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Gap 2 Directional Back Absoptance Matrix Name"]

    @gap_2_directional_back_absoptance_matrix_name.setter
    def gap_2_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `gap_2_directional_back_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `gap_2_directional_back_absoptance_matrix_name`
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
                                 'for field `gap_2_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_2_directional_back_absoptance_matrix_name`')

        self._data["Gap 2 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_3_material(self):
        """Get layer_3_material

        Returns:
            str: the value of `layer_3_material` or None if not set
        """
        return self._data["Layer 3 Material"]

    @layer_3_material.setter
    def layer_3_material(self, value=None):
        """  Corresponds to IDD Field `layer_3_material`

        Args:
            value (str): value for IDD Field `layer_3_material`
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
                                 'for field `layer_3_material`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3_material`')

        self._data["Layer 3 Material"] = value

    @property
    def layer_3_directional_front_absoptance_matrix_name(self):
        """Get layer_3_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `layer_3_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 3 Directional Front Absoptance Matrix Name"]

    @layer_3_directional_front_absoptance_matrix_name.setter
    def layer_3_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_3_directional_front_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_3_directional_front_absoptance_matrix_name`
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
                                 'for field `layer_3_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3_directional_front_absoptance_matrix_name`')

        self._data["Layer 3 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_3_directional_back_absoptance_matrix_name(self):
        """Get layer_3_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `layer_3_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 3 Directional Back Absoptance Matrix Name"]

    @layer_3_directional_back_absoptance_matrix_name.setter
    def layer_3_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_3_directional_back_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_3_directional_back_absoptance_matrix_name`
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
                                 'for field `layer_3_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3_directional_back_absoptance_matrix_name`')

        self._data["Layer 3 Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_3_name(self):
        """Get gap_3_name

        Returns:
            str: the value of `gap_3_name` or None if not set
        """
        return self._data["Gap 3 Name"]

    @gap_3_name.setter
    def gap_3_name(self, value=None):
        """  Corresponds to IDD Field `gap_3_name`

        Args:
            value (str): value for IDD Field `gap_3_name`
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
                                 'for field `gap_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_3_name`')

        self._data["Gap 3 Name"] = value

    @property
    def gap_3_directional_front_absoptance_matrix_name(self):
        """Get gap_3_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `gap_3_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Gap 3 Directional Front Absoptance Matrix Name"]

    @gap_3_directional_front_absoptance_matrix_name.setter
    def gap_3_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `gap_3_directional_front_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `gap_3_directional_front_absoptance_matrix_name`
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
                                 'for field `gap_3_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_3_directional_front_absoptance_matrix_name`')

        self._data["Gap 3 Directional Front Absoptance Matrix Name"] = value

    @property
    def gap_3_directional_back_absoptance_matrix_name(self):
        """Get gap_3_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `gap_3_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Gap 3 Directional Back Absoptance Matrix Name"]

    @gap_3_directional_back_absoptance_matrix_name.setter
    def gap_3_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `gap_3_directional_back_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `gap_3_directional_back_absoptance_matrix_name`
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
                                 'for field `gap_3_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_3_directional_back_absoptance_matrix_name`')

        self._data["Gap 3 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_4_name(self):
        """Get layer_4_name

        Returns:
            str: the value of `layer_4_name` or None if not set
        """
        return self._data["Layer 4 Name"]

    @layer_4_name.setter
    def layer_4_name(self, value=None):
        """  Corresponds to IDD Field `layer_4_name`

        Args:
            value (str): value for IDD Field `layer_4_name`
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
                                 'for field `layer_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4_name`')

        self._data["Layer 4 Name"] = value

    @property
    def layer_4_directional_front_absoptance_matrix_name(self):
        """Get layer_4_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `layer_4_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 4 Directional Front Absoptance Matrix Name"]

    @layer_4_directional_front_absoptance_matrix_name.setter
    def layer_4_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_4_directional_front_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_4_directional_front_absoptance_matrix_name`
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
                                 'for field `layer_4_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4_directional_front_absoptance_matrix_name`')

        self._data["Layer 4 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_4_directional_back_absoptance_matrix_name(self):
        """Get layer_4_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `layer_4_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 4 Directional Back Absoptance Matrix Name"]

    @layer_4_directional_back_absoptance_matrix_name.setter
    def layer_4_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_4_directional_back_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_4_directional_back_absoptance_matrix_name`
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
                                 'for field `layer_4_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4_directional_back_absoptance_matrix_name`')

        self._data["Layer 4 Directional Back Absoptance Matrix Name"] = value

    @property
    def gap_4_name(self):
        """Get gap_4_name

        Returns:
            str: the value of `gap_4_name` or None if not set
        """
        return self._data["Gap 4 Name"]

    @gap_4_name.setter
    def gap_4_name(self, value=None):
        """  Corresponds to IDD Field `gap_4_name`

        Args:
            value (str): value for IDD Field `gap_4_name`
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
                                 'for field `gap_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_4_name`')

        self._data["Gap 4 Name"] = value

    @property
    def gap_4_directional_front_absoptance_matrix_name(self):
        """Get gap_4_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `gap_4_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Gap 4 Directional Front Absoptance Matrix Name"]

    @gap_4_directional_front_absoptance_matrix_name.setter
    def gap_4_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `gap_4_directional_front_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `gap_4_directional_front_absoptance_matrix_name`
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
                                 'for field `gap_4_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_4_directional_front_absoptance_matrix_name`')

        self._data["Gap 4 Directional Front Absoptance Matrix Name"] = value

    @property
    def gap_4_directional_back_absoptance_matrix_name(self):
        """Get gap_4_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `gap_4_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Gap 4 Directional Back Absoptance Matrix Name"]

    @gap_4_directional_back_absoptance_matrix_name.setter
    def gap_4_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `gap_4_directional_back_absoptance_matrix_name`
        Reserved for future use. Leave it blank for this version

        Args:
            value (str): value for IDD Field `gap_4_directional_back_absoptance_matrix_name`
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
                                 'for field `gap_4_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gap_4_directional_back_absoptance_matrix_name`')

        self._data["Gap 4 Directional Back Absoptance Matrix Name"] = value

    @property
    def layer_5_name(self):
        """Get layer_5_name

        Returns:
            str: the value of `layer_5_name` or None if not set
        """
        return self._data["Layer 5 Name"]

    @layer_5_name.setter
    def layer_5_name(self, value=None):
        """  Corresponds to IDD Field `layer_5_name`

        Args:
            value (str): value for IDD Field `layer_5_name`
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
                                 'for field `layer_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5_name`')

        self._data["Layer 5 Name"] = value

    @property
    def layer_5_directional_front_absoptance_matrix_name(self):
        """Get layer_5_directional_front_absoptance_matrix_name

        Returns:
            str: the value of `layer_5_directional_front_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 5 Directional Front Absoptance Matrix Name"]

    @layer_5_directional_front_absoptance_matrix_name.setter
    def layer_5_directional_front_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_5_directional_front_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_5_directional_front_absoptance_matrix_name`
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
                                 'for field `layer_5_directional_front_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5_directional_front_absoptance_matrix_name`')

        self._data["Layer 5 Directional Front Absoptance Matrix Name"] = value

    @property
    def layer_5_directional_back_absoptance_matrix_name(self):
        """Get layer_5_directional_back_absoptance_matrix_name

        Returns:
            str: the value of `layer_5_directional_back_absoptance_matrix_name` or None if not set
        """
        return self._data["Layer 5 Directional Back Absoptance Matrix Name"]

    @layer_5_directional_back_absoptance_matrix_name.setter
    def layer_5_directional_back_absoptance_matrix_name(self, value=None):
        """  Corresponds to IDD Field `layer_5_directional_back_absoptance_matrix_name`

        Args:
            value (str): value for IDD Field `layer_5_directional_back_absoptance_matrix_name`
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
                                 'for field `layer_5_directional_back_absoptance_matrix_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5_directional_back_absoptance_matrix_name`')

        self._data["Layer 5 Directional Back Absoptance Matrix Name"] = value

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
        out.append(self._to_str(self.basis_type))
        out.append(self._to_str(self.basis_symmetry_type))
        out.append(self._to_str(self.window_thermal_model))
        out.append(self._to_str(self.basis_matrix_name))
        out.append(self._to_str(self.solar_optical_complex_front_transmittance_matrix_name))
        out.append(self._to_str(self.solar_optical_complex_back_reflectance_matrix_name))
        out.append(self._to_str(self.visible_optical_complex_front_transmittance_matrix_name))
        out.append(self._to_str(self.visible_optical_complex_back_transmittance_matrix_name))
        out.append(self._to_str(self.outside_layer_name))
        out.append(self._to_str(self.outside_layer_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.outside_layer_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.gap_1_name))
        out.append(self._to_str(self.cfs_gap_1_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.cfs_gap_1_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.layer_2_name))
        out.append(self._to_str(self.layer_2_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.layer_2_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.gap_2_name))
        out.append(self._to_str(self.gap_2_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.gap_2_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.layer_3_material))
        out.append(self._to_str(self.layer_3_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.layer_3_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.gap_3_name))
        out.append(self._to_str(self.gap_3_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.gap_3_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.layer_4_name))
        out.append(self._to_str(self.layer_4_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.layer_4_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.gap_4_name))
        out.append(self._to_str(self.gap_4_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.gap_4_directional_back_absoptance_matrix_name))
        out.append(self._to_str(self.layer_5_name))
        out.append(self._to_str(self.layer_5_directional_front_absoptance_matrix_name))
        out.append(self._to_str(self.layer_5_directional_back_absoptance_matrix_name))
        return ",".join(out)

class ConstructionWindowDataFile(object):
    """ Corresponds to IDD object `Construction:WindowDataFile`
        Initiates search of the Window data file for a window called Name.
    """
    internal_name = "Construction:WindowDataFile"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Construction:WindowDataFile`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["File Name"] = None

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
            self.file_name = None
        else:
            self.file_name = vals[i]
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
    def file_name(self):
        """Get file_name

        Returns:
            str: the value of `file_name` or None if not set
        """
        return self._data["File Name"]

    @file_name.setter
    def file_name(self, value=None):
        """  Corresponds to IDD Field `file_name`
        default file name is "Window5DataFile.dat"
        limit on this field is 100 characters.

        Args:
            value (str): value for IDD Field `file_name`
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
                                 'for field `file_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `file_name`')

        self._data["File Name"] = value

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
        out.append(self._to_str(self.file_name))
        return ",".join(out)