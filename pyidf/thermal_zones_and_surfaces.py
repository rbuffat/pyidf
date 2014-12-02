from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class GlobalGeometryRules(object):
    """ Corresponds to IDD object `GlobalGeometryRules`
        Specifes the geometric rules used to describe the input of surface vertices and
        daylighting reference points.
    """
    internal_name = "GlobalGeometryRules"
    field_count = 5
    required_fields = ["Starting Vertex Position", "Vertex Entry Direction", "Coordinate System"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GlobalGeometryRules`
        """
        self._data = OrderedDict()
        self._data["Starting Vertex Position"] = None
        self._data["Vertex Entry Direction"] = None
        self._data["Coordinate System"] = None
        self._data["Daylighting Reference Point Coordinate System"] = None
        self._data["Rectangular Surface Coordinate System"] = None
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
            self.starting_vertex_position = None
        else:
            self.starting_vertex_position = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_entry_direction = None
        else:
            self.vertex_entry_direction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coordinate_system = None
        else:
            self.coordinate_system = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.daylighting_reference_point_coordinate_system = None
        else:
            self.daylighting_reference_point_coordinate_system = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rectangular_surface_coordinate_system = None
        else:
            self.rectangular_surface_coordinate_system = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def starting_vertex_position(self):
        """Get starting_vertex_position

        Returns:
            str: the value of `starting_vertex_position` or None if not set
        """
        return self._data["Starting Vertex Position"]

    @starting_vertex_position.setter
    def starting_vertex_position(self, value=None):
        """  Corresponds to IDD Field `Starting Vertex Position`
        Specified as entry for a 4 sided surface/rectangle
        Surfaces are specified as viewed from outside the surface
        Shading surfaces as viewed from behind.  (towards what they are shading)

        Args:
            value (str): value for IDD Field `Starting Vertex Position`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `GlobalGeometryRules.starting_vertex_position`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlobalGeometryRules.starting_vertex_position`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlobalGeometryRules.starting_vertex_position`')
            vals = {}
            vals["upperleftcorner"] = "UpperLeftCorner"
            vals["lowerleftcorner"] = "LowerLeftCorner"
            vals["upperrightcorner"] = "UpperRightCorner"
            vals["lowerrightcorner"] = "LowerRightCorner"
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
                                     'field `GlobalGeometryRules.starting_vertex_position`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `GlobalGeometryRules.starting_vertex_position`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Vertex Entry Direction`

        Args:
            value (str): value for IDD Field `Vertex Entry Direction`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `GlobalGeometryRules.vertex_entry_direction`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlobalGeometryRules.vertex_entry_direction`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlobalGeometryRules.vertex_entry_direction`')
            vals = {}
            vals["counterclockwise"] = "Counterclockwise"
            vals["clockwise"] = "Clockwise"
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
                                     'field `GlobalGeometryRules.vertex_entry_direction`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `GlobalGeometryRules.vertex_entry_direction`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Coordinate System`
        relative -- coordinates are entered relative to zone origin
        world -- all coordinates entered are "absolute" for this facility
        absolute -- same as world

        Args:
            value (str): value for IDD Field `Coordinate System`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `GlobalGeometryRules.coordinate_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlobalGeometryRules.coordinate_system`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlobalGeometryRules.coordinate_system`')
            vals = {}
            vals["relative"] = "Relative"
            vals["world"] = "World"
            vals["absolute"] = "Absolute"
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
                                     'field `GlobalGeometryRules.coordinate_system`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `GlobalGeometryRules.coordinate_system`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Daylighting Reference Point Coordinate System`
        Relative -- coordinates are entered relative to zone origin
        World -- all coordinates entered are "absolute" for this facility
        absolute -- same as world

        Args:
            value (str): value for IDD Field `Daylighting Reference Point Coordinate System`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `GlobalGeometryRules.daylighting_reference_point_coordinate_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlobalGeometryRules.daylighting_reference_point_coordinate_system`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlobalGeometryRules.daylighting_reference_point_coordinate_system`')
            vals = {}
            vals["relative"] = "Relative"
            vals["world"] = "World"
            vals["absolute"] = "Absolute"
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
                                     'field `GlobalGeometryRules.daylighting_reference_point_coordinate_system`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `GlobalGeometryRules.daylighting_reference_point_coordinate_system`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Rectangular Surface Coordinate System`
        Relative -- Starting corner is entered relative to zone origin
        World -- Starting corner is entered in "absolute"
        absolute -- same as world

        Args:
            value (str): value for IDD Field `Rectangular Surface Coordinate System`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `GlobalGeometryRules.rectangular_surface_coordinate_system`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlobalGeometryRules.rectangular_surface_coordinate_system`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlobalGeometryRules.rectangular_surface_coordinate_system`')
            vals = {}
            vals["relative"] = "Relative"
            vals["world"] = "World"
            vals["absolute"] = "Absolute"
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
                                     'field `GlobalGeometryRules.rectangular_surface_coordinate_system`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `GlobalGeometryRules.rectangular_surface_coordinate_system`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Rectangular Surface Coordinate System"] = value

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
                    raise ValueError("Required field GlobalGeometryRules:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field GlobalGeometryRules:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for GlobalGeometryRules: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for GlobalGeometryRules: {} / {}".format(out_fields,
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

class GeometryTransform(object):
    """ Corresponds to IDD object `GeometryTransform`
        Provides a simple method of altering the footprint geometry of a model. The intent
        is to provide a single parameter that can be used to reshape the building description
        contained in the rest of the input file.
    """
    internal_name = "GeometryTransform"
    field_count = 3
    required_fields = ["Plane of Transform", "Current Aspect Ratio", "New Aspect Ratio"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GeometryTransform`
        """
        self._data = OrderedDict()
        self._data["Plane of Transform"] = None
        self._data["Current Aspect Ratio"] = None
        self._data["New Aspect Ratio"] = None
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
            self.plane_of_transform = None
        else:
            self.plane_of_transform = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.current_aspect_ratio = None
        else:
            self.current_aspect_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.new_aspect_ratio = None
        else:
            self.new_aspect_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def plane_of_transform(self):
        """Get plane_of_transform

        Returns:
            str: the value of `plane_of_transform` or None if not set
        """
        return self._data["Plane of Transform"]

    @plane_of_transform.setter
    def plane_of_transform(self, value="XY"):
        """  Corresponds to IDD Field `Plane of Transform`
        only current allowed value is "XY"

        Args:
            value (str): value for IDD Field `Plane of Transform`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `GeometryTransform.plane_of_transform`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GeometryTransform.plane_of_transform`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GeometryTransform.plane_of_transform`')
            vals = {}
            vals["xy"] = "XY"
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
                                     'field `GeometryTransform.plane_of_transform`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `GeometryTransform.plane_of_transform`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Current Aspect Ratio`
        Aspect ratio of building as described in idf

        Args:
            value (float): value for IDD Field `Current Aspect Ratio`
                value > 0.0
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
                                 ' for field `GeometryTransform.current_aspect_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `GeometryTransform.current_aspect_ratio`')
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
        """  Corresponds to IDD Field `New Aspect Ratio`
        Aspect ratio to transform to during run

        Args:
            value (float): value for IDD Field `New Aspect Ratio`
                value > 0.0
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
                                 ' for field `GeometryTransform.new_aspect_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `GeometryTransform.new_aspect_ratio`')
        self._data["New Aspect Ratio"] = value

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
                    raise ValueError("Required field GeometryTransform:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field GeometryTransform:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for GeometryTransform: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for GeometryTransform: {} / {}".format(out_fields,
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

class Zone(object):
    """ Corresponds to IDD object `Zone`
        Defines a thermal zone of the building.
    """
    internal_name = "Zone"
    field_count = 13
    required_fields = ["Name"]
    extensible_fields = 0
    format = "vertices"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Zone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Direction of Relative North"] = None
        self._data["X Origin"] = None
        self._data["Y Origin"] = None
        self._data["Z Origin"] = None
        self._data["Type"] = None
        self._data["Multiplier"] = None
        self._data["Ceiling Height"] = None
        self._data["Volume"] = None
        self._data["Floor Area"] = None
        self._data["Zone Inside Convection Algorithm"] = None
        self._data["Zone Outside Convection Algorithm"] = None
        self._data["Part of Total Floor Area"] = None
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
            self.direction_of_relative_north = None
        else:
            self.direction_of_relative_north = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.x_origin = None
        else:
            self.x_origin = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.y_origin = None
        else:
            self.y_origin = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.z_origin = None
        else:
            self.z_origin = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type = None
        else:
            self.type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ceiling_height = None
        else:
            self.ceiling_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.volume = None
        else:
            self.volume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_area = None
        else:
            self.floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_inside_convection_algorithm = None
        else:
            self.zone_inside_convection_algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_outside_convection_algorithm = None
        else:
            self.zone_outside_convection_algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.part_of_total_floor_area = None
        else:
            self.part_of_total_floor_area = vals[i]
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
                                 ' for field `Zone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Zone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Zone.name`')
        self._data["Name"] = value

    @property
    def direction_of_relative_north(self):
        """Get direction_of_relative_north

        Returns:
            float: the value of `direction_of_relative_north` or None if not set
        """
        return self._data["Direction of Relative North"]

    @direction_of_relative_north.setter
    def direction_of_relative_north(self, value=0.0):
        """  Corresponds to IDD Field `Direction of Relative North`

        Args:
            value (float): value for IDD Field `Direction of Relative North`
                Units: deg
                Default value: 0.0
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
                                 ' for field `Zone.direction_of_relative_north`'.format(value))
        self._data["Direction of Relative North"] = value

    @property
    def x_origin(self):
        """Get x_origin

        Returns:
            float: the value of `x_origin` or None if not set
        """
        return self._data["X Origin"]

    @x_origin.setter
    def x_origin(self, value=0.0):
        """  Corresponds to IDD Field `X Origin`

        Args:
            value (float): value for IDD Field `X Origin`
                Units: m
                Default value: 0.0
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
                                 ' for field `Zone.x_origin`'.format(value))
        self._data["X Origin"] = value

    @property
    def y_origin(self):
        """Get y_origin

        Returns:
            float: the value of `y_origin` or None if not set
        """
        return self._data["Y Origin"]

    @y_origin.setter
    def y_origin(self, value=0.0):
        """  Corresponds to IDD Field `Y Origin`

        Args:
            value (float): value for IDD Field `Y Origin`
                Units: m
                Default value: 0.0
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
                                 ' for field `Zone.y_origin`'.format(value))
        self._data["Y Origin"] = value

    @property
    def z_origin(self):
        """Get z_origin

        Returns:
            float: the value of `z_origin` or None if not set
        """
        return self._data["Z Origin"]

    @z_origin.setter
    def z_origin(self, value=0.0):
        """  Corresponds to IDD Field `Z Origin`

        Args:
            value (float): value for IDD Field `Z Origin`
                Units: m
                Default value: 0.0
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
                                 ' for field `Zone.z_origin`'.format(value))
        self._data["Z Origin"] = value

    @property
    def type(self):
        """Get type

        Returns:
            int: the value of `type` or None if not set
        """
        return self._data["Type"]

    @type.setter
    def type(self, value=1):
        """  Corresponds to IDD Field `Type`

        Args:
            value (int): value for IDD Field `Type`
                Default value: 1
                value >= 1
                value <= 1
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `Zone.type`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `Zone.type`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `Zone.type`')
            if value > 1:
                raise ValueError('value need to be smaller 1 '
                                 'for field `Zone.type`')
        self._data["Type"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            int: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1):
        """  Corresponds to IDD Field `Multiplier`

        Args:
            value (int): value for IDD Field `Multiplier`
                Default value: 1
                value >= 1
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `Zone.multiplier`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `Zone.multiplier`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `Zone.multiplier`')
        self._data["Multiplier"] = value

    @property
    def ceiling_height(self):
        """Get ceiling_height

        Returns:
            float: the value of `ceiling_height` or None if not set
        """
        return self._data["Ceiling Height"]

    @ceiling_height.setter
    def ceiling_height(self, value="autocalculate"):
        """  Corresponds to IDD Field `Ceiling Height`
        If this field is 0.0, negative or autocalculate, then the average height
        of the zone is automatically calculated and used in subsequent calculations.
        If this field is positive, then the number entered here will be used.
        Note that the Zone Ceiling Height is the distance from the Floor to
        the Ceiling in the Zone, not an absolute height from the ground.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Ceiling Height`
                Units: m
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Ceiling Height"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `Zone.ceiling_height`'.format(value))
                    self._data["Ceiling Height"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `Zone.ceiling_height`'.format(value))
        self._data["Ceiling Height"] = value

    @property
    def volume(self):
        """Get volume

        Returns:
            float: the value of `volume` or None if not set
        """
        return self._data["Volume"]

    @volume.setter
    def volume(self, value="autocalculate"):
        """  Corresponds to IDD Field `Volume`
        If this field is 0.0, negative or autocalculate, then the volume of the zone
        is automatically calculated and used in subsequent calculations.
        If this field is positive, then the number entered here will be used.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Volume`
                Units: m3
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Volume"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `Zone.volume`'.format(value))
                    self._data["Volume"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `Zone.volume`'.format(value))
        self._data["Volume"] = value

    @property
    def floor_area(self):
        """Get floor_area

        Returns:
            float: the value of `floor_area` or None if not set
        """
        return self._data["Floor Area"]

    @floor_area.setter
    def floor_area(self, value="autocalculate"):
        """  Corresponds to IDD Field `Floor Area`
        If this field is 0.0, negative or autocalculate, then the floor area of the zone
        is automatically calculated and used in subsequent calculations.
        If this field is positive, then the number entered here will be used.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Floor Area`
                Units: m2
                Default value: "autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Floor Area"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `Zone.floor_area`'.format(value))
                    self._data["Floor Area"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `Zone.floor_area`'.format(value))
        self._data["Floor Area"] = value

    @property
    def zone_inside_convection_algorithm(self):
        """Get zone_inside_convection_algorithm

        Returns:
            str: the value of `zone_inside_convection_algorithm` or None if not set
        """
        return self._data["Zone Inside Convection Algorithm"]

    @zone_inside_convection_algorithm.setter
    def zone_inside_convection_algorithm(self, value=None):
        """  Corresponds to IDD Field `Zone Inside Convection Algorithm`
        Will default to same value as SurfaceConvectionAlgorithm:Inside object
        setting this field overrides the default SurfaceConvectionAlgorithm:Inside for this zone
        Simple = constant natural convection (ASHRAE)
        TARP = variable natural convection based on temperature difference (ASHRAE)
        CeilingDiffuser = ACH based forced and mixed convection correlations
        for ceiling diffuser configuration with simple natural convection limit
        AdaptiveConvectionAlgorithm = dynamic selection of convection models based on conditions
        TrombeWall = variable natural convection in an enclosed rectangular cavity

        Args:
            value (str): value for IDD Field `Zone Inside Convection Algorithm`
                Accepted values are:
                      - Simple
                      - TARP
                      - CeilingDiffuser
                      - AdaptiveConvectionAlgorithm
                      - TrombeWall
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
                                 ' for field `Zone.zone_inside_convection_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Zone.zone_inside_convection_algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Zone.zone_inside_convection_algorithm`')
            vals = {}
            vals["simple"] = "Simple"
            vals["tarp"] = "TARP"
            vals["ceilingdiffuser"] = "CeilingDiffuser"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
            vals["trombewall"] = "TrombeWall"
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
                                     'field `Zone.zone_inside_convection_algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `Zone.zone_inside_convection_algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Inside Convection Algorithm"] = value

    @property
    def zone_outside_convection_algorithm(self):
        """Get zone_outside_convection_algorithm

        Returns:
            str: the value of `zone_outside_convection_algorithm` or None if not set
        """
        return self._data["Zone Outside Convection Algorithm"]

    @zone_outside_convection_algorithm.setter
    def zone_outside_convection_algorithm(self, value=None):
        """  Corresponds to IDD Field `Zone Outside Convection Algorithm`
        Will default to same value as SurfaceConvectionAlgorithm:Outside object
        setting this field overrides the default SurfaceConvectionAlgorithm:Outside for this zone
        SimpleCombined = Combined radiation and convection coefficient using simple ASHRAE model
        TARP = correlation from models developed by ASHRAE, Walton, and Sparrow et. al.
        MoWiTT = correlation from measurements by Klems and Yazdanian for smooth surfaces
        DOE-2 = correlation from measurements by Klems and Yazdanian for rough surfaces
        AdaptiveConvectionAlgorithm = dynamic selection of correlations based on conditions

        Args:
            value (str): value for IDD Field `Zone Outside Convection Algorithm`
                Accepted values are:
                      - SimpleCombined
                      - TARP
                      - DOE-2
                      - MoWiTT
                      - AdaptiveConvectionAlgorithm
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
                                 ' for field `Zone.zone_outside_convection_algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Zone.zone_outside_convection_algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Zone.zone_outside_convection_algorithm`')
            vals = {}
            vals["simplecombined"] = "SimpleCombined"
            vals["tarp"] = "TARP"
            vals["doe-2"] = "DOE-2"
            vals["mowitt"] = "MoWiTT"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
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
                                     'field `Zone.zone_outside_convection_algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `Zone.zone_outside_convection_algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Outside Convection Algorithm"] = value

    @property
    def part_of_total_floor_area(self):
        """Get part_of_total_floor_area

        Returns:
            str: the value of `part_of_total_floor_area` or None if not set
        """
        return self._data["Part of Total Floor Area"]

    @part_of_total_floor_area.setter
    def part_of_total_floor_area(self, value="Yes"):
        """  Corresponds to IDD Field `Part of Total Floor Area`

        Args:
            value (str): value for IDD Field `Part of Total Floor Area`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
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
                                 ' for field `Zone.part_of_total_floor_area`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Zone.part_of_total_floor_area`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Zone.part_of_total_floor_area`')
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
                                     'field `Zone.part_of_total_floor_area`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `Zone.part_of_total_floor_area`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Part of Total Floor Area"] = value

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
                    raise ValueError("Required field Zone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Zone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Zone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Zone: {} / {}".format(out_fields,
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

class ZoneList(object):
    """ Corresponds to IDD object `ZoneList`
        Defines a list of thermal zones which can be referenced as a group. The ZoneList name
        may be used elsewhere in the input to apply a parameter to all zones in the list.
        ZoneLists can be used effectively with the following objects: People, Lights,
        ElectricEquipment, GasEquipment, HotWaterEquipment, ZoneInfiltration:DesignFlowRate,
        ZoneVentilation:DesignFlowRate, Sizing:Zone, ZoneControl:Thermostat, and others.
    """
    internal_name = "ZoneList"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 1
    format = None
    min_fields = 2
    extensible_keys = ["Zone 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneList`
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
        Name of the Zone List

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
                                 ' for field `ZoneList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneList.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       zone_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            zone_1_name (str): value for IDD Field `Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_zone_1_name(zone_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_zone_1_name(self, value):
        """ Validates falue of field `Zone 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneList.zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneList.zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneList.zone_1_name`')
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
                    raise ValueError("Required field ZoneList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneList: {} / {}".format(out_fields,
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

class ZoneGroup(object):
    """ Corresponds to IDD object `ZoneGroup`
        Adds a multiplier to a ZoneList. This can be used to reduce the amount of input
        necessary for simulating repetitive structures, such as the identical floors of a
        multi-story building.
    """
    internal_name = "ZoneGroup"
    field_count = 3
    required_fields = ["Name", "Zone List Name"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneGroup`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone List Name"] = None
        self._data["Zone List Multiplier"] = None
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
            self.zone_list_name = None
        else:
            self.zone_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_list_multiplier = None
        else:
            self.zone_list_multiplier = vals[i]
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
        Name of the Zone Group

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
                                 ' for field `ZoneGroup.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneGroup.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneGroup.name`')
        self._data["Name"] = value

    @property
    def zone_list_name(self):
        """Get zone_list_name

        Returns:
            str: the value of `zone_list_name` or None if not set
        """
        return self._data["Zone List Name"]

    @zone_list_name.setter
    def zone_list_name(self, value=None):
        """  Corresponds to IDD Field `Zone List Name`

        Args:
            value (str): value for IDD Field `Zone List Name`
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
                                 ' for field `ZoneGroup.zone_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneGroup.zone_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneGroup.zone_list_name`')
        self._data["Zone List Name"] = value

    @property
    def zone_list_multiplier(self):
        """Get zone_list_multiplier

        Returns:
            int: the value of `zone_list_multiplier` or None if not set
        """
        return self._data["Zone List Multiplier"]

    @zone_list_multiplier.setter
    def zone_list_multiplier(self, value=1):
        """  Corresponds to IDD Field `Zone List Multiplier`

        Args:
            value (int): value for IDD Field `Zone List Multiplier`
                Default value: 1
                value >= 1
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ZoneGroup.zone_list_multiplier`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ZoneGroup.zone_list_multiplier`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ZoneGroup.zone_list_multiplier`')
        self._data["Zone List Multiplier"] = value

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
                    raise ValueError("Required field ZoneGroup:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneGroup:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneGroup: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneGroup: {} / {}".format(out_fields,
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

class BuildingSurfaceDetailed(object):
    """ Corresponds to IDD object `BuildingSurface:Detailed`
        Allows for detailed entry of building heat transfer surfaces.  Does not include subsurfaces such as windows or doors.
    """
    internal_name = "BuildingSurface:Detailed"
    field_count = 10
    required_fields = ["Name", "Surface Type", "Construction Name", "Zone Name", "Outside Boundary Condition", "Sun Exposure", "Wind Exposure"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 19
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `BuildingSurface:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Type"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Sun Exposure"] = None
        self._data["Wind Exposure"] = None
        self._data["View Factor to Ground"] = None
        self._data["Number of Vertices"] = None
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
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition = None
        else:
            self.outside_boundary_condition = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_exposure = None
        else:
            self.wind_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `BuildingSurfaceDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.name`')
        self._data["Name"] = value

    @property
    def surface_type(self):
        """Get surface_type

        Returns:
            str: the value of `surface_type` or None if not set
        """
        return self._data["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """  Corresponds to IDD Field `Surface Type`

        Args:
            value (str): value for IDD Field `Surface Type`
                Accepted values are:
                      - Floor
                      - Wall
                      - Ceiling
                      - Roof
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
                                 ' for field `BuildingSurfaceDetailed.surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.surface_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.surface_type`')
            vals = {}
            vals["floor"] = "Floor"
            vals["wall"] = "Wall"
            vals["ceiling"] = "Ceiling"
            vals["roof"] = "Roof"
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
                                     'field `BuildingSurfaceDetailed.surface_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `BuildingSurfaceDetailed.surface_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Surface Type"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `BuildingSurfaceDetailed.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `BuildingSurfaceDetailed.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition(self):
        """Get outside_boundary_condition

        Returns:
            str: the value of `outside_boundary_condition` or None if not set
        """
        return self._data["Outside Boundary Condition"]

    @outside_boundary_condition.setter
    def outside_boundary_condition(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition`

        Args:
            value (str): value for IDD Field `Outside Boundary Condition`
                Accepted values are:
                      - Adiabatic
                      - Surface
                      - Zone
                      - Outdoors
                      - Ground
                      - GroundFCfactorMethod
                      - OtherSideCoefficients
                      - OtherSideConditionsModel
                      - GroundSlabPreprocessorAverage
                      - GroundSlabPreprocessorCore
                      - GroundSlabPreprocessorPerimeter
                      - GroundBasementPreprocessorAverageWall
                      - GroundBasementPreprocessorAverageFloor
                      - GroundBasementPreprocessorUpperWall
                      - GroundBasementPreprocessorLowerWall
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
                                 ' for field `BuildingSurfaceDetailed.outside_boundary_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.outside_boundary_condition`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.outside_boundary_condition`')
            vals = {}
            vals["adiabatic"] = "Adiabatic"
            vals["surface"] = "Surface"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            vals["ground"] = "Ground"
            vals["groundfcfactormethod"] = "GroundFCfactorMethod"
            vals["othersidecoefficients"] = "OtherSideCoefficients"
            vals["othersideconditionsmodel"] = "OtherSideConditionsModel"
            vals["groundslabpreprocessoraverage"] = "GroundSlabPreprocessorAverage"
            vals["groundslabpreprocessorcore"] = "GroundSlabPreprocessorCore"
            vals["groundslabpreprocessorperimeter"] = "GroundSlabPreprocessorPerimeter"
            vals["groundbasementpreprocessoraveragewall"] = "GroundBasementPreprocessorAverageWall"
            vals["groundbasementpreprocessoraveragefloor"] = "GroundBasementPreprocessorAverageFloor"
            vals["groundbasementpreprocessorupperwall"] = "GroundBasementPreprocessorUpperWall"
            vals["groundbasementpreprocessorlowerwall"] = "GroundBasementPreprocessorLowerWall"
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
                                     'field `BuildingSurfaceDetailed.outside_boundary_condition`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `BuildingSurfaceDetailed.outside_boundary_condition`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Outside Boundary Condition"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Non-blank only if the field Outside Boundary Condition is Surface,
        Zone, OtherSideCoefficients or OtherSideConditionsModel
        If Surface, specify name of corresponding surface in adjacent zone or
        specify current surface name for internal partition separating like zones
        If Zone, specify the name of the corresponding zone and
        the program will generate the corresponding interzone surface
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        If OtherSideConditionsModel, specify name of SurfaceProperty:OtherSideConditionsModel

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `BuildingSurfaceDetailed.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value="SunExposed"):
        """  Corresponds to IDD Field `Sun Exposure`

        Args:
            value (str): value for IDD Field `Sun Exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                Default value: SunExposed
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
                                 ' for field `BuildingSurfaceDetailed.sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.sun_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.sun_exposure`')
            vals = {}
            vals["sunexposed"] = "SunExposed"
            vals["nosun"] = "NoSun"
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
                                     'field `BuildingSurfaceDetailed.sun_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `BuildingSurfaceDetailed.sun_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sun Exposure"] = value

    @property
    def wind_exposure(self):
        """Get wind_exposure

        Returns:
            str: the value of `wind_exposure` or None if not set
        """
        return self._data["Wind Exposure"]

    @wind_exposure.setter
    def wind_exposure(self, value="WindExposed"):
        """  Corresponds to IDD Field `Wind Exposure`

        Args:
            value (str): value for IDD Field `Wind Exposure`
                Accepted values are:
                      - WindExposed
                      - NoWind
                Default value: WindExposed
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
                                 ' for field `BuildingSurfaceDetailed.wind_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `BuildingSurfaceDetailed.wind_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `BuildingSurfaceDetailed.wind_exposure`')
            vals = {}
            vals["windexposed"] = "WindExposed"
            vals["nowind"] = "NoWind"
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
                                     'field `BuildingSurfaceDetailed.wind_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `BuildingSurfaceDetailed.wind_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Exposure"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value="autocalculate"):
        """  Corresponds to IDD Field `View Factor to Ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float or "Autocalculate"): value for IDD Field `View Factor to Ground`
                Default value: "autocalculate"
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `BuildingSurfaceDetailed.view_factor_to_ground`'.format(value))
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `BuildingSurfaceDetailed.view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `BuildingSurfaceDetailed.view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `BuildingSurfaceDetailed.view_factor_to_ground`')
        self._data["View Factor to Ground"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 120 vertex coordinates -- extensible object
        "extensible" -- duplicate last set of x,y,z coordinates (last 3 fields),
        remembering to remove ; from "inner" fields.
        for clarity in any error messages, renumber the fields as well.
        (and changing z terminator to a comma "," for all but last one which needs a semi-colon ";")
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `BuildingSurfaceDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `BuildingSurfaceDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `BuildingSurfaceDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `BuildingSurfaceDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `BuildingSurfaceDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `BuildingSurfaceDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field BuildingSurfaceDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field BuildingSurfaceDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for BuildingSurfaceDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for BuildingSurfaceDetailed: {} / {}".format(out_fields,
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

class WallDetailed(object):
    """ Corresponds to IDD object `Wall:Detailed`
        Allows for detailed entry of wall heat transfer surfaces.
    """
    internal_name = "Wall:Detailed"
    field_count = 9
    required_fields = ["Name", "Construction Name", "Zone Name", "Outside Boundary Condition", "Sun Exposure", "Wind Exposure"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 18
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Wall:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Sun Exposure"] = None
        self._data["Wind Exposure"] = None
        self._data["View Factor to Ground"] = None
        self._data["Number of Vertices"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition = None
        else:
            self.outside_boundary_condition = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_exposure = None
        else:
            self.wind_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `WallDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `WallDetailed.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `WallDetailed.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition(self):
        """Get outside_boundary_condition

        Returns:
            str: the value of `outside_boundary_condition` or None if not set
        """
        return self._data["Outside Boundary Condition"]

    @outside_boundary_condition.setter
    def outside_boundary_condition(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition`

        Args:
            value (str): value for IDD Field `Outside Boundary Condition`
                Accepted values are:
                      - Adiabatic
                      - Surface
                      - Zone
                      - Outdoors
                      - Ground
                      - GroundFCfactorMethod
                      - OtherSideCoefficients
                      - OtherSideConditionsModel
                      - GroundSlabPreprocessorAverage
                      - GroundSlabPreprocessorCore
                      - GroundSlabPreprocessorPerimeter
                      - GroundBasementPreprocessorAverageWall
                      - GroundBasementPreprocessorAverageFloor
                      - GroundBasementPreprocessorUpperWall
                      - GroundBasementPreprocessorLowerWall
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
                                 ' for field `WallDetailed.outside_boundary_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.outside_boundary_condition`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.outside_boundary_condition`')
            vals = {}
            vals["adiabatic"] = "Adiabatic"
            vals["surface"] = "Surface"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            vals["ground"] = "Ground"
            vals["groundfcfactormethod"] = "GroundFCfactorMethod"
            vals["othersidecoefficients"] = "OtherSideCoefficients"
            vals["othersideconditionsmodel"] = "OtherSideConditionsModel"
            vals["groundslabpreprocessoraverage"] = "GroundSlabPreprocessorAverage"
            vals["groundslabpreprocessorcore"] = "GroundSlabPreprocessorCore"
            vals["groundslabpreprocessorperimeter"] = "GroundSlabPreprocessorPerimeter"
            vals["groundbasementpreprocessoraveragewall"] = "GroundBasementPreprocessorAverageWall"
            vals["groundbasementpreprocessoraveragefloor"] = "GroundBasementPreprocessorAverageFloor"
            vals["groundbasementpreprocessorupperwall"] = "GroundBasementPreprocessorUpperWall"
            vals["groundbasementpreprocessorlowerwall"] = "GroundBasementPreprocessorLowerWall"
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
                                     'field `WallDetailed.outside_boundary_condition`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WallDetailed.outside_boundary_condition`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Outside Boundary Condition"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Non-blank only if the field Outside Boundary Condition is Surface,
        Zone, OtherSideCoefficients or OtherSideConditionsModel
        If Surface, specify name of corresponding surface in adjacent zone or
        specify current surface name for internal partition separating like zones
        If Zone, specify the name of the corresponding zone and
        the program will generate the corresponding interzone surface
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        If OtherSideConditionsModel, specify name of SurfaceProperty:OtherSideConditionsModel

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `WallDetailed.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value="SunExposed"):
        """  Corresponds to IDD Field `Sun Exposure`

        Args:
            value (str): value for IDD Field `Sun Exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                Default value: SunExposed
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
                                 ' for field `WallDetailed.sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.sun_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.sun_exposure`')
            vals = {}
            vals["sunexposed"] = "SunExposed"
            vals["nosun"] = "NoSun"
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
                                     'field `WallDetailed.sun_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WallDetailed.sun_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sun Exposure"] = value

    @property
    def wind_exposure(self):
        """Get wind_exposure

        Returns:
            str: the value of `wind_exposure` or None if not set
        """
        return self._data["Wind Exposure"]

    @wind_exposure.setter
    def wind_exposure(self, value="WindExposed"):
        """  Corresponds to IDD Field `Wind Exposure`

        Args:
            value (str): value for IDD Field `Wind Exposure`
                Accepted values are:
                      - WindExposed
                      - NoWind
                Default value: WindExposed
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
                                 ' for field `WallDetailed.wind_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallDetailed.wind_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallDetailed.wind_exposure`')
            vals = {}
            vals["windexposed"] = "WindExposed"
            vals["nowind"] = "NoWind"
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
                                     'field `WallDetailed.wind_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WallDetailed.wind_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Exposure"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value="autocalculate"):
        """  Corresponds to IDD Field `View Factor to Ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float or "Autocalculate"): value for IDD Field `View Factor to Ground`
                Default value: "autocalculate"
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `WallDetailed.view_factor_to_ground`'.format(value))
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `WallDetailed.view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallDetailed.view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WallDetailed.view_factor_to_ground`')
        self._data["View Factor to Ground"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 10 vertex coordinates -- extensible object
        "extensible" -- duplicate last set of x,y,z coordinates, renumbering please
        (and changing z terminator to a comma "," for all but last one which needs a semi-colon ";")
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `WallDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `WallDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `WallDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `WallDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `WallDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `WallDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field WallDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WallDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WallDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WallDetailed: {} / {}".format(out_fields,
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

class RoofCeilingDetailed(object):
    """ Corresponds to IDD object `RoofCeiling:Detailed`
        Allows for detailed entry of roof/ceiling heat transfer surfaces.
    """
    internal_name = "RoofCeiling:Detailed"
    field_count = 9
    required_fields = ["Name", "Construction Name", "Zone Name", "Outside Boundary Condition", "Sun Exposure", "Wind Exposure"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 18
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoofCeiling:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Sun Exposure"] = None
        self._data["Wind Exposure"] = None
        self._data["View Factor to Ground"] = None
        self._data["Number of Vertices"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition = None
        else:
            self.outside_boundary_condition = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_exposure = None
        else:
            self.wind_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `RoofCeilingDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `RoofCeilingDetailed.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `RoofCeilingDetailed.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition(self):
        """Get outside_boundary_condition

        Returns:
            str: the value of `outside_boundary_condition` or None if not set
        """
        return self._data["Outside Boundary Condition"]

    @outside_boundary_condition.setter
    def outside_boundary_condition(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition`

        Args:
            value (str): value for IDD Field `Outside Boundary Condition`
                Accepted values are:
                      - Adiabatic
                      - Surface
                      - Zone
                      - Outdoors
                      - Ground
                      - OtherSideCoefficients
                      - OtherSideConditionsModel
                      - GroundSlabPreprocessorAverage
                      - GroundSlabPreprocessorCore
                      - GroundSlabPreprocessorPerimeter
                      - GroundBasementPreprocessorAverageWall
                      - GroundBasementPreprocessorAverageFloor
                      - GroundBasementPreprocessorUpperWall
                      - GroundBasementPreprocessorLowerWall
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
                                 ' for field `RoofCeilingDetailed.outside_boundary_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.outside_boundary_condition`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.outside_boundary_condition`')
            vals = {}
            vals["adiabatic"] = "Adiabatic"
            vals["surface"] = "Surface"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            vals["ground"] = "Ground"
            vals["othersidecoefficients"] = "OtherSideCoefficients"
            vals["othersideconditionsmodel"] = "OtherSideConditionsModel"
            vals["groundslabpreprocessoraverage"] = "GroundSlabPreprocessorAverage"
            vals["groundslabpreprocessorcore"] = "GroundSlabPreprocessorCore"
            vals["groundslabpreprocessorperimeter"] = "GroundSlabPreprocessorPerimeter"
            vals["groundbasementpreprocessoraveragewall"] = "GroundBasementPreprocessorAverageWall"
            vals["groundbasementpreprocessoraveragefloor"] = "GroundBasementPreprocessorAverageFloor"
            vals["groundbasementpreprocessorupperwall"] = "GroundBasementPreprocessorUpperWall"
            vals["groundbasementpreprocessorlowerwall"] = "GroundBasementPreprocessorLowerWall"
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
                                     'field `RoofCeilingDetailed.outside_boundary_condition`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `RoofCeilingDetailed.outside_boundary_condition`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Outside Boundary Condition"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Non-blank only if the field Outside Boundary Condition is Surface,
        Zone, OtherSideCoefficients or OtherSideConditionsModel
        If Surface, specify name of corresponding surface in adjacent zone or
        specify current surface name for internal partition separating like zones
        If Zone, specify the name of the corresponding zone and
        the program will generate the corresponding interzone surface
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        If OtherSideConditionsModel, specify name of SurfaceProperty:OtherSideConditionsModel

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `RoofCeilingDetailed.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value="SunExposed"):
        """  Corresponds to IDD Field `Sun Exposure`

        Args:
            value (str): value for IDD Field `Sun Exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                Default value: SunExposed
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
                                 ' for field `RoofCeilingDetailed.sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.sun_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.sun_exposure`')
            vals = {}
            vals["sunexposed"] = "SunExposed"
            vals["nosun"] = "NoSun"
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
                                     'field `RoofCeilingDetailed.sun_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `RoofCeilingDetailed.sun_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sun Exposure"] = value

    @property
    def wind_exposure(self):
        """Get wind_exposure

        Returns:
            str: the value of `wind_exposure` or None if not set
        """
        return self._data["Wind Exposure"]

    @wind_exposure.setter
    def wind_exposure(self, value="WindExposed"):
        """  Corresponds to IDD Field `Wind Exposure`

        Args:
            value (str): value for IDD Field `Wind Exposure`
                Accepted values are:
                      - WindExposed
                      - NoWind
                Default value: WindExposed
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
                                 ' for field `RoofCeilingDetailed.wind_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `RoofCeilingDetailed.wind_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `RoofCeilingDetailed.wind_exposure`')
            vals = {}
            vals["windexposed"] = "WindExposed"
            vals["nowind"] = "NoWind"
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
                                     'field `RoofCeilingDetailed.wind_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `RoofCeilingDetailed.wind_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Exposure"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value="autocalculate"):
        """  Corresponds to IDD Field `View Factor to Ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float or "Autocalculate"): value for IDD Field `View Factor to Ground`
                Default value: "autocalculate"
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `RoofCeilingDetailed.view_factor_to_ground`'.format(value))
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `RoofCeilingDetailed.view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `RoofCeilingDetailed.view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `RoofCeilingDetailed.view_factor_to_ground`')
        self._data["View Factor to Ground"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 10 vertex coordinates -- extensible object
        "extensible" -- duplicate last set of x,y,z coordinates, renumbering please
        (and changing z terminator to a comma "," for all but last one which needs a semi-colon ";")
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `RoofCeilingDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `RoofCeilingDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `RoofCeilingDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `RoofCeilingDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `RoofCeilingDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `RoofCeilingDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field RoofCeilingDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field RoofCeilingDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for RoofCeilingDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for RoofCeilingDetailed: {} / {}".format(out_fields,
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

class FloorDetailed(object):
    """ Corresponds to IDD object `Floor:Detailed`
        Allows for detailed entry of floor heat transfer surfaces.
    """
    internal_name = "Floor:Detailed"
    field_count = 9
    required_fields = ["Name", "Construction Name", "Zone Name", "Outside Boundary Condition", "Sun Exposure", "Wind Exposure"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 18
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Floor:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Sun Exposure"] = None
        self._data["Wind Exposure"] = None
        self._data["View Factor to Ground"] = None
        self._data["Number of Vertices"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition = None
        else:
            self.outside_boundary_condition = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_exposure = None
        else:
            self.wind_exposure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `FloorDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `FloorDetailed.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `FloorDetailed.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition(self):
        """Get outside_boundary_condition

        Returns:
            str: the value of `outside_boundary_condition` or None if not set
        """
        return self._data["Outside Boundary Condition"]

    @outside_boundary_condition.setter
    def outside_boundary_condition(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition`

        Args:
            value (str): value for IDD Field `Outside Boundary Condition`
                Accepted values are:
                      - Adiabatic
                      - Surface
                      - Zone
                      - Outdoors
                      - Ground
                      - GroundFCfactorMethod
                      - OtherSideCoefficients
                      - OtherSideConditionsModel
                      - GroundSlabPreprocessorAverage
                      - GroundSlabPreprocessorCore
                      - GroundSlabPreprocessorPerimeter
                      - GroundBasementPreprocessorAverageWall
                      - GroundBasementPreprocessorAverageFloor
                      - GroundBasementPreprocessorUpperWall
                      - GroundBasementPreprocessorLowerWall
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
                                 ' for field `FloorDetailed.outside_boundary_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.outside_boundary_condition`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.outside_boundary_condition`')
            vals = {}
            vals["adiabatic"] = "Adiabatic"
            vals["surface"] = "Surface"
            vals["zone"] = "Zone"
            vals["outdoors"] = "Outdoors"
            vals["ground"] = "Ground"
            vals["groundfcfactormethod"] = "GroundFCfactorMethod"
            vals["othersidecoefficients"] = "OtherSideCoefficients"
            vals["othersideconditionsmodel"] = "OtherSideConditionsModel"
            vals["groundslabpreprocessoraverage"] = "GroundSlabPreprocessorAverage"
            vals["groundslabpreprocessorcore"] = "GroundSlabPreprocessorCore"
            vals["groundslabpreprocessorperimeter"] = "GroundSlabPreprocessorPerimeter"
            vals["groundbasementpreprocessoraveragewall"] = "GroundBasementPreprocessorAverageWall"
            vals["groundbasementpreprocessoraveragefloor"] = "GroundBasementPreprocessorAverageFloor"
            vals["groundbasementpreprocessorupperwall"] = "GroundBasementPreprocessorUpperWall"
            vals["groundbasementpreprocessorlowerwall"] = "GroundBasementPreprocessorLowerWall"
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
                                     'field `FloorDetailed.outside_boundary_condition`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FloorDetailed.outside_boundary_condition`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Outside Boundary Condition"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Non-blank only if the field Outside Boundary Condition is Surface,
        Zone, OtherSideCoefficients or OtherSideConditionsModel
        If Surface, specify name of corresponding surface in adjacent zone or
        specify current surface name for internal partition separating like zones
        If Zone, specify the name of the corresponding zone and
        the program will generate the corresponding interzone surface
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        If OtherSideConditionsModel, specify name of SurfaceProperty:OtherSideConditionsModel

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `FloorDetailed.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value="SunExposed"):
        """  Corresponds to IDD Field `Sun Exposure`

        Args:
            value (str): value for IDD Field `Sun Exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                Default value: SunExposed
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
                                 ' for field `FloorDetailed.sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.sun_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.sun_exposure`')
            vals = {}
            vals["sunexposed"] = "SunExposed"
            vals["nosun"] = "NoSun"
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
                                     'field `FloorDetailed.sun_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FloorDetailed.sun_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sun Exposure"] = value

    @property
    def wind_exposure(self):
        """Get wind_exposure

        Returns:
            str: the value of `wind_exposure` or None if not set
        """
        return self._data["Wind Exposure"]

    @wind_exposure.setter
    def wind_exposure(self, value="WindExposed"):
        """  Corresponds to IDD Field `Wind Exposure`

        Args:
            value (str): value for IDD Field `Wind Exposure`
                Accepted values are:
                      - WindExposed
                      - NoWind
                Default value: WindExposed
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
                                 ' for field `FloorDetailed.wind_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorDetailed.wind_exposure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorDetailed.wind_exposure`')
            vals = {}
            vals["windexposed"] = "WindExposed"
            vals["nowind"] = "NoWind"
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
                                     'field `FloorDetailed.wind_exposure`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FloorDetailed.wind_exposure`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Exposure"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value="autocalculate"):
        """  Corresponds to IDD Field `View Factor to Ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float or "Autocalculate"): value for IDD Field `View Factor to Ground`
                Default value: "autocalculate"
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `FloorDetailed.view_factor_to_ground`'.format(value))
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `FloorDetailed.view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorDetailed.view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `FloorDetailed.view_factor_to_ground`')
        self._data["View Factor to Ground"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 10 vertex coordinates -- extensible object
        "extensible" -- duplicate last set of x,y,z coordinates, renumbering please
        (and changing z terminator to a comma "," for all but last one which needs a semi-colon ";")
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `FloorDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `FloorDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `FloorDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `FloorDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `FloorDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `FloorDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field FloorDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FloorDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FloorDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FloorDetailed: {} / {}".format(out_fields,
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

class WallExterior(object):
    """ Corresponds to IDD object `Wall:Exterior`
        Allows for simplified entry of exterior walls.
        View Factor to Ground is automatically calculated.
    """
    internal_name = "Wall:Exterior"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Wall:Exterior`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `WallExterior.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallExterior.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallExterior.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `WallExterior.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallExterior.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallExterior.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `WallExterior.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallExterior.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallExterior.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `WallExterior.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallExterior.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `WallExterior.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `WallExterior.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallExterior.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `WallExterior.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `WallExterior.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `WallExterior.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `WallExterior.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `WallExterior.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `WallExterior.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field WallExterior:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WallExterior:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WallExterior: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WallExterior: {} / {}".format(out_fields,
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

class WallAdiabatic(object):
    """ Corresponds to IDD object `Wall:Adiabatic`
        Allows for simplified entry of interior walls.
    """
    internal_name = "Wall:Adiabatic"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Wall:Adiabatic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `WallAdiabatic.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallAdiabatic.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallAdiabatic.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `WallAdiabatic.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallAdiabatic.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallAdiabatic.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `WallAdiabatic.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallAdiabatic.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallAdiabatic.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `WallAdiabatic.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallAdiabatic.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `WallAdiabatic.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `WallAdiabatic.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallAdiabatic.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `WallAdiabatic.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `WallAdiabatic.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `WallAdiabatic.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `WallAdiabatic.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `WallAdiabatic.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `WallAdiabatic.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field WallAdiabatic:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WallAdiabatic:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WallAdiabatic: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WallAdiabatic: {} / {}".format(out_fields,
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

class WallUnderground(object):
    """ Corresponds to IDD object `Wall:Underground`
        Allows for simplified entry of underground walls.
    """
    internal_name = "Wall:Underground"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Wall:Underground`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `WallUnderground.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallUnderground.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallUnderground.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file.
        If the construction is type "Construction:CfactorUndergroundWall",
        then the GroundFCfactorMethod will be used.

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `WallUnderground.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallUnderground.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallUnderground.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `WallUnderground.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallUnderground.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallUnderground.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `WallUnderground.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallUnderground.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `WallUnderground.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `WallUnderground.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallUnderground.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `WallUnderground.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `WallUnderground.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `WallUnderground.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `WallUnderground.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `WallUnderground.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `WallUnderground.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field WallUnderground:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WallUnderground:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WallUnderground: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WallUnderground: {} / {}".format(out_fields,
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

class WallInterzone(object):
    """ Corresponds to IDD object `Wall:Interzone`
        Allows for simplified entry of interzone walls (walls between zones).
    """
    internal_name = "Wall:Interzone"
    field_count = 11
    required_fields = ["Name", "Construction Name", "Zone Name", "Outside Boundary Condition Object"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Wall:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `WallInterzone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallInterzone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallInterzone.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `WallInterzone.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallInterzone.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallInterzone.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone for the inside of the surface

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `WallInterzone.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallInterzone.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallInterzone.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Specify a surface name in an adjacent zone for known interior walls.
        Specify a zone name of an adjacent zone to automatically generate
        the interior wall in the adjacent zone.

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `WallInterzone.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WallInterzone.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WallInterzone.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `WallInterzone.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallInterzone.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `WallInterzone.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Walls are usually tilted 90 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `WallInterzone.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WallInterzone.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `WallInterzone.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Starting (x,y,z) coordinate is the Lower Left Corner of the Wall

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `WallInterzone.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `WallInterzone.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `WallInterzone.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `WallInterzone.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `WallInterzone.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field WallInterzone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WallInterzone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WallInterzone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WallInterzone: {} / {}".format(out_fields,
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

class Roof(object):
    """ Corresponds to IDD object `Roof`
        Allows for simplified entry of roofs (exterior).
        View Factor to Ground is automatically calculated.
    """
    internal_name = "Roof"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Roof`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Width"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width = None
        else:
            self.width = vals[i]
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
                                 ' for field `Roof.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Roof.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Roof.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `Roof.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Roof.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Roof.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `Roof.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Roof.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Roof.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of Roof

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `Roof.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `Roof.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `Roof.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=0.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Flat Roofs are tilted 0 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 0.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `Roof.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `Roof.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `Roof.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        If not Flat, Starting coordinate is the Lower Left Corner of the Roof

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `Roof.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `Roof.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `Roof.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        Along X Axis

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `Roof.length`'.format(value))
        self._data["Length"] = value

    @property
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `Width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `Width`
                Units: m
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
                                 ' for field `Roof.width`'.format(value))
        self._data["Width"] = value

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
                    raise ValueError("Required field Roof:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Roof:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Roof: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Roof: {} / {}".format(out_fields,
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

class CeilingAdiabatic(object):
    """ Corresponds to IDD object `Ceiling:Adiabatic`
        Allows for simplified entry of interior ceilings.
    """
    internal_name = "Ceiling:Adiabatic"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Ceiling:Adiabatic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Width"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width = None
        else:
            self.width = vals[i]
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
                                 ' for field `CeilingAdiabatic.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingAdiabatic.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingAdiabatic.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `CeilingAdiabatic.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingAdiabatic.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingAdiabatic.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `CeilingAdiabatic.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingAdiabatic.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingAdiabatic.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of Ceiling

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `CeilingAdiabatic.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `CeilingAdiabatic.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `CeilingAdiabatic.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=0.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Ceilings are usually tilted 0 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 0.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `CeilingAdiabatic.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `CeilingAdiabatic.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `CeilingAdiabatic.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        If not Flat, Starting coordinate is the Lower Left Corner of the Ceiling

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `CeilingAdiabatic.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `CeilingAdiabatic.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `CeilingAdiabatic.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        Along X Axis

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `CeilingAdiabatic.length`'.format(value))
        self._data["Length"] = value

    @property
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `Width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `Width`
                Units: m
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
                                 ' for field `CeilingAdiabatic.width`'.format(value))
        self._data["Width"] = value

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
                    raise ValueError("Required field CeilingAdiabatic:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field CeilingAdiabatic:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for CeilingAdiabatic: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for CeilingAdiabatic: {} / {}".format(out_fields,
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

class CeilingInterzone(object):
    """ Corresponds to IDD object `Ceiling:Interzone`
        Allows for simplified entry of ceilings using adjacent zone
        (interzone) heat transfer - adjacent surface should be a floor
    """
    internal_name = "Ceiling:Interzone"
    field_count = 11
    required_fields = ["Name", "Construction Name", "Zone Name", "Outside Boundary Condition Object"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Ceiling:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Width"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width = None
        else:
            self.width = vals[i]
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
                                 ' for field `CeilingInterzone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingInterzone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingInterzone.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `CeilingInterzone.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingInterzone.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingInterzone.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone for the inside of the surface

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `CeilingInterzone.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingInterzone.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingInterzone.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Specify a surface name in an adjacent zone for known interior floors
        Specify a zone name of an adjacent zone to automatically generate
        the interior floor in the adjacent zone.

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `CeilingInterzone.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `CeilingInterzone.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `CeilingInterzone.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of wall (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `CeilingInterzone.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `CeilingInterzone.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `CeilingInterzone.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=0.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Ceilings are usually tilted 0 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 0.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `CeilingInterzone.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `CeilingInterzone.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `CeilingInterzone.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        If not Flat, should be Lower Left Corner (from outside)

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `CeilingInterzone.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `CeilingInterzone.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `CeilingInterzone.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        Along X Axis

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `CeilingInterzone.length`'.format(value))
        self._data["Length"] = value

    @property
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `Width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `Width`
                Units: m
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
                                 ' for field `CeilingInterzone.width`'.format(value))
        self._data["Width"] = value

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
                    raise ValueError("Required field CeilingInterzone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field CeilingInterzone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for CeilingInterzone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for CeilingInterzone: {} / {}".format(out_fields,
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

class FloorGroundContact(object):
    """ Corresponds to IDD object `Floor:GroundContact`
        Allows for simplified entry of exterior floors with ground contact.
        View Factors to Ground is automatically calculated.
    """
    internal_name = "Floor:GroundContact"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Floor:GroundContact`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Width"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width = None
        else:
            self.width = vals[i]
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
                                 ' for field `FloorGroundContact.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorGroundContact.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorGroundContact.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file
        If the construction is type "Construction:FfactorGroundFloor",
        then the GroundFCfactorMethod will be used.

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `FloorGroundContact.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorGroundContact.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorGroundContact.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `FloorGroundContact.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorGroundContact.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorGroundContact.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `FloorGroundContact.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorGroundContact.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `FloorGroundContact.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=180.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Floors are usually tilted 180 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 180.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `FloorGroundContact.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorGroundContact.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `FloorGroundContact.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        if not flat, should be lower left corner (from outside)

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `FloorGroundContact.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `FloorGroundContact.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `FloorGroundContact.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        Along X Axis

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `FloorGroundContact.length`'.format(value))
        self._data["Length"] = value

    @property
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `Width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `Width`
                Units: m
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
                                 ' for field `FloorGroundContact.width`'.format(value))
        self._data["Width"] = value

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
                    raise ValueError("Required field FloorGroundContact:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FloorGroundContact:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FloorGroundContact: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FloorGroundContact: {} / {}".format(out_fields,
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

class FloorAdiabatic(object):
    """ Corresponds to IDD object `Floor:Adiabatic`
        Allows for simplified entry of exterior floors
        ignoring ground contact or interior floors.
        View Factor to Ground is automatically calculated.
    """
    internal_name = "Floor:Adiabatic"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Floor:Adiabatic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Width"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width = None
        else:
            self.width = vals[i]
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
                                 ' for field `FloorAdiabatic.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorAdiabatic.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorAdiabatic.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `FloorAdiabatic.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorAdiabatic.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorAdiabatic.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `FloorAdiabatic.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorAdiabatic.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorAdiabatic.zone_name`')
        self._data["Zone Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `FloorAdiabatic.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorAdiabatic.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `FloorAdiabatic.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=180.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Floors are usually tilted 180 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 180.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `FloorAdiabatic.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorAdiabatic.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `FloorAdiabatic.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        if not flat, should be lower left corner (from outside)

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `FloorAdiabatic.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `FloorAdiabatic.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `FloorAdiabatic.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        Along X Axis

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `FloorAdiabatic.length`'.format(value))
        self._data["Length"] = value

    @property
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `Width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `Width`
                Units: m
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
                                 ' for field `FloorAdiabatic.width`'.format(value))
        self._data["Width"] = value

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
                    raise ValueError("Required field FloorAdiabatic:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FloorAdiabatic:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FloorAdiabatic: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FloorAdiabatic: {} / {}".format(out_fields,
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

class FloorInterzone(object):
    """ Corresponds to IDD object `Floor:Interzone`
        Allows for simplified entry of floors using adjacent zone
        (interzone) heat transfer - adjacent surface should be a ceiling.
    """
    internal_name = "Floor:Interzone"
    field_count = 11
    required_fields = ["Name", "Construction Name", "Zone Name", "Outside Boundary Condition Object"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Floor:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Width"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.width = None
        else:
            self.width = vals[i]
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
                                 ' for field `FloorInterzone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorInterzone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorInterzone.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `FloorInterzone.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorInterzone.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorInterzone.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone for the inside of the surface

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `FloorInterzone.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorInterzone.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorInterzone.zone_name`')
        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Specify a surface name in an adjacent zone for known interior ceilings.
        Specify a zone name of an adjacent zone to automatically generate
        the interior ceiling in the adjacent zone.

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `FloorInterzone.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FloorInterzone.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FloorInterzone.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `FloorInterzone.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorInterzone.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `FloorInterzone.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=180.0):
        """  Corresponds to IDD Field `Tilt Angle`
        Floors are usually tilted 180 degrees

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 180.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `FloorInterzone.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FloorInterzone.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `FloorInterzone.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        If not Flat, should be Lower Left Corner (from outside)

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `FloorInterzone.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `FloorInterzone.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `FloorInterzone.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`
        Along X Axis

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `FloorInterzone.length`'.format(value))
        self._data["Length"] = value

    @property
    def width(self):
        """Get width

        Returns:
            float: the value of `width` or None if not set
        """
        return self._data["Width"]

    @width.setter
    def width(self, value=None):
        """  Corresponds to IDD Field `Width`
        Along Y Axis

        Args:
            value (float): value for IDD Field `Width`
                Units: m
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
                                 ' for field `FloorInterzone.width`'.format(value))
        self._data["Width"] = value

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
                    raise ValueError("Required field FloorInterzone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FloorInterzone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FloorInterzone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FloorInterzone: {} / {}".format(out_fields,
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

class FenestrationSurfaceDetailed(object):
    """ Corresponds to IDD object `FenestrationSurface:Detailed`
        Allows for detailed entry of subsurfaces
        (windows, doors, glass doors, tubular daylighting devices).
    """
    internal_name = "FenestrationSurface:Detailed"
    field_count = 22
    required_fields = ["Name", "Surface Type", "Construction Name", "Building Surface Name", "Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate", "Vertex 2 X-coordinate", "Vertex 2 Y-coordinate", "Vertex 2 Z-coordinate", "Vertex 3 X-coordinate", "Vertex 3 Y-coordinate", "Vertex 3 Z-coordinate"]
    extensible_fields = 0
    format = "vertices"
    min_fields = 19
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FenestrationSurface:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Type"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["View Factor to Ground"] = None
        self._data["Shading Control Name"] = None
        self._data["Frame and Divider Name"] = None
        self._data["Multiplier"] = None
        self._data["Number of Vertices"] = None
        self._data["Vertex 1 X-coordinate"] = None
        self._data["Vertex 1 Y-coordinate"] = None
        self._data["Vertex 1 Z-coordinate"] = None
        self._data["Vertex 2 X-coordinate"] = None
        self._data["Vertex 2 Y-coordinate"] = None
        self._data["Vertex 2 Z-coordinate"] = None
        self._data["Vertex 3 X-coordinate"] = None
        self._data["Vertex 3 Y-coordinate"] = None
        self._data["Vertex 3 Z-coordinate"] = None
        self._data["Vertex 4 X-coordinate"] = None
        self._data["Vertex 4 Y-coordinate"] = None
        self._data["Vertex 4 Z-coordinate"] = None
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
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shading_control_name = None
        else:
            self.shading_control_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_and_divider_name = None
        else:
            self.frame_and_divider_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_1_xcoordinate = None
        else:
            self.vertex_1_xcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_1_ycoordinate = None
        else:
            self.vertex_1_ycoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_1_zcoordinate = None
        else:
            self.vertex_1_zcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_2_xcoordinate = None
        else:
            self.vertex_2_xcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_2_ycoordinate = None
        else:
            self.vertex_2_ycoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_2_zcoordinate = None
        else:
            self.vertex_2_zcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_3_xcoordinate = None
        else:
            self.vertex_3_xcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_3_ycoordinate = None
        else:
            self.vertex_3_ycoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_3_zcoordinate = None
        else:
            self.vertex_3_zcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_4_xcoordinate = None
        else:
            self.vertex_4_xcoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_4_ycoordinate = None
        else:
            self.vertex_4_ycoordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertex_4_zcoordinate = None
        else:
            self.vertex_4_zcoordinate = vals[i]
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
                                 ' for field `FenestrationSurfaceDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.name`')
        self._data["Name"] = value

    @property
    def surface_type(self):
        """Get surface_type

        Returns:
            str: the value of `surface_type` or None if not set
        """
        return self._data["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """  Corresponds to IDD Field `Surface Type`

        Args:
            value (str): value for IDD Field `Surface Type`
                Accepted values are:
                      - Window
                      - Door
                      - GlassDoor
                      - TubularDaylightDome
                      - TubularDaylightDiffuser
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
                                 ' for field `FenestrationSurfaceDetailed.surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.surface_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.surface_type`')
            vals = {}
            vals["window"] = "Window"
            vals["door"] = "Door"
            vals["glassdoor"] = "GlassDoor"
            vals["tubulardaylightdome"] = "TubularDaylightDome"
            vals["tubulardaylightdiffuser"] = "TubularDaylightDiffuser"
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
                                     'field `FenestrationSurfaceDetailed.surface_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FenestrationSurfaceDetailed.surface_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Surface Type"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `FenestrationSurfaceDetailed.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `FenestrationSurfaceDetailed.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Non-blank only if base surface field Outside Boundary Condition is
        Surface or OtherSideCoefficients
        If Base Surface's Surface, specify name of corresponding subsurface in adjacent zone or
        specify current subsurface name for internal partition separating like zones
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        or leave blank to inherit Base Surface's OtherSide Coefficients

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `FenestrationSurfaceDetailed.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value="autocalculate"):
        """  Corresponds to IDD Field `View Factor to Ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float or "Autocalculate"): value for IDD Field `View Factor to Ground`
                Default value: "autocalculate"
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `FenestrationSurfaceDetailed.view_factor_to_ground`'.format(value))
                    self._data["View Factor to Ground"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `FenestrationSurfaceDetailed.view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `FenestrationSurfaceDetailed.view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `FenestrationSurfaceDetailed.view_factor_to_ground`')
        self._data["View Factor to Ground"] = value

    @property
    def shading_control_name(self):
        """Get shading_control_name

        Returns:
            str: the value of `shading_control_name` or None if not set
        """
        return self._data["Shading Control Name"]

    @shading_control_name.setter
    def shading_control_name(self, value=None):
        """  Corresponds to IDD Field `Shading Control Name`
        enter the name of a WindowProperty:ShadingControl object
        used for windows and glass doors only
        If not specified, window or glass door has no shading (blind, roller shade, etc.)

        Args:
            value (str): value for IDD Field `Shading Control Name`
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
                                 ' for field `FenestrationSurfaceDetailed.shading_control_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.shading_control_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.shading_control_name`')
        self._data["Shading Control Name"] = value

    @property
    def frame_and_divider_name(self):
        """Get frame_and_divider_name

        Returns:
            str: the value of `frame_and_divider_name` or None if not set
        """
        return self._data["Frame and Divider Name"]

    @frame_and_divider_name.setter
    def frame_and_divider_name(self, value=None):
        """  Corresponds to IDD Field `Frame and Divider Name`
        Enter the name of a WindowProperty:FrameAndDivider object
        Used only for exterior windows (rectangular) and glass doors.
        Unused for triangular windows.
        If not specified (blank), window or glass door has no frame or divider
        and no beam solar reflection from reveal surfaces.

        Args:
            value (str): value for IDD Field `Frame and Divider Name`
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
                                 ' for field `FenestrationSurfaceDetailed.frame_and_divider_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FenestrationSurfaceDetailed.frame_and_divider_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FenestrationSurfaceDetailed.frame_and_divider_name`')
        self._data["Frame and Divider Name"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `FenestrationSurfaceDetailed.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `FenestrationSurfaceDetailed.multiplier`')
        self._data["Multiplier"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                value <= 4.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `FenestrationSurfaceDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `FenestrationSurfaceDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `FenestrationSurfaceDetailed.number_of_vertices`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `FenestrationSurfaceDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    @property
    def vertex_1_xcoordinate(self):
        """Get vertex_1_xcoordinate

        Returns:
            float: the value of `vertex_1_xcoordinate` or None if not set
        """
        return self._data["Vertex 1 X-coordinate"]

    @vertex_1_xcoordinate.setter
    def vertex_1_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 1 X-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_1_xcoordinate`'.format(value))
        self._data["Vertex 1 X-coordinate"] = value

    @property
    def vertex_1_ycoordinate(self):
        """Get vertex_1_ycoordinate

        Returns:
            float: the value of `vertex_1_ycoordinate` or None if not set
        """
        return self._data["Vertex 1 Y-coordinate"]

    @vertex_1_ycoordinate.setter
    def vertex_1_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 1 Y-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_1_ycoordinate`'.format(value))
        self._data["Vertex 1 Y-coordinate"] = value

    @property
    def vertex_1_zcoordinate(self):
        """Get vertex_1_zcoordinate

        Returns:
            float: the value of `vertex_1_zcoordinate` or None if not set
        """
        return self._data["Vertex 1 Z-coordinate"]

    @vertex_1_zcoordinate.setter
    def vertex_1_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 1 Z-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_1_zcoordinate`'.format(value))
        self._data["Vertex 1 Z-coordinate"] = value

    @property
    def vertex_2_xcoordinate(self):
        """Get vertex_2_xcoordinate

        Returns:
            float: the value of `vertex_2_xcoordinate` or None if not set
        """
        return self._data["Vertex 2 X-coordinate"]

    @vertex_2_xcoordinate.setter
    def vertex_2_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 2 X-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 2 X-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_2_xcoordinate`'.format(value))
        self._data["Vertex 2 X-coordinate"] = value

    @property
    def vertex_2_ycoordinate(self):
        """Get vertex_2_ycoordinate

        Returns:
            float: the value of `vertex_2_ycoordinate` or None if not set
        """
        return self._data["Vertex 2 Y-coordinate"]

    @vertex_2_ycoordinate.setter
    def vertex_2_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 2 Y-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 2 Y-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_2_ycoordinate`'.format(value))
        self._data["Vertex 2 Y-coordinate"] = value

    @property
    def vertex_2_zcoordinate(self):
        """Get vertex_2_zcoordinate

        Returns:
            float: the value of `vertex_2_zcoordinate` or None if not set
        """
        return self._data["Vertex 2 Z-coordinate"]

    @vertex_2_zcoordinate.setter
    def vertex_2_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 2 Z-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 2 Z-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_2_zcoordinate`'.format(value))
        self._data["Vertex 2 Z-coordinate"] = value

    @property
    def vertex_3_xcoordinate(self):
        """Get vertex_3_xcoordinate

        Returns:
            float: the value of `vertex_3_xcoordinate` or None if not set
        """
        return self._data["Vertex 3 X-coordinate"]

    @vertex_3_xcoordinate.setter
    def vertex_3_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 3 X-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 3 X-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_3_xcoordinate`'.format(value))
        self._data["Vertex 3 X-coordinate"] = value

    @property
    def vertex_3_ycoordinate(self):
        """Get vertex_3_ycoordinate

        Returns:
            float: the value of `vertex_3_ycoordinate` or None if not set
        """
        return self._data["Vertex 3 Y-coordinate"]

    @vertex_3_ycoordinate.setter
    def vertex_3_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 3 Y-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 3 Y-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_3_ycoordinate`'.format(value))
        self._data["Vertex 3 Y-coordinate"] = value

    @property
    def vertex_3_zcoordinate(self):
        """Get vertex_3_zcoordinate

        Returns:
            float: the value of `vertex_3_zcoordinate` or None if not set
        """
        return self._data["Vertex 3 Z-coordinate"]

    @vertex_3_zcoordinate.setter
    def vertex_3_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 3 Z-coordinate`

        Args:
            value (float): value for IDD Field `Vertex 3 Z-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_3_zcoordinate`'.format(value))
        self._data["Vertex 3 Z-coordinate"] = value

    @property
    def vertex_4_xcoordinate(self):
        """Get vertex_4_xcoordinate

        Returns:
            float: the value of `vertex_4_xcoordinate` or None if not set
        """
        return self._data["Vertex 4 X-coordinate"]

    @vertex_4_xcoordinate.setter
    def vertex_4_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 4 X-coordinate`
        Not used for triangles

        Args:
            value (float): value for IDD Field `Vertex 4 X-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_4_xcoordinate`'.format(value))
        self._data["Vertex 4 X-coordinate"] = value

    @property
    def vertex_4_ycoordinate(self):
        """Get vertex_4_ycoordinate

        Returns:
            float: the value of `vertex_4_ycoordinate` or None if not set
        """
        return self._data["Vertex 4 Y-coordinate"]

    @vertex_4_ycoordinate.setter
    def vertex_4_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 4 Y-coordinate`
        Not used for triangles

        Args:
            value (float): value for IDD Field `Vertex 4 Y-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_4_ycoordinate`'.format(value))
        self._data["Vertex 4 Y-coordinate"] = value

    @property
    def vertex_4_zcoordinate(self):
        """Get vertex_4_zcoordinate

        Returns:
            float: the value of `vertex_4_zcoordinate` or None if not set
        """
        return self._data["Vertex 4 Z-coordinate"]

    @vertex_4_zcoordinate.setter
    def vertex_4_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `Vertex 4 Z-coordinate`
        Not used for triangles

        Args:
            value (float): value for IDD Field `Vertex 4 Z-coordinate`
                Units: m
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
                                 ' for field `FenestrationSurfaceDetailed.vertex_4_zcoordinate`'.format(value))
        self._data["Vertex 4 Z-coordinate"] = value

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
                    raise ValueError("Required field FenestrationSurfaceDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FenestrationSurfaceDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FenestrationSurfaceDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FenestrationSurfaceDetailed: {} / {}".format(out_fields,
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

class Window(object):
    """ Corresponds to IDD object `Window`
        Allows for simplified entry of Windows.
    """
    internal_name = "Window"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Building Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Window`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Shading Control Name"] = None
        self._data["Frame and Divider Name"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shading_control_name = None
        else:
            self.shading_control_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_and_divider_name = None
        else:
            self.frame_and_divider_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `Window.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Window.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Window.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `Window.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Window.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Window.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        Name of Surface (Wall, usually) the Window is on (i.e., Base Surface)
        Window assumes the azimuth and tilt angles of the surface it is on.

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `Window.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Window.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Window.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def shading_control_name(self):
        """Get shading_control_name

        Returns:
            str: the value of `shading_control_name` or None if not set
        """
        return self._data["Shading Control Name"]

    @shading_control_name.setter
    def shading_control_name(self, value=None):
        """  Corresponds to IDD Field `Shading Control Name`
        enter the name of a WindowProperty:ShadingControl object
        used for windows and glass doors only
        If not specified, window or glass door has no shading (blind, roller shade, etc.)

        Args:
            value (str): value for IDD Field `Shading Control Name`
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
                                 ' for field `Window.shading_control_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Window.shading_control_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Window.shading_control_name`')
        self._data["Shading Control Name"] = value

    @property
    def frame_and_divider_name(self):
        """Get frame_and_divider_name

        Returns:
            str: the value of `frame_and_divider_name` or None if not set
        """
        return self._data["Frame and Divider Name"]

    @frame_and_divider_name.setter
    def frame_and_divider_name(self, value=None):
        """  Corresponds to IDD Field `Frame and Divider Name`
        Enter the name of a WindowProperty:FrameAndDivider object
        Used only for exterior windows (rectangular) and glass doors.
        Unused for triangular windows.
        If not specified (blank), window or glass door has no frame or divider
        and no beam solar reflection from reveal surfaces.

        Args:
            value (str): value for IDD Field `Frame and Divider Name`
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
                                 ' for field `Window.frame_and_divider_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Window.frame_and_divider_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Window.frame_and_divider_name`')
        self._data["Frame and Divider Name"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `Window.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `Window.multiplier`')
        self._data["Multiplier"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Window starting coordinate is specified relative to the Base Surface origin.

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `Window.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`
        How far up the wall the Window starts. (in 2-d, this would be a Y Coordinate)

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `Window.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `Window.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `Window.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field Window:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Window:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Window: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Window: {} / {}".format(out_fields,
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

class Door(object):
    """ Corresponds to IDD object `Door`
        Allows for simplified entry of opaque Doors.
    """
    internal_name = "Door"
    field_count = 8
    required_fields = ["Name", "Construction Name", "Building Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Door`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `Door.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Door.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Door.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `Door.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Door.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Door.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        Name of Surface (Wall, usually) the Door is on (i.e., Base Surface)
        Door assumes the azimuth and tilt angles of the surface it is on.

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `Door.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `Door.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `Door.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `Door.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `Door.multiplier`')
        self._data["Multiplier"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Door starting coordinate is specified relative to the Base Surface origin.

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `Door.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`
        How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `Door.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `Door.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `Door.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field Door:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field Door:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for Door: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for Door: {} / {}".format(out_fields,
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

class GlazedDoor(object):
    """ Corresponds to IDD object `GlazedDoor`
        Allows for simplified entry of glass Doors.
    """
    internal_name = "GlazedDoor"
    field_count = 10
    required_fields = ["Name", "Construction Name", "Building Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GlazedDoor`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Shading Control Name"] = None
        self._data["Frame and Divider Name"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shading_control_name = None
        else:
            self.shading_control_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_and_divider_name = None
        else:
            self.frame_and_divider_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `GlazedDoor.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoor.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoor.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `GlazedDoor.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoor.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoor.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        Name of Surface (Wall, usually) the Door is on (i.e., Base Surface)
        Door assumes the azimuth and tilt angles of the surface it is on.

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `GlazedDoor.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoor.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoor.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def shading_control_name(self):
        """Get shading_control_name

        Returns:
            str: the value of `shading_control_name` or None if not set
        """
        return self._data["Shading Control Name"]

    @shading_control_name.setter
    def shading_control_name(self, value=None):
        """  Corresponds to IDD Field `Shading Control Name`
        enter the name of a WindowProperty:ShadingControl object
        used for windows and glass doors only
        If not specified, window or glass door has no shading (blind, roller shade, etc.)

        Args:
            value (str): value for IDD Field `Shading Control Name`
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
                                 ' for field `GlazedDoor.shading_control_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoor.shading_control_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoor.shading_control_name`')
        self._data["Shading Control Name"] = value

    @property
    def frame_and_divider_name(self):
        """Get frame_and_divider_name

        Returns:
            str: the value of `frame_and_divider_name` or None if not set
        """
        return self._data["Frame and Divider Name"]

    @frame_and_divider_name.setter
    def frame_and_divider_name(self, value=None):
        """  Corresponds to IDD Field `Frame and Divider Name`
        Enter the name of a WindowProperty:FrameAndDivider object
        Used only for exterior windows (rectangular) and glass doors.
        Unused for triangular windows.
        If not specified (blank), window or glass door has no frame or divider
        and no beam solar reflection from reveal surfaces.

        Args:
            value (str): value for IDD Field `Frame and Divider Name`
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
                                 ' for field `GlazedDoor.frame_and_divider_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoor.frame_and_divider_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoor.frame_and_divider_name`')
        self._data["Frame and Divider Name"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `GlazedDoor.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `GlazedDoor.multiplier`')
        self._data["Multiplier"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Door starting coordinate is specified relative to the Base Surface origin.

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `GlazedDoor.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`
        How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `GlazedDoor.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `GlazedDoor.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `GlazedDoor.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field GlazedDoor:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field GlazedDoor:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for GlazedDoor: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for GlazedDoor: {} / {}".format(out_fields,
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

class WindowInterzone(object):
    """ Corresponds to IDD object `Window:Interzone`
        Allows for simplified entry of interzone windows (adjacent to
        other zones).
    """
    internal_name = "Window:Interzone"
    field_count = 9
    required_fields = ["Name", "Construction Name", "Building Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Window:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `WindowInterzone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowInterzone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowInterzone.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `WindowInterzone.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowInterzone.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowInterzone.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        Name of Surface (Wall, usually) the Window is on (i.e., Base Surface)
        Window assumes the azimuth and tilt angles of the surface it is on.

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `WindowInterzone.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowInterzone.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowInterzone.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Specify a surface name in an adjacent zone for known interior windows.
        Specify a zone name of an adjacent zone to automatically generate
        the interior window in the adjacent zone.
        a blank field will set up a Window in an adjacent zone
        (same zone as adjacent to base surface)

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `WindowInterzone.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowInterzone.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowInterzone.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `WindowInterzone.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `WindowInterzone.multiplier`')
        self._data["Multiplier"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Window starting coordinate is specified relative to the Base Surface origin.

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `WindowInterzone.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`
        How far up the wall the Window starts. (in 2-d, this would be a Y Coordinate)

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `WindowInterzone.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `WindowInterzone.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `WindowInterzone.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field WindowInterzone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WindowInterzone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WindowInterzone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WindowInterzone: {} / {}".format(out_fields,
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

class DoorInterzone(object):
    """ Corresponds to IDD object `Door:Interzone`
        Allows for simplified entry of interzone (opaque interior) doors (adjacent to
        other zones).
    """
    internal_name = "Door:Interzone"
    field_count = 9
    required_fields = ["Name", "Construction Name", "Building Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Door:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `DoorInterzone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DoorInterzone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DoorInterzone.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `DoorInterzone.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DoorInterzone.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DoorInterzone.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        Name of Surface (Wall, usually) the Door is on (i.e., Base Surface)
        Door assumes the azimuth and tilt angles of the surface it is on.

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `DoorInterzone.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DoorInterzone.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DoorInterzone.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Specify a surface name in an adjacent zone for known interior doors.
        Specify a zone name of an adjacent zone to automatically generate
        the interior door in the adjacent zone.
        a blank field will set up a Window in an adjacent zone
        (same zone as adjacent to base surface)

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `DoorInterzone.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DoorInterzone.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DoorInterzone.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `DoorInterzone.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `DoorInterzone.multiplier`')
        self._data["Multiplier"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Door starting coordinate is specified relative to the Base Surface origin.

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `DoorInterzone.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`
        How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `DoorInterzone.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `DoorInterzone.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `DoorInterzone.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field DoorInterzone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DoorInterzone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DoorInterzone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DoorInterzone: {} / {}".format(out_fields,
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

class GlazedDoorInterzone(object):
    """ Corresponds to IDD object `GlazedDoor:Interzone`
        Allows for simplified entry of interzone (glass interior) doors (adjacent to
        other zones).
    """
    internal_name = "GlazedDoor:Interzone"
    field_count = 9
    required_fields = ["Name", "Construction Name", "Building Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `GlazedDoor:Interzone`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Building Surface Name"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Multiplier"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.multiplier = None
        else:
            self.multiplier = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `GlazedDoorInterzone.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoorInterzone.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoorInterzone.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `GlazedDoorInterzone.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoorInterzone.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoorInterzone.construction_name`')
        self._data["Construction Name"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        Name of Surface (Wall, usually) the Door is on (i.e., Base Surface)
        Door assumes the azimuth and tilt angles of the surface it is on.

        Args:
            value (str): value for IDD Field `Building Surface Name`
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
                                 ' for field `GlazedDoorInterzone.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoorInterzone.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoorInterzone.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `Outside Boundary Condition Object`
        Specify a surface name in an adjacent zone for known interior doors.
        Specify a zone name of an adjacent zone to automatically generate
        the interior door in the adjacent zone.
        a blank field will set up a Window in an adjacent zone
        (same zone as adjacent to base surface)

        Args:
            value (str): value for IDD Field `Outside Boundary Condition Object`
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
                                 ' for field `GlazedDoorInterzone.outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `GlazedDoorInterzone.outside_boundary_condition_object`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `GlazedDoorInterzone.outside_boundary_condition_object`')
        self._data["Outside Boundary Condition Object"] = value

    @property
    def multiplier(self):
        """Get multiplier

        Returns:
            float: the value of `multiplier` or None if not set
        """
        return self._data["Multiplier"]

    @multiplier.setter
    def multiplier(self, value=1.0):
        """  Corresponds to IDD Field `Multiplier`
        Used only for Surface Type = WINDOW, GLASSDOOR or DOOR
        Non-integer values will be truncated to integer

        Args:
            value (float): value for IDD Field `Multiplier`
                Default value: 1.0
                value >= 1.0
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
                                 ' for field `GlazedDoorInterzone.multiplier`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `GlazedDoorInterzone.multiplier`')
        self._data["Multiplier"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Door starting coordinate is specified relative to the Base Surface origin.

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `GlazedDoorInterzone.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`
        How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `GlazedDoorInterzone.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `GlazedDoorInterzone.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `GlazedDoorInterzone.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field GlazedDoorInterzone:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field GlazedDoorInterzone:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for GlazedDoorInterzone: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for GlazedDoorInterzone: {} / {}".format(out_fields,
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

class WindowPropertyShadingControl(object):
    """ Corresponds to IDD object `WindowProperty:ShadingControl`
        Specifies the type, location, and controls for window shades, window blinds, and
        switchable glazing. Referenced by the surface objects for exterior windows and glass
        doors (ref: FenestrationSurface:Detailed, Window, and GlazedDoor).
    """
    internal_name = "WindowProperty:ShadingControl"
    field_count = 12
    required_fields = ["Name", "Shading Type", "Shading Control Type"]
    extensible_fields = 0
    format = None
    min_fields = 11
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `WindowProperty:ShadingControl`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Shading Type"] = None
        self._data["Construction with Shading Name"] = None
        self._data["Shading Control Type"] = None
        self._data["Schedule Name"] = None
        self._data["Setpoint"] = None
        self._data["Shading Control Is Scheduled"] = None
        self._data["Glare Control Is Active"] = None
        self._data["Shading Device Material Name"] = None
        self._data["Type of Slat Angle Control for Blinds"] = None
        self._data["Slat Angle Schedule Name"] = None
        self._data["Setpoint 2"] = None
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
            self.shading_type = None
        else:
            self.shading_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.construction_with_shading_name = None
        else:
            self.construction_with_shading_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shading_control_type = None
        else:
            self.shading_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint = None
        else:
            self.setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shading_control_is_scheduled = None
        else:
            self.shading_control_is_scheduled = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glare_control_is_active = None
        else:
            self.glare_control_is_active = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.shading_device_material_name = None
        else:
            self.shading_device_material_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type_of_slat_angle_control_for_blinds = None
        else:
            self.type_of_slat_angle_control_for_blinds = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.slat_angle_schedule_name = None
        else:
            self.slat_angle_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.setpoint_2 = None
        else:
            self.setpoint_2 = vals[i]
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
        Referenced by surfaces that are exterior windows
        Not used by interzone windows

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
                                 ' for field `WindowPropertyShadingControl.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.name`')
        self._data["Name"] = value

    @property
    def shading_type(self):
        """Get shading_type

        Returns:
            str: the value of `shading_type` or None if not set
        """
        return self._data["Shading Type"]

    @shading_type.setter
    def shading_type(self, value=None):
        """  Corresponds to IDD Field `Shading Type`

        Args:
            value (str): value for IDD Field `Shading Type`
                Accepted values are:
                      - InteriorShade
                      - ExteriorShade
                      - ExteriorScreen
                      - InteriorBlind
                      - ExteriorBlind
                      - BetweenGlassShade
                      - BetweenGlassBlind
                      - SwitchableGlazing
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
                                 ' for field `WindowPropertyShadingControl.shading_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.shading_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.shading_type`')
            vals = {}
            vals["interiorshade"] = "InteriorShade"
            vals["exteriorshade"] = "ExteriorShade"
            vals["exteriorscreen"] = "ExteriorScreen"
            vals["interiorblind"] = "InteriorBlind"
            vals["exteriorblind"] = "ExteriorBlind"
            vals["betweenglassshade"] = "BetweenGlassShade"
            vals["betweenglassblind"] = "BetweenGlassBlind"
            vals["switchableglazing"] = "SwitchableGlazing"
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
                                     'field `WindowPropertyShadingControl.shading_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyShadingControl.shading_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Shading Type"] = value

    @property
    def construction_with_shading_name(self):
        """Get construction_with_shading_name

        Returns:
            str: the value of `construction_with_shading_name` or None if not set
        """
        return self._data["Construction with Shading Name"]

    @construction_with_shading_name.setter
    def construction_with_shading_name(self, value=None):
        """  Corresponds to IDD Field `Construction with Shading Name`
        Required if Shading Type = SwitchableGlazing
        Required if Shading Type = interior or exterior shade or blind, or exterior screen, and
        "Shading Device Material Name" is not specified.
        If both "Construction with Shading Name" and "Shading Device Material Name" are entered,
        the former takes precedence.

        Args:
            value (str): value for IDD Field `Construction with Shading Name`
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
                                 ' for field `WindowPropertyShadingControl.construction_with_shading_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.construction_with_shading_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.construction_with_shading_name`')
        self._data["Construction with Shading Name"] = value

    @property
    def shading_control_type(self):
        """Get shading_control_type

        Returns:
            str: the value of `shading_control_type` or None if not set
        """
        return self._data["Shading Control Type"]

    @shading_control_type.setter
    def shading_control_type(self, value=None):
        """  Corresponds to IDD Field `Shading Control Type`
        OnIfScheduleAllows requires that Schedule Name be specified and
        Shading Control Is Scheduled = Yes.
        AlwaysOn, AlwaysOff and OnIfScheduleAllows are the only valid control types for ExteriorScreen.
        The following six control types are used primarily to reduce
        zone cooling load due to window solar gain
        Following entry should be used only if Shading Type = SwitchableGlazing
        and window is in a daylit zone
        The following three control types are used to reduce zone Heating load. They can be
        used with any Shading Type but are most appropriate for opaque interior or exterior
        shades with high insulating value ("opaque movable insulation")
        The following two control types are used to reduce zone heating and cooling load.
        They can be used with any Shading Type but are most appropriate for translucent interior
        or exterior shades with high insulating value ("translucent movable insulation")
        The following two control types are used to reduce zone Cooling load.
        They can be used with any Shading Type but are most appropriate for interior
        or exterior blinds,interior or exterior shades with low insulating value, or
        switchable glazing
        The following four control types require that both Setpoint and Setpoint2 be specified
        Setpoint will correspond to outdoor air temp or zone air temp (deg C)
        Setpoint2 will correspond to solar on window or horizontal solar (W/m2)

        Args:
            value (str): value for IDD Field `Shading Control Type`
                Accepted values are:
                      - AlwaysOn
                      - AlwaysOff
                      - OnIfScheduleAllows
                      - OnIfHighSolarOnWindow
                      - OnIfHighHorizontalSolar
                      - OnIfHighOutdoorAirTemperature
                      - OnIfHighZoneAirTemperature
                      - OnIfHighZoneCooling
                      - OnIfHighGlare
                      - MeetDaylightIlluminanceSetpoint
                      - OnNightIfLowOutdoorTempAndOffDay
                      - OnNightIfLowInsideTempAndOffDay
                      - OnNightIfHeatingAndOffDay
                      - OnNightIfLowOutdoorTempAndOnDayIfCooling
                      - OnNightIfHeatingAndOnDayIfCooling
                      - OffNightAndOnDayIfCoolingAndHighSolarOnWindow
                      - OnNightAndOnDayIfCoolingAndHighSolarOnWindow
                      - OnIfHighOutdoorAirTempAndHighSolarOnWindow
                      - OnIfHighOutdoorAirTempAndHighHorizontalSolar
                      - OnIfHighZoneAirTempAndHighSolarOnWindow
                      - OnIfHighZoneAirTempAndHighHorizontalSolar
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
                                 ' for field `WindowPropertyShadingControl.shading_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.shading_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.shading_control_type`')
            vals = {}
            vals["alwayson"] = "AlwaysOn"
            vals["alwaysoff"] = "AlwaysOff"
            vals["onifscheduleallows"] = "OnIfScheduleAllows"
            vals["onifhighsolaronwindow"] = "OnIfHighSolarOnWindow"
            vals["onifhighhorizontalsolar"] = "OnIfHighHorizontalSolar"
            vals["onifhighoutdoorairtemperature"] = "OnIfHighOutdoorAirTemperature"
            vals["onifhighzoneairtemperature"] = "OnIfHighZoneAirTemperature"
            vals["onifhighzonecooling"] = "OnIfHighZoneCooling"
            vals["onifhighglare"] = "OnIfHighGlare"
            vals["meetdaylightilluminancesetpoint"] = "MeetDaylightIlluminanceSetpoint"
            vals["onnightiflowoutdoortempandoffday"] = "OnNightIfLowOutdoorTempAndOffDay"
            vals["onnightiflowinsidetempandoffday"] = "OnNightIfLowInsideTempAndOffDay"
            vals["onnightifheatingandoffday"] = "OnNightIfHeatingAndOffDay"
            vals["onnightiflowoutdoortempandondayifcooling"] = "OnNightIfLowOutdoorTempAndOnDayIfCooling"
            vals["onnightifheatingandondayifcooling"] = "OnNightIfHeatingAndOnDayIfCooling"
            vals["offnightandondayifcoolingandhighsolaronwindow"] = "OffNightAndOnDayIfCoolingAndHighSolarOnWindow"
            vals["onnightandondayifcoolingandhighsolaronwindow"] = "OnNightAndOnDayIfCoolingAndHighSolarOnWindow"
            vals["onifhighoutdoorairtempandhighsolaronwindow"] = "OnIfHighOutdoorAirTempAndHighSolarOnWindow"
            vals["onifhighoutdoorairtempandhighhorizontalsolar"] = "OnIfHighOutdoorAirTempAndHighHorizontalSolar"
            vals["onifhighzoneairtempandhighsolaronwindow"] = "OnIfHighZoneAirTempAndHighSolarOnWindow"
            vals["onifhighzoneairtempandhighhorizontalsolar"] = "OnIfHighZoneAirTempAndHighHorizontalSolar"
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
                                     'field `WindowPropertyShadingControl.shading_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyShadingControl.shading_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Shading Control Type"] = value

    @property
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `Schedule Name`
        Required if Shading Control Is Scheduled = Yes.
        If schedule value = 1, shading control is active, i.e., shading can take place only
        if the control test passes. If schedule value = 0, shading is off whether or not
        the control test passes. Schedule Name is required if Shading Control Is Scheduled = Yes.
        If Schedule Name is not specified, shading control is assumed to be active at all times.

        Args:
            value (str): value for IDD Field `Schedule Name`
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
                                 ' for field `WindowPropertyShadingControl.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def setpoint(self):
        """Get setpoint

        Returns:
            float: the value of `setpoint` or None if not set
        """
        return self._data["Setpoint"]

    @setpoint.setter
    def setpoint(self, value=None):
        """  Corresponds to IDD Field `Setpoint`
        W/m2 for solar-based controls, W for cooling- or heating-based controls,
        deg C for temperature-based controls.
        Unused for Shading Control Type = AlwaysOn, AlwaysOff, OnIfScheduleAllows,
        OnIfHighGlare, Glare, and DaylightIlluminance

        Args:
            value (float): value for IDD Field `Setpoint`
                Units: W/m2, W or deg C
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
                                 ' for field `WindowPropertyShadingControl.setpoint`'.format(value))
        self._data["Setpoint"] = value

    @property
    def shading_control_is_scheduled(self):
        """Get shading_control_is_scheduled

        Returns:
            str: the value of `shading_control_is_scheduled` or None if not set
        """
        return self._data["Shading Control Is Scheduled"]

    @shading_control_is_scheduled.setter
    def shading_control_is_scheduled(self, value="No"):
        """  Corresponds to IDD Field `Shading Control Is Scheduled`
        If Yes, Schedule Name is required; if No, Schedule Name is not used.
        Shading Control Is Scheduled = Yes is required if Shading Control Type = OnIfScheduleAllows.

        Args:
            value (str): value for IDD Field `Shading Control Is Scheduled`
                Accepted values are:
                      - No
                      - Yes
                Default value: No
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
                                 ' for field `WindowPropertyShadingControl.shading_control_is_scheduled`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.shading_control_is_scheduled`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.shading_control_is_scheduled`')
            vals = {}
            vals["no"] = "No"
            vals["yes"] = "Yes"
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
                                     'field `WindowPropertyShadingControl.shading_control_is_scheduled`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyShadingControl.shading_control_is_scheduled`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Shading Control Is Scheduled"] = value

    @property
    def glare_control_is_active(self):
        """Get glare_control_is_active

        Returns:
            str: the value of `glare_control_is_active` or None if not set
        """
        return self._data["Glare Control Is Active"]

    @glare_control_is_active.setter
    def glare_control_is_active(self, value="No"):
        """  Corresponds to IDD Field `Glare Control Is Active`
        If Yes and window is in a daylit zone, shading is on if zone's discomfort glare index exceeds
        the maximum discomfort glare index specified in the Daylighting object referenced by the zone.
        The glare test is OR'ed with the test specified by Shading Control Type.
        Glare Control Is Active = Yes is required if Shading Control Type = OnIfHighGlare.

        Args:
            value (str): value for IDD Field `Glare Control Is Active`
                Accepted values are:
                      - No
                      - Yes
                Default value: No
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
                                 ' for field `WindowPropertyShadingControl.glare_control_is_active`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.glare_control_is_active`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.glare_control_is_active`')
            vals = {}
            vals["no"] = "No"
            vals["yes"] = "Yes"
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
                                     'field `WindowPropertyShadingControl.glare_control_is_active`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyShadingControl.glare_control_is_active`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Glare Control Is Active"] = value

    @property
    def shading_device_material_name(self):
        """Get shading_device_material_name

        Returns:
            str: the value of `shading_device_material_name` or None if not set
        """
        return self._data["Shading Device Material Name"]

    @shading_device_material_name.setter
    def shading_device_material_name(self, value=None):
        """  Corresponds to IDD Field `Shading Device Material Name`
        Enter the name of a WindowMaterial:Shade, WindowMaterial:Screen or WindowMaterial:Blind object.
        Required if "Construction with Shading Name" is not specified.
        Not used if Shading Control Type = SwitchableGlazing, BetweenGlassShade, or BetweenGlassBlind.
        If both "Construction with Shading Name" and "Shading Device Material Name" are entered,
        the former takes precedence.

        Args:
            value (str): value for IDD Field `Shading Device Material Name`
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
                                 ' for field `WindowPropertyShadingControl.shading_device_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.shading_device_material_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.shading_device_material_name`')
        self._data["Shading Device Material Name"] = value

    @property
    def type_of_slat_angle_control_for_blinds(self):
        """Get type_of_slat_angle_control_for_blinds

        Returns:
            str: the value of `type_of_slat_angle_control_for_blinds` or None if not set
        """
        return self._data["Type of Slat Angle Control for Blinds"]

    @type_of_slat_angle_control_for_blinds.setter
    def type_of_slat_angle_control_for_blinds(self, value="FixedSlatAngle"):
        """  Corresponds to IDD Field `Type of Slat Angle Control for Blinds`
        Used only if Shading Type = InteriorBlind, ExteriorBlind or BetweenGlassBlind.
        If choice is ScheduledSlatAngle then Slat Angle Schedule Name is required.

        Args:
            value (str): value for IDD Field `Type of Slat Angle Control for Blinds`
                Accepted values are:
                      - FixedSlatAngle
                      - ScheduledSlatAngle
                      - BlockBeamSolar
                Default value: FixedSlatAngle
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
                                 ' for field `WindowPropertyShadingControl.type_of_slat_angle_control_for_blinds`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.type_of_slat_angle_control_for_blinds`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.type_of_slat_angle_control_for_blinds`')
            vals = {}
            vals["fixedslatangle"] = "FixedSlatAngle"
            vals["scheduledslatangle"] = "ScheduledSlatAngle"
            vals["blockbeamsolar"] = "BlockBeamSolar"
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
                                     'field `WindowPropertyShadingControl.type_of_slat_angle_control_for_blinds`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyShadingControl.type_of_slat_angle_control_for_blinds`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Type of Slat Angle Control for Blinds"] = value

    @property
    def slat_angle_schedule_name(self):
        """Get slat_angle_schedule_name

        Returns:
            str: the value of `slat_angle_schedule_name` or None if not set
        """
        return self._data["Slat Angle Schedule Name"]

    @slat_angle_schedule_name.setter
    def slat_angle_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Slat Angle Schedule Name`
        Used only if Shading Type = InteriorBlind, ExteriorBlind or BetweenGlassBlind.
        Required if Type of Slat Angle Control for Blinds = ScheduledSlatAngle
        Schedule values should be degrees (0 minimum, 180 maximum)

        Args:
            value (str): value for IDD Field `Slat Angle Schedule Name`
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
                                 ' for field `WindowPropertyShadingControl.slat_angle_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyShadingControl.slat_angle_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyShadingControl.slat_angle_schedule_name`')
        self._data["Slat Angle Schedule Name"] = value

    @property
    def setpoint_2(self):
        """Get setpoint_2

        Returns:
            float: the value of `setpoint_2` or None if not set
        """
        return self._data["Setpoint 2"]

    @setpoint_2.setter
    def setpoint_2(self, value=None):
        """  Corresponds to IDD Field `Setpoint 2`
        W/m2 for solar-based controls, deg C for temperature-based controls.
        Used only as the second setpoint for the following two-setpoint control types:
        OnIfHighOutdoorAirTempAndHighSolarOnWindow, OnIfHighOutdoorAirTempAndHighHorizontalSolar,
        OnIfHighZoneAirTempAndHighSolarOnWindow, and OnIfHighZoneAirTempAndHighHorizontalSolar

        Args:
            value (float): value for IDD Field `Setpoint 2`
                Units: W/m2 or deg C
                IP-Units: unknown
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
                                 ' for field `WindowPropertyShadingControl.setpoint_2`'.format(value))
        self._data["Setpoint 2"] = value

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
                    raise ValueError("Required field WindowPropertyShadingControl:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WindowPropertyShadingControl:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WindowPropertyShadingControl: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WindowPropertyShadingControl: {} / {}".format(out_fields,
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

class WindowPropertyFrameAndDivider(object):
    """ Corresponds to IDD object `WindowProperty:FrameAndDivider`
        Specifies the dimensions of a window frame, dividers, and inside reveal surfaces.
        Referenced by the surface objects for exterior windows and glass doors
        (ref: FenestrationSurface:Detailed, Window, and GlazedDoor).
    """
    internal_name = "WindowProperty:FrameAndDivider"
    field_count = 25
    required_fields = ["Name", "Divider Type"]
    extensible_fields = 0
    format = None
    min_fields = 20
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `WindowProperty:FrameAndDivider`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Frame Width"] = None
        self._data["Frame Outside Projection"] = None
        self._data["Frame Inside Projection"] = None
        self._data["Frame Conductance"] = None
        self._data["Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance"] = None
        self._data["Frame Solar Absorptance"] = None
        self._data["Frame Visible Absorptance"] = None
        self._data["Frame Thermal Hemispherical Emissivity"] = None
        self._data["Divider Type"] = None
        self._data["Divider Width"] = None
        self._data["Number of Horizontal Dividers"] = None
        self._data["Number of Vertical Dividers"] = None
        self._data["Divider Outside Projection"] = None
        self._data["Divider Inside Projection"] = None
        self._data["Divider Conductance"] = None
        self._data["Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance"] = None
        self._data["Divider Solar Absorptance"] = None
        self._data["Divider Visible Absorptance"] = None
        self._data["Divider Thermal Hemispherical Emissivity"] = None
        self._data["Outside Reveal Solar Absorptance"] = None
        self._data["Inside Sill Depth"] = None
        self._data["Inside Sill Solar Absorptance"] = None
        self._data["Inside Reveal Depth"] = None
        self._data["Inside Reveal Solar Absorptance"] = None
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
            self.frame_width = None
        else:
            self.frame_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_outside_projection = None
        else:
            self.frame_outside_projection = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_inside_projection = None
        else:
            self.frame_inside_projection = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_conductance = None
        else:
            self.frame_conductance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance = None
        else:
            self.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_solar_absorptance = None
        else:
            self.frame_solar_absorptance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_visible_absorptance = None
        else:
            self.frame_visible_absorptance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.frame_thermal_hemispherical_emissivity = None
        else:
            self.frame_thermal_hemispherical_emissivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_type = None
        else:
            self.divider_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_width = None
        else:
            self.divider_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_horizontal_dividers = None
        else:
            self.number_of_horizontal_dividers = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertical_dividers = None
        else:
            self.number_of_vertical_dividers = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_outside_projection = None
        else:
            self.divider_outside_projection = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_inside_projection = None
        else:
            self.divider_inside_projection = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_conductance = None
        else:
            self.divider_conductance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance = None
        else:
            self.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_solar_absorptance = None
        else:
            self.divider_solar_absorptance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_visible_absorptance = None
        else:
            self.divider_visible_absorptance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.divider_thermal_hemispherical_emissivity = None
        else:
            self.divider_thermal_hemispherical_emissivity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_reveal_solar_absorptance = None
        else:
            self.outside_reveal_solar_absorptance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_sill_depth = None
        else:
            self.inside_sill_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_sill_solar_absorptance = None
        else:
            self.inside_sill_solar_absorptance = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_reveal_depth = None
        else:
            self.inside_reveal_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_reveal_solar_absorptance = None
        else:
            self.inside_reveal_solar_absorptance = vals[i]
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
        Referenced by surfaces that are exterior windows
        Not used by interzone windows

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
                                 ' for field `WindowPropertyFrameAndDivider.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyFrameAndDivider.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyFrameAndDivider.name`')
        self._data["Name"] = value

    @property
    def frame_width(self):
        """Get frame_width

        Returns:
            float: the value of `frame_width` or None if not set
        """
        return self._data["Frame Width"]

    @frame_width.setter
    def frame_width(self, value=0.0):
        """  Corresponds to IDD Field `Frame Width`
        Width of frame in plane of window
        Frame width assumed the same on all sides of window

        Args:
            value (float): value for IDD Field `Frame Width`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_width`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_width`')
        self._data["Frame Width"] = value

    @property
    def frame_outside_projection(self):
        """Get frame_outside_projection

        Returns:
            float: the value of `frame_outside_projection` or None if not set
        """
        return self._data["Frame Outside Projection"]

    @frame_outside_projection.setter
    def frame_outside_projection(self, value=0.0):
        """  Corresponds to IDD Field `Frame Outside Projection`
        Amount that frame projects outward from the outside face of the glazing

        Args:
            value (float): value for IDD Field `Frame Outside Projection`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 0.5
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_outside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_outside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `WindowPropertyFrameAndDivider.frame_outside_projection`')
        self._data["Frame Outside Projection"] = value

    @property
    def frame_inside_projection(self):
        """Get frame_inside_projection

        Returns:
            float: the value of `frame_inside_projection` or None if not set
        """
        return self._data["Frame Inside Projection"]

    @frame_inside_projection.setter
    def frame_inside_projection(self, value=0.0):
        """  Corresponds to IDD Field `Frame Inside Projection`
        Amount that frame projects inward from the inside face of the glazing

        Args:
            value (float): value for IDD Field `Frame Inside Projection`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 0.5
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_inside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_inside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `WindowPropertyFrameAndDivider.frame_inside_projection`')
        self._data["Frame Inside Projection"] = value

    @property
    def frame_conductance(self):
        """Get frame_conductance

        Returns:
            float: the value of `frame_conductance` or None if not set
        """
        return self._data["Frame Conductance"]

    @frame_conductance.setter
    def frame_conductance(self, value=None):
        """  Corresponds to IDD Field `Frame Conductance`
        Effective conductance of frame
        Excludes air films
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `Frame Conductance`
                Units: W/m2-K
                value >= 0.0
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_conductance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_conductance`')
        self._data["Frame Conductance"] = value

    @property
    def ratio_of_frameedge_glass_conductance_to_centerofglass_conductance(self):
        """Get ratio_of_frameedge_glass_conductance_to_centerofglass_conductance

        Returns:
            float: the value of `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance` or None if not set
        """
        return self._data["Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance"]

    @ratio_of_frameedge_glass_conductance_to_centerofglass_conductance.setter
    def ratio_of_frameedge_glass_conductance_to_centerofglass_conductance(self, value=1.0):
        """  Corresponds to IDD Field `Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance`
        Excludes air films; applies only to multipane windows
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance`
                Default value: 1.0
                value > 0.0
                value <= 4.0
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
                                 ' for field `WindowPropertyFrameAndDivider.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `WindowPropertyFrameAndDivider.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`')
        self._data["Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance"] = value

    @property
    def frame_solar_absorptance(self):
        """Get frame_solar_absorptance

        Returns:
            float: the value of `frame_solar_absorptance` or None if not set
        """
        return self._data["Frame Solar Absorptance"]

    @frame_solar_absorptance.setter
    def frame_solar_absorptance(self, value=0.7):
        """  Corresponds to IDD Field `Frame Solar Absorptance`
        Assumed same on outside and inside of frame

        Args:
            value (float): value for IDD Field `Frame Solar Absorptance`
                Default value: 0.7
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_solar_absorptance`')
        self._data["Frame Solar Absorptance"] = value

    @property
    def frame_visible_absorptance(self):
        """Get frame_visible_absorptance

        Returns:
            float: the value of `frame_visible_absorptance` or None if not set
        """
        return self._data["Frame Visible Absorptance"]

    @frame_visible_absorptance.setter
    def frame_visible_absorptance(self, value=0.7):
        """  Corresponds to IDD Field `Frame Visible Absorptance`
        Assumed same on outside and inside of frame

        Args:
            value (float): value for IDD Field `Frame Visible Absorptance`
                Default value: 0.7
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_visible_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_visible_absorptance`')
        self._data["Frame Visible Absorptance"] = value

    @property
    def frame_thermal_hemispherical_emissivity(self):
        """Get frame_thermal_hemispherical_emissivity

        Returns:
            float: the value of `frame_thermal_hemispherical_emissivity` or None if not set
        """
        return self._data["Frame Thermal Hemispherical Emissivity"]

    @frame_thermal_hemispherical_emissivity.setter
    def frame_thermal_hemispherical_emissivity(self, value=0.9):
        """  Corresponds to IDD Field `Frame Thermal Hemispherical Emissivity`
        Assumed same on outside and inside of frame

        Args:
            value (float): value for IDD Field `Frame Thermal Hemispherical Emissivity`
                Default value: 0.9
                value > 0.0
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
                                 ' for field `WindowPropertyFrameAndDivider.frame_thermal_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.frame_thermal_hemispherical_emissivity`')
        self._data["Frame Thermal Hemispherical Emissivity"] = value

    @property
    def divider_type(self):
        """Get divider_type

        Returns:
            str: the value of `divider_type` or None if not set
        """
        return self._data["Divider Type"]

    @divider_type.setter
    def divider_type(self, value="DividedLite"):
        """  Corresponds to IDD Field `Divider Type`

        Args:
            value (str): value for IDD Field `Divider Type`
                Accepted values are:
                      - DividedLite
                      - Suspended
                Default value: DividedLite
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyFrameAndDivider.divider_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyFrameAndDivider.divider_type`')
            vals = {}
            vals["dividedlite"] = "DividedLite"
            vals["suspended"] = "Suspended"
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
                                     'field `WindowPropertyFrameAndDivider.divider_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyFrameAndDivider.divider_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Divider Type"] = value

    @property
    def divider_width(self):
        """Get divider_width

        Returns:
            float: the value of `divider_width` or None if not set
        """
        return self._data["Divider Width"]

    @divider_width.setter
    def divider_width(self, value=0.0):
        """  Corresponds to IDD Field `Divider Width`
        Width of dividers in plane of window
        Width assumed the same for all dividers

        Args:
            value (float): value for IDD Field `Divider Width`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 0.5
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_width`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `WindowPropertyFrameAndDivider.divider_width`')
        self._data["Divider Width"] = value

    @property
    def number_of_horizontal_dividers(self):
        """Get number_of_horizontal_dividers

        Returns:
            float: the value of `number_of_horizontal_dividers` or None if not set
        """
        return self._data["Number of Horizontal Dividers"]

    @number_of_horizontal_dividers.setter
    def number_of_horizontal_dividers(self, value=0.0):
        """  Corresponds to IDD Field `Number of Horizontal Dividers`
        "Horizontal" means parallel to local window X-axis

        Args:
            value (float): value for IDD Field `Number of Horizontal Dividers`
                Default value: 0.0
                value >= 0.0
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
                                 ' for field `WindowPropertyFrameAndDivider.number_of_horizontal_dividers`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.number_of_horizontal_dividers`')
        self._data["Number of Horizontal Dividers"] = value

    @property
    def number_of_vertical_dividers(self):
        """Get number_of_vertical_dividers

        Returns:
            float: the value of `number_of_vertical_dividers` or None if not set
        """
        return self._data["Number of Vertical Dividers"]

    @number_of_vertical_dividers.setter
    def number_of_vertical_dividers(self, value=0.0):
        """  Corresponds to IDD Field `Number of Vertical Dividers`
        "Vertical" means parallel to local window Y-axis

        Args:
            value (float): value for IDD Field `Number of Vertical Dividers`
                Default value: 0.0
                value >= 0.0
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
                                 ' for field `WindowPropertyFrameAndDivider.number_of_vertical_dividers`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.number_of_vertical_dividers`')
        self._data["Number of Vertical Dividers"] = value

    @property
    def divider_outside_projection(self):
        """Get divider_outside_projection

        Returns:
            float: the value of `divider_outside_projection` or None if not set
        """
        return self._data["Divider Outside Projection"]

    @divider_outside_projection.setter
    def divider_outside_projection(self, value=0.0):
        """  Corresponds to IDD Field `Divider Outside Projection`
        Amount that divider projects outward from the outside face of the glazing
        Outside projection assumed the same for all divider elements

        Args:
            value (float): value for IDD Field `Divider Outside Projection`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 0.5
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_outside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_outside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `WindowPropertyFrameAndDivider.divider_outside_projection`')
        self._data["Divider Outside Projection"] = value

    @property
    def divider_inside_projection(self):
        """Get divider_inside_projection

        Returns:
            float: the value of `divider_inside_projection` or None if not set
        """
        return self._data["Divider Inside Projection"]

    @divider_inside_projection.setter
    def divider_inside_projection(self, value=0.0):
        """  Corresponds to IDD Field `Divider Inside Projection`
        Amount that divider projects inward from the inside face of the glazing
        Inside projection assumed the same for all divider elements

        Args:
            value (float): value for IDD Field `Divider Inside Projection`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 0.5
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_inside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_inside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `WindowPropertyFrameAndDivider.divider_inside_projection`')
        self._data["Divider Inside Projection"] = value

    @property
    def divider_conductance(self):
        """Get divider_conductance

        Returns:
            float: the value of `divider_conductance` or None if not set
        """
        return self._data["Divider Conductance"]

    @divider_conductance.setter
    def divider_conductance(self, value=0.0):
        """  Corresponds to IDD Field `Divider Conductance`
        Effective conductance of divider
        Excludes air films
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `Divider Conductance`
                Units: W/m2-K
                Default value: 0.0
                value >= 0.0
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_conductance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_conductance`')
        self._data["Divider Conductance"] = value

    @property
    def ratio_of_divideredge_glass_conductance_to_centerofglass_conductance(self):
        """Get ratio_of_divideredge_glass_conductance_to_centerofglass_conductance

        Returns:
            float: the value of `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance` or None if not set
        """
        return self._data["Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance"]

    @ratio_of_divideredge_glass_conductance_to_centerofglass_conductance.setter
    def ratio_of_divideredge_glass_conductance_to_centerofglass_conductance(self, value=1.0):
        """  Corresponds to IDD Field `Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance`
        Excludes air films
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance`
                Default value: 1.0
                value > 0.0
                value <= 4.0
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
                                 ' for field `WindowPropertyFrameAndDivider.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `WindowPropertyFrameAndDivider.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`')
        self._data["Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance"] = value

    @property
    def divider_solar_absorptance(self):
        """Get divider_solar_absorptance

        Returns:
            float: the value of `divider_solar_absorptance` or None if not set
        """
        return self._data["Divider Solar Absorptance"]

    @divider_solar_absorptance.setter
    def divider_solar_absorptance(self, value=0.0):
        """  Corresponds to IDD Field `Divider Solar Absorptance`
        Assumed same on outside and inside of divider

        Args:
            value (float): value for IDD Field `Divider Solar Absorptance`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_solar_absorptance`')
        self._data["Divider Solar Absorptance"] = value

    @property
    def divider_visible_absorptance(self):
        """Get divider_visible_absorptance

        Returns:
            float: the value of `divider_visible_absorptance` or None if not set
        """
        return self._data["Divider Visible Absorptance"]

    @divider_visible_absorptance.setter
    def divider_visible_absorptance(self, value=0.0):
        """  Corresponds to IDD Field `Divider Visible Absorptance`
        Assumed same on outside and inside of divider

        Args:
            value (float): value for IDD Field `Divider Visible Absorptance`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_visible_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_visible_absorptance`')
        self._data["Divider Visible Absorptance"] = value

    @property
    def divider_thermal_hemispherical_emissivity(self):
        """Get divider_thermal_hemispherical_emissivity

        Returns:
            float: the value of `divider_thermal_hemispherical_emissivity` or None if not set
        """
        return self._data["Divider Thermal Hemispherical Emissivity"]

    @divider_thermal_hemispherical_emissivity.setter
    def divider_thermal_hemispherical_emissivity(self, value=0.9):
        """  Corresponds to IDD Field `Divider Thermal Hemispherical Emissivity`
        Assumed same on outside and inside of divider

        Args:
            value (float): value for IDD Field `Divider Thermal Hemispherical Emissivity`
                Default value: 0.9
                value > 0.0
                value < 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.divider_thermal_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_thermal_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.divider_thermal_hemispherical_emissivity`')
        self._data["Divider Thermal Hemispherical Emissivity"] = value

    @property
    def outside_reveal_solar_absorptance(self):
        """Get outside_reveal_solar_absorptance

        Returns:
            float: the value of `outside_reveal_solar_absorptance` or None if not set
        """
        return self._data["Outside Reveal Solar Absorptance"]

    @outside_reveal_solar_absorptance.setter
    def outside_reveal_solar_absorptance(self, value=0.0):
        """  Corresponds to IDD Field `Outside Reveal Solar Absorptance`

        Args:
            value (float): value for IDD Field `Outside Reveal Solar Absorptance`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.outside_reveal_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.outside_reveal_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.outside_reveal_solar_absorptance`')
        self._data["Outside Reveal Solar Absorptance"] = value

    @property
    def inside_sill_depth(self):
        """Get inside_sill_depth

        Returns:
            float: the value of `inside_sill_depth` or None if not set
        """
        return self._data["Inside Sill Depth"]

    @inside_sill_depth.setter
    def inside_sill_depth(self, value=0.0):
        """  Corresponds to IDD Field `Inside Sill Depth`

        Args:
            value (float): value for IDD Field `Inside Sill Depth`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 2.0
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
                                 ' for field `WindowPropertyFrameAndDivider.inside_sill_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_sill_depth`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_sill_depth`')
        self._data["Inside Sill Depth"] = value

    @property
    def inside_sill_solar_absorptance(self):
        """Get inside_sill_solar_absorptance

        Returns:
            float: the value of `inside_sill_solar_absorptance` or None if not set
        """
        return self._data["Inside Sill Solar Absorptance"]

    @inside_sill_solar_absorptance.setter
    def inside_sill_solar_absorptance(self, value=0.0):
        """  Corresponds to IDD Field `Inside Sill Solar Absorptance`

        Args:
            value (float): value for IDD Field `Inside Sill Solar Absorptance`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.inside_sill_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_sill_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_sill_solar_absorptance`')
        self._data["Inside Sill Solar Absorptance"] = value

    @property
    def inside_reveal_depth(self):
        """Get inside_reveal_depth

        Returns:
            float: the value of `inside_reveal_depth` or None if not set
        """
        return self._data["Inside Reveal Depth"]

    @inside_reveal_depth.setter
    def inside_reveal_depth(self, value=0.0):
        """  Corresponds to IDD Field `Inside Reveal Depth`
        Distance from plane of inside surface of glazing
        to plane of inside surface of wall.
        Outside reveal depth is determined from the geometry
        of the window and the wall it is on; it is non-zero if the plane of
        the outside surface of the glazing is set back from the plane of the
        outside surface of the wall.

        Args:
            value (float): value for IDD Field `Inside Reveal Depth`
                Units: m
                Default value: 0.0
                value >= 0.0
                value <= 2.0
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
                                 ' for field `WindowPropertyFrameAndDivider.inside_reveal_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_reveal_depth`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_reveal_depth`')
        self._data["Inside Reveal Depth"] = value

    @property
    def inside_reveal_solar_absorptance(self):
        """Get inside_reveal_solar_absorptance

        Returns:
            float: the value of `inside_reveal_solar_absorptance` or None if not set
        """
        return self._data["Inside Reveal Solar Absorptance"]

    @inside_reveal_solar_absorptance.setter
    def inside_reveal_solar_absorptance(self, value=0.0):
        """  Corresponds to IDD Field `Inside Reveal Solar Absorptance`

        Args:
            value (float): value for IDD Field `Inside Reveal Solar Absorptance`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `WindowPropertyFrameAndDivider.inside_reveal_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_reveal_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `WindowPropertyFrameAndDivider.inside_reveal_solar_absorptance`')
        self._data["Inside Reveal Solar Absorptance"] = value

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
                    raise ValueError("Required field WindowPropertyFrameAndDivider:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WindowPropertyFrameAndDivider:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WindowPropertyFrameAndDivider: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WindowPropertyFrameAndDivider: {} / {}".format(out_fields,
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

class WindowPropertyAirflowControl(object):
    """ Corresponds to IDD object `WindowProperty:AirflowControl`
        Used to control forced airflow through a gap between glass layers
    """
    internal_name = "WindowProperty:AirflowControl"
    field_count = 7
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 7
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `WindowProperty:AirflowControl`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Airflow Source"] = None
        self._data["Airflow Destination"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Airflow Control Type"] = None
        self._data["Airflow Is Scheduled"] = None
        self._data["Airflow Multiplier Schedule Name"] = None
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
            self.airflow_source = None
        else:
            self.airflow_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airflow_destination = None
        else:
            self.airflow_destination = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airflow_control_type = None
        else:
            self.airflow_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airflow_is_scheduled = None
        else:
            self.airflow_is_scheduled = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airflow_multiplier_schedule_name = None
        else:
            self.airflow_multiplier_schedule_name = vals[i]
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
        Name must be that of an exterior window with two or three glass layers.

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
                                 ' for field `WindowPropertyAirflowControl.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyAirflowControl.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyAirflowControl.name`')
        self._data["Name"] = value

    @property
    def airflow_source(self):
        """Get airflow_source

        Returns:
            str: the value of `airflow_source` or None if not set
        """
        return self._data["Airflow Source"]

    @airflow_source.setter
    def airflow_source(self, value="IndoorAir"):
        """  Corresponds to IDD Field `Airflow Source`

        Args:
            value (str): value for IDD Field `Airflow Source`
                Accepted values are:
                      - IndoorAir
                      - OutdoorAir
                Default value: IndoorAir
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
                                 ' for field `WindowPropertyAirflowControl.airflow_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyAirflowControl.airflow_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyAirflowControl.airflow_source`')
            vals = {}
            vals["indoorair"] = "IndoorAir"
            vals["outdoorair"] = "OutdoorAir"
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
                                     'field `WindowPropertyAirflowControl.airflow_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyAirflowControl.airflow_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Airflow Source"] = value

    @property
    def airflow_destination(self):
        """Get airflow_destination

        Returns:
            str: the value of `airflow_destination` or None if not set
        """
        return self._data["Airflow Destination"]

    @airflow_destination.setter
    def airflow_destination(self, value="OutdoorAir"):
        """  Corresponds to IDD Field `Airflow Destination`

        Args:
            value (str): value for IDD Field `Airflow Destination`
                Accepted values are:
                      - IndoorAir
                      - OutdoorAir
                      - ReturnAir
                Default value: OutdoorAir
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
                                 ' for field `WindowPropertyAirflowControl.airflow_destination`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyAirflowControl.airflow_destination`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyAirflowControl.airflow_destination`')
            vals = {}
            vals["indoorair"] = "IndoorAir"
            vals["outdoorair"] = "OutdoorAir"
            vals["returnair"] = "ReturnAir"
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
                                     'field `WindowPropertyAirflowControl.airflow_destination`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyAirflowControl.airflow_destination`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Airflow Destination"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Maximum Flow Rate`
        Above is m3/s per m of glazing width

        Args:
            value (float): value for IDD Field `Maximum Flow Rate`
                Units: m3/s-m
                IP-Units: ft3/min-ft
                Default value: 0.0
                value >= 0.0
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
                                 ' for field `WindowPropertyAirflowControl.maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `WindowPropertyAirflowControl.maximum_flow_rate`')
        self._data["Maximum Flow Rate"] = value

    @property
    def airflow_control_type(self):
        """Get airflow_control_type

        Returns:
            str: the value of `airflow_control_type` or None if not set
        """
        return self._data["Airflow Control Type"]

    @airflow_control_type.setter
    def airflow_control_type(self, value="AlwaysOnAtMaximumFlow"):
        """  Corresponds to IDD Field `Airflow Control Type`
        ScheduledOnly requires that Airflow Has Multiplier Schedule Name = Yes
        and that Airflow Multiplier Schedule Name is specified.

        Args:
            value (str): value for IDD Field `Airflow Control Type`
                Accepted values are:
                      - AlwaysOnAtMaximumFlow
                      - AlwaysOff
                      - ScheduledOnly
                Default value: AlwaysOnAtMaximumFlow
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
                                 ' for field `WindowPropertyAirflowControl.airflow_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyAirflowControl.airflow_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyAirflowControl.airflow_control_type`')
            vals = {}
            vals["alwaysonatmaximumflow"] = "AlwaysOnAtMaximumFlow"
            vals["alwaysoff"] = "AlwaysOff"
            vals["scheduledonly"] = "ScheduledOnly"
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
                                     'field `WindowPropertyAirflowControl.airflow_control_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyAirflowControl.airflow_control_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Airflow Control Type"] = value

    @property
    def airflow_is_scheduled(self):
        """Get airflow_is_scheduled

        Returns:
            str: the value of `airflow_is_scheduled` or None if not set
        """
        return self._data["Airflow Is Scheduled"]

    @airflow_is_scheduled.setter
    def airflow_is_scheduled(self, value="No"):
        """  Corresponds to IDD Field `Airflow Is Scheduled`
        If Yes, then Airflow Multiplier Schedule Name must be specified

        Args:
            value (str): value for IDD Field `Airflow Is Scheduled`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 ' for field `WindowPropertyAirflowControl.airflow_is_scheduled`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyAirflowControl.airflow_is_scheduled`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyAirflowControl.airflow_is_scheduled`')
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
                                     'field `WindowPropertyAirflowControl.airflow_is_scheduled`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `WindowPropertyAirflowControl.airflow_is_scheduled`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Airflow Is Scheduled"] = value

    @property
    def airflow_multiplier_schedule_name(self):
        """Get airflow_multiplier_schedule_name

        Returns:
            str: the value of `airflow_multiplier_schedule_name` or None if not set
        """
        return self._data["Airflow Multiplier Schedule Name"]

    @airflow_multiplier_schedule_name.setter
    def airflow_multiplier_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Airflow Multiplier Schedule Name`
        Required if Airflow Is Scheduled = Yes.
        Schedule values are 0.0 or 1.0 and multiply Maximum Air Flow.

        Args:
            value (str): value for IDD Field `Airflow Multiplier Schedule Name`
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
                                 ' for field `WindowPropertyAirflowControl.airflow_multiplier_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyAirflowControl.airflow_multiplier_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyAirflowControl.airflow_multiplier_schedule_name`')
        self._data["Airflow Multiplier Schedule Name"] = value

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
                    raise ValueError("Required field WindowPropertyAirflowControl:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WindowPropertyAirflowControl:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WindowPropertyAirflowControl: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WindowPropertyAirflowControl: {} / {}".format(out_fields,
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

class WindowPropertyStormWindow(object):
    """ Corresponds to IDD object `WindowProperty:StormWindow`
        This is a movable exterior glass layer that is usually applied in the winter
        and removed in the summer.
    """
    internal_name = "WindowProperty:StormWindow"
    field_count = 7
    required_fields = ["Window Name", "Storm Glass Layer Name", "Month that Storm Glass Layer is Put On", "Day of Month that Storm Glass Layer is Put On", "Month that Storm Glass Layer is Taken Off", "Day of Month that Storm Glass Layer is Taken Off"]
    extensible_fields = 0
    format = None
    min_fields = 7
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `WindowProperty:StormWindow`
        """
        self._data = OrderedDict()
        self._data["Window Name"] = None
        self._data["Storm Glass Layer Name"] = None
        self._data["Distance Between Storm Glass Layer and Adjacent Glass"] = None
        self._data["Month that Storm Glass Layer is Put On"] = None
        self._data["Day of Month that Storm Glass Layer is Put On"] = None
        self._data["Month that Storm Glass Layer is Taken Off"] = None
        self._data["Day of Month that Storm Glass Layer is Taken Off"] = None
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
            self.window_name = None
        else:
            self.window_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.storm_glass_layer_name = None
        else:
            self.storm_glass_layer_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.distance_between_storm_glass_layer_and_adjacent_glass = None
        else:
            self.distance_between_storm_glass_layer_and_adjacent_glass = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.month_that_storm_glass_layer_is_put_on = None
        else:
            self.month_that_storm_glass_layer_is_put_on = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_month_that_storm_glass_layer_is_put_on = None
        else:
            self.day_of_month_that_storm_glass_layer_is_put_on = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.month_that_storm_glass_layer_is_taken_off = None
        else:
            self.month_that_storm_glass_layer_is_taken_off = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.day_of_month_that_storm_glass_layer_is_taken_off = None
        else:
            self.day_of_month_that_storm_glass_layer_is_taken_off = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def window_name(self):
        """Get window_name

        Returns:
            str: the value of `window_name` or None if not set
        """
        return self._data["Window Name"]

    @window_name.setter
    def window_name(self, value=None):
        """  Corresponds to IDD Field `Window Name`
        Must be the name of a FenestrationSurface:Detailed object with Surface Type = WINDOW.
        The WindowProperty:StormWindow object can only be used with exterior windows.

        Args:
            value (str): value for IDD Field `Window Name`
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
                                 ' for field `WindowPropertyStormWindow.window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyStormWindow.window_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyStormWindow.window_name`')
        self._data["Window Name"] = value

    @property
    def storm_glass_layer_name(self):
        """Get storm_glass_layer_name

        Returns:
            str: the value of `storm_glass_layer_name` or None if not set
        """
        return self._data["Storm Glass Layer Name"]

    @storm_glass_layer_name.setter
    def storm_glass_layer_name(self, value=None):
        """  Corresponds to IDD Field `Storm Glass Layer Name`
        Must be a WindowMaterial:Glazing or WindowMaterial:Glazing:RefractionExtinctionMethod
        Gap between storm glass layer and adjacent glass layer is assumed to be filled
        with Air

        Args:
            value (str): value for IDD Field `Storm Glass Layer Name`
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
                                 ' for field `WindowPropertyStormWindow.storm_glass_layer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `WindowPropertyStormWindow.storm_glass_layer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `WindowPropertyStormWindow.storm_glass_layer_name`')
        self._data["Storm Glass Layer Name"] = value

    @property
    def distance_between_storm_glass_layer_and_adjacent_glass(self):
        """Get distance_between_storm_glass_layer_and_adjacent_glass

        Returns:
            float: the value of `distance_between_storm_glass_layer_and_adjacent_glass` or None if not set
        """
        return self._data["Distance Between Storm Glass Layer and Adjacent Glass"]

    @distance_between_storm_glass_layer_and_adjacent_glass.setter
    def distance_between_storm_glass_layer_and_adjacent_glass(self, value=0.05):
        """  Corresponds to IDD Field `Distance Between Storm Glass Layer and Adjacent Glass`

        Args:
            value (float): value for IDD Field `Distance Between Storm Glass Layer and Adjacent Glass`
                Units: m
                Default value: 0.05
                value > 0.0
                value <= 0.5
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
                                 ' for field `WindowPropertyStormWindow.distance_between_storm_glass_layer_and_adjacent_glass`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `WindowPropertyStormWindow.distance_between_storm_glass_layer_and_adjacent_glass`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `WindowPropertyStormWindow.distance_between_storm_glass_layer_and_adjacent_glass`')
        self._data["Distance Between Storm Glass Layer and Adjacent Glass"] = value

    @property
    def month_that_storm_glass_layer_is_put_on(self):
        """Get month_that_storm_glass_layer_is_put_on

        Returns:
            int: the value of `month_that_storm_glass_layer_is_put_on` or None if not set
        """
        return self._data["Month that Storm Glass Layer is Put On"]

    @month_that_storm_glass_layer_is_put_on.setter
    def month_that_storm_glass_layer_is_put_on(self, value=None):
        """  Corresponds to IDD Field `Month that Storm Glass Layer is Put On`

        Args:
            value (int): value for IDD Field `Month that Storm Glass Layer is Put On`
                value >= 1
                value <= 12
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_put_on`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_put_on`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_put_on`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_put_on`')
        self._data["Month that Storm Glass Layer is Put On"] = value

    @property
    def day_of_month_that_storm_glass_layer_is_put_on(self):
        """Get day_of_month_that_storm_glass_layer_is_put_on

        Returns:
            int: the value of `day_of_month_that_storm_glass_layer_is_put_on` or None if not set
        """
        return self._data["Day of Month that Storm Glass Layer is Put On"]

    @day_of_month_that_storm_glass_layer_is_put_on.setter
    def day_of_month_that_storm_glass_layer_is_put_on(self, value=None):
        """  Corresponds to IDD Field `Day of Month that Storm Glass Layer is Put On`

        Args:
            value (int): value for IDD Field `Day of Month that Storm Glass Layer is Put On`
                value >= 1
                value <= 31
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_put_on`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_put_on`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_put_on`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_put_on`')
        self._data["Day of Month that Storm Glass Layer is Put On"] = value

    @property
    def month_that_storm_glass_layer_is_taken_off(self):
        """Get month_that_storm_glass_layer_is_taken_off

        Returns:
            int: the value of `month_that_storm_glass_layer_is_taken_off` or None if not set
        """
        return self._data["Month that Storm Glass Layer is Taken Off"]

    @month_that_storm_glass_layer_is_taken_off.setter
    def month_that_storm_glass_layer_is_taken_off(self, value=None):
        """  Corresponds to IDD Field `Month that Storm Glass Layer is Taken Off`

        Args:
            value (int): value for IDD Field `Month that Storm Glass Layer is Taken Off`
                value >= 1
                value <= 12
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_taken_off`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_taken_off`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_taken_off`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `WindowPropertyStormWindow.month_that_storm_glass_layer_is_taken_off`')
        self._data["Month that Storm Glass Layer is Taken Off"] = value

    @property
    def day_of_month_that_storm_glass_layer_is_taken_off(self):
        """Get day_of_month_that_storm_glass_layer_is_taken_off

        Returns:
            int: the value of `day_of_month_that_storm_glass_layer_is_taken_off` or None if not set
        """
        return self._data["Day of Month that Storm Glass Layer is Taken Off"]

    @day_of_month_that_storm_glass_layer_is_taken_off.setter
    def day_of_month_that_storm_glass_layer_is_taken_off(self, value=None):
        """  Corresponds to IDD Field `Day of Month that Storm Glass Layer is Taken Off`

        Args:
            value (int): value for IDD Field `Day of Month that Storm Glass Layer is Taken Off`
                value >= 1
                value <= 31
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
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_taken_off`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_taken_off`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_taken_off`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `WindowPropertyStormWindow.day_of_month_that_storm_glass_layer_is_taken_off`')
        self._data["Day of Month that Storm Glass Layer is Taken Off"] = value

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
                    raise ValueError("Required field WindowPropertyStormWindow:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field WindowPropertyStormWindow:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for WindowPropertyStormWindow: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for WindowPropertyStormWindow: {} / {}".format(out_fields,
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

class InternalMass(object):
    """ Corresponds to IDD object `InternalMass`
        Used to describe internal zone surface area that does not need to be part of geometric
        representation. This should be the total surface area exposed to the zone air.
    """
    internal_name = "InternalMass"
    field_count = 4
    required_fields = ["Name", "Construction Name", "Zone Name", "Surface Area"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `InternalMass`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Surface Area"] = None
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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_area = None
        else:
            self.surface_area = vals[i]
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
                                 ' for field `InternalMass.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `InternalMass.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `InternalMass.name`')
        self._data["Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Construction Name`
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
                                 ' for field `InternalMass.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `InternalMass.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `InternalMass.construction_name`')
        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Zone the surface is a part of
        used to be Interior Environment

        Args:
            value (str): value for IDD Field `Zone Name`
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
                                 ' for field `InternalMass.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `InternalMass.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `InternalMass.zone_name`')
        self._data["Zone Name"] = value

    @property
    def surface_area(self):
        """Get surface_area

        Returns:
            float: the value of `surface_area` or None if not set
        """
        return self._data["Surface Area"]

    @surface_area.setter
    def surface_area(self, value=None):
        """  Corresponds to IDD Field `Surface Area`

        Args:
            value (float): value for IDD Field `Surface Area`
                Units: m2
                value > 0.0
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
                                 ' for field `InternalMass.surface_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `InternalMass.surface_area`')
        self._data["Surface Area"] = value

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
                    raise ValueError("Required field InternalMass:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field InternalMass:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for InternalMass: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for InternalMass: {} / {}".format(out_fields,
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

class ShadingSite(object):
    """ Corresponds to IDD object `Shading:Site`
        used for shading elements such as trees
        these items are fixed in space and would not move with relative geometry
    """
    internal_name = "Shading:Site"
    field_count = 8
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Site`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `ShadingSite.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingSite.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingSite.name`')
        self._data["Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of shading device (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `ShadingSite.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingSite.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `ShadingSite.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle`

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingSite.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingSite.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingSite.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Starting coordinate is the Lower Left Corner of the Shade

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `ShadingSite.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `ShadingSite.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `ShadingSite.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `ShadingSite.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `ShadingSite.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field ShadingSite:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingSite:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingSite: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingSite: {} / {}".format(out_fields,
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

class ShadingBuilding(object):
    """ Corresponds to IDD object `Shading:Building`
        used for shading elements such as trees, other buildings, parts of this building not being modeled
        these items are relative to the current building and would move with relative geometry
    """
    internal_name = "Shading:Building"
    field_count = 8
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Building`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Azimuth Angle"] = None
        self._data["Tilt Angle"] = None
        self._data["Starting X Coordinate"] = None
        self._data["Starting Y Coordinate"] = None
        self._data["Starting Z Coordinate"] = None
        self._data["Length"] = None
        self._data["Height"] = None
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
            self.azimuth_angle = None
        else:
            self.azimuth_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle = None
        else:
            self.tilt_angle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_x_coordinate = None
        else:
            self.starting_x_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_y_coordinate = None
        else:
            self.starting_y_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.starting_z_coordinate = None
        else:
            self.starting_z_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.length = None
        else:
            self.length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height = None
        else:
            self.height = vals[i]
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
                                 ' for field `ShadingBuilding.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingBuilding.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingBuilding.name`')
        self._data["Name"] = value

    @property
    def azimuth_angle(self):
        """Get azimuth_angle

        Returns:
            float: the value of `azimuth_angle` or None if not set
        """
        return self._data["Azimuth Angle"]

    @azimuth_angle.setter
    def azimuth_angle(self, value=None):
        """  Corresponds to IDD Field `Azimuth Angle`
        Facing direction of outside of shading device (S=180,N=0,E=90,W=270)

        Args:
            value (float): value for IDD Field `Azimuth Angle`
                Units: deg
                value >= 0.0
                value <= 360.0
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
                                 ' for field `ShadingBuilding.azimuth_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingBuilding.azimuth_angle`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `ShadingBuilding.azimuth_angle`')
        self._data["Azimuth Angle"] = value

    @property
    def tilt_angle(self):
        """Get tilt_angle

        Returns:
            float: the value of `tilt_angle` or None if not set
        """
        return self._data["Tilt Angle"]

    @tilt_angle.setter
    def tilt_angle(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle`

        Args:
            value (float): value for IDD Field `Tilt Angle`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingBuilding.tilt_angle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingBuilding.tilt_angle`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingBuilding.tilt_angle`')
        self._data["Tilt Angle"] = value

    @property
    def starting_x_coordinate(self):
        """Get starting_x_coordinate

        Returns:
            float: the value of `starting_x_coordinate` or None if not set
        """
        return self._data["Starting X Coordinate"]

    @starting_x_coordinate.setter
    def starting_x_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting X Coordinate`
        Starting coordinate is the Lower Left Corner of the Shade

        Args:
            value (float): value for IDD Field `Starting X Coordinate`
                Units: m
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
                                 ' for field `ShadingBuilding.starting_x_coordinate`'.format(value))
        self._data["Starting X Coordinate"] = value

    @property
    def starting_y_coordinate(self):
        """Get starting_y_coordinate

        Returns:
            float: the value of `starting_y_coordinate` or None if not set
        """
        return self._data["Starting Y Coordinate"]

    @starting_y_coordinate.setter
    def starting_y_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Y Coordinate`

        Args:
            value (float): value for IDD Field `Starting Y Coordinate`
                Units: m
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
                                 ' for field `ShadingBuilding.starting_y_coordinate`'.format(value))
        self._data["Starting Y Coordinate"] = value

    @property
    def starting_z_coordinate(self):
        """Get starting_z_coordinate

        Returns:
            float: the value of `starting_z_coordinate` or None if not set
        """
        return self._data["Starting Z Coordinate"]

    @starting_z_coordinate.setter
    def starting_z_coordinate(self, value=None):
        """  Corresponds to IDD Field `Starting Z Coordinate`

        Args:
            value (float): value for IDD Field `Starting Z Coordinate`
                Units: m
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
                                 ' for field `ShadingBuilding.starting_z_coordinate`'.format(value))
        self._data["Starting Z Coordinate"] = value

    @property
    def length(self):
        """Get length

        Returns:
            float: the value of `length` or None if not set
        """
        return self._data["Length"]

    @length.setter
    def length(self, value=None):
        """  Corresponds to IDD Field `Length`

        Args:
            value (float): value for IDD Field `Length`
                Units: m
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
                                 ' for field `ShadingBuilding.length`'.format(value))
        self._data["Length"] = value

    @property
    def height(self):
        """Get height

        Returns:
            float: the value of `height` or None if not set
        """
        return self._data["Height"]

    @height.setter
    def height(self, value=None):
        """  Corresponds to IDD Field `Height`

        Args:
            value (float): value for IDD Field `Height`
                Units: m
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
                                 ' for field `ShadingBuilding.height`'.format(value))
        self._data["Height"] = value

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
                    raise ValueError("Required field ShadingBuilding:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingBuilding:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingBuilding: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingBuilding: {} / {}".format(out_fields,
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

class ShadingSiteDetailed(object):
    """ Corresponds to IDD object `Shading:Site:Detailed`
        used for shading elements such as trees
        these items are fixed in space and would not move with relative geometry
    """
    internal_name = "Shading:Site:Detailed"
    field_count = 3
    required_fields = ["Name", "Number of Vertices"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 12
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Site:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Transmittance Schedule Name"] = None
        self._data["Number of Vertices"] = None
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
            self.transmittance_schedule_name = None
        else:
            self.transmittance_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `ShadingSiteDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingSiteDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingSiteDetailed.name`')
        self._data["Name"] = value

    @property
    def transmittance_schedule_name(self):
        """Get transmittance_schedule_name

        Returns:
            str: the value of `transmittance_schedule_name` or None if not set
        """
        return self._data["Transmittance Schedule Name"]

    @transmittance_schedule_name.setter
    def transmittance_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Transmittance Schedule Name`
        Transmittance schedule for the shading device, defaults to zero (always opaque)

        Args:
            value (str): value for IDD Field `Transmittance Schedule Name`
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
                                 ' for field `ShadingSiteDetailed.transmittance_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingSiteDetailed.transmittance_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingSiteDetailed.transmittance_schedule_name`')
        self._data["Transmittance Schedule Name"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 6 vertex coordinates -- extensible object
        Rules for vertices are given in GlobalGeometryRules coordinates --
        For this object all surface coordinates are in world coordinates.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `ShadingSiteDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `ShadingSiteDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `ShadingSiteDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingSiteDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingSiteDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingSiteDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field ShadingSiteDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingSiteDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingSiteDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingSiteDetailed: {} / {}".format(out_fields,
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

class ShadingBuildingDetailed(object):
    """ Corresponds to IDD object `Shading:Building:Detailed`
        used for shading elements such as trees, other buildings, parts of this building not being modeled
        these items are relative to the current building and would move with relative geometry
    """
    internal_name = "Shading:Building:Detailed"
    field_count = 3
    required_fields = ["Name", "Number of Vertices"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 12
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Building:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Transmittance Schedule Name"] = None
        self._data["Number of Vertices"] = None
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
            self.transmittance_schedule_name = None
        else:
            self.transmittance_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `ShadingBuildingDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingBuildingDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingBuildingDetailed.name`')
        self._data["Name"] = value

    @property
    def transmittance_schedule_name(self):
        """Get transmittance_schedule_name

        Returns:
            str: the value of `transmittance_schedule_name` or None if not set
        """
        return self._data["Transmittance Schedule Name"]

    @transmittance_schedule_name.setter
    def transmittance_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Transmittance Schedule Name`
        Transmittance schedule for the shading device, defaults to zero (always opaque)

        Args:
            value (str): value for IDD Field `Transmittance Schedule Name`
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
                                 ' for field `ShadingBuildingDetailed.transmittance_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingBuildingDetailed.transmittance_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingBuildingDetailed.transmittance_schedule_name`')
        self._data["Transmittance Schedule Name"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 6 vertex coordinates -- extensible object
        Rules for vertices are given in GlobalGeometryRules coordinates --
        For this object all surface coordinates are relative to the building origin (0,0,0)
        and will rotate with the BUILDING north axis.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `ShadingBuildingDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `ShadingBuildingDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `ShadingBuildingDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingBuildingDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingBuildingDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingBuildingDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field ShadingBuildingDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingBuildingDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingBuildingDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingBuildingDetailed: {} / {}".format(out_fields,
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

class ShadingOverhang(object):
    """ Corresponds to IDD object `Shading:Overhang`
        Overhangs are usually flat shading surfaces that reference a window or door.
    """
    internal_name = "Shading:Overhang"
    field_count = 7
    required_fields = ["Name", "Window or Door Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Overhang`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Window or Door Name"] = None
        self._data["Height above Window or Door"] = None
        self._data["Tilt Angle from Window/Door"] = None
        self._data["Left extension from Window/Door Width"] = None
        self._data["Right extension from Window/Door Width"] = None
        self._data["Depth"] = None
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
            self.window_or_door_name = None
        else:
            self.window_or_door_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_above_window_or_door = None
        else:
            self.height_above_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle_from_window_or_door = None
        else:
            self.tilt_angle_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_extension_from_window_or_door_width = None
        else:
            self.left_extension_from_window_or_door_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_extension_from_window_or_door_width = None
        else:
            self.right_extension_from_window_or_door_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.depth = None
        else:
            self.depth = vals[i]
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
                                 ' for field `ShadingOverhang.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingOverhang.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingOverhang.name`')
        self._data["Name"] = value

    @property
    def window_or_door_name(self):
        """Get window_or_door_name

        Returns:
            str: the value of `window_or_door_name` or None if not set
        """
        return self._data["Window or Door Name"]

    @window_or_door_name.setter
    def window_or_door_name(self, value=None):
        """  Corresponds to IDD Field `Window or Door Name`

        Args:
            value (str): value for IDD Field `Window or Door Name`
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
                                 ' for field `ShadingOverhang.window_or_door_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingOverhang.window_or_door_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingOverhang.window_or_door_name`')
        self._data["Window or Door Name"] = value

    @property
    def height_above_window_or_door(self):
        """Get height_above_window_or_door

        Returns:
            float: the value of `height_above_window_or_door` or None if not set
        """
        return self._data["Height above Window or Door"]

    @height_above_window_or_door.setter
    def height_above_window_or_door(self, value=None):
        """  Corresponds to IDD Field `Height above Window or Door`

        Args:
            value (float): value for IDD Field `Height above Window or Door`
                Units: m
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
                                 ' for field `ShadingOverhang.height_above_window_or_door`'.format(value))
        self._data["Height above Window or Door"] = value

    @property
    def tilt_angle_from_window_or_door(self):
        """Get tilt_angle_from_window_or_door

        Returns:
            float: the value of `tilt_angle_from_window_or_door` or None if not set
        """
        return self._data["Tilt Angle from Window/Door"]

    @tilt_angle_from_window_or_door.setter
    def tilt_angle_from_window_or_door(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle from Window/Door`

        Args:
            value (float): value for IDD Field `Tilt Angle from Window/Door`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingOverhang.tilt_angle_from_window_or_door`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingOverhang.tilt_angle_from_window_or_door`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingOverhang.tilt_angle_from_window_or_door`')
        self._data["Tilt Angle from Window/Door"] = value

    @property
    def left_extension_from_window_or_door_width(self):
        """Get left_extension_from_window_or_door_width

        Returns:
            float: the value of `left_extension_from_window_or_door_width` or None if not set
        """
        return self._data["Left extension from Window/Door Width"]

    @left_extension_from_window_or_door_width.setter
    def left_extension_from_window_or_door_width(self, value=None):
        """  Corresponds to IDD Field `Left extension from Window/Door Width`

        Args:
            value (float): value for IDD Field `Left extension from Window/Door Width`
                Units: m
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
                                 ' for field `ShadingOverhang.left_extension_from_window_or_door_width`'.format(value))
        self._data["Left extension from Window/Door Width"] = value

    @property
    def right_extension_from_window_or_door_width(self):
        """Get right_extension_from_window_or_door_width

        Returns:
            float: the value of `right_extension_from_window_or_door_width` or None if not set
        """
        return self._data["Right extension from Window/Door Width"]

    @right_extension_from_window_or_door_width.setter
    def right_extension_from_window_or_door_width(self, value=None):
        """  Corresponds to IDD Field `Right extension from Window/Door Width`
        N3 + N4 + Window/Door Width is Overhang Length

        Args:
            value (float): value for IDD Field `Right extension from Window/Door Width`
                Units: m
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
                                 ' for field `ShadingOverhang.right_extension_from_window_or_door_width`'.format(value))
        self._data["Right extension from Window/Door Width"] = value

    @property
    def depth(self):
        """Get depth

        Returns:
            float: the value of `depth` or None if not set
        """
        return self._data["Depth"]

    @depth.setter
    def depth(self, value=None):
        """  Corresponds to IDD Field `Depth`

        Args:
            value (float): value for IDD Field `Depth`
                Units: m
                value >= 0.0
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
                                 ' for field `ShadingOverhang.depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingOverhang.depth`')
        self._data["Depth"] = value

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
                    raise ValueError("Required field ShadingOverhang:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingOverhang:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingOverhang: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingOverhang: {} / {}".format(out_fields,
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

class ShadingOverhangProjection(object):
    """ Corresponds to IDD object `Shading:Overhang:Projection`
        Overhangs are typically flat shading surfaces that reference a window or door.
    """
    internal_name = "Shading:Overhang:Projection"
    field_count = 7
    required_fields = ["Name", "Window or Door Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Overhang:Projection`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Window or Door Name"] = None
        self._data["Height above Window or Door"] = None
        self._data["Tilt Angle from Window/Door"] = None
        self._data["Left extension from Window/Door Width"] = None
        self._data["Right extension from Window/Door Width"] = None
        self._data["Depth as Fraction of Window/Door Height"] = None
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
            self.window_or_door_name = None
        else:
            self.window_or_door_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_above_window_or_door = None
        else:
            self.height_above_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tilt_angle_from_window_or_door = None
        else:
            self.tilt_angle_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_extension_from_window_or_door_width = None
        else:
            self.left_extension_from_window_or_door_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_extension_from_window_or_door_width = None
        else:
            self.right_extension_from_window_or_door_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.depth_as_fraction_of_window_or_door_height = None
        else:
            self.depth_as_fraction_of_window_or_door_height = vals[i]
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
                                 ' for field `ShadingOverhangProjection.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingOverhangProjection.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingOverhangProjection.name`')
        self._data["Name"] = value

    @property
    def window_or_door_name(self):
        """Get window_or_door_name

        Returns:
            str: the value of `window_or_door_name` or None if not set
        """
        return self._data["Window or Door Name"]

    @window_or_door_name.setter
    def window_or_door_name(self, value=None):
        """  Corresponds to IDD Field `Window or Door Name`

        Args:
            value (str): value for IDD Field `Window or Door Name`
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
                                 ' for field `ShadingOverhangProjection.window_or_door_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingOverhangProjection.window_or_door_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingOverhangProjection.window_or_door_name`')
        self._data["Window or Door Name"] = value

    @property
    def height_above_window_or_door(self):
        """Get height_above_window_or_door

        Returns:
            float: the value of `height_above_window_or_door` or None if not set
        """
        return self._data["Height above Window or Door"]

    @height_above_window_or_door.setter
    def height_above_window_or_door(self, value=None):
        """  Corresponds to IDD Field `Height above Window or Door`

        Args:
            value (float): value for IDD Field `Height above Window or Door`
                Units: m
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
                                 ' for field `ShadingOverhangProjection.height_above_window_or_door`'.format(value))
        self._data["Height above Window or Door"] = value

    @property
    def tilt_angle_from_window_or_door(self):
        """Get tilt_angle_from_window_or_door

        Returns:
            float: the value of `tilt_angle_from_window_or_door` or None if not set
        """
        return self._data["Tilt Angle from Window/Door"]

    @tilt_angle_from_window_or_door.setter
    def tilt_angle_from_window_or_door(self, value=90.0):
        """  Corresponds to IDD Field `Tilt Angle from Window/Door`

        Args:
            value (float): value for IDD Field `Tilt Angle from Window/Door`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingOverhangProjection.tilt_angle_from_window_or_door`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingOverhangProjection.tilt_angle_from_window_or_door`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingOverhangProjection.tilt_angle_from_window_or_door`')
        self._data["Tilt Angle from Window/Door"] = value

    @property
    def left_extension_from_window_or_door_width(self):
        """Get left_extension_from_window_or_door_width

        Returns:
            float: the value of `left_extension_from_window_or_door_width` or None if not set
        """
        return self._data["Left extension from Window/Door Width"]

    @left_extension_from_window_or_door_width.setter
    def left_extension_from_window_or_door_width(self, value=None):
        """  Corresponds to IDD Field `Left extension from Window/Door Width`

        Args:
            value (float): value for IDD Field `Left extension from Window/Door Width`
                Units: m
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
                                 ' for field `ShadingOverhangProjection.left_extension_from_window_or_door_width`'.format(value))
        self._data["Left extension from Window/Door Width"] = value

    @property
    def right_extension_from_window_or_door_width(self):
        """Get right_extension_from_window_or_door_width

        Returns:
            float: the value of `right_extension_from_window_or_door_width` or None if not set
        """
        return self._data["Right extension from Window/Door Width"]

    @right_extension_from_window_or_door_width.setter
    def right_extension_from_window_or_door_width(self, value=None):
        """  Corresponds to IDD Field `Right extension from Window/Door Width`
        N3 + N4 + Window/Door Width is Overhang Length

        Args:
            value (float): value for IDD Field `Right extension from Window/Door Width`
                Units: m
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
                                 ' for field `ShadingOverhangProjection.right_extension_from_window_or_door_width`'.format(value))
        self._data["Right extension from Window/Door Width"] = value

    @property
    def depth_as_fraction_of_window_or_door_height(self):
        """Get depth_as_fraction_of_window_or_door_height

        Returns:
            float: the value of `depth_as_fraction_of_window_or_door_height` or None if not set
        """
        return self._data["Depth as Fraction of Window/Door Height"]

    @depth_as_fraction_of_window_or_door_height.setter
    def depth_as_fraction_of_window_or_door_height(self, value=None):
        """  Corresponds to IDD Field `Depth as Fraction of Window/Door Height`

        Args:
            value (float): value for IDD Field `Depth as Fraction of Window/Door Height`
                Units: dimensionless
                value >= 0.0
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
                                 ' for field `ShadingOverhangProjection.depth_as_fraction_of_window_or_door_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingOverhangProjection.depth_as_fraction_of_window_or_door_height`')
        self._data["Depth as Fraction of Window/Door Height"] = value

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
                    raise ValueError("Required field ShadingOverhangProjection:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingOverhangProjection:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingOverhangProjection: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingOverhangProjection: {} / {}".format(out_fields,
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

class ShadingFin(object):
    """ Corresponds to IDD object `Shading:Fin`
        Fins are usually shading surfaces that are perpendicular to a window or door.
    """
    internal_name = "Shading:Fin"
    field_count = 12
    required_fields = ["Name", "Window or Door Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Fin`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Window or Door Name"] = None
        self._data["Left Extension from Window/Door"] = None
        self._data["Left Distance Above Top of Window"] = None
        self._data["Left Distance Below Bottom of Window"] = None
        self._data["Left Tilt Angle from Window/Door"] = None
        self._data["Left Depth"] = None
        self._data["Right Extension from Window/Door"] = None
        self._data["Right Distance Above Top of Window"] = None
        self._data["Right Distance Below Bottom of Window"] = None
        self._data["Right Tilt Angle from Window/Door"] = None
        self._data["Right Depth"] = None
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
            self.window_or_door_name = None
        else:
            self.window_or_door_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_extension_from_window_or_door = None
        else:
            self.left_extension_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_distance_above_top_of_window = None
        else:
            self.left_distance_above_top_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_distance_below_bottom_of_window = None
        else:
            self.left_distance_below_bottom_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_tilt_angle_from_window_or_door = None
        else:
            self.left_tilt_angle_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_depth = None
        else:
            self.left_depth = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_extension_from_window_or_door = None
        else:
            self.right_extension_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_distance_above_top_of_window = None
        else:
            self.right_distance_above_top_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_distance_below_bottom_of_window = None
        else:
            self.right_distance_below_bottom_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_tilt_angle_from_window_or_door = None
        else:
            self.right_tilt_angle_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_depth = None
        else:
            self.right_depth = vals[i]
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
                                 ' for field `ShadingFin.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingFin.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingFin.name`')
        self._data["Name"] = value

    @property
    def window_or_door_name(self):
        """Get window_or_door_name

        Returns:
            str: the value of `window_or_door_name` or None if not set
        """
        return self._data["Window or Door Name"]

    @window_or_door_name.setter
    def window_or_door_name(self, value=None):
        """  Corresponds to IDD Field `Window or Door Name`

        Args:
            value (str): value for IDD Field `Window or Door Name`
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
                                 ' for field `ShadingFin.window_or_door_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingFin.window_or_door_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingFin.window_or_door_name`')
        self._data["Window or Door Name"] = value

    @property
    def left_extension_from_window_or_door(self):
        """Get left_extension_from_window_or_door

        Returns:
            float: the value of `left_extension_from_window_or_door` or None if not set
        """
        return self._data["Left Extension from Window/Door"]

    @left_extension_from_window_or_door.setter
    def left_extension_from_window_or_door(self, value=None):
        """  Corresponds to IDD Field `Left Extension from Window/Door`

        Args:
            value (float): value for IDD Field `Left Extension from Window/Door`
                Units: m
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
                                 ' for field `ShadingFin.left_extension_from_window_or_door`'.format(value))
        self._data["Left Extension from Window/Door"] = value

    @property
    def left_distance_above_top_of_window(self):
        """Get left_distance_above_top_of_window

        Returns:
            float: the value of `left_distance_above_top_of_window` or None if not set
        """
        return self._data["Left Distance Above Top of Window"]

    @left_distance_above_top_of_window.setter
    def left_distance_above_top_of_window(self, value=None):
        """  Corresponds to IDD Field `Left Distance Above Top of Window`

        Args:
            value (float): value for IDD Field `Left Distance Above Top of Window`
                Units: m
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
                                 ' for field `ShadingFin.left_distance_above_top_of_window`'.format(value))
        self._data["Left Distance Above Top of Window"] = value

    @property
    def left_distance_below_bottom_of_window(self):
        """Get left_distance_below_bottom_of_window

        Returns:
            float: the value of `left_distance_below_bottom_of_window` or None if not set
        """
        return self._data["Left Distance Below Bottom of Window"]

    @left_distance_below_bottom_of_window.setter
    def left_distance_below_bottom_of_window(self, value=None):
        """  Corresponds to IDD Field `Left Distance Below Bottom of Window`
        N2 + N3 + height of Window/Door is height of Fin

        Args:
            value (float): value for IDD Field `Left Distance Below Bottom of Window`
                Units: m
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
                                 ' for field `ShadingFin.left_distance_below_bottom_of_window`'.format(value))
        self._data["Left Distance Below Bottom of Window"] = value

    @property
    def left_tilt_angle_from_window_or_door(self):
        """Get left_tilt_angle_from_window_or_door

        Returns:
            float: the value of `left_tilt_angle_from_window_or_door` or None if not set
        """
        return self._data["Left Tilt Angle from Window/Door"]

    @left_tilt_angle_from_window_or_door.setter
    def left_tilt_angle_from_window_or_door(self, value=90.0):
        """  Corresponds to IDD Field `Left Tilt Angle from Window/Door`

        Args:
            value (float): value for IDD Field `Left Tilt Angle from Window/Door`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingFin.left_tilt_angle_from_window_or_door`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFin.left_tilt_angle_from_window_or_door`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingFin.left_tilt_angle_from_window_or_door`')
        self._data["Left Tilt Angle from Window/Door"] = value

    @property
    def left_depth(self):
        """Get left_depth

        Returns:
            float: the value of `left_depth` or None if not set
        """
        return self._data["Left Depth"]

    @left_depth.setter
    def left_depth(self, value=None):
        """  Corresponds to IDD Field `Left Depth`

        Args:
            value (float): value for IDD Field `Left Depth`
                Units: m
                value >= 0.0
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
                                 ' for field `ShadingFin.left_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFin.left_depth`')
        self._data["Left Depth"] = value

    @property
    def right_extension_from_window_or_door(self):
        """Get right_extension_from_window_or_door

        Returns:
            float: the value of `right_extension_from_window_or_door` or None if not set
        """
        return self._data["Right Extension from Window/Door"]

    @right_extension_from_window_or_door.setter
    def right_extension_from_window_or_door(self, value=None):
        """  Corresponds to IDD Field `Right Extension from Window/Door`

        Args:
            value (float): value for IDD Field `Right Extension from Window/Door`
                Units: m
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
                                 ' for field `ShadingFin.right_extension_from_window_or_door`'.format(value))
        self._data["Right Extension from Window/Door"] = value

    @property
    def right_distance_above_top_of_window(self):
        """Get right_distance_above_top_of_window

        Returns:
            float: the value of `right_distance_above_top_of_window` or None if not set
        """
        return self._data["Right Distance Above Top of Window"]

    @right_distance_above_top_of_window.setter
    def right_distance_above_top_of_window(self, value=None):
        """  Corresponds to IDD Field `Right Distance Above Top of Window`

        Args:
            value (float): value for IDD Field `Right Distance Above Top of Window`
                Units: m
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
                                 ' for field `ShadingFin.right_distance_above_top_of_window`'.format(value))
        self._data["Right Distance Above Top of Window"] = value

    @property
    def right_distance_below_bottom_of_window(self):
        """Get right_distance_below_bottom_of_window

        Returns:
            float: the value of `right_distance_below_bottom_of_window` or None if not set
        """
        return self._data["Right Distance Below Bottom of Window"]

    @right_distance_below_bottom_of_window.setter
    def right_distance_below_bottom_of_window(self, value=None):
        """  Corresponds to IDD Field `Right Distance Below Bottom of Window`
        N7 + N8 + height of Window/Door is height of Fin

        Args:
            value (float): value for IDD Field `Right Distance Below Bottom of Window`
                Units: m
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
                                 ' for field `ShadingFin.right_distance_below_bottom_of_window`'.format(value))
        self._data["Right Distance Below Bottom of Window"] = value

    @property
    def right_tilt_angle_from_window_or_door(self):
        """Get right_tilt_angle_from_window_or_door

        Returns:
            float: the value of `right_tilt_angle_from_window_or_door` or None if not set
        """
        return self._data["Right Tilt Angle from Window/Door"]

    @right_tilt_angle_from_window_or_door.setter
    def right_tilt_angle_from_window_or_door(self, value=90.0):
        """  Corresponds to IDD Field `Right Tilt Angle from Window/Door`

        Args:
            value (float): value for IDD Field `Right Tilt Angle from Window/Door`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingFin.right_tilt_angle_from_window_or_door`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFin.right_tilt_angle_from_window_or_door`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingFin.right_tilt_angle_from_window_or_door`')
        self._data["Right Tilt Angle from Window/Door"] = value

    @property
    def right_depth(self):
        """Get right_depth

        Returns:
            float: the value of `right_depth` or None if not set
        """
        return self._data["Right Depth"]

    @right_depth.setter
    def right_depth(self, value=None):
        """  Corresponds to IDD Field `Right Depth`

        Args:
            value (float): value for IDD Field `Right Depth`
                Units: m
                value >= 0.0
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
                                 ' for field `ShadingFin.right_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFin.right_depth`')
        self._data["Right Depth"] = value

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
                    raise ValueError("Required field ShadingFin:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingFin:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingFin: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingFin: {} / {}".format(out_fields,
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

class ShadingFinProjection(object):
    """ Corresponds to IDD object `Shading:Fin:Projection`
        Fins are usually shading surfaces that are perpendicular to a window or door.
    """
    internal_name = "Shading:Fin:Projection"
    field_count = 12
    required_fields = ["Name", "Window or Door Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Fin:Projection`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Window or Door Name"] = None
        self._data["Left Extension from Window/Door"] = None
        self._data["Left Distance Above Top of Window"] = None
        self._data["Left Distance Below Bottom of Window"] = None
        self._data["Left Tilt Angle from Window/Door"] = None
        self._data["Left Depth as Fraction of Window/Door Width"] = None
        self._data["Right Extension from Window/Door"] = None
        self._data["Right Distance Above Top of Window"] = None
        self._data["Right Distance Below Bottom of Window"] = None
        self._data["Right Tilt Angle from Window/Door"] = None
        self._data["Right Depth as Fraction of Window/Door Width"] = None
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
            self.window_or_door_name = None
        else:
            self.window_or_door_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_extension_from_window_or_door = None
        else:
            self.left_extension_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_distance_above_top_of_window = None
        else:
            self.left_distance_above_top_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_distance_below_bottom_of_window = None
        else:
            self.left_distance_below_bottom_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_tilt_angle_from_window_or_door = None
        else:
            self.left_tilt_angle_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.left_depth_as_fraction_of_window_or_door_width = None
        else:
            self.left_depth_as_fraction_of_window_or_door_width = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_extension_from_window_or_door = None
        else:
            self.right_extension_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_distance_above_top_of_window = None
        else:
            self.right_distance_above_top_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_distance_below_bottom_of_window = None
        else:
            self.right_distance_below_bottom_of_window = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_tilt_angle_from_window_or_door = None
        else:
            self.right_tilt_angle_from_window_or_door = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.right_depth_as_fraction_of_window_or_door_width = None
        else:
            self.right_depth_as_fraction_of_window_or_door_width = vals[i]
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
                                 ' for field `ShadingFinProjection.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingFinProjection.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingFinProjection.name`')
        self._data["Name"] = value

    @property
    def window_or_door_name(self):
        """Get window_or_door_name

        Returns:
            str: the value of `window_or_door_name` or None if not set
        """
        return self._data["Window or Door Name"]

    @window_or_door_name.setter
    def window_or_door_name(self, value=None):
        """  Corresponds to IDD Field `Window or Door Name`

        Args:
            value (str): value for IDD Field `Window or Door Name`
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
                                 ' for field `ShadingFinProjection.window_or_door_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingFinProjection.window_or_door_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingFinProjection.window_or_door_name`')
        self._data["Window or Door Name"] = value

    @property
    def left_extension_from_window_or_door(self):
        """Get left_extension_from_window_or_door

        Returns:
            float: the value of `left_extension_from_window_or_door` or None if not set
        """
        return self._data["Left Extension from Window/Door"]

    @left_extension_from_window_or_door.setter
    def left_extension_from_window_or_door(self, value=None):
        """  Corresponds to IDD Field `Left Extension from Window/Door`

        Args:
            value (float): value for IDD Field `Left Extension from Window/Door`
                Units: m
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
                                 ' for field `ShadingFinProjection.left_extension_from_window_or_door`'.format(value))
        self._data["Left Extension from Window/Door"] = value

    @property
    def left_distance_above_top_of_window(self):
        """Get left_distance_above_top_of_window

        Returns:
            float: the value of `left_distance_above_top_of_window` or None if not set
        """
        return self._data["Left Distance Above Top of Window"]

    @left_distance_above_top_of_window.setter
    def left_distance_above_top_of_window(self, value=None):
        """  Corresponds to IDD Field `Left Distance Above Top of Window`

        Args:
            value (float): value for IDD Field `Left Distance Above Top of Window`
                Units: m
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
                                 ' for field `ShadingFinProjection.left_distance_above_top_of_window`'.format(value))
        self._data["Left Distance Above Top of Window"] = value

    @property
    def left_distance_below_bottom_of_window(self):
        """Get left_distance_below_bottom_of_window

        Returns:
            float: the value of `left_distance_below_bottom_of_window` or None if not set
        """
        return self._data["Left Distance Below Bottom of Window"]

    @left_distance_below_bottom_of_window.setter
    def left_distance_below_bottom_of_window(self, value=None):
        """  Corresponds to IDD Field `Left Distance Below Bottom of Window`
        N2 + N3 + height of Window/Door is height of Fin

        Args:
            value (float): value for IDD Field `Left Distance Below Bottom of Window`
                Units: m
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
                                 ' for field `ShadingFinProjection.left_distance_below_bottom_of_window`'.format(value))
        self._data["Left Distance Below Bottom of Window"] = value

    @property
    def left_tilt_angle_from_window_or_door(self):
        """Get left_tilt_angle_from_window_or_door

        Returns:
            float: the value of `left_tilt_angle_from_window_or_door` or None if not set
        """
        return self._data["Left Tilt Angle from Window/Door"]

    @left_tilt_angle_from_window_or_door.setter
    def left_tilt_angle_from_window_or_door(self, value=90.0):
        """  Corresponds to IDD Field `Left Tilt Angle from Window/Door`

        Args:
            value (float): value for IDD Field `Left Tilt Angle from Window/Door`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingFinProjection.left_tilt_angle_from_window_or_door`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFinProjection.left_tilt_angle_from_window_or_door`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingFinProjection.left_tilt_angle_from_window_or_door`')
        self._data["Left Tilt Angle from Window/Door"] = value

    @property
    def left_depth_as_fraction_of_window_or_door_width(self):
        """Get left_depth_as_fraction_of_window_or_door_width

        Returns:
            float: the value of `left_depth_as_fraction_of_window_or_door_width` or None if not set
        """
        return self._data["Left Depth as Fraction of Window/Door Width"]

    @left_depth_as_fraction_of_window_or_door_width.setter
    def left_depth_as_fraction_of_window_or_door_width(self, value=None):
        """  Corresponds to IDD Field `Left Depth as Fraction of Window/Door Width`

        Args:
            value (float): value for IDD Field `Left Depth as Fraction of Window/Door Width`
                Units: dimensionless
                value >= 0.0
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
                                 ' for field `ShadingFinProjection.left_depth_as_fraction_of_window_or_door_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFinProjection.left_depth_as_fraction_of_window_or_door_width`')
        self._data["Left Depth as Fraction of Window/Door Width"] = value

    @property
    def right_extension_from_window_or_door(self):
        """Get right_extension_from_window_or_door

        Returns:
            float: the value of `right_extension_from_window_or_door` or None if not set
        """
        return self._data["Right Extension from Window/Door"]

    @right_extension_from_window_or_door.setter
    def right_extension_from_window_or_door(self, value=None):
        """  Corresponds to IDD Field `Right Extension from Window/Door`

        Args:
            value (float): value for IDD Field `Right Extension from Window/Door`
                Units: m
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
                                 ' for field `ShadingFinProjection.right_extension_from_window_or_door`'.format(value))
        self._data["Right Extension from Window/Door"] = value

    @property
    def right_distance_above_top_of_window(self):
        """Get right_distance_above_top_of_window

        Returns:
            float: the value of `right_distance_above_top_of_window` or None if not set
        """
        return self._data["Right Distance Above Top of Window"]

    @right_distance_above_top_of_window.setter
    def right_distance_above_top_of_window(self, value=None):
        """  Corresponds to IDD Field `Right Distance Above Top of Window`

        Args:
            value (float): value for IDD Field `Right Distance Above Top of Window`
                Units: m
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
                                 ' for field `ShadingFinProjection.right_distance_above_top_of_window`'.format(value))
        self._data["Right Distance Above Top of Window"] = value

    @property
    def right_distance_below_bottom_of_window(self):
        """Get right_distance_below_bottom_of_window

        Returns:
            float: the value of `right_distance_below_bottom_of_window` or None if not set
        """
        return self._data["Right Distance Below Bottom of Window"]

    @right_distance_below_bottom_of_window.setter
    def right_distance_below_bottom_of_window(self, value=None):
        """  Corresponds to IDD Field `Right Distance Below Bottom of Window`
        N7 + N8 + height of Window/Door is height of Fin

        Args:
            value (float): value for IDD Field `Right Distance Below Bottom of Window`
                Units: m
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
                                 ' for field `ShadingFinProjection.right_distance_below_bottom_of_window`'.format(value))
        self._data["Right Distance Below Bottom of Window"] = value

    @property
    def right_tilt_angle_from_window_or_door(self):
        """Get right_tilt_angle_from_window_or_door

        Returns:
            float: the value of `right_tilt_angle_from_window_or_door` or None if not set
        """
        return self._data["Right Tilt Angle from Window/Door"]

    @right_tilt_angle_from_window_or_door.setter
    def right_tilt_angle_from_window_or_door(self, value=90.0):
        """  Corresponds to IDD Field `Right Tilt Angle from Window/Door`

        Args:
            value (float): value for IDD Field `Right Tilt Angle from Window/Door`
                Units: deg
                Default value: 90.0
                value >= 0.0
                value <= 180.0
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
                                 ' for field `ShadingFinProjection.right_tilt_angle_from_window_or_door`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFinProjection.right_tilt_angle_from_window_or_door`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `ShadingFinProjection.right_tilt_angle_from_window_or_door`')
        self._data["Right Tilt Angle from Window/Door"] = value

    @property
    def right_depth_as_fraction_of_window_or_door_width(self):
        """Get right_depth_as_fraction_of_window_or_door_width

        Returns:
            float: the value of `right_depth_as_fraction_of_window_or_door_width` or None if not set
        """
        return self._data["Right Depth as Fraction of Window/Door Width"]

    @right_depth_as_fraction_of_window_or_door_width.setter
    def right_depth_as_fraction_of_window_or_door_width(self, value=None):
        """  Corresponds to IDD Field `Right Depth as Fraction of Window/Door Width`

        Args:
            value (float): value for IDD Field `Right Depth as Fraction of Window/Door Width`
                Units: dimensionless
                value >= 0.0
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
                                 ' for field `ShadingFinProjection.right_depth_as_fraction_of_window_or_door_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingFinProjection.right_depth_as_fraction_of_window_or_door_width`')
        self._data["Right Depth as Fraction of Window/Door Width"] = value

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
                    raise ValueError("Required field ShadingFinProjection:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingFinProjection:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingFinProjection: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingFinProjection: {} / {}".format(out_fields,
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

class ShadingZoneDetailed(object):
    """ Corresponds to IDD object `Shading:Zone:Detailed`
        used For fins, overhangs, elements that shade the building, are attached to the building
        but are not part of the heat transfer calculations
    """
    internal_name = "Shading:Zone:Detailed"
    field_count = 4
    required_fields = ["Name", "Base Surface Name", "Number of Vertices"]
    extensible_fields = 3
    format = "vertices"
    min_fields = 13
    extensible_keys = ["Vertex 1 X-coordinate", "Vertex 1 Y-coordinate", "Vertex 1 Z-coordinate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Shading:Zone:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Base Surface Name"] = None
        self._data["Transmittance Schedule Name"] = None
        self._data["Number of Vertices"] = None
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
            self.base_surface_name = None
        else:
            self.base_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transmittance_schedule_name = None
        else:
            self.transmittance_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
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
                                 ' for field `ShadingZoneDetailed.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingZoneDetailed.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingZoneDetailed.name`')
        self._data["Name"] = value

    @property
    def base_surface_name(self):
        """Get base_surface_name

        Returns:
            str: the value of `base_surface_name` or None if not set
        """
        return self._data["Base Surface Name"]

    @base_surface_name.setter
    def base_surface_name(self, value=None):
        """  Corresponds to IDD Field `Base Surface Name`

        Args:
            value (str): value for IDD Field `Base Surface Name`
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
                                 ' for field `ShadingZoneDetailed.base_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingZoneDetailed.base_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingZoneDetailed.base_surface_name`')
        self._data["Base Surface Name"] = value

    @property
    def transmittance_schedule_name(self):
        """Get transmittance_schedule_name

        Returns:
            str: the value of `transmittance_schedule_name` or None if not set
        """
        return self._data["Transmittance Schedule Name"]

    @transmittance_schedule_name.setter
    def transmittance_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Transmittance Schedule Name`
        Transmittance schedule for the shading device, defaults to zero (always opaque)

        Args:
            value (str): value for IDD Field `Transmittance Schedule Name`
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
                                 ' for field `ShadingZoneDetailed.transmittance_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingZoneDetailed.transmittance_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingZoneDetailed.transmittance_schedule_name`')
        self._data["Transmittance Schedule Name"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value="autocalculate"):
        """  Corresponds to IDD Field `Number of Vertices`
        shown with 6 vertex coordinates -- extensible object
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  if world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Vertices`
                Default value: "autocalculate"
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autocalculate" '
                                 'for field `ShadingZoneDetailed.number_of_vertices`'.format(value))
                    self._data["Number of Vertices"] = "Autocalculate"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autocalculate"'
                                 ' for field `ShadingZoneDetailed.number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `ShadingZoneDetailed.number_of_vertices`')
        self._data["Number of Vertices"] = value

    def add_extensible(self,
                       vertex_1_xcoordinate=None,
                       vertex_1_ycoordinate=None,
                       vertex_1_zcoordinate=None,
                       ):
        """ Add values for extensible fields

        Args:

            vertex_1_xcoordinate (float): value for IDD Field `Vertex 1 X-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_ycoordinate (float): value for IDD Field `Vertex 1 Y-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            vertex_1_zcoordinate (float): value for IDD Field `Vertex 1 Z-coordinate`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_vertex_1_xcoordinate(vertex_1_xcoordinate))
        vals.append(self._check_vertex_1_ycoordinate(vertex_1_ycoordinate))
        vals.append(self._check_vertex_1_zcoordinate(vertex_1_zcoordinate))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_vertex_1_xcoordinate(self, value):
        """ Validates falue of field `Vertex 1 X-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingZoneDetailed.vertex_1_xcoordinate`'.format(value))
        return value

    def _check_vertex_1_ycoordinate(self, value):
        """ Validates falue of field `Vertex 1 Y-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingZoneDetailed.vertex_1_ycoordinate`'.format(value))
        return value

    def _check_vertex_1_zcoordinate(self, value):
        """ Validates falue of field `Vertex 1 Z-coordinate`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ShadingZoneDetailed.vertex_1_zcoordinate`'.format(value))
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
                    raise ValueError("Required field ShadingZoneDetailed:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingZoneDetailed:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingZoneDetailed: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingZoneDetailed: {} / {}".format(out_fields,
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

class ShadingPropertyReflectance(object):
    """ Corresponds to IDD object `ShadingProperty:Reflectance`
        If this object is not defined for a shading surface the default values
        listed in following fields will be used in the solar reflection calculation.
    """
    internal_name = "ShadingProperty:Reflectance"
    field_count = 5
    required_fields = ["Shading Surface Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ShadingProperty:Reflectance`
        """
        self._data = OrderedDict()
        self._data["Shading Surface Name"] = None
        self._data["Diffuse Solar Reflectance of Unglazed Part of Shading Surface"] = None
        self._data["Diffuse Visible Reflectance of Unglazed Part of Shading Surface"] = None
        self._data["Fraction of Shading Surface That Is Glazed"] = None
        self._data["Glazing Construction Name"] = None
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
            self.shading_surface_name = None
        else:
            self.shading_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface = None
        else:
            self.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface = None
        else:
            self.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_shading_surface_that_is_glazed = None
        else:
            self.fraction_of_shading_surface_that_is_glazed = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glazing_construction_name = None
        else:
            self.glazing_construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def shading_surface_name(self):
        """Get shading_surface_name

        Returns:
            str: the value of `shading_surface_name` or None if not set
        """
        return self._data["Shading Surface Name"]

    @shading_surface_name.setter
    def shading_surface_name(self, value=None):
        """  Corresponds to IDD Field `Shading Surface Name`

        Args:
            value (str): value for IDD Field `Shading Surface Name`
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
                                 ' for field `ShadingPropertyReflectance.shading_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingPropertyReflectance.shading_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingPropertyReflectance.shading_surface_name`')
        self._data["Shading Surface Name"] = value

    @property
    def diffuse_solar_reflectance_of_unglazed_part_of_shading_surface(self):
        """Get diffuse_solar_reflectance_of_unglazed_part_of_shading_surface

        Returns:
            float: the value of `diffuse_solar_reflectance_of_unglazed_part_of_shading_surface` or None if not set
        """
        return self._data["Diffuse Solar Reflectance of Unglazed Part of Shading Surface"]

    @diffuse_solar_reflectance_of_unglazed_part_of_shading_surface.setter
    def diffuse_solar_reflectance_of_unglazed_part_of_shading_surface(self, value=0.2):
        """  Corresponds to IDD Field `Diffuse Solar Reflectance of Unglazed Part of Shading Surface`

        Args:
            value (float): value for IDD Field `Diffuse Solar Reflectance of Unglazed Part of Shading Surface`
                Default value: 0.2
                value >= 0.0
                value <= 1.0
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
                                 ' for field `ShadingPropertyReflectance.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingPropertyReflectance.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ShadingPropertyReflectance.diffuse_solar_reflectance_of_unglazed_part_of_shading_surface`')
        self._data["Diffuse Solar Reflectance of Unglazed Part of Shading Surface"] = value

    @property
    def diffuse_visible_reflectance_of_unglazed_part_of_shading_surface(self):
        """Get diffuse_visible_reflectance_of_unglazed_part_of_shading_surface

        Returns:
            float: the value of `diffuse_visible_reflectance_of_unglazed_part_of_shading_surface` or None if not set
        """
        return self._data["Diffuse Visible Reflectance of Unglazed Part of Shading Surface"]

    @diffuse_visible_reflectance_of_unglazed_part_of_shading_surface.setter
    def diffuse_visible_reflectance_of_unglazed_part_of_shading_surface(self, value=0.2):
        """  Corresponds to IDD Field `Diffuse Visible Reflectance of Unglazed Part of Shading Surface`

        Args:
            value (float): value for IDD Field `Diffuse Visible Reflectance of Unglazed Part of Shading Surface`
                Default value: 0.2
                value >= 0.0
                value <= 1.0
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
                                 ' for field `ShadingPropertyReflectance.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingPropertyReflectance.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ShadingPropertyReflectance.diffuse_visible_reflectance_of_unglazed_part_of_shading_surface`')
        self._data["Diffuse Visible Reflectance of Unglazed Part of Shading Surface"] = value

    @property
    def fraction_of_shading_surface_that_is_glazed(self):
        """Get fraction_of_shading_surface_that_is_glazed

        Returns:
            float: the value of `fraction_of_shading_surface_that_is_glazed` or None if not set
        """
        return self._data["Fraction of Shading Surface That Is Glazed"]

    @fraction_of_shading_surface_that_is_glazed.setter
    def fraction_of_shading_surface_that_is_glazed(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Shading Surface That Is Glazed`

        Args:
            value (float): value for IDD Field `Fraction of Shading Surface That Is Glazed`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 ' for field `ShadingPropertyReflectance.fraction_of_shading_surface_that_is_glazed`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ShadingPropertyReflectance.fraction_of_shading_surface_that_is_glazed`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ShadingPropertyReflectance.fraction_of_shading_surface_that_is_glazed`')
        self._data["Fraction of Shading Surface That Is Glazed"] = value

    @property
    def glazing_construction_name(self):
        """Get glazing_construction_name

        Returns:
            str: the value of `glazing_construction_name` or None if not set
        """
        return self._data["Glazing Construction Name"]

    @glazing_construction_name.setter
    def glazing_construction_name(self, value=None):
        """  Corresponds to IDD Field `Glazing Construction Name`
        Required if Fraction of Shading Surface That Is Glazed > 0.0

        Args:
            value (str): value for IDD Field `Glazing Construction Name`
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
                                 ' for field `ShadingPropertyReflectance.glazing_construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ShadingPropertyReflectance.glazing_construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ShadingPropertyReflectance.glazing_construction_name`')
        self._data["Glazing Construction Name"] = value

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
                    raise ValueError("Required field ShadingPropertyReflectance:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ShadingPropertyReflectance:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ShadingPropertyReflectance: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ShadingPropertyReflectance: {} / {}".format(out_fields,
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