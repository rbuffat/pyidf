from collections import OrderedDict

class SurfaceControlMovableInsulation(object):
    """ Corresponds to IDD object `SurfaceControl:MovableInsulation`
        Exterior or Interior Insulation on opaque surfaces
    """
    internal_name = "SurfaceControl:MovableInsulation"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceControl:MovableInsulation`
        """
        self._data = OrderedDict()
        self._data["Insulation Type"] = None
        self._data["Surface Name"] = None
        self._data["Material Name"] = None
        self._data["Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.insulation_type = None
        else:
            self.insulation_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1

    @property
    def insulation_type(self):
        """Get insulation_type

        Returns:
            str: the value of `insulation_type` or None if not set
        """
        return self._data["Insulation Type"]

    @insulation_type.setter
    def insulation_type(self, value=None):
        """  Corresponds to IDD Field `insulation_type`

        Args:
            value (str): value for IDD Field `insulation_type`
                Accepted values are:
                      - Outside
                      - Inside
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
                                 'for field `insulation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `insulation_type`')
            vals = set()
            vals.add("Outside")
            vals.add("Inside")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `insulation_type`'.format(value))

        self._data["Insulation Type"] = value

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def material_name(self):
        """Get material_name

        Returns:
            str: the value of `material_name` or None if not set
        """
        return self._data["Material Name"]

    @material_name.setter
    def material_name(self, value=None):
        """  Corresponds to IDD Field `material_name`

        Args:
            value (str): value for IDD Field `material_name`
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
                                 'for field `material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `material_name`')

        self._data["Material Name"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

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
        out.append(self._to_str(self.insulation_type))
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)