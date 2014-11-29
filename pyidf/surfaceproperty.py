from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:HeatTransferAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

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
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ConductionTransferFunction")
            vals.add("MoisturePenetrationDepthConductionTransferFunction")
            vals.add("ConductionFiniteDifference")
            vals.add("CombinedHeatAndMoistureFiniteElement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:HeatTransferAlgorithm:MultipleSurface`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Type"] = None
        self._data["Algorithm"] = None

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
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
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
    def surface_type(self):
        """Get surface_type

        Returns:
            str: the value of `surface_type` or None if not set
        """
        return self._data["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """  Corresponds to IDD Field `surface_type`

        Args:
            value (str): value for IDD Field `surface_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_type`')
            vals = set()
            vals.add("AllExteriorSurfaces")
            vals.add("AllExteriorWalls")
            vals.add("AllExteriorRoofs")
            vals.add("AllExteriorFloors")
            vals.add("AllGroundContactSurfaces")
            vals.add("AllInteriorSurfaces")
            vals.add("AllInteriorWalls")
            vals.add("AllInteriorCeilings")
            vals.add("AllInteriorFloors")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `surface_type`'.format(value))

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
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ConductionTransferFunction")
            vals.add("MoisturePenetrationDepthConductionTransferFunction")
            vals.add("ConductionFiniteDifference")
            vals.add("CombinedHeatAndMoistureFiniteElement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

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
        out.append(self._to_str(self.surface_type))
        out.append(self._to_str(self.algorithm))
        return ",".join(out)

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
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:HeatTransferAlgorithm:SurfaceList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Algorithm"] = None
        self._data["Surface Name 1"] = None
        self._data["Surface Name 2"] = None
        self._data["Surface Name 3"] = None
        self._data["Surface Name 4"] = None
        self._data["Surface Name 5"] = None
        self._data["Surface Name 6"] = None

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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_1 = None
        else:
            self.surface_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_2 = None
        else:
            self.surface_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_3 = None
        else:
            self.surface_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_4 = None
        else:
            self.surface_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_5 = None
        else:
            self.surface_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_name_6 = None
        else:
            self.surface_name_6 = vals[i]
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
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ConductionTransferFunction")
            vals.add("MoisturePenetrationDepthConductionTransferFunction")
            vals.add("ConductionFiniteDifference")
            vals.add("CombinedHeatAndMoistureFiniteElement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

    @property
    def surface_name_1(self):
        """Get surface_name_1

        Returns:
            str: the value of `surface_name_1` or None if not set
        """
        return self._data["Surface Name 1"]

    @surface_name_1.setter
    def surface_name_1(self, value=None):
        """  Corresponds to IDD Field `surface_name_1`

        Args:
            value (str): value for IDD Field `surface_name_1`
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
                                 'for field `surface_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_1`')

        self._data["Surface Name 1"] = value

    @property
    def surface_name_2(self):
        """Get surface_name_2

        Returns:
            str: the value of `surface_name_2` or None if not set
        """
        return self._data["Surface Name 2"]

    @surface_name_2.setter
    def surface_name_2(self, value=None):
        """  Corresponds to IDD Field `surface_name_2`

        Args:
            value (str): value for IDD Field `surface_name_2`
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
                                 'for field `surface_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_2`')

        self._data["Surface Name 2"] = value

    @property
    def surface_name_3(self):
        """Get surface_name_3

        Returns:
            str: the value of `surface_name_3` or None if not set
        """
        return self._data["Surface Name 3"]

    @surface_name_3.setter
    def surface_name_3(self, value=None):
        """  Corresponds to IDD Field `surface_name_3`

        Args:
            value (str): value for IDD Field `surface_name_3`
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
                                 'for field `surface_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_3`')

        self._data["Surface Name 3"] = value

    @property
    def surface_name_4(self):
        """Get surface_name_4

        Returns:
            str: the value of `surface_name_4` or None if not set
        """
        return self._data["Surface Name 4"]

    @surface_name_4.setter
    def surface_name_4(self, value=None):
        """  Corresponds to IDD Field `surface_name_4`

        Args:
            value (str): value for IDD Field `surface_name_4`
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
                                 'for field `surface_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_4`')

        self._data["Surface Name 4"] = value

    @property
    def surface_name_5(self):
        """Get surface_name_5

        Returns:
            str: the value of `surface_name_5` or None if not set
        """
        return self._data["Surface Name 5"]

    @surface_name_5.setter
    def surface_name_5(self, value=None):
        """  Corresponds to IDD Field `surface_name_5`

        Args:
            value (str): value for IDD Field `surface_name_5`
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
                                 'for field `surface_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_5`')

        self._data["Surface Name 5"] = value

    @property
    def surface_name_6(self):
        """Get surface_name_6

        Returns:
            str: the value of `surface_name_6` or None if not set
        """
        return self._data["Surface Name 6"]

    @surface_name_6.setter
    def surface_name_6(self, value=None):
        """  Corresponds to IDD Field `surface_name_6`

        Args:
            value (str): value for IDD Field `surface_name_6`
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
                                 'for field `surface_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_6`')

        self._data["Surface Name 6"] = value

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
        out.append(self._to_str(self.algorithm))
        out.append(self._to_str(self.surface_name_1))
        out.append(self._to_str(self.surface_name_2))
        out.append(self._to_str(self.surface_name_3))
        out.append(self._to_str(self.surface_name_4))
        out.append(self._to_str(self.surface_name_5))
        out.append(self._to_str(self.surface_name_6))
        return ",".join(out)

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:HeatTransferAlgorithm:Construction`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Algorithm"] = None
        self._data["Construction Name"] = None

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
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
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
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ConductionTransferFunction")
            vals.add("MoisturePenetrationDepthConductionTransferFunction")
            vals.add("ConductionFiniteDifference")
            vals.add("CombinedHeatAndMoistureFiniteElement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

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
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

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
        out.append(self._to_str(self.algorithm))
        out.append(self._to_str(self.construction_name))
        return ",".join(out)

class SurfacePropertyOtherSideCoefficients(object):
    """ Corresponds to IDD object `SurfaceProperty:OtherSideCoefficients`
        This object sets the other side conditions for a surface in a variety of ways.
    """
    internal_name = "SurfaceProperty:OtherSideCoefficients"
    field_count = 14

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:OtherSideCoefficients`
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
            self.combined_convective_or_radiative_film_coefficient = None
        else:
            self.combined_convective_or_radiative_film_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_temperature = None
        else:
            self.constant_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_temperature_coefficient = None
        else:
            self.constant_temperature_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.external_drybulb_temperature_coefficient = None
        else:
            self.external_drybulb_temperature_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ground_temperature_coefficient = None
        else:
            self.ground_temperature_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_speed_coefficient = None
        else:
            self.wind_speed_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_air_temperature_coefficient = None
        else:
            self.zone_air_temperature_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_temperature_schedule_name = None
        else:
            self.constant_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sinusoidal_variation_of_constant_temperature_coefficient = None
        else:
            self.sinusoidal_variation_of_constant_temperature_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.period_of_sinusoidal_variation = None
        else:
            self.period_of_sinusoidal_variation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.previous_other_side_temperature_coefficient = None
        else:
            self.previous_other_side_temperature_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_other_side_temperature_limit = None
        else:
            self.minimum_other_side_temperature_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_other_side_temperature_limit = None
        else:
            self.maximum_other_side_temperature_limit = vals[i]
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
    def combined_convective_or_radiative_film_coefficient(self):
        """Get combined_convective_or_radiative_film_coefficient

        Returns:
            float: the value of `combined_convective_or_radiative_film_coefficient` or None if not set
        """
        return self._data["Combined Convective/Radiative Film Coefficient"]

    @combined_convective_or_radiative_film_coefficient.setter
    def combined_convective_or_radiative_film_coefficient(self, value=None):
        """  Corresponds to IDD Field `combined_convective_or_radiative_film_coefficient`
        if>0, this field becomes the exterior convective/radiative film coefficient
        and the other fields are used to calculate the outdoor air temperature
        then exterior surface temperature based on outdoor air and specified coefficient
        if<=0, then remaining fields calculate the outside surface temperature
        The following fields are used in the equation:
        OtherSideTemp=N2*N3 + N4*OutdoorDry-bulb + N5*GroundTemp + N6*WindSpeed*OutdoorDry-bulb + N7*TempZone + N9*TempPrev

        Args:
            value (float): value for IDD Field `combined_convective_or_radiative_film_coefficient`
                Unit: W/m2-K
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
                                 'for field `combined_convective_or_radiative_film_coefficient`'.format(value))

        self._data["Combined Convective/Radiative Film Coefficient"] = value

    @property
    def constant_temperature(self):
        """Get constant_temperature

        Returns:
            float: the value of `constant_temperature` or None if not set
        """
        return self._data["Constant Temperature"]

    @constant_temperature.setter
    def constant_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `constant_temperature`
        This parameter will be overwritten by the values from the Constant Temperature Schedule Name (below) if one is present

        Args:
            value (float): value for IDD Field `constant_temperature`
                Unit: C
                Default value: 0.0
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
                                 'for field `constant_temperature`'.format(value))

        self._data["Constant Temperature"] = value

    @property
    def constant_temperature_coefficient(self):
        """Get constant_temperature_coefficient

        Returns:
            float: the value of `constant_temperature_coefficient` or None if not set
        """
        return self._data["Constant Temperature Coefficient"]

    @constant_temperature_coefficient.setter
    def constant_temperature_coefficient(self, value=1.0 ):
        """  Corresponds to IDD Field `constant_temperature_coefficient`
        This coefficient is used even with a Schedule.  It should normally be 1.0 in that case.
        This field is ignored if Sinusoidal Variation of Constant Temperature Coefficient = Yes.

        Args:
            value (float): value for IDD Field `constant_temperature_coefficient`
                Default value: 1.0
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
                                 'for field `constant_temperature_coefficient`'.format(value))

        self._data["Constant Temperature Coefficient"] = value

    @property
    def external_drybulb_temperature_coefficient(self):
        """Get external_drybulb_temperature_coefficient

        Returns:
            float: the value of `external_drybulb_temperature_coefficient` or None if not set
        """
        return self._data["External Dry-Bulb Temperature Coefficient"]

    @external_drybulb_temperature_coefficient.setter
    def external_drybulb_temperature_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `external_drybulb_temperature_coefficient`

        Args:
            value (float): value for IDD Field `external_drybulb_temperature_coefficient`
                Default value: 0.0
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
                                 'for field `external_drybulb_temperature_coefficient`'.format(value))

        self._data["External Dry-Bulb Temperature Coefficient"] = value

    @property
    def ground_temperature_coefficient(self):
        """Get ground_temperature_coefficient

        Returns:
            float: the value of `ground_temperature_coefficient` or None if not set
        """
        return self._data["Ground Temperature Coefficient"]

    @ground_temperature_coefficient.setter
    def ground_temperature_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `ground_temperature_coefficient`

        Args:
            value (float): value for IDD Field `ground_temperature_coefficient`
                Default value: 0.0
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
                                 'for field `ground_temperature_coefficient`'.format(value))

        self._data["Ground Temperature Coefficient"] = value

    @property
    def wind_speed_coefficient(self):
        """Get wind_speed_coefficient

        Returns:
            float: the value of `wind_speed_coefficient` or None if not set
        """
        return self._data["Wind Speed Coefficient"]

    @wind_speed_coefficient.setter
    def wind_speed_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `wind_speed_coefficient`

        Args:
            value (float): value for IDD Field `wind_speed_coefficient`
                Default value: 0.0
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
                                 'for field `wind_speed_coefficient`'.format(value))

        self._data["Wind Speed Coefficient"] = value

    @property
    def zone_air_temperature_coefficient(self):
        """Get zone_air_temperature_coefficient

        Returns:
            float: the value of `zone_air_temperature_coefficient` or None if not set
        """
        return self._data["Zone Air Temperature Coefficient"]

    @zone_air_temperature_coefficient.setter
    def zone_air_temperature_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `zone_air_temperature_coefficient`

        Args:
            value (float): value for IDD Field `zone_air_temperature_coefficient`
                Default value: 0.0
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
                                 'for field `zone_air_temperature_coefficient`'.format(value))

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
        """  Corresponds to IDD Field `constant_temperature_schedule_name`
        Name of schedule for values of constant temperature.
        Schedule values replace any value specified in the field Constant Temperature.

        Args:
            value (str): value for IDD Field `constant_temperature_schedule_name`
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
                                 'for field `constant_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `constant_temperature_schedule_name`')

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
        """  Corresponds to IDD Field `sinusoidal_variation_of_constant_temperature_coefficient`
        Optionally used to vary Constant Temperature Coefficient with unitary sine wave

        Args:
            value (str): value for IDD Field `sinusoidal_variation_of_constant_temperature_coefficient`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sinusoidal_variation_of_constant_temperature_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sinusoidal_variation_of_constant_temperature_coefficient`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `sinusoidal_variation_of_constant_temperature_coefficient`'.format(value))

        self._data["Sinusoidal Variation of Constant Temperature Coefficient"] = value

    @property
    def period_of_sinusoidal_variation(self):
        """Get period_of_sinusoidal_variation

        Returns:
            float: the value of `period_of_sinusoidal_variation` or None if not set
        """
        return self._data["Period of Sinusoidal Variation"]

    @period_of_sinusoidal_variation.setter
    def period_of_sinusoidal_variation(self, value=24.0 ):
        """  Corresponds to IDD Field `period_of_sinusoidal_variation`
        Use with sinusoidal variation to define the time period

        Args:
            value (float): value for IDD Field `period_of_sinusoidal_variation`
                Unit: hr
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `period_of_sinusoidal_variation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `period_of_sinusoidal_variation`')

        self._data["Period of Sinusoidal Variation"] = value

    @property
    def previous_other_side_temperature_coefficient(self):
        """Get previous_other_side_temperature_coefficient

        Returns:
            float: the value of `previous_other_side_temperature_coefficient` or None if not set
        """
        return self._data["Previous Other Side Temperature Coefficient"]

    @previous_other_side_temperature_coefficient.setter
    def previous_other_side_temperature_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `previous_other_side_temperature_coefficient`
        This coefficient multiplies the other side temperature result from the
        previous zone timestep

        Args:
            value (float): value for IDD Field `previous_other_side_temperature_coefficient`
                Default value: 0.0
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
                                 'for field `previous_other_side_temperature_coefficient`'.format(value))

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
        """  Corresponds to IDD Field `minimum_other_side_temperature_limit`
        This field specifies a lower limit for the other side temperature result.
        Blank indicates no limit

        Args:
            value (float): value for IDD Field `minimum_other_side_temperature_limit`
                Unit: C
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
                                 'for field `minimum_other_side_temperature_limit`'.format(value))

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
        """  Corresponds to IDD Field `maximum_other_side_temperature_limit`
        This field specifies an upper limit for the other side temperature result.
        Blank indicates no limit

        Args:
            value (float): value for IDD Field `maximum_other_side_temperature_limit`
                Unit: C
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
                                 'for field `maximum_other_side_temperature_limit`'.format(value))

        self._data["Maximum Other Side Temperature Limit"] = value

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
        out.append(self._to_str(self.combined_convective_or_radiative_film_coefficient))
        out.append(self._to_str(self.constant_temperature))
        out.append(self._to_str(self.constant_temperature_coefficient))
        out.append(self._to_str(self.external_drybulb_temperature_coefficient))
        out.append(self._to_str(self.ground_temperature_coefficient))
        out.append(self._to_str(self.wind_speed_coefficient))
        out.append(self._to_str(self.zone_air_temperature_coefficient))
        out.append(self._to_str(self.constant_temperature_schedule_name))
        out.append(self._to_str(self.sinusoidal_variation_of_constant_temperature_coefficient))
        out.append(self._to_str(self.period_of_sinusoidal_variation))
        out.append(self._to_str(self.previous_other_side_temperature_coefficient))
        out.append(self._to_str(self.minimum_other_side_temperature_limit))
        out.append(self._to_str(self.maximum_other_side_temperature_limit))
        return ",".join(out)

class SurfacePropertyOtherSideConditionsModel(object):
    """ Corresponds to IDD object `SurfaceProperty:OtherSideConditionsModel`
        This object sets up modifying the other side conditions for a surface from other model results.
    """
    internal_name = "SurfaceProperty:OtherSideConditionsModel"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:OtherSideConditionsModel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Type of Modeling"] = None

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
            self.type_of_modeling = None
        else:
            self.type_of_modeling = vals[i]
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
    def type_of_modeling(self):
        """Get type_of_modeling

        Returns:
            str: the value of `type_of_modeling` or None if not set
        """
        return self._data["Type of Modeling"]

    @type_of_modeling.setter
    def type_of_modeling(self, value="GapConvectionRadiation"):
        """  Corresponds to IDD Field `type_of_modeling`
        GapConvectionRadiation provides boundary conditions for convection
        and linearized thermal radiation across a gap or cavity
        on the other side of the surface that are modeled sperately.
        UndergroundPipingSystemSurface provides boundary conditions for
        surfaces in contact with PipingSystem:Underground domains
        GroundCoupledSurface provides boundary conditions for surfaces
        in contact with GroundDomain objects

        Args:
            value (str): value for IDD Field `type_of_modeling`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_modeling`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_modeling`')
            vals = set()
            vals.add("GapConvectionRadiation")
            vals.add("UndergroundPipingSystemSurface")
            vals.add("GroundCoupledSurface")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `type_of_modeling`'.format(value))

        self._data["Type of Modeling"] = value

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
        out.append(self._to_str(self.type_of_modeling))
        return ",".join(out)

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:ConvectionCoefficients`
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

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_location = None
        else:
            self.convection_coefficient_1_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_type = None
        else:
            self.convection_coefficient_1_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1 = None
        else:
            self.convection_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_schedule_name = None
        else:
            self.convection_coefficient_1_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_user_curve_name = None
        else:
            self.convection_coefficient_1_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_location = None
        else:
            self.convection_coefficient_2_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_type = None
        else:
            self.convection_coefficient_2_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2 = None
        else:
            self.convection_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_schedule_name = None
        else:
            self.convection_coefficient_2_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_user_curve_name = None
        else:
            self.convection_coefficient_2_user_curve_name = vals[i]
        i += 1

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
    def convection_coefficient_1_location(self):
        """Get convection_coefficient_1_location

        Returns:
            str: the value of `convection_coefficient_1_location` or None if not set
        """
        return self._data["Convection Coefficient 1 Location"]

    @convection_coefficient_1_location.setter
    def convection_coefficient_1_location(self, value=None):
        """  Corresponds to IDD Field `convection_coefficient_1_location`

        Args:
            value (str): value for IDD Field `convection_coefficient_1_location`
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
                                 'for field `convection_coefficient_1_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_location`')
            vals = set()
            vals.add("Outside")
            vals.add("Inside")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_1_location`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1_type`

        Args:
            value (str): value for IDD Field `convection_coefficient_1_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convection_coefficient_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_type`')
            vals = set()
            vals.add("Value")
            vals.add("Schedule")
            vals.add("UserCurve")
            vals.add("Simple")
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("DOE-2")
            vals.add("MoWitt")
            vals.add("AdaptiveConvectionAlgorithm")
            vals.add("ASHRAEVerticalWall")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("FisherPedersenCeilingDiffuserCeiling")
            vals.add("FisherPedersenCeilingDiffuserFloor")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("KhalifaEq7Ceiling")
            vals.add("AwbiHattonHeatedFloor")
            vals.add("AwbiHattonHeatedWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("KaradagChilledCeiling")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserFloor")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("EmmelVertical")
            vals.add("EmmelRoof")
            vals.add("ClearRoof")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_1_type`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `convection_coefficient_1`
                Unit: W/m2-K
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
                                 'for field `convection_coefficient_1`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1_schedule_name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `convection_coefficient_1_schedule_name`
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
                                 'for field `convection_coefficient_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_schedule_name`')

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
        """  Corresponds to IDD Field `convection_coefficient_1_user_curve_name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `convection_coefficient_1_user_curve_name`
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
                                 'for field `convection_coefficient_1_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_user_curve_name`')

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
        """  Corresponds to IDD Field `convection_coefficient_2_location`

        Args:
            value (str): value for IDD Field `convection_coefficient_2_location`
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
                                 'for field `convection_coefficient_2_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_location`')
            vals = set()
            vals.add("Outside")
            vals.add("Inside")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_2_location`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_2_type`

        Args:
            value (str): value for IDD Field `convection_coefficient_2_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convection_coefficient_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_type`')
            vals = set()
            vals.add("Value")
            vals.add("Schedule")
            vals.add("UserCurve")
            vals.add("Simple")
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("DOE-2")
            vals.add("MoWitt")
            vals.add("AdaptiveConvectionAlgorithm")
            vals.add("ASHRAEVerticalWall")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("FisherPedersenCeilingDiffuserCeiling")
            vals.add("FisherPedersenCeilingDiffuserFloor")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("KhalifaEq7Ceiling")
            vals.add("AwbiHattonHeatedFloor")
            vals.add("AwbiHattonHeatedWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("KaradagChilledCeiling")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserFloor")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("EmmelVertical")
            vals.add("EmmelRoof")
            vals.add("ClearRoof")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_2_type`'.format(value))

        self._data["Convection Coefficient 2 Type"] = value

    @property
    def convection_coefficient_2(self):
        """Get convection_coefficient_2

        Returns:
            float: the value of `convection_coefficient_2` or None if not set
        """
        return self._data["Convection Coefficient 2"]

    @convection_coefficient_2.setter
    def convection_coefficient_2(self, value=0.1 ):
        """  Corresponds to IDD Field `convection_coefficient_2`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `convection_coefficient_2`
                Unit: W/m2-K
                Default value: 0.1
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
                                 'for field `convection_coefficient_2`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_2_schedule_name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `convection_coefficient_2_schedule_name`
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
                                 'for field `convection_coefficient_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_schedule_name`')

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
        """  Corresponds to IDD Field `convection_coefficient_2_user_curve_name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `convection_coefficient_2_user_curve_name`
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
                                 'for field `convection_coefficient_2_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_user_curve_name`')

        self._data["Convection Coefficient 2 User Curve Name"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.convection_coefficient_1_location))
        out.append(self._to_str(self.convection_coefficient_1_type))
        out.append(self._to_str(self.convection_coefficient_1))
        out.append(self._to_str(self.convection_coefficient_1_schedule_name))
        out.append(self._to_str(self.convection_coefficient_1_user_curve_name))
        out.append(self._to_str(self.convection_coefficient_2_location))
        out.append(self._to_str(self.convection_coefficient_2_type))
        out.append(self._to_str(self.convection_coefficient_2))
        out.append(self._to_str(self.convection_coefficient_2_schedule_name))
        out.append(self._to_str(self.convection_coefficient_2_user_curve_name))
        return ",".join(out)

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:ConvectionCoefficients:MultipleSurface`
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

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_location = None
        else:
            self.convection_coefficient_1_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_type = None
        else:
            self.convection_coefficient_1_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1 = None
        else:
            self.convection_coefficient_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_schedule_name = None
        else:
            self.convection_coefficient_1_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_1_user_curve_name = None
        else:
            self.convection_coefficient_1_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_location = None
        else:
            self.convection_coefficient_2_location = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_type = None
        else:
            self.convection_coefficient_2_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2 = None
        else:
            self.convection_coefficient_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_schedule_name = None
        else:
            self.convection_coefficient_2_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convection_coefficient_2_user_curve_name = None
        else:
            self.convection_coefficient_2_user_curve_name = vals[i]
        i += 1

    @property
    def surface_type(self):
        """Get surface_type

        Returns:
            str: the value of `surface_type` or None if not set
        """
        return self._data["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """  Corresponds to IDD Field `surface_type`

        Args:
            value (str): value for IDD Field `surface_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_type`')
            vals = set()
            vals.add("AllExteriorSurfaces")
            vals.add("AllExteriorWindows")
            vals.add("AllExteriorWalls")
            vals.add("AllExteriorRoofs")
            vals.add("AllExteriorFloors")
            vals.add("AllInteriorSurfaces")
            vals.add("AllInteriorWalls")
            vals.add("AllInteriorWindows")
            vals.add("AllInteriorCeilings")
            vals.add("AllInteriorFloors")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `surface_type`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1_location`

        Args:
            value (str): value for IDD Field `convection_coefficient_1_location`
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
                                 'for field `convection_coefficient_1_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_location`')
            vals = set()
            vals.add("Outside")
            vals.add("Inside")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_1_location`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1_type`

        Args:
            value (str): value for IDD Field `convection_coefficient_1_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convection_coefficient_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_type`')
            vals = set()
            vals.add("Value")
            vals.add("Schedule")
            vals.add("Simple")
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("DOE-2")
            vals.add("MoWitt")
            vals.add("AdaptiveConvectionAlgorithm")
            vals.add("ASHRAEVerticalWall")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("FisherPedersenCeilingDiffuserCeiling")
            vals.add("FisherPedersenCeilingDiffuserFloor")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("KhalifaEq7Ceiling")
            vals.add("AwbiHattonHeatedFloor")
            vals.add("AwbiHattonHeatedWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("KaradagChilledCeiling")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserFloor")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("BlockenWindard")
            vals.add("EmmelVertical")
            vals.add("EmmelRoof")
            vals.add("ClearRoof")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_1_type`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `convection_coefficient_1`
                Unit: W/m2-K
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
                                 'for field `convection_coefficient_1`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_1_schedule_name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `convection_coefficient_1_schedule_name`
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
                                 'for field `convection_coefficient_1_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_schedule_name`')

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
        """  Corresponds to IDD Field `convection_coefficient_1_user_curve_name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `convection_coefficient_1_user_curve_name`
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
                                 'for field `convection_coefficient_1_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_1_user_curve_name`')

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
        """  Corresponds to IDD Field `convection_coefficient_2_location`

        Args:
            value (str): value for IDD Field `convection_coefficient_2_location`
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
                                 'for field `convection_coefficient_2_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_location`')
            vals = set()
            vals.add("Outside")
            vals.add("Inside")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_2_location`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_2_type`

        Args:
            value (str): value for IDD Field `convection_coefficient_2_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convection_coefficient_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_type`')
            vals = set()
            vals.add("Value")
            vals.add("Schedule")
            vals.add("Simple")
            vals.add("SimpleCombined")
            vals.add("TARP")
            vals.add("DOE-2")
            vals.add("MoWitt")
            vals.add("AdaptiveConvectionAlgorithm")
            vals.add("ASHRAEVerticalWall")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("FisherPedersenCeilingDiffuserCeiling")
            vals.add("FisherPedersenCeilingDiffuserFloor")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("KhalifaEq7Ceiling")
            vals.add("AwbiHattonHeatedFloor")
            vals.add("AwbiHattonHeatedWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("KaradagChilledCeiling")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserFloor")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("BlockenWindard")
            vals.add("EmmelVertical")
            vals.add("EmmelRoof")
            vals.add("ClearRoof")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convection_coefficient_2_type`'.format(value))

        self._data["Convection Coefficient 2 Type"] = value

    @property
    def convection_coefficient_2(self):
        """Get convection_coefficient_2

        Returns:
            float: the value of `convection_coefficient_2` or None if not set
        """
        return self._data["Convection Coefficient 2"]

    @convection_coefficient_2.setter
    def convection_coefficient_2(self, value=0.1 ):
        """  Corresponds to IDD Field `convection_coefficient_2`
        used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (float): value for IDD Field `convection_coefficient_2`
                Unit: W/m2-K
                Default value: 0.1
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
                                 'for field `convection_coefficient_2`'.format(value))

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
        """  Corresponds to IDD Field `convection_coefficient_2_schedule_name`
        used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object.
        Default limits are Minimum >= 0.1 and Maximum <= 1000

        Args:
            value (str): value for IDD Field `convection_coefficient_2_schedule_name`
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
                                 'for field `convection_coefficient_2_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_schedule_name`')

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
        """  Corresponds to IDD Field `convection_coefficient_2_user_curve_name`
        used if Convection Type = UserCurve

        Args:
            value (str): value for IDD Field `convection_coefficient_2_user_curve_name`
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
                                 'for field `convection_coefficient_2_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convection_coefficient_2_user_curve_name`')

        self._data["Convection Coefficient 2 User Curve Name"] = value

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
        out.append(self._to_str(self.surface_type))
        out.append(self._to_str(self.convection_coefficient_1_location))
        out.append(self._to_str(self.convection_coefficient_1_type))
        out.append(self._to_str(self.convection_coefficient_1))
        out.append(self._to_str(self.convection_coefficient_1_schedule_name))
        out.append(self._to_str(self.convection_coefficient_1_user_curve_name))
        out.append(self._to_str(self.convection_coefficient_2_location))
        out.append(self._to_str(self.convection_coefficient_2_type))
        out.append(self._to_str(self.convection_coefficient_2))
        out.append(self._to_str(self.convection_coefficient_2_schedule_name))
        out.append(self._to_str(self.convection_coefficient_2_user_curve_name))
        return ",".join(out)

class SurfacePropertyExteriorNaturalVentedCavity(object):
    """ Corresponds to IDD object `SurfaceProperty:ExteriorNaturalVentedCavity`
        Used to describe the decoupled layer, or baffle, and the characteristics of the cavity
        and openings for naturally ventilated exterior surfaces. This object is also used in
        conjunction with the OtherSideConditionsModel.
    """
    internal_name = "SurfaceProperty:ExteriorNaturalVentedCavity"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:ExteriorNaturalVentedCavity`
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
        self._data["Surface 1 Name"] = None
        self._data["Surface 2 Name"] = None
        self._data["Surface 3 Name"] = None
        self._data["Surface 4 Name"] = None
        self._data["Surface 5 Name"] = None
        self._data["Surface 6 Name"] = None
        self._data["Surface 7 Name"] = None
        self._data["Surface 8 Name"] = None
        self._data["Surface 9 Name"] = None
        self._data["Surface 10 Name"] = None

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
            self.boundary_conditions_model_name = None
        else:
            self.boundary_conditions_model_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.area_fraction_of_openings = None
        else:
            self.area_fraction_of_openings = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermal_emissivity_of_exterior_baffle_material = None
        else:
            self.thermal_emissivity_of_exterior_baffle_material = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.solar_absorbtivity_of_exterior_baffle = None
        else:
            self.solar_absorbtivity_of_exterior_baffle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_scale_for_buoyancydriven_ventilation = None
        else:
            self.height_scale_for_buoyancydriven_ventilation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_thickness_of_cavity_behind_exterior_baffle = None
        else:
            self.effective_thickness_of_cavity_behind_exterior_baffle = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_actual_surface_area_to_projected_surface_area = None
        else:
            self.ratio_of_actual_surface_area_to_projected_surface_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.roughness_of_exterior_surface = None
        else:
            self.roughness_of_exterior_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effectiveness_for_perforations_with_respect_to_wind = None
        else:
            self.effectiveness_for_perforations_with_respect_to_wind = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = None
        else:
            self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_1_name = None
        else:
            self.surface_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_2_name = None
        else:
            self.surface_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_3_name = None
        else:
            self.surface_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_4_name = None
        else:
            self.surface_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_5_name = None
        else:
            self.surface_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_6_name = None
        else:
            self.surface_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_7_name = None
        else:
            self.surface_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_8_name = None
        else:
            self.surface_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_9_name = None
        else:
            self.surface_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_10_name = None
        else:
            self.surface_10_name = vals[i]
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
    def boundary_conditions_model_name(self):
        """Get boundary_conditions_model_name

        Returns:
            str: the value of `boundary_conditions_model_name` or None if not set
        """
        return self._data["Boundary Conditions Model Name"]

    @boundary_conditions_model_name.setter
    def boundary_conditions_model_name(self, value=None):
        """  Corresponds to IDD Field `boundary_conditions_model_name`
        Enter the name of a SurfaceProperty:OtherSideConditionsModel object

        Args:
            value (str): value for IDD Field `boundary_conditions_model_name`
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
                                 'for field `boundary_conditions_model_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `boundary_conditions_model_name`')

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
        """  Corresponds to IDD Field `area_fraction_of_openings`

        Args:
            value (float): value for IDD Field `area_fraction_of_openings`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `area_fraction_of_openings`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `area_fraction_of_openings`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `area_fraction_of_openings`')

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
        """  Corresponds to IDD Field `thermal_emissivity_of_exterior_baffle_material`

        Args:
            value (float): value for IDD Field `thermal_emissivity_of_exterior_baffle_material`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermal_emissivity_of_exterior_baffle_material`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `thermal_emissivity_of_exterior_baffle_material`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `thermal_emissivity_of_exterior_baffle_material`')

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
        """  Corresponds to IDD Field `solar_absorbtivity_of_exterior_baffle`

        Args:
            value (float): value for IDD Field `solar_absorbtivity_of_exterior_baffle`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `solar_absorbtivity_of_exterior_baffle`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `solar_absorbtivity_of_exterior_baffle`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `solar_absorbtivity_of_exterior_baffle`')

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
        """  Corresponds to IDD Field `height_scale_for_buoyancydriven_ventilation`

        Args:
            value (float): value for IDD Field `height_scale_for_buoyancydriven_ventilation`
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
                                 'for field `height_scale_for_buoyancydriven_ventilation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `height_scale_for_buoyancydriven_ventilation`')

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
        """  Corresponds to IDD Field `effective_thickness_of_cavity_behind_exterior_baffle`
        if corrugated, use average depth

        Args:
            value (float): value for IDD Field `effective_thickness_of_cavity_behind_exterior_baffle`
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
                                 'for field `effective_thickness_of_cavity_behind_exterior_baffle`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_thickness_of_cavity_behind_exterior_baffle`')

        self._data["Effective Thickness of Cavity Behind Exterior Baffle"] = value

    @property
    def ratio_of_actual_surface_area_to_projected_surface_area(self):
        """Get ratio_of_actual_surface_area_to_projected_surface_area

        Returns:
            float: the value of `ratio_of_actual_surface_area_to_projected_surface_area` or None if not set
        """
        return self._data["Ratio of Actual Surface Area to Projected Surface Area"]

    @ratio_of_actual_surface_area_to_projected_surface_area.setter
    def ratio_of_actual_surface_area_to_projected_surface_area(self, value=1.0 ):
        """  Corresponds to IDD Field `ratio_of_actual_surface_area_to_projected_surface_area`
        this parameter is used to help account for corrugations in the collector

        Args:
            value (float): value for IDD Field `ratio_of_actual_surface_area_to_projected_surface_area`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ratio_of_actual_surface_area_to_projected_surface_area`'.format(value))
            if value < 0.8:
                raise ValueError('value need to be greater or equal 0.8 '
                                 'for field `ratio_of_actual_surface_area_to_projected_surface_area`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `ratio_of_actual_surface_area_to_projected_surface_area`')

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
        """  Corresponds to IDD Field `roughness_of_exterior_surface`

        Args:
            value (str): value for IDD Field `roughness_of_exterior_surface`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `roughness_of_exterior_surface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roughness_of_exterior_surface`')
            vals = set()
            vals.add("VeryRough")
            vals.add("Rough")
            vals.add("MediumRough")
            vals.add("MediumSmooth")
            vals.add("Smooth")
            vals.add("VerySmooth")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `roughness_of_exterior_surface`'.format(value))

        self._data["Roughness of Exterior Surface"] = value

    @property
    def effectiveness_for_perforations_with_respect_to_wind(self):
        """Get effectiveness_for_perforations_with_respect_to_wind

        Returns:
            float: the value of `effectiveness_for_perforations_with_respect_to_wind` or None if not set
        """
        return self._data["Effectiveness for Perforations with Respect to Wind"]

    @effectiveness_for_perforations_with_respect_to_wind.setter
    def effectiveness_for_perforations_with_respect_to_wind(self, value=0.25 ):
        """  Corresponds to IDD Field `effectiveness_for_perforations_with_respect_to_wind`

        Args:
            value (float): value for IDD Field `effectiveness_for_perforations_with_respect_to_wind`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `effectiveness_for_perforations_with_respect_to_wind`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effectiveness_for_perforations_with_respect_to_wind`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `effectiveness_for_perforations_with_respect_to_wind`')

        self._data["Effectiveness for Perforations with Respect to Wind"] = value

    @property
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self):
        """Get discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow

        Returns:
            float: the value of `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow` or None if not set
        """
        return self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"]

    @discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow.setter
    def discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow(self, value=0.65 ):
        """  Corresponds to IDD Field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`

        Args:
            value (float): value for IDD Field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`
                Unit: dimensionless
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow`')

        self._data["Discharge Coefficient for Openings with Respect to Buoyancy Driven Flow"] = value

    @property
    def surface_1_name(self):
        """Get surface_1_name

        Returns:
            str: the value of `surface_1_name` or None if not set
        """
        return self._data["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """  Corresponds to IDD Field `surface_1_name`

        Args:
            value (str): value for IDD Field `surface_1_name`
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
                                 'for field `surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_1_name`')

        self._data["Surface 1 Name"] = value

    @property
    def surface_2_name(self):
        """Get surface_2_name

        Returns:
            str: the value of `surface_2_name` or None if not set
        """
        return self._data["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """  Corresponds to IDD Field `surface_2_name`

        Args:
            value (str): value for IDD Field `surface_2_name`
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
                                 'for field `surface_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_2_name`')

        self._data["Surface 2 Name"] = value

    @property
    def surface_3_name(self):
        """Get surface_3_name

        Returns:
            str: the value of `surface_3_name` or None if not set
        """
        return self._data["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """  Corresponds to IDD Field `surface_3_name`

        Args:
            value (str): value for IDD Field `surface_3_name`
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
                                 'for field `surface_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_3_name`')

        self._data["Surface 3 Name"] = value

    @property
    def surface_4_name(self):
        """Get surface_4_name

        Returns:
            str: the value of `surface_4_name` or None if not set
        """
        return self._data["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """  Corresponds to IDD Field `surface_4_name`

        Args:
            value (str): value for IDD Field `surface_4_name`
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
                                 'for field `surface_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_4_name`')

        self._data["Surface 4 Name"] = value

    @property
    def surface_5_name(self):
        """Get surface_5_name

        Returns:
            str: the value of `surface_5_name` or None if not set
        """
        return self._data["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """  Corresponds to IDD Field `surface_5_name`

        Args:
            value (str): value for IDD Field `surface_5_name`
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
                                 'for field `surface_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_5_name`')

        self._data["Surface 5 Name"] = value

    @property
    def surface_6_name(self):
        """Get surface_6_name

        Returns:
            str: the value of `surface_6_name` or None if not set
        """
        return self._data["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """  Corresponds to IDD Field `surface_6_name`

        Args:
            value (str): value for IDD Field `surface_6_name`
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
                                 'for field `surface_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_6_name`')

        self._data["Surface 6 Name"] = value

    @property
    def surface_7_name(self):
        """Get surface_7_name

        Returns:
            str: the value of `surface_7_name` or None if not set
        """
        return self._data["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """  Corresponds to IDD Field `surface_7_name`

        Args:
            value (str): value for IDD Field `surface_7_name`
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
                                 'for field `surface_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_7_name`')

        self._data["Surface 7 Name"] = value

    @property
    def surface_8_name(self):
        """Get surface_8_name

        Returns:
            str: the value of `surface_8_name` or None if not set
        """
        return self._data["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """  Corresponds to IDD Field `surface_8_name`

        Args:
            value (str): value for IDD Field `surface_8_name`
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
                                 'for field `surface_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_8_name`')

        self._data["Surface 8 Name"] = value

    @property
    def surface_9_name(self):
        """Get surface_9_name

        Returns:
            str: the value of `surface_9_name` or None if not set
        """
        return self._data["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """  Corresponds to IDD Field `surface_9_name`

        Args:
            value (str): value for IDD Field `surface_9_name`
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
                                 'for field `surface_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_9_name`')

        self._data["Surface 9 Name"] = value

    @property
    def surface_10_name(self):
        """Get surface_10_name

        Returns:
            str: the value of `surface_10_name` or None if not set
        """
        return self._data["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """  Corresponds to IDD Field `surface_10_name`

        Args:
            value (str): value for IDD Field `surface_10_name`
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
                                 'for field `surface_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_10_name`')

        self._data["Surface 10 Name"] = value

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
        out.append(self._to_str(self.boundary_conditions_model_name))
        out.append(self._to_str(self.area_fraction_of_openings))
        out.append(self._to_str(self.thermal_emissivity_of_exterior_baffle_material))
        out.append(self._to_str(self.solar_absorbtivity_of_exterior_baffle))
        out.append(self._to_str(self.height_scale_for_buoyancydriven_ventilation))
        out.append(self._to_str(self.effective_thickness_of_cavity_behind_exterior_baffle))
        out.append(self._to_str(self.ratio_of_actual_surface_area_to_projected_surface_area))
        out.append(self._to_str(self.roughness_of_exterior_surface))
        out.append(self._to_str(self.effectiveness_for_perforations_with_respect_to_wind))
        out.append(self._to_str(self.discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow))
        out.append(self._to_str(self.surface_1_name))
        out.append(self._to_str(self.surface_2_name))
        out.append(self._to_str(self.surface_3_name))
        out.append(self._to_str(self.surface_4_name))
        out.append(self._to_str(self.surface_5_name))
        out.append(self._to_str(self.surface_6_name))
        out.append(self._to_str(self.surface_7_name))
        out.append(self._to_str(self.surface_8_name))
        out.append(self._to_str(self.surface_9_name))
        out.append(self._to_str(self.surface_10_name))
        return ",".join(out)

class SurfacePropertySolarIncidentInside(object):
    """ Corresponds to IDD object `SurfaceProperty:SolarIncidentInside`
        Used to provide incident solar radiation on the inside of the surface. Reference surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedule instead of calculating it.
    """
    internal_name = "SurfaceProperty:SolarIncidentInside"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperty:SolarIncidentInside`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Construction Name"] = None
        self._data["Inside Surface Incident Sun Solar Radiation Schedule Name"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_surface_incident_sun_solar_radiation_schedule_name = None
        else:
            self.inside_surface_incident_sun_solar_radiation_schedule_name = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

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
        """  Corresponds to IDD Field `inside_surface_incident_sun_solar_radiation_schedule_name`

        Args:
            value (str): value for IDD Field `inside_surface_incident_sun_solar_radiation_schedule_name`
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
                                 'for field `inside_surface_incident_sun_solar_radiation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inside_surface_incident_sun_solar_radiation_schedule_name`')

        self._data["Inside Surface Incident Sun Solar Radiation Schedule Name"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.inside_surface_incident_sun_solar_radiation_schedule_name))
        return ",".join(out)