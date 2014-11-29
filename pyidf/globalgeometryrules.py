from collections import OrderedDict

class GlobalGeometryRules(object):
    """ Corresponds to IDD object `GlobalGeometryRules`
        Specifes the geometric rules used to describe the input of surface vertices and
        daylighting reference points.
    """
    internal_name = "GlobalGeometryRules"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `GlobalGeometryRules`
        """
        self._data = OrderedDict()
        self._data["Starting Vertex Position"] = None
        self._data["Vertex Entry Direction"] = None
        self._data["Coordinate System"] = None
        self._data["Daylighting Reference Point Coordinate System"] = None
        self._data["Rectangular Surface Coordinate System"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.starting_vertex_position = None
        else:
            self.starting_vertex_position = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_entry_direction = None
        else:
            self.vertex_entry_direction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.coordinate_system = None
        else:
            self.coordinate_system = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.daylighting_reference_point_coordinate_system = None
        else:
            self.daylighting_reference_point_coordinate_system = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rectangular_surface_coordinate_system = None
        else:
            self.rectangular_surface_coordinate_system = vals[i]
        i += 1

    @property
    def starting_vertex_position(self):
        """Get starting_vertex_position

        Returns:
            str: the value of `starting_vertex_position` or None if not set
        """
        return self._data["Starting Vertex Position"]

    @starting_vertex_position.setter
    def starting_vertex_position(self, value=None):
        """  Corresponds to IDD Field `starting_vertex_position`
        Specified as entry for a 4 sided surface/rectangle
        Surfaces are specified as viewed from outside the surface
        Shading surfaces as viewed from behind.  (towards what they are shading)

        Args:
            value (str): value for IDD Field `starting_vertex_position`
                Accepted values are:
                      - UpperLeftCorner
                      - LowerLeftCorner
                      - UpperRightCorner
                      - LowerRightCorner
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
                                 'for field `starting_vertex_position`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `starting_vertex_position`')
            vals = set()
            vals.add("UpperLeftCorner")
            vals.add("LowerLeftCorner")
            vals.add("UpperRightCorner")
            vals.add("LowerRightCorner")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `starting_vertex_position`'.format(value))

        self._data["Starting Vertex Position"] = value

    @property
    def vertex_entry_direction(self):
        """Get vertex_entry_direction

        Returns:
            str: the value of `vertex_entry_direction` or None if not set
        """
        return self._data["Vertex Entry Direction"]

    @vertex_entry_direction.setter
    def vertex_entry_direction(self, value=None):
        """  Corresponds to IDD Field `vertex_entry_direction`

        Args:
            value (str): value for IDD Field `vertex_entry_direction`
                Accepted values are:
                      - Counterclockwise
                      - Clockwise
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
                                 'for field `vertex_entry_direction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `vertex_entry_direction`')
            vals = set()
            vals.add("Counterclockwise")
            vals.add("Clockwise")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `vertex_entry_direction`'.format(value))

        self._data["Vertex Entry Direction"] = value

    @property
    def coordinate_system(self):
        """Get coordinate_system

        Returns:
            str: the value of `coordinate_system` or None if not set
        """
        return self._data["Coordinate System"]

    @coordinate_system.setter
    def coordinate_system(self, value=None):
        """  Corresponds to IDD Field `coordinate_system`
        relative -- coordinates are entered relative to zone origin
        world -- all coordinates entered are "absolute" for this facility
        absolute -- same as world

        Args:
            value (str): value for IDD Field `coordinate_system`
                Accepted values are:
                      - Relative
                      - World
                      - Absolute
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
                                 'for field `coordinate_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `coordinate_system`')
            vals = set()
            vals.add("Relative")
            vals.add("World")
            vals.add("Absolute")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `coordinate_system`'.format(value))

        self._data["Coordinate System"] = value

    @property
    def daylighting_reference_point_coordinate_system(self):
        """Get daylighting_reference_point_coordinate_system

        Returns:
            str: the value of `daylighting_reference_point_coordinate_system` or None if not set
        """
        return self._data["Daylighting Reference Point Coordinate System"]

    @daylighting_reference_point_coordinate_system.setter
    def daylighting_reference_point_coordinate_system(self, value="Relative"):
        """  Corresponds to IDD Field `daylighting_reference_point_coordinate_system`
        Relative -- coordinates are entered relative to zone origin
        World -- all coordinates entered are "absolute" for this facility
        absolute -- same as world

        Args:
            value (str): value for IDD Field `daylighting_reference_point_coordinate_system`
                Accepted values are:
                      - Relative
                      - World
                      - Absolute
                Default value: Relative
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
                                 'for field `daylighting_reference_point_coordinate_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `daylighting_reference_point_coordinate_system`')
            vals = set()
            vals.add("Relative")
            vals.add("World")
            vals.add("Absolute")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `daylighting_reference_point_coordinate_system`'.format(value))

        self._data["Daylighting Reference Point Coordinate System"] = value

    @property
    def rectangular_surface_coordinate_system(self):
        """Get rectangular_surface_coordinate_system

        Returns:
            str: the value of `rectangular_surface_coordinate_system` or None if not set
        """
        return self._data["Rectangular Surface Coordinate System"]

    @rectangular_surface_coordinate_system.setter
    def rectangular_surface_coordinate_system(self, value="Relative"):
        """  Corresponds to IDD Field `rectangular_surface_coordinate_system`
        Relative -- Starting corner is entered relative to zone origin
        World -- Starting corner is entered in "absolute"
        absolute -- same as world

        Args:
            value (str): value for IDD Field `rectangular_surface_coordinate_system`
                Accepted values are:
                      - Relative
                      - World
                      - Absolute
                Default value: Relative
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
                                 'for field `rectangular_surface_coordinate_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `rectangular_surface_coordinate_system`')
            vals = set()
            vals.add("Relative")
            vals.add("World")
            vals.add("Absolute")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `rectangular_surface_coordinate_system`'.format(value))

        self._data["Rectangular Surface Coordinate System"] = value

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
        out.append(self._to_str(self.starting_vertex_position))
        out.append(self._to_str(self.vertex_entry_direction))
        out.append(self._to_str(self.coordinate_system))
        out.append(self._to_str(self.daylighting_reference_point_coordinate_system))
        out.append(self._to_str(self.rectangular_surface_coordinate_system))
        return ",".join(out)