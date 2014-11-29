from collections import OrderedDict

class GeometryTransform(object):
    """ Corresponds to IDD object `GeometryTransform`
        Provides a simple method of altering the footprint geometry of a model. The intent
        is to provide a single parameter that can be used to reshape the building description
        contained in the rest of the input file.
    """
    internal_name = "GeometryTransform"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `GeometryTransform`
        """
        self._data = OrderedDict()
        self._data["Plane of Transform"] = None
        self._data["Current Aspect Ratio"] = None
        self._data["New Aspect Ratio"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.plane_of_transform = None
        else:
            self.plane_of_transform = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.current_aspect_ratio = None
        else:
            self.current_aspect_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.new_aspect_ratio = None
        else:
            self.new_aspect_ratio = vals[i]
        i += 1

    @property
    def plane_of_transform(self):
        """Get plane_of_transform

        Returns:
            str: the value of `plane_of_transform` or None if not set
        """
        return self._data["Plane of Transform"]

    @plane_of_transform.setter
    def plane_of_transform(self, value="XY"):
        """  Corresponds to IDD Field `plane_of_transform`
        only current allowed value is "XY"

        Args:
            value (str): value for IDD Field `plane_of_transform`
                Accepted values are:
                      - XY
                Default value: XY
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
                                 'for field `plane_of_transform`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plane_of_transform`')
            vals = set()
            vals.add("XY")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plane_of_transform`'.format(value))

        self._data["Plane of Transform"] = value

    @property
    def current_aspect_ratio(self):
        """Get current_aspect_ratio

        Returns:
            float: the value of `current_aspect_ratio` or None if not set
        """
        return self._data["Current Aspect Ratio"]

    @current_aspect_ratio.setter
    def current_aspect_ratio(self, value=None):
        """  Corresponds to IDD Field `current_aspect_ratio`
        Aspect ratio of building as described in idf

        Args:
            value (float): value for IDD Field `current_aspect_ratio`
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
                                 'for field `current_aspect_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `current_aspect_ratio`')

        self._data["Current Aspect Ratio"] = value

    @property
    def new_aspect_ratio(self):
        """Get new_aspect_ratio

        Returns:
            float: the value of `new_aspect_ratio` or None if not set
        """
        return self._data["New Aspect Ratio"]

    @new_aspect_ratio.setter
    def new_aspect_ratio(self, value=None):
        """  Corresponds to IDD Field `new_aspect_ratio`
        Aspect ratio to transform to during run

        Args:
            value (float): value for IDD Field `new_aspect_ratio`
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
                                 'for field `new_aspect_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `new_aspect_ratio`')

        self._data["New Aspect Ratio"] = value

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
        out.append(self._to_str(self.plane_of_transform))
        out.append(self._to_str(self.current_aspect_ratio))
        out.append(self._to_str(self.new_aspect_ratio))
        return ",".join(out)