from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class SurfacePropertyHeatTransferAlgorithm(object):
    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm`
        Determines which Heat Balance Algorithm will be used for a specific surface
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    internal_name = "SurfaceProperty:HeatTransferAlgorithm"
    field_count = 2
    required_fields = ["Surface Name", "Algorithm"]
    extensible_fields = 0
    format = None
    min_fields = 2
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Algorithm"] = None
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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithm.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithm.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithm.surface_name`')
        self._data["Surface Name"] = value

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `Algorithm`

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithm.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithm.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithm.algorithm`')
            vals = {}
            vals["conductiontransferfunction"] = "ConductionTransferFunction"
            vals["moisturepenetrationdepthconductiontransferfunction"] = "MoisturePenetrationDepthConductionTransferFunction"
            vals["conductionfinitedifference"] = "ConductionFiniteDifference"
            vals["combinedheatandmoisturefiniteelement"] = "CombinedHeatAndMoistureFiniteElement"
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
                                     'field `SurfacePropertyHeatTransferAlgorithm.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyHeatTransferAlgorithm.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

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
                    raise ValueError("Required field SurfacePropertyHeatTransferAlgorithm:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyHeatTransferAlgorithm:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyHeatTransferAlgorithm: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyHeatTransferAlgorithm: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyHeatTransferAlgorithmMultipleSurface(object):
    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm:MultipleSurface`
        Determines which Heat Balance Algorithm will be used for a group of surface types
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    internal_name = "SurfaceProperty:HeatTransferAlgorithm:MultipleSurface"
    field_count = 3
    required_fields = ["Name", "Surface Type", "Algorithm"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm:MultipleSurface`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Type"] = None
        self._data["Algorithm"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.name`')
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
                      - AllExteriorSurfaces
                      - AllExteriorWalls
                      - AllExteriorRoofs
                      - AllExteriorFloors
                      - AllGroundContactSurfaces
                      - AllInteriorSurfaces
                      - AllInteriorWalls
                      - AllInteriorCeilings
                      - AllInteriorFloors
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.surface_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.surface_type`')
            vals = {}
            vals["allexteriorsurfaces"] = "AllExteriorSurfaces"
            vals["allexteriorwalls"] = "AllExteriorWalls"
            vals["allexteriorroofs"] = "AllExteriorRoofs"
            vals["allexteriorfloors"] = "AllExteriorFloors"
            vals["allgroundcontactsurfaces"] = "AllGroundContactSurfaces"
            vals["allinteriorsurfaces"] = "AllInteriorSurfaces"
            vals["allinteriorwalls"] = "AllInteriorWalls"
            vals["allinteriorceilings"] = "AllInteriorCeilings"
            vals["allinteriorfloors"] = "AllInteriorFloors"
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
                                     'field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.surface_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.surface_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Surface Type"] = value

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `Algorithm`

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.algorithm`')
            vals = {}
            vals["conductiontransferfunction"] = "ConductionTransferFunction"
            vals["moisturepenetrationdepthconductiontransferfunction"] = "MoisturePenetrationDepthConductionTransferFunction"
            vals["conductionfinitedifference"] = "ConductionFiniteDifference"
            vals["combinedheatandmoisturefiniteelement"] = "CombinedHeatAndMoistureFiniteElement"
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
                                     'field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyHeatTransferAlgorithmMultipleSurface.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

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
                    raise ValueError("Required field SurfacePropertyHeatTransferAlgorithmMultipleSurface:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyHeatTransferAlgorithmMultipleSurface:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyHeatTransferAlgorithmMultipleSurface: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyHeatTransferAlgorithmMultipleSurface: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyHeatTransferAlgorithmSurfaceList(object):
    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm:SurfaceList`
        Determines which Heat Balance Algorithm will be used for a list of surfaces
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    internal_name = "SurfaceProperty:HeatTransferAlgorithm:SurfaceList"
    field_count = 2
    required_fields = ["Name", "Algorithm"]
    extensible_fields = 1
    format = None
    min_fields = 3
    extensible_keys = ["Surface Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm:SurfaceList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Algorithm"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.name`')
        self._data["Name"] = value

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `Algorithm`

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.algorithm`')
            vals = {}
            vals["conductiontransferfunction"] = "ConductionTransferFunction"
            vals["moisturepenetrationdepthconductiontransferfunction"] = "MoisturePenetrationDepthConductionTransferFunction"
            vals["conductionfinitedifference"] = "ConductionFiniteDifference"
            vals["combinedheatandmoisturefiniteelement"] = "CombinedHeatAndMoistureFiniteElement"
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
                                     'field `SurfacePropertyHeatTransferAlgorithmSurfaceList.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyHeatTransferAlgorithmSurfaceList.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

    def add_extensible(self,
                       surface_name_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_name_1 (str): value for IDD Field `Surface Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_name_1(surface_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_name_1(self, value):
        """ Validates falue of field `Surface Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.surface_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.surface_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmSurfaceList.surface_name_1`')
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
                    raise ValueError("Required field SurfacePropertyHeatTransferAlgorithmSurfaceList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyHeatTransferAlgorithmSurfaceList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyHeatTransferAlgorithmSurfaceList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyHeatTransferAlgorithmSurfaceList: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyHeatTransferAlgorithmConstruction(object):
    """ Corresponds to IDD object `SurfaceProperty:HeatTransferAlgorithm:Construction`
        Determines which Heat Balance Algorithm will be used for surfaces that have a specific type of construction
        Allows selectively overriding the global setting in HeatBalanceAlgorithm
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    internal_name = "SurfaceProperty:HeatTransferAlgorithm:Construction"
    field_count = 3
    required_fields = ["Algorithm", "Construction Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm:Construction`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Algorithm"] = None
        self._data["Construction Name"] = None
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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmConstruction.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmConstruction.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmConstruction.name`')
        self._data["Name"] = value

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `Algorithm`

        Args:
            value (str): value for IDD Field `Algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmConstruction.algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmConstruction.algorithm`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmConstruction.algorithm`')
            vals = {}
            vals["conductiontransferfunction"] = "ConductionTransferFunction"
            vals["moisturepenetrationdepthconductiontransferfunction"] = "MoisturePenetrationDepthConductionTransferFunction"
            vals["conductionfinitedifference"] = "ConductionFiniteDifference"
            vals["combinedheatandmoisturefiniteelement"] = "CombinedHeatAndMoistureFiniteElement"
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
                                     'field `SurfacePropertyHeatTransferAlgorithmConstruction.algorithm`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyHeatTransferAlgorithmConstruction.algorithm`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Algorithm"] = value

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
                                 ' for field `SurfacePropertyHeatTransferAlgorithmConstruction.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyHeatTransferAlgorithmConstruction.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyHeatTransferAlgorithmConstruction.construction_name`')
        self._data["Construction Name"] = value

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
                    raise ValueError("Required field SurfacePropertyHeatTransferAlgorithmConstruction:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyHeatTransferAlgorithmConstruction:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyHeatTransferAlgorithmConstruction: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyHeatTransferAlgorithmConstruction: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfaceControlMovableInsulation(object):
    """ Corresponds to IDD object `SurfaceControl:MovableInsulation`
        Exterior or Interior Insulation on opaque surfaces
    """
    internal_name = "SurfaceControl:MovableInsulation"
    field_count = 4
    required_fields = ["Insulation Type", "Surface Name", "Material Name", "Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceControl:MovableInsulation`
        """
        self._data = OrderedDict()
        self._data["Insulation Type"] = None
        self._data["Surface Name"] = None
        self._data["Material Name"] = None
        self._data["Schedule Name"] = None
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
            self.insulation_type = None
        else:
            self.insulation_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.material_name = None
        else:
            self.material_name = vals[i]
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
        self.strict = old_strict

    @property
    def insulation_type(self):
        """Get insulation_type

        Returns:
            str: the value of `insulation_type` or None if not set
        """
        return self._data["Insulation Type"]

    @insulation_type.setter
    def insulation_type(self, value=None):
        """  Corresponds to IDD Field `Insulation Type`

        Args:
            value (str): value for IDD Field `Insulation Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfaceControlMovableInsulation.insulation_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceControlMovableInsulation.insulation_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceControlMovableInsulation.insulation_type`')
            vals = {}
            vals["outside"] = "Outside"
            vals["inside"] = "Inside"
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
                                     'field `SurfaceControlMovableInsulation.insulation_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceControlMovableInsulation.insulation_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SurfaceControlMovableInsulation.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceControlMovableInsulation.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceControlMovableInsulation.surface_name`')
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
        """  Corresponds to IDD Field `Material Name`

        Args:
            value (str): value for IDD Field `Material Name`
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
                                 ' for field `SurfaceControlMovableInsulation.material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceControlMovableInsulation.material_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceControlMovableInsulation.material_name`')
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
        """  Corresponds to IDD Field `Schedule Name`

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
                                 ' for field `SurfaceControlMovableInsulation.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceControlMovableInsulation.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceControlMovableInsulation.schedule_name`')
        self._data["Schedule Name"] = value

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
                    raise ValueError("Required field SurfaceControlMovableInsulation:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceControlMovableInsulation:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceControlMovableInsulation: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceControlMovableInsulation: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyOtherSideCoefficients(object):
    """ Corresponds to IDD object `SurfaceProperty:OtherSideCoefficients`
        This object sets the other side conditions for a surface in a variety of ways.
    """
    internal_name = "SurfaceProperty:OtherSideCoefficients"
    field_count = 14
    required_fields = ["Name", "Combined Convective/Radiative Film Coefficient"]
    extensible_fields = 0
    format = None
    min_fields = 8
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:OtherSideCoefficients`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Combined Convective/Radiative Film Coefficient"] = None
        self._data["Constant Temperature"] = None
        self._data["Constant Temperature Coefficient"] = None
        self._data["External Dry-Bulb Temperature Coefficient"] = None
        self._data["Ground Temperature Coefficient"] = None
        self._data["Wind Speed Coefficient"] = None
        self._data["Zone Air Temperature Coefficient"] = None
        self._data["Constant Temperature Schedule Name"] = None
        self._data["Sinusoidal Variation of Constant Temperature Coefficient"] = None
        self._data["Period of Sinusoidal Variation"] = None
        self._data["Previous Other Side Temperature Coefficient"] = None
        self._data["Minimum Other Side Temperature Limit"] = None
        self._data["Maximum Other Side Temperature Limit"] = None
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
            self.combined_convective_or_radiative_film_coefficient = None
        else:
            self.combined_convective_or_radiative_film_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_temperature = None
        else:
            self.constant_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_temperature_coefficient = None
        else:
            self.constant_temperature_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.external_drybulb_temperature_coefficient = None
        else:
            self.external_drybulb_temperature_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ground_temperature_coefficient = None
        else:
            self.ground_temperature_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_speed_coefficient = None
        else:
            self.wind_speed_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_air_temperature_coefficient = None
        else:
            self.zone_air_temperature_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_temperature_schedule_name = None
        else:
            self.constant_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sinusoidal_variation_of_constant_temperature_coefficient = None
        else:
            self.sinusoidal_variation_of_constant_temperature_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.period_of_sinusoidal_variation = None
        else:
            self.period_of_sinusoidal_variation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.previous_other_side_temperature_coefficient = None
        else:
            self.previous_other_side_temperature_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_other_side_temperature_limit = None
        else:
            self.minimum_other_side_temperature_limit = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_other_side_temperature_limit = None
        else:
            self.maximum_other_side_temperature_limit = vals[i]
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyOtherSideCoefficients.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyOtherSideCoefficients.name`')
        self._data["Name"] = value

    @property
    def combined_convective_or_radiative_film_coefficient(self):
        """Get combined_convective_or_radiative_film_coefficient

        Returns:
            float: the value of `combined_convective_or_radiative_film_coefficient` or None if not set
        """
        return self._data["Combined Convective/Radiative Film Coefficient"]

    @combined_convective_or_radiative_film_coefficient.setter
    def combined_convective_or_radiative_film_coefficient(self, value=None):
        """  Corresponds to IDD Field `Combined Convective/Radiative Film Coefficient`
        if>0, this field becomes the exterior convective/radiative film coefficient
        and the other fields are used to calculate the outdoor air temperature
        then exterior surface temperature based on outdoor air and specified coefficient
        if<=0, then remaining fields calculate the outside surface temperature
        The following fields are used in the equation:
        OtherSideTemp=N2*N3 + N4*OutdoorDry-bulb + N5*GroundTemp + N6*WindSpeed*OutdoorDry-bulb + N7*TempZone + N9*TempPrev

        Args:
            value (float): value for IDD Field `Combined Convective/Radiative Film Coefficient`
                Units: W/m2-K
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.combined_convective_or_radiative_film_coefficient`'.format(value))
        self._data["Combined Convective/Radiative Film Coefficient"] = value

    @property
    def constant_temperature(self):
        """Get constant_temperature

        Returns:
            float: the value of `constant_temperature` or None if not set
        """
        return self._data["Constant Temperature"]

    @constant_temperature.setter
    def constant_temperature(self, value=0.0):
        """  Corresponds to IDD Field `Constant Temperature`
        This parameter will be overwritten by the values from the Constant Temperature Schedule Name (below) if one is present

        Args:
            value (float): value for IDD Field `Constant Temperature`
                Units: C
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.constant_temperature`'.format(value))
        self._data["Constant Temperature"] = value

    @property
    def constant_temperature_coefficient(self):
        """Get constant_temperature_coefficient

        Returns:
            float: the value of `constant_temperature_coefficient` or None if not set
        """
        return self._data["Constant Temperature Coefficient"]

    @constant_temperature_coefficient.setter
    def constant_temperature_coefficient(self, value=1.0):
        """  Corresponds to IDD Field `Constant Temperature Coefficient`
        This coefficient is used even with a Schedule.  It should normally be 1.0 in that case.
        This field is ignored if Sinusoidal Variation of Constant Temperature Coefficient = Yes.

        Args:
            value (float): value for IDD Field `Constant Temperature Coefficient`
                Default value: 1.0
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.constant_temperature_coefficient`'.format(value))
        self._data["Constant Temperature Coefficient"] = value

    @property
    def external_drybulb_temperature_coefficient(self):
        """Get external_drybulb_temperature_coefficient

        Returns:
            float: the value of `external_drybulb_temperature_coefficient` or None if not set
        """
        return self._data["External Dry-Bulb Temperature Coefficient"]

    @external_drybulb_temperature_coefficient.setter
    def external_drybulb_temperature_coefficient(self, value=0.0):
        """  Corresponds to IDD Field `External Dry-Bulb Temperature Coefficient`

        Args:
            value (float): value for IDD Field `External Dry-Bulb Temperature Coefficient`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.external_drybulb_temperature_coefficient`'.format(value))
        self._data["External Dry-Bulb Temperature Coefficient"] = value

    @property
    def ground_temperature_coefficient(self):
        """Get ground_temperature_coefficient

        Returns:
            float: the value of `ground_temperature_coefficient` or None if not set
        """
        return self._data["Ground Temperature Coefficient"]

    @ground_temperature_coefficient.setter
    def ground_temperature_coefficient(self, value=0.0):
        """  Corresponds to IDD Field `Ground Temperature Coefficient`

        Args:
            value (float): value for IDD Field `Ground Temperature Coefficient`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.ground_temperature_coefficient`'.format(value))
        self._data["Ground Temperature Coefficient"] = value

    @property
    def wind_speed_coefficient(self):
        """Get wind_speed_coefficient

        Returns:
            float: the value of `wind_speed_coefficient` or None if not set
        """
        return self._data["Wind Speed Coefficient"]

    @wind_speed_coefficient.setter
    def wind_speed_coefficient(self, value=0.0):
        """  Corresponds to IDD Field `Wind Speed Coefficient`

        Args:
            value (float): value for IDD Field `Wind Speed Coefficient`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.wind_speed_coefficient`'.format(value))
        self._data["Wind Speed Coefficient"] = value

    @property
    def zone_air_temperature_coefficient(self):
        """Get zone_air_temperature_coefficient

        Returns:
            float: the value of `zone_air_temperature_coefficient` or None if not set
        """
        return self._data["Zone Air Temperature Coefficient"]

    @zone_air_temperature_coefficient.setter
    def zone_air_temperature_coefficient(self, value=0.0):
        """  Corresponds to IDD Field `Zone Air Temperature Coefficient`

        Args:
            value (float): value for IDD Field `Zone Air Temperature Coefficient`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.zone_air_temperature_coefficient`'.format(value))
        self._data["Zone Air Temperature Coefficient"] = value

    @property
    def constant_temperature_schedule_name(self):
        """Get constant_temperature_schedule_name

        Returns:
            str: the value of `constant_temperature_schedule_name` or None if not set
        """
        return self._data["Constant Temperature Schedule Name"]

    @constant_temperature_schedule_name.setter
    def constant_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Constant Temperature Schedule Name`
        Name of schedule for values of constant temperature.
        Schedule values replace any value specified in the field Constant Temperature.

        Args:
            value (str): value for IDD Field `Constant Temperature Schedule Name`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.constant_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyOtherSideCoefficients.constant_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyOtherSideCoefficients.constant_temperature_schedule_name`')
        self._data["Constant Temperature Schedule Name"] = value

    @property
    def sinusoidal_variation_of_constant_temperature_coefficient(self):
        """Get sinusoidal_variation_of_constant_temperature_coefficient

        Returns:
            str: the value of `sinusoidal_variation_of_constant_temperature_coefficient` or None if not set
        """
        return self._data["Sinusoidal Variation of Constant Temperature Coefficient"]

    @sinusoidal_variation_of_constant_temperature_coefficient.setter
    def sinusoidal_variation_of_constant_temperature_coefficient(self, value="No"):
        """  Corresponds to IDD Field `Sinusoidal Variation of Constant Temperature Coefficient`
        Optionally used to vary Constant Temperature Coefficient with unitary sine wave

        Args:
            value (str): value for IDD Field `Sinusoidal Variation of Constant Temperature Coefficient`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.sinusoidal_variation_of_constant_temperature_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyOtherSideCoefficients.sinusoidal_variation_of_constant_temperature_coefficient`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyOtherSideCoefficients.sinusoidal_variation_of_constant_temperature_coefficient`')
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
                                     'field `SurfacePropertyOtherSideCoefficients.sinusoidal_variation_of_constant_temperature_coefficient`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyOtherSideCoefficients.sinusoidal_variation_of_constant_temperature_coefficient`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sinusoidal Variation of Constant Temperature Coefficient"] = value

    @property
    def period_of_sinusoidal_variation(self):
        """Get period_of_sinusoidal_variation

        Returns:
            float: the value of `period_of_sinusoidal_variation` or None if not set
        """
        return self._data["Period of Sinusoidal Variation"]

    @period_of_sinusoidal_variation.setter
    def period_of_sinusoidal_variation(self, value=24.0):
        """  Corresponds to IDD Field `Period of Sinusoidal Variation`
        Use with sinusoidal variation to define the time period

        Args:
            value (float): value for IDD Field `Period of Sinusoidal Variation`
                Units: hr
                Default value: 24.0
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.period_of_sinusoidal_variation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SurfacePropertyOtherSideCoefficients.period_of_sinusoidal_variation`')
        self._data["Period of Sinusoidal Variation"] = value

    @property
    def previous_other_side_temperature_coefficient(self):
        """Get previous_other_side_temperature_coefficient

        Returns:
            float: the value of `previous_other_side_temperature_coefficient` or None if not set
        """
        return self._data["Previous Other Side Temperature Coefficient"]

    @previous_other_side_temperature_coefficient.setter
    def previous_other_side_temperature_coefficient(self, value=0.0):
        """  Corresponds to IDD Field `Previous Other Side Temperature Coefficient`
        This coefficient multiplies the other side temperature result from the
        previous zone timestep

        Args:
            value (float): value for IDD Field `Previous Other Side Temperature Coefficient`
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.previous_other_side_temperature_coefficient`'.format(value))
        self._data["Previous Other Side Temperature Coefficient"] = value

    @property
    def minimum_other_side_temperature_limit(self):
        """Get minimum_other_side_temperature_limit

        Returns:
            float: the value of `minimum_other_side_temperature_limit` or None if not set
        """
        return self._data["Minimum Other Side Temperature Limit"]

    @minimum_other_side_temperature_limit.setter
    def minimum_other_side_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `Minimum Other Side Temperature Limit`
        This field specifies a lower limit for the other side temperature result.
        Blank indicates no limit

        Args:
            value (float): value for IDD Field `Minimum Other Side Temperature Limit`
                Units: C
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.minimum_other_side_temperature_limit`'.format(value))
        self._data["Minimum Other Side Temperature Limit"] = value

    @property
    def maximum_other_side_temperature_limit(self):
        """Get maximum_other_side_temperature_limit

        Returns:
            float: the value of `maximum_other_side_temperature_limit` or None if not set
        """
        return self._data["Maximum Other Side Temperature Limit"]

    @maximum_other_side_temperature_limit.setter
    def maximum_other_side_temperature_limit(self, value=None):
        """  Corresponds to IDD Field `Maximum Other Side Temperature Limit`
        This field specifies an upper limit for the other side temperature result.
        Blank indicates no limit

        Args:
            value (float): value for IDD Field `Maximum Other Side Temperature Limit`
                Units: C
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
                                 ' for field `SurfacePropertyOtherSideCoefficients.maximum_other_side_temperature_limit`'.format(value))
        self._data["Maximum Other Side Temperature Limit"] = value

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
                    raise ValueError("Required field SurfacePropertyOtherSideCoefficients:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyOtherSideCoefficients:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyOtherSideCoefficients: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyOtherSideCoefficients: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyOtherSideConditionsModel(object):
    """ Corresponds to IDD object `SurfaceProperty:OtherSideConditionsModel`
        This object sets up modifying the other side conditions for a surface from other model results.
    """
    internal_name = "SurfaceProperty:OtherSideConditionsModel"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:OtherSideConditionsModel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Type of Modeling"] = None
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
            self.type_of_modeling = None
        else:
            self.type_of_modeling = vals[i]
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
                                 ' for field `SurfacePropertyOtherSideConditionsModel.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyOtherSideConditionsModel.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyOtherSideConditionsModel.name`')
        self._data["Name"] = value

    @property
    def type_of_modeling(self):
        """Get type_of_modeling

        Returns:
            str: the value of `type_of_modeling` or None if not set
        """
        return self._data["Type of Modeling"]

    @type_of_modeling.setter
    def type_of_modeling(self, value="GapConvectionRadiation"):
        """  Corresponds to IDD Field `Type of Modeling`
        GapConvectionRadiation provides boundary conditions for convection
        and linearized thermal radiation across a gap or cavity
        on the other side of the surface that are modeled sperately.
        UndergroundPipingSystemSurface provides boundary conditions for
        surfaces in contact with PipingSystem:Underground domains
        GroundCoupledSurface provides boundary conditions for surfaces
        in contact with GroundDomain objects

        Args:
            value (str): value for IDD Field `Type of Modeling`
                Accepted values are:
                      - GapConvectionRadiation
                      - UndergroundPipingSystemSurface
                      - GroundCoupledSurface
                Default value: GapConvectionRadiation
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
                                 ' for field `SurfacePropertyOtherSideConditionsModel.type_of_modeling`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyOtherSideConditionsModel.type_of_modeling`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyOtherSideConditionsModel.type_of_modeling`')
            vals = {}
            vals["gapconvectionradiation"] = "GapConvectionRadiation"
            vals["undergroundpipingsystemsurface"] = "UndergroundPipingSystemSurface"
            vals["groundcoupledsurface"] = "GroundCoupledSurface"
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
                                     'field `SurfacePropertyOtherSideConditionsModel.type_of_modeling`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyOtherSideConditionsModel.type_of_modeling`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Type of Modeling"] = value

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
                    raise ValueError("Required field SurfacePropertyOtherSideConditionsModel:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyOtherSideConditionsModel:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyOtherSideConditionsModel: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyOtherSideConditionsModel: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfaceConvectionAlgorithmInsideAdaptiveModelSelections(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the inside face, the side of the surface facing a thermal zone.
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections"
    field_count = 91
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Simple Bouyancy Vertical Wall Equation Source"] = None
        self._data["Simple Bouyancy Vertical Wall User Curve Name"] = None
        self._data["Simple Bouyancy Stable Horizontal Equation Source"] = None
        self._data["Simple Bouyancy Stable Horizontal Equation User Curve Name"] = None
        self._data["Simple Bouyancy Unstable Horizontal Equation Source"] = None
        self._data["Simple Bouyancy Unstable Horizontal Equation User Curve Name"] = None
        self._data["Simple Bouyancy Stable Tilted Equation Source"] = None
        self._data["Simple Bouyancy Stable Tilted Equation User Curve Name"] = None
        self._data["Simple Bouyancy Unstable Tilted Equation Source"] = None
        self._data["Simple Bouyancy Unstable Tilted Equation User Curve Name"] = None
        self._data["Simple Bouyancy Windows Equation Source"] = None
        self._data["Simple Bouyancy Windows Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Vertical Wall Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Heated Floor Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Stable Tilted Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"] = None
        self._data["Floor Heat Ceiling Cool Window Equation Source"] = None
        self._data["Floor Heat Ceiling Cool Window Equation User Curve Name"] = None
        self._data["Wall Panel Heating Vertical Wall Equation Source"] = None
        self._data["Wall Panel Heating Vertical Wall Equation User Curve Name"] = None
        self._data["Wall Panel Heating Heated Wall Equation Source"] = None
        self._data["Wall Panel Heating Heated Wall Equation User Curve Name"] = None
        self._data["Wall Panel Heating Stable Horizontal Equation Source"] = None
        self._data["Wall Panel Heating Stable Horizontal Equation User Curve Name"] = None
        self._data["Wall Panel Heating Unstable Horizontal Equation Source"] = None
        self._data["Wall Panel Heating Unstable Horizontal Equation User Curve Name"] = None
        self._data["Wall Panel Heating Stable Tilted Equation Source"] = None
        self._data["Wall Panel Heating Stable Tilted Equation User Curve Name"] = None
        self._data["Wall Panel Heating Unstable Tilted Equation Source"] = None
        self._data["Wall Panel Heating Unstable Tilted Equation User Curve Name"] = None
        self._data["Wall Panel Heating Window Equation Source"] = None
        self._data["Wall Panel Heating Window Equation User Curve Name"] = None
        self._data["Convective Zone Heater Vertical Wall Equation Source"] = None
        self._data["Convective Zone Heater Vertical Wall Equation User Curve Name"] = None
        self._data["Convective Zone Heater Vertical Walls Near Heater Equation Source"] = None
        self._data["Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"] = None
        self._data["Convective Zone Heater Stable Horizontal Equation Source"] = None
        self._data["Convective Zone Heater Stable Horizontal Equation User Curve Name"] = None
        self._data["Convective Zone Heater Unstable Horizontal Equation Source"] = None
        self._data["Convective Zone Heater Unstable Horizontal Equation User Curve Name"] = None
        self._data["Convective Zone Heater Stable Tilted Equation Source"] = None
        self._data["Convective Zone Heater Stable Tilted Equation User Curve Name"] = None
        self._data["Convective Zone Heater Unstable Tilted Equation Source"] = None
        self._data["Convective Zone Heater Unstable Tilted Equation User Curve Name"] = None
        self._data["Convective Zone Heater Windows Equation Source"] = None
        self._data["Convective Zone Heater Windows Equation User Curve Name"] = None
        self._data["Central Air Diffuser Wall Equation Source"] = None
        self._data["Central Air Diffuser Wall Equation User Curve Name"] = None
        self._data["Central Air Diffuser Ceiling Equation Source"] = None
        self._data["Central Air Diffuser Ceiling Equation User Curve Name"] = None
        self._data["Central Air Diffuser Floor Equation Source"] = None
        self._data["Central Air Diffuser Floor Equation User Curve Name"] = None
        self._data["Central Air Diffuser Window Equation Source"] = None
        self._data["Central Air Diffuser Window Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"] = None
        self._data["Mechanical Zone Fan Circulation Window Equation Source"] = None
        self._data["Mechanical Zone Fan Circulation Window Equation User Curve Name"] = None
        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation Source"] = None
        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name"] = None
        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source"] = None
        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name"] = None
        self._data["Mixed Regime Stable Floor Equation Source"] = None
        self._data["Mixed Regime Stable Floor Equation User Curve Name"] = None
        self._data["Mixed Regime Unstable Floor Equation Source"] = None
        self._data["Mixed Regime Unstable Floor Equation User Curve Name"] = None
        self._data["Mixed Regime Stable Ceiling Equation Source"] = None
        self._data["Mixed Regime Stable Ceiling Equation User Curve Name"] = None
        self._data["Mixed Regime Unstable Ceiling Equation Source"] = None
        self._data["Mixed Regime Unstable Ceiling Equation User Curve Name"] = None
        self._data["Mixed Regime Window Equation Source"] = None
        self._data["Mixed Regime Window Equation User Curve Name"] = None
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
            self.simple_bouyancy_vertical_wall_equation_source = None
        else:
            self.simple_bouyancy_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_vertical_wall_user_curve_name = None
        else:
            self.simple_bouyancy_vertical_wall_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_horizontal_equation_source = None
        else:
            self.simple_bouyancy_stable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_horizontal_equation_user_curve_name = None
        else:
            self.simple_bouyancy_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_horizontal_equation_source = None
        else:
            self.simple_bouyancy_unstable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_horizontal_equation_user_curve_name = None
        else:
            self.simple_bouyancy_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_tilted_equation_source = None
        else:
            self.simple_bouyancy_stable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_tilted_equation_user_curve_name = None
        else:
            self.simple_bouyancy_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_tilted_equation_source = None
        else:
            self.simple_bouyancy_unstable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_tilted_equation_user_curve_name = None
        else:
            self.simple_bouyancy_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_windows_equation_source = None
        else:
            self.simple_bouyancy_windows_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.simple_bouyancy_windows_equation_user_curve_name = None
        else:
            self.simple_bouyancy_windows_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_vertical_wall_equation_source = None
        else:
            self.floor_heat_ceiling_cool_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_source = None
        else:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_source = None
        else:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_heated_floor_equation_source = None
        else:
            self.floor_heat_ceiling_cool_heated_floor_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_source = None
        else:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_tilted_equation_source = None
        else:
            self.floor_heat_ceiling_cool_stable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_source = None
        else:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_window_equation_source = None
        else:
            self.floor_heat_ceiling_cool_window_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_window_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_window_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_vertical_wall_equation_source = None
        else:
            self.wall_panel_heating_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_vertical_wall_equation_user_curve_name = None
        else:
            self.wall_panel_heating_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_heated_wall_equation_source = None
        else:
            self.wall_panel_heating_heated_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_heated_wall_equation_user_curve_name = None
        else:
            self.wall_panel_heating_heated_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_horizontal_equation_source = None
        else:
            self.wall_panel_heating_stable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_horizontal_equation_user_curve_name = None
        else:
            self.wall_panel_heating_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_horizontal_equation_source = None
        else:
            self.wall_panel_heating_unstable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_horizontal_equation_user_curve_name = None
        else:
            self.wall_panel_heating_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_tilted_equation_source = None
        else:
            self.wall_panel_heating_stable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_tilted_equation_user_curve_name = None
        else:
            self.wall_panel_heating_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_tilted_equation_source = None
        else:
            self.wall_panel_heating_unstable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_tilted_equation_user_curve_name = None
        else:
            self.wall_panel_heating_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_window_equation_source = None
        else:
            self.wall_panel_heating_window_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wall_panel_heating_window_equation_user_curve_name = None
        else:
            self.wall_panel_heating_window_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_wall_equation_source = None
        else:
            self.convective_zone_heater_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_wall_equation_user_curve_name = None
        else:
            self.convective_zone_heater_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_walls_near_heater_equation_source = None
        else:
            self.convective_zone_heater_vertical_walls_near_heater_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = None
        else:
            self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_horizontal_equation_source = None
        else:
            self.convective_zone_heater_stable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_horizontal_equation_user_curve_name = None
        else:
            self.convective_zone_heater_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_horizontal_equation_source = None
        else:
            self.convective_zone_heater_unstable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_horizontal_equation_user_curve_name = None
        else:
            self.convective_zone_heater_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_tilted_equation_source = None
        else:
            self.convective_zone_heater_stable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_tilted_equation_user_curve_name = None
        else:
            self.convective_zone_heater_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_tilted_equation_source = None
        else:
            self.convective_zone_heater_unstable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_tilted_equation_user_curve_name = None
        else:
            self.convective_zone_heater_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_windows_equation_source = None
        else:
            self.convective_zone_heater_windows_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convective_zone_heater_windows_equation_user_curve_name = None
        else:
            self.convective_zone_heater_windows_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_wall_equation_source = None
        else:
            self.central_air_diffuser_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_wall_equation_user_curve_name = None
        else:
            self.central_air_diffuser_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_ceiling_equation_source = None
        else:
            self.central_air_diffuser_ceiling_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_ceiling_equation_user_curve_name = None
        else:
            self.central_air_diffuser_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_floor_equation_source = None
        else:
            self.central_air_diffuser_floor_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_floor_equation_user_curve_name = None
        else:
            self.central_air_diffuser_floor_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_window_equation_source = None
        else:
            self.central_air_diffuser_window_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_air_diffuser_window_equation_user_curve_name = None
        else:
            self.central_air_diffuser_window_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_window_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_window_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_window_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_window_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source = None
        else:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name = None
        else:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source = None
        else:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name = None
        else:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_stable_floor_equation_source = None
        else:
            self.mixed_regime_stable_floor_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_stable_floor_equation_user_curve_name = None
        else:
            self.mixed_regime_stable_floor_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_floor_equation_source = None
        else:
            self.mixed_regime_unstable_floor_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_floor_equation_user_curve_name = None
        else:
            self.mixed_regime_unstable_floor_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_stable_ceiling_equation_source = None
        else:
            self.mixed_regime_stable_ceiling_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_stable_ceiling_equation_user_curve_name = None
        else:
            self.mixed_regime_stable_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_ceiling_equation_source = None
        else:
            self.mixed_regime_unstable_ceiling_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_ceiling_equation_user_curve_name = None
        else:
            self.mixed_regime_unstable_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_window_equation_source = None
        else:
            self.mixed_regime_window_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.mixed_regime_window_equation_user_curve_name = None
        else:
            self.mixed_regime_window_equation_user_curve_name = vals[i]
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.name`')
        self._data["Name"] = value

    @property
    def simple_bouyancy_vertical_wall_equation_source(self):
        """Get simple_bouyancy_vertical_wall_equation_source

        Returns:
            str: the value of `simple_bouyancy_vertical_wall_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Vertical Wall Equation Source"]

    @simple_bouyancy_vertical_wall_equation_source.setter
    def simple_bouyancy_vertical_wall_equation_source(self, value="FohannoPolidoriVerticalWall"):
        """  Corresponds to IDD Field `Simple Bouyancy Vertical Wall Equation Source`
        Applies to zone with no HVAC or when HVAC is off
        This is for vertical walls

        Args:
            value (str): value for IDD Field `Simple Bouyancy Vertical Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq6NonHeatedWalls
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: FohannoPolidoriVerticalWall
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Simple Bouyancy Vertical Wall Equation Source"] = value

    @property
    def simple_bouyancy_vertical_wall_user_curve_name(self):
        """Get simple_bouyancy_vertical_wall_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_vertical_wall_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Vertical Wall User Curve Name"]

    @simple_bouyancy_vertical_wall_user_curve_name.setter
    def simple_bouyancy_vertical_wall_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Simple Bouyancy Vertical Wall User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Bouyancy Vertical Wall User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_vertical_wall_user_curve_name`')
        self._data["Simple Bouyancy Vertical Wall User Curve Name"] = value

    @property
    def simple_bouyancy_stable_horizontal_equation_source(self):
        """Get simple_bouyancy_stable_horizontal_equation_source

        Returns:
            str: the value of `simple_bouyancy_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Stable Horizontal Equation Source"]

    @simple_bouyancy_stable_horizontal_equation_source.setter
    def simple_bouyancy_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `Simple Bouyancy Stable Horizontal Equation Source`
        Applies to zone with no HVAC or when HVAC is off
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `Simple Bouyancy Stable Horizontal Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Simple Bouyancy Stable Horizontal Equation Source"] = value

    @property
    def simple_bouyancy_stable_horizontal_equation_user_curve_name(self):
        """Get simple_bouyancy_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Stable Horizontal Equation User Curve Name"]

    @simple_bouyancy_stable_horizontal_equation_user_curve_name.setter
    def simple_bouyancy_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Simple Bouyancy Stable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Bouyancy Stable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_horizontal_equation_user_curve_name`')
        self._data["Simple Bouyancy Stable Horizontal Equation User Curve Name"] = value

    @property
    def simple_bouyancy_unstable_horizontal_equation_source(self):
        """Get simple_bouyancy_unstable_horizontal_equation_source

        Returns:
            str: the value of `simple_bouyancy_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Horizontal Equation Source"]

    @simple_bouyancy_unstable_horizontal_equation_source.setter
    def simple_bouyancy_unstable_horizontal_equation_source(self, value="AlamdariHammondUnstableHorizontal"):
        """  Corresponds to IDD Field `Simple Bouyancy Unstable Horizontal Equation Source`
        Applies to zone with no HVAC or when HVAC is off
        This is for passive horizontal surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Simple Bouyancy Unstable Horizontal Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: AlamdariHammondUnstableHorizontal
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Simple Bouyancy Unstable Horizontal Equation Source"] = value

    @property
    def simple_bouyancy_unstable_horizontal_equation_user_curve_name(self):
        """Get simple_bouyancy_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Horizontal Equation User Curve Name"]

    @simple_bouyancy_unstable_horizontal_equation_user_curve_name.setter
    def simple_bouyancy_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Simple Bouyancy Unstable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Bouyancy Unstable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_horizontal_equation_user_curve_name`')
        self._data["Simple Bouyancy Unstable Horizontal Equation User Curve Name"] = value

    @property
    def simple_bouyancy_stable_tilted_equation_source(self):
        """Get simple_bouyancy_stable_tilted_equation_source

        Returns:
            str: the value of `simple_bouyancy_stable_tilted_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Stable Tilted Equation Source"]

    @simple_bouyancy_stable_tilted_equation_source.setter
    def simple_bouyancy_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Simple Bouyancy Stable Tilted Equation Source`
        Applies to zone with no HVAC or when HVAC is off
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `Simple Bouyancy Stable Tilted Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Simple Bouyancy Stable Tilted Equation Source"] = value

    @property
    def simple_bouyancy_stable_tilted_equation_user_curve_name(self):
        """Get simple_bouyancy_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Stable Tilted Equation User Curve Name"]

    @simple_bouyancy_stable_tilted_equation_user_curve_name.setter
    def simple_bouyancy_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Simple Bouyancy Stable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Bouyancy Stable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_stable_tilted_equation_user_curve_name`')
        self._data["Simple Bouyancy Stable Tilted Equation User Curve Name"] = value

    @property
    def simple_bouyancy_unstable_tilted_equation_source(self):
        """Get simple_bouyancy_unstable_tilted_equation_source

        Returns:
            str: the value of `simple_bouyancy_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Tilted Equation Source"]

    @simple_bouyancy_unstable_tilted_equation_source.setter
    def simple_bouyancy_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Simple Bouyancy Unstable Tilted Equation Source`
        Applies to zone with no HVAC or when HVAC is off
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Simple Bouyancy Unstable Tilted Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Simple Bouyancy Unstable Tilted Equation Source"] = value

    @property
    def simple_bouyancy_unstable_tilted_equation_user_curve_name(self):
        """Get simple_bouyancy_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Unstable Tilted Equation User Curve Name"]

    @simple_bouyancy_unstable_tilted_equation_user_curve_name.setter
    def simple_bouyancy_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Simple Bouyancy Unstable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Bouyancy Unstable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_unstable_tilted_equation_user_curve_name`')
        self._data["Simple Bouyancy Unstable Tilted Equation User Curve Name"] = value

    @property
    def simple_bouyancy_windows_equation_source(self):
        """Get simple_bouyancy_windows_equation_source

        Returns:
            str: the value of `simple_bouyancy_windows_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Windows Equation Source"]

    @simple_bouyancy_windows_equation_source.setter
    def simple_bouyancy_windows_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `Simple Bouyancy Windows Equation Source`
        Applies to zone with no HVAC or when HVAC is off
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `Simple Bouyancy Windows Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - KaradagChilledCeiling
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Simple Bouyancy Windows Equation Source"] = value

    @property
    def simple_bouyancy_windows_equation_user_curve_name(self):
        """Get simple_bouyancy_windows_equation_user_curve_name

        Returns:
            str: the value of `simple_bouyancy_windows_equation_user_curve_name` or None if not set
        """
        return self._data["Simple Bouyancy Windows Equation User Curve Name"]

    @simple_bouyancy_windows_equation_user_curve_name.setter
    def simple_bouyancy_windows_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Simple Bouyancy Windows Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Simple Bouyancy Windows Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.simple_bouyancy_windows_equation_user_curve_name`')
        self._data["Simple Bouyancy Windows Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_vertical_wall_equation_source(self):
        """Get floor_heat_ceiling_cool_vertical_wall_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_vertical_wall_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Vertical Wall Equation Source"]

    @floor_heat_ceiling_cool_vertical_wall_equation_source.setter
    def floor_heat_ceiling_cool_vertical_wall_equation_source(self, value="KhalifaEq3WallAwayFromHeat"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Vertical Wall Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for vertical walls

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Vertical Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: KhalifaEq3WallAwayFromHeat
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Vertical Wall Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"]

    @floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Vertical Wall Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_stable_horizontal_equation_source(self):
        """Get floor_heat_ceiling_cool_stable_horizontal_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Horizontal Equation Source"]

    @floor_heat_ceiling_cool_stable_horizontal_equation_source.setter
    def floor_heat_ceiling_cool_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Stable Horizontal Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for passive horizontal surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Horizontal Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"]

    @floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Stable Horizontal Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_unstable_horizontal_equation_source(self):
        """Get floor_heat_ceiling_cool_unstable_horizontal_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation Source"]

    @floor_heat_ceiling_cool_unstable_horizontal_equation_source.setter
    def floor_heat_ceiling_cool_unstable_horizontal_equation_source(self, value="KhalifaEq4CeilingAwayFromHeat"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Unstable Horizontal Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for passive horizontal surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Horizontal Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KhalifaEq4CeilingAwayFromHeat
                      - UserCurve
                Default value: KhalifaEq4CeilingAwayFromHeat
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"]

    @floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Unstable Horizontal Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_heated_floor_equation_source(self):
        """Get floor_heat_ceiling_cool_heated_floor_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_heated_floor_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Heated Floor Equation Source"]

    @floor_heat_ceiling_cool_heated_floor_equation_source.setter
    def floor_heat_ceiling_cool_heated_floor_equation_source(self, value="AwbiHattonHeatedFloor"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Heated Floor Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for a floor with active heating elements

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Heated Floor Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - AwbiHattonHeatedFloor
                      - UserCurve
                Default value: AwbiHattonHeatedFloor
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["awbihattonheatedfloor"] = "AwbiHattonHeatedFloor"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Heated Floor Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_heated_floor_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_heated_floor_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"]

    @floor_heat_ceiling_cool_heated_floor_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_heated_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Heated Floor Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Heated Floor Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Heated Floor Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_chilled_ceiling_equation_source(self):
        """Get floor_heat_ceiling_cool_chilled_ceiling_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_chilled_ceiling_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"]

    @floor_heat_ceiling_cool_chilled_ceiling_equation_source.setter
    def floor_heat_ceiling_cool_chilled_ceiling_equation_source(self, value="KaradagChilledCeiling"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Chilled Ceiling Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for a ceiling with active cooling elements

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Chilled Ceiling Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KaradagChilledCeiling
                      - UserCurve
                Default value: KaradagChilledCeiling
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"]

    @floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Chilled Ceiling Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_stable_tilted_equation_source(self):
        """Get floor_heat_ceiling_cool_stable_tilted_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_tilted_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Tilted Equation Source"]

    @floor_heat_ceiling_cool_stable_tilted_equation_source.setter
    def floor_heat_ceiling_cool_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Stable Tilted Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Tilted Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Stable Tilted Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"]

    @floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Stable Tilted Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_unstable_tilted_equation_source(self):
        """Get floor_heat_ceiling_cool_unstable_tilted_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Tilted Equation Source"]

    @floor_heat_ceiling_cool_unstable_tilted_equation_source.setter
    def floor_heat_ceiling_cool_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Unstable Tilted Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Tilted Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"]

    @floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Unstable Tilted Equation User Curve Name"] = value

    @property
    def floor_heat_ceiling_cool_window_equation_source(self):
        """Get floor_heat_ceiling_cool_window_equation_source

        Returns:
            str: the value of `floor_heat_ceiling_cool_window_equation_source` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Window Equation Source"]

    @floor_heat_ceiling_cool_window_equation_source.setter
    def floor_heat_ceiling_cool_window_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Window Equation Source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Window Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Floor Heat Ceiling Cool Window Equation Source"] = value

    @property
    def floor_heat_ceiling_cool_window_equation_user_curve_name(self):
        """Get floor_heat_ceiling_cool_window_equation_user_curve_name

        Returns:
            str: the value of `floor_heat_ceiling_cool_window_equation_user_curve_name` or None if not set
        """
        return self._data["Floor Heat Ceiling Cool Window Equation User Curve Name"]

    @floor_heat_ceiling_cool_window_equation_user_curve_name.setter
    def floor_heat_ceiling_cool_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Floor Heat Ceiling Cool Window Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Floor Heat Ceiling Cool Window Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.floor_heat_ceiling_cool_window_equation_user_curve_name`')
        self._data["Floor Heat Ceiling Cool Window Equation User Curve Name"] = value

    @property
    def wall_panel_heating_vertical_wall_equation_source(self):
        """Get wall_panel_heating_vertical_wall_equation_source

        Returns:
            str: the value of `wall_panel_heating_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Vertical Wall Equation Source"]

    @wall_panel_heating_vertical_wall_equation_source.setter
    def wall_panel_heating_vertical_wall_equation_source(self, value="KhalifaEq6NonHeatedWalls"):
        """  Corresponds to IDD Field `Wall Panel Heating Vertical Wall Equation Source`
        Applies to zone with in-wall panel heating
        This is for vertical walls that are not actively heated

        Args:
            value (str): value for IDD Field `Wall Panel Heating Vertical Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq6NonHeatedWalls
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: KhalifaEq6NonHeatedWalls
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Vertical Wall Equation Source"] = value

    @property
    def wall_panel_heating_vertical_wall_equation_user_curve_name(self):
        """Get wall_panel_heating_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Vertical Wall Equation User Curve Name"]

    @wall_panel_heating_vertical_wall_equation_user_curve_name.setter
    def wall_panel_heating_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Vertical Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Vertical Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_vertical_wall_equation_user_curve_name`')
        self._data["Wall Panel Heating Vertical Wall Equation User Curve Name"] = value

    @property
    def wall_panel_heating_heated_wall_equation_source(self):
        """Get wall_panel_heating_heated_wall_equation_source

        Returns:
            str: the value of `wall_panel_heating_heated_wall_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Heated Wall Equation Source"]

    @wall_panel_heating_heated_wall_equation_source.setter
    def wall_panel_heating_heated_wall_equation_source(self, value="AwbiHattonHeatedWall"):
        """  Corresponds to IDD Field `Wall Panel Heating Heated Wall Equation Source`
        Applies to zone with in-wall panel heating
        This is for vertical walls that are being actively heated

        Args:
            value (str): value for IDD Field `Wall Panel Heating Heated Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq5WallNearHeat
                      - AwbiHattonHeatedWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: AwbiHattonHeatedWall
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq5wallnearheat"] = "KhalifaEq5WallNearHeat"
            vals["awbihattonheatedwall"] = "AwbiHattonHeatedWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Heated Wall Equation Source"] = value

    @property
    def wall_panel_heating_heated_wall_equation_user_curve_name(self):
        """Get wall_panel_heating_heated_wall_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_heated_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Heated Wall Equation User Curve Name"]

    @wall_panel_heating_heated_wall_equation_user_curve_name.setter
    def wall_panel_heating_heated_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Heated Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Heated Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_heated_wall_equation_user_curve_name`')
        self._data["Wall Panel Heating Heated Wall Equation User Curve Name"] = value

    @property
    def wall_panel_heating_stable_horizontal_equation_source(self):
        """Get wall_panel_heating_stable_horizontal_equation_source

        Returns:
            str: the value of `wall_panel_heating_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Stable Horizontal Equation Source"]

    @wall_panel_heating_stable_horizontal_equation_source.setter
    def wall_panel_heating_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `Wall Panel Heating Stable Horizontal Equation Source`
        Applies to zone with in-wall panel heating
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Horizontal Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Stable Horizontal Equation Source"] = value

    @property
    def wall_panel_heating_stable_horizontal_equation_user_curve_name(self):
        """Get wall_panel_heating_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Stable Horizontal Equation User Curve Name"]

    @wall_panel_heating_stable_horizontal_equation_user_curve_name.setter
    def wall_panel_heating_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Stable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_horizontal_equation_user_curve_name`')
        self._data["Wall Panel Heating Stable Horizontal Equation User Curve Name"] = value

    @property
    def wall_panel_heating_unstable_horizontal_equation_source(self):
        """Get wall_panel_heating_unstable_horizontal_equation_source

        Returns:
            str: the value of `wall_panel_heating_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Horizontal Equation Source"]

    @wall_panel_heating_unstable_horizontal_equation_source.setter
    def wall_panel_heating_unstable_horizontal_equation_source(self, value="KhalifaEq7Ceiling"):
        """  Corresponds to IDD Field `Wall Panel Heating Unstable Horizontal Equation Source`
        Applies to zone with in-wall panel heating
        This is for horizontal surfaces with heat flow directed for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Horizontal Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KhalifaEq7Ceiling
                      - KaradagChilledCeiling
                      - UserCurve
                Default value: KhalifaEq7Ceiling
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["khalifaeq7ceiling"] = "KhalifaEq7Ceiling"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Unstable Horizontal Equation Source"] = value

    @property
    def wall_panel_heating_unstable_horizontal_equation_user_curve_name(self):
        """Get wall_panel_heating_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Horizontal Equation User Curve Name"]

    @wall_panel_heating_unstable_horizontal_equation_user_curve_name.setter
    def wall_panel_heating_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Unstable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_horizontal_equation_user_curve_name`')
        self._data["Wall Panel Heating Unstable Horizontal Equation User Curve Name"] = value

    @property
    def wall_panel_heating_stable_tilted_equation_source(self):
        """Get wall_panel_heating_stable_tilted_equation_source

        Returns:
            str: the value of `wall_panel_heating_stable_tilted_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Stable Tilted Equation Source"]

    @wall_panel_heating_stable_tilted_equation_source.setter
    def wall_panel_heating_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Wall Panel Heating Stable Tilted Equation Source`
        Applies to zone with in-wall panel heating
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Tilted Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Stable Tilted Equation Source"] = value

    @property
    def wall_panel_heating_stable_tilted_equation_user_curve_name(self):
        """Get wall_panel_heating_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Stable Tilted Equation User Curve Name"]

    @wall_panel_heating_stable_tilted_equation_user_curve_name.setter
    def wall_panel_heating_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Stable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Stable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_stable_tilted_equation_user_curve_name`')
        self._data["Wall Panel Heating Stable Tilted Equation User Curve Name"] = value

    @property
    def wall_panel_heating_unstable_tilted_equation_source(self):
        """Get wall_panel_heating_unstable_tilted_equation_source

        Returns:
            str: the value of `wall_panel_heating_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Tilted Equation Source"]

    @wall_panel_heating_unstable_tilted_equation_source.setter
    def wall_panel_heating_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Wall Panel Heating Unstable Tilted Equation Source`
        Applies to zone with in-wall panel heating
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Tilted Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - ISO15099Windows
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Unstable Tilted Equation Source"] = value

    @property
    def wall_panel_heating_unstable_tilted_equation_user_curve_name(self):
        """Get wall_panel_heating_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Unstable Tilted Equation User Curve Name"]

    @wall_panel_heating_unstable_tilted_equation_user_curve_name.setter
    def wall_panel_heating_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Unstable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Unstable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_unstable_tilted_equation_user_curve_name`')
        self._data["Wall Panel Heating Unstable Tilted Equation User Curve Name"] = value

    @property
    def wall_panel_heating_window_equation_source(self):
        """Get wall_panel_heating_window_equation_source

        Returns:
            str: the value of `wall_panel_heating_window_equation_source` or None if not set
        """
        return self._data["Wall Panel Heating Window Equation Source"]

    @wall_panel_heating_window_equation_source.setter
    def wall_panel_heating_window_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `Wall Panel Heating Window Equation Source`
        Applies to zone with in-wall panel heating
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `Wall Panel Heating Window Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wall Panel Heating Window Equation Source"] = value

    @property
    def wall_panel_heating_window_equation_user_curve_name(self):
        """Get wall_panel_heating_window_equation_user_curve_name

        Returns:
            str: the value of `wall_panel_heating_window_equation_user_curve_name` or None if not set
        """
        return self._data["Wall Panel Heating Window Equation User Curve Name"]

    @wall_panel_heating_window_equation_user_curve_name.setter
    def wall_panel_heating_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wall Panel Heating Window Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wall Panel Heating Window Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.wall_panel_heating_window_equation_user_curve_name`')
        self._data["Wall Panel Heating Window Equation User Curve Name"] = value

    @property
    def convective_zone_heater_vertical_wall_equation_source(self):
        """Get convective_zone_heater_vertical_wall_equation_source

        Returns:
            str: the value of `convective_zone_heater_vertical_wall_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Wall Equation Source"]

    @convective_zone_heater_vertical_wall_equation_source.setter
    def convective_zone_heater_vertical_wall_equation_source(self, value="FohannoPolidoriVerticalWall"):
        """  Corresponds to IDD Field `Convective Zone Heater Vertical Wall Equation Source`
        Applies to zone with convective heater
        This is for vertical walls not directly affected by heater

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq6NonHeatedWalls
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: FohannoPolidoriVerticalWall
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Vertical Wall Equation Source"] = value

    @property
    def convective_zone_heater_vertical_wall_equation_user_curve_name(self):
        """Get convective_zone_heater_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Wall Equation User Curve Name"]

    @convective_zone_heater_vertical_wall_equation_user_curve_name.setter
    def convective_zone_heater_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Vertical Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_wall_equation_user_curve_name`')
        self._data["Convective Zone Heater Vertical Wall Equation User Curve Name"] = value

    @property
    def convective_zone_heater_vertical_walls_near_heater_equation_source(self):
        """Get convective_zone_heater_vertical_walls_near_heater_equation_source

        Returns:
            str: the value of `convective_zone_heater_vertical_walls_near_heater_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Walls Near Heater Equation Source"]

    @convective_zone_heater_vertical_walls_near_heater_equation_source.setter
    def convective_zone_heater_vertical_walls_near_heater_equation_source(self, value="KhalifaEq5WallNearHeat"):
        """  Corresponds to IDD Field `Convective Zone Heater Vertical Walls Near Heater Equation Source`
        Applies to zone with convective heater
        This is for vertical walls that are directly affected by heater
        Walls are considered "near" when listed in field set for Fraction of Radiant Energy to Surface

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Walls Near Heater Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq5WallNearHeat
                      - AwbiHattonHeatedWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: KhalifaEq5WallNearHeat
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq5wallnearheat"] = "KhalifaEq5WallNearHeat"
            vals["awbihattonheatedwall"] = "AwbiHattonHeatedWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Vertical Walls Near Heater Equation Source"] = value

    @property
    def convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name(self):
        """Get convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"]

    @convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name.setter
    def convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`')
        self._data["Convective Zone Heater Vertical Walls Near Heater Equation User Curve Name"] = value

    @property
    def convective_zone_heater_stable_horizontal_equation_source(self):
        """Get convective_zone_heater_stable_horizontal_equation_source

        Returns:
            str: the value of `convective_zone_heater_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Stable Horizontal Equation Source"]

    @convective_zone_heater_stable_horizontal_equation_source.setter
    def convective_zone_heater_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `Convective Zone Heater Stable Horizontal Equation Source`
        Applies to zone with convective heater
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Horizontal Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Stable Horizontal Equation Source"] = value

    @property
    def convective_zone_heater_stable_horizontal_equation_user_curve_name(self):
        """Get convective_zone_heater_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Stable Horizontal Equation User Curve Name"]

    @convective_zone_heater_stable_horizontal_equation_user_curve_name.setter
    def convective_zone_heater_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Stable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_horizontal_equation_user_curve_name`')
        self._data["Convective Zone Heater Stable Horizontal Equation User Curve Name"] = value

    @property
    def convective_zone_heater_unstable_horizontal_equation_source(self):
        """Get convective_zone_heater_unstable_horizontal_equation_source

        Returns:
            str: the value of `convective_zone_heater_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Horizontal Equation Source"]

    @convective_zone_heater_unstable_horizontal_equation_source.setter
    def convective_zone_heater_unstable_horizontal_equation_source(self, value="KhalifaEq7Ceiling"):
        """  Corresponds to IDD Field `Convective Zone Heater Unstable Horizontal Equation Source`
        Applies to zone with convective heater
        This is for horizontal surfaces with heat flow directed for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Horizontal Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - KhalifaEq4CeilingAwayFromHeat
                      - KhalifaEq7Ceiling
                      - UserCurve
                Default value: KhalifaEq7Ceiling
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["khalifaeq7ceiling"] = "KhalifaEq7Ceiling"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Unstable Horizontal Equation Source"] = value

    @property
    def convective_zone_heater_unstable_horizontal_equation_user_curve_name(self):
        """Get convective_zone_heater_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Horizontal Equation User Curve Name"]

    @convective_zone_heater_unstable_horizontal_equation_user_curve_name.setter
    def convective_zone_heater_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Unstable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_horizontal_equation_user_curve_name`')
        self._data["Convective Zone Heater Unstable Horizontal Equation User Curve Name"] = value

    @property
    def convective_zone_heater_stable_tilted_equation_source(self):
        """Get convective_zone_heater_stable_tilted_equation_source

        Returns:
            str: the value of `convective_zone_heater_stable_tilted_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Stable Tilted Equation Source"]

    @convective_zone_heater_stable_tilted_equation_source.setter
    def convective_zone_heater_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Convective Zone Heater Stable Tilted Equation Source`
        Applies to zone with convective heater
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Tilted Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Stable Tilted Equation Source"] = value

    @property
    def convective_zone_heater_stable_tilted_equation_user_curve_name(self):
        """Get convective_zone_heater_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Stable Tilted Equation User Curve Name"]

    @convective_zone_heater_stable_tilted_equation_user_curve_name.setter
    def convective_zone_heater_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Stable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Stable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_stable_tilted_equation_user_curve_name`')
        self._data["Convective Zone Heater Stable Tilted Equation User Curve Name"] = value

    @property
    def convective_zone_heater_unstable_tilted_equation_source(self):
        """Get convective_zone_heater_unstable_tilted_equation_source

        Returns:
            str: the value of `convective_zone_heater_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Tilted Equation Source"]

    @convective_zone_heater_unstable_tilted_equation_source.setter
    def convective_zone_heater_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Convective Zone Heater Unstable Tilted Equation Source`
        Applies to zone with convective heater
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Tilted Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Unstable Tilted Equation Source"] = value

    @property
    def convective_zone_heater_unstable_tilted_equation_user_curve_name(self):
        """Get convective_zone_heater_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Unstable Tilted Equation User Curve Name"]

    @convective_zone_heater_unstable_tilted_equation_user_curve_name.setter
    def convective_zone_heater_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Unstable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Unstable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_unstable_tilted_equation_user_curve_name`')
        self._data["Convective Zone Heater Unstable Tilted Equation User Curve Name"] = value

    @property
    def convective_zone_heater_windows_equation_source(self):
        """Get convective_zone_heater_windows_equation_source

        Returns:
            str: the value of `convective_zone_heater_windows_equation_source` or None if not set
        """
        return self._data["Convective Zone Heater Windows Equation Source"]

    @convective_zone_heater_windows_equation_source.setter
    def convective_zone_heater_windows_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `Convective Zone Heater Windows Equation Source`
        Applies to zone with convective heater
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `Convective Zone Heater Windows Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                Default value: ISO15099Windows
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convective Zone Heater Windows Equation Source"] = value

    @property
    def convective_zone_heater_windows_equation_user_curve_name(self):
        """Get convective_zone_heater_windows_equation_user_curve_name

        Returns:
            str: the value of `convective_zone_heater_windows_equation_user_curve_name` or None if not set
        """
        return self._data["Convective Zone Heater Windows Equation User Curve Name"]

    @convective_zone_heater_windows_equation_user_curve_name.setter
    def convective_zone_heater_windows_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convective Zone Heater Windows Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Convective Zone Heater Windows Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.convective_zone_heater_windows_equation_user_curve_name`')
        self._data["Convective Zone Heater Windows Equation User Curve Name"] = value

    @property
    def central_air_diffuser_wall_equation_source(self):
        """Get central_air_diffuser_wall_equation_source

        Returns:
            str: the value of `central_air_diffuser_wall_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Wall Equation Source"]

    @central_air_diffuser_wall_equation_source.setter
    def central_air_diffuser_wall_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserWalls"):
        """  Corresponds to IDD Field `Central Air Diffuser Wall Equation Source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all wall surfaces

        Args:
            value (str): value for IDD Field `Central Air Diffuser Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - AlamdariHammondVerticalWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserWalls
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Central Air Diffuser Wall Equation Source"] = value

    @property
    def central_air_diffuser_wall_equation_user_curve_name(self):
        """Get central_air_diffuser_wall_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Wall Equation User Curve Name"]

    @central_air_diffuser_wall_equation_user_curve_name.setter
    def central_air_diffuser_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Central Air Diffuser Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_wall_equation_user_curve_name`')
        self._data["Central Air Diffuser Wall Equation User Curve Name"] = value

    @property
    def central_air_diffuser_ceiling_equation_source(self):
        """Get central_air_diffuser_ceiling_equation_source

        Returns:
            str: the value of `central_air_diffuser_ceiling_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Ceiling Equation Source"]

    @central_air_diffuser_ceiling_equation_source.setter
    def central_air_diffuser_ceiling_equation_source(self, value="FisherPedersenCeilingDiffuserCeiling"):
        """  Corresponds to IDD Field `Central Air Diffuser Ceiling Equation Source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all ceiling surfaces

        Args:
            value (str): value for IDD Field `Central Air Diffuser Ceiling Equation Source`
                Accepted values are:
                      - FisherPedersenCeilingDiffuserCeiling
                      - BeausoleilMorrisonMixedStableCeiling
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - UserCurve
                Default value: FisherPedersenCeilingDiffuserCeiling
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_source`')
            vals = {}
            vals["fisherpedersenceilingdiffuserceiling"] = "FisherPedersenCeilingDiffuserCeiling"
            vals["beausoleilmorrisonmixedstableceiling"] = "BeausoleilMorrisonMixedStableCeiling"
            vals["beausoleilmorrisonmixedunstableceiling"] = "BeausoleilMorrisonMixedUnstableCeiling"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Central Air Diffuser Ceiling Equation Source"] = value

    @property
    def central_air_diffuser_ceiling_equation_user_curve_name(self):
        """Get central_air_diffuser_ceiling_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Ceiling Equation User Curve Name"]

    @central_air_diffuser_ceiling_equation_user_curve_name.setter
    def central_air_diffuser_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Central Air Diffuser Ceiling Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Ceiling Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_ceiling_equation_user_curve_name`')
        self._data["Central Air Diffuser Ceiling Equation User Curve Name"] = value

    @property
    def central_air_diffuser_floor_equation_source(self):
        """Get central_air_diffuser_floor_equation_source

        Returns:
            str: the value of `central_air_diffuser_floor_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Floor Equation Source"]

    @central_air_diffuser_floor_equation_source.setter
    def central_air_diffuser_floor_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserFloor"):
        """  Corresponds to IDD Field `Central Air Diffuser Floor Equation Source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all floor surfaces

        Args:
            value (str): value for IDD Field `Central Air Diffuser Floor Equation Source`
                Accepted values are:
                      - FisherPedersenCeilingDiffuserFloor
                      - BeausoleilMorrisonMixedStableFloor
                      - BeausoleilMorrisonMixedUnstableFloor
                      - GoldsteinNovoselacCeilingDiffuserFloor
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserFloor
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_source`')
            vals = {}
            vals["fisherpedersenceilingdiffuserfloor"] = "FisherPedersenCeilingDiffuserFloor"
            vals["beausoleilmorrisonmixedstablefloor"] = "BeausoleilMorrisonMixedStableFloor"
            vals["beausoleilmorrisonmixedunstablefloor"] = "BeausoleilMorrisonMixedUnstableFloor"
            vals["goldsteinnovoselacceilingdiffuserfloor"] = "GoldsteinNovoselacCeilingDiffuserFloor"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Central Air Diffuser Floor Equation Source"] = value

    @property
    def central_air_diffuser_floor_equation_user_curve_name(self):
        """Get central_air_diffuser_floor_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Floor Equation User Curve Name"]

    @central_air_diffuser_floor_equation_user_curve_name.setter
    def central_air_diffuser_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Central Air Diffuser Floor Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Floor Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_floor_equation_user_curve_name`')
        self._data["Central Air Diffuser Floor Equation User Curve Name"] = value

    @property
    def central_air_diffuser_window_equation_source(self):
        """Get central_air_diffuser_window_equation_source

        Returns:
            str: the value of `central_air_diffuser_window_equation_source` or None if not set
        """
        return self._data["Central Air Diffuser Window Equation Source"]

    @central_air_diffuser_window_equation_source.setter
    def central_air_diffuser_window_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserWindow"):
        """  Corresponds to IDD Field `Central Air Diffuser Window Equation Source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `Central Air Diffuser Window Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - FohannoPolidoriVerticalWall
                      - AlamdariHammondVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserWindow
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Central Air Diffuser Window Equation Source"] = value

    @property
    def central_air_diffuser_window_equation_user_curve_name(self):
        """Get central_air_diffuser_window_equation_user_curve_name

        Returns:
            str: the value of `central_air_diffuser_window_equation_user_curve_name` or None if not set
        """
        return self._data["Central Air Diffuser Window Equation User Curve Name"]

    @central_air_diffuser_window_equation_user_curve_name.setter
    def central_air_diffuser_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Central Air Diffuser Window Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Central Air Diffuser Window Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.central_air_diffuser_window_equation_user_curve_name`')
        self._data["Central Air Diffuser Window Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_vertical_wall_equation_source(self):
        """Get mechanical_zone_fan_circulation_vertical_wall_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_vertical_wall_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Vertical Wall Equation Source"]

    @mechanical_zone_fan_circulation_vertical_wall_equation_source.setter
    def mechanical_zone_fan_circulation_vertical_wall_equation_source(self, value="KhalifaEq3WallAwayFromHeat"):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Vertical Wall Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Vertical Wall Equation Source`
                Accepted values are:
                      - KhalifaEq3WallAwayFromHeat
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - AlamdariHammondVerticalWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: KhalifaEq3WallAwayFromHeat
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_source`')
            vals = {}
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"]

    @mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`')
        self._data["Mechanical Zone Fan Circulation Vertical Wall Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_stable_horizontal_equation_source(self):
        """Get mechanical_zone_fan_circulation_stable_horizontal_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation Source"]

    @mechanical_zone_fan_circulation_stable_horizontal_equation_source.setter
    def mechanical_zone_fan_circulation_stable_horizontal_equation_source(self, value="AlamdariHammondStableHorizontal"):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Stable Horizontal Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Horizontal Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: AlamdariHammondStableHorizontal
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"]

    @mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`')
        self._data["Mechanical Zone Fan Circulation Stable Horizontal Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_source(self):
        """Get mechanical_zone_fan_circulation_unstable_horizontal_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"]

    @mechanical_zone_fan_circulation_unstable_horizontal_equation_source.setter
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_source(self, value="KhalifaEq4CeilingAwayFromHeat"):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Unstable Horizontal Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Horizontal Equation Source`
                Accepted values are:
                      - KhalifaEq4CeilingAwayFromHeat
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: KhalifaEq4CeilingAwayFromHeat
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_source`')
            vals = {}
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"]

    @mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`')
        self._data["Mechanical Zone Fan Circulation Unstable Horizontal Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_stable_tilted_equation_source(self):
        """Get mechanical_zone_fan_circulation_stable_tilted_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_tilted_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Tilted Equation Source"]

    @mechanical_zone_fan_circulation_stable_tilted_equation_source.setter
    def mechanical_zone_fan_circulation_stable_tilted_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Stable Tilted Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Tilted Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - UserCurve
                Default value: WaltonStableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"]

    @mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`')
        self._data["Mechanical Zone Fan Circulation Stable Tilted Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_tilted_equation_source(self):
        """Get mechanical_zone_fan_circulation_unstable_tilted_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_tilted_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation Source"]

    @mechanical_zone_fan_circulation_unstable_tilted_equation_source.setter
    def mechanical_zone_fan_circulation_unstable_tilted_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Unstable Tilted Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Tilted Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: WaltonUnstableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"]

    @mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`')
        self._data["Mechanical Zone Fan Circulation Unstable Tilted Equation User Curve Name"] = value

    @property
    def mechanical_zone_fan_circulation_window_equation_source(self):
        """Get mechanical_zone_fan_circulation_window_equation_source

        Returns:
            str: the value of `mechanical_zone_fan_circulation_window_equation_source` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Window Equation Source"]

    @mechanical_zone_fan_circulation_window_equation_source.setter
    def mechanical_zone_fan_circulation_window_equation_source(self, value="ISO15099Windows"):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Window Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Window Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - UserCurve
                Default value: ISO15099Windows
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mechanical Zone Fan Circulation Window Equation Source"] = value

    @property
    def mechanical_zone_fan_circulation_window_equation_user_curve_name(self):
        """Get mechanical_zone_fan_circulation_window_equation_user_curve_name

        Returns:
            str: the value of `mechanical_zone_fan_circulation_window_equation_user_curve_name` or None if not set
        """
        return self._data["Mechanical Zone Fan Circulation Window Equation User Curve Name"]

    @mechanical_zone_fan_circulation_window_equation_user_curve_name.setter
    def mechanical_zone_fan_circulation_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mechanical Zone Fan Circulation Window Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mechanical Zone Fan Circulation Window Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mechanical_zone_fan_circulation_window_equation_user_curve_name`')
        self._data["Mechanical Zone Fan Circulation Window Equation User Curve Name"] = value

    @property
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_source(self):
        """Get mixed_regime_bouyancy_assisting_flow_on_walls_equation_source

        Returns:
            str: the value of `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation Source"]

    @mixed_regime_bouyancy_assisting_flow_on_walls_equation_source.setter
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_source(self, value="BeausoleilMorrisonMixedAssistedWall"):
        """  Corresponds to IDD Field `Mixed Regime Bouyancy Assisting Flow on Walls Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Bouyancy Assisting Flow on Walls Equation Source`
                Accepted values are:
                      - BeausoleilMorrisonMixedAssistedWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: BeausoleilMorrisonMixedAssistedWall
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`')
            vals = {}
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation Source"] = value

    @property
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name(self):
        """Get mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name"]

    @mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name.setter
    def mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`')
        self._data["Mixed Regime Bouyancy Assisting Flow on Walls Equation User Curve Name"] = value

    @property
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source(self):
        """Get mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source

        Returns:
            str: the value of `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source"]

    @mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source.setter
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source(self, value="BeausoleilMorrisonMixedOpposingWall"):
        """  Corresponds to IDD Field `Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source`
                Accepted values are:
                      - BeausoleilMorrisonMixedOpposingWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ASHRAEVerticalWall
                      - FisherPedersenCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - UserCurve
                Default value: BeausoleilMorrisonMixedOpposingWall
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`')
            vals = {}
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation Source"] = value

    @property
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name(self):
        """Get mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name"]

    @mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name.setter
    def mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`')
        self._data["Mixed Regime Bouyancy Oppossing Flow on Walls Equation User Curve Name"] = value

    @property
    def mixed_regime_stable_floor_equation_source(self):
        """Get mixed_regime_stable_floor_equation_source

        Returns:
            str: the value of `mixed_regime_stable_floor_equation_source` or None if not set
        """
        return self._data["Mixed Regime Stable Floor Equation Source"]

    @mixed_regime_stable_floor_equation_source.setter
    def mixed_regime_stable_floor_equation_source(self, value="BeausoleilMorrisonMixedStableFloor"):
        """  Corresponds to IDD Field `Mixed Regime Stable Floor Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Floor Equation Source`
                Accepted values are:
                      - BeausoleilMorrisonMixedStableFloor
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedStableFloor
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_source`')
            vals = {}
            vals["beausoleilmorrisonmixedstablefloor"] = "BeausoleilMorrisonMixedStableFloor"
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Stable Floor Equation Source"] = value

    @property
    def mixed_regime_stable_floor_equation_user_curve_name(self):
        """Get mixed_regime_stable_floor_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_stable_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Stable Floor Equation User Curve Name"]

    @mixed_regime_stable_floor_equation_user_curve_name.setter
    def mixed_regime_stable_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Stable Floor Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Floor Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_floor_equation_user_curve_name`')
        self._data["Mixed Regime Stable Floor Equation User Curve Name"] = value

    @property
    def mixed_regime_unstable_floor_equation_source(self):
        """Get mixed_regime_unstable_floor_equation_source

        Returns:
            str: the value of `mixed_regime_unstable_floor_equation_source` or None if not set
        """
        return self._data["Mixed Regime Unstable Floor Equation Source"]

    @mixed_regime_unstable_floor_equation_source.setter
    def mixed_regime_unstable_floor_equation_source(self, value="BeausoleilMorrisonMixedUnstableFloor"):
        """  Corresponds to IDD Field `Mixed Regime Unstable Floor Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Floor Equation Source`
                Accepted values are:
                      - BeausoleilMorrisonMixedUnstableFloor
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedUnstableFloor
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_source`')
            vals = {}
            vals["beausoleilmorrisonmixedunstablefloor"] = "BeausoleilMorrisonMixedUnstableFloor"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Unstable Floor Equation Source"] = value

    @property
    def mixed_regime_unstable_floor_equation_user_curve_name(self):
        """Get mixed_regime_unstable_floor_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_unstable_floor_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Unstable Floor Equation User Curve Name"]

    @mixed_regime_unstable_floor_equation_user_curve_name.setter
    def mixed_regime_unstable_floor_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Unstable Floor Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Floor Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_floor_equation_user_curve_name`')
        self._data["Mixed Regime Unstable Floor Equation User Curve Name"] = value

    @property
    def mixed_regime_stable_ceiling_equation_source(self):
        """Get mixed_regime_stable_ceiling_equation_source

        Returns:
            str: the value of `mixed_regime_stable_ceiling_equation_source` or None if not set
        """
        return self._data["Mixed Regime Stable Ceiling Equation Source"]

    @mixed_regime_stable_ceiling_equation_source.setter
    def mixed_regime_stable_ceiling_equation_source(self, value="BeausoleilMorrisonMixedStableCeiling"):
        """  Corresponds to IDD Field `Mixed Regime Stable Ceiling Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Ceiling Equation Source`
                Accepted values are:
                      - BeausoleilMorrisonMixedStableCeiling
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedStableCeiling
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_source`')
            vals = {}
            vals["beausoleilmorrisonmixedstableceiling"] = "BeausoleilMorrisonMixedStableCeiling"
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Stable Ceiling Equation Source"] = value

    @property
    def mixed_regime_stable_ceiling_equation_user_curve_name(self):
        """Get mixed_regime_stable_ceiling_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_stable_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Stable Ceiling Equation User Curve Name"]

    @mixed_regime_stable_ceiling_equation_user_curve_name.setter
    def mixed_regime_stable_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Stable Ceiling Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Stable Ceiling Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_stable_ceiling_equation_user_curve_name`')
        self._data["Mixed Regime Stable Ceiling Equation User Curve Name"] = value

    @property
    def mixed_regime_unstable_ceiling_equation_source(self):
        """Get mixed_regime_unstable_ceiling_equation_source

        Returns:
            str: the value of `mixed_regime_unstable_ceiling_equation_source` or None if not set
        """
        return self._data["Mixed Regime Unstable Ceiling Equation Source"]

    @mixed_regime_unstable_ceiling_equation_source.setter
    def mixed_regime_unstable_ceiling_equation_source(self, value="BeausoleilMorrisonMixedUnstableCeiling"):
        """  Corresponds to IDD Field `Mixed Regime Unstable Ceiling Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Ceiling Equation Source`
                Accepted values are:
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                Default value: BeausoleilMorrisonMixedUnstableCeiling
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_source`')
            vals = {}
            vals["beausoleilmorrisonmixedunstableceiling"] = "BeausoleilMorrisonMixedUnstableCeiling"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Unstable Ceiling Equation Source"] = value

    @property
    def mixed_regime_unstable_ceiling_equation_user_curve_name(self):
        """Get mixed_regime_unstable_ceiling_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_unstable_ceiling_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Unstable Ceiling Equation User Curve Name"]

    @mixed_regime_unstable_ceiling_equation_user_curve_name.setter
    def mixed_regime_unstable_ceiling_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Unstable Ceiling Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Unstable Ceiling Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_unstable_ceiling_equation_user_curve_name`')
        self._data["Mixed Regime Unstable Ceiling Equation User Curve Name"] = value

    @property
    def mixed_regime_window_equation_source(self):
        """Get mixed_regime_window_equation_source

        Returns:
            str: the value of `mixed_regime_window_equation_source` or None if not set
        """
        return self._data["Mixed Regime Window Equation Source"]

    @mixed_regime_window_equation_source.setter
    def mixed_regime_window_equation_source(self, value="GoldsteinNovoselacCeilingDiffuserWindow"):
        """  Corresponds to IDD Field `Mixed Regime Window Equation Source`
        reference choice fields

        Args:
            value (str): value for IDD Field `Mixed Regime Window Equation Source`
                Accepted values are:
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - ISO15099Windows
                      - UserCurve
                Default value: GoldsteinNovoselacCeilingDiffuserWindow
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_source`')
            vals = {}
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Mixed Regime Window Equation Source"] = value

    @property
    def mixed_regime_window_equation_user_curve_name(self):
        """Get mixed_regime_window_equation_user_curve_name

        Returns:
            str: the value of `mixed_regime_window_equation_user_curve_name` or None if not set
        """
        return self._data["Mixed Regime Window Equation User Curve Name"]

    @mixed_regime_window_equation_user_curve_name.setter
    def mixed_regime_window_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Regime Window Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Mixed Regime Window Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideAdaptiveModelSelections.mixed_regime_window_equation_user_curve_name`')
        self._data["Mixed Regime Window Equation User Curve Name"] = value

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
                    raise ValueError("Required field SurfaceConvectionAlgorithmInsideAdaptiveModelSelections:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceConvectionAlgorithmInsideAdaptiveModelSelections:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceConvectionAlgorithmInsideAdaptiveModelSelections: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceConvectionAlgorithmInsideAdaptiveModelSelections: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the outside face, the side of the surface facing away from the thermal zone.
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections"
    field_count = 13
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wind Convection Windward Vertical Wall Equation Source"] = None
        self._data["Wind Convection Windward Equation Vertical Wall User Curve Name"] = None
        self._data["Wind Convection Leeward Vertical Wall Equation Source"] = None
        self._data["Wind Convection Leeward Vertical Wall Equation User Curve Name"] = None
        self._data["Wind Convection Horizontal Roof Equation Source"] = None
        self._data["Wind Convection Horizontal Roof User Curve Name"] = None
        self._data["Natural Convection Vertical Wall Equation Source"] = None
        self._data["Natural Convection Vertical Wall Equation User Curve Name"] = None
        self._data["Natural Convection Stable Horizontal Equation Source"] = None
        self._data["Natural Convection Stable Horizontal Equation User Curve Name"] = None
        self._data["Natural Convection Unstable Horizontal Equation Source"] = None
        self._data["Natural Convection Unstable Horizontal Equation User Curve Name"] = None
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
            self.wind_convection_windward_vertical_wall_equation_source = None
        else:
            self.wind_convection_windward_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_convection_windward_equation_vertical_wall_user_curve_name = None
        else:
            self.wind_convection_windward_equation_vertical_wall_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_convection_leeward_vertical_wall_equation_source = None
        else:
            self.wind_convection_leeward_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_convection_leeward_vertical_wall_equation_user_curve_name = None
        else:
            self.wind_convection_leeward_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_convection_horizontal_roof_equation_source = None
        else:
            self.wind_convection_horizontal_roof_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.wind_convection_horizontal_roof_user_curve_name = None
        else:
            self.wind_convection_horizontal_roof_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.natural_convection_vertical_wall_equation_source = None
        else:
            self.natural_convection_vertical_wall_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.natural_convection_vertical_wall_equation_user_curve_name = None
        else:
            self.natural_convection_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.natural_convection_stable_horizontal_equation_source = None
        else:
            self.natural_convection_stable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.natural_convection_stable_horizontal_equation_user_curve_name = None
        else:
            self.natural_convection_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.natural_convection_unstable_horizontal_equation_source = None
        else:
            self.natural_convection_unstable_horizontal_equation_source = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.natural_convection_unstable_horizontal_equation_user_curve_name = None
        else:
            self.natural_convection_unstable_horizontal_equation_user_curve_name = vals[i]
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.name`')
        self._data["Name"] = value

    @property
    def wind_convection_windward_vertical_wall_equation_source(self):
        """Get wind_convection_windward_vertical_wall_equation_source

        Returns:
            str: the value of `wind_convection_windward_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wind Convection Windward Vertical Wall Equation Source"]

    @wind_convection_windward_vertical_wall_equation_source.setter
    def wind_convection_windward_vertical_wall_equation_source(self, value="TARPWindward"):
        """  Corresponds to IDD Field `Wind Convection Windward Vertical Wall Equation Source`

        Args:
            value (str): value for IDD Field `Wind Convection Windward Vertical Wall Equation Source`
                Accepted values are:
                      - SimpleCombined
                      - TARPWindward
                      - MoWiTTWindward
                      - DOE2Windward
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - BlockenWindward
                      - EmmelVertical
                      - UserCurve
                Default value: TARPWindward
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_vertical_wall_equation_source`')
            vals = {}
            vals["simplecombined"] = "SimpleCombined"
            vals["tarpwindward"] = "TARPWindward"
            vals["mowittwindward"] = "MoWiTTWindward"
            vals["doe2windward"] = "DOE2Windward"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["blockenwindward"] = "BlockenWindward"
            vals["emmelvertical"] = "EmmelVertical"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Convection Windward Vertical Wall Equation Source"] = value

    @property
    def wind_convection_windward_equation_vertical_wall_user_curve_name(self):
        """Get wind_convection_windward_equation_vertical_wall_user_curve_name

        Returns:
            str: the value of `wind_convection_windward_equation_vertical_wall_user_curve_name` or None if not set
        """
        return self._data["Wind Convection Windward Equation Vertical Wall User Curve Name"]

    @wind_convection_windward_equation_vertical_wall_user_curve_name.setter
    def wind_convection_windward_equation_vertical_wall_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wind Convection Windward Equation Vertical Wall User Curve Name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wind Convection Windward Equation Vertical Wall User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_equation_vertical_wall_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_equation_vertical_wall_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_windward_equation_vertical_wall_user_curve_name`')
        self._data["Wind Convection Windward Equation Vertical Wall User Curve Name"] = value

    @property
    def wind_convection_leeward_vertical_wall_equation_source(self):
        """Get wind_convection_leeward_vertical_wall_equation_source

        Returns:
            str: the value of `wind_convection_leeward_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wind Convection Leeward Vertical Wall Equation Source"]

    @wind_convection_leeward_vertical_wall_equation_source.setter
    def wind_convection_leeward_vertical_wall_equation_source(self, value="TARPLeeward"):
        """  Corresponds to IDD Field `Wind Convection Leeward Vertical Wall Equation Source`

        Args:
            value (str): value for IDD Field `Wind Convection Leeward Vertical Wall Equation Source`
                Accepted values are:
                      - SimpleCombined
                      - TARPLeeward
                      - MoWiTTLeeward
                      - DOE2Leeward
                      - EmmelVertical
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - UserCurve
                Default value: TARPLeeward
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_source`')
            vals = {}
            vals["simplecombined"] = "SimpleCombined"
            vals["tarpleeward"] = "TARPLeeward"
            vals["mowittleeward"] = "MoWiTTLeeward"
            vals["doe2leeward"] = "DOE2Leeward"
            vals["emmelvertical"] = "EmmelVertical"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Convection Leeward Vertical Wall Equation Source"] = value

    @property
    def wind_convection_leeward_vertical_wall_equation_user_curve_name(self):
        """Get wind_convection_leeward_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `wind_convection_leeward_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Wind Convection Leeward Vertical Wall Equation User Curve Name"]

    @wind_convection_leeward_vertical_wall_equation_user_curve_name.setter
    def wind_convection_leeward_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wind Convection Leeward Vertical Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wind Convection Leeward Vertical Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_leeward_vertical_wall_equation_user_curve_name`')
        self._data["Wind Convection Leeward Vertical Wall Equation User Curve Name"] = value

    @property
    def wind_convection_horizontal_roof_equation_source(self):
        """Get wind_convection_horizontal_roof_equation_source

        Returns:
            str: the value of `wind_convection_horizontal_roof_equation_source` or None if not set
        """
        return self._data["Wind Convection Horizontal Roof Equation Source"]

    @wind_convection_horizontal_roof_equation_source.setter
    def wind_convection_horizontal_roof_equation_source(self, value="ClearRoof"):
        """  Corresponds to IDD Field `Wind Convection Horizontal Roof Equation Source`

        Args:
            value (str): value for IDD Field `Wind Convection Horizontal Roof Equation Source`
                Accepted values are:
                      - SimpleCombined
                      - TARPWindward
                      - MoWiTTWindward
                      - DOE2Windward
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - BlockenWindward
                      - EmmelRoof
                      - ClearRoof
                      - UserCurve
                Default value: ClearRoof
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_equation_source`')
            vals = {}
            vals["simplecombined"] = "SimpleCombined"
            vals["tarpwindward"] = "TARPWindward"
            vals["mowittwindward"] = "MoWiTTWindward"
            vals["doe2windward"] = "DOE2Windward"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["blockenwindward"] = "BlockenWindward"
            vals["emmelroof"] = "EmmelRoof"
            vals["clearroof"] = "ClearRoof"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Convection Horizontal Roof Equation Source"] = value

    @property
    def wind_convection_horizontal_roof_user_curve_name(self):
        """Get wind_convection_horizontal_roof_user_curve_name

        Returns:
            str: the value of `wind_convection_horizontal_roof_user_curve_name` or None if not set
        """
        return self._data["Wind Convection Horizontal Roof User Curve Name"]

    @wind_convection_horizontal_roof_user_curve_name.setter
    def wind_convection_horizontal_roof_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Wind Convection Horizontal Roof User Curve Name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Wind Convection Horizontal Roof User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.wind_convection_horizontal_roof_user_curve_name`')
        self._data["Wind Convection Horizontal Roof User Curve Name"] = value

    @property
    def natural_convection_vertical_wall_equation_source(self):
        """Get natural_convection_vertical_wall_equation_source

        Returns:
            str: the value of `natural_convection_vertical_wall_equation_source` or None if not set
        """
        return self._data["Natural Convection Vertical Wall Equation Source"]

    @natural_convection_vertical_wall_equation_source.setter
    def natural_convection_vertical_wall_equation_source(self, value="ASHRAEVerticalWall"):
        """  Corresponds to IDD Field `Natural Convection Vertical Wall Equation Source`
        This is for vertical walls

        Args:
            value (str): value for IDD Field `Natural Convection Vertical Wall Equation Source`
                Accepted values are:
                      - ASHRAEVerticalWall
                      - AlamdariHammondVerticalWall
                      - FohannoPolidoriVerticalWall
                      - ISO15099Windows
                      - UserCurve
                      - None
                Default value: ASHRAEVerticalWall
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_source`')
            vals = {}
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["usercurve"] = "UserCurve"
            vals["none"] = "None"
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
                                     'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Natural Convection Vertical Wall Equation Source"] = value

    @property
    def natural_convection_vertical_wall_equation_user_curve_name(self):
        """Get natural_convection_vertical_wall_equation_user_curve_name

        Returns:
            str: the value of `natural_convection_vertical_wall_equation_user_curve_name` or None if not set
        """
        return self._data["Natural Convection Vertical Wall Equation User Curve Name"]

    @natural_convection_vertical_wall_equation_user_curve_name.setter
    def natural_convection_vertical_wall_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Natural Convection Vertical Wall Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Natural Convection Vertical Wall Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_vertical_wall_equation_user_curve_name`')
        self._data["Natural Convection Vertical Wall Equation User Curve Name"] = value

    @property
    def natural_convection_stable_horizontal_equation_source(self):
        """Get natural_convection_stable_horizontal_equation_source

        Returns:
            str: the value of `natural_convection_stable_horizontal_equation_source` or None if not set
        """
        return self._data["Natural Convection Stable Horizontal Equation Source"]

    @natural_convection_stable_horizontal_equation_source.setter
    def natural_convection_stable_horizontal_equation_source(self, value="WaltonStableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Natural Convection Stable Horizontal Equation Source`
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `Natural Convection Stable Horizontal Equation Source`
                Accepted values are:
                      - WaltonStableHorizontalOrTilt
                      - AlamdariHammondStableHorizontal
                      - UserCurve
                      - None
                Default value: WaltonStableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_source`')
            vals = {}
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["usercurve"] = "UserCurve"
            vals["none"] = "None"
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
                                     'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Natural Convection Stable Horizontal Equation Source"] = value

    @property
    def natural_convection_stable_horizontal_equation_user_curve_name(self):
        """Get natural_convection_stable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `natural_convection_stable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Natural Convection Stable Horizontal Equation User Curve Name"]

    @natural_convection_stable_horizontal_equation_user_curve_name.setter
    def natural_convection_stable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Natural Convection Stable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Natural Convection Stable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_stable_horizontal_equation_user_curve_name`')
        self._data["Natural Convection Stable Horizontal Equation User Curve Name"] = value

    @property
    def natural_convection_unstable_horizontal_equation_source(self):
        """Get natural_convection_unstable_horizontal_equation_source

        Returns:
            str: the value of `natural_convection_unstable_horizontal_equation_source` or None if not set
        """
        return self._data["Natural Convection Unstable Horizontal Equation Source"]

    @natural_convection_unstable_horizontal_equation_source.setter
    def natural_convection_unstable_horizontal_equation_source(self, value="WaltonUnstableHorizontalOrTilt"):
        """  Corresponds to IDD Field `Natural Convection Unstable Horizontal Equation Source`

        Args:
            value (str): value for IDD Field `Natural Convection Unstable Horizontal Equation Source`
                Accepted values are:
                      - WaltonUnstableHorizontalOrTilt
                      - AlamdariHammondUnstableHorizontal
                      - UserCurve
                      - None
                Default value: WaltonUnstableHorizontalOrTilt
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_source`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_source`')
            vals = {}
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["usercurve"] = "UserCurve"
            vals["none"] = "None"
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
                                     'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_source`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_source`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Natural Convection Unstable Horizontal Equation Source"] = value

    @property
    def natural_convection_unstable_horizontal_equation_user_curve_name(self):
        """Get natural_convection_unstable_horizontal_equation_user_curve_name

        Returns:
            str: the value of `natural_convection_unstable_horizontal_equation_user_curve_name` or None if not set
        """
        return self._data["Natural Convection Unstable Horizontal Equation User Curve Name"]

    @natural_convection_unstable_horizontal_equation_user_curve_name.setter
    def natural_convection_unstable_horizontal_equation_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Natural Convection Unstable Horizontal Equation User Curve Name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `Natural Convection Unstable Horizontal Equation User Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections.natural_convection_unstable_horizontal_equation_user_curve_name`')
        self._data["Natural Convection Unstable Horizontal Equation User Curve Name"] = value

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
                    raise ValueError("Required field SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfaceConvectionAlgorithmInsideUserCurve(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside:UserCurve"
    field_count = 6
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Inside:UserCurve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reference Temperature for Convection Heat Transfer"] = None
        self._data["Hc Function of Temperature Difference Curve Name"] = None
        self._data["Hc Function of Temperature Difference Divided by Height Curve Name"] = None
        self._data["Hc Function of Air Change Rate Curve Name"] = None
        self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"] = None
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
            self.reference_temperature_for_convection_heat_transfer = None
        else:
            self.reference_temperature_for_convection_heat_transfer = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hc_function_of_temperature_difference_curve_name = None
        else:
            self.hc_function_of_temperature_difference_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hc_function_of_temperature_difference_divided_by_height_curve_name = None
        else:
            self.hc_function_of_temperature_difference_divided_by_height_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hc_function_of_air_change_rate_curve_name = None
        else:
            self.hc_function_of_air_change_rate_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = None
        else:
            self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = vals[i]
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
                                 ' for field `SurfaceConvectionAlgorithmInsideUserCurve.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.name`')
        self._data["Name"] = value

    @property
    def reference_temperature_for_convection_heat_transfer(self):
        """Get reference_temperature_for_convection_heat_transfer

        Returns:
            str: the value of `reference_temperature_for_convection_heat_transfer` or None if not set
        """
        return self._data["Reference Temperature for Convection Heat Transfer"]

    @reference_temperature_for_convection_heat_transfer.setter
    def reference_temperature_for_convection_heat_transfer(self, value=None):
        """  Corresponds to IDD Field `Reference Temperature for Convection Heat Transfer`
        Controls which temperature is differenced from surface temperature when using the Hc value

        Args:
            value (str): value for IDD Field `Reference Temperature for Convection Heat Transfer`
                Accepted values are:
                      - MeanAirTemperature
                      - AdjacentAirTemperature
                      - SupplyAirTemperature
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
                                 ' for field `SurfaceConvectionAlgorithmInsideUserCurve.reference_temperature_for_convection_heat_transfer`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.reference_temperature_for_convection_heat_transfer`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.reference_temperature_for_convection_heat_transfer`')
            vals = {}
            vals["meanairtemperature"] = "MeanAirTemperature"
            vals["adjacentairtemperature"] = "AdjacentAirTemperature"
            vals["supplyairtemperature"] = "SupplyAirTemperature"
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
                                     'field `SurfaceConvectionAlgorithmInsideUserCurve.reference_temperature_for_convection_heat_transfer`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmInsideUserCurve.reference_temperature_for_convection_heat_transfer`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reference Temperature for Convection Heat Transfer"] = value

    @property
    def hc_function_of_temperature_difference_curve_name(self):
        """Get hc_function_of_temperature_difference_curve_name

        Returns:
            str: the value of `hc_function_of_temperature_difference_curve_name` or None if not set
        """
        return self._data["Hc Function of Temperature Difference Curve Name"]

    @hc_function_of_temperature_difference_curve_name.setter
    def hc_function_of_temperature_difference_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hc Function of Temperature Difference Curve Name`
        Curve's "x" is absolute value of delta-T (Surface temperature minus reference temperature, (C))
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `Hc Function of Temperature Difference Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_temperature_difference_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_temperature_difference_curve_name`')
        self._data["Hc Function of Temperature Difference Curve Name"] = value

    @property
    def hc_function_of_temperature_difference_divided_by_height_curve_name(self):
        """Get hc_function_of_temperature_difference_divided_by_height_curve_name

        Returns:
            str: the value of `hc_function_of_temperature_difference_divided_by_height_curve_name` or None if not set
        """
        return self._data["Hc Function of Temperature Difference Divided by Height Curve Name"]

    @hc_function_of_temperature_difference_divided_by_height_curve_name.setter
    def hc_function_of_temperature_difference_divided_by_height_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hc Function of Temperature Difference Divided by Height Curve Name`
        Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        when used for an inside face the vertical length scale is the zone's interior height
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Hc Function of Temperature Difference Divided by Height Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_temperature_difference_divided_by_height_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_temperature_difference_divided_by_height_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_temperature_difference_divided_by_height_curve_name`')
        self._data["Hc Function of Temperature Difference Divided by Height Curve Name"] = value

    @property
    def hc_function_of_air_change_rate_curve_name(self):
        """Get hc_function_of_air_change_rate_curve_name

        Returns:
            str: the value of `hc_function_of_air_change_rate_curve_name` or None if not set
        """
        return self._data["Hc Function of Air Change Rate Curve Name"]

    @hc_function_of_air_change_rate_curve_name.setter
    def hc_function_of_air_change_rate_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hc Function of Air Change Rate Curve Name`
        Curve's "x" is mechanical ACH (Air Changes per hour from mechanical air system), (1/hr)
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `Hc Function of Air Change Rate Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_air_change_rate_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_air_change_rate_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_air_change_rate_curve_name`')
        self._data["Hc Function of Air Change Rate Curve Name"] = value

    @property
    def hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name(self):
        """Get hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name

        Returns:
            str: the value of `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name` or None if not set
        """
        return self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"]

    @hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name.setter
    def hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name`
        Curve's "x" is mechanical system air flow rate (m3/s) divided by zone's length along
        exterior walls (m).
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmInsideUserCurve.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`')
        self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"] = value

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
                    raise ValueError("Required field SurfaceConvectionAlgorithmInsideUserCurve:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceConvectionAlgorithmInsideUserCurve:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceConvectionAlgorithmInsideUserCurve: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceConvectionAlgorithmInsideUserCurve: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfaceConvectionAlgorithmOutsideUserCurve(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside:UserCurve"
    field_count = 5
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Outside:UserCurve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wind Speed Type for Curve"] = None
        self._data["Hf Function of Wind Speed Curve Name"] = None
        self._data["Hn Function of Temperature Difference Curve Name"] = None
        self._data["Hn Function of Temperature Difference Divided by Height Curve Name"] = None
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
            self.wind_speed_type_for_curve = None
        else:
            self.wind_speed_type_for_curve = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hf_function_of_wind_speed_curve_name = None
        else:
            self.hf_function_of_wind_speed_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hn_function_of_temperature_difference_curve_name = None
        else:
            self.hn_function_of_temperature_difference_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hn_function_of_temperature_difference_divided_by_height_curve_name = None
        else:
            self.hn_function_of_temperature_difference_divided_by_height_curve_name = vals[i]
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideUserCurve.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.name`')
        self._data["Name"] = value

    @property
    def wind_speed_type_for_curve(self):
        """Get wind_speed_type_for_curve

        Returns:
            str: the value of `wind_speed_type_for_curve` or None if not set
        """
        return self._data["Wind Speed Type for Curve"]

    @wind_speed_type_for_curve.setter
    def wind_speed_type_for_curve(self, value="HeightAdjust"):
        """  Corresponds to IDD Field `Wind Speed Type for Curve`

        Args:
            value (str): value for IDD Field `Wind Speed Type for Curve`
                Accepted values are:
                      - WeatherFile
                      - HeightAdjust
                      - ParallelComponent
                      - ParallelComponentHeightAdjust
                Default value: HeightAdjust
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideUserCurve.wind_speed_type_for_curve`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.wind_speed_type_for_curve`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.wind_speed_type_for_curve`')
            vals = {}
            vals["weatherfile"] = "WeatherFile"
            vals["heightadjust"] = "HeightAdjust"
            vals["parallelcomponent"] = "ParallelComponent"
            vals["parallelcomponentheightadjust"] = "ParallelComponentHeightAdjust"
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
                                     'field `SurfaceConvectionAlgorithmOutsideUserCurve.wind_speed_type_for_curve`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfaceConvectionAlgorithmOutsideUserCurve.wind_speed_type_for_curve`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Wind Speed Type for Curve"] = value

    @property
    def hf_function_of_wind_speed_curve_name(self):
        """Get hf_function_of_wind_speed_curve_name

        Returns:
            str: the value of `hf_function_of_wind_speed_curve_name` or None if not set
        """
        return self._data["Hf Function of Wind Speed Curve Name"]

    @hf_function_of_wind_speed_curve_name.setter
    def hf_function_of_wind_speed_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hf Function of Wind Speed Curve Name`
        Curve's "x" is wind speed of the type determined in the previous field (m/s)
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `Hf Function of Wind Speed Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideUserCurve.hf_function_of_wind_speed_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.hf_function_of_wind_speed_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.hf_function_of_wind_speed_curve_name`')
        self._data["Hf Function of Wind Speed Curve Name"] = value

    @property
    def hn_function_of_temperature_difference_curve_name(self):
        """Get hn_function_of_temperature_difference_curve_name

        Returns:
            str: the value of `hn_function_of_temperature_difference_curve_name` or None if not set
        """
        return self._data["Hn Function of Temperature Difference Curve Name"]

    @hn_function_of_temperature_difference_curve_name.setter
    def hn_function_of_temperature_difference_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hn Function of Temperature Difference Curve Name`
        Curve's "x" is absolute value of delta-T (Surface temperature minus air temperature, (C))
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Hn Function of Temperature Difference Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideUserCurve.hn_function_of_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.hn_function_of_temperature_difference_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.hn_function_of_temperature_difference_curve_name`')
        self._data["Hn Function of Temperature Difference Curve Name"] = value

    @property
    def hn_function_of_temperature_difference_divided_by_height_curve_name(self):
        """Get hn_function_of_temperature_difference_divided_by_height_curve_name

        Returns:
            str: the value of `hn_function_of_temperature_difference_divided_by_height_curve_name` or None if not set
        """
        return self._data["Hn Function of Temperature Difference Divided by Height Curve Name"]

    @hn_function_of_temperature_difference_divided_by_height_curve_name.setter
    def hn_function_of_temperature_difference_divided_by_height_curve_name(self, value=None):
        """  Corresponds to IDD Field `Hn Function of Temperature Difference Divided by Height Curve Name`
        Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        when used for an outside face the vertical length scale is the exterior facade's overall height
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `Hn Function of Temperature Difference Divided by Height Curve Name`
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
                                 ' for field `SurfaceConvectionAlgorithmOutsideUserCurve.hn_function_of_temperature_difference_divided_by_height_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.hn_function_of_temperature_difference_divided_by_height_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfaceConvectionAlgorithmOutsideUserCurve.hn_function_of_temperature_difference_divided_by_height_curve_name`')
        self._data["Hn Function of Temperature Difference Divided by Height Curve Name"] = value

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
                    raise ValueError("Required field SurfaceConvectionAlgorithmOutsideUserCurve:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfaceConvectionAlgorithmOutsideUserCurve:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfaceConvectionAlgorithmOutsideUserCurve: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfaceConvectionAlgorithmOutsideUserCurve: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyConvectionCoefficients(object):
    """ Corresponds to IDD object `SurfaceProperty:ConvectionCoefficients`
        Allow user settable interior and/or exterior convection coefficients.
        Note that some other factors may limit the lower bounds for these values, such as
        for windows, the interior convection coefficient must be >.28,
        for trombe wall algorithm selection (zone), the interior convection coefficient must be >.1
        for TARP interior convection, the lower limit is also .1
        Minimum and maximum limits are set in HeatBalanceAlgorithm object.
        Defaults in HeatBalanceAlgorithm object are [.1,1000].
    """
    internal_name = "SurfaceProperty:ConvectionCoefficients"
    field_count = 11
    required_fields = ["Surface Name", "Convection Coefficient 1 Location", "Convection Coefficient 1 Type"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:ConvectionCoefficients`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Convection Coefficient 1 Location"] = None
        self._data["Convection Coefficient 1 Type"] = None
        self._data["Convection Coefficient 1"] = None
        self._data["Convection Coefficient 1 Schedule Name"] = None
        self._data["Convection Coefficient 1 User Curve Name"] = None
        self._data["Convection Coefficient 2 Location"] = None
        self._data["Convection Coefficient 2 Type"] = None
        self._data["Convection Coefficient 2"] = None
        self._data["Convection Coefficient 2 Schedule Name"] = None
        self._data["Convection Coefficient 2 User Curve Name"] = None
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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_location = None
        else:
            self.convection_coefficient_1_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_type = None
        else:
            self.convection_coefficient_1_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1 = None
        else:
            self.convection_coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_schedule_name = None
        else:
            self.convection_coefficient_1_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_user_curve_name = None
        else:
            self.convection_coefficient_1_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_location = None
        else:
            self.convection_coefficient_2_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_type = None
        else:
            self.convection_coefficient_2_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2 = None
        else:
            self.convection_coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_schedule_name = None
        else:
            self.convection_coefficient_2_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_user_curve_name = None
        else:
            self.convection_coefficient_2_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficients.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.surface_name`')
        self._data["Surface Name"] = value

    @property
    def convection_coefficient_1_location(self):
        """Get convection_coefficient_1_location

        Returns:
            str: the value of `convection_coefficient_1_location` or None if not set
        """
        return self._data["Convection Coefficient 1 Location"]

    @convection_coefficient_1_location.setter
    def convection_coefficient_1_location(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Location`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_location`')
            vals = {}
            vals["outside"] = "Outside"
            vals["inside"] = "Inside"
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
                                     'field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_location`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_location`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 1 Location"] = value

    @property
    def convection_coefficient_1_type(self):
        """Get convection_coefficient_1_type

        Returns:
            str: the value of `convection_coefficient_1_type` or None if not set
        """
        return self._data["Convection Coefficient 1 Type"]

    @convection_coefficient_1_type.setter
    def convection_coefficient_1_type(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Type`
                Accepted values are:
                      - Value
                      - Schedule
                      - UserCurve
                      - Simple
                      - SimpleCombined
                      - TARP
                      - DOE-2
                      - MoWitt
                      - AdaptiveConvectionAlgorithm
                      - ASHRAEVerticalWall
                      - WaltonUnstableHorizontalOrTilt
                      - WaltonStableHorizontalOrTilt
                      - FisherPedersenCeilingDiffuserWalls
                      - FisherPedersenCeilingDiffuserCeiling
                      - FisherPedersenCeilingDiffuserFloor
                      - AlamdariHammondStableHorizontal
                      - AlamdariHammondUnstableHorizontal
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq4CeilingAwayFromHeat
                      - KhalifaEq5WallNearHeat
                      - KhalifaEq6NonHeatedWalls
                      - KhalifaEq7Ceiling
                      - AwbiHattonHeatedFloor
                      - AwbiHattonHeatedWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - BeausoleilMorrisonMixedStableFloor
                      - BeausoleilMorrisonMixedUnstableFloor
                      - BeausoleilMorrisonMixedStableCeiling
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - FohannoPolidoriVerticalWall
                      - KaradagChilledCeiling
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserFloor
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - EmmelVertical
                      - EmmelRoof
                      - ClearRoof
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_type`')
            vals = {}
            vals["value"] = "Value"
            vals["schedule"] = "Schedule"
            vals["usercurve"] = "UserCurve"
            vals["simple"] = "Simple"
            vals["simplecombined"] = "SimpleCombined"
            vals["tarp"] = "TARP"
            vals["doe-2"] = "DOE-2"
            vals["mowitt"] = "MoWitt"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["fisherpedersenceilingdiffuserceiling"] = "FisherPedersenCeilingDiffuserCeiling"
            vals["fisherpedersenceilingdiffuserfloor"] = "FisherPedersenCeilingDiffuserFloor"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["khalifaeq5wallnearheat"] = "KhalifaEq5WallNearHeat"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["khalifaeq7ceiling"] = "KhalifaEq7Ceiling"
            vals["awbihattonheatedfloor"] = "AwbiHattonHeatedFloor"
            vals["awbihattonheatedwall"] = "AwbiHattonHeatedWall"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["beausoleilmorrisonmixedstablefloor"] = "BeausoleilMorrisonMixedStableFloor"
            vals["beausoleilmorrisonmixedunstablefloor"] = "BeausoleilMorrisonMixedUnstableFloor"
            vals["beausoleilmorrisonmixedstableceiling"] = "BeausoleilMorrisonMixedStableCeiling"
            vals["beausoleilmorrisonmixedunstableceiling"] = "BeausoleilMorrisonMixedUnstableCeiling"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["goldsteinnovoselacceilingdiffuserfloor"] = "GoldsteinNovoselacCeilingDiffuserFloor"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["emmelvertical"] = "EmmelVertical"
            vals["emmelroof"] = "EmmelRoof"
            vals["clearroof"] = "ClearRoof"
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
                                     'field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 1 Type"] = value

    @property
    def convection_coefficient_1(self):
        """Get convection_coefficient_1

        Returns:
            float: the value of `convection_coefficient_1` or None if not set
        """
        return self._data["Convection Coefficient 1"]

    @convection_coefficient_1.setter
    def convection_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `Convection Coefficient 1`
                Units: W/m2-K
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1`'.format(value))
        self._data["Convection Coefficient 1"] = value

    @property
    def convection_coefficient_1_schedule_name(self):
        """Get convection_coefficient_1_schedule_name

        Returns:
            str: the value of `convection_coefficient_1_schedule_name` or None if not set
        """
        return self._data["Convection Coefficient 1 Schedule Name"]

    @convection_coefficient_1_schedule_name.setter
    def convection_coefficient_1_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 Schedule Name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Schedule Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_schedule_name`')
        self._data["Convection Coefficient 1 Schedule Name"] = value

    @property
    def convection_coefficient_1_user_curve_name(self):
        """Get convection_coefficient_1_user_curve_name

        Returns:
            str: the value of `convection_coefficient_1_user_curve_name` or None if not set
        """
        return self._data["Convection Coefficient 1 User Curve Name"]

    @convection_coefficient_1_user_curve_name.setter
    def convection_coefficient_1_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 User Curve Name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 User Curve Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_1_user_curve_name`')
        self._data["Convection Coefficient 1 User Curve Name"] = value

    @property
    def convection_coefficient_2_location(self):
        """Get convection_coefficient_2_location

        Returns:
            str: the value of `convection_coefficient_2_location` or None if not set
        """
        return self._data["Convection Coefficient 2 Location"]

    @convection_coefficient_2_location.setter
    def convection_coefficient_2_location(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Location`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_location`')
            vals = {}
            vals["outside"] = "Outside"
            vals["inside"] = "Inside"
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
                                     'field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_location`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_location`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 2 Location"] = value

    @property
    def convection_coefficient_2_type(self):
        """Get convection_coefficient_2_type

        Returns:
            str: the value of `convection_coefficient_2_type` or None if not set
        """
        return self._data["Convection Coefficient 2 Type"]

    @convection_coefficient_2_type.setter
    def convection_coefficient_2_type(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Type`
                Accepted values are:
                      - Value
                      - Schedule
                      - UserCurve
                      - Simple
                      - SimpleCombined
                      - TARP
                      - DOE-2
                      - MoWitt
                      - AdaptiveConvectionAlgorithm
                      - ASHRAEVerticalWall
                      - WaltonUnstableHorizontalOrTilt
                      - WaltonStableHorizontalOrTilt
                      - FisherPedersenCeilingDiffuserWalls
                      - FisherPedersenCeilingDiffuserCeiling
                      - FisherPedersenCeilingDiffuserFloor
                      - AlamdariHammondStableHorizontal
                      - AlamdariHammondUnstableHorizontal
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq4CeilingAwayFromHeat
                      - KhalifaEq5WallNearHeat
                      - KhalifaEq6NonHeatedWalls
                      - KhalifaEq7Ceiling
                      - AwbiHattonHeatedFloor
                      - AwbiHattonHeatedWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - BeausoleilMorrisonMixedStableFloor
                      - BeausoleilMorrisonMixedUnstableFloor
                      - BeausoleilMorrisonMixedStableCeiling
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - FohannoPolidoriVerticalWall
                      - KaradagChilledCeiling
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserFloor
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - EmmelVertical
                      - EmmelRoof
                      - ClearRoof
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_type`')
            vals = {}
            vals["value"] = "Value"
            vals["schedule"] = "Schedule"
            vals["usercurve"] = "UserCurve"
            vals["simple"] = "Simple"
            vals["simplecombined"] = "SimpleCombined"
            vals["tarp"] = "TARP"
            vals["doe-2"] = "DOE-2"
            vals["mowitt"] = "MoWitt"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["fisherpedersenceilingdiffuserceiling"] = "FisherPedersenCeilingDiffuserCeiling"
            vals["fisherpedersenceilingdiffuserfloor"] = "FisherPedersenCeilingDiffuserFloor"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["khalifaeq5wallnearheat"] = "KhalifaEq5WallNearHeat"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["khalifaeq7ceiling"] = "KhalifaEq7Ceiling"
            vals["awbihattonheatedfloor"] = "AwbiHattonHeatedFloor"
            vals["awbihattonheatedwall"] = "AwbiHattonHeatedWall"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["beausoleilmorrisonmixedstablefloor"] = "BeausoleilMorrisonMixedStableFloor"
            vals["beausoleilmorrisonmixedunstablefloor"] = "BeausoleilMorrisonMixedUnstableFloor"
            vals["beausoleilmorrisonmixedstableceiling"] = "BeausoleilMorrisonMixedStableCeiling"
            vals["beausoleilmorrisonmixedunstableceiling"] = "BeausoleilMorrisonMixedUnstableCeiling"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["goldsteinnovoselacceilingdiffuserfloor"] = "GoldsteinNovoselacCeilingDiffuserFloor"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["emmelvertical"] = "EmmelVertical"
            vals["emmelroof"] = "EmmelRoof"
            vals["clearroof"] = "ClearRoof"
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
                                     'field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 2 Type"] = value

    @property
    def convection_coefficient_2(self):
        """Get convection_coefficient_2

        Returns:
            float: the value of `convection_coefficient_2` or None if not set
        """
        return self._data["Convection Coefficient 2"]

    @convection_coefficient_2.setter
    def convection_coefficient_2(self, value=0.1):
        """  Corresponds to IDD Field `Convection Coefficient 2`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `Convection Coefficient 2`
                Units: W/m2-K
                Default value: 0.1
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2`'.format(value))
        self._data["Convection Coefficient 2"] = value

    @property
    def convection_coefficient_2_schedule_name(self):
        """Get convection_coefficient_2_schedule_name

        Returns:
            str: the value of `convection_coefficient_2_schedule_name` or None if not set
        """
        return self._data["Convection Coefficient 2 Schedule Name"]

    @convection_coefficient_2_schedule_name.setter
    def convection_coefficient_2_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 Schedule Name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Schedule Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_schedule_name`')
        self._data["Convection Coefficient 2 Schedule Name"] = value

    @property
    def convection_coefficient_2_user_curve_name(self):
        """Get convection_coefficient_2_user_curve_name

        Returns:
            str: the value of `convection_coefficient_2_user_curve_name` or None if not set
        """
        return self._data["Convection Coefficient 2 User Curve Name"]

    @convection_coefficient_2_user_curve_name.setter
    def convection_coefficient_2_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 User Curve Name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 User Curve Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficients.convection_coefficient_2_user_curve_name`')
        self._data["Convection Coefficient 2 User Curve Name"] = value

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
                    raise ValueError("Required field SurfacePropertyConvectionCoefficients:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyConvectionCoefficients:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyConvectionCoefficients: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyConvectionCoefficients: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyConvectionCoefficientsMultipleSurface(object):
    """ Corresponds to IDD object `SurfaceProperty:ConvectionCoefficients:MultipleSurface`
        Allow user settable interior and/or exterior convection coefficients.
        Note that some other factors may limit the lower bounds for these values, such as
        for windows, the interior convection coefficient must be >.28,
        for trombe wall algorithm selection (zone), the interior convection coefficient must be >.1
        for TARP interior convection, the lower limit is also .1
        Minimum and maximum limits are set in HeatBalanceAlgorithm object.
        Defaults in HeatBalanceAlgorithm object are [.1,1000].
    """
    internal_name = "SurfaceProperty:ConvectionCoefficients:MultipleSurface"
    field_count = 11
    required_fields = ["Surface Type", "Convection Coefficient 1 Location", "Convection Coefficient 1 Type"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:ConvectionCoefficients:MultipleSurface`
        """
        self._data = OrderedDict()
        self._data["Surface Type"] = None
        self._data["Convection Coefficient 1 Location"] = None
        self._data["Convection Coefficient 1 Type"] = None
        self._data["Convection Coefficient 1"] = None
        self._data["Convection Coefficient 1 Schedule Name"] = None
        self._data["Convection Coefficient 1 User Curve Name"] = None
        self._data["Convection Coefficient 2 Location"] = None
        self._data["Convection Coefficient 2 Type"] = None
        self._data["Convection Coefficient 2"] = None
        self._data["Convection Coefficient 2 Schedule Name"] = None
        self._data["Convection Coefficient 2 User Curve Name"] = None
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
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_location = None
        else:
            self.convection_coefficient_1_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_type = None
        else:
            self.convection_coefficient_1_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1 = None
        else:
            self.convection_coefficient_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_schedule_name = None
        else:
            self.convection_coefficient_1_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_1_user_curve_name = None
        else:
            self.convection_coefficient_1_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_location = None
        else:
            self.convection_coefficient_2_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_type = None
        else:
            self.convection_coefficient_2_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2 = None
        else:
            self.convection_coefficient_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_schedule_name = None
        else:
            self.convection_coefficient_2_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.convection_coefficient_2_user_curve_name = None
        else:
            self.convection_coefficient_2_user_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
                      - AllExteriorSurfaces
                      - AllExteriorWindows
                      - AllExteriorWalls
                      - AllExteriorRoofs
                      - AllExteriorFloors
                      - AllInteriorSurfaces
                      - AllInteriorWalls
                      - AllInteriorWindows
                      - AllInteriorCeilings
                      - AllInteriorFloors
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.surface_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.surface_type`')
            vals = {}
            vals["allexteriorsurfaces"] = "AllExteriorSurfaces"
            vals["allexteriorwindows"] = "AllExteriorWindows"
            vals["allexteriorwalls"] = "AllExteriorWalls"
            vals["allexteriorroofs"] = "AllExteriorRoofs"
            vals["allexteriorfloors"] = "AllExteriorFloors"
            vals["allinteriorsurfaces"] = "AllInteriorSurfaces"
            vals["allinteriorwalls"] = "AllInteriorWalls"
            vals["allinteriorwindows"] = "AllInteriorWindows"
            vals["allinteriorceilings"] = "AllInteriorCeilings"
            vals["allinteriorfloors"] = "AllInteriorFloors"
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
                                     'field `SurfacePropertyConvectionCoefficientsMultipleSurface.surface_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficientsMultipleSurface.surface_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Surface Type"] = value

    @property
    def convection_coefficient_1_location(self):
        """Get convection_coefficient_1_location

        Returns:
            str: the value of `convection_coefficient_1_location` or None if not set
        """
        return self._data["Convection Coefficient 1 Location"]

    @convection_coefficient_1_location.setter
    def convection_coefficient_1_location(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Location`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_location`')
            vals = {}
            vals["outside"] = "Outside"
            vals["inside"] = "Inside"
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
                                     'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_location`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_location`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 1 Location"] = value

    @property
    def convection_coefficient_1_type(self):
        """Get convection_coefficient_1_type

        Returns:
            str: the value of `convection_coefficient_1_type` or None if not set
        """
        return self._data["Convection Coefficient 1 Type"]

    @convection_coefficient_1_type.setter
    def convection_coefficient_1_type(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Type`
                Accepted values are:
                      - Value
                      - Schedule
                      - Simple
                      - SimpleCombined
                      - TARP
                      - DOE-2
                      - MoWitt
                      - AdaptiveConvectionAlgorithm
                      - ASHRAEVerticalWall
                      - WaltonUnstableHorizontalOrTilt
                      - WaltonStableHorizontalOrTilt
                      - FisherPedersenCeilingDiffuserWalls
                      - FisherPedersenCeilingDiffuserCeiling
                      - FisherPedersenCeilingDiffuserFloor
                      - AlamdariHammondStableHorizontal
                      - AlamdariHammondUnstableHorizontal
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq4CeilingAwayFromHeat
                      - KhalifaEq5WallNearHeat
                      - KhalifaEq6NonHeatedWalls
                      - KhalifaEq7Ceiling
                      - AwbiHattonHeatedFloor
                      - AwbiHattonHeatedWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - BeausoleilMorrisonMixedStableFloor
                      - BeausoleilMorrisonMixedUnstableFloor
                      - BeausoleilMorrisonMixedStableCeiling
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - FohannoPolidoriVerticalWall
                      - KaradagChilledCeiling
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserFloor
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - BlockenWindard
                      - EmmelVertical
                      - EmmelRoof
                      - ClearRoof
                      - UserCurve
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_type`')
            vals = {}
            vals["value"] = "Value"
            vals["schedule"] = "Schedule"
            vals["simple"] = "Simple"
            vals["simplecombined"] = "SimpleCombined"
            vals["tarp"] = "TARP"
            vals["doe-2"] = "DOE-2"
            vals["mowitt"] = "MoWitt"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["fisherpedersenceilingdiffuserceiling"] = "FisherPedersenCeilingDiffuserCeiling"
            vals["fisherpedersenceilingdiffuserfloor"] = "FisherPedersenCeilingDiffuserFloor"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["khalifaeq5wallnearheat"] = "KhalifaEq5WallNearHeat"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["khalifaeq7ceiling"] = "KhalifaEq7Ceiling"
            vals["awbihattonheatedfloor"] = "AwbiHattonHeatedFloor"
            vals["awbihattonheatedwall"] = "AwbiHattonHeatedWall"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["beausoleilmorrisonmixedstablefloor"] = "BeausoleilMorrisonMixedStableFloor"
            vals["beausoleilmorrisonmixedunstablefloor"] = "BeausoleilMorrisonMixedUnstableFloor"
            vals["beausoleilmorrisonmixedstableceiling"] = "BeausoleilMorrisonMixedStableCeiling"
            vals["beausoleilmorrisonmixedunstableceiling"] = "BeausoleilMorrisonMixedUnstableCeiling"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["goldsteinnovoselacceilingdiffuserfloor"] = "GoldsteinNovoselacCeilingDiffuserFloor"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["blockenwindard"] = "BlockenWindard"
            vals["emmelvertical"] = "EmmelVertical"
            vals["emmelroof"] = "EmmelRoof"
            vals["clearroof"] = "ClearRoof"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 1 Type"] = value

    @property
    def convection_coefficient_1(self):
        """Get convection_coefficient_1

        Returns:
            float: the value of `convection_coefficient_1` or None if not set
        """
        return self._data["Convection Coefficient 1"]

    @convection_coefficient_1.setter
    def convection_coefficient_1(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `Convection Coefficient 1`
                Units: W/m2-K
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1`'.format(value))
        self._data["Convection Coefficient 1"] = value

    @property
    def convection_coefficient_1_schedule_name(self):
        """Get convection_coefficient_1_schedule_name

        Returns:
            str: the value of `convection_coefficient_1_schedule_name` or None if not set
        """
        return self._data["Convection Coefficient 1 Schedule Name"]

    @convection_coefficient_1_schedule_name.setter
    def convection_coefficient_1_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 Schedule Name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 Schedule Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_schedule_name`')
        self._data["Convection Coefficient 1 Schedule Name"] = value

    @property
    def convection_coefficient_1_user_curve_name(self):
        """Get convection_coefficient_1_user_curve_name

        Returns:
            str: the value of `convection_coefficient_1_user_curve_name` or None if not set
        """
        return self._data["Convection Coefficient 1 User Curve Name"]

    @convection_coefficient_1_user_curve_name.setter
    def convection_coefficient_1_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 1 User Curve Name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 1 User Curve Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_1_user_curve_name`')
        self._data["Convection Coefficient 1 User Curve Name"] = value

    @property
    def convection_coefficient_2_location(self):
        """Get convection_coefficient_2_location

        Returns:
            str: the value of `convection_coefficient_2_location` or None if not set
        """
        return self._data["Convection Coefficient 2 Location"]

    @convection_coefficient_2_location.setter
    def convection_coefficient_2_location(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 Location`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Location`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_location`')
            vals = {}
            vals["outside"] = "Outside"
            vals["inside"] = "Inside"
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
                                     'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_location`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_location`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 2 Location"] = value

    @property
    def convection_coefficient_2_type(self):
        """Get convection_coefficient_2_type

        Returns:
            str: the value of `convection_coefficient_2_type` or None if not set
        """
        return self._data["Convection Coefficient 2 Type"]

    @convection_coefficient_2_type.setter
    def convection_coefficient_2_type(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 Type`

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Type`
                Accepted values are:
                      - Value
                      - Schedule
                      - Simple
                      - SimpleCombined
                      - TARP
                      - DOE-2
                      - MoWitt
                      - AdaptiveConvectionAlgorithm
                      - ASHRAEVerticalWall
                      - WaltonUnstableHorizontalOrTilt
                      - WaltonStableHorizontalOrTilt
                      - FisherPedersenCeilingDiffuserWalls
                      - FisherPedersenCeilingDiffuserCeiling
                      - FisherPedersenCeilingDiffuserFloor
                      - AlamdariHammondStableHorizontal
                      - AlamdariHammondUnstableHorizontal
                      - AlamdariHammondVerticalWall
                      - KhalifaEq3WallAwayFromHeat
                      - KhalifaEq4CeilingAwayFromHeat
                      - KhalifaEq5WallNearHeat
                      - KhalifaEq6NonHeatedWalls
                      - KhalifaEq7Ceiling
                      - AwbiHattonHeatedFloor
                      - AwbiHattonHeatedWall
                      - BeausoleilMorrisonMixedAssistedWall
                      - BeausoleilMorrisonMixedOpposingWall
                      - BeausoleilMorrisonMixedStableFloor
                      - BeausoleilMorrisonMixedUnstableFloor
                      - BeausoleilMorrisonMixedStableCeiling
                      - BeausoleilMorrisonMixedUnstableCeiling
                      - FohannoPolidoriVerticalWall
                      - KaradagChilledCeiling
                      - ISO15099Windows
                      - GoldsteinNovoselacCeilingDiffuserWindow
                      - GoldsteinNovoselacCeilingDiffuserWalls
                      - GoldsteinNovoselacCeilingDiffuserFloor
                      - NusseltJurges
                      - McAdams
                      - Mitchell
                      - BlockenWindard
                      - EmmelVertical
                      - EmmelRoof
                      - ClearRoof
                      - UserCurve
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_type`')
            vals = {}
            vals["value"] = "Value"
            vals["schedule"] = "Schedule"
            vals["simple"] = "Simple"
            vals["simplecombined"] = "SimpleCombined"
            vals["tarp"] = "TARP"
            vals["doe-2"] = "DOE-2"
            vals["mowitt"] = "MoWitt"
            vals["adaptiveconvectionalgorithm"] = "AdaptiveConvectionAlgorithm"
            vals["ashraeverticalwall"] = "ASHRAEVerticalWall"
            vals["waltonunstablehorizontalortilt"] = "WaltonUnstableHorizontalOrTilt"
            vals["waltonstablehorizontalortilt"] = "WaltonStableHorizontalOrTilt"
            vals["fisherpedersenceilingdiffuserwalls"] = "FisherPedersenCeilingDiffuserWalls"
            vals["fisherpedersenceilingdiffuserceiling"] = "FisherPedersenCeilingDiffuserCeiling"
            vals["fisherpedersenceilingdiffuserfloor"] = "FisherPedersenCeilingDiffuserFloor"
            vals["alamdarihammondstablehorizontal"] = "AlamdariHammondStableHorizontal"
            vals["alamdarihammondunstablehorizontal"] = "AlamdariHammondUnstableHorizontal"
            vals["alamdarihammondverticalwall"] = "AlamdariHammondVerticalWall"
            vals["khalifaeq3wallawayfromheat"] = "KhalifaEq3WallAwayFromHeat"
            vals["khalifaeq4ceilingawayfromheat"] = "KhalifaEq4CeilingAwayFromHeat"
            vals["khalifaeq5wallnearheat"] = "KhalifaEq5WallNearHeat"
            vals["khalifaeq6nonheatedwalls"] = "KhalifaEq6NonHeatedWalls"
            vals["khalifaeq7ceiling"] = "KhalifaEq7Ceiling"
            vals["awbihattonheatedfloor"] = "AwbiHattonHeatedFloor"
            vals["awbihattonheatedwall"] = "AwbiHattonHeatedWall"
            vals["beausoleilmorrisonmixedassistedwall"] = "BeausoleilMorrisonMixedAssistedWall"
            vals["beausoleilmorrisonmixedopposingwall"] = "BeausoleilMorrisonMixedOpposingWall"
            vals["beausoleilmorrisonmixedstablefloor"] = "BeausoleilMorrisonMixedStableFloor"
            vals["beausoleilmorrisonmixedunstablefloor"] = "BeausoleilMorrisonMixedUnstableFloor"
            vals["beausoleilmorrisonmixedstableceiling"] = "BeausoleilMorrisonMixedStableCeiling"
            vals["beausoleilmorrisonmixedunstableceiling"] = "BeausoleilMorrisonMixedUnstableCeiling"
            vals["fohannopolidoriverticalwall"] = "FohannoPolidoriVerticalWall"
            vals["karadagchilledceiling"] = "KaradagChilledCeiling"
            vals["iso15099windows"] = "ISO15099Windows"
            vals["goldsteinnovoselacceilingdiffuserwindow"] = "GoldsteinNovoselacCeilingDiffuserWindow"
            vals["goldsteinnovoselacceilingdiffuserwalls"] = "GoldsteinNovoselacCeilingDiffuserWalls"
            vals["goldsteinnovoselacceilingdiffuserfloor"] = "GoldsteinNovoselacCeilingDiffuserFloor"
            vals["nusseltjurges"] = "NusseltJurges"
            vals["mcadams"] = "McAdams"
            vals["mitchell"] = "Mitchell"
            vals["blockenwindard"] = "BlockenWindard"
            vals["emmelvertical"] = "EmmelVertical"
            vals["emmelroof"] = "EmmelRoof"
            vals["clearroof"] = "ClearRoof"
            vals["usercurve"] = "UserCurve"
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
                                     'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Convection Coefficient 2 Type"] = value

    @property
    def convection_coefficient_2(self):
        """Get convection_coefficient_2

        Returns:
            float: the value of `convection_coefficient_2` or None if not set
        """
        return self._data["Convection Coefficient 2"]

    @convection_coefficient_2.setter
    def convection_coefficient_2(self, value=0.1):
        """  Corresponds to IDD Field `Convection Coefficient 2`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `Convection Coefficient 2`
                Units: W/m2-K
                Default value: 0.1
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2`'.format(value))
        self._data["Convection Coefficient 2"] = value

    @property
    def convection_coefficient_2_schedule_name(self):
        """Get convection_coefficient_2_schedule_name

        Returns:
            str: the value of `convection_coefficient_2_schedule_name` or None if not set
        """
        return self._data["Convection Coefficient 2 Schedule Name"]

    @convection_coefficient_2_schedule_name.setter
    def convection_coefficient_2_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 Schedule Name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 Schedule Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_schedule_name`')
        self._data["Convection Coefficient 2 Schedule Name"] = value

    @property
    def convection_coefficient_2_user_curve_name(self):
        """Get convection_coefficient_2_user_curve_name

        Returns:
            str: the value of `convection_coefficient_2_user_curve_name` or None if not set
        """
        return self._data["Convection Coefficient 2 User Curve Name"]

    @convection_coefficient_2_user_curve_name.setter
    def convection_coefficient_2_user_curve_name(self, value=None):
        """  Corresponds to IDD Field `Convection Coefficient 2 User Curve Name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `Convection Coefficient 2 User Curve Name`
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
                                 ' for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_user_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyConvectionCoefficientsMultipleSurface.convection_coefficient_2_user_curve_name`')
        self._data["Convection Coefficient 2 User Curve Name"] = value

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
                    raise ValueError("Required field SurfacePropertyConvectionCoefficientsMultipleSurface:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyConvectionCoefficientsMultipleSurface:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyConvectionCoefficientsMultipleSurface: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyConvectionCoefficientsMultipleSurface: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertiesVaporCoefficients(object):
    """ Corresponds to IDD object `SurfaceProperties:VaporCoefficients`
        The interior and external vapor transfer coefficients.
        Normally these value are calculated using the heat convection coefficient values.
        Use this object to used fixed constant values.
        Units are kg/Pa.s.m2
        This will only work with the CombinedHeatAndMoistureFiniteElement algorithm for surfaces.
        Other algorithms will ignore these coefficients
    """
    internal_name = "SurfaceProperties:VaporCoefficients"
    field_count = 5
    required_fields = ["Surface Name", "Constant External Vapor Transfer Coefficient", "Constant Internal vapor Transfer Coefficient"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperties:VaporCoefficients`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Constant External Vapor Transfer Coefficient"] = None
        self._data["External Vapor Coefficient Value"] = None
        self._data["Constant Internal vapor Transfer Coefficient"] = None
        self._data["Internal Vapor Coefficient Value"] = None
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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_external_vapor_transfer_coefficient = None
        else:
            self.constant_external_vapor_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.external_vapor_coefficient_value = None
        else:
            self.external_vapor_coefficient_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.constant_internal_vapor_transfer_coefficient = None
        else:
            self.constant_internal_vapor_transfer_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.internal_vapor_coefficient_value = None
        else:
            self.internal_vapor_coefficient_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SurfacePropertiesVaporCoefficients.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertiesVaporCoefficients.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertiesVaporCoefficients.surface_name`')
        self._data["Surface Name"] = value

    @property
    def constant_external_vapor_transfer_coefficient(self):
        """Get constant_external_vapor_transfer_coefficient

        Returns:
            str: the value of `constant_external_vapor_transfer_coefficient` or None if not set
        """
        return self._data["Constant External Vapor Transfer Coefficient"]

    @constant_external_vapor_transfer_coefficient.setter
    def constant_external_vapor_transfer_coefficient(self, value="No"):
        """  Corresponds to IDD Field `Constant External Vapor Transfer Coefficient`

        Args:
            value (str): value for IDD Field `Constant External Vapor Transfer Coefficient`
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
                                 ' for field `SurfacePropertiesVaporCoefficients.constant_external_vapor_transfer_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertiesVaporCoefficients.constant_external_vapor_transfer_coefficient`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertiesVaporCoefficients.constant_external_vapor_transfer_coefficient`')
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
                                     'field `SurfacePropertiesVaporCoefficients.constant_external_vapor_transfer_coefficient`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertiesVaporCoefficients.constant_external_vapor_transfer_coefficient`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Constant External Vapor Transfer Coefficient"] = value

    @property
    def external_vapor_coefficient_value(self):
        """Get external_vapor_coefficient_value

        Returns:
            float: the value of `external_vapor_coefficient_value` or None if not set
        """
        return self._data["External Vapor Coefficient Value"]

    @external_vapor_coefficient_value.setter
    def external_vapor_coefficient_value(self, value=0.0):
        """  Corresponds to IDD Field `External Vapor Coefficient Value`

        Args:
            value (float): value for IDD Field `External Vapor Coefficient Value`
                Units: kg/Pa-s-m2
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
                                 ' for field `SurfacePropertiesVaporCoefficients.external_vapor_coefficient_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SurfacePropertiesVaporCoefficients.external_vapor_coefficient_value`')
        self._data["External Vapor Coefficient Value"] = value

    @property
    def constant_internal_vapor_transfer_coefficient(self):
        """Get constant_internal_vapor_transfer_coefficient

        Returns:
            str: the value of `constant_internal_vapor_transfer_coefficient` or None if not set
        """
        return self._data["Constant Internal vapor Transfer Coefficient"]

    @constant_internal_vapor_transfer_coefficient.setter
    def constant_internal_vapor_transfer_coefficient(self, value="No"):
        """  Corresponds to IDD Field `Constant Internal vapor Transfer Coefficient`

        Args:
            value (str): value for IDD Field `Constant Internal vapor Transfer Coefficient`
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
                                 ' for field `SurfacePropertiesVaporCoefficients.constant_internal_vapor_transfer_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertiesVaporCoefficients.constant_internal_vapor_transfer_coefficient`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertiesVaporCoefficients.constant_internal_vapor_transfer_coefficient`')
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
                                     'field `SurfacePropertiesVaporCoefficients.constant_internal_vapor_transfer_coefficient`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertiesVaporCoefficients.constant_internal_vapor_transfer_coefficient`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Constant Internal vapor Transfer Coefficient"] = value

    @property
    def internal_vapor_coefficient_value(self):
        """Get internal_vapor_coefficient_value

        Returns:
            float: the value of `internal_vapor_coefficient_value` or None if not set
        """
        return self._data["Internal Vapor Coefficient Value"]

    @internal_vapor_coefficient_value.setter
    def internal_vapor_coefficient_value(self, value=0.0):
        """  Corresponds to IDD Field `Internal Vapor Coefficient Value`

        Args:
            value (float): value for IDD Field `Internal Vapor Coefficient Value`
                Units: kg/Pa-s-m2
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
                                 ' for field `SurfacePropertiesVaporCoefficients.internal_vapor_coefficient_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SurfacePropertiesVaporCoefficients.internal_vapor_coefficient_value`')
        self._data["Internal Vapor Coefficient Value"] = value

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
                    raise ValueError("Required field SurfacePropertiesVaporCoefficients:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertiesVaporCoefficients:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertiesVaporCoefficients: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertiesVaporCoefficients: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertyExteriorNaturalVentedCavity(object):
    """ Corresponds to IDD object `SurfaceProperty:ExteriorNaturalVentedCavity`
        Used to describe the decoupled layer, or baffle, and the characteristics of the cavity
        and openings for naturally ventilated exterior surfaces. This object is also used in
        conjunction with the OtherSideConditionsModel.
    """
    internal_name = "SurfaceProperty:ExteriorNaturalVentedCavity"
    field_count = 11
    required_fields = ["Name", "Boundary Conditions Model Name", "Roughness of Exterior Surface"]
    extensible_fields = 1
    format = None
    min_fields = 0
    extensible_keys = ["Surface 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:ExteriorNaturalVentedCavity`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Boundary Conditions Model Name"] = None
        self._data["Area Fraction of Openings"] = None
        self._data["Thermal Emissivity of Exterior Baffle Material"] = None
        self._data["Solar Absorbtivity of Exterior Baffle"] = None
        self._data["Height Scale for Buoyancy-Driven Ventilation"] = None
        self._data["Effective Thickness of Cavity Behind Exterior Baffle"] = None
        self._data["Ratio of Actual Surface Area to Projected Surface Area"] = None
        self._data["Roughness of Exterior Surface"] = None
        self._data["Effectiveness for Perforations with Respect to Wind"] = None
        self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = None
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
            self.boundary_conditions_model_name = None
        else:
            self.boundary_conditions_model_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_fraction_of_openings = None
        else:
            self.area_fraction_of_openings = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_emissivity_of_exterior_baffle_material = None
        else:
            self.thermal_emissivity_of_exterior_baffle_material = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.solar_absorbtivity_of_exterior_baffle = None
        else:
            self.solar_absorbtivity_of_exterior_baffle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_scale_for_buoyancydriven_ventilation = None
        else:
            self.height_scale_for_buoyancydriven_ventilation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effective_thickness_of_cavity_behind_exterior_baffle = None
        else:
            self.effective_thickness_of_cavity_behind_exterior_baffle = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_actual_surface_area_to_projected_surface_area = None
        else:
            self.ratio_of_actual_surface_area_to_projected_surface_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.roughness_of_exterior_surface = None
        else:
            self.roughness_of_exterior_surface = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effectiveness_for_perforations_with_respect_to_wind = None
        else:
            self.effectiveness_for_perforations_with_respect_to_wind = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = None
        else:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = vals[i]
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.name`')
        self._data["Name"] = value

    @property
    def boundary_conditions_model_name(self):
        """Get boundary_conditions_model_name

        Returns:
            str: the value of `boundary_conditions_model_name` or None if not set
        """
        return self._data["Boundary Conditions Model Name"]

    @boundary_conditions_model_name.setter
    def boundary_conditions_model_name(self, value=None):
        """  Corresponds to IDD Field `Boundary Conditions Model Name`
        Enter the name of a SurfaceProperty:OtherSideConditionsModel object

        Args:
            value (str): value for IDD Field `Boundary Conditions Model Name`
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.boundary_conditions_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.boundary_conditions_model_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.boundary_conditions_model_name`')
        self._data["Boundary Conditions Model Name"] = value

    @property
    def area_fraction_of_openings(self):
        """Get area_fraction_of_openings

        Returns:
            float: the value of `area_fraction_of_openings` or None if not set
        """
        return self._data["Area Fraction of Openings"]

    @area_fraction_of_openings.setter
    def area_fraction_of_openings(self, value=None):
        """  Corresponds to IDD Field `Area Fraction of Openings`

        Args:
            value (float): value for IDD Field `Area Fraction of Openings`
                Units: dimensionless
                value > 0.0
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.area_fraction_of_openings`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.area_fraction_of_openings`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.area_fraction_of_openings`')
        self._data["Area Fraction of Openings"] = value

    @property
    def thermal_emissivity_of_exterior_baffle_material(self):
        """Get thermal_emissivity_of_exterior_baffle_material

        Returns:
            float: the value of `thermal_emissivity_of_exterior_baffle_material` or None if not set
        """
        return self._data["Thermal Emissivity of Exterior Baffle Material"]

    @thermal_emissivity_of_exterior_baffle_material.setter
    def thermal_emissivity_of_exterior_baffle_material(self, value=None):
        """  Corresponds to IDD Field `Thermal Emissivity of Exterior Baffle Material`

        Args:
            value (float): value for IDD Field `Thermal Emissivity of Exterior Baffle Material`
                Units: dimensionless
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.thermal_emissivity_of_exterior_baffle_material`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.thermal_emissivity_of_exterior_baffle_material`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.thermal_emissivity_of_exterior_baffle_material`')
        self._data["Thermal Emissivity of Exterior Baffle Material"] = value

    @property
    def solar_absorbtivity_of_exterior_baffle(self):
        """Get solar_absorbtivity_of_exterior_baffle

        Returns:
            float: the value of `solar_absorbtivity_of_exterior_baffle` or None if not set
        """
        return self._data["Solar Absorbtivity of Exterior Baffle"]

    @solar_absorbtivity_of_exterior_baffle.setter
    def solar_absorbtivity_of_exterior_baffle(self, value=None):
        """  Corresponds to IDD Field `Solar Absorbtivity of Exterior Baffle`

        Args:
            value (float): value for IDD Field `Solar Absorbtivity of Exterior Baffle`
                Units: dimensionless
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.solar_absorbtivity_of_exterior_baffle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.solar_absorbtivity_of_exterior_baffle`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.solar_absorbtivity_of_exterior_baffle`')
        self._data["Solar Absorbtivity of Exterior Baffle"] = value

    @property
    def height_scale_for_buoyancydriven_ventilation(self):
        """Get height_scale_for_buoyancydriven_ventilation

        Returns:
            float: the value of `height_scale_for_buoyancydriven_ventilation` or None if not set
        """
        return self._data["Height Scale for Buoyancy-Driven Ventilation"]

    @height_scale_for_buoyancydriven_ventilation.setter
    def height_scale_for_buoyancydriven_ventilation(self, value=None):
        """  Corresponds to IDD Field `Height Scale for Buoyancy-Driven Ventilation`

        Args:
            value (float): value for IDD Field `Height Scale for Buoyancy-Driven Ventilation`
                Units: m
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.height_scale_for_buoyancydriven_ventilation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.height_scale_for_buoyancydriven_ventilation`')
        self._data["Height Scale for Buoyancy-Driven Ventilation"] = value

    @property
    def effective_thickness_of_cavity_behind_exterior_baffle(self):
        """Get effective_thickness_of_cavity_behind_exterior_baffle

        Returns:
            float: the value of `effective_thickness_of_cavity_behind_exterior_baffle` or None if not set
        """
        return self._data["Effective Thickness of Cavity Behind Exterior Baffle"]

    @effective_thickness_of_cavity_behind_exterior_baffle.setter
    def effective_thickness_of_cavity_behind_exterior_baffle(self, value=None):
        """  Corresponds to IDD Field `Effective Thickness of Cavity Behind Exterior Baffle`
        if corrugated, use average depth

        Args:
            value (float): value for IDD Field `Effective Thickness of Cavity Behind Exterior Baffle`
                Units: m
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.effective_thickness_of_cavity_behind_exterior_baffle`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.effective_thickness_of_cavity_behind_exterior_baffle`')
        self._data["Effective Thickness of Cavity Behind Exterior Baffle"] = value

    @property
    def ratio_of_actual_surface_area_to_projected_surface_area(self):
        """Get ratio_of_actual_surface_area_to_projected_surface_area

        Returns:
            float: the value of `ratio_of_actual_surface_area_to_projected_surface_area` or None if not set
        """
        return self._data["Ratio of Actual Surface Area to Projected Surface Area"]

    @ratio_of_actual_surface_area_to_projected_surface_area.setter
    def ratio_of_actual_surface_area_to_projected_surface_area(self, value=1.0):
        """  Corresponds to IDD Field `Ratio of Actual Surface Area to Projected Surface Area`
        this parameter is used to help account for corrugations in the collector

        Args:
            value (float): value for IDD Field `Ratio of Actual Surface Area to Projected Surface Area`
                Units: dimensionless
                Default value: 1.0
                value >= 0.8
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.ratio_of_actual_surface_area_to_projected_surface_area`'.format(value))
            if value < 0.8:
                raise ValueError('value need to be greater or equal 0.8 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.ratio_of_actual_surface_area_to_projected_surface_area`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.ratio_of_actual_surface_area_to_projected_surface_area`')
        self._data["Ratio of Actual Surface Area to Projected Surface Area"] = value

    @property
    def roughness_of_exterior_surface(self):
        """Get roughness_of_exterior_surface

        Returns:
            str: the value of `roughness_of_exterior_surface` or None if not set
        """
        return self._data["Roughness of Exterior Surface"]

    @roughness_of_exterior_surface.setter
    def roughness_of_exterior_surface(self, value=None):
        """  Corresponds to IDD Field `Roughness of Exterior Surface`

        Args:
            value (str): value for IDD Field `Roughness of Exterior Surface`
                Accepted values are:
                      - VeryRough
                      - Rough
                      - MediumRough
                      - MediumSmooth
                      - Smooth
                      - VerySmooth
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.roughness_of_exterior_surface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.roughness_of_exterior_surface`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.roughness_of_exterior_surface`')
            vals = {}
            vals["veryrough"] = "VeryRough"
            vals["rough"] = "Rough"
            vals["mediumrough"] = "MediumRough"
            vals["mediumsmooth"] = "MediumSmooth"
            vals["smooth"] = "Smooth"
            vals["verysmooth"] = "VerySmooth"
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
                                     'field `SurfacePropertyExteriorNaturalVentedCavity.roughness_of_exterior_surface`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `SurfacePropertyExteriorNaturalVentedCavity.roughness_of_exterior_surface`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Roughness of Exterior Surface"] = value

    @property
    def effectiveness_for_perforations_with_respect_to_wind(self):
        """Get effectiveness_for_perforations_with_respect_to_wind

        Returns:
            float: the value of `effectiveness_for_perforations_with_respect_to_wind` or None if not set
        """
        return self._data["Effectiveness for Perforations with Respect to Wind"]

    @effectiveness_for_perforations_with_respect_to_wind.setter
    def effectiveness_for_perforations_with_respect_to_wind(self, value=0.25):
        """  Corresponds to IDD Field `Effectiveness for Perforations with Respect to Wind`

        Args:
            value (float): value for IDD Field `Effectiveness for Perforations with Respect to Wind`
                Units: dimensionless
                Default value: 0.25
                value > 0.0
                value <= 1.5
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.effectiveness_for_perforations_with_respect_to_wind`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.effectiveness_for_perforations_with_respect_to_wind`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.effectiveness_for_perforations_with_respect_to_wind`')
        self._data["Effectiveness for Perforations with Respect to Wind"] = value

    @property
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self):
        """Get discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow

        Returns:
            float: the value of `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow` or None if not set
        """
        return self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"]

    @discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow.setter
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self, value=0.65):
        """  Corresponds to IDD Field `Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow`

        Args:
            value (float): value for IDD Field `Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow`
                Units: dimensionless
                Default value: 0.65
                value > 0.0
                value <= 1.5
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
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')
        self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = value

    def add_extensible(self,
                       surface_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            surface_1_name (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_surface_1_name(surface_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_surface_1_name(self, value):
        """ Validates falue of field `Surface 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `SurfacePropertyExteriorNaturalVentedCavity.surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertyExteriorNaturalVentedCavity.surface_1_name`')
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
                    raise ValueError("Required field SurfacePropertyExteriorNaturalVentedCavity:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertyExteriorNaturalVentedCavity:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertyExteriorNaturalVentedCavity: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertyExteriorNaturalVentedCavity: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class SurfacePropertySolarIncidentInside(object):
    """ Corresponds to IDD object `SurfaceProperty:SolarIncidentInside`
        Used to provide incident solar radiation on the inside of the surface. Reference surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedule instead of calculating it.
    """
    internal_name = "SurfaceProperty:SolarIncidentInside"
    field_count = 4
    required_fields = ["Name", "Surface Name", "Construction Name", "Inside Surface Incident Sun Solar Radiation Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:SolarIncidentInside`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Construction Name"] = None
        self._data["Inside Surface Incident Sun Solar Radiation Schedule Name"] = None
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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
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
            self.inside_surface_incident_sun_solar_radiation_schedule_name = None
        else:
            self.inside_surface_incident_sun_solar_radiation_schedule_name = vals[i]
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
                                 ' for field `SurfacePropertySolarIncidentInside.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertySolarIncidentInside.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertySolarIncidentInside.name`')
        self._data["Name"] = value

    @property
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`
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
                                 ' for field `SurfacePropertySolarIncidentInside.surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertySolarIncidentInside.surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertySolarIncidentInside.surface_name`')
        self._data["Surface Name"] = value

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
                                 ' for field `SurfacePropertySolarIncidentInside.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertySolarIncidentInside.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertySolarIncidentInside.construction_name`')
        self._data["Construction Name"] = value

    @property
    def inside_surface_incident_sun_solar_radiation_schedule_name(self):
        """Get inside_surface_incident_sun_solar_radiation_schedule_name

        Returns:
            str: the value of `inside_surface_incident_sun_solar_radiation_schedule_name` or None if not set
        """
        return self._data["Inside Surface Incident Sun Solar Radiation Schedule Name"]

    @inside_surface_incident_sun_solar_radiation_schedule_name.setter
    def inside_surface_incident_sun_solar_radiation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Inside Surface Incident Sun Solar Radiation Schedule Name`

        Args:
            value (str): value for IDD Field `Inside Surface Incident Sun Solar Radiation Schedule Name`
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
                                 ' for field `SurfacePropertySolarIncidentInside.inside_surface_incident_sun_solar_radiation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `SurfacePropertySolarIncidentInside.inside_surface_incident_sun_solar_radiation_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `SurfacePropertySolarIncidentInside.inside_surface_incident_sun_solar_radiation_schedule_name`')
        self._data["Inside Surface Incident Sun Solar Radiation Schedule Name"] = value

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
                    raise ValueError("Required field SurfacePropertySolarIncidentInside:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field SurfacePropertySolarIncidentInside:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for SurfacePropertySolarIncidentInside: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for SurfacePropertySolarIncidentInside: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class ComplexFenestrationPropertySolarAbsorbedLayers(object):
    """ Corresponds to IDD object `ComplexFenestrationProperty:SolarAbsorbedLayers`
        Used to provide solar radiation absorbed in fenestration layers. References surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedules instead of calculating it.
    """
    internal_name = "ComplexFenestrationProperty:SolarAbsorbedLayers"
    field_count = 8
    required_fields = ["Name", "Fenestration Surface", "Construction Name", "Layer 1 Solar Radiation Absorbed Schedule Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ComplexFenestrationProperty:SolarAbsorbedLayers`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fenestration Surface"] = None
        self._data["Construction Name"] = None
        self._data["Layer 1 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 2 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 3 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 4 Solar Radiation Absorbed Schedule Name"] = None
        self._data["Layer 5 Solar Radiation Absorbed Schedule Name"] = None
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
            self.fenestration_surface = None
        else:
            self.fenestration_surface = vals[i]
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
            self.layer_1_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_1_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.layer_2_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_2_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.layer_3_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_3_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.layer_4_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_4_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.layer_5_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_5_solar_radiation_absorbed_schedule_name = vals[i]
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.name`')
        self._data["Name"] = value

    @property
    def fenestration_surface(self):
        """Get fenestration_surface

        Returns:
            str: the value of `fenestration_surface` or None if not set
        """
        return self._data["Fenestration Surface"]

    @fenestration_surface.setter
    def fenestration_surface(self, value=None):
        """  Corresponds to IDD Field `Fenestration Surface`

        Args:
            value (str): value for IDD Field `Fenestration Surface`
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.fenestration_surface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.fenestration_surface`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.fenestration_surface`')
        self._data["Fenestration Surface"] = value

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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.construction_name`')
        self._data["Construction Name"] = value

    @property
    def layer_1_solar_radiation_absorbed_schedule_name(self):
        """Get layer_1_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_1_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 1 Solar Radiation Absorbed Schedule Name"]

    @layer_1_solar_radiation_absorbed_schedule_name.setter
    def layer_1_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Layer 1 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 1 Solar Radiation Absorbed Schedule Name`
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_1_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_1_solar_radiation_absorbed_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_1_solar_radiation_absorbed_schedule_name`')
        self._data["Layer 1 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_2_solar_radiation_absorbed_schedule_name(self):
        """Get layer_2_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_2_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 2 Solar Radiation Absorbed Schedule Name"]

    @layer_2_solar_radiation_absorbed_schedule_name.setter
    def layer_2_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Layer 2 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 2 Solar Radiation Absorbed Schedule Name`
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_2_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_2_solar_radiation_absorbed_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_2_solar_radiation_absorbed_schedule_name`')
        self._data["Layer 2 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_3_solar_radiation_absorbed_schedule_name(self):
        """Get layer_3_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_3_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 3 Solar Radiation Absorbed Schedule Name"]

    @layer_3_solar_radiation_absorbed_schedule_name.setter
    def layer_3_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Layer 3 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 3 Solar Radiation Absorbed Schedule Name`
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_3_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_3_solar_radiation_absorbed_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_3_solar_radiation_absorbed_schedule_name`')
        self._data["Layer 3 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_4_solar_radiation_absorbed_schedule_name(self):
        """Get layer_4_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_4_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 4 Solar Radiation Absorbed Schedule Name"]

    @layer_4_solar_radiation_absorbed_schedule_name.setter
    def layer_4_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Layer 4 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 4 Solar Radiation Absorbed Schedule Name`
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_4_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_4_solar_radiation_absorbed_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_4_solar_radiation_absorbed_schedule_name`')
        self._data["Layer 4 Solar Radiation Absorbed Schedule Name"] = value

    @property
    def layer_5_solar_radiation_absorbed_schedule_name(self):
        """Get layer_5_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_5_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 5 Solar Radiation Absorbed Schedule Name"]

    @layer_5_solar_radiation_absorbed_schedule_name.setter
    def layer_5_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Layer 5 Solar Radiation Absorbed Schedule Name`

        Args:
            value (str): value for IDD Field `Layer 5 Solar Radiation Absorbed Schedule Name`
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
                                 ' for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_5_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_5_solar_radiation_absorbed_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ComplexFenestrationPropertySolarAbsorbedLayers.layer_5_solar_radiation_absorbed_schedule_name`')
        self._data["Layer 5 Solar Radiation Absorbed Schedule Name"] = value

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
                    raise ValueError("Required field ComplexFenestrationPropertySolarAbsorbedLayers:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ComplexFenestrationPropertySolarAbsorbedLayers:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ComplexFenestrationPropertySolarAbsorbedLayers: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ComplexFenestrationPropertySolarAbsorbedLayers: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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

class ZonePropertyUserViewFactorsBySurfaceName(object):
    """ Corresponds to IDD object `ZoneProperty:UserViewFactors:bySurfaceName`
        View factors for Surface to Surface in a zone.
        (Number of Surfaces)**2 must be entered.
    """
    internal_name = "ZoneProperty:UserViewFactors:bySurfaceName"
    field_count = 1
    required_fields = []
    extensible_fields = 3
    format = "viewfactor"
    min_fields = 0
    extensible_keys = ["From Surface 1", "To Surface 1", "View Factor 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneProperty:UserViewFactors:bySurfaceName`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

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
                                 ' for field `ZonePropertyUserViewFactorsBySurfaceName.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.zone_name`')
        self._data["Zone Name"] = value

    def add_extensible(self,
                       from_surface_1=None,
                       to_surface_1=None,
                       view_factor_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            from_surface_1 (str): value for IDD Field `From Surface 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            to_surface_1 (str): value for IDD Field `To Surface 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            view_factor_1 (float): value for IDD Field `View Factor 1`
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_from_surface_1(from_surface_1))
        vals.append(self._check_to_surface_1(to_surface_1))
        vals.append(self._check_view_factor_1(view_factor_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_from_surface_1(self, value):
        """ Validates falue of field `From Surface 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZonePropertyUserViewFactorsBySurfaceName.from_surface_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.from_surface_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.from_surface_1`')
        return value

    def _check_to_surface_1(self, value):
        """ Validates falue of field `To Surface 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZonePropertyUserViewFactorsBySurfaceName.to_surface_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.to_surface_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.to_surface_1`')
        return value

    def _check_view_factor_1(self, value):
        """ Validates falue of field `View Factor 1`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `ZonePropertyUserViewFactorsBySurfaceName.view_factor_1`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `ZonePropertyUserViewFactorsBySurfaceName.view_factor_1`')
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
                    raise ValueError("Required field ZonePropertyUserViewFactorsBySurfaceName:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZonePropertyUserViewFactorsBySurfaceName:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZonePropertyUserViewFactorsBySurfaceName: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZonePropertyUserViewFactorsBySurfaceName: {} / {}".format(out_fields,
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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

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