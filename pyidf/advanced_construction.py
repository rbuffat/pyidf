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
    required_fields = ["Surface Name", "Algorithm"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm`
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
    required_fields = ["Name", "Surface Type", "Algorithm"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm:MultipleSurface`
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
    required_fields = ["Name", "Algorithm", "Surface Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm:SurfaceList`
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
    required_fields = ["Algorithm", "Construction Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:HeatTransferAlgorithm:Construction`
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.algorithm))
        out.append(self._to_str(self.construction_name))
        return ",".join(out)

class SurfaceControlMovableInsulation(object):
    """ Corresponds to IDD object `SurfaceControl:MovableInsulation`
        Exterior or Interior Insulation on opaque surfaces
    
    """
    internal_name = "SurfaceControl:MovableInsulation"
    field_count = 4
    required_fields = ["Insulation Type", "Surface Name", "Material Name", "Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceControl:MovableInsulation`
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.insulation_type))
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.material_name))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class SurfacePropertyOtherSideCoefficients(object):
    """ Corresponds to IDD object `SurfaceProperty:OtherSideCoefficients`
        This object sets the other side conditions for a surface in a variety of ways.
    
    """
    internal_name = "SurfaceProperty:OtherSideCoefficients"
    field_count = 14
    required_fields = ["Name", "Combined Convective/Radiative Film Coefficient"]

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
                Units: W/m2-K
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
                Units: C
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
                Units: C
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
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:OtherSideConditionsModel`
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.type_of_modeling))
        return ",".join(out)

class SurfaceConvectionAlgorithmInsideAdaptiveModelSelections(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the inside face, the side of the surface facing a thermal zone.
    
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections"
    field_count = 91
    required_fields = []

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
            self.simple_bouyancy_vertical_wall_equation_source = None
        else:
            self.simple_bouyancy_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_vertical_wall_user_curve_name = None
        else:
            self.simple_bouyancy_vertical_wall_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_horizontal_equation_source = None
        else:
            self.simple_bouyancy_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_horizontal_equation_user_curve_name = None
        else:
            self.simple_bouyancy_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_horizontal_equation_source = None
        else:
            self.simple_bouyancy_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_horizontal_equation_user_curve_name = None
        else:
            self.simple_bouyancy_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_tilted_equation_source = None
        else:
            self.simple_bouyancy_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_stable_tilted_equation_user_curve_name = None
        else:
            self.simple_bouyancy_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_tilted_equation_source = None
        else:
            self.simple_bouyancy_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_unstable_tilted_equation_user_curve_name = None
        else:
            self.simple_bouyancy_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_windows_equation_source = None
        else:
            self.simple_bouyancy_windows_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.simple_bouyancy_windows_equation_user_curve_name = None
        else:
            self.simple_bouyancy_windows_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_vertical_wall_equation_source = None
        else:
            self.floor_heat_ceiling_cool_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_source = None
        else:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_source = None
        else:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_heated_floor_equation_source = None
        else:
            self.floor_heat_ceiling_cool_heated_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_source = None
        else:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_tilted_equation_source = None
        else:
            self.floor_heat_ceiling_cool_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_source = None
        else:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_window_equation_source = None
        else:
            self.floor_heat_ceiling_cool_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.floor_heat_ceiling_cool_window_equation_user_curve_name = None
        else:
            self.floor_heat_ceiling_cool_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_vertical_wall_equation_source = None
        else:
            self.wall_panel_heating_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_vertical_wall_equation_user_curve_name = None
        else:
            self.wall_panel_heating_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_heated_wall_equation_source = None
        else:
            self.wall_panel_heating_heated_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_heated_wall_equation_user_curve_name = None
        else:
            self.wall_panel_heating_heated_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_horizontal_equation_source = None
        else:
            self.wall_panel_heating_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_horizontal_equation_user_curve_name = None
        else:
            self.wall_panel_heating_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_horizontal_equation_source = None
        else:
            self.wall_panel_heating_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_horizontal_equation_user_curve_name = None
        else:
            self.wall_panel_heating_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_tilted_equation_source = None
        else:
            self.wall_panel_heating_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_stable_tilted_equation_user_curve_name = None
        else:
            self.wall_panel_heating_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_tilted_equation_source = None
        else:
            self.wall_panel_heating_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_unstable_tilted_equation_user_curve_name = None
        else:
            self.wall_panel_heating_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_window_equation_source = None
        else:
            self.wall_panel_heating_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wall_panel_heating_window_equation_user_curve_name = None
        else:
            self.wall_panel_heating_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_wall_equation_source = None
        else:
            self.convective_zone_heater_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_wall_equation_user_curve_name = None
        else:
            self.convective_zone_heater_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_walls_near_heater_equation_source = None
        else:
            self.convective_zone_heater_vertical_walls_near_heater_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = None
        else:
            self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_horizontal_equation_source = None
        else:
            self.convective_zone_heater_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_horizontal_equation_user_curve_name = None
        else:
            self.convective_zone_heater_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_horizontal_equation_source = None
        else:
            self.convective_zone_heater_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_horizontal_equation_user_curve_name = None
        else:
            self.convective_zone_heater_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_tilted_equation_source = None
        else:
            self.convective_zone_heater_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_stable_tilted_equation_user_curve_name = None
        else:
            self.convective_zone_heater_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_tilted_equation_source = None
        else:
            self.convective_zone_heater_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_unstable_tilted_equation_user_curve_name = None
        else:
            self.convective_zone_heater_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_windows_equation_source = None
        else:
            self.convective_zone_heater_windows_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.convective_zone_heater_windows_equation_user_curve_name = None
        else:
            self.convective_zone_heater_windows_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_wall_equation_source = None
        else:
            self.central_air_diffuser_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_wall_equation_user_curve_name = None
        else:
            self.central_air_diffuser_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_ceiling_equation_source = None
        else:
            self.central_air_diffuser_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_ceiling_equation_user_curve_name = None
        else:
            self.central_air_diffuser_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_floor_equation_source = None
        else:
            self.central_air_diffuser_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_floor_equation_user_curve_name = None
        else:
            self.central_air_diffuser_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_window_equation_source = None
        else:
            self.central_air_diffuser_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.central_air_diffuser_window_equation_user_curve_name = None
        else:
            self.central_air_diffuser_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_window_equation_source = None
        else:
            self.mechanical_zone_fan_circulation_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mechanical_zone_fan_circulation_window_equation_user_curve_name = None
        else:
            self.mechanical_zone_fan_circulation_window_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source = None
        else:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name = None
        else:
            self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source = None
        else:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name = None
        else:
            self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_floor_equation_source = None
        else:
            self.mixed_regime_stable_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_floor_equation_user_curve_name = None
        else:
            self.mixed_regime_stable_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_floor_equation_source = None
        else:
            self.mixed_regime_unstable_floor_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_floor_equation_user_curve_name = None
        else:
            self.mixed_regime_unstable_floor_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_ceiling_equation_source = None
        else:
            self.mixed_regime_stable_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_stable_ceiling_equation_user_curve_name = None
        else:
            self.mixed_regime_stable_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_ceiling_equation_source = None
        else:
            self.mixed_regime_unstable_ceiling_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_unstable_ceiling_equation_user_curve_name = None
        else:
            self.mixed_regime_unstable_ceiling_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_window_equation_source = None
        else:
            self.mixed_regime_window_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mixed_regime_window_equation_user_curve_name = None
        else:
            self.mixed_regime_window_equation_user_curve_name = vals[i]
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
    def simple_bouyancy_vertical_wall_equation_source(self):
        """Get simple_bouyancy_vertical_wall_equation_source

        Returns:
            str: the value of `simple_bouyancy_vertical_wall_equation_source` or None if not set
        """
        return self._data["Simple Bouyancy Vertical Wall Equation Source"]

    @simple_bouyancy_vertical_wall_equation_source.setter
    def simple_bouyancy_vertical_wall_equation_source(self, value="FohannoPolidoriVerticalWall"):
        """  Corresponds to IDD Field `simple_bouyancy_vertical_wall_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for vertical walls

        Args:
            value (str): value for IDD Field `simple_bouyancy_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `simple_bouyancy_vertical_wall_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_vertical_wall_user_curve_name`
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
                                 'for field `simple_bouyancy_vertical_wall_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_vertical_wall_user_curve_name`')

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
        """  Corresponds to IDD Field `simple_bouyancy_stable_horizontal_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_stable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `simple_bouyancy_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_horizontal_equation_user_curve_name`
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
                                 'for field `simple_bouyancy_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `simple_bouyancy_unstable_horizontal_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for passive horizontal surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_unstable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`
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
                                 'for field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `simple_bouyancy_stable_tilted_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_stable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `simple_bouyancy_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_stable_tilted_equation_user_curve_name`
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
                                 'for field `simple_bouyancy_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_stable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `simple_bouyancy_unstable_tilted_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_unstable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `simple_bouyancy_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_unstable_tilted_equation_user_curve_name`
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
                                 'for field `simple_bouyancy_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_unstable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `simple_bouyancy_windows_equation_source`
        Applies to zone with no HVAC or when HVAC is off
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `simple_bouyancy_windows_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `simple_bouyancy_windows_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_windows_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("KaradagChilledCeiling")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `simple_bouyancy_windows_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `simple_bouyancy_windows_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `simple_bouyancy_windows_equation_user_curve_name`
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
                                 'for field `simple_bouyancy_windows_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `simple_bouyancy_windows_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for vertical walls

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for passive horizontal surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_stable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for passive horizontal surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_unstable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_heated_floor_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for a floor with active heating elements

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_heated_floor_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("AwbiHattonHeatedFloor")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_heated_floor_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_heated_floor_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for a ceiling with active cooling elements

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KaradagChilledCeiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_chilled_ceiling_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_stable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_unstable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_window_equation_source`
        Applies to zone with in-floor heating and/or in-ceiling cooling
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_window_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_heat_ceiling_cool_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `floor_heat_ceiling_cool_window_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `floor_heat_ceiling_cool_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `floor_heat_ceiling_cool_window_equation_user_curve_name`
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
                                 'for field `floor_heat_ceiling_cool_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_heat_ceiling_cool_window_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_vertical_wall_equation_source`
        Applies to zone with in-wall panel heating
        This is for vertical walls that are not actively heated

        Args:
            value (str): value for IDD Field `wall_panel_heating_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_vertical_wall_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_vertical_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_heated_wall_equation_source`
        Applies to zone with in-wall panel heating
        This is for vertical walls that are being actively heated

        Args:
            value (str): value for IDD Field `wall_panel_heating_heated_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_heated_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_heated_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("AwbiHattonHeatedWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_heated_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_heated_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_heated_wall_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_heated_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_heated_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_stable_horizontal_equation_source`
        Applies to zone with in-wall panel heating
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_stable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_horizontal_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_unstable_horizontal_equation_source`
        Applies to zone with in-wall panel heating
        This is for horizontal surfaces with heat flow directed for unstable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KhalifaEq7Ceiling")
            vals.add("KaradagChilledCeiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_unstable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_stable_tilted_equation_source`
        Applies to zone with in-wall panel heating
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_stable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_stable_tilted_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_stable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_unstable_tilted_equation_source`
        Applies to zone with in-wall panel heating
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_unstable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_unstable_tilted_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_unstable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wall_panel_heating_window_equation_source`
        Applies to zone with in-wall panel heating
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `wall_panel_heating_window_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wall_panel_heating_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wall_panel_heating_window_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wall_panel_heating_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wall_panel_heating_window_equation_user_curve_name`
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
                                 'for field `wall_panel_heating_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wall_panel_heating_window_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_vertical_wall_equation_source`
        Applies to zone with convective heater
        This is for vertical walls not directly affected by heater

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("KhalifaEq6NonHeatedWalls")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_wall_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_source`
        Applies to zone with convective heater
        This is for vertical walls that are directly affected by heater
        Walls are considered "near" when listed in field set for Fraction of Radiant Energy to Surface

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq5WallNearHeat")
            vals.add("AwbiHattonHeatedWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_vertical_walls_near_heater_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_stable_horizontal_equation_source`
        Applies to zone with convective heater
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_stable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_horizontal_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_unstable_horizontal_equation_source`
        Applies to zone with convective heater
        This is for horizontal surfaces with heat flow directed for unstable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("KhalifaEq7Ceiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_unstable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_stable_tilted_equation_source`
        Applies to zone with convective heater
        This is for tilted surfaces with heat flow for stable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_stable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_stable_tilted_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_stable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_unstable_tilted_equation_source`
        Applies to zone with convective heater
        This is for tilted surfaces with heat flow for unstable thermal stratification

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_unstable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_unstable_tilted_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_unstable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `convective_zone_heater_windows_equation_source`
        Applies to zone with convective heater
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `convective_zone_heater_windows_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `convective_zone_heater_windows_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_windows_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `convective_zone_heater_windows_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `convective_zone_heater_windows_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `convective_zone_heater_windows_equation_user_curve_name`
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
                                 'for field `convective_zone_heater_windows_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `convective_zone_heater_windows_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `central_air_diffuser_wall_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all wall surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `central_air_diffuser_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_wall_equation_user_curve_name`
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
                                 'for field `central_air_diffuser_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `central_air_diffuser_ceiling_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all ceiling surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_ceiling_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_ceiling_equation_source`')
            vals = set()
            vals.add("FisherPedersenCeilingDiffuserCeiling")
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_ceiling_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `central_air_diffuser_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_ceiling_equation_user_curve_name`
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
                                 'for field `central_air_diffuser_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_ceiling_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `central_air_diffuser_floor_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all floor surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_floor_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_floor_equation_source`')
            vals = set()
            vals.add("FisherPedersenCeilingDiffuserFloor")
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("GoldsteinNovoselacCeilingDiffuserFloor")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_floor_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `central_air_diffuser_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_floor_equation_user_curve_name`
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
                                 'for field `central_air_diffuser_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_floor_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `central_air_diffuser_window_equation_source`
        Applies to zone with mechanical forced central air with diffusers
        This is for all window surfaces

        Args:
            value (str): value for IDD Field `central_air_diffuser_window_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `central_air_diffuser_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `central_air_diffuser_window_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `central_air_diffuser_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `central_air_diffuser_window_equation_user_curve_name`
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
                                 'for field `central_air_diffuser_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `central_air_diffuser_window_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_source`')
            vals = set()
            vals.add("KhalifaEq3WallAwayFromHeat")
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`
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
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_stable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`
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
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("KhalifaEq4CeilingAwayFromHeat")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_unstable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`
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
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_stable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`
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
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_unstable_tilted_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`
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
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_window_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_window_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mechanical_zone_fan_circulation_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_window_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mechanical_zone_fan_circulation_window_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mechanical_zone_fan_circulation_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mechanical_zone_fan_circulation_window_equation_user_curve_name`
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
                                 'for field `mechanical_zone_fan_circulation_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mechanical_zone_fan_circulation_window_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedAssistedWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`
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
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedOpposingWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ASHRAEVerticalWall")
            vals.add("FisherPedersenCeilingDiffuserWalls")
            vals.add("GoldsteinNovoselacCeilingDiffuserWalls")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`
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
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_stable_floor_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_stable_floor_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_stable_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_floor_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedStableFloor")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_stable_floor_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_stable_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_stable_floor_equation_user_curve_name`
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
                                 'for field `mixed_regime_stable_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_floor_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_unstable_floor_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_floor_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_unstable_floor_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_floor_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedUnstableFloor")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_unstable_floor_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_unstable_floor_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_floor_equation_user_curve_name`
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
                                 'for field `mixed_regime_unstable_floor_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_floor_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_stable_ceiling_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_stable_ceiling_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_stable_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_ceiling_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedStableCeiling")
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_stable_ceiling_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_stable_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_stable_ceiling_equation_user_curve_name`
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
                                 'for field `mixed_regime_stable_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_stable_ceiling_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_unstable_ceiling_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_ceiling_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_unstable_ceiling_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_ceiling_equation_source`')
            vals = set()
            vals.add("BeausoleilMorrisonMixedUnstableCeiling")
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_unstable_ceiling_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_unstable_ceiling_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_unstable_ceiling_equation_user_curve_name`
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
                                 'for field `mixed_regime_unstable_ceiling_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_unstable_ceiling_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `mixed_regime_window_equation_source`
        reference choice fields

        Args:
            value (str): value for IDD Field `mixed_regime_window_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `mixed_regime_window_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_window_equation_source`')
            vals = set()
            vals.add("GoldsteinNovoselacCeilingDiffuserWindow")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `mixed_regime_window_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `mixed_regime_window_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `mixed_regime_window_equation_user_curve_name`
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
                                 'for field `mixed_regime_window_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `mixed_regime_window_equation_user_curve_name`')

        self._data["Mixed Regime Window Equation User Curve Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.simple_bouyancy_vertical_wall_equation_source))
        out.append(self._to_str(self.simple_bouyancy_vertical_wall_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_stable_horizontal_equation_source))
        out.append(self._to_str(self.simple_bouyancy_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_unstable_horizontal_equation_source))
        out.append(self._to_str(self.simple_bouyancy_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_stable_tilted_equation_source))
        out.append(self._to_str(self.simple_bouyancy_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_unstable_tilted_equation_source))
        out.append(self._to_str(self.simple_bouyancy_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.simple_bouyancy_windows_equation_source))
        out.append(self._to_str(self.simple_bouyancy_windows_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_vertical_wall_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_horizontal_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_horizontal_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_heated_floor_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_heated_floor_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_chilled_ceiling_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_tilted_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_tilted_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.floor_heat_ceiling_cool_window_equation_source))
        out.append(self._to_str(self.floor_heat_ceiling_cool_window_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_vertical_wall_equation_source))
        out.append(self._to_str(self.wall_panel_heating_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_heated_wall_equation_source))
        out.append(self._to_str(self.wall_panel_heating_heated_wall_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_stable_horizontal_equation_source))
        out.append(self._to_str(self.wall_panel_heating_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_unstable_horizontal_equation_source))
        out.append(self._to_str(self.wall_panel_heating_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_stable_tilted_equation_source))
        out.append(self._to_str(self.wall_panel_heating_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_unstable_tilted_equation_source))
        out.append(self._to_str(self.wall_panel_heating_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.wall_panel_heating_window_equation_source))
        out.append(self._to_str(self.wall_panel_heating_window_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_vertical_wall_equation_source))
        out.append(self._to_str(self.convective_zone_heater_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_vertical_walls_near_heater_equation_source))
        out.append(self._to_str(self.convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_stable_horizontal_equation_source))
        out.append(self._to_str(self.convective_zone_heater_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_unstable_horizontal_equation_source))
        out.append(self._to_str(self.convective_zone_heater_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_stable_tilted_equation_source))
        out.append(self._to_str(self.convective_zone_heater_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_unstable_tilted_equation_source))
        out.append(self._to_str(self.convective_zone_heater_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.convective_zone_heater_windows_equation_source))
        out.append(self._to_str(self.convective_zone_heater_windows_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_wall_equation_source))
        out.append(self._to_str(self.central_air_diffuser_wall_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_ceiling_equation_source))
        out.append(self._to_str(self.central_air_diffuser_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_floor_equation_source))
        out.append(self._to_str(self.central_air_diffuser_floor_equation_user_curve_name))
        out.append(self._to_str(self.central_air_diffuser_window_equation_source))
        out.append(self._to_str(self.central_air_diffuser_window_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_vertical_wall_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_horizontal_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_horizontal_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_tilted_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_tilted_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_window_equation_source))
        out.append(self._to_str(self.mechanical_zone_fan_circulation_window_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_source))
        out.append(self._to_str(self.mixed_regime_bouyancy_assisting_flow_on_walls_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_source))
        out.append(self._to_str(self.mixed_regime_bouyancy_oppossing_flow_on_walls_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_stable_floor_equation_source))
        out.append(self._to_str(self.mixed_regime_stable_floor_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_unstable_floor_equation_source))
        out.append(self._to_str(self.mixed_regime_unstable_floor_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_stable_ceiling_equation_source))
        out.append(self._to_str(self.mixed_regime_stable_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_unstable_ceiling_equation_source))
        out.append(self._to_str(self.mixed_regime_unstable_ceiling_equation_user_curve_name))
        out.append(self._to_str(self.mixed_regime_window_equation_source))
        out.append(self._to_str(self.mixed_regime_window_equation_user_curve_name))
        return ",".join(out)

class SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections`
        Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm
        This object is only needed to make changes to the default model selections for any or all of the surface categories.
        This object is for the outside face, the side of the surface facing away from the thermal zone.
    
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections"
    field_count = 13
    required_fields = []

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
            self.wind_convection_windward_vertical_wall_equation_source = None
        else:
            self.wind_convection_windward_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_windward_equation_vertical_wall_user_curve_name = None
        else:
            self.wind_convection_windward_equation_vertical_wall_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_leeward_vertical_wall_equation_source = None
        else:
            self.wind_convection_leeward_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_leeward_vertical_wall_equation_user_curve_name = None
        else:
            self.wind_convection_leeward_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_horizontal_roof_equation_source = None
        else:
            self.wind_convection_horizontal_roof_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_convection_horizontal_roof_user_curve_name = None
        else:
            self.wind_convection_horizontal_roof_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_vertical_wall_equation_source = None
        else:
            self.natural_convection_vertical_wall_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_vertical_wall_equation_user_curve_name = None
        else:
            self.natural_convection_vertical_wall_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_stable_horizontal_equation_source = None
        else:
            self.natural_convection_stable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_stable_horizontal_equation_user_curve_name = None
        else:
            self.natural_convection_stable_horizontal_equation_user_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_unstable_horizontal_equation_source = None
        else:
            self.natural_convection_unstable_horizontal_equation_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.natural_convection_unstable_horizontal_equation_user_curve_name = None
        else:
            self.natural_convection_unstable_horizontal_equation_user_curve_name = vals[i]
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
    def wind_convection_windward_vertical_wall_equation_source(self):
        """Get wind_convection_windward_vertical_wall_equation_source

        Returns:
            str: the value of `wind_convection_windward_vertical_wall_equation_source` or None if not set
        """
        return self._data["Wind Convection Windward Vertical Wall Equation Source"]

    @wind_convection_windward_vertical_wall_equation_source.setter
    def wind_convection_windward_vertical_wall_equation_source(self, value="TARPWindward"):
        """  Corresponds to IDD Field `wind_convection_windward_vertical_wall_equation_source`

        Args:
            value (str): value for IDD Field `wind_convection_windward_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_windward_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_windward_vertical_wall_equation_source`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARPWindward")
            vals.add("MoWiTTWindward")
            vals.add("DOE2Windward")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("BlockenWindward")
            vals.add("EmmelVertical")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_convection_windward_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wind_convection_windward_equation_vertical_wall_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wind_convection_windward_equation_vertical_wall_user_curve_name`
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
                                 'for field `wind_convection_windward_equation_vertical_wall_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_windward_equation_vertical_wall_user_curve_name`')

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
        """  Corresponds to IDD Field `wind_convection_leeward_vertical_wall_equation_source`

        Args:
            value (str): value for IDD Field `wind_convection_leeward_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_leeward_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_leeward_vertical_wall_equation_source`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARPLeeward")
            vals.add("MoWiTTLeeward")
            vals.add("DOE2Leeward")
            vals.add("EmmelVertical")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_convection_leeward_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wind_convection_leeward_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wind_convection_leeward_vertical_wall_equation_user_curve_name`
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
                                 'for field `wind_convection_leeward_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_leeward_vertical_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `wind_convection_horizontal_roof_equation_source`

        Args:
            value (str): value for IDD Field `wind_convection_horizontal_roof_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_convection_horizontal_roof_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_horizontal_roof_equation_source`')
            vals = set()
            vals.add("SimpleCombined")
            vals.add("TARPWindward")
            vals.add("MoWiTTWindward")
            vals.add("DOE2Windward")
            vals.add("NusseltJurges")
            vals.add("McAdams")
            vals.add("Mitchell")
            vals.add("BlockenWindward")
            vals.add("EmmelRoof")
            vals.add("ClearRoof")
            vals.add("UserCurve")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_convection_horizontal_roof_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `wind_convection_horizontal_roof_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `wind_convection_horizontal_roof_user_curve_name`
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
                                 'for field `wind_convection_horizontal_roof_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_convection_horizontal_roof_user_curve_name`')

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
        """  Corresponds to IDD Field `natural_convection_vertical_wall_equation_source`
        This is for vertical walls

        Args:
            value (str): value for IDD Field `natural_convection_vertical_wall_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_vertical_wall_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_vertical_wall_equation_source`')
            vals = set()
            vals.add("ASHRAEVerticalWall")
            vals.add("AlamdariHammondVerticalWall")
            vals.add("FohannoPolidoriVerticalWall")
            vals.add("ISO15099Windows")
            vals.add("UserCurve")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `natural_convection_vertical_wall_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `natural_convection_vertical_wall_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `natural_convection_vertical_wall_equation_user_curve_name`
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
                                 'for field `natural_convection_vertical_wall_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_vertical_wall_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `natural_convection_stable_horizontal_equation_source`
        This is for horizontal surfaces with heat flow directed for stable thermal stratification

        Args:
            value (str): value for IDD Field `natural_convection_stable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_stable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_stable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonStableHorizontalOrTilt")
            vals.add("AlamdariHammondStableHorizontal")
            vals.add("UserCurve")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `natural_convection_stable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `natural_convection_stable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `natural_convection_stable_horizontal_equation_user_curve_name`
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
                                 'for field `natural_convection_stable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_stable_horizontal_equation_user_curve_name`')

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
        """  Corresponds to IDD Field `natural_convection_unstable_horizontal_equation_source`

        Args:
            value (str): value for IDD Field `natural_convection_unstable_horizontal_equation_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `natural_convection_unstable_horizontal_equation_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_unstable_horizontal_equation_source`')
            vals = set()
            vals.add("WaltonUnstableHorizontalOrTilt")
            vals.add("AlamdariHammondUnstableHorizontal")
            vals.add("UserCurve")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `natural_convection_unstable_horizontal_equation_source`'.format(value))

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
        """  Corresponds to IDD Field `natural_convection_unstable_horizontal_equation_user_curve_name`
        The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve

        Args:
            value (str): value for IDD Field `natural_convection_unstable_horizontal_equation_user_curve_name`
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
                                 'for field `natural_convection_unstable_horizontal_equation_user_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `natural_convection_unstable_horizontal_equation_user_curve_name`')

        self._data["Natural Convection Unstable Horizontal Equation User Curve Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.wind_convection_windward_vertical_wall_equation_source))
        out.append(self._to_str(self.wind_convection_windward_equation_vertical_wall_user_curve_name))
        out.append(self._to_str(self.wind_convection_leeward_vertical_wall_equation_source))
        out.append(self._to_str(self.wind_convection_leeward_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.wind_convection_horizontal_roof_equation_source))
        out.append(self._to_str(self.wind_convection_horizontal_roof_user_curve_name))
        out.append(self._to_str(self.natural_convection_vertical_wall_equation_source))
        out.append(self._to_str(self.natural_convection_vertical_wall_equation_user_curve_name))
        out.append(self._to_str(self.natural_convection_stable_horizontal_equation_source))
        out.append(self._to_str(self.natural_convection_stable_horizontal_equation_user_curve_name))
        out.append(self._to_str(self.natural_convection_unstable_horizontal_equation_source))
        out.append(self._to_str(self.natural_convection_unstable_horizontal_equation_user_curve_name))
        return ",".join(out)

class SurfaceConvectionAlgorithmInsideUserCurve(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Inside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    
    """
    internal_name = "SurfaceConvectionAlgorithm:Inside:UserCurve"
    field_count = 6
    required_fields = []

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
            self.reference_temperature_for_convection_heat_transfer = None
        else:
            self.reference_temperature_for_convection_heat_transfer = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_temperature_difference_curve_name = None
        else:
            self.hc_function_of_temperature_difference_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_temperature_difference_divided_by_height_curve_name = None
        else:
            self.hc_function_of_temperature_difference_divided_by_height_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_air_change_rate_curve_name = None
        else:
            self.hc_function_of_air_change_rate_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = None
        else:
            self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name = vals[i]
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
    def reference_temperature_for_convection_heat_transfer(self):
        """Get reference_temperature_for_convection_heat_transfer

        Returns:
            str: the value of `reference_temperature_for_convection_heat_transfer` or None if not set
        """
        return self._data["Reference Temperature for Convection Heat Transfer"]

    @reference_temperature_for_convection_heat_transfer.setter
    def reference_temperature_for_convection_heat_transfer(self, value=None):
        """  Corresponds to IDD Field `reference_temperature_for_convection_heat_transfer`
        Controls which temperature is differenced from surface temperature when using the Hc value

        Args:
            value (str): value for IDD Field `reference_temperature_for_convection_heat_transfer`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reference_temperature_for_convection_heat_transfer`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reference_temperature_for_convection_heat_transfer`')
            vals = set()
            vals.add("MeanAirTemperature")
            vals.add("AdjacentAirTemperature")
            vals.add("SupplyAirTemperature")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `reference_temperature_for_convection_heat_transfer`'.format(value))

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
        """  Corresponds to IDD Field `hc_function_of_temperature_difference_curve_name`
        Curve's "x" is absolute value of delta-T (Surface temperature minus reference temperature, (C))
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_temperature_difference_curve_name`
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
                                 'for field `hc_function_of_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_temperature_difference_curve_name`')

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
        """  Corresponds to IDD Field `hc_function_of_temperature_difference_divided_by_height_curve_name`
        Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        when used for an inside face the vertical length scale is the zone's interior height
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_temperature_difference_divided_by_height_curve_name`
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
                                 'for field `hc_function_of_temperature_difference_divided_by_height_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_temperature_difference_divided_by_height_curve_name`')

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
        """  Corresponds to IDD Field `hc_function_of_air_change_rate_curve_name`
        Curve's "x" is mechanical ACH (Air Changes per hour from mechanical air system), (1/hr)
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_air_change_rate_curve_name`
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
                                 'for field `hc_function_of_air_change_rate_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_air_change_rate_curve_name`')

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
        """  Corresponds to IDD Field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`
        Curve's "x" is mechanical system air flow rate (m3/s) divided by zone's length along
        exterior walls (m).
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`
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
                                 'for field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name`')

        self._data["Hc Function of Air System Volume Flow Rate Divided by Zone Perimeter Length Curve Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.reference_temperature_for_convection_heat_transfer))
        out.append(self._to_str(self.hc_function_of_temperature_difference_curve_name))
        out.append(self._to_str(self.hc_function_of_temperature_difference_divided_by_height_curve_name))
        out.append(self._to_str(self.hc_function_of_air_change_rate_curve_name))
        out.append(self._to_str(self.hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name))
        return ",".join(out)

class SurfaceConvectionAlgorithmOutsideUserCurve(object):
    """ Corresponds to IDD object `SurfaceConvectionAlgorithm:Outside:UserCurve`
        Used to describe a custom model equation for surface convection heat transfer coefficient
        If more than one curve is referenced they are all used and added together.
    
    """
    internal_name = "SurfaceConvectionAlgorithm:Outside:UserCurve"
    field_count = 5
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceConvectionAlgorithm:Outside:UserCurve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Wind Speed Type for Curve"] = None
        self._data["Hf Function of Wind Speed Curve Name"] = None
        self._data["Hn Function of Temperature Difference Curve Name"] = None
        self._data["Hn Function of Temperature Difference Divided by Height Curve Name"] = None

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
            self.wind_speed_type_for_curve = None
        else:
            self.wind_speed_type_for_curve = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hf_function_of_wind_speed_curve_name = None
        else:
            self.hf_function_of_wind_speed_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hn_function_of_temperature_difference_curve_name = None
        else:
            self.hn_function_of_temperature_difference_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hn_function_of_temperature_difference_divided_by_height_curve_name = None
        else:
            self.hn_function_of_temperature_difference_divided_by_height_curve_name = vals[i]
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
    def wind_speed_type_for_curve(self):
        """Get wind_speed_type_for_curve

        Returns:
            str: the value of `wind_speed_type_for_curve` or None if not set
        """
        return self._data["Wind Speed Type for Curve"]

    @wind_speed_type_for_curve.setter
    def wind_speed_type_for_curve(self, value="HeightAdjust"):
        """  Corresponds to IDD Field `wind_speed_type_for_curve`

        Args:
            value (str): value for IDD Field `wind_speed_type_for_curve`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_speed_type_for_curve`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_speed_type_for_curve`')
            vals = set()
            vals.add("WeatherFile")
            vals.add("HeightAdjust")
            vals.add("ParallelComponent")
            vals.add("ParallelComponentHeightAdjust")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_speed_type_for_curve`'.format(value))

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
        """  Corresponds to IDD Field `hf_function_of_wind_speed_curve_name`
        Curve's "x" is wind speed of the type determined in the previous field (m/s)
        Table:OneIndependentVariable objects can also be used

        Args:
            value (str): value for IDD Field `hf_function_of_wind_speed_curve_name`
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
                                 'for field `hf_function_of_wind_speed_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hf_function_of_wind_speed_curve_name`')

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
        """  Corresponds to IDD Field `hn_function_of_temperature_difference_curve_name`
        Curve's "x" is absolute value of delta-T (Surface temperature minus air temperature, (C))
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hn_function_of_temperature_difference_curve_name`
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
                                 'for field `hn_function_of_temperature_difference_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hn_function_of_temperature_difference_curve_name`')

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
        """  Corresponds to IDD Field `hn_function_of_temperature_difference_divided_by_height_curve_name`
        Curve's "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m)
        when used for an outside face the vertical length scale is the exterior facade's overall height
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `hn_function_of_temperature_difference_divided_by_height_curve_name`
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
                                 'for field `hn_function_of_temperature_difference_divided_by_height_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hn_function_of_temperature_difference_divided_by_height_curve_name`')

        self._data["Hn Function of Temperature Difference Divided by Height Curve Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.wind_speed_type_for_curve))
        out.append(self._to_str(self.hf_function_of_wind_speed_curve_name))
        out.append(self._to_str(self.hn_function_of_temperature_difference_curve_name))
        out.append(self._to_str(self.hn_function_of_temperature_difference_divided_by_height_curve_name))
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
    required_fields = ["Surface Name", "Convection Coefficient 1 Location", "Convection Coefficient 1 Type"]

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
                Units: W/m2-K
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
    required_fields = ["Surface Type", "Convection Coefficient 1 Location", "Convection Coefficient 1 Type"]

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
                Units: W/m2-K
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

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperties:VaporCoefficients`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Constant External Vapor Transfer Coefficient"] = None
        self._data["External Vapor Coefficient Value"] = None
        self._data["Constant Internal vapor Transfer Coefficient"] = None
        self._data["Internal Vapor Coefficient Value"] = None

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
            self.constant_external_vapor_transfer_coefficient = None
        else:
            self.constant_external_vapor_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.external_vapor_coefficient_value = None
        else:
            self.external_vapor_coefficient_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_internal_vapor_transfer_coefficient = None
        else:
            self.constant_internal_vapor_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.internal_vapor_coefficient_value = None
        else:
            self.internal_vapor_coefficient_value = vals[i]
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
    def constant_external_vapor_transfer_coefficient(self):
        """Get constant_external_vapor_transfer_coefficient

        Returns:
            str: the value of `constant_external_vapor_transfer_coefficient` or None if not set
        """
        return self._data["Constant External Vapor Transfer Coefficient"]

    @constant_external_vapor_transfer_coefficient.setter
    def constant_external_vapor_transfer_coefficient(self, value="No"):
        """  Corresponds to IDD Field `constant_external_vapor_transfer_coefficient`

        Args:
            value (str): value for IDD Field `constant_external_vapor_transfer_coefficient`
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
                                 'for field `constant_external_vapor_transfer_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `constant_external_vapor_transfer_coefficient`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `constant_external_vapor_transfer_coefficient`'.format(value))

        self._data["Constant External Vapor Transfer Coefficient"] = value

    @property
    def external_vapor_coefficient_value(self):
        """Get external_vapor_coefficient_value

        Returns:
            float: the value of `external_vapor_coefficient_value` or None if not set
        """
        return self._data["External Vapor Coefficient Value"]

    @external_vapor_coefficient_value.setter
    def external_vapor_coefficient_value(self, value=0.0 ):
        """  Corresponds to IDD Field `external_vapor_coefficient_value`

        Args:
            value (float): value for IDD Field `external_vapor_coefficient_value`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `external_vapor_coefficient_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `external_vapor_coefficient_value`')

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
        """  Corresponds to IDD Field `constant_internal_vapor_transfer_coefficient`

        Args:
            value (str): value for IDD Field `constant_internal_vapor_transfer_coefficient`
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
                                 'for field `constant_internal_vapor_transfer_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `constant_internal_vapor_transfer_coefficient`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `constant_internal_vapor_transfer_coefficient`'.format(value))

        self._data["Constant Internal vapor Transfer Coefficient"] = value

    @property
    def internal_vapor_coefficient_value(self):
        """Get internal_vapor_coefficient_value

        Returns:
            float: the value of `internal_vapor_coefficient_value` or None if not set
        """
        return self._data["Internal Vapor Coefficient Value"]

    @internal_vapor_coefficient_value.setter
    def internal_vapor_coefficient_value(self, value=0.0 ):
        """  Corresponds to IDD Field `internal_vapor_coefficient_value`

        Args:
            value (float): value for IDD Field `internal_vapor_coefficient_value`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `internal_vapor_coefficient_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `internal_vapor_coefficient_value`')

        self._data["Internal Vapor Coefficient Value"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.constant_external_vapor_transfer_coefficient))
        out.append(self._to_str(self.external_vapor_coefficient_value))
        out.append(self._to_str(self.constant_internal_vapor_transfer_coefficient))
        out.append(self._to_str(self.internal_vapor_coefficient_value))
        return ",".join(out)

class SurfacePropertyExteriorNaturalVentedCavity(object):
    """ Corresponds to IDD object `SurfaceProperty:ExteriorNaturalVentedCavity`
        Used to describe the decoupled layer, or baffle, and the characteristics of the cavity
        and openings for naturally ventilated exterior surfaces. This object is also used in
        conjunction with the OtherSideConditionsModel.
    
    """
    internal_name = "SurfaceProperty:ExteriorNaturalVentedCavity"
    field_count = 21
    required_fields = ["Name", "Boundary Conditions Model Name", "Roughness of Exterior Surface", "Surface 1 Name"]

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
    required_fields = ["Name", "Surface Name", "Construction Name", "Inside Surface Incident Sun Solar Radiation Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `SurfaceProperty:SolarIncidentInside`
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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.inside_surface_incident_sun_solar_radiation_schedule_name))
        return ",".join(out)

class ComplexFenestrationPropertySolarAbsorbedLayers(object):
    """ Corresponds to IDD object `ComplexFenestrationProperty:SolarAbsorbedLayers`
        Used to provide solar radiation absorbed in fenestration layers. References surface-construction pair
        and if that pair is used in a simulation, then program will use value provided in schedules instead of calculating it.
    
    """
    internal_name = "ComplexFenestrationProperty:SolarAbsorbedLayers"
    field_count = 8
    required_fields = ["Name", "Fenestration Surface", "Construction Name", "Layer 1 Solar Radiation Absorbed Schedule Name"]

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
            self.fenestration_surface = None
        else:
            self.fenestration_surface = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_1_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_1_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_2_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_2_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_3_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_3_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_4_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_4_solar_radiation_absorbed_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.layer_5_solar_radiation_absorbed_schedule_name = None
        else:
            self.layer_5_solar_radiation_absorbed_schedule_name = vals[i]
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
    def fenestration_surface(self):
        """Get fenestration_surface

        Returns:
            str: the value of `fenestration_surface` or None if not set
        """
        return self._data["Fenestration Surface"]

    @fenestration_surface.setter
    def fenestration_surface(self, value=None):
        """  Corresponds to IDD Field `fenestration_surface`

        Args:
            value (str): value for IDD Field `fenestration_surface`
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
                                 'for field `fenestration_surface`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fenestration_surface`')

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
    def layer_1_solar_radiation_absorbed_schedule_name(self):
        """Get layer_1_solar_radiation_absorbed_schedule_name

        Returns:
            str: the value of `layer_1_solar_radiation_absorbed_schedule_name` or None if not set
        """
        return self._data["Layer 1 Solar Radiation Absorbed Schedule Name"]

    @layer_1_solar_radiation_absorbed_schedule_name.setter
    def layer_1_solar_radiation_absorbed_schedule_name(self, value=None):
        """  Corresponds to IDD Field `layer_1_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_1_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_1_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_1_solar_radiation_absorbed_schedule_name`')

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
        """  Corresponds to IDD Field `layer_2_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_2_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_2_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_2_solar_radiation_absorbed_schedule_name`')

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
        """  Corresponds to IDD Field `layer_3_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_3_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_3_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_3_solar_radiation_absorbed_schedule_name`')

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
        """  Corresponds to IDD Field `layer_4_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_4_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_4_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_4_solar_radiation_absorbed_schedule_name`')

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
        """  Corresponds to IDD Field `layer_5_solar_radiation_absorbed_schedule_name`

        Args:
            value (str): value for IDD Field `layer_5_solar_radiation_absorbed_schedule_name`
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
                                 'for field `layer_5_solar_radiation_absorbed_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `layer_5_solar_radiation_absorbed_schedule_name`')

        self._data["Layer 5 Solar Radiation Absorbed Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.fenestration_surface))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.layer_1_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_2_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_3_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_4_solar_radiation_absorbed_schedule_name))
        out.append(self._to_str(self.layer_5_solar_radiation_absorbed_schedule_name))
        return ",".join(out)

class ZonePropertyUserViewFactorsBySurfaceName(object):
    """ Corresponds to IDD object `ZoneProperty:UserViewFactors:bySurfaceName`
        View factors for Surface to Surface in a zone.
        (Number of Surfaces)**2 must be entered.
    
    """
    internal_name = "ZoneProperty:UserViewFactors:bySurfaceName"
    field_count = 364
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneProperty:UserViewFactors:bySurfaceName`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["From Surface 1"] = None
        self._data["To Surface 1"] = None
        self._data["View Factor 1"] = None
        self._data["From Surface 2"] = None
        self._data["To Surface 2"] = None
        self._data["View Factor 2"] = None
        self._data["From Surface 3"] = None
        self._data["To Surface 3"] = None
        self._data["View Factor 3"] = None
        self._data["From Surface 4"] = None
        self._data["To Surface 4"] = None
        self._data["View Factor 4"] = None
        self._data["From Surface 5"] = None
        self._data["To Surface 5"] = None
        self._data["View Factor 5"] = None
        self._data["From Surface 6"] = None
        self._data["To Surface 6"] = None
        self._data["View Factor 6"] = None
        self._data["From Surface 7"] = None
        self._data["To Surface 7"] = None
        self._data["View Factor 7"] = None
        self._data["From Surface 8"] = None
        self._data["To Surface 8"] = None
        self._data["View Factor 8"] = None
        self._data["From Surface 9"] = None
        self._data["To Surface 9"] = None
        self._data["View Factor 9"] = None
        self._data["From Surface 10"] = None
        self._data["To Surface 10"] = None
        self._data["View Factor 10"] = None
        self._data["From Surface 11"] = None
        self._data["To Surface 11"] = None
        self._data["View Factor 11"] = None
        self._data["From Surface 12"] = None
        self._data["To Surface 12"] = None
        self._data["View Factor 12"] = None
        self._data["From Surface 13"] = None
        self._data["To Surface 13"] = None
        self._data["View Factor 13"] = None
        self._data["From Surface 14"] = None
        self._data["To Surface 14"] = None
        self._data["View Factor 14"] = None
        self._data["From Surface 15"] = None
        self._data["To Surface 15"] = None
        self._data["View Factor 15"] = None
        self._data["From Surface 16"] = None
        self._data["To Surface 16"] = None
        self._data["View Factor 16"] = None
        self._data["From Surface 17"] = None
        self._data["To Surface 17"] = None
        self._data["View Factor 17"] = None
        self._data["From Surface 18"] = None
        self._data["To Surface 18"] = None
        self._data["View Factor 18"] = None
        self._data["From Surface 19"] = None
        self._data["To Surface 19"] = None
        self._data["View Factor 19"] = None
        self._data["From Surface 20"] = None
        self._data["To Surface 20"] = None
        self._data["View Factor 20"] = None
        self._data["From Surface 21"] = None
        self._data["To Surface 21"] = None
        self._data["View Factor 21"] = None
        self._data["From Surface 22"] = None
        self._data["To Surface 22"] = None
        self._data["View Factor 22"] = None
        self._data["From Surface 23"] = None
        self._data["To Surface 23"] = None
        self._data["View Factor 23"] = None
        self._data["From Surface 24"] = None
        self._data["To Surface 24"] = None
        self._data["View Factor 24"] = None
        self._data["From Surface 25"] = None
        self._data["To Surface 25"] = None
        self._data["View Factor 25"] = None
        self._data["From Surface 26"] = None
        self._data["To Surface 26"] = None
        self._data["View Factor 26"] = None
        self._data["From Surface 27"] = None
        self._data["To Surface 27"] = None
        self._data["View Factor 27"] = None
        self._data["From Surface 28"] = None
        self._data["To Surface 28"] = None
        self._data["View Factor 28"] = None
        self._data["From Surface 29"] = None
        self._data["To Surface 29"] = None
        self._data["View Factor 29"] = None
        self._data["From Surface 30"] = None
        self._data["To Surface 30"] = None
        self._data["View Factor 30"] = None
        self._data["From Surface 31"] = None
        self._data["To Surface 31"] = None
        self._data["View Factor 31"] = None
        self._data["From Surface 32"] = None
        self._data["To Surface 32"] = None
        self._data["View Factor 32"] = None
        self._data["From Surface 33"] = None
        self._data["To Surface 33"] = None
        self._data["View Factor 33"] = None
        self._data["From Surface 34"] = None
        self._data["To Surface 34"] = None
        self._data["View Factor 34"] = None
        self._data["From Surface 35"] = None
        self._data["To Surface 35"] = None
        self._data["View Factor 35"] = None
        self._data["From Surface 36"] = None
        self._data["To Surface 36"] = None
        self._data["View Factor 36"] = None
        self._data["From Surface 37"] = None
        self._data["To Surface 37"] = None
        self._data["View Factor 37"] = None
        self._data["From Surface 38"] = None
        self._data["To Surface 38"] = None
        self._data["View Factor 38"] = None
        self._data["From Surface 39"] = None
        self._data["To Surface 39"] = None
        self._data["View Factor 39"] = None
        self._data["From Surface 40"] = None
        self._data["To Surface 40"] = None
        self._data["View Factor 40"] = None
        self._data["From Surface 41"] = None
        self._data["To Surface 41"] = None
        self._data["View Factor 41"] = None
        self._data["From Surface 42"] = None
        self._data["To Surface 42"] = None
        self._data["View Factor 42"] = None
        self._data["From Surface 43"] = None
        self._data["To Surface 43"] = None
        self._data["View Factor 43"] = None
        self._data["From Surface 44"] = None
        self._data["To Surface 44"] = None
        self._data["View Factor 44"] = None
        self._data["From Surface 45"] = None
        self._data["To Surface 45"] = None
        self._data["View Factor 45"] = None
        self._data["From Surface 46"] = None
        self._data["To Surface 46"] = None
        self._data["View Factor 46"] = None
        self._data["From Surface 47"] = None
        self._data["To Surface 47"] = None
        self._data["View Factor 47"] = None
        self._data["From Surface 48"] = None
        self._data["To Surface 48"] = None
        self._data["View Factor 48"] = None
        self._data["From Surface 49"] = None
        self._data["To Surface 49"] = None
        self._data["View Factor 49"] = None
        self._data["From Surface 50"] = None
        self._data["To Surface 50"] = None
        self._data["View Factor 50"] = None
        self._data["From Surface 51"] = None
        self._data["To Surface 51"] = None
        self._data["View Factor 51"] = None
        self._data["From Surface 52"] = None
        self._data["To Surface 52"] = None
        self._data["View Factor 52"] = None
        self._data["From Surface 53"] = None
        self._data["To Surface 53"] = None
        self._data["View Factor 53"] = None
        self._data["From Surface 54"] = None
        self._data["To Surface 54"] = None
        self._data["View Factor 54"] = None
        self._data["From Surface 55"] = None
        self._data["To Surface 55"] = None
        self._data["View Factor 55"] = None
        self._data["From Surface 56"] = None
        self._data["To Surface 56"] = None
        self._data["View Factor 56"] = None
        self._data["From Surface 57"] = None
        self._data["To Surface 57"] = None
        self._data["View Factor 57"] = None
        self._data["From Surface 58"] = None
        self._data["To Surface 58"] = None
        self._data["View Factor 58"] = None
        self._data["From Surface 59"] = None
        self._data["To Surface 59"] = None
        self._data["View Factor 59"] = None
        self._data["From Surface 60"] = None
        self._data["To Surface 60"] = None
        self._data["View Factor 60"] = None
        self._data["From Surface 61"] = None
        self._data["To Surface 61"] = None
        self._data["View Factor 61"] = None
        self._data["From Surface 62"] = None
        self._data["To Surface 62"] = None
        self._data["View Factor 62"] = None
        self._data["From Surface 63"] = None
        self._data["To Surface 63"] = None
        self._data["View Factor 63"] = None
        self._data["From Surface 64"] = None
        self._data["To Surface 64"] = None
        self._data["View Factor 64"] = None
        self._data["From Surface 65"] = None
        self._data["To Surface 65"] = None
        self._data["View Factor 65"] = None
        self._data["From Surface 66"] = None
        self._data["To Surface 66"] = None
        self._data["View Factor 66"] = None
        self._data["From Surface 67"] = None
        self._data["To Surface 67"] = None
        self._data["View Factor 67"] = None
        self._data["From Surface 68"] = None
        self._data["To Surface 68"] = None
        self._data["View Factor 68"] = None
        self._data["From Surface 69"] = None
        self._data["To Surface 69"] = None
        self._data["View Factor 69"] = None
        self._data["From Surface 70"] = None
        self._data["To Surface 70"] = None
        self._data["View Factor 70"] = None
        self._data["From Surface 71"] = None
        self._data["To Surface 71"] = None
        self._data["View Factor 71"] = None
        self._data["From Surface 72"] = None
        self._data["To Surface 72"] = None
        self._data["View Factor 72"] = None
        self._data["From Surface 73"] = None
        self._data["To Surface 73"] = None
        self._data["View Factor 73"] = None
        self._data["From Surface 74"] = None
        self._data["To Surface 74"] = None
        self._data["View Factor 74"] = None
        self._data["From Surface 75"] = None
        self._data["To Surface 75"] = None
        self._data["View Factor 75"] = None
        self._data["From Surface 76"] = None
        self._data["To Surface 76"] = None
        self._data["View Factor 76"] = None
        self._data["From Surface 77"] = None
        self._data["To Surface 77"] = None
        self._data["View Factor 77"] = None
        self._data["From Surface 78"] = None
        self._data["To Surface 78"] = None
        self._data["View Factor 78"] = None
        self._data["From Surface 79"] = None
        self._data["To Surface 79"] = None
        self._data["View Factor 79"] = None
        self._data["From Surface 80"] = None
        self._data["To Surface 80"] = None
        self._data["View Factor 80"] = None
        self._data["From Surface 81"] = None
        self._data["To Surface 81"] = None
        self._data["View Factor 81"] = None
        self._data["From Surface 82"] = None
        self._data["To Surface 82"] = None
        self._data["View Factor 82"] = None
        self._data["From Surface 83"] = None
        self._data["To Surface 83"] = None
        self._data["View Factor 83"] = None
        self._data["From Surface 84"] = None
        self._data["To Surface 84"] = None
        self._data["View Factor 84"] = None
        self._data["From Surface 85"] = None
        self._data["To Surface 85"] = None
        self._data["View Factor 85"] = None
        self._data["From Surface 86"] = None
        self._data["To Surface 86"] = None
        self._data["View Factor 86"] = None
        self._data["From Surface 87"] = None
        self._data["To Surface 87"] = None
        self._data["View Factor 87"] = None
        self._data["From Surface 88"] = None
        self._data["To Surface 88"] = None
        self._data["View Factor 88"] = None
        self._data["From Surface 89"] = None
        self._data["To Surface 89"] = None
        self._data["View Factor 89"] = None
        self._data["From Surface 90"] = None
        self._data["To Surface 90"] = None
        self._data["View Factor 90"] = None
        self._data["From Surface 91"] = None
        self._data["To Surface 91"] = None
        self._data["View Factor 91"] = None
        self._data["From Surface 92"] = None
        self._data["To Surface 92"] = None
        self._data["View Factor 92"] = None
        self._data["From Surface 93"] = None
        self._data["To Surface 93"] = None
        self._data["View Factor 93"] = None
        self._data["From Surface 94"] = None
        self._data["To Surface 94"] = None
        self._data["View Factor 94"] = None
        self._data["From Surface 95"] = None
        self._data["To Surface 95"] = None
        self._data["View Factor 95"] = None
        self._data["From Surface 96"] = None
        self._data["To Surface 96"] = None
        self._data["View Factor 96"] = None
        self._data["From Surface 97"] = None
        self._data["To Surface 97"] = None
        self._data["View Factor 97"] = None
        self._data["From Surface 98"] = None
        self._data["To Surface 98"] = None
        self._data["View Factor 98"] = None
        self._data["From Surface 99"] = None
        self._data["To Surface 99"] = None
        self._data["View Factor 99"] = None
        self._data["From Surface 100"] = None
        self._data["To Surface 100"] = None
        self._data["View Factor 100"] = None
        self._data["From Surface 101"] = None
        self._data["To Surface 101"] = None
        self._data["View Factor 101"] = None
        self._data["From Surface 102"] = None
        self._data["To Surface 102"] = None
        self._data["View Factor 102"] = None
        self._data["From Surface 103"] = None
        self._data["To Surface 103"] = None
        self._data["View Factor 103"] = None
        self._data["From Surface 104"] = None
        self._data["To Surface 104"] = None
        self._data["View Factor 104"] = None
        self._data["From Surface 105"] = None
        self._data["To Surface 105"] = None
        self._data["View Factor 105"] = None
        self._data["From Surface 106"] = None
        self._data["To Surface 106"] = None
        self._data["View Factor 106"] = None
        self._data["From Surface 107"] = None
        self._data["To Surface 107"] = None
        self._data["View Factor 107"] = None
        self._data["From Surface 108"] = None
        self._data["To Surface 108"] = None
        self._data["View Factor 108"] = None
        self._data["From Surface 109"] = None
        self._data["To Surface 109"] = None
        self._data["View Factor 109"] = None
        self._data["From Surface 110"] = None
        self._data["To Surface 110"] = None
        self._data["View Factor 110"] = None
        self._data["From Surface 111"] = None
        self._data["To Surface 111"] = None
        self._data["View Factor 111"] = None
        self._data["From Surface 112"] = None
        self._data["To Surface 112"] = None
        self._data["View Factor 112"] = None
        self._data["From Surface 113"] = None
        self._data["To Surface 113"] = None
        self._data["View Factor 113"] = None
        self._data["From Surface 114"] = None
        self._data["To Surface 114"] = None
        self._data["View Factor 114"] = None
        self._data["From Surface 115"] = None
        self._data["To Surface 115"] = None
        self._data["View Factor 115"] = None
        self._data["From Surface 116"] = None
        self._data["To Surface 116"] = None
        self._data["View Factor 116"] = None
        self._data["From Surface 117"] = None
        self._data["To Surface 117"] = None
        self._data["View Factor 117"] = None
        self._data["From Surface 118"] = None
        self._data["To Surface 118"] = None
        self._data["View Factor 118"] = None
        self._data["From Surface 119"] = None
        self._data["To Surface 119"] = None
        self._data["View Factor 119"] = None
        self._data["From Surface 120"] = None
        self._data["To Surface 120"] = None
        self._data["View Factor 120"] = None
        self._data["From Surface 121"] = None
        self._data["To Surface 121"] = None
        self._data["View Factor 121"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_1 = None
        else:
            self.from_surface_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_1 = None
        else:
            self.to_surface_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_1 = None
        else:
            self.view_factor_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_2 = None
        else:
            self.from_surface_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_2 = None
        else:
            self.to_surface_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_2 = None
        else:
            self.view_factor_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_3 = None
        else:
            self.from_surface_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_3 = None
        else:
            self.to_surface_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_3 = None
        else:
            self.view_factor_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_4 = None
        else:
            self.from_surface_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_4 = None
        else:
            self.to_surface_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_4 = None
        else:
            self.view_factor_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_5 = None
        else:
            self.from_surface_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_5 = None
        else:
            self.to_surface_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_5 = None
        else:
            self.view_factor_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_6 = None
        else:
            self.from_surface_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_6 = None
        else:
            self.to_surface_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_6 = None
        else:
            self.view_factor_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_7 = None
        else:
            self.from_surface_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_7 = None
        else:
            self.to_surface_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_7 = None
        else:
            self.view_factor_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_8 = None
        else:
            self.from_surface_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_8 = None
        else:
            self.to_surface_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_8 = None
        else:
            self.view_factor_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_9 = None
        else:
            self.from_surface_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_9 = None
        else:
            self.to_surface_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_9 = None
        else:
            self.view_factor_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_10 = None
        else:
            self.from_surface_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_10 = None
        else:
            self.to_surface_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_10 = None
        else:
            self.view_factor_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_11 = None
        else:
            self.from_surface_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_11 = None
        else:
            self.to_surface_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_11 = None
        else:
            self.view_factor_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_12 = None
        else:
            self.from_surface_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_12 = None
        else:
            self.to_surface_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_12 = None
        else:
            self.view_factor_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_13 = None
        else:
            self.from_surface_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_13 = None
        else:
            self.to_surface_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_13 = None
        else:
            self.view_factor_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_14 = None
        else:
            self.from_surface_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_14 = None
        else:
            self.to_surface_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_14 = None
        else:
            self.view_factor_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_15 = None
        else:
            self.from_surface_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_15 = None
        else:
            self.to_surface_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_15 = None
        else:
            self.view_factor_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_16 = None
        else:
            self.from_surface_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_16 = None
        else:
            self.to_surface_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_16 = None
        else:
            self.view_factor_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_17 = None
        else:
            self.from_surface_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_17 = None
        else:
            self.to_surface_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_17 = None
        else:
            self.view_factor_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_18 = None
        else:
            self.from_surface_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_18 = None
        else:
            self.to_surface_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_18 = None
        else:
            self.view_factor_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_19 = None
        else:
            self.from_surface_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_19 = None
        else:
            self.to_surface_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_19 = None
        else:
            self.view_factor_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_20 = None
        else:
            self.from_surface_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_20 = None
        else:
            self.to_surface_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_20 = None
        else:
            self.view_factor_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_21 = None
        else:
            self.from_surface_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_21 = None
        else:
            self.to_surface_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_21 = None
        else:
            self.view_factor_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_22 = None
        else:
            self.from_surface_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_22 = None
        else:
            self.to_surface_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_22 = None
        else:
            self.view_factor_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_23 = None
        else:
            self.from_surface_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_23 = None
        else:
            self.to_surface_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_23 = None
        else:
            self.view_factor_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_24 = None
        else:
            self.from_surface_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_24 = None
        else:
            self.to_surface_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_24 = None
        else:
            self.view_factor_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_25 = None
        else:
            self.from_surface_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_25 = None
        else:
            self.to_surface_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_25 = None
        else:
            self.view_factor_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_26 = None
        else:
            self.from_surface_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_26 = None
        else:
            self.to_surface_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_26 = None
        else:
            self.view_factor_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_27 = None
        else:
            self.from_surface_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_27 = None
        else:
            self.to_surface_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_27 = None
        else:
            self.view_factor_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_28 = None
        else:
            self.from_surface_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_28 = None
        else:
            self.to_surface_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_28 = None
        else:
            self.view_factor_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_29 = None
        else:
            self.from_surface_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_29 = None
        else:
            self.to_surface_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_29 = None
        else:
            self.view_factor_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_30 = None
        else:
            self.from_surface_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_30 = None
        else:
            self.to_surface_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_30 = None
        else:
            self.view_factor_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_31 = None
        else:
            self.from_surface_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_31 = None
        else:
            self.to_surface_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_31 = None
        else:
            self.view_factor_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_32 = None
        else:
            self.from_surface_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_32 = None
        else:
            self.to_surface_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_32 = None
        else:
            self.view_factor_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_33 = None
        else:
            self.from_surface_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_33 = None
        else:
            self.to_surface_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_33 = None
        else:
            self.view_factor_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_34 = None
        else:
            self.from_surface_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_34 = None
        else:
            self.to_surface_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_34 = None
        else:
            self.view_factor_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_35 = None
        else:
            self.from_surface_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_35 = None
        else:
            self.to_surface_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_35 = None
        else:
            self.view_factor_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_36 = None
        else:
            self.from_surface_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_36 = None
        else:
            self.to_surface_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_36 = None
        else:
            self.view_factor_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_37 = None
        else:
            self.from_surface_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_37 = None
        else:
            self.to_surface_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_37 = None
        else:
            self.view_factor_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_38 = None
        else:
            self.from_surface_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_38 = None
        else:
            self.to_surface_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_38 = None
        else:
            self.view_factor_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_39 = None
        else:
            self.from_surface_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_39 = None
        else:
            self.to_surface_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_39 = None
        else:
            self.view_factor_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_40 = None
        else:
            self.from_surface_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_40 = None
        else:
            self.to_surface_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_40 = None
        else:
            self.view_factor_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_41 = None
        else:
            self.from_surface_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_41 = None
        else:
            self.to_surface_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_41 = None
        else:
            self.view_factor_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_42 = None
        else:
            self.from_surface_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_42 = None
        else:
            self.to_surface_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_42 = None
        else:
            self.view_factor_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_43 = None
        else:
            self.from_surface_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_43 = None
        else:
            self.to_surface_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_43 = None
        else:
            self.view_factor_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_44 = None
        else:
            self.from_surface_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_44 = None
        else:
            self.to_surface_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_44 = None
        else:
            self.view_factor_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_45 = None
        else:
            self.from_surface_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_45 = None
        else:
            self.to_surface_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_45 = None
        else:
            self.view_factor_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_46 = None
        else:
            self.from_surface_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_46 = None
        else:
            self.to_surface_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_46 = None
        else:
            self.view_factor_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_47 = None
        else:
            self.from_surface_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_47 = None
        else:
            self.to_surface_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_47 = None
        else:
            self.view_factor_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_48 = None
        else:
            self.from_surface_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_48 = None
        else:
            self.to_surface_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_48 = None
        else:
            self.view_factor_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_49 = None
        else:
            self.from_surface_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_49 = None
        else:
            self.to_surface_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_49 = None
        else:
            self.view_factor_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_50 = None
        else:
            self.from_surface_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_50 = None
        else:
            self.to_surface_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_50 = None
        else:
            self.view_factor_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_51 = None
        else:
            self.from_surface_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_51 = None
        else:
            self.to_surface_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_51 = None
        else:
            self.view_factor_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_52 = None
        else:
            self.from_surface_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_52 = None
        else:
            self.to_surface_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_52 = None
        else:
            self.view_factor_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_53 = None
        else:
            self.from_surface_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_53 = None
        else:
            self.to_surface_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_53 = None
        else:
            self.view_factor_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_54 = None
        else:
            self.from_surface_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_54 = None
        else:
            self.to_surface_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_54 = None
        else:
            self.view_factor_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_55 = None
        else:
            self.from_surface_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_55 = None
        else:
            self.to_surface_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_55 = None
        else:
            self.view_factor_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_56 = None
        else:
            self.from_surface_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_56 = None
        else:
            self.to_surface_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_56 = None
        else:
            self.view_factor_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_57 = None
        else:
            self.from_surface_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_57 = None
        else:
            self.to_surface_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_57 = None
        else:
            self.view_factor_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_58 = None
        else:
            self.from_surface_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_58 = None
        else:
            self.to_surface_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_58 = None
        else:
            self.view_factor_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_59 = None
        else:
            self.from_surface_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_59 = None
        else:
            self.to_surface_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_59 = None
        else:
            self.view_factor_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_60 = None
        else:
            self.from_surface_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_60 = None
        else:
            self.to_surface_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_60 = None
        else:
            self.view_factor_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_61 = None
        else:
            self.from_surface_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_61 = None
        else:
            self.to_surface_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_61 = None
        else:
            self.view_factor_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_62 = None
        else:
            self.from_surface_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_62 = None
        else:
            self.to_surface_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_62 = None
        else:
            self.view_factor_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_63 = None
        else:
            self.from_surface_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_63 = None
        else:
            self.to_surface_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_63 = None
        else:
            self.view_factor_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_64 = None
        else:
            self.from_surface_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_64 = None
        else:
            self.to_surface_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_64 = None
        else:
            self.view_factor_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_65 = None
        else:
            self.from_surface_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_65 = None
        else:
            self.to_surface_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_65 = None
        else:
            self.view_factor_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_66 = None
        else:
            self.from_surface_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_66 = None
        else:
            self.to_surface_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_66 = None
        else:
            self.view_factor_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_67 = None
        else:
            self.from_surface_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_67 = None
        else:
            self.to_surface_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_67 = None
        else:
            self.view_factor_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_68 = None
        else:
            self.from_surface_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_68 = None
        else:
            self.to_surface_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_68 = None
        else:
            self.view_factor_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_69 = None
        else:
            self.from_surface_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_69 = None
        else:
            self.to_surface_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_69 = None
        else:
            self.view_factor_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_70 = None
        else:
            self.from_surface_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_70 = None
        else:
            self.to_surface_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_70 = None
        else:
            self.view_factor_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_71 = None
        else:
            self.from_surface_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_71 = None
        else:
            self.to_surface_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_71 = None
        else:
            self.view_factor_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_72 = None
        else:
            self.from_surface_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_72 = None
        else:
            self.to_surface_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_72 = None
        else:
            self.view_factor_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_73 = None
        else:
            self.from_surface_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_73 = None
        else:
            self.to_surface_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_73 = None
        else:
            self.view_factor_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_74 = None
        else:
            self.from_surface_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_74 = None
        else:
            self.to_surface_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_74 = None
        else:
            self.view_factor_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_75 = None
        else:
            self.from_surface_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_75 = None
        else:
            self.to_surface_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_75 = None
        else:
            self.view_factor_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_76 = None
        else:
            self.from_surface_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_76 = None
        else:
            self.to_surface_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_76 = None
        else:
            self.view_factor_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_77 = None
        else:
            self.from_surface_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_77 = None
        else:
            self.to_surface_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_77 = None
        else:
            self.view_factor_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_78 = None
        else:
            self.from_surface_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_78 = None
        else:
            self.to_surface_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_78 = None
        else:
            self.view_factor_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_79 = None
        else:
            self.from_surface_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_79 = None
        else:
            self.to_surface_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_79 = None
        else:
            self.view_factor_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_80 = None
        else:
            self.from_surface_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_80 = None
        else:
            self.to_surface_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_80 = None
        else:
            self.view_factor_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_81 = None
        else:
            self.from_surface_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_81 = None
        else:
            self.to_surface_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_81 = None
        else:
            self.view_factor_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_82 = None
        else:
            self.from_surface_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_82 = None
        else:
            self.to_surface_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_82 = None
        else:
            self.view_factor_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_83 = None
        else:
            self.from_surface_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_83 = None
        else:
            self.to_surface_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_83 = None
        else:
            self.view_factor_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_84 = None
        else:
            self.from_surface_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_84 = None
        else:
            self.to_surface_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_84 = None
        else:
            self.view_factor_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_85 = None
        else:
            self.from_surface_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_85 = None
        else:
            self.to_surface_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_85 = None
        else:
            self.view_factor_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_86 = None
        else:
            self.from_surface_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_86 = None
        else:
            self.to_surface_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_86 = None
        else:
            self.view_factor_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_87 = None
        else:
            self.from_surface_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_87 = None
        else:
            self.to_surface_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_87 = None
        else:
            self.view_factor_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_88 = None
        else:
            self.from_surface_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_88 = None
        else:
            self.to_surface_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_88 = None
        else:
            self.view_factor_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_89 = None
        else:
            self.from_surface_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_89 = None
        else:
            self.to_surface_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_89 = None
        else:
            self.view_factor_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_90 = None
        else:
            self.from_surface_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_90 = None
        else:
            self.to_surface_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_90 = None
        else:
            self.view_factor_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_91 = None
        else:
            self.from_surface_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_91 = None
        else:
            self.to_surface_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_91 = None
        else:
            self.view_factor_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_92 = None
        else:
            self.from_surface_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_92 = None
        else:
            self.to_surface_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_92 = None
        else:
            self.view_factor_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_93 = None
        else:
            self.from_surface_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_93 = None
        else:
            self.to_surface_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_93 = None
        else:
            self.view_factor_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_94 = None
        else:
            self.from_surface_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_94 = None
        else:
            self.to_surface_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_94 = None
        else:
            self.view_factor_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_95 = None
        else:
            self.from_surface_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_95 = None
        else:
            self.to_surface_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_95 = None
        else:
            self.view_factor_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_96 = None
        else:
            self.from_surface_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_96 = None
        else:
            self.to_surface_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_96 = None
        else:
            self.view_factor_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_97 = None
        else:
            self.from_surface_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_97 = None
        else:
            self.to_surface_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_97 = None
        else:
            self.view_factor_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_98 = None
        else:
            self.from_surface_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_98 = None
        else:
            self.to_surface_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_98 = None
        else:
            self.view_factor_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_99 = None
        else:
            self.from_surface_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_99 = None
        else:
            self.to_surface_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_99 = None
        else:
            self.view_factor_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_100 = None
        else:
            self.from_surface_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_100 = None
        else:
            self.to_surface_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_100 = None
        else:
            self.view_factor_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_101 = None
        else:
            self.from_surface_101 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_101 = None
        else:
            self.to_surface_101 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_101 = None
        else:
            self.view_factor_101 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_102 = None
        else:
            self.from_surface_102 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_102 = None
        else:
            self.to_surface_102 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_102 = None
        else:
            self.view_factor_102 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_103 = None
        else:
            self.from_surface_103 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_103 = None
        else:
            self.to_surface_103 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_103 = None
        else:
            self.view_factor_103 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_104 = None
        else:
            self.from_surface_104 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_104 = None
        else:
            self.to_surface_104 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_104 = None
        else:
            self.view_factor_104 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_105 = None
        else:
            self.from_surface_105 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_105 = None
        else:
            self.to_surface_105 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_105 = None
        else:
            self.view_factor_105 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_106 = None
        else:
            self.from_surface_106 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_106 = None
        else:
            self.to_surface_106 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_106 = None
        else:
            self.view_factor_106 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_107 = None
        else:
            self.from_surface_107 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_107 = None
        else:
            self.to_surface_107 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_107 = None
        else:
            self.view_factor_107 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_108 = None
        else:
            self.from_surface_108 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_108 = None
        else:
            self.to_surface_108 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_108 = None
        else:
            self.view_factor_108 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_109 = None
        else:
            self.from_surface_109 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_109 = None
        else:
            self.to_surface_109 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_109 = None
        else:
            self.view_factor_109 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_110 = None
        else:
            self.from_surface_110 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_110 = None
        else:
            self.to_surface_110 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_110 = None
        else:
            self.view_factor_110 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_111 = None
        else:
            self.from_surface_111 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_111 = None
        else:
            self.to_surface_111 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_111 = None
        else:
            self.view_factor_111 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_112 = None
        else:
            self.from_surface_112 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_112 = None
        else:
            self.to_surface_112 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_112 = None
        else:
            self.view_factor_112 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_113 = None
        else:
            self.from_surface_113 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_113 = None
        else:
            self.to_surface_113 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_113 = None
        else:
            self.view_factor_113 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_114 = None
        else:
            self.from_surface_114 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_114 = None
        else:
            self.to_surface_114 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_114 = None
        else:
            self.view_factor_114 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_115 = None
        else:
            self.from_surface_115 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_115 = None
        else:
            self.to_surface_115 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_115 = None
        else:
            self.view_factor_115 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_116 = None
        else:
            self.from_surface_116 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_116 = None
        else:
            self.to_surface_116 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_116 = None
        else:
            self.view_factor_116 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_117 = None
        else:
            self.from_surface_117 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_117 = None
        else:
            self.to_surface_117 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_117 = None
        else:
            self.view_factor_117 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_118 = None
        else:
            self.from_surface_118 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_118 = None
        else:
            self.to_surface_118 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_118 = None
        else:
            self.view_factor_118 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_119 = None
        else:
            self.from_surface_119 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_119 = None
        else:
            self.to_surface_119 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_119 = None
        else:
            self.view_factor_119 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_120 = None
        else:
            self.from_surface_120 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_120 = None
        else:
            self.to_surface_120 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_120 = None
        else:
            self.view_factor_120 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.from_surface_121 = None
        else:
            self.from_surface_121 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.to_surface_121 = None
        else:
            self.to_surface_121 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_121 = None
        else:
            self.view_factor_121 = vals[i]
        i += 1

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def from_surface_1(self):
        """Get from_surface_1

        Returns:
            str: the value of `from_surface_1` or None if not set
        """
        return self._data["From Surface 1"]

    @from_surface_1.setter
    def from_surface_1(self, value=None):
        """  Corresponds to IDD Field `from_surface_1`

        Args:
            value (str): value for IDD Field `from_surface_1`
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
                                 'for field `from_surface_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_1`')

        self._data["From Surface 1"] = value

    @property
    def to_surface_1(self):
        """Get to_surface_1

        Returns:
            str: the value of `to_surface_1` or None if not set
        """
        return self._data["To Surface 1"]

    @to_surface_1.setter
    def to_surface_1(self, value=None):
        """  Corresponds to IDD Field `to_surface_1`

        Args:
            value (str): value for IDD Field `to_surface_1`
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
                                 'for field `to_surface_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_1`')

        self._data["To Surface 1"] = value

    @property
    def view_factor_1(self):
        """Get view_factor_1

        Returns:
            float: the value of `view_factor_1` or None if not set
        """
        return self._data["View Factor 1"]

    @view_factor_1.setter
    def view_factor_1(self, value=None):
        """  Corresponds to IDD Field `view_factor_1`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_1`
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
                                 'for field `view_factor_1`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_1`')

        self._data["View Factor 1"] = value

    @property
    def from_surface_2(self):
        """Get from_surface_2

        Returns:
            str: the value of `from_surface_2` or None if not set
        """
        return self._data["From Surface 2"]

    @from_surface_2.setter
    def from_surface_2(self, value=None):
        """  Corresponds to IDD Field `from_surface_2`

        Args:
            value (str): value for IDD Field `from_surface_2`
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
                                 'for field `from_surface_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_2`')

        self._data["From Surface 2"] = value

    @property
    def to_surface_2(self):
        """Get to_surface_2

        Returns:
            str: the value of `to_surface_2` or None if not set
        """
        return self._data["To Surface 2"]

    @to_surface_2.setter
    def to_surface_2(self, value=None):
        """  Corresponds to IDD Field `to_surface_2`

        Args:
            value (str): value for IDD Field `to_surface_2`
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
                                 'for field `to_surface_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_2`')

        self._data["To Surface 2"] = value

    @property
    def view_factor_2(self):
        """Get view_factor_2

        Returns:
            float: the value of `view_factor_2` or None if not set
        """
        return self._data["View Factor 2"]

    @view_factor_2.setter
    def view_factor_2(self, value=None):
        """  Corresponds to IDD Field `view_factor_2`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_2`
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
                                 'for field `view_factor_2`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_2`')

        self._data["View Factor 2"] = value

    @property
    def from_surface_3(self):
        """Get from_surface_3

        Returns:
            str: the value of `from_surface_3` or None if not set
        """
        return self._data["From Surface 3"]

    @from_surface_3.setter
    def from_surface_3(self, value=None):
        """  Corresponds to IDD Field `from_surface_3`

        Args:
            value (str): value for IDD Field `from_surface_3`
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
                                 'for field `from_surface_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_3`')

        self._data["From Surface 3"] = value

    @property
    def to_surface_3(self):
        """Get to_surface_3

        Returns:
            str: the value of `to_surface_3` or None if not set
        """
        return self._data["To Surface 3"]

    @to_surface_3.setter
    def to_surface_3(self, value=None):
        """  Corresponds to IDD Field `to_surface_3`

        Args:
            value (str): value for IDD Field `to_surface_3`
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
                                 'for field `to_surface_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_3`')

        self._data["To Surface 3"] = value

    @property
    def view_factor_3(self):
        """Get view_factor_3

        Returns:
            float: the value of `view_factor_3` or None if not set
        """
        return self._data["View Factor 3"]

    @view_factor_3.setter
    def view_factor_3(self, value=None):
        """  Corresponds to IDD Field `view_factor_3`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_3`
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
                                 'for field `view_factor_3`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_3`')

        self._data["View Factor 3"] = value

    @property
    def from_surface_4(self):
        """Get from_surface_4

        Returns:
            str: the value of `from_surface_4` or None if not set
        """
        return self._data["From Surface 4"]

    @from_surface_4.setter
    def from_surface_4(self, value=None):
        """  Corresponds to IDD Field `from_surface_4`

        Args:
            value (str): value for IDD Field `from_surface_4`
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
                                 'for field `from_surface_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_4`')

        self._data["From Surface 4"] = value

    @property
    def to_surface_4(self):
        """Get to_surface_4

        Returns:
            str: the value of `to_surface_4` or None if not set
        """
        return self._data["To Surface 4"]

    @to_surface_4.setter
    def to_surface_4(self, value=None):
        """  Corresponds to IDD Field `to_surface_4`

        Args:
            value (str): value for IDD Field `to_surface_4`
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
                                 'for field `to_surface_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_4`')

        self._data["To Surface 4"] = value

    @property
    def view_factor_4(self):
        """Get view_factor_4

        Returns:
            float: the value of `view_factor_4` or None if not set
        """
        return self._data["View Factor 4"]

    @view_factor_4.setter
    def view_factor_4(self, value=None):
        """  Corresponds to IDD Field `view_factor_4`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_4`
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
                                 'for field `view_factor_4`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_4`')

        self._data["View Factor 4"] = value

    @property
    def from_surface_5(self):
        """Get from_surface_5

        Returns:
            str: the value of `from_surface_5` or None if not set
        """
        return self._data["From Surface 5"]

    @from_surface_5.setter
    def from_surface_5(self, value=None):
        """  Corresponds to IDD Field `from_surface_5`

        Args:
            value (str): value for IDD Field `from_surface_5`
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
                                 'for field `from_surface_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_5`')

        self._data["From Surface 5"] = value

    @property
    def to_surface_5(self):
        """Get to_surface_5

        Returns:
            str: the value of `to_surface_5` or None if not set
        """
        return self._data["To Surface 5"]

    @to_surface_5.setter
    def to_surface_5(self, value=None):
        """  Corresponds to IDD Field `to_surface_5`

        Args:
            value (str): value for IDD Field `to_surface_5`
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
                                 'for field `to_surface_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_5`')

        self._data["To Surface 5"] = value

    @property
    def view_factor_5(self):
        """Get view_factor_5

        Returns:
            float: the value of `view_factor_5` or None if not set
        """
        return self._data["View Factor 5"]

    @view_factor_5.setter
    def view_factor_5(self, value=None):
        """  Corresponds to IDD Field `view_factor_5`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_5`
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
                                 'for field `view_factor_5`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_5`')

        self._data["View Factor 5"] = value

    @property
    def from_surface_6(self):
        """Get from_surface_6

        Returns:
            str: the value of `from_surface_6` or None if not set
        """
        return self._data["From Surface 6"]

    @from_surface_6.setter
    def from_surface_6(self, value=None):
        """  Corresponds to IDD Field `from_surface_6`

        Args:
            value (str): value for IDD Field `from_surface_6`
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
                                 'for field `from_surface_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_6`')

        self._data["From Surface 6"] = value

    @property
    def to_surface_6(self):
        """Get to_surface_6

        Returns:
            str: the value of `to_surface_6` or None if not set
        """
        return self._data["To Surface 6"]

    @to_surface_6.setter
    def to_surface_6(self, value=None):
        """  Corresponds to IDD Field `to_surface_6`

        Args:
            value (str): value for IDD Field `to_surface_6`
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
                                 'for field `to_surface_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_6`')

        self._data["To Surface 6"] = value

    @property
    def view_factor_6(self):
        """Get view_factor_6

        Returns:
            float: the value of `view_factor_6` or None if not set
        """
        return self._data["View Factor 6"]

    @view_factor_6.setter
    def view_factor_6(self, value=None):
        """  Corresponds to IDD Field `view_factor_6`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_6`
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
                                 'for field `view_factor_6`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_6`')

        self._data["View Factor 6"] = value

    @property
    def from_surface_7(self):
        """Get from_surface_7

        Returns:
            str: the value of `from_surface_7` or None if not set
        """
        return self._data["From Surface 7"]

    @from_surface_7.setter
    def from_surface_7(self, value=None):
        """  Corresponds to IDD Field `from_surface_7`

        Args:
            value (str): value for IDD Field `from_surface_7`
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
                                 'for field `from_surface_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_7`')

        self._data["From Surface 7"] = value

    @property
    def to_surface_7(self):
        """Get to_surface_7

        Returns:
            str: the value of `to_surface_7` or None if not set
        """
        return self._data["To Surface 7"]

    @to_surface_7.setter
    def to_surface_7(self, value=None):
        """  Corresponds to IDD Field `to_surface_7`

        Args:
            value (str): value for IDD Field `to_surface_7`
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
                                 'for field `to_surface_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_7`')

        self._data["To Surface 7"] = value

    @property
    def view_factor_7(self):
        """Get view_factor_7

        Returns:
            float: the value of `view_factor_7` or None if not set
        """
        return self._data["View Factor 7"]

    @view_factor_7.setter
    def view_factor_7(self, value=None):
        """  Corresponds to IDD Field `view_factor_7`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_7`
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
                                 'for field `view_factor_7`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_7`')

        self._data["View Factor 7"] = value

    @property
    def from_surface_8(self):
        """Get from_surface_8

        Returns:
            str: the value of `from_surface_8` or None if not set
        """
        return self._data["From Surface 8"]

    @from_surface_8.setter
    def from_surface_8(self, value=None):
        """  Corresponds to IDD Field `from_surface_8`

        Args:
            value (str): value for IDD Field `from_surface_8`
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
                                 'for field `from_surface_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_8`')

        self._data["From Surface 8"] = value

    @property
    def to_surface_8(self):
        """Get to_surface_8

        Returns:
            str: the value of `to_surface_8` or None if not set
        """
        return self._data["To Surface 8"]

    @to_surface_8.setter
    def to_surface_8(self, value=None):
        """  Corresponds to IDD Field `to_surface_8`

        Args:
            value (str): value for IDD Field `to_surface_8`
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
                                 'for field `to_surface_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_8`')

        self._data["To Surface 8"] = value

    @property
    def view_factor_8(self):
        """Get view_factor_8

        Returns:
            float: the value of `view_factor_8` or None if not set
        """
        return self._data["View Factor 8"]

    @view_factor_8.setter
    def view_factor_8(self, value=None):
        """  Corresponds to IDD Field `view_factor_8`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_8`
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
                                 'for field `view_factor_8`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_8`')

        self._data["View Factor 8"] = value

    @property
    def from_surface_9(self):
        """Get from_surface_9

        Returns:
            str: the value of `from_surface_9` or None if not set
        """
        return self._data["From Surface 9"]

    @from_surface_9.setter
    def from_surface_9(self, value=None):
        """  Corresponds to IDD Field `from_surface_9`

        Args:
            value (str): value for IDD Field `from_surface_9`
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
                                 'for field `from_surface_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_9`')

        self._data["From Surface 9"] = value

    @property
    def to_surface_9(self):
        """Get to_surface_9

        Returns:
            str: the value of `to_surface_9` or None if not set
        """
        return self._data["To Surface 9"]

    @to_surface_9.setter
    def to_surface_9(self, value=None):
        """  Corresponds to IDD Field `to_surface_9`

        Args:
            value (str): value for IDD Field `to_surface_9`
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
                                 'for field `to_surface_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_9`')

        self._data["To Surface 9"] = value

    @property
    def view_factor_9(self):
        """Get view_factor_9

        Returns:
            float: the value of `view_factor_9` or None if not set
        """
        return self._data["View Factor 9"]

    @view_factor_9.setter
    def view_factor_9(self, value=None):
        """  Corresponds to IDD Field `view_factor_9`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_9`
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
                                 'for field `view_factor_9`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_9`')

        self._data["View Factor 9"] = value

    @property
    def from_surface_10(self):
        """Get from_surface_10

        Returns:
            str: the value of `from_surface_10` or None if not set
        """
        return self._data["From Surface 10"]

    @from_surface_10.setter
    def from_surface_10(self, value=None):
        """  Corresponds to IDD Field `from_surface_10`

        Args:
            value (str): value for IDD Field `from_surface_10`
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
                                 'for field `from_surface_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_10`')

        self._data["From Surface 10"] = value

    @property
    def to_surface_10(self):
        """Get to_surface_10

        Returns:
            str: the value of `to_surface_10` or None if not set
        """
        return self._data["To Surface 10"]

    @to_surface_10.setter
    def to_surface_10(self, value=None):
        """  Corresponds to IDD Field `to_surface_10`

        Args:
            value (str): value for IDD Field `to_surface_10`
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
                                 'for field `to_surface_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_10`')

        self._data["To Surface 10"] = value

    @property
    def view_factor_10(self):
        """Get view_factor_10

        Returns:
            float: the value of `view_factor_10` or None if not set
        """
        return self._data["View Factor 10"]

    @view_factor_10.setter
    def view_factor_10(self, value=None):
        """  Corresponds to IDD Field `view_factor_10`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_10`
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
                                 'for field `view_factor_10`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_10`')

        self._data["View Factor 10"] = value

    @property
    def from_surface_11(self):
        """Get from_surface_11

        Returns:
            str: the value of `from_surface_11` or None if not set
        """
        return self._data["From Surface 11"]

    @from_surface_11.setter
    def from_surface_11(self, value=None):
        """  Corresponds to IDD Field `from_surface_11`

        Args:
            value (str): value for IDD Field `from_surface_11`
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
                                 'for field `from_surface_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_11`')

        self._data["From Surface 11"] = value

    @property
    def to_surface_11(self):
        """Get to_surface_11

        Returns:
            str: the value of `to_surface_11` or None if not set
        """
        return self._data["To Surface 11"]

    @to_surface_11.setter
    def to_surface_11(self, value=None):
        """  Corresponds to IDD Field `to_surface_11`

        Args:
            value (str): value for IDD Field `to_surface_11`
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
                                 'for field `to_surface_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_11`')

        self._data["To Surface 11"] = value

    @property
    def view_factor_11(self):
        """Get view_factor_11

        Returns:
            float: the value of `view_factor_11` or None if not set
        """
        return self._data["View Factor 11"]

    @view_factor_11.setter
    def view_factor_11(self, value=None):
        """  Corresponds to IDD Field `view_factor_11`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_11`
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
                                 'for field `view_factor_11`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_11`')

        self._data["View Factor 11"] = value

    @property
    def from_surface_12(self):
        """Get from_surface_12

        Returns:
            str: the value of `from_surface_12` or None if not set
        """
        return self._data["From Surface 12"]

    @from_surface_12.setter
    def from_surface_12(self, value=None):
        """  Corresponds to IDD Field `from_surface_12`

        Args:
            value (str): value for IDD Field `from_surface_12`
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
                                 'for field `from_surface_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_12`')

        self._data["From Surface 12"] = value

    @property
    def to_surface_12(self):
        """Get to_surface_12

        Returns:
            str: the value of `to_surface_12` or None if not set
        """
        return self._data["To Surface 12"]

    @to_surface_12.setter
    def to_surface_12(self, value=None):
        """  Corresponds to IDD Field `to_surface_12`

        Args:
            value (str): value for IDD Field `to_surface_12`
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
                                 'for field `to_surface_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_12`')

        self._data["To Surface 12"] = value

    @property
    def view_factor_12(self):
        """Get view_factor_12

        Returns:
            float: the value of `view_factor_12` or None if not set
        """
        return self._data["View Factor 12"]

    @view_factor_12.setter
    def view_factor_12(self, value=None):
        """  Corresponds to IDD Field `view_factor_12`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_12`
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
                                 'for field `view_factor_12`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_12`')

        self._data["View Factor 12"] = value

    @property
    def from_surface_13(self):
        """Get from_surface_13

        Returns:
            str: the value of `from_surface_13` or None if not set
        """
        return self._data["From Surface 13"]

    @from_surface_13.setter
    def from_surface_13(self, value=None):
        """  Corresponds to IDD Field `from_surface_13`

        Args:
            value (str): value for IDD Field `from_surface_13`
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
                                 'for field `from_surface_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_13`')

        self._data["From Surface 13"] = value

    @property
    def to_surface_13(self):
        """Get to_surface_13

        Returns:
            str: the value of `to_surface_13` or None if not set
        """
        return self._data["To Surface 13"]

    @to_surface_13.setter
    def to_surface_13(self, value=None):
        """  Corresponds to IDD Field `to_surface_13`

        Args:
            value (str): value for IDD Field `to_surface_13`
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
                                 'for field `to_surface_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_13`')

        self._data["To Surface 13"] = value

    @property
    def view_factor_13(self):
        """Get view_factor_13

        Returns:
            float: the value of `view_factor_13` or None if not set
        """
        return self._data["View Factor 13"]

    @view_factor_13.setter
    def view_factor_13(self, value=None):
        """  Corresponds to IDD Field `view_factor_13`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_13`
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
                                 'for field `view_factor_13`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_13`')

        self._data["View Factor 13"] = value

    @property
    def from_surface_14(self):
        """Get from_surface_14

        Returns:
            str: the value of `from_surface_14` or None if not set
        """
        return self._data["From Surface 14"]

    @from_surface_14.setter
    def from_surface_14(self, value=None):
        """  Corresponds to IDD Field `from_surface_14`

        Args:
            value (str): value for IDD Field `from_surface_14`
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
                                 'for field `from_surface_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_14`')

        self._data["From Surface 14"] = value

    @property
    def to_surface_14(self):
        """Get to_surface_14

        Returns:
            str: the value of `to_surface_14` or None if not set
        """
        return self._data["To Surface 14"]

    @to_surface_14.setter
    def to_surface_14(self, value=None):
        """  Corresponds to IDD Field `to_surface_14`

        Args:
            value (str): value for IDD Field `to_surface_14`
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
                                 'for field `to_surface_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_14`')

        self._data["To Surface 14"] = value

    @property
    def view_factor_14(self):
        """Get view_factor_14

        Returns:
            float: the value of `view_factor_14` or None if not set
        """
        return self._data["View Factor 14"]

    @view_factor_14.setter
    def view_factor_14(self, value=None):
        """  Corresponds to IDD Field `view_factor_14`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_14`
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
                                 'for field `view_factor_14`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_14`')

        self._data["View Factor 14"] = value

    @property
    def from_surface_15(self):
        """Get from_surface_15

        Returns:
            str: the value of `from_surface_15` or None if not set
        """
        return self._data["From Surface 15"]

    @from_surface_15.setter
    def from_surface_15(self, value=None):
        """  Corresponds to IDD Field `from_surface_15`

        Args:
            value (str): value for IDD Field `from_surface_15`
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
                                 'for field `from_surface_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_15`')

        self._data["From Surface 15"] = value

    @property
    def to_surface_15(self):
        """Get to_surface_15

        Returns:
            str: the value of `to_surface_15` or None if not set
        """
        return self._data["To Surface 15"]

    @to_surface_15.setter
    def to_surface_15(self, value=None):
        """  Corresponds to IDD Field `to_surface_15`

        Args:
            value (str): value for IDD Field `to_surface_15`
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
                                 'for field `to_surface_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_15`')

        self._data["To Surface 15"] = value

    @property
    def view_factor_15(self):
        """Get view_factor_15

        Returns:
            float: the value of `view_factor_15` or None if not set
        """
        return self._data["View Factor 15"]

    @view_factor_15.setter
    def view_factor_15(self, value=None):
        """  Corresponds to IDD Field `view_factor_15`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_15`
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
                                 'for field `view_factor_15`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_15`')

        self._data["View Factor 15"] = value

    @property
    def from_surface_16(self):
        """Get from_surface_16

        Returns:
            str: the value of `from_surface_16` or None if not set
        """
        return self._data["From Surface 16"]

    @from_surface_16.setter
    def from_surface_16(self, value=None):
        """  Corresponds to IDD Field `from_surface_16`

        Args:
            value (str): value for IDD Field `from_surface_16`
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
                                 'for field `from_surface_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_16`')

        self._data["From Surface 16"] = value

    @property
    def to_surface_16(self):
        """Get to_surface_16

        Returns:
            str: the value of `to_surface_16` or None if not set
        """
        return self._data["To Surface 16"]

    @to_surface_16.setter
    def to_surface_16(self, value=None):
        """  Corresponds to IDD Field `to_surface_16`

        Args:
            value (str): value for IDD Field `to_surface_16`
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
                                 'for field `to_surface_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_16`')

        self._data["To Surface 16"] = value

    @property
    def view_factor_16(self):
        """Get view_factor_16

        Returns:
            float: the value of `view_factor_16` or None if not set
        """
        return self._data["View Factor 16"]

    @view_factor_16.setter
    def view_factor_16(self, value=None):
        """  Corresponds to IDD Field `view_factor_16`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_16`
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
                                 'for field `view_factor_16`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_16`')

        self._data["View Factor 16"] = value

    @property
    def from_surface_17(self):
        """Get from_surface_17

        Returns:
            str: the value of `from_surface_17` or None if not set
        """
        return self._data["From Surface 17"]

    @from_surface_17.setter
    def from_surface_17(self, value=None):
        """  Corresponds to IDD Field `from_surface_17`

        Args:
            value (str): value for IDD Field `from_surface_17`
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
                                 'for field `from_surface_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_17`')

        self._data["From Surface 17"] = value

    @property
    def to_surface_17(self):
        """Get to_surface_17

        Returns:
            str: the value of `to_surface_17` or None if not set
        """
        return self._data["To Surface 17"]

    @to_surface_17.setter
    def to_surface_17(self, value=None):
        """  Corresponds to IDD Field `to_surface_17`

        Args:
            value (str): value for IDD Field `to_surface_17`
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
                                 'for field `to_surface_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_17`')

        self._data["To Surface 17"] = value

    @property
    def view_factor_17(self):
        """Get view_factor_17

        Returns:
            float: the value of `view_factor_17` or None if not set
        """
        return self._data["View Factor 17"]

    @view_factor_17.setter
    def view_factor_17(self, value=None):
        """  Corresponds to IDD Field `view_factor_17`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_17`
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
                                 'for field `view_factor_17`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_17`')

        self._data["View Factor 17"] = value

    @property
    def from_surface_18(self):
        """Get from_surface_18

        Returns:
            str: the value of `from_surface_18` or None if not set
        """
        return self._data["From Surface 18"]

    @from_surface_18.setter
    def from_surface_18(self, value=None):
        """  Corresponds to IDD Field `from_surface_18`

        Args:
            value (str): value for IDD Field `from_surface_18`
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
                                 'for field `from_surface_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_18`')

        self._data["From Surface 18"] = value

    @property
    def to_surface_18(self):
        """Get to_surface_18

        Returns:
            str: the value of `to_surface_18` or None if not set
        """
        return self._data["To Surface 18"]

    @to_surface_18.setter
    def to_surface_18(self, value=None):
        """  Corresponds to IDD Field `to_surface_18`

        Args:
            value (str): value for IDD Field `to_surface_18`
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
                                 'for field `to_surface_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_18`')

        self._data["To Surface 18"] = value

    @property
    def view_factor_18(self):
        """Get view_factor_18

        Returns:
            float: the value of `view_factor_18` or None if not set
        """
        return self._data["View Factor 18"]

    @view_factor_18.setter
    def view_factor_18(self, value=None):
        """  Corresponds to IDD Field `view_factor_18`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_18`
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
                                 'for field `view_factor_18`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_18`')

        self._data["View Factor 18"] = value

    @property
    def from_surface_19(self):
        """Get from_surface_19

        Returns:
            str: the value of `from_surface_19` or None if not set
        """
        return self._data["From Surface 19"]

    @from_surface_19.setter
    def from_surface_19(self, value=None):
        """  Corresponds to IDD Field `from_surface_19`

        Args:
            value (str): value for IDD Field `from_surface_19`
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
                                 'for field `from_surface_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_19`')

        self._data["From Surface 19"] = value

    @property
    def to_surface_19(self):
        """Get to_surface_19

        Returns:
            str: the value of `to_surface_19` or None if not set
        """
        return self._data["To Surface 19"]

    @to_surface_19.setter
    def to_surface_19(self, value=None):
        """  Corresponds to IDD Field `to_surface_19`

        Args:
            value (str): value for IDD Field `to_surface_19`
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
                                 'for field `to_surface_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_19`')

        self._data["To Surface 19"] = value

    @property
    def view_factor_19(self):
        """Get view_factor_19

        Returns:
            float: the value of `view_factor_19` or None if not set
        """
        return self._data["View Factor 19"]

    @view_factor_19.setter
    def view_factor_19(self, value=None):
        """  Corresponds to IDD Field `view_factor_19`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_19`
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
                                 'for field `view_factor_19`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_19`')

        self._data["View Factor 19"] = value

    @property
    def from_surface_20(self):
        """Get from_surface_20

        Returns:
            str: the value of `from_surface_20` or None if not set
        """
        return self._data["From Surface 20"]

    @from_surface_20.setter
    def from_surface_20(self, value=None):
        """  Corresponds to IDD Field `from_surface_20`

        Args:
            value (str): value for IDD Field `from_surface_20`
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
                                 'for field `from_surface_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_20`')

        self._data["From Surface 20"] = value

    @property
    def to_surface_20(self):
        """Get to_surface_20

        Returns:
            str: the value of `to_surface_20` or None if not set
        """
        return self._data["To Surface 20"]

    @to_surface_20.setter
    def to_surface_20(self, value=None):
        """  Corresponds to IDD Field `to_surface_20`

        Args:
            value (str): value for IDD Field `to_surface_20`
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
                                 'for field `to_surface_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_20`')

        self._data["To Surface 20"] = value

    @property
    def view_factor_20(self):
        """Get view_factor_20

        Returns:
            float: the value of `view_factor_20` or None if not set
        """
        return self._data["View Factor 20"]

    @view_factor_20.setter
    def view_factor_20(self, value=None):
        """  Corresponds to IDD Field `view_factor_20`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_20`
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
                                 'for field `view_factor_20`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_20`')

        self._data["View Factor 20"] = value

    @property
    def from_surface_21(self):
        """Get from_surface_21

        Returns:
            str: the value of `from_surface_21` or None if not set
        """
        return self._data["From Surface 21"]

    @from_surface_21.setter
    def from_surface_21(self, value=None):
        """  Corresponds to IDD Field `from_surface_21`

        Args:
            value (str): value for IDD Field `from_surface_21`
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
                                 'for field `from_surface_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_21`')

        self._data["From Surface 21"] = value

    @property
    def to_surface_21(self):
        """Get to_surface_21

        Returns:
            str: the value of `to_surface_21` or None if not set
        """
        return self._data["To Surface 21"]

    @to_surface_21.setter
    def to_surface_21(self, value=None):
        """  Corresponds to IDD Field `to_surface_21`

        Args:
            value (str): value for IDD Field `to_surface_21`
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
                                 'for field `to_surface_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_21`')

        self._data["To Surface 21"] = value

    @property
    def view_factor_21(self):
        """Get view_factor_21

        Returns:
            float: the value of `view_factor_21` or None if not set
        """
        return self._data["View Factor 21"]

    @view_factor_21.setter
    def view_factor_21(self, value=None):
        """  Corresponds to IDD Field `view_factor_21`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_21`
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
                                 'for field `view_factor_21`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_21`')

        self._data["View Factor 21"] = value

    @property
    def from_surface_22(self):
        """Get from_surface_22

        Returns:
            str: the value of `from_surface_22` or None if not set
        """
        return self._data["From Surface 22"]

    @from_surface_22.setter
    def from_surface_22(self, value=None):
        """  Corresponds to IDD Field `from_surface_22`

        Args:
            value (str): value for IDD Field `from_surface_22`
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
                                 'for field `from_surface_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_22`')

        self._data["From Surface 22"] = value

    @property
    def to_surface_22(self):
        """Get to_surface_22

        Returns:
            str: the value of `to_surface_22` or None if not set
        """
        return self._data["To Surface 22"]

    @to_surface_22.setter
    def to_surface_22(self, value=None):
        """  Corresponds to IDD Field `to_surface_22`

        Args:
            value (str): value for IDD Field `to_surface_22`
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
                                 'for field `to_surface_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_22`')

        self._data["To Surface 22"] = value

    @property
    def view_factor_22(self):
        """Get view_factor_22

        Returns:
            float: the value of `view_factor_22` or None if not set
        """
        return self._data["View Factor 22"]

    @view_factor_22.setter
    def view_factor_22(self, value=None):
        """  Corresponds to IDD Field `view_factor_22`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_22`
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
                                 'for field `view_factor_22`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_22`')

        self._data["View Factor 22"] = value

    @property
    def from_surface_23(self):
        """Get from_surface_23

        Returns:
            str: the value of `from_surface_23` or None if not set
        """
        return self._data["From Surface 23"]

    @from_surface_23.setter
    def from_surface_23(self, value=None):
        """  Corresponds to IDD Field `from_surface_23`

        Args:
            value (str): value for IDD Field `from_surface_23`
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
                                 'for field `from_surface_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_23`')

        self._data["From Surface 23"] = value

    @property
    def to_surface_23(self):
        """Get to_surface_23

        Returns:
            str: the value of `to_surface_23` or None if not set
        """
        return self._data["To Surface 23"]

    @to_surface_23.setter
    def to_surface_23(self, value=None):
        """  Corresponds to IDD Field `to_surface_23`

        Args:
            value (str): value for IDD Field `to_surface_23`
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
                                 'for field `to_surface_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_23`')

        self._data["To Surface 23"] = value

    @property
    def view_factor_23(self):
        """Get view_factor_23

        Returns:
            float: the value of `view_factor_23` or None if not set
        """
        return self._data["View Factor 23"]

    @view_factor_23.setter
    def view_factor_23(self, value=None):
        """  Corresponds to IDD Field `view_factor_23`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_23`
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
                                 'for field `view_factor_23`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_23`')

        self._data["View Factor 23"] = value

    @property
    def from_surface_24(self):
        """Get from_surface_24

        Returns:
            str: the value of `from_surface_24` or None if not set
        """
        return self._data["From Surface 24"]

    @from_surface_24.setter
    def from_surface_24(self, value=None):
        """  Corresponds to IDD Field `from_surface_24`

        Args:
            value (str): value for IDD Field `from_surface_24`
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
                                 'for field `from_surface_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_24`')

        self._data["From Surface 24"] = value

    @property
    def to_surface_24(self):
        """Get to_surface_24

        Returns:
            str: the value of `to_surface_24` or None if not set
        """
        return self._data["To Surface 24"]

    @to_surface_24.setter
    def to_surface_24(self, value=None):
        """  Corresponds to IDD Field `to_surface_24`

        Args:
            value (str): value for IDD Field `to_surface_24`
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
                                 'for field `to_surface_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_24`')

        self._data["To Surface 24"] = value

    @property
    def view_factor_24(self):
        """Get view_factor_24

        Returns:
            float: the value of `view_factor_24` or None if not set
        """
        return self._data["View Factor 24"]

    @view_factor_24.setter
    def view_factor_24(self, value=None):
        """  Corresponds to IDD Field `view_factor_24`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_24`
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
                                 'for field `view_factor_24`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_24`')

        self._data["View Factor 24"] = value

    @property
    def from_surface_25(self):
        """Get from_surface_25

        Returns:
            str: the value of `from_surface_25` or None if not set
        """
        return self._data["From Surface 25"]

    @from_surface_25.setter
    def from_surface_25(self, value=None):
        """  Corresponds to IDD Field `from_surface_25`

        Args:
            value (str): value for IDD Field `from_surface_25`
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
                                 'for field `from_surface_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_25`')

        self._data["From Surface 25"] = value

    @property
    def to_surface_25(self):
        """Get to_surface_25

        Returns:
            str: the value of `to_surface_25` or None if not set
        """
        return self._data["To Surface 25"]

    @to_surface_25.setter
    def to_surface_25(self, value=None):
        """  Corresponds to IDD Field `to_surface_25`

        Args:
            value (str): value for IDD Field `to_surface_25`
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
                                 'for field `to_surface_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_25`')

        self._data["To Surface 25"] = value

    @property
    def view_factor_25(self):
        """Get view_factor_25

        Returns:
            float: the value of `view_factor_25` or None if not set
        """
        return self._data["View Factor 25"]

    @view_factor_25.setter
    def view_factor_25(self, value=None):
        """  Corresponds to IDD Field `view_factor_25`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_25`
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
                                 'for field `view_factor_25`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_25`')

        self._data["View Factor 25"] = value

    @property
    def from_surface_26(self):
        """Get from_surface_26

        Returns:
            str: the value of `from_surface_26` or None if not set
        """
        return self._data["From Surface 26"]

    @from_surface_26.setter
    def from_surface_26(self, value=None):
        """  Corresponds to IDD Field `from_surface_26`

        Args:
            value (str): value for IDD Field `from_surface_26`
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
                                 'for field `from_surface_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_26`')

        self._data["From Surface 26"] = value

    @property
    def to_surface_26(self):
        """Get to_surface_26

        Returns:
            str: the value of `to_surface_26` or None if not set
        """
        return self._data["To Surface 26"]

    @to_surface_26.setter
    def to_surface_26(self, value=None):
        """  Corresponds to IDD Field `to_surface_26`

        Args:
            value (str): value for IDD Field `to_surface_26`
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
                                 'for field `to_surface_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_26`')

        self._data["To Surface 26"] = value

    @property
    def view_factor_26(self):
        """Get view_factor_26

        Returns:
            float: the value of `view_factor_26` or None if not set
        """
        return self._data["View Factor 26"]

    @view_factor_26.setter
    def view_factor_26(self, value=None):
        """  Corresponds to IDD Field `view_factor_26`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_26`
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
                                 'for field `view_factor_26`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_26`')

        self._data["View Factor 26"] = value

    @property
    def from_surface_27(self):
        """Get from_surface_27

        Returns:
            str: the value of `from_surface_27` or None if not set
        """
        return self._data["From Surface 27"]

    @from_surface_27.setter
    def from_surface_27(self, value=None):
        """  Corresponds to IDD Field `from_surface_27`

        Args:
            value (str): value for IDD Field `from_surface_27`
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
                                 'for field `from_surface_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_27`')

        self._data["From Surface 27"] = value

    @property
    def to_surface_27(self):
        """Get to_surface_27

        Returns:
            str: the value of `to_surface_27` or None if not set
        """
        return self._data["To Surface 27"]

    @to_surface_27.setter
    def to_surface_27(self, value=None):
        """  Corresponds to IDD Field `to_surface_27`

        Args:
            value (str): value for IDD Field `to_surface_27`
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
                                 'for field `to_surface_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_27`')

        self._data["To Surface 27"] = value

    @property
    def view_factor_27(self):
        """Get view_factor_27

        Returns:
            float: the value of `view_factor_27` or None if not set
        """
        return self._data["View Factor 27"]

    @view_factor_27.setter
    def view_factor_27(self, value=None):
        """  Corresponds to IDD Field `view_factor_27`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_27`
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
                                 'for field `view_factor_27`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_27`')

        self._data["View Factor 27"] = value

    @property
    def from_surface_28(self):
        """Get from_surface_28

        Returns:
            str: the value of `from_surface_28` or None if not set
        """
        return self._data["From Surface 28"]

    @from_surface_28.setter
    def from_surface_28(self, value=None):
        """  Corresponds to IDD Field `from_surface_28`

        Args:
            value (str): value for IDD Field `from_surface_28`
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
                                 'for field `from_surface_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_28`')

        self._data["From Surface 28"] = value

    @property
    def to_surface_28(self):
        """Get to_surface_28

        Returns:
            str: the value of `to_surface_28` or None if not set
        """
        return self._data["To Surface 28"]

    @to_surface_28.setter
    def to_surface_28(self, value=None):
        """  Corresponds to IDD Field `to_surface_28`

        Args:
            value (str): value for IDD Field `to_surface_28`
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
                                 'for field `to_surface_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_28`')

        self._data["To Surface 28"] = value

    @property
    def view_factor_28(self):
        """Get view_factor_28

        Returns:
            float: the value of `view_factor_28` or None if not set
        """
        return self._data["View Factor 28"]

    @view_factor_28.setter
    def view_factor_28(self, value=None):
        """  Corresponds to IDD Field `view_factor_28`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_28`
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
                                 'for field `view_factor_28`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_28`')

        self._data["View Factor 28"] = value

    @property
    def from_surface_29(self):
        """Get from_surface_29

        Returns:
            str: the value of `from_surface_29` or None if not set
        """
        return self._data["From Surface 29"]

    @from_surface_29.setter
    def from_surface_29(self, value=None):
        """  Corresponds to IDD Field `from_surface_29`

        Args:
            value (str): value for IDD Field `from_surface_29`
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
                                 'for field `from_surface_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_29`')

        self._data["From Surface 29"] = value

    @property
    def to_surface_29(self):
        """Get to_surface_29

        Returns:
            str: the value of `to_surface_29` or None if not set
        """
        return self._data["To Surface 29"]

    @to_surface_29.setter
    def to_surface_29(self, value=None):
        """  Corresponds to IDD Field `to_surface_29`

        Args:
            value (str): value for IDD Field `to_surface_29`
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
                                 'for field `to_surface_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_29`')

        self._data["To Surface 29"] = value

    @property
    def view_factor_29(self):
        """Get view_factor_29

        Returns:
            float: the value of `view_factor_29` or None if not set
        """
        return self._data["View Factor 29"]

    @view_factor_29.setter
    def view_factor_29(self, value=None):
        """  Corresponds to IDD Field `view_factor_29`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_29`
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
                                 'for field `view_factor_29`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_29`')

        self._data["View Factor 29"] = value

    @property
    def from_surface_30(self):
        """Get from_surface_30

        Returns:
            str: the value of `from_surface_30` or None if not set
        """
        return self._data["From Surface 30"]

    @from_surface_30.setter
    def from_surface_30(self, value=None):
        """  Corresponds to IDD Field `from_surface_30`

        Args:
            value (str): value for IDD Field `from_surface_30`
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
                                 'for field `from_surface_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_30`')

        self._data["From Surface 30"] = value

    @property
    def to_surface_30(self):
        """Get to_surface_30

        Returns:
            str: the value of `to_surface_30` or None if not set
        """
        return self._data["To Surface 30"]

    @to_surface_30.setter
    def to_surface_30(self, value=None):
        """  Corresponds to IDD Field `to_surface_30`

        Args:
            value (str): value for IDD Field `to_surface_30`
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
                                 'for field `to_surface_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_30`')

        self._data["To Surface 30"] = value

    @property
    def view_factor_30(self):
        """Get view_factor_30

        Returns:
            float: the value of `view_factor_30` or None if not set
        """
        return self._data["View Factor 30"]

    @view_factor_30.setter
    def view_factor_30(self, value=None):
        """  Corresponds to IDD Field `view_factor_30`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_30`
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
                                 'for field `view_factor_30`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_30`')

        self._data["View Factor 30"] = value

    @property
    def from_surface_31(self):
        """Get from_surface_31

        Returns:
            str: the value of `from_surface_31` or None if not set
        """
        return self._data["From Surface 31"]

    @from_surface_31.setter
    def from_surface_31(self, value=None):
        """  Corresponds to IDD Field `from_surface_31`

        Args:
            value (str): value for IDD Field `from_surface_31`
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
                                 'for field `from_surface_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_31`')

        self._data["From Surface 31"] = value

    @property
    def to_surface_31(self):
        """Get to_surface_31

        Returns:
            str: the value of `to_surface_31` or None if not set
        """
        return self._data["To Surface 31"]

    @to_surface_31.setter
    def to_surface_31(self, value=None):
        """  Corresponds to IDD Field `to_surface_31`

        Args:
            value (str): value for IDD Field `to_surface_31`
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
                                 'for field `to_surface_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_31`')

        self._data["To Surface 31"] = value

    @property
    def view_factor_31(self):
        """Get view_factor_31

        Returns:
            float: the value of `view_factor_31` or None if not set
        """
        return self._data["View Factor 31"]

    @view_factor_31.setter
    def view_factor_31(self, value=None):
        """  Corresponds to IDD Field `view_factor_31`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_31`
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
                                 'for field `view_factor_31`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_31`')

        self._data["View Factor 31"] = value

    @property
    def from_surface_32(self):
        """Get from_surface_32

        Returns:
            str: the value of `from_surface_32` or None if not set
        """
        return self._data["From Surface 32"]

    @from_surface_32.setter
    def from_surface_32(self, value=None):
        """  Corresponds to IDD Field `from_surface_32`

        Args:
            value (str): value for IDD Field `from_surface_32`
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
                                 'for field `from_surface_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_32`')

        self._data["From Surface 32"] = value

    @property
    def to_surface_32(self):
        """Get to_surface_32

        Returns:
            str: the value of `to_surface_32` or None if not set
        """
        return self._data["To Surface 32"]

    @to_surface_32.setter
    def to_surface_32(self, value=None):
        """  Corresponds to IDD Field `to_surface_32`

        Args:
            value (str): value for IDD Field `to_surface_32`
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
                                 'for field `to_surface_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_32`')

        self._data["To Surface 32"] = value

    @property
    def view_factor_32(self):
        """Get view_factor_32

        Returns:
            float: the value of `view_factor_32` or None if not set
        """
        return self._data["View Factor 32"]

    @view_factor_32.setter
    def view_factor_32(self, value=None):
        """  Corresponds to IDD Field `view_factor_32`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_32`
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
                                 'for field `view_factor_32`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_32`')

        self._data["View Factor 32"] = value

    @property
    def from_surface_33(self):
        """Get from_surface_33

        Returns:
            str: the value of `from_surface_33` or None if not set
        """
        return self._data["From Surface 33"]

    @from_surface_33.setter
    def from_surface_33(self, value=None):
        """  Corresponds to IDD Field `from_surface_33`

        Args:
            value (str): value for IDD Field `from_surface_33`
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
                                 'for field `from_surface_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_33`')

        self._data["From Surface 33"] = value

    @property
    def to_surface_33(self):
        """Get to_surface_33

        Returns:
            str: the value of `to_surface_33` or None if not set
        """
        return self._data["To Surface 33"]

    @to_surface_33.setter
    def to_surface_33(self, value=None):
        """  Corresponds to IDD Field `to_surface_33`

        Args:
            value (str): value for IDD Field `to_surface_33`
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
                                 'for field `to_surface_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_33`')

        self._data["To Surface 33"] = value

    @property
    def view_factor_33(self):
        """Get view_factor_33

        Returns:
            float: the value of `view_factor_33` or None if not set
        """
        return self._data["View Factor 33"]

    @view_factor_33.setter
    def view_factor_33(self, value=None):
        """  Corresponds to IDD Field `view_factor_33`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_33`
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
                                 'for field `view_factor_33`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_33`')

        self._data["View Factor 33"] = value

    @property
    def from_surface_34(self):
        """Get from_surface_34

        Returns:
            str: the value of `from_surface_34` or None if not set
        """
        return self._data["From Surface 34"]

    @from_surface_34.setter
    def from_surface_34(self, value=None):
        """  Corresponds to IDD Field `from_surface_34`

        Args:
            value (str): value for IDD Field `from_surface_34`
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
                                 'for field `from_surface_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_34`')

        self._data["From Surface 34"] = value

    @property
    def to_surface_34(self):
        """Get to_surface_34

        Returns:
            str: the value of `to_surface_34` or None if not set
        """
        return self._data["To Surface 34"]

    @to_surface_34.setter
    def to_surface_34(self, value=None):
        """  Corresponds to IDD Field `to_surface_34`

        Args:
            value (str): value for IDD Field `to_surface_34`
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
                                 'for field `to_surface_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_34`')

        self._data["To Surface 34"] = value

    @property
    def view_factor_34(self):
        """Get view_factor_34

        Returns:
            float: the value of `view_factor_34` or None if not set
        """
        return self._data["View Factor 34"]

    @view_factor_34.setter
    def view_factor_34(self, value=None):
        """  Corresponds to IDD Field `view_factor_34`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_34`
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
                                 'for field `view_factor_34`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_34`')

        self._data["View Factor 34"] = value

    @property
    def from_surface_35(self):
        """Get from_surface_35

        Returns:
            str: the value of `from_surface_35` or None if not set
        """
        return self._data["From Surface 35"]

    @from_surface_35.setter
    def from_surface_35(self, value=None):
        """  Corresponds to IDD Field `from_surface_35`

        Args:
            value (str): value for IDD Field `from_surface_35`
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
                                 'for field `from_surface_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_35`')

        self._data["From Surface 35"] = value

    @property
    def to_surface_35(self):
        """Get to_surface_35

        Returns:
            str: the value of `to_surface_35` or None if not set
        """
        return self._data["To Surface 35"]

    @to_surface_35.setter
    def to_surface_35(self, value=None):
        """  Corresponds to IDD Field `to_surface_35`

        Args:
            value (str): value for IDD Field `to_surface_35`
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
                                 'for field `to_surface_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_35`')

        self._data["To Surface 35"] = value

    @property
    def view_factor_35(self):
        """Get view_factor_35

        Returns:
            float: the value of `view_factor_35` or None if not set
        """
        return self._data["View Factor 35"]

    @view_factor_35.setter
    def view_factor_35(self, value=None):
        """  Corresponds to IDD Field `view_factor_35`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_35`
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
                                 'for field `view_factor_35`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_35`')

        self._data["View Factor 35"] = value

    @property
    def from_surface_36(self):
        """Get from_surface_36

        Returns:
            str: the value of `from_surface_36` or None if not set
        """
        return self._data["From Surface 36"]

    @from_surface_36.setter
    def from_surface_36(self, value=None):
        """  Corresponds to IDD Field `from_surface_36`

        Args:
            value (str): value for IDD Field `from_surface_36`
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
                                 'for field `from_surface_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_36`')

        self._data["From Surface 36"] = value

    @property
    def to_surface_36(self):
        """Get to_surface_36

        Returns:
            str: the value of `to_surface_36` or None if not set
        """
        return self._data["To Surface 36"]

    @to_surface_36.setter
    def to_surface_36(self, value=None):
        """  Corresponds to IDD Field `to_surface_36`

        Args:
            value (str): value for IDD Field `to_surface_36`
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
                                 'for field `to_surface_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_36`')

        self._data["To Surface 36"] = value

    @property
    def view_factor_36(self):
        """Get view_factor_36

        Returns:
            float: the value of `view_factor_36` or None if not set
        """
        return self._data["View Factor 36"]

    @view_factor_36.setter
    def view_factor_36(self, value=None):
        """  Corresponds to IDD Field `view_factor_36`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_36`
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
                                 'for field `view_factor_36`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_36`')

        self._data["View Factor 36"] = value

    @property
    def from_surface_37(self):
        """Get from_surface_37

        Returns:
            str: the value of `from_surface_37` or None if not set
        """
        return self._data["From Surface 37"]

    @from_surface_37.setter
    def from_surface_37(self, value=None):
        """  Corresponds to IDD Field `from_surface_37`

        Args:
            value (str): value for IDD Field `from_surface_37`
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
                                 'for field `from_surface_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_37`')

        self._data["From Surface 37"] = value

    @property
    def to_surface_37(self):
        """Get to_surface_37

        Returns:
            str: the value of `to_surface_37` or None if not set
        """
        return self._data["To Surface 37"]

    @to_surface_37.setter
    def to_surface_37(self, value=None):
        """  Corresponds to IDD Field `to_surface_37`

        Args:
            value (str): value for IDD Field `to_surface_37`
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
                                 'for field `to_surface_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_37`')

        self._data["To Surface 37"] = value

    @property
    def view_factor_37(self):
        """Get view_factor_37

        Returns:
            float: the value of `view_factor_37` or None if not set
        """
        return self._data["View Factor 37"]

    @view_factor_37.setter
    def view_factor_37(self, value=None):
        """  Corresponds to IDD Field `view_factor_37`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_37`
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
                                 'for field `view_factor_37`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_37`')

        self._data["View Factor 37"] = value

    @property
    def from_surface_38(self):
        """Get from_surface_38

        Returns:
            str: the value of `from_surface_38` or None if not set
        """
        return self._data["From Surface 38"]

    @from_surface_38.setter
    def from_surface_38(self, value=None):
        """  Corresponds to IDD Field `from_surface_38`

        Args:
            value (str): value for IDD Field `from_surface_38`
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
                                 'for field `from_surface_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_38`')

        self._data["From Surface 38"] = value

    @property
    def to_surface_38(self):
        """Get to_surface_38

        Returns:
            str: the value of `to_surface_38` or None if not set
        """
        return self._data["To Surface 38"]

    @to_surface_38.setter
    def to_surface_38(self, value=None):
        """  Corresponds to IDD Field `to_surface_38`

        Args:
            value (str): value for IDD Field `to_surface_38`
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
                                 'for field `to_surface_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_38`')

        self._data["To Surface 38"] = value

    @property
    def view_factor_38(self):
        """Get view_factor_38

        Returns:
            float: the value of `view_factor_38` or None if not set
        """
        return self._data["View Factor 38"]

    @view_factor_38.setter
    def view_factor_38(self, value=None):
        """  Corresponds to IDD Field `view_factor_38`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_38`
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
                                 'for field `view_factor_38`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_38`')

        self._data["View Factor 38"] = value

    @property
    def from_surface_39(self):
        """Get from_surface_39

        Returns:
            str: the value of `from_surface_39` or None if not set
        """
        return self._data["From Surface 39"]

    @from_surface_39.setter
    def from_surface_39(self, value=None):
        """  Corresponds to IDD Field `from_surface_39`

        Args:
            value (str): value for IDD Field `from_surface_39`
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
                                 'for field `from_surface_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_39`')

        self._data["From Surface 39"] = value

    @property
    def to_surface_39(self):
        """Get to_surface_39

        Returns:
            str: the value of `to_surface_39` or None if not set
        """
        return self._data["To Surface 39"]

    @to_surface_39.setter
    def to_surface_39(self, value=None):
        """  Corresponds to IDD Field `to_surface_39`

        Args:
            value (str): value for IDD Field `to_surface_39`
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
                                 'for field `to_surface_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_39`')

        self._data["To Surface 39"] = value

    @property
    def view_factor_39(self):
        """Get view_factor_39

        Returns:
            float: the value of `view_factor_39` or None if not set
        """
        return self._data["View Factor 39"]

    @view_factor_39.setter
    def view_factor_39(self, value=None):
        """  Corresponds to IDD Field `view_factor_39`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_39`
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
                                 'for field `view_factor_39`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_39`')

        self._data["View Factor 39"] = value

    @property
    def from_surface_40(self):
        """Get from_surface_40

        Returns:
            str: the value of `from_surface_40` or None if not set
        """
        return self._data["From Surface 40"]

    @from_surface_40.setter
    def from_surface_40(self, value=None):
        """  Corresponds to IDD Field `from_surface_40`

        Args:
            value (str): value for IDD Field `from_surface_40`
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
                                 'for field `from_surface_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_40`')

        self._data["From Surface 40"] = value

    @property
    def to_surface_40(self):
        """Get to_surface_40

        Returns:
            str: the value of `to_surface_40` or None if not set
        """
        return self._data["To Surface 40"]

    @to_surface_40.setter
    def to_surface_40(self, value=None):
        """  Corresponds to IDD Field `to_surface_40`

        Args:
            value (str): value for IDD Field `to_surface_40`
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
                                 'for field `to_surface_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_40`')

        self._data["To Surface 40"] = value

    @property
    def view_factor_40(self):
        """Get view_factor_40

        Returns:
            float: the value of `view_factor_40` or None if not set
        """
        return self._data["View Factor 40"]

    @view_factor_40.setter
    def view_factor_40(self, value=None):
        """  Corresponds to IDD Field `view_factor_40`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_40`
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
                                 'for field `view_factor_40`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_40`')

        self._data["View Factor 40"] = value

    @property
    def from_surface_41(self):
        """Get from_surface_41

        Returns:
            str: the value of `from_surface_41` or None if not set
        """
        return self._data["From Surface 41"]

    @from_surface_41.setter
    def from_surface_41(self, value=None):
        """  Corresponds to IDD Field `from_surface_41`

        Args:
            value (str): value for IDD Field `from_surface_41`
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
                                 'for field `from_surface_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_41`')

        self._data["From Surface 41"] = value

    @property
    def to_surface_41(self):
        """Get to_surface_41

        Returns:
            str: the value of `to_surface_41` or None if not set
        """
        return self._data["To Surface 41"]

    @to_surface_41.setter
    def to_surface_41(self, value=None):
        """  Corresponds to IDD Field `to_surface_41`

        Args:
            value (str): value for IDD Field `to_surface_41`
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
                                 'for field `to_surface_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_41`')

        self._data["To Surface 41"] = value

    @property
    def view_factor_41(self):
        """Get view_factor_41

        Returns:
            float: the value of `view_factor_41` or None if not set
        """
        return self._data["View Factor 41"]

    @view_factor_41.setter
    def view_factor_41(self, value=None):
        """  Corresponds to IDD Field `view_factor_41`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_41`
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
                                 'for field `view_factor_41`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_41`')

        self._data["View Factor 41"] = value

    @property
    def from_surface_42(self):
        """Get from_surface_42

        Returns:
            str: the value of `from_surface_42` or None if not set
        """
        return self._data["From Surface 42"]

    @from_surface_42.setter
    def from_surface_42(self, value=None):
        """  Corresponds to IDD Field `from_surface_42`

        Args:
            value (str): value for IDD Field `from_surface_42`
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
                                 'for field `from_surface_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_42`')

        self._data["From Surface 42"] = value

    @property
    def to_surface_42(self):
        """Get to_surface_42

        Returns:
            str: the value of `to_surface_42` or None if not set
        """
        return self._data["To Surface 42"]

    @to_surface_42.setter
    def to_surface_42(self, value=None):
        """  Corresponds to IDD Field `to_surface_42`

        Args:
            value (str): value for IDD Field `to_surface_42`
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
                                 'for field `to_surface_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_42`')

        self._data["To Surface 42"] = value

    @property
    def view_factor_42(self):
        """Get view_factor_42

        Returns:
            float: the value of `view_factor_42` or None if not set
        """
        return self._data["View Factor 42"]

    @view_factor_42.setter
    def view_factor_42(self, value=None):
        """  Corresponds to IDD Field `view_factor_42`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_42`
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
                                 'for field `view_factor_42`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_42`')

        self._data["View Factor 42"] = value

    @property
    def from_surface_43(self):
        """Get from_surface_43

        Returns:
            str: the value of `from_surface_43` or None if not set
        """
        return self._data["From Surface 43"]

    @from_surface_43.setter
    def from_surface_43(self, value=None):
        """  Corresponds to IDD Field `from_surface_43`

        Args:
            value (str): value for IDD Field `from_surface_43`
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
                                 'for field `from_surface_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_43`')

        self._data["From Surface 43"] = value

    @property
    def to_surface_43(self):
        """Get to_surface_43

        Returns:
            str: the value of `to_surface_43` or None if not set
        """
        return self._data["To Surface 43"]

    @to_surface_43.setter
    def to_surface_43(self, value=None):
        """  Corresponds to IDD Field `to_surface_43`

        Args:
            value (str): value for IDD Field `to_surface_43`
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
                                 'for field `to_surface_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_43`')

        self._data["To Surface 43"] = value

    @property
    def view_factor_43(self):
        """Get view_factor_43

        Returns:
            float: the value of `view_factor_43` or None if not set
        """
        return self._data["View Factor 43"]

    @view_factor_43.setter
    def view_factor_43(self, value=None):
        """  Corresponds to IDD Field `view_factor_43`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_43`
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
                                 'for field `view_factor_43`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_43`')

        self._data["View Factor 43"] = value

    @property
    def from_surface_44(self):
        """Get from_surface_44

        Returns:
            str: the value of `from_surface_44` or None if not set
        """
        return self._data["From Surface 44"]

    @from_surface_44.setter
    def from_surface_44(self, value=None):
        """  Corresponds to IDD Field `from_surface_44`

        Args:
            value (str): value for IDD Field `from_surface_44`
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
                                 'for field `from_surface_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_44`')

        self._data["From Surface 44"] = value

    @property
    def to_surface_44(self):
        """Get to_surface_44

        Returns:
            str: the value of `to_surface_44` or None if not set
        """
        return self._data["To Surface 44"]

    @to_surface_44.setter
    def to_surface_44(self, value=None):
        """  Corresponds to IDD Field `to_surface_44`

        Args:
            value (str): value for IDD Field `to_surface_44`
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
                                 'for field `to_surface_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_44`')

        self._data["To Surface 44"] = value

    @property
    def view_factor_44(self):
        """Get view_factor_44

        Returns:
            float: the value of `view_factor_44` or None if not set
        """
        return self._data["View Factor 44"]

    @view_factor_44.setter
    def view_factor_44(self, value=None):
        """  Corresponds to IDD Field `view_factor_44`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_44`
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
                                 'for field `view_factor_44`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_44`')

        self._data["View Factor 44"] = value

    @property
    def from_surface_45(self):
        """Get from_surface_45

        Returns:
            str: the value of `from_surface_45` or None if not set
        """
        return self._data["From Surface 45"]

    @from_surface_45.setter
    def from_surface_45(self, value=None):
        """  Corresponds to IDD Field `from_surface_45`

        Args:
            value (str): value for IDD Field `from_surface_45`
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
                                 'for field `from_surface_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_45`')

        self._data["From Surface 45"] = value

    @property
    def to_surface_45(self):
        """Get to_surface_45

        Returns:
            str: the value of `to_surface_45` or None if not set
        """
        return self._data["To Surface 45"]

    @to_surface_45.setter
    def to_surface_45(self, value=None):
        """  Corresponds to IDD Field `to_surface_45`

        Args:
            value (str): value for IDD Field `to_surface_45`
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
                                 'for field `to_surface_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_45`')

        self._data["To Surface 45"] = value

    @property
    def view_factor_45(self):
        """Get view_factor_45

        Returns:
            float: the value of `view_factor_45` or None if not set
        """
        return self._data["View Factor 45"]

    @view_factor_45.setter
    def view_factor_45(self, value=None):
        """  Corresponds to IDD Field `view_factor_45`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_45`
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
                                 'for field `view_factor_45`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_45`')

        self._data["View Factor 45"] = value

    @property
    def from_surface_46(self):
        """Get from_surface_46

        Returns:
            str: the value of `from_surface_46` or None if not set
        """
        return self._data["From Surface 46"]

    @from_surface_46.setter
    def from_surface_46(self, value=None):
        """  Corresponds to IDD Field `from_surface_46`

        Args:
            value (str): value for IDD Field `from_surface_46`
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
                                 'for field `from_surface_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_46`')

        self._data["From Surface 46"] = value

    @property
    def to_surface_46(self):
        """Get to_surface_46

        Returns:
            str: the value of `to_surface_46` or None if not set
        """
        return self._data["To Surface 46"]

    @to_surface_46.setter
    def to_surface_46(self, value=None):
        """  Corresponds to IDD Field `to_surface_46`

        Args:
            value (str): value for IDD Field `to_surface_46`
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
                                 'for field `to_surface_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_46`')

        self._data["To Surface 46"] = value

    @property
    def view_factor_46(self):
        """Get view_factor_46

        Returns:
            float: the value of `view_factor_46` or None if not set
        """
        return self._data["View Factor 46"]

    @view_factor_46.setter
    def view_factor_46(self, value=None):
        """  Corresponds to IDD Field `view_factor_46`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_46`
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
                                 'for field `view_factor_46`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_46`')

        self._data["View Factor 46"] = value

    @property
    def from_surface_47(self):
        """Get from_surface_47

        Returns:
            str: the value of `from_surface_47` or None if not set
        """
        return self._data["From Surface 47"]

    @from_surface_47.setter
    def from_surface_47(self, value=None):
        """  Corresponds to IDD Field `from_surface_47`

        Args:
            value (str): value for IDD Field `from_surface_47`
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
                                 'for field `from_surface_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_47`')

        self._data["From Surface 47"] = value

    @property
    def to_surface_47(self):
        """Get to_surface_47

        Returns:
            str: the value of `to_surface_47` or None if not set
        """
        return self._data["To Surface 47"]

    @to_surface_47.setter
    def to_surface_47(self, value=None):
        """  Corresponds to IDD Field `to_surface_47`

        Args:
            value (str): value for IDD Field `to_surface_47`
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
                                 'for field `to_surface_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_47`')

        self._data["To Surface 47"] = value

    @property
    def view_factor_47(self):
        """Get view_factor_47

        Returns:
            float: the value of `view_factor_47` or None if not set
        """
        return self._data["View Factor 47"]

    @view_factor_47.setter
    def view_factor_47(self, value=None):
        """  Corresponds to IDD Field `view_factor_47`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_47`
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
                                 'for field `view_factor_47`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_47`')

        self._data["View Factor 47"] = value

    @property
    def from_surface_48(self):
        """Get from_surface_48

        Returns:
            str: the value of `from_surface_48` or None if not set
        """
        return self._data["From Surface 48"]

    @from_surface_48.setter
    def from_surface_48(self, value=None):
        """  Corresponds to IDD Field `from_surface_48`

        Args:
            value (str): value for IDD Field `from_surface_48`
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
                                 'for field `from_surface_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_48`')

        self._data["From Surface 48"] = value

    @property
    def to_surface_48(self):
        """Get to_surface_48

        Returns:
            str: the value of `to_surface_48` or None if not set
        """
        return self._data["To Surface 48"]

    @to_surface_48.setter
    def to_surface_48(self, value=None):
        """  Corresponds to IDD Field `to_surface_48`

        Args:
            value (str): value for IDD Field `to_surface_48`
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
                                 'for field `to_surface_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_48`')

        self._data["To Surface 48"] = value

    @property
    def view_factor_48(self):
        """Get view_factor_48

        Returns:
            float: the value of `view_factor_48` or None if not set
        """
        return self._data["View Factor 48"]

    @view_factor_48.setter
    def view_factor_48(self, value=None):
        """  Corresponds to IDD Field `view_factor_48`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_48`
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
                                 'for field `view_factor_48`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_48`')

        self._data["View Factor 48"] = value

    @property
    def from_surface_49(self):
        """Get from_surface_49

        Returns:
            str: the value of `from_surface_49` or None if not set
        """
        return self._data["From Surface 49"]

    @from_surface_49.setter
    def from_surface_49(self, value=None):
        """  Corresponds to IDD Field `from_surface_49`

        Args:
            value (str): value for IDD Field `from_surface_49`
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
                                 'for field `from_surface_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_49`')

        self._data["From Surface 49"] = value

    @property
    def to_surface_49(self):
        """Get to_surface_49

        Returns:
            str: the value of `to_surface_49` or None if not set
        """
        return self._data["To Surface 49"]

    @to_surface_49.setter
    def to_surface_49(self, value=None):
        """  Corresponds to IDD Field `to_surface_49`

        Args:
            value (str): value for IDD Field `to_surface_49`
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
                                 'for field `to_surface_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_49`')

        self._data["To Surface 49"] = value

    @property
    def view_factor_49(self):
        """Get view_factor_49

        Returns:
            float: the value of `view_factor_49` or None if not set
        """
        return self._data["View Factor 49"]

    @view_factor_49.setter
    def view_factor_49(self, value=None):
        """  Corresponds to IDD Field `view_factor_49`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_49`
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
                                 'for field `view_factor_49`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_49`')

        self._data["View Factor 49"] = value

    @property
    def from_surface_50(self):
        """Get from_surface_50

        Returns:
            str: the value of `from_surface_50` or None if not set
        """
        return self._data["From Surface 50"]

    @from_surface_50.setter
    def from_surface_50(self, value=None):
        """  Corresponds to IDD Field `from_surface_50`

        Args:
            value (str): value for IDD Field `from_surface_50`
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
                                 'for field `from_surface_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_50`')

        self._data["From Surface 50"] = value

    @property
    def to_surface_50(self):
        """Get to_surface_50

        Returns:
            str: the value of `to_surface_50` or None if not set
        """
        return self._data["To Surface 50"]

    @to_surface_50.setter
    def to_surface_50(self, value=None):
        """  Corresponds to IDD Field `to_surface_50`

        Args:
            value (str): value for IDD Field `to_surface_50`
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
                                 'for field `to_surface_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_50`')

        self._data["To Surface 50"] = value

    @property
    def view_factor_50(self):
        """Get view_factor_50

        Returns:
            float: the value of `view_factor_50` or None if not set
        """
        return self._data["View Factor 50"]

    @view_factor_50.setter
    def view_factor_50(self, value=None):
        """  Corresponds to IDD Field `view_factor_50`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_50`
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
                                 'for field `view_factor_50`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_50`')

        self._data["View Factor 50"] = value

    @property
    def from_surface_51(self):
        """Get from_surface_51

        Returns:
            str: the value of `from_surface_51` or None if not set
        """
        return self._data["From Surface 51"]

    @from_surface_51.setter
    def from_surface_51(self, value=None):
        """  Corresponds to IDD Field `from_surface_51`

        Args:
            value (str): value for IDD Field `from_surface_51`
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
                                 'for field `from_surface_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_51`')

        self._data["From Surface 51"] = value

    @property
    def to_surface_51(self):
        """Get to_surface_51

        Returns:
            str: the value of `to_surface_51` or None if not set
        """
        return self._data["To Surface 51"]

    @to_surface_51.setter
    def to_surface_51(self, value=None):
        """  Corresponds to IDD Field `to_surface_51`

        Args:
            value (str): value for IDD Field `to_surface_51`
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
                                 'for field `to_surface_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_51`')

        self._data["To Surface 51"] = value

    @property
    def view_factor_51(self):
        """Get view_factor_51

        Returns:
            float: the value of `view_factor_51` or None if not set
        """
        return self._data["View Factor 51"]

    @view_factor_51.setter
    def view_factor_51(self, value=None):
        """  Corresponds to IDD Field `view_factor_51`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_51`
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
                                 'for field `view_factor_51`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_51`')

        self._data["View Factor 51"] = value

    @property
    def from_surface_52(self):
        """Get from_surface_52

        Returns:
            str: the value of `from_surface_52` or None if not set
        """
        return self._data["From Surface 52"]

    @from_surface_52.setter
    def from_surface_52(self, value=None):
        """  Corresponds to IDD Field `from_surface_52`

        Args:
            value (str): value for IDD Field `from_surface_52`
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
                                 'for field `from_surface_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_52`')

        self._data["From Surface 52"] = value

    @property
    def to_surface_52(self):
        """Get to_surface_52

        Returns:
            str: the value of `to_surface_52` or None if not set
        """
        return self._data["To Surface 52"]

    @to_surface_52.setter
    def to_surface_52(self, value=None):
        """  Corresponds to IDD Field `to_surface_52`

        Args:
            value (str): value for IDD Field `to_surface_52`
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
                                 'for field `to_surface_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_52`')

        self._data["To Surface 52"] = value

    @property
    def view_factor_52(self):
        """Get view_factor_52

        Returns:
            float: the value of `view_factor_52` or None if not set
        """
        return self._data["View Factor 52"]

    @view_factor_52.setter
    def view_factor_52(self, value=None):
        """  Corresponds to IDD Field `view_factor_52`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_52`
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
                                 'for field `view_factor_52`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_52`')

        self._data["View Factor 52"] = value

    @property
    def from_surface_53(self):
        """Get from_surface_53

        Returns:
            str: the value of `from_surface_53` or None if not set
        """
        return self._data["From Surface 53"]

    @from_surface_53.setter
    def from_surface_53(self, value=None):
        """  Corresponds to IDD Field `from_surface_53`

        Args:
            value (str): value for IDD Field `from_surface_53`
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
                                 'for field `from_surface_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_53`')

        self._data["From Surface 53"] = value

    @property
    def to_surface_53(self):
        """Get to_surface_53

        Returns:
            str: the value of `to_surface_53` or None if not set
        """
        return self._data["To Surface 53"]

    @to_surface_53.setter
    def to_surface_53(self, value=None):
        """  Corresponds to IDD Field `to_surface_53`

        Args:
            value (str): value for IDD Field `to_surface_53`
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
                                 'for field `to_surface_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_53`')

        self._data["To Surface 53"] = value

    @property
    def view_factor_53(self):
        """Get view_factor_53

        Returns:
            float: the value of `view_factor_53` or None if not set
        """
        return self._data["View Factor 53"]

    @view_factor_53.setter
    def view_factor_53(self, value=None):
        """  Corresponds to IDD Field `view_factor_53`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_53`
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
                                 'for field `view_factor_53`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_53`')

        self._data["View Factor 53"] = value

    @property
    def from_surface_54(self):
        """Get from_surface_54

        Returns:
            str: the value of `from_surface_54` or None if not set
        """
        return self._data["From Surface 54"]

    @from_surface_54.setter
    def from_surface_54(self, value=None):
        """  Corresponds to IDD Field `from_surface_54`

        Args:
            value (str): value for IDD Field `from_surface_54`
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
                                 'for field `from_surface_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_54`')

        self._data["From Surface 54"] = value

    @property
    def to_surface_54(self):
        """Get to_surface_54

        Returns:
            str: the value of `to_surface_54` or None if not set
        """
        return self._data["To Surface 54"]

    @to_surface_54.setter
    def to_surface_54(self, value=None):
        """  Corresponds to IDD Field `to_surface_54`

        Args:
            value (str): value for IDD Field `to_surface_54`
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
                                 'for field `to_surface_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_54`')

        self._data["To Surface 54"] = value

    @property
    def view_factor_54(self):
        """Get view_factor_54

        Returns:
            float: the value of `view_factor_54` or None if not set
        """
        return self._data["View Factor 54"]

    @view_factor_54.setter
    def view_factor_54(self, value=None):
        """  Corresponds to IDD Field `view_factor_54`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_54`
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
                                 'for field `view_factor_54`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_54`')

        self._data["View Factor 54"] = value

    @property
    def from_surface_55(self):
        """Get from_surface_55

        Returns:
            str: the value of `from_surface_55` or None if not set
        """
        return self._data["From Surface 55"]

    @from_surface_55.setter
    def from_surface_55(self, value=None):
        """  Corresponds to IDD Field `from_surface_55`

        Args:
            value (str): value for IDD Field `from_surface_55`
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
                                 'for field `from_surface_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_55`')

        self._data["From Surface 55"] = value

    @property
    def to_surface_55(self):
        """Get to_surface_55

        Returns:
            str: the value of `to_surface_55` or None if not set
        """
        return self._data["To Surface 55"]

    @to_surface_55.setter
    def to_surface_55(self, value=None):
        """  Corresponds to IDD Field `to_surface_55`

        Args:
            value (str): value for IDD Field `to_surface_55`
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
                                 'for field `to_surface_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_55`')

        self._data["To Surface 55"] = value

    @property
    def view_factor_55(self):
        """Get view_factor_55

        Returns:
            float: the value of `view_factor_55` or None if not set
        """
        return self._data["View Factor 55"]

    @view_factor_55.setter
    def view_factor_55(self, value=None):
        """  Corresponds to IDD Field `view_factor_55`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_55`
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
                                 'for field `view_factor_55`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_55`')

        self._data["View Factor 55"] = value

    @property
    def from_surface_56(self):
        """Get from_surface_56

        Returns:
            str: the value of `from_surface_56` or None if not set
        """
        return self._data["From Surface 56"]

    @from_surface_56.setter
    def from_surface_56(self, value=None):
        """  Corresponds to IDD Field `from_surface_56`

        Args:
            value (str): value for IDD Field `from_surface_56`
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
                                 'for field `from_surface_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_56`')

        self._data["From Surface 56"] = value

    @property
    def to_surface_56(self):
        """Get to_surface_56

        Returns:
            str: the value of `to_surface_56` or None if not set
        """
        return self._data["To Surface 56"]

    @to_surface_56.setter
    def to_surface_56(self, value=None):
        """  Corresponds to IDD Field `to_surface_56`

        Args:
            value (str): value for IDD Field `to_surface_56`
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
                                 'for field `to_surface_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_56`')

        self._data["To Surface 56"] = value

    @property
    def view_factor_56(self):
        """Get view_factor_56

        Returns:
            float: the value of `view_factor_56` or None if not set
        """
        return self._data["View Factor 56"]

    @view_factor_56.setter
    def view_factor_56(self, value=None):
        """  Corresponds to IDD Field `view_factor_56`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_56`
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
                                 'for field `view_factor_56`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_56`')

        self._data["View Factor 56"] = value

    @property
    def from_surface_57(self):
        """Get from_surface_57

        Returns:
            str: the value of `from_surface_57` or None if not set
        """
        return self._data["From Surface 57"]

    @from_surface_57.setter
    def from_surface_57(self, value=None):
        """  Corresponds to IDD Field `from_surface_57`

        Args:
            value (str): value for IDD Field `from_surface_57`
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
                                 'for field `from_surface_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_57`')

        self._data["From Surface 57"] = value

    @property
    def to_surface_57(self):
        """Get to_surface_57

        Returns:
            str: the value of `to_surface_57` or None if not set
        """
        return self._data["To Surface 57"]

    @to_surface_57.setter
    def to_surface_57(self, value=None):
        """  Corresponds to IDD Field `to_surface_57`

        Args:
            value (str): value for IDD Field `to_surface_57`
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
                                 'for field `to_surface_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_57`')

        self._data["To Surface 57"] = value

    @property
    def view_factor_57(self):
        """Get view_factor_57

        Returns:
            float: the value of `view_factor_57` or None if not set
        """
        return self._data["View Factor 57"]

    @view_factor_57.setter
    def view_factor_57(self, value=None):
        """  Corresponds to IDD Field `view_factor_57`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_57`
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
                                 'for field `view_factor_57`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_57`')

        self._data["View Factor 57"] = value

    @property
    def from_surface_58(self):
        """Get from_surface_58

        Returns:
            str: the value of `from_surface_58` or None if not set
        """
        return self._data["From Surface 58"]

    @from_surface_58.setter
    def from_surface_58(self, value=None):
        """  Corresponds to IDD Field `from_surface_58`

        Args:
            value (str): value for IDD Field `from_surface_58`
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
                                 'for field `from_surface_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_58`')

        self._data["From Surface 58"] = value

    @property
    def to_surface_58(self):
        """Get to_surface_58

        Returns:
            str: the value of `to_surface_58` or None if not set
        """
        return self._data["To Surface 58"]

    @to_surface_58.setter
    def to_surface_58(self, value=None):
        """  Corresponds to IDD Field `to_surface_58`

        Args:
            value (str): value for IDD Field `to_surface_58`
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
                                 'for field `to_surface_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_58`')

        self._data["To Surface 58"] = value

    @property
    def view_factor_58(self):
        """Get view_factor_58

        Returns:
            float: the value of `view_factor_58` or None if not set
        """
        return self._data["View Factor 58"]

    @view_factor_58.setter
    def view_factor_58(self, value=None):
        """  Corresponds to IDD Field `view_factor_58`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_58`
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
                                 'for field `view_factor_58`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_58`')

        self._data["View Factor 58"] = value

    @property
    def from_surface_59(self):
        """Get from_surface_59

        Returns:
            str: the value of `from_surface_59` or None if not set
        """
        return self._data["From Surface 59"]

    @from_surface_59.setter
    def from_surface_59(self, value=None):
        """  Corresponds to IDD Field `from_surface_59`

        Args:
            value (str): value for IDD Field `from_surface_59`
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
                                 'for field `from_surface_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_59`')

        self._data["From Surface 59"] = value

    @property
    def to_surface_59(self):
        """Get to_surface_59

        Returns:
            str: the value of `to_surface_59` or None if not set
        """
        return self._data["To Surface 59"]

    @to_surface_59.setter
    def to_surface_59(self, value=None):
        """  Corresponds to IDD Field `to_surface_59`

        Args:
            value (str): value for IDD Field `to_surface_59`
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
                                 'for field `to_surface_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_59`')

        self._data["To Surface 59"] = value

    @property
    def view_factor_59(self):
        """Get view_factor_59

        Returns:
            float: the value of `view_factor_59` or None if not set
        """
        return self._data["View Factor 59"]

    @view_factor_59.setter
    def view_factor_59(self, value=None):
        """  Corresponds to IDD Field `view_factor_59`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_59`
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
                                 'for field `view_factor_59`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_59`')

        self._data["View Factor 59"] = value

    @property
    def from_surface_60(self):
        """Get from_surface_60

        Returns:
            str: the value of `from_surface_60` or None if not set
        """
        return self._data["From Surface 60"]

    @from_surface_60.setter
    def from_surface_60(self, value=None):
        """  Corresponds to IDD Field `from_surface_60`

        Args:
            value (str): value for IDD Field `from_surface_60`
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
                                 'for field `from_surface_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_60`')

        self._data["From Surface 60"] = value

    @property
    def to_surface_60(self):
        """Get to_surface_60

        Returns:
            str: the value of `to_surface_60` or None if not set
        """
        return self._data["To Surface 60"]

    @to_surface_60.setter
    def to_surface_60(self, value=None):
        """  Corresponds to IDD Field `to_surface_60`

        Args:
            value (str): value for IDD Field `to_surface_60`
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
                                 'for field `to_surface_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_60`')

        self._data["To Surface 60"] = value

    @property
    def view_factor_60(self):
        """Get view_factor_60

        Returns:
            float: the value of `view_factor_60` or None if not set
        """
        return self._data["View Factor 60"]

    @view_factor_60.setter
    def view_factor_60(self, value=None):
        """  Corresponds to IDD Field `view_factor_60`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_60`
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
                                 'for field `view_factor_60`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_60`')

        self._data["View Factor 60"] = value

    @property
    def from_surface_61(self):
        """Get from_surface_61

        Returns:
            str: the value of `from_surface_61` or None if not set
        """
        return self._data["From Surface 61"]

    @from_surface_61.setter
    def from_surface_61(self, value=None):
        """  Corresponds to IDD Field `from_surface_61`

        Args:
            value (str): value for IDD Field `from_surface_61`
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
                                 'for field `from_surface_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_61`')

        self._data["From Surface 61"] = value

    @property
    def to_surface_61(self):
        """Get to_surface_61

        Returns:
            str: the value of `to_surface_61` or None if not set
        """
        return self._data["To Surface 61"]

    @to_surface_61.setter
    def to_surface_61(self, value=None):
        """  Corresponds to IDD Field `to_surface_61`

        Args:
            value (str): value for IDD Field `to_surface_61`
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
                                 'for field `to_surface_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_61`')

        self._data["To Surface 61"] = value

    @property
    def view_factor_61(self):
        """Get view_factor_61

        Returns:
            float: the value of `view_factor_61` or None if not set
        """
        return self._data["View Factor 61"]

    @view_factor_61.setter
    def view_factor_61(self, value=None):
        """  Corresponds to IDD Field `view_factor_61`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_61`
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
                                 'for field `view_factor_61`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_61`')

        self._data["View Factor 61"] = value

    @property
    def from_surface_62(self):
        """Get from_surface_62

        Returns:
            str: the value of `from_surface_62` or None if not set
        """
        return self._data["From Surface 62"]

    @from_surface_62.setter
    def from_surface_62(self, value=None):
        """  Corresponds to IDD Field `from_surface_62`

        Args:
            value (str): value for IDD Field `from_surface_62`
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
                                 'for field `from_surface_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_62`')

        self._data["From Surface 62"] = value

    @property
    def to_surface_62(self):
        """Get to_surface_62

        Returns:
            str: the value of `to_surface_62` or None if not set
        """
        return self._data["To Surface 62"]

    @to_surface_62.setter
    def to_surface_62(self, value=None):
        """  Corresponds to IDD Field `to_surface_62`

        Args:
            value (str): value for IDD Field `to_surface_62`
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
                                 'for field `to_surface_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_62`')

        self._data["To Surface 62"] = value

    @property
    def view_factor_62(self):
        """Get view_factor_62

        Returns:
            float: the value of `view_factor_62` or None if not set
        """
        return self._data["View Factor 62"]

    @view_factor_62.setter
    def view_factor_62(self, value=None):
        """  Corresponds to IDD Field `view_factor_62`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_62`
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
                                 'for field `view_factor_62`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_62`')

        self._data["View Factor 62"] = value

    @property
    def from_surface_63(self):
        """Get from_surface_63

        Returns:
            str: the value of `from_surface_63` or None if not set
        """
        return self._data["From Surface 63"]

    @from_surface_63.setter
    def from_surface_63(self, value=None):
        """  Corresponds to IDD Field `from_surface_63`

        Args:
            value (str): value for IDD Field `from_surface_63`
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
                                 'for field `from_surface_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_63`')

        self._data["From Surface 63"] = value

    @property
    def to_surface_63(self):
        """Get to_surface_63

        Returns:
            str: the value of `to_surface_63` or None if not set
        """
        return self._data["To Surface 63"]

    @to_surface_63.setter
    def to_surface_63(self, value=None):
        """  Corresponds to IDD Field `to_surface_63`

        Args:
            value (str): value for IDD Field `to_surface_63`
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
                                 'for field `to_surface_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_63`')

        self._data["To Surface 63"] = value

    @property
    def view_factor_63(self):
        """Get view_factor_63

        Returns:
            float: the value of `view_factor_63` or None if not set
        """
        return self._data["View Factor 63"]

    @view_factor_63.setter
    def view_factor_63(self, value=None):
        """  Corresponds to IDD Field `view_factor_63`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_63`
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
                                 'for field `view_factor_63`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_63`')

        self._data["View Factor 63"] = value

    @property
    def from_surface_64(self):
        """Get from_surface_64

        Returns:
            str: the value of `from_surface_64` or None if not set
        """
        return self._data["From Surface 64"]

    @from_surface_64.setter
    def from_surface_64(self, value=None):
        """  Corresponds to IDD Field `from_surface_64`

        Args:
            value (str): value for IDD Field `from_surface_64`
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
                                 'for field `from_surface_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_64`')

        self._data["From Surface 64"] = value

    @property
    def to_surface_64(self):
        """Get to_surface_64

        Returns:
            str: the value of `to_surface_64` or None if not set
        """
        return self._data["To Surface 64"]

    @to_surface_64.setter
    def to_surface_64(self, value=None):
        """  Corresponds to IDD Field `to_surface_64`

        Args:
            value (str): value for IDD Field `to_surface_64`
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
                                 'for field `to_surface_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_64`')

        self._data["To Surface 64"] = value

    @property
    def view_factor_64(self):
        """Get view_factor_64

        Returns:
            float: the value of `view_factor_64` or None if not set
        """
        return self._data["View Factor 64"]

    @view_factor_64.setter
    def view_factor_64(self, value=None):
        """  Corresponds to IDD Field `view_factor_64`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_64`
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
                                 'for field `view_factor_64`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_64`')

        self._data["View Factor 64"] = value

    @property
    def from_surface_65(self):
        """Get from_surface_65

        Returns:
            str: the value of `from_surface_65` or None if not set
        """
        return self._data["From Surface 65"]

    @from_surface_65.setter
    def from_surface_65(self, value=None):
        """  Corresponds to IDD Field `from_surface_65`

        Args:
            value (str): value for IDD Field `from_surface_65`
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
                                 'for field `from_surface_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_65`')

        self._data["From Surface 65"] = value

    @property
    def to_surface_65(self):
        """Get to_surface_65

        Returns:
            str: the value of `to_surface_65` or None if not set
        """
        return self._data["To Surface 65"]

    @to_surface_65.setter
    def to_surface_65(self, value=None):
        """  Corresponds to IDD Field `to_surface_65`

        Args:
            value (str): value for IDD Field `to_surface_65`
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
                                 'for field `to_surface_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_65`')

        self._data["To Surface 65"] = value

    @property
    def view_factor_65(self):
        """Get view_factor_65

        Returns:
            float: the value of `view_factor_65` or None if not set
        """
        return self._data["View Factor 65"]

    @view_factor_65.setter
    def view_factor_65(self, value=None):
        """  Corresponds to IDD Field `view_factor_65`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_65`
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
                                 'for field `view_factor_65`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_65`')

        self._data["View Factor 65"] = value

    @property
    def from_surface_66(self):
        """Get from_surface_66

        Returns:
            str: the value of `from_surface_66` or None if not set
        """
        return self._data["From Surface 66"]

    @from_surface_66.setter
    def from_surface_66(self, value=None):
        """  Corresponds to IDD Field `from_surface_66`

        Args:
            value (str): value for IDD Field `from_surface_66`
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
                                 'for field `from_surface_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_66`')

        self._data["From Surface 66"] = value

    @property
    def to_surface_66(self):
        """Get to_surface_66

        Returns:
            str: the value of `to_surface_66` or None if not set
        """
        return self._data["To Surface 66"]

    @to_surface_66.setter
    def to_surface_66(self, value=None):
        """  Corresponds to IDD Field `to_surface_66`

        Args:
            value (str): value for IDD Field `to_surface_66`
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
                                 'for field `to_surface_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_66`')

        self._data["To Surface 66"] = value

    @property
    def view_factor_66(self):
        """Get view_factor_66

        Returns:
            float: the value of `view_factor_66` or None if not set
        """
        return self._data["View Factor 66"]

    @view_factor_66.setter
    def view_factor_66(self, value=None):
        """  Corresponds to IDD Field `view_factor_66`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_66`
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
                                 'for field `view_factor_66`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_66`')

        self._data["View Factor 66"] = value

    @property
    def from_surface_67(self):
        """Get from_surface_67

        Returns:
            str: the value of `from_surface_67` or None if not set
        """
        return self._data["From Surface 67"]

    @from_surface_67.setter
    def from_surface_67(self, value=None):
        """  Corresponds to IDD Field `from_surface_67`

        Args:
            value (str): value for IDD Field `from_surface_67`
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
                                 'for field `from_surface_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_67`')

        self._data["From Surface 67"] = value

    @property
    def to_surface_67(self):
        """Get to_surface_67

        Returns:
            str: the value of `to_surface_67` or None if not set
        """
        return self._data["To Surface 67"]

    @to_surface_67.setter
    def to_surface_67(self, value=None):
        """  Corresponds to IDD Field `to_surface_67`

        Args:
            value (str): value for IDD Field `to_surface_67`
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
                                 'for field `to_surface_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_67`')

        self._data["To Surface 67"] = value

    @property
    def view_factor_67(self):
        """Get view_factor_67

        Returns:
            float: the value of `view_factor_67` or None if not set
        """
        return self._data["View Factor 67"]

    @view_factor_67.setter
    def view_factor_67(self, value=None):
        """  Corresponds to IDD Field `view_factor_67`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_67`
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
                                 'for field `view_factor_67`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_67`')

        self._data["View Factor 67"] = value

    @property
    def from_surface_68(self):
        """Get from_surface_68

        Returns:
            str: the value of `from_surface_68` or None if not set
        """
        return self._data["From Surface 68"]

    @from_surface_68.setter
    def from_surface_68(self, value=None):
        """  Corresponds to IDD Field `from_surface_68`

        Args:
            value (str): value for IDD Field `from_surface_68`
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
                                 'for field `from_surface_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_68`')

        self._data["From Surface 68"] = value

    @property
    def to_surface_68(self):
        """Get to_surface_68

        Returns:
            str: the value of `to_surface_68` or None if not set
        """
        return self._data["To Surface 68"]

    @to_surface_68.setter
    def to_surface_68(self, value=None):
        """  Corresponds to IDD Field `to_surface_68`

        Args:
            value (str): value for IDD Field `to_surface_68`
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
                                 'for field `to_surface_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_68`')

        self._data["To Surface 68"] = value

    @property
    def view_factor_68(self):
        """Get view_factor_68

        Returns:
            float: the value of `view_factor_68` or None if not set
        """
        return self._data["View Factor 68"]

    @view_factor_68.setter
    def view_factor_68(self, value=None):
        """  Corresponds to IDD Field `view_factor_68`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_68`
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
                                 'for field `view_factor_68`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_68`')

        self._data["View Factor 68"] = value

    @property
    def from_surface_69(self):
        """Get from_surface_69

        Returns:
            str: the value of `from_surface_69` or None if not set
        """
        return self._data["From Surface 69"]

    @from_surface_69.setter
    def from_surface_69(self, value=None):
        """  Corresponds to IDD Field `from_surface_69`

        Args:
            value (str): value for IDD Field `from_surface_69`
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
                                 'for field `from_surface_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_69`')

        self._data["From Surface 69"] = value

    @property
    def to_surface_69(self):
        """Get to_surface_69

        Returns:
            str: the value of `to_surface_69` or None if not set
        """
        return self._data["To Surface 69"]

    @to_surface_69.setter
    def to_surface_69(self, value=None):
        """  Corresponds to IDD Field `to_surface_69`

        Args:
            value (str): value for IDD Field `to_surface_69`
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
                                 'for field `to_surface_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_69`')

        self._data["To Surface 69"] = value

    @property
    def view_factor_69(self):
        """Get view_factor_69

        Returns:
            float: the value of `view_factor_69` or None if not set
        """
        return self._data["View Factor 69"]

    @view_factor_69.setter
    def view_factor_69(self, value=None):
        """  Corresponds to IDD Field `view_factor_69`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_69`
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
                                 'for field `view_factor_69`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_69`')

        self._data["View Factor 69"] = value

    @property
    def from_surface_70(self):
        """Get from_surface_70

        Returns:
            str: the value of `from_surface_70` or None if not set
        """
        return self._data["From Surface 70"]

    @from_surface_70.setter
    def from_surface_70(self, value=None):
        """  Corresponds to IDD Field `from_surface_70`

        Args:
            value (str): value for IDD Field `from_surface_70`
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
                                 'for field `from_surface_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_70`')

        self._data["From Surface 70"] = value

    @property
    def to_surface_70(self):
        """Get to_surface_70

        Returns:
            str: the value of `to_surface_70` or None if not set
        """
        return self._data["To Surface 70"]

    @to_surface_70.setter
    def to_surface_70(self, value=None):
        """  Corresponds to IDD Field `to_surface_70`

        Args:
            value (str): value for IDD Field `to_surface_70`
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
                                 'for field `to_surface_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_70`')

        self._data["To Surface 70"] = value

    @property
    def view_factor_70(self):
        """Get view_factor_70

        Returns:
            float: the value of `view_factor_70` or None if not set
        """
        return self._data["View Factor 70"]

    @view_factor_70.setter
    def view_factor_70(self, value=None):
        """  Corresponds to IDD Field `view_factor_70`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_70`
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
                                 'for field `view_factor_70`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_70`')

        self._data["View Factor 70"] = value

    @property
    def from_surface_71(self):
        """Get from_surface_71

        Returns:
            str: the value of `from_surface_71` or None if not set
        """
        return self._data["From Surface 71"]

    @from_surface_71.setter
    def from_surface_71(self, value=None):
        """  Corresponds to IDD Field `from_surface_71`

        Args:
            value (str): value for IDD Field `from_surface_71`
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
                                 'for field `from_surface_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_71`')

        self._data["From Surface 71"] = value

    @property
    def to_surface_71(self):
        """Get to_surface_71

        Returns:
            str: the value of `to_surface_71` or None if not set
        """
        return self._data["To Surface 71"]

    @to_surface_71.setter
    def to_surface_71(self, value=None):
        """  Corresponds to IDD Field `to_surface_71`

        Args:
            value (str): value for IDD Field `to_surface_71`
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
                                 'for field `to_surface_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_71`')

        self._data["To Surface 71"] = value

    @property
    def view_factor_71(self):
        """Get view_factor_71

        Returns:
            float: the value of `view_factor_71` or None if not set
        """
        return self._data["View Factor 71"]

    @view_factor_71.setter
    def view_factor_71(self, value=None):
        """  Corresponds to IDD Field `view_factor_71`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_71`
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
                                 'for field `view_factor_71`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_71`')

        self._data["View Factor 71"] = value

    @property
    def from_surface_72(self):
        """Get from_surface_72

        Returns:
            str: the value of `from_surface_72` or None if not set
        """
        return self._data["From Surface 72"]

    @from_surface_72.setter
    def from_surface_72(self, value=None):
        """  Corresponds to IDD Field `from_surface_72`

        Args:
            value (str): value for IDD Field `from_surface_72`
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
                                 'for field `from_surface_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_72`')

        self._data["From Surface 72"] = value

    @property
    def to_surface_72(self):
        """Get to_surface_72

        Returns:
            str: the value of `to_surface_72` or None if not set
        """
        return self._data["To Surface 72"]

    @to_surface_72.setter
    def to_surface_72(self, value=None):
        """  Corresponds to IDD Field `to_surface_72`

        Args:
            value (str): value for IDD Field `to_surface_72`
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
                                 'for field `to_surface_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_72`')

        self._data["To Surface 72"] = value

    @property
    def view_factor_72(self):
        """Get view_factor_72

        Returns:
            float: the value of `view_factor_72` or None if not set
        """
        return self._data["View Factor 72"]

    @view_factor_72.setter
    def view_factor_72(self, value=None):
        """  Corresponds to IDD Field `view_factor_72`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_72`
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
                                 'for field `view_factor_72`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_72`')

        self._data["View Factor 72"] = value

    @property
    def from_surface_73(self):
        """Get from_surface_73

        Returns:
            str: the value of `from_surface_73` or None if not set
        """
        return self._data["From Surface 73"]

    @from_surface_73.setter
    def from_surface_73(self, value=None):
        """  Corresponds to IDD Field `from_surface_73`

        Args:
            value (str): value for IDD Field `from_surface_73`
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
                                 'for field `from_surface_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_73`')

        self._data["From Surface 73"] = value

    @property
    def to_surface_73(self):
        """Get to_surface_73

        Returns:
            str: the value of `to_surface_73` or None if not set
        """
        return self._data["To Surface 73"]

    @to_surface_73.setter
    def to_surface_73(self, value=None):
        """  Corresponds to IDD Field `to_surface_73`

        Args:
            value (str): value for IDD Field `to_surface_73`
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
                                 'for field `to_surface_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_73`')

        self._data["To Surface 73"] = value

    @property
    def view_factor_73(self):
        """Get view_factor_73

        Returns:
            float: the value of `view_factor_73` or None if not set
        """
        return self._data["View Factor 73"]

    @view_factor_73.setter
    def view_factor_73(self, value=None):
        """  Corresponds to IDD Field `view_factor_73`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_73`
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
                                 'for field `view_factor_73`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_73`')

        self._data["View Factor 73"] = value

    @property
    def from_surface_74(self):
        """Get from_surface_74

        Returns:
            str: the value of `from_surface_74` or None if not set
        """
        return self._data["From Surface 74"]

    @from_surface_74.setter
    def from_surface_74(self, value=None):
        """  Corresponds to IDD Field `from_surface_74`

        Args:
            value (str): value for IDD Field `from_surface_74`
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
                                 'for field `from_surface_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_74`')

        self._data["From Surface 74"] = value

    @property
    def to_surface_74(self):
        """Get to_surface_74

        Returns:
            str: the value of `to_surface_74` or None if not set
        """
        return self._data["To Surface 74"]

    @to_surface_74.setter
    def to_surface_74(self, value=None):
        """  Corresponds to IDD Field `to_surface_74`

        Args:
            value (str): value for IDD Field `to_surface_74`
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
                                 'for field `to_surface_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_74`')

        self._data["To Surface 74"] = value

    @property
    def view_factor_74(self):
        """Get view_factor_74

        Returns:
            float: the value of `view_factor_74` or None if not set
        """
        return self._data["View Factor 74"]

    @view_factor_74.setter
    def view_factor_74(self, value=None):
        """  Corresponds to IDD Field `view_factor_74`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_74`
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
                                 'for field `view_factor_74`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_74`')

        self._data["View Factor 74"] = value

    @property
    def from_surface_75(self):
        """Get from_surface_75

        Returns:
            str: the value of `from_surface_75` or None if not set
        """
        return self._data["From Surface 75"]

    @from_surface_75.setter
    def from_surface_75(self, value=None):
        """  Corresponds to IDD Field `from_surface_75`

        Args:
            value (str): value for IDD Field `from_surface_75`
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
                                 'for field `from_surface_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_75`')

        self._data["From Surface 75"] = value

    @property
    def to_surface_75(self):
        """Get to_surface_75

        Returns:
            str: the value of `to_surface_75` or None if not set
        """
        return self._data["To Surface 75"]

    @to_surface_75.setter
    def to_surface_75(self, value=None):
        """  Corresponds to IDD Field `to_surface_75`

        Args:
            value (str): value for IDD Field `to_surface_75`
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
                                 'for field `to_surface_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_75`')

        self._data["To Surface 75"] = value

    @property
    def view_factor_75(self):
        """Get view_factor_75

        Returns:
            float: the value of `view_factor_75` or None if not set
        """
        return self._data["View Factor 75"]

    @view_factor_75.setter
    def view_factor_75(self, value=None):
        """  Corresponds to IDD Field `view_factor_75`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_75`
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
                                 'for field `view_factor_75`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_75`')

        self._data["View Factor 75"] = value

    @property
    def from_surface_76(self):
        """Get from_surface_76

        Returns:
            str: the value of `from_surface_76` or None if not set
        """
        return self._data["From Surface 76"]

    @from_surface_76.setter
    def from_surface_76(self, value=None):
        """  Corresponds to IDD Field `from_surface_76`

        Args:
            value (str): value for IDD Field `from_surface_76`
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
                                 'for field `from_surface_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_76`')

        self._data["From Surface 76"] = value

    @property
    def to_surface_76(self):
        """Get to_surface_76

        Returns:
            str: the value of `to_surface_76` or None if not set
        """
        return self._data["To Surface 76"]

    @to_surface_76.setter
    def to_surface_76(self, value=None):
        """  Corresponds to IDD Field `to_surface_76`

        Args:
            value (str): value for IDD Field `to_surface_76`
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
                                 'for field `to_surface_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_76`')

        self._data["To Surface 76"] = value

    @property
    def view_factor_76(self):
        """Get view_factor_76

        Returns:
            float: the value of `view_factor_76` or None if not set
        """
        return self._data["View Factor 76"]

    @view_factor_76.setter
    def view_factor_76(self, value=None):
        """  Corresponds to IDD Field `view_factor_76`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_76`
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
                                 'for field `view_factor_76`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_76`')

        self._data["View Factor 76"] = value

    @property
    def from_surface_77(self):
        """Get from_surface_77

        Returns:
            str: the value of `from_surface_77` or None if not set
        """
        return self._data["From Surface 77"]

    @from_surface_77.setter
    def from_surface_77(self, value=None):
        """  Corresponds to IDD Field `from_surface_77`

        Args:
            value (str): value for IDD Field `from_surface_77`
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
                                 'for field `from_surface_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_77`')

        self._data["From Surface 77"] = value

    @property
    def to_surface_77(self):
        """Get to_surface_77

        Returns:
            str: the value of `to_surface_77` or None if not set
        """
        return self._data["To Surface 77"]

    @to_surface_77.setter
    def to_surface_77(self, value=None):
        """  Corresponds to IDD Field `to_surface_77`

        Args:
            value (str): value for IDD Field `to_surface_77`
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
                                 'for field `to_surface_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_77`')

        self._data["To Surface 77"] = value

    @property
    def view_factor_77(self):
        """Get view_factor_77

        Returns:
            float: the value of `view_factor_77` or None if not set
        """
        return self._data["View Factor 77"]

    @view_factor_77.setter
    def view_factor_77(self, value=None):
        """  Corresponds to IDD Field `view_factor_77`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_77`
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
                                 'for field `view_factor_77`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_77`')

        self._data["View Factor 77"] = value

    @property
    def from_surface_78(self):
        """Get from_surface_78

        Returns:
            str: the value of `from_surface_78` or None if not set
        """
        return self._data["From Surface 78"]

    @from_surface_78.setter
    def from_surface_78(self, value=None):
        """  Corresponds to IDD Field `from_surface_78`

        Args:
            value (str): value for IDD Field `from_surface_78`
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
                                 'for field `from_surface_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_78`')

        self._data["From Surface 78"] = value

    @property
    def to_surface_78(self):
        """Get to_surface_78

        Returns:
            str: the value of `to_surface_78` or None if not set
        """
        return self._data["To Surface 78"]

    @to_surface_78.setter
    def to_surface_78(self, value=None):
        """  Corresponds to IDD Field `to_surface_78`

        Args:
            value (str): value for IDD Field `to_surface_78`
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
                                 'for field `to_surface_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_78`')

        self._data["To Surface 78"] = value

    @property
    def view_factor_78(self):
        """Get view_factor_78

        Returns:
            float: the value of `view_factor_78` or None if not set
        """
        return self._data["View Factor 78"]

    @view_factor_78.setter
    def view_factor_78(self, value=None):
        """  Corresponds to IDD Field `view_factor_78`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_78`
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
                                 'for field `view_factor_78`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_78`')

        self._data["View Factor 78"] = value

    @property
    def from_surface_79(self):
        """Get from_surface_79

        Returns:
            str: the value of `from_surface_79` or None if not set
        """
        return self._data["From Surface 79"]

    @from_surface_79.setter
    def from_surface_79(self, value=None):
        """  Corresponds to IDD Field `from_surface_79`

        Args:
            value (str): value for IDD Field `from_surface_79`
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
                                 'for field `from_surface_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_79`')

        self._data["From Surface 79"] = value

    @property
    def to_surface_79(self):
        """Get to_surface_79

        Returns:
            str: the value of `to_surface_79` or None if not set
        """
        return self._data["To Surface 79"]

    @to_surface_79.setter
    def to_surface_79(self, value=None):
        """  Corresponds to IDD Field `to_surface_79`

        Args:
            value (str): value for IDD Field `to_surface_79`
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
                                 'for field `to_surface_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_79`')

        self._data["To Surface 79"] = value

    @property
    def view_factor_79(self):
        """Get view_factor_79

        Returns:
            float: the value of `view_factor_79` or None if not set
        """
        return self._data["View Factor 79"]

    @view_factor_79.setter
    def view_factor_79(self, value=None):
        """  Corresponds to IDD Field `view_factor_79`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_79`
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
                                 'for field `view_factor_79`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_79`')

        self._data["View Factor 79"] = value

    @property
    def from_surface_80(self):
        """Get from_surface_80

        Returns:
            str: the value of `from_surface_80` or None if not set
        """
        return self._data["From Surface 80"]

    @from_surface_80.setter
    def from_surface_80(self, value=None):
        """  Corresponds to IDD Field `from_surface_80`

        Args:
            value (str): value for IDD Field `from_surface_80`
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
                                 'for field `from_surface_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_80`')

        self._data["From Surface 80"] = value

    @property
    def to_surface_80(self):
        """Get to_surface_80

        Returns:
            str: the value of `to_surface_80` or None if not set
        """
        return self._data["To Surface 80"]

    @to_surface_80.setter
    def to_surface_80(self, value=None):
        """  Corresponds to IDD Field `to_surface_80`

        Args:
            value (str): value for IDD Field `to_surface_80`
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
                                 'for field `to_surface_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_80`')

        self._data["To Surface 80"] = value

    @property
    def view_factor_80(self):
        """Get view_factor_80

        Returns:
            float: the value of `view_factor_80` or None if not set
        """
        return self._data["View Factor 80"]

    @view_factor_80.setter
    def view_factor_80(self, value=None):
        """  Corresponds to IDD Field `view_factor_80`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_80`
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
                                 'for field `view_factor_80`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_80`')

        self._data["View Factor 80"] = value

    @property
    def from_surface_81(self):
        """Get from_surface_81

        Returns:
            str: the value of `from_surface_81` or None if not set
        """
        return self._data["From Surface 81"]

    @from_surface_81.setter
    def from_surface_81(self, value=None):
        """  Corresponds to IDD Field `from_surface_81`

        Args:
            value (str): value for IDD Field `from_surface_81`
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
                                 'for field `from_surface_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_81`')

        self._data["From Surface 81"] = value

    @property
    def to_surface_81(self):
        """Get to_surface_81

        Returns:
            str: the value of `to_surface_81` or None if not set
        """
        return self._data["To Surface 81"]

    @to_surface_81.setter
    def to_surface_81(self, value=None):
        """  Corresponds to IDD Field `to_surface_81`

        Args:
            value (str): value for IDD Field `to_surface_81`
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
                                 'for field `to_surface_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_81`')

        self._data["To Surface 81"] = value

    @property
    def view_factor_81(self):
        """Get view_factor_81

        Returns:
            float: the value of `view_factor_81` or None if not set
        """
        return self._data["View Factor 81"]

    @view_factor_81.setter
    def view_factor_81(self, value=None):
        """  Corresponds to IDD Field `view_factor_81`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_81`
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
                                 'for field `view_factor_81`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_81`')

        self._data["View Factor 81"] = value

    @property
    def from_surface_82(self):
        """Get from_surface_82

        Returns:
            str: the value of `from_surface_82` or None if not set
        """
        return self._data["From Surface 82"]

    @from_surface_82.setter
    def from_surface_82(self, value=None):
        """  Corresponds to IDD Field `from_surface_82`

        Args:
            value (str): value for IDD Field `from_surface_82`
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
                                 'for field `from_surface_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_82`')

        self._data["From Surface 82"] = value

    @property
    def to_surface_82(self):
        """Get to_surface_82

        Returns:
            str: the value of `to_surface_82` or None if not set
        """
        return self._data["To Surface 82"]

    @to_surface_82.setter
    def to_surface_82(self, value=None):
        """  Corresponds to IDD Field `to_surface_82`

        Args:
            value (str): value for IDD Field `to_surface_82`
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
                                 'for field `to_surface_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_82`')

        self._data["To Surface 82"] = value

    @property
    def view_factor_82(self):
        """Get view_factor_82

        Returns:
            float: the value of `view_factor_82` or None if not set
        """
        return self._data["View Factor 82"]

    @view_factor_82.setter
    def view_factor_82(self, value=None):
        """  Corresponds to IDD Field `view_factor_82`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_82`
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
                                 'for field `view_factor_82`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_82`')

        self._data["View Factor 82"] = value

    @property
    def from_surface_83(self):
        """Get from_surface_83

        Returns:
            str: the value of `from_surface_83` or None if not set
        """
        return self._data["From Surface 83"]

    @from_surface_83.setter
    def from_surface_83(self, value=None):
        """  Corresponds to IDD Field `from_surface_83`

        Args:
            value (str): value for IDD Field `from_surface_83`
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
                                 'for field `from_surface_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_83`')

        self._data["From Surface 83"] = value

    @property
    def to_surface_83(self):
        """Get to_surface_83

        Returns:
            str: the value of `to_surface_83` or None if not set
        """
        return self._data["To Surface 83"]

    @to_surface_83.setter
    def to_surface_83(self, value=None):
        """  Corresponds to IDD Field `to_surface_83`

        Args:
            value (str): value for IDD Field `to_surface_83`
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
                                 'for field `to_surface_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_83`')

        self._data["To Surface 83"] = value

    @property
    def view_factor_83(self):
        """Get view_factor_83

        Returns:
            float: the value of `view_factor_83` or None if not set
        """
        return self._data["View Factor 83"]

    @view_factor_83.setter
    def view_factor_83(self, value=None):
        """  Corresponds to IDD Field `view_factor_83`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_83`
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
                                 'for field `view_factor_83`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_83`')

        self._data["View Factor 83"] = value

    @property
    def from_surface_84(self):
        """Get from_surface_84

        Returns:
            str: the value of `from_surface_84` or None if not set
        """
        return self._data["From Surface 84"]

    @from_surface_84.setter
    def from_surface_84(self, value=None):
        """  Corresponds to IDD Field `from_surface_84`

        Args:
            value (str): value for IDD Field `from_surface_84`
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
                                 'for field `from_surface_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_84`')

        self._data["From Surface 84"] = value

    @property
    def to_surface_84(self):
        """Get to_surface_84

        Returns:
            str: the value of `to_surface_84` or None if not set
        """
        return self._data["To Surface 84"]

    @to_surface_84.setter
    def to_surface_84(self, value=None):
        """  Corresponds to IDD Field `to_surface_84`

        Args:
            value (str): value for IDD Field `to_surface_84`
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
                                 'for field `to_surface_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_84`')

        self._data["To Surface 84"] = value

    @property
    def view_factor_84(self):
        """Get view_factor_84

        Returns:
            float: the value of `view_factor_84` or None if not set
        """
        return self._data["View Factor 84"]

    @view_factor_84.setter
    def view_factor_84(self, value=None):
        """  Corresponds to IDD Field `view_factor_84`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_84`
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
                                 'for field `view_factor_84`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_84`')

        self._data["View Factor 84"] = value

    @property
    def from_surface_85(self):
        """Get from_surface_85

        Returns:
            str: the value of `from_surface_85` or None if not set
        """
        return self._data["From Surface 85"]

    @from_surface_85.setter
    def from_surface_85(self, value=None):
        """  Corresponds to IDD Field `from_surface_85`

        Args:
            value (str): value for IDD Field `from_surface_85`
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
                                 'for field `from_surface_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_85`')

        self._data["From Surface 85"] = value

    @property
    def to_surface_85(self):
        """Get to_surface_85

        Returns:
            str: the value of `to_surface_85` or None if not set
        """
        return self._data["To Surface 85"]

    @to_surface_85.setter
    def to_surface_85(self, value=None):
        """  Corresponds to IDD Field `to_surface_85`

        Args:
            value (str): value for IDD Field `to_surface_85`
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
                                 'for field `to_surface_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_85`')

        self._data["To Surface 85"] = value

    @property
    def view_factor_85(self):
        """Get view_factor_85

        Returns:
            float: the value of `view_factor_85` or None if not set
        """
        return self._data["View Factor 85"]

    @view_factor_85.setter
    def view_factor_85(self, value=None):
        """  Corresponds to IDD Field `view_factor_85`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_85`
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
                                 'for field `view_factor_85`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_85`')

        self._data["View Factor 85"] = value

    @property
    def from_surface_86(self):
        """Get from_surface_86

        Returns:
            str: the value of `from_surface_86` or None if not set
        """
        return self._data["From Surface 86"]

    @from_surface_86.setter
    def from_surface_86(self, value=None):
        """  Corresponds to IDD Field `from_surface_86`

        Args:
            value (str): value for IDD Field `from_surface_86`
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
                                 'for field `from_surface_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_86`')

        self._data["From Surface 86"] = value

    @property
    def to_surface_86(self):
        """Get to_surface_86

        Returns:
            str: the value of `to_surface_86` or None if not set
        """
        return self._data["To Surface 86"]

    @to_surface_86.setter
    def to_surface_86(self, value=None):
        """  Corresponds to IDD Field `to_surface_86`

        Args:
            value (str): value for IDD Field `to_surface_86`
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
                                 'for field `to_surface_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_86`')

        self._data["To Surface 86"] = value

    @property
    def view_factor_86(self):
        """Get view_factor_86

        Returns:
            float: the value of `view_factor_86` or None if not set
        """
        return self._data["View Factor 86"]

    @view_factor_86.setter
    def view_factor_86(self, value=None):
        """  Corresponds to IDD Field `view_factor_86`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_86`
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
                                 'for field `view_factor_86`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_86`')

        self._data["View Factor 86"] = value

    @property
    def from_surface_87(self):
        """Get from_surface_87

        Returns:
            str: the value of `from_surface_87` or None if not set
        """
        return self._data["From Surface 87"]

    @from_surface_87.setter
    def from_surface_87(self, value=None):
        """  Corresponds to IDD Field `from_surface_87`

        Args:
            value (str): value for IDD Field `from_surface_87`
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
                                 'for field `from_surface_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_87`')

        self._data["From Surface 87"] = value

    @property
    def to_surface_87(self):
        """Get to_surface_87

        Returns:
            str: the value of `to_surface_87` or None if not set
        """
        return self._data["To Surface 87"]

    @to_surface_87.setter
    def to_surface_87(self, value=None):
        """  Corresponds to IDD Field `to_surface_87`

        Args:
            value (str): value for IDD Field `to_surface_87`
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
                                 'for field `to_surface_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_87`')

        self._data["To Surface 87"] = value

    @property
    def view_factor_87(self):
        """Get view_factor_87

        Returns:
            float: the value of `view_factor_87` or None if not set
        """
        return self._data["View Factor 87"]

    @view_factor_87.setter
    def view_factor_87(self, value=None):
        """  Corresponds to IDD Field `view_factor_87`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_87`
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
                                 'for field `view_factor_87`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_87`')

        self._data["View Factor 87"] = value

    @property
    def from_surface_88(self):
        """Get from_surface_88

        Returns:
            str: the value of `from_surface_88` or None if not set
        """
        return self._data["From Surface 88"]

    @from_surface_88.setter
    def from_surface_88(self, value=None):
        """  Corresponds to IDD Field `from_surface_88`

        Args:
            value (str): value for IDD Field `from_surface_88`
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
                                 'for field `from_surface_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_88`')

        self._data["From Surface 88"] = value

    @property
    def to_surface_88(self):
        """Get to_surface_88

        Returns:
            str: the value of `to_surface_88` or None if not set
        """
        return self._data["To Surface 88"]

    @to_surface_88.setter
    def to_surface_88(self, value=None):
        """  Corresponds to IDD Field `to_surface_88`

        Args:
            value (str): value for IDD Field `to_surface_88`
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
                                 'for field `to_surface_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_88`')

        self._data["To Surface 88"] = value

    @property
    def view_factor_88(self):
        """Get view_factor_88

        Returns:
            float: the value of `view_factor_88` or None if not set
        """
        return self._data["View Factor 88"]

    @view_factor_88.setter
    def view_factor_88(self, value=None):
        """  Corresponds to IDD Field `view_factor_88`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_88`
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
                                 'for field `view_factor_88`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_88`')

        self._data["View Factor 88"] = value

    @property
    def from_surface_89(self):
        """Get from_surface_89

        Returns:
            str: the value of `from_surface_89` or None if not set
        """
        return self._data["From Surface 89"]

    @from_surface_89.setter
    def from_surface_89(self, value=None):
        """  Corresponds to IDD Field `from_surface_89`

        Args:
            value (str): value for IDD Field `from_surface_89`
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
                                 'for field `from_surface_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_89`')

        self._data["From Surface 89"] = value

    @property
    def to_surface_89(self):
        """Get to_surface_89

        Returns:
            str: the value of `to_surface_89` or None if not set
        """
        return self._data["To Surface 89"]

    @to_surface_89.setter
    def to_surface_89(self, value=None):
        """  Corresponds to IDD Field `to_surface_89`

        Args:
            value (str): value for IDD Field `to_surface_89`
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
                                 'for field `to_surface_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_89`')

        self._data["To Surface 89"] = value

    @property
    def view_factor_89(self):
        """Get view_factor_89

        Returns:
            float: the value of `view_factor_89` or None if not set
        """
        return self._data["View Factor 89"]

    @view_factor_89.setter
    def view_factor_89(self, value=None):
        """  Corresponds to IDD Field `view_factor_89`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_89`
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
                                 'for field `view_factor_89`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_89`')

        self._data["View Factor 89"] = value

    @property
    def from_surface_90(self):
        """Get from_surface_90

        Returns:
            str: the value of `from_surface_90` or None if not set
        """
        return self._data["From Surface 90"]

    @from_surface_90.setter
    def from_surface_90(self, value=None):
        """  Corresponds to IDD Field `from_surface_90`

        Args:
            value (str): value for IDD Field `from_surface_90`
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
                                 'for field `from_surface_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_90`')

        self._data["From Surface 90"] = value

    @property
    def to_surface_90(self):
        """Get to_surface_90

        Returns:
            str: the value of `to_surface_90` or None if not set
        """
        return self._data["To Surface 90"]

    @to_surface_90.setter
    def to_surface_90(self, value=None):
        """  Corresponds to IDD Field `to_surface_90`

        Args:
            value (str): value for IDD Field `to_surface_90`
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
                                 'for field `to_surface_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_90`')

        self._data["To Surface 90"] = value

    @property
    def view_factor_90(self):
        """Get view_factor_90

        Returns:
            float: the value of `view_factor_90` or None if not set
        """
        return self._data["View Factor 90"]

    @view_factor_90.setter
    def view_factor_90(self, value=None):
        """  Corresponds to IDD Field `view_factor_90`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_90`
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
                                 'for field `view_factor_90`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_90`')

        self._data["View Factor 90"] = value

    @property
    def from_surface_91(self):
        """Get from_surface_91

        Returns:
            str: the value of `from_surface_91` or None if not set
        """
        return self._data["From Surface 91"]

    @from_surface_91.setter
    def from_surface_91(self, value=None):
        """  Corresponds to IDD Field `from_surface_91`

        Args:
            value (str): value for IDD Field `from_surface_91`
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
                                 'for field `from_surface_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_91`')

        self._data["From Surface 91"] = value

    @property
    def to_surface_91(self):
        """Get to_surface_91

        Returns:
            str: the value of `to_surface_91` or None if not set
        """
        return self._data["To Surface 91"]

    @to_surface_91.setter
    def to_surface_91(self, value=None):
        """  Corresponds to IDD Field `to_surface_91`

        Args:
            value (str): value for IDD Field `to_surface_91`
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
                                 'for field `to_surface_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_91`')

        self._data["To Surface 91"] = value

    @property
    def view_factor_91(self):
        """Get view_factor_91

        Returns:
            float: the value of `view_factor_91` or None if not set
        """
        return self._data["View Factor 91"]

    @view_factor_91.setter
    def view_factor_91(self, value=None):
        """  Corresponds to IDD Field `view_factor_91`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_91`
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
                                 'for field `view_factor_91`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_91`')

        self._data["View Factor 91"] = value

    @property
    def from_surface_92(self):
        """Get from_surface_92

        Returns:
            str: the value of `from_surface_92` or None if not set
        """
        return self._data["From Surface 92"]

    @from_surface_92.setter
    def from_surface_92(self, value=None):
        """  Corresponds to IDD Field `from_surface_92`

        Args:
            value (str): value for IDD Field `from_surface_92`
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
                                 'for field `from_surface_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_92`')

        self._data["From Surface 92"] = value

    @property
    def to_surface_92(self):
        """Get to_surface_92

        Returns:
            str: the value of `to_surface_92` or None if not set
        """
        return self._data["To Surface 92"]

    @to_surface_92.setter
    def to_surface_92(self, value=None):
        """  Corresponds to IDD Field `to_surface_92`

        Args:
            value (str): value for IDD Field `to_surface_92`
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
                                 'for field `to_surface_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_92`')

        self._data["To Surface 92"] = value

    @property
    def view_factor_92(self):
        """Get view_factor_92

        Returns:
            float: the value of `view_factor_92` or None if not set
        """
        return self._data["View Factor 92"]

    @view_factor_92.setter
    def view_factor_92(self, value=None):
        """  Corresponds to IDD Field `view_factor_92`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_92`
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
                                 'for field `view_factor_92`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_92`')

        self._data["View Factor 92"] = value

    @property
    def from_surface_93(self):
        """Get from_surface_93

        Returns:
            str: the value of `from_surface_93` or None if not set
        """
        return self._data["From Surface 93"]

    @from_surface_93.setter
    def from_surface_93(self, value=None):
        """  Corresponds to IDD Field `from_surface_93`

        Args:
            value (str): value for IDD Field `from_surface_93`
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
                                 'for field `from_surface_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_93`')

        self._data["From Surface 93"] = value

    @property
    def to_surface_93(self):
        """Get to_surface_93

        Returns:
            str: the value of `to_surface_93` or None if not set
        """
        return self._data["To Surface 93"]

    @to_surface_93.setter
    def to_surface_93(self, value=None):
        """  Corresponds to IDD Field `to_surface_93`

        Args:
            value (str): value for IDD Field `to_surface_93`
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
                                 'for field `to_surface_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_93`')

        self._data["To Surface 93"] = value

    @property
    def view_factor_93(self):
        """Get view_factor_93

        Returns:
            float: the value of `view_factor_93` or None if not set
        """
        return self._data["View Factor 93"]

    @view_factor_93.setter
    def view_factor_93(self, value=None):
        """  Corresponds to IDD Field `view_factor_93`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_93`
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
                                 'for field `view_factor_93`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_93`')

        self._data["View Factor 93"] = value

    @property
    def from_surface_94(self):
        """Get from_surface_94

        Returns:
            str: the value of `from_surface_94` or None if not set
        """
        return self._data["From Surface 94"]

    @from_surface_94.setter
    def from_surface_94(self, value=None):
        """  Corresponds to IDD Field `from_surface_94`

        Args:
            value (str): value for IDD Field `from_surface_94`
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
                                 'for field `from_surface_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_94`')

        self._data["From Surface 94"] = value

    @property
    def to_surface_94(self):
        """Get to_surface_94

        Returns:
            str: the value of `to_surface_94` or None if not set
        """
        return self._data["To Surface 94"]

    @to_surface_94.setter
    def to_surface_94(self, value=None):
        """  Corresponds to IDD Field `to_surface_94`

        Args:
            value (str): value for IDD Field `to_surface_94`
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
                                 'for field `to_surface_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_94`')

        self._data["To Surface 94"] = value

    @property
    def view_factor_94(self):
        """Get view_factor_94

        Returns:
            float: the value of `view_factor_94` or None if not set
        """
        return self._data["View Factor 94"]

    @view_factor_94.setter
    def view_factor_94(self, value=None):
        """  Corresponds to IDD Field `view_factor_94`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_94`
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
                                 'for field `view_factor_94`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_94`')

        self._data["View Factor 94"] = value

    @property
    def from_surface_95(self):
        """Get from_surface_95

        Returns:
            str: the value of `from_surface_95` or None if not set
        """
        return self._data["From Surface 95"]

    @from_surface_95.setter
    def from_surface_95(self, value=None):
        """  Corresponds to IDD Field `from_surface_95`

        Args:
            value (str): value for IDD Field `from_surface_95`
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
                                 'for field `from_surface_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_95`')

        self._data["From Surface 95"] = value

    @property
    def to_surface_95(self):
        """Get to_surface_95

        Returns:
            str: the value of `to_surface_95` or None if not set
        """
        return self._data["To Surface 95"]

    @to_surface_95.setter
    def to_surface_95(self, value=None):
        """  Corresponds to IDD Field `to_surface_95`

        Args:
            value (str): value for IDD Field `to_surface_95`
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
                                 'for field `to_surface_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_95`')

        self._data["To Surface 95"] = value

    @property
    def view_factor_95(self):
        """Get view_factor_95

        Returns:
            float: the value of `view_factor_95` or None if not set
        """
        return self._data["View Factor 95"]

    @view_factor_95.setter
    def view_factor_95(self, value=None):
        """  Corresponds to IDD Field `view_factor_95`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_95`
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
                                 'for field `view_factor_95`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_95`')

        self._data["View Factor 95"] = value

    @property
    def from_surface_96(self):
        """Get from_surface_96

        Returns:
            str: the value of `from_surface_96` or None if not set
        """
        return self._data["From Surface 96"]

    @from_surface_96.setter
    def from_surface_96(self, value=None):
        """  Corresponds to IDD Field `from_surface_96`

        Args:
            value (str): value for IDD Field `from_surface_96`
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
                                 'for field `from_surface_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_96`')

        self._data["From Surface 96"] = value

    @property
    def to_surface_96(self):
        """Get to_surface_96

        Returns:
            str: the value of `to_surface_96` or None if not set
        """
        return self._data["To Surface 96"]

    @to_surface_96.setter
    def to_surface_96(self, value=None):
        """  Corresponds to IDD Field `to_surface_96`

        Args:
            value (str): value for IDD Field `to_surface_96`
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
                                 'for field `to_surface_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_96`')

        self._data["To Surface 96"] = value

    @property
    def view_factor_96(self):
        """Get view_factor_96

        Returns:
            float: the value of `view_factor_96` or None if not set
        """
        return self._data["View Factor 96"]

    @view_factor_96.setter
    def view_factor_96(self, value=None):
        """  Corresponds to IDD Field `view_factor_96`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_96`
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
                                 'for field `view_factor_96`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_96`')

        self._data["View Factor 96"] = value

    @property
    def from_surface_97(self):
        """Get from_surface_97

        Returns:
            str: the value of `from_surface_97` or None if not set
        """
        return self._data["From Surface 97"]

    @from_surface_97.setter
    def from_surface_97(self, value=None):
        """  Corresponds to IDD Field `from_surface_97`

        Args:
            value (str): value for IDD Field `from_surface_97`
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
                                 'for field `from_surface_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_97`')

        self._data["From Surface 97"] = value

    @property
    def to_surface_97(self):
        """Get to_surface_97

        Returns:
            str: the value of `to_surface_97` or None if not set
        """
        return self._data["To Surface 97"]

    @to_surface_97.setter
    def to_surface_97(self, value=None):
        """  Corresponds to IDD Field `to_surface_97`

        Args:
            value (str): value for IDD Field `to_surface_97`
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
                                 'for field `to_surface_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_97`')

        self._data["To Surface 97"] = value

    @property
    def view_factor_97(self):
        """Get view_factor_97

        Returns:
            float: the value of `view_factor_97` or None if not set
        """
        return self._data["View Factor 97"]

    @view_factor_97.setter
    def view_factor_97(self, value=None):
        """  Corresponds to IDD Field `view_factor_97`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_97`
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
                                 'for field `view_factor_97`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_97`')

        self._data["View Factor 97"] = value

    @property
    def from_surface_98(self):
        """Get from_surface_98

        Returns:
            str: the value of `from_surface_98` or None if not set
        """
        return self._data["From Surface 98"]

    @from_surface_98.setter
    def from_surface_98(self, value=None):
        """  Corresponds to IDD Field `from_surface_98`

        Args:
            value (str): value for IDD Field `from_surface_98`
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
                                 'for field `from_surface_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_98`')

        self._data["From Surface 98"] = value

    @property
    def to_surface_98(self):
        """Get to_surface_98

        Returns:
            str: the value of `to_surface_98` or None if not set
        """
        return self._data["To Surface 98"]

    @to_surface_98.setter
    def to_surface_98(self, value=None):
        """  Corresponds to IDD Field `to_surface_98`

        Args:
            value (str): value for IDD Field `to_surface_98`
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
                                 'for field `to_surface_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_98`')

        self._data["To Surface 98"] = value

    @property
    def view_factor_98(self):
        """Get view_factor_98

        Returns:
            float: the value of `view_factor_98` or None if not set
        """
        return self._data["View Factor 98"]

    @view_factor_98.setter
    def view_factor_98(self, value=None):
        """  Corresponds to IDD Field `view_factor_98`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_98`
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
                                 'for field `view_factor_98`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_98`')

        self._data["View Factor 98"] = value

    @property
    def from_surface_99(self):
        """Get from_surface_99

        Returns:
            str: the value of `from_surface_99` or None if not set
        """
        return self._data["From Surface 99"]

    @from_surface_99.setter
    def from_surface_99(self, value=None):
        """  Corresponds to IDD Field `from_surface_99`

        Args:
            value (str): value for IDD Field `from_surface_99`
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
                                 'for field `from_surface_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_99`')

        self._data["From Surface 99"] = value

    @property
    def to_surface_99(self):
        """Get to_surface_99

        Returns:
            str: the value of `to_surface_99` or None if not set
        """
        return self._data["To Surface 99"]

    @to_surface_99.setter
    def to_surface_99(self, value=None):
        """  Corresponds to IDD Field `to_surface_99`

        Args:
            value (str): value for IDD Field `to_surface_99`
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
                                 'for field `to_surface_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_99`')

        self._data["To Surface 99"] = value

    @property
    def view_factor_99(self):
        """Get view_factor_99

        Returns:
            float: the value of `view_factor_99` or None if not set
        """
        return self._data["View Factor 99"]

    @view_factor_99.setter
    def view_factor_99(self, value=None):
        """  Corresponds to IDD Field `view_factor_99`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_99`
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
                                 'for field `view_factor_99`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_99`')

        self._data["View Factor 99"] = value

    @property
    def from_surface_100(self):
        """Get from_surface_100

        Returns:
            str: the value of `from_surface_100` or None if not set
        """
        return self._data["From Surface 100"]

    @from_surface_100.setter
    def from_surface_100(self, value=None):
        """  Corresponds to IDD Field `from_surface_100`

        Args:
            value (str): value for IDD Field `from_surface_100`
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
                                 'for field `from_surface_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_100`')

        self._data["From Surface 100"] = value

    @property
    def to_surface_100(self):
        """Get to_surface_100

        Returns:
            str: the value of `to_surface_100` or None if not set
        """
        return self._data["To Surface 100"]

    @to_surface_100.setter
    def to_surface_100(self, value=None):
        """  Corresponds to IDD Field `to_surface_100`

        Args:
            value (str): value for IDD Field `to_surface_100`
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
                                 'for field `to_surface_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_100`')

        self._data["To Surface 100"] = value

    @property
    def view_factor_100(self):
        """Get view_factor_100

        Returns:
            float: the value of `view_factor_100` or None if not set
        """
        return self._data["View Factor 100"]

    @view_factor_100.setter
    def view_factor_100(self, value=None):
        """  Corresponds to IDD Field `view_factor_100`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_100`
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
                                 'for field `view_factor_100`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_100`')

        self._data["View Factor 100"] = value

    @property
    def from_surface_101(self):
        """Get from_surface_101

        Returns:
            str: the value of `from_surface_101` or None if not set
        """
        return self._data["From Surface 101"]

    @from_surface_101.setter
    def from_surface_101(self, value=None):
        """  Corresponds to IDD Field `from_surface_101`

        Args:
            value (str): value for IDD Field `from_surface_101`
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
                                 'for field `from_surface_101`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_101`')

        self._data["From Surface 101"] = value

    @property
    def to_surface_101(self):
        """Get to_surface_101

        Returns:
            str: the value of `to_surface_101` or None if not set
        """
        return self._data["To Surface 101"]

    @to_surface_101.setter
    def to_surface_101(self, value=None):
        """  Corresponds to IDD Field `to_surface_101`

        Args:
            value (str): value for IDD Field `to_surface_101`
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
                                 'for field `to_surface_101`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_101`')

        self._data["To Surface 101"] = value

    @property
    def view_factor_101(self):
        """Get view_factor_101

        Returns:
            float: the value of `view_factor_101` or None if not set
        """
        return self._data["View Factor 101"]

    @view_factor_101.setter
    def view_factor_101(self, value=None):
        """  Corresponds to IDD Field `view_factor_101`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_101`
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
                                 'for field `view_factor_101`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_101`')

        self._data["View Factor 101"] = value

    @property
    def from_surface_102(self):
        """Get from_surface_102

        Returns:
            str: the value of `from_surface_102` or None if not set
        """
        return self._data["From Surface 102"]

    @from_surface_102.setter
    def from_surface_102(self, value=None):
        """  Corresponds to IDD Field `from_surface_102`

        Args:
            value (str): value for IDD Field `from_surface_102`
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
                                 'for field `from_surface_102`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_102`')

        self._data["From Surface 102"] = value

    @property
    def to_surface_102(self):
        """Get to_surface_102

        Returns:
            str: the value of `to_surface_102` or None if not set
        """
        return self._data["To Surface 102"]

    @to_surface_102.setter
    def to_surface_102(self, value=None):
        """  Corresponds to IDD Field `to_surface_102`

        Args:
            value (str): value for IDD Field `to_surface_102`
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
                                 'for field `to_surface_102`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_102`')

        self._data["To Surface 102"] = value

    @property
    def view_factor_102(self):
        """Get view_factor_102

        Returns:
            float: the value of `view_factor_102` or None if not set
        """
        return self._data["View Factor 102"]

    @view_factor_102.setter
    def view_factor_102(self, value=None):
        """  Corresponds to IDD Field `view_factor_102`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_102`
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
                                 'for field `view_factor_102`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_102`')

        self._data["View Factor 102"] = value

    @property
    def from_surface_103(self):
        """Get from_surface_103

        Returns:
            str: the value of `from_surface_103` or None if not set
        """
        return self._data["From Surface 103"]

    @from_surface_103.setter
    def from_surface_103(self, value=None):
        """  Corresponds to IDD Field `from_surface_103`

        Args:
            value (str): value for IDD Field `from_surface_103`
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
                                 'for field `from_surface_103`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_103`')

        self._data["From Surface 103"] = value

    @property
    def to_surface_103(self):
        """Get to_surface_103

        Returns:
            str: the value of `to_surface_103` or None if not set
        """
        return self._data["To Surface 103"]

    @to_surface_103.setter
    def to_surface_103(self, value=None):
        """  Corresponds to IDD Field `to_surface_103`

        Args:
            value (str): value for IDD Field `to_surface_103`
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
                                 'for field `to_surface_103`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_103`')

        self._data["To Surface 103"] = value

    @property
    def view_factor_103(self):
        """Get view_factor_103

        Returns:
            float: the value of `view_factor_103` or None if not set
        """
        return self._data["View Factor 103"]

    @view_factor_103.setter
    def view_factor_103(self, value=None):
        """  Corresponds to IDD Field `view_factor_103`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_103`
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
                                 'for field `view_factor_103`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_103`')

        self._data["View Factor 103"] = value

    @property
    def from_surface_104(self):
        """Get from_surface_104

        Returns:
            str: the value of `from_surface_104` or None if not set
        """
        return self._data["From Surface 104"]

    @from_surface_104.setter
    def from_surface_104(self, value=None):
        """  Corresponds to IDD Field `from_surface_104`

        Args:
            value (str): value for IDD Field `from_surface_104`
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
                                 'for field `from_surface_104`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_104`')

        self._data["From Surface 104"] = value

    @property
    def to_surface_104(self):
        """Get to_surface_104

        Returns:
            str: the value of `to_surface_104` or None if not set
        """
        return self._data["To Surface 104"]

    @to_surface_104.setter
    def to_surface_104(self, value=None):
        """  Corresponds to IDD Field `to_surface_104`

        Args:
            value (str): value for IDD Field `to_surface_104`
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
                                 'for field `to_surface_104`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_104`')

        self._data["To Surface 104"] = value

    @property
    def view_factor_104(self):
        """Get view_factor_104

        Returns:
            float: the value of `view_factor_104` or None if not set
        """
        return self._data["View Factor 104"]

    @view_factor_104.setter
    def view_factor_104(self, value=None):
        """  Corresponds to IDD Field `view_factor_104`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_104`
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
                                 'for field `view_factor_104`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_104`')

        self._data["View Factor 104"] = value

    @property
    def from_surface_105(self):
        """Get from_surface_105

        Returns:
            str: the value of `from_surface_105` or None if not set
        """
        return self._data["From Surface 105"]

    @from_surface_105.setter
    def from_surface_105(self, value=None):
        """  Corresponds to IDD Field `from_surface_105`

        Args:
            value (str): value for IDD Field `from_surface_105`
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
                                 'for field `from_surface_105`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_105`')

        self._data["From Surface 105"] = value

    @property
    def to_surface_105(self):
        """Get to_surface_105

        Returns:
            str: the value of `to_surface_105` or None if not set
        """
        return self._data["To Surface 105"]

    @to_surface_105.setter
    def to_surface_105(self, value=None):
        """  Corresponds to IDD Field `to_surface_105`

        Args:
            value (str): value for IDD Field `to_surface_105`
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
                                 'for field `to_surface_105`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_105`')

        self._data["To Surface 105"] = value

    @property
    def view_factor_105(self):
        """Get view_factor_105

        Returns:
            float: the value of `view_factor_105` or None if not set
        """
        return self._data["View Factor 105"]

    @view_factor_105.setter
    def view_factor_105(self, value=None):
        """  Corresponds to IDD Field `view_factor_105`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_105`
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
                                 'for field `view_factor_105`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_105`')

        self._data["View Factor 105"] = value

    @property
    def from_surface_106(self):
        """Get from_surface_106

        Returns:
            str: the value of `from_surface_106` or None if not set
        """
        return self._data["From Surface 106"]

    @from_surface_106.setter
    def from_surface_106(self, value=None):
        """  Corresponds to IDD Field `from_surface_106`

        Args:
            value (str): value for IDD Field `from_surface_106`
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
                                 'for field `from_surface_106`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_106`')

        self._data["From Surface 106"] = value

    @property
    def to_surface_106(self):
        """Get to_surface_106

        Returns:
            str: the value of `to_surface_106` or None if not set
        """
        return self._data["To Surface 106"]

    @to_surface_106.setter
    def to_surface_106(self, value=None):
        """  Corresponds to IDD Field `to_surface_106`

        Args:
            value (str): value for IDD Field `to_surface_106`
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
                                 'for field `to_surface_106`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_106`')

        self._data["To Surface 106"] = value

    @property
    def view_factor_106(self):
        """Get view_factor_106

        Returns:
            float: the value of `view_factor_106` or None if not set
        """
        return self._data["View Factor 106"]

    @view_factor_106.setter
    def view_factor_106(self, value=None):
        """  Corresponds to IDD Field `view_factor_106`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_106`
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
                                 'for field `view_factor_106`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_106`')

        self._data["View Factor 106"] = value

    @property
    def from_surface_107(self):
        """Get from_surface_107

        Returns:
            str: the value of `from_surface_107` or None if not set
        """
        return self._data["From Surface 107"]

    @from_surface_107.setter
    def from_surface_107(self, value=None):
        """  Corresponds to IDD Field `from_surface_107`

        Args:
            value (str): value for IDD Field `from_surface_107`
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
                                 'for field `from_surface_107`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_107`')

        self._data["From Surface 107"] = value

    @property
    def to_surface_107(self):
        """Get to_surface_107

        Returns:
            str: the value of `to_surface_107` or None if not set
        """
        return self._data["To Surface 107"]

    @to_surface_107.setter
    def to_surface_107(self, value=None):
        """  Corresponds to IDD Field `to_surface_107`

        Args:
            value (str): value for IDD Field `to_surface_107`
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
                                 'for field `to_surface_107`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_107`')

        self._data["To Surface 107"] = value

    @property
    def view_factor_107(self):
        """Get view_factor_107

        Returns:
            float: the value of `view_factor_107` or None if not set
        """
        return self._data["View Factor 107"]

    @view_factor_107.setter
    def view_factor_107(self, value=None):
        """  Corresponds to IDD Field `view_factor_107`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_107`
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
                                 'for field `view_factor_107`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_107`')

        self._data["View Factor 107"] = value

    @property
    def from_surface_108(self):
        """Get from_surface_108

        Returns:
            str: the value of `from_surface_108` or None if not set
        """
        return self._data["From Surface 108"]

    @from_surface_108.setter
    def from_surface_108(self, value=None):
        """  Corresponds to IDD Field `from_surface_108`

        Args:
            value (str): value for IDD Field `from_surface_108`
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
                                 'for field `from_surface_108`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_108`')

        self._data["From Surface 108"] = value

    @property
    def to_surface_108(self):
        """Get to_surface_108

        Returns:
            str: the value of `to_surface_108` or None if not set
        """
        return self._data["To Surface 108"]

    @to_surface_108.setter
    def to_surface_108(self, value=None):
        """  Corresponds to IDD Field `to_surface_108`

        Args:
            value (str): value for IDD Field `to_surface_108`
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
                                 'for field `to_surface_108`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_108`')

        self._data["To Surface 108"] = value

    @property
    def view_factor_108(self):
        """Get view_factor_108

        Returns:
            float: the value of `view_factor_108` or None if not set
        """
        return self._data["View Factor 108"]

    @view_factor_108.setter
    def view_factor_108(self, value=None):
        """  Corresponds to IDD Field `view_factor_108`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_108`
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
                                 'for field `view_factor_108`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_108`')

        self._data["View Factor 108"] = value

    @property
    def from_surface_109(self):
        """Get from_surface_109

        Returns:
            str: the value of `from_surface_109` or None if not set
        """
        return self._data["From Surface 109"]

    @from_surface_109.setter
    def from_surface_109(self, value=None):
        """  Corresponds to IDD Field `from_surface_109`

        Args:
            value (str): value for IDD Field `from_surface_109`
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
                                 'for field `from_surface_109`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_109`')

        self._data["From Surface 109"] = value

    @property
    def to_surface_109(self):
        """Get to_surface_109

        Returns:
            str: the value of `to_surface_109` or None if not set
        """
        return self._data["To Surface 109"]

    @to_surface_109.setter
    def to_surface_109(self, value=None):
        """  Corresponds to IDD Field `to_surface_109`

        Args:
            value (str): value for IDD Field `to_surface_109`
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
                                 'for field `to_surface_109`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_109`')

        self._data["To Surface 109"] = value

    @property
    def view_factor_109(self):
        """Get view_factor_109

        Returns:
            float: the value of `view_factor_109` or None if not set
        """
        return self._data["View Factor 109"]

    @view_factor_109.setter
    def view_factor_109(self, value=None):
        """  Corresponds to IDD Field `view_factor_109`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_109`
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
                                 'for field `view_factor_109`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_109`')

        self._data["View Factor 109"] = value

    @property
    def from_surface_110(self):
        """Get from_surface_110

        Returns:
            str: the value of `from_surface_110` or None if not set
        """
        return self._data["From Surface 110"]

    @from_surface_110.setter
    def from_surface_110(self, value=None):
        """  Corresponds to IDD Field `from_surface_110`

        Args:
            value (str): value for IDD Field `from_surface_110`
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
                                 'for field `from_surface_110`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_110`')

        self._data["From Surface 110"] = value

    @property
    def to_surface_110(self):
        """Get to_surface_110

        Returns:
            str: the value of `to_surface_110` or None if not set
        """
        return self._data["To Surface 110"]

    @to_surface_110.setter
    def to_surface_110(self, value=None):
        """  Corresponds to IDD Field `to_surface_110`

        Args:
            value (str): value for IDD Field `to_surface_110`
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
                                 'for field `to_surface_110`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_110`')

        self._data["To Surface 110"] = value

    @property
    def view_factor_110(self):
        """Get view_factor_110

        Returns:
            float: the value of `view_factor_110` or None if not set
        """
        return self._data["View Factor 110"]

    @view_factor_110.setter
    def view_factor_110(self, value=None):
        """  Corresponds to IDD Field `view_factor_110`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_110`
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
                                 'for field `view_factor_110`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_110`')

        self._data["View Factor 110"] = value

    @property
    def from_surface_111(self):
        """Get from_surface_111

        Returns:
            str: the value of `from_surface_111` or None if not set
        """
        return self._data["From Surface 111"]

    @from_surface_111.setter
    def from_surface_111(self, value=None):
        """  Corresponds to IDD Field `from_surface_111`

        Args:
            value (str): value for IDD Field `from_surface_111`
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
                                 'for field `from_surface_111`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_111`')

        self._data["From Surface 111"] = value

    @property
    def to_surface_111(self):
        """Get to_surface_111

        Returns:
            str: the value of `to_surface_111` or None if not set
        """
        return self._data["To Surface 111"]

    @to_surface_111.setter
    def to_surface_111(self, value=None):
        """  Corresponds to IDD Field `to_surface_111`

        Args:
            value (str): value for IDD Field `to_surface_111`
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
                                 'for field `to_surface_111`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_111`')

        self._data["To Surface 111"] = value

    @property
    def view_factor_111(self):
        """Get view_factor_111

        Returns:
            float: the value of `view_factor_111` or None if not set
        """
        return self._data["View Factor 111"]

    @view_factor_111.setter
    def view_factor_111(self, value=None):
        """  Corresponds to IDD Field `view_factor_111`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_111`
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
                                 'for field `view_factor_111`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_111`')

        self._data["View Factor 111"] = value

    @property
    def from_surface_112(self):
        """Get from_surface_112

        Returns:
            str: the value of `from_surface_112` or None if not set
        """
        return self._data["From Surface 112"]

    @from_surface_112.setter
    def from_surface_112(self, value=None):
        """  Corresponds to IDD Field `from_surface_112`

        Args:
            value (str): value for IDD Field `from_surface_112`
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
                                 'for field `from_surface_112`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_112`')

        self._data["From Surface 112"] = value

    @property
    def to_surface_112(self):
        """Get to_surface_112

        Returns:
            str: the value of `to_surface_112` or None if not set
        """
        return self._data["To Surface 112"]

    @to_surface_112.setter
    def to_surface_112(self, value=None):
        """  Corresponds to IDD Field `to_surface_112`

        Args:
            value (str): value for IDD Field `to_surface_112`
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
                                 'for field `to_surface_112`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_112`')

        self._data["To Surface 112"] = value

    @property
    def view_factor_112(self):
        """Get view_factor_112

        Returns:
            float: the value of `view_factor_112` or None if not set
        """
        return self._data["View Factor 112"]

    @view_factor_112.setter
    def view_factor_112(self, value=None):
        """  Corresponds to IDD Field `view_factor_112`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_112`
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
                                 'for field `view_factor_112`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_112`')

        self._data["View Factor 112"] = value

    @property
    def from_surface_113(self):
        """Get from_surface_113

        Returns:
            str: the value of `from_surface_113` or None if not set
        """
        return self._data["From Surface 113"]

    @from_surface_113.setter
    def from_surface_113(self, value=None):
        """  Corresponds to IDD Field `from_surface_113`

        Args:
            value (str): value for IDD Field `from_surface_113`
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
                                 'for field `from_surface_113`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_113`')

        self._data["From Surface 113"] = value

    @property
    def to_surface_113(self):
        """Get to_surface_113

        Returns:
            str: the value of `to_surface_113` or None if not set
        """
        return self._data["To Surface 113"]

    @to_surface_113.setter
    def to_surface_113(self, value=None):
        """  Corresponds to IDD Field `to_surface_113`

        Args:
            value (str): value for IDD Field `to_surface_113`
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
                                 'for field `to_surface_113`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_113`')

        self._data["To Surface 113"] = value

    @property
    def view_factor_113(self):
        """Get view_factor_113

        Returns:
            float: the value of `view_factor_113` or None if not set
        """
        return self._data["View Factor 113"]

    @view_factor_113.setter
    def view_factor_113(self, value=None):
        """  Corresponds to IDD Field `view_factor_113`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_113`
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
                                 'for field `view_factor_113`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_113`')

        self._data["View Factor 113"] = value

    @property
    def from_surface_114(self):
        """Get from_surface_114

        Returns:
            str: the value of `from_surface_114` or None if not set
        """
        return self._data["From Surface 114"]

    @from_surface_114.setter
    def from_surface_114(self, value=None):
        """  Corresponds to IDD Field `from_surface_114`

        Args:
            value (str): value for IDD Field `from_surface_114`
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
                                 'for field `from_surface_114`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_114`')

        self._data["From Surface 114"] = value

    @property
    def to_surface_114(self):
        """Get to_surface_114

        Returns:
            str: the value of `to_surface_114` or None if not set
        """
        return self._data["To Surface 114"]

    @to_surface_114.setter
    def to_surface_114(self, value=None):
        """  Corresponds to IDD Field `to_surface_114`

        Args:
            value (str): value for IDD Field `to_surface_114`
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
                                 'for field `to_surface_114`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_114`')

        self._data["To Surface 114"] = value

    @property
    def view_factor_114(self):
        """Get view_factor_114

        Returns:
            float: the value of `view_factor_114` or None if not set
        """
        return self._data["View Factor 114"]

    @view_factor_114.setter
    def view_factor_114(self, value=None):
        """  Corresponds to IDD Field `view_factor_114`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_114`
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
                                 'for field `view_factor_114`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_114`')

        self._data["View Factor 114"] = value

    @property
    def from_surface_115(self):
        """Get from_surface_115

        Returns:
            str: the value of `from_surface_115` or None if not set
        """
        return self._data["From Surface 115"]

    @from_surface_115.setter
    def from_surface_115(self, value=None):
        """  Corresponds to IDD Field `from_surface_115`

        Args:
            value (str): value for IDD Field `from_surface_115`
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
                                 'for field `from_surface_115`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_115`')

        self._data["From Surface 115"] = value

    @property
    def to_surface_115(self):
        """Get to_surface_115

        Returns:
            str: the value of `to_surface_115` or None if not set
        """
        return self._data["To Surface 115"]

    @to_surface_115.setter
    def to_surface_115(self, value=None):
        """  Corresponds to IDD Field `to_surface_115`

        Args:
            value (str): value for IDD Field `to_surface_115`
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
                                 'for field `to_surface_115`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_115`')

        self._data["To Surface 115"] = value

    @property
    def view_factor_115(self):
        """Get view_factor_115

        Returns:
            float: the value of `view_factor_115` or None if not set
        """
        return self._data["View Factor 115"]

    @view_factor_115.setter
    def view_factor_115(self, value=None):
        """  Corresponds to IDD Field `view_factor_115`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_115`
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
                                 'for field `view_factor_115`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_115`')

        self._data["View Factor 115"] = value

    @property
    def from_surface_116(self):
        """Get from_surface_116

        Returns:
            str: the value of `from_surface_116` or None if not set
        """
        return self._data["From Surface 116"]

    @from_surface_116.setter
    def from_surface_116(self, value=None):
        """  Corresponds to IDD Field `from_surface_116`

        Args:
            value (str): value for IDD Field `from_surface_116`
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
                                 'for field `from_surface_116`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_116`')

        self._data["From Surface 116"] = value

    @property
    def to_surface_116(self):
        """Get to_surface_116

        Returns:
            str: the value of `to_surface_116` or None if not set
        """
        return self._data["To Surface 116"]

    @to_surface_116.setter
    def to_surface_116(self, value=None):
        """  Corresponds to IDD Field `to_surface_116`

        Args:
            value (str): value for IDD Field `to_surface_116`
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
                                 'for field `to_surface_116`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_116`')

        self._data["To Surface 116"] = value

    @property
    def view_factor_116(self):
        """Get view_factor_116

        Returns:
            float: the value of `view_factor_116` or None if not set
        """
        return self._data["View Factor 116"]

    @view_factor_116.setter
    def view_factor_116(self, value=None):
        """  Corresponds to IDD Field `view_factor_116`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_116`
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
                                 'for field `view_factor_116`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_116`')

        self._data["View Factor 116"] = value

    @property
    def from_surface_117(self):
        """Get from_surface_117

        Returns:
            str: the value of `from_surface_117` or None if not set
        """
        return self._data["From Surface 117"]

    @from_surface_117.setter
    def from_surface_117(self, value=None):
        """  Corresponds to IDD Field `from_surface_117`

        Args:
            value (str): value for IDD Field `from_surface_117`
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
                                 'for field `from_surface_117`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_117`')

        self._data["From Surface 117"] = value

    @property
    def to_surface_117(self):
        """Get to_surface_117

        Returns:
            str: the value of `to_surface_117` or None if not set
        """
        return self._data["To Surface 117"]

    @to_surface_117.setter
    def to_surface_117(self, value=None):
        """  Corresponds to IDD Field `to_surface_117`

        Args:
            value (str): value for IDD Field `to_surface_117`
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
                                 'for field `to_surface_117`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_117`')

        self._data["To Surface 117"] = value

    @property
    def view_factor_117(self):
        """Get view_factor_117

        Returns:
            float: the value of `view_factor_117` or None if not set
        """
        return self._data["View Factor 117"]

    @view_factor_117.setter
    def view_factor_117(self, value=None):
        """  Corresponds to IDD Field `view_factor_117`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_117`
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
                                 'for field `view_factor_117`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_117`')

        self._data["View Factor 117"] = value

    @property
    def from_surface_118(self):
        """Get from_surface_118

        Returns:
            str: the value of `from_surface_118` or None if not set
        """
        return self._data["From Surface 118"]

    @from_surface_118.setter
    def from_surface_118(self, value=None):
        """  Corresponds to IDD Field `from_surface_118`

        Args:
            value (str): value for IDD Field `from_surface_118`
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
                                 'for field `from_surface_118`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_118`')

        self._data["From Surface 118"] = value

    @property
    def to_surface_118(self):
        """Get to_surface_118

        Returns:
            str: the value of `to_surface_118` or None if not set
        """
        return self._data["To Surface 118"]

    @to_surface_118.setter
    def to_surface_118(self, value=None):
        """  Corresponds to IDD Field `to_surface_118`

        Args:
            value (str): value for IDD Field `to_surface_118`
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
                                 'for field `to_surface_118`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_118`')

        self._data["To Surface 118"] = value

    @property
    def view_factor_118(self):
        """Get view_factor_118

        Returns:
            float: the value of `view_factor_118` or None if not set
        """
        return self._data["View Factor 118"]

    @view_factor_118.setter
    def view_factor_118(self, value=None):
        """  Corresponds to IDD Field `view_factor_118`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_118`
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
                                 'for field `view_factor_118`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_118`')

        self._data["View Factor 118"] = value

    @property
    def from_surface_119(self):
        """Get from_surface_119

        Returns:
            str: the value of `from_surface_119` or None if not set
        """
        return self._data["From Surface 119"]

    @from_surface_119.setter
    def from_surface_119(self, value=None):
        """  Corresponds to IDD Field `from_surface_119`

        Args:
            value (str): value for IDD Field `from_surface_119`
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
                                 'for field `from_surface_119`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_119`')

        self._data["From Surface 119"] = value

    @property
    def to_surface_119(self):
        """Get to_surface_119

        Returns:
            str: the value of `to_surface_119` or None if not set
        """
        return self._data["To Surface 119"]

    @to_surface_119.setter
    def to_surface_119(self, value=None):
        """  Corresponds to IDD Field `to_surface_119`

        Args:
            value (str): value for IDD Field `to_surface_119`
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
                                 'for field `to_surface_119`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_119`')

        self._data["To Surface 119"] = value

    @property
    def view_factor_119(self):
        """Get view_factor_119

        Returns:
            float: the value of `view_factor_119` or None if not set
        """
        return self._data["View Factor 119"]

    @view_factor_119.setter
    def view_factor_119(self, value=None):
        """  Corresponds to IDD Field `view_factor_119`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_119`
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
                                 'for field `view_factor_119`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_119`')

        self._data["View Factor 119"] = value

    @property
    def from_surface_120(self):
        """Get from_surface_120

        Returns:
            str: the value of `from_surface_120` or None if not set
        """
        return self._data["From Surface 120"]

    @from_surface_120.setter
    def from_surface_120(self, value=None):
        """  Corresponds to IDD Field `from_surface_120`

        Args:
            value (str): value for IDD Field `from_surface_120`
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
                                 'for field `from_surface_120`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_120`')

        self._data["From Surface 120"] = value

    @property
    def to_surface_120(self):
        """Get to_surface_120

        Returns:
            str: the value of `to_surface_120` or None if not set
        """
        return self._data["To Surface 120"]

    @to_surface_120.setter
    def to_surface_120(self, value=None):
        """  Corresponds to IDD Field `to_surface_120`

        Args:
            value (str): value for IDD Field `to_surface_120`
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
                                 'for field `to_surface_120`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_120`')

        self._data["To Surface 120"] = value

    @property
    def view_factor_120(self):
        """Get view_factor_120

        Returns:
            float: the value of `view_factor_120` or None if not set
        """
        return self._data["View Factor 120"]

    @view_factor_120.setter
    def view_factor_120(self, value=None):
        """  Corresponds to IDD Field `view_factor_120`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_120`
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
                                 'for field `view_factor_120`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_120`')

        self._data["View Factor 120"] = value

    @property
    def from_surface_121(self):
        """Get from_surface_121

        Returns:
            str: the value of `from_surface_121` or None if not set
        """
        return self._data["From Surface 121"]

    @from_surface_121.setter
    def from_surface_121(self, value=None):
        """  Corresponds to IDD Field `from_surface_121`

        Args:
            value (str): value for IDD Field `from_surface_121`
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
                                 'for field `from_surface_121`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `from_surface_121`')

        self._data["From Surface 121"] = value

    @property
    def to_surface_121(self):
        """Get to_surface_121

        Returns:
            str: the value of `to_surface_121` or None if not set
        """
        return self._data["To Surface 121"]

    @to_surface_121.setter
    def to_surface_121(self, value=None):
        """  Corresponds to IDD Field `to_surface_121`

        Args:
            value (str): value for IDD Field `to_surface_121`
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
                                 'for field `to_surface_121`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `to_surface_121`')

        self._data["To Surface 121"] = value

    @property
    def view_factor_121(self):
        """Get view_factor_121

        Returns:
            float: the value of `view_factor_121` or None if not set
        """
        return self._data["View Factor 121"]

    @view_factor_121.setter
    def view_factor_121(self, value=None):
        """  Corresponds to IDD Field `view_factor_121`
        This value is the view factor value From Surface => To Surface

        Args:
            value (float): value for IDD Field `view_factor_121`
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
                                 'for field `view_factor_121`'.format(value))
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_121`')

        self._data["View Factor 121"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.from_surface_1))
        out.append(self._to_str(self.to_surface_1))
        out.append(self._to_str(self.view_factor_1))
        out.append(self._to_str(self.from_surface_2))
        out.append(self._to_str(self.to_surface_2))
        out.append(self._to_str(self.view_factor_2))
        out.append(self._to_str(self.from_surface_3))
        out.append(self._to_str(self.to_surface_3))
        out.append(self._to_str(self.view_factor_3))
        out.append(self._to_str(self.from_surface_4))
        out.append(self._to_str(self.to_surface_4))
        out.append(self._to_str(self.view_factor_4))
        out.append(self._to_str(self.from_surface_5))
        out.append(self._to_str(self.to_surface_5))
        out.append(self._to_str(self.view_factor_5))
        out.append(self._to_str(self.from_surface_6))
        out.append(self._to_str(self.to_surface_6))
        out.append(self._to_str(self.view_factor_6))
        out.append(self._to_str(self.from_surface_7))
        out.append(self._to_str(self.to_surface_7))
        out.append(self._to_str(self.view_factor_7))
        out.append(self._to_str(self.from_surface_8))
        out.append(self._to_str(self.to_surface_8))
        out.append(self._to_str(self.view_factor_8))
        out.append(self._to_str(self.from_surface_9))
        out.append(self._to_str(self.to_surface_9))
        out.append(self._to_str(self.view_factor_9))
        out.append(self._to_str(self.from_surface_10))
        out.append(self._to_str(self.to_surface_10))
        out.append(self._to_str(self.view_factor_10))
        out.append(self._to_str(self.from_surface_11))
        out.append(self._to_str(self.to_surface_11))
        out.append(self._to_str(self.view_factor_11))
        out.append(self._to_str(self.from_surface_12))
        out.append(self._to_str(self.to_surface_12))
        out.append(self._to_str(self.view_factor_12))
        out.append(self._to_str(self.from_surface_13))
        out.append(self._to_str(self.to_surface_13))
        out.append(self._to_str(self.view_factor_13))
        out.append(self._to_str(self.from_surface_14))
        out.append(self._to_str(self.to_surface_14))
        out.append(self._to_str(self.view_factor_14))
        out.append(self._to_str(self.from_surface_15))
        out.append(self._to_str(self.to_surface_15))
        out.append(self._to_str(self.view_factor_15))
        out.append(self._to_str(self.from_surface_16))
        out.append(self._to_str(self.to_surface_16))
        out.append(self._to_str(self.view_factor_16))
        out.append(self._to_str(self.from_surface_17))
        out.append(self._to_str(self.to_surface_17))
        out.append(self._to_str(self.view_factor_17))
        out.append(self._to_str(self.from_surface_18))
        out.append(self._to_str(self.to_surface_18))
        out.append(self._to_str(self.view_factor_18))
        out.append(self._to_str(self.from_surface_19))
        out.append(self._to_str(self.to_surface_19))
        out.append(self._to_str(self.view_factor_19))
        out.append(self._to_str(self.from_surface_20))
        out.append(self._to_str(self.to_surface_20))
        out.append(self._to_str(self.view_factor_20))
        out.append(self._to_str(self.from_surface_21))
        out.append(self._to_str(self.to_surface_21))
        out.append(self._to_str(self.view_factor_21))
        out.append(self._to_str(self.from_surface_22))
        out.append(self._to_str(self.to_surface_22))
        out.append(self._to_str(self.view_factor_22))
        out.append(self._to_str(self.from_surface_23))
        out.append(self._to_str(self.to_surface_23))
        out.append(self._to_str(self.view_factor_23))
        out.append(self._to_str(self.from_surface_24))
        out.append(self._to_str(self.to_surface_24))
        out.append(self._to_str(self.view_factor_24))
        out.append(self._to_str(self.from_surface_25))
        out.append(self._to_str(self.to_surface_25))
        out.append(self._to_str(self.view_factor_25))
        out.append(self._to_str(self.from_surface_26))
        out.append(self._to_str(self.to_surface_26))
        out.append(self._to_str(self.view_factor_26))
        out.append(self._to_str(self.from_surface_27))
        out.append(self._to_str(self.to_surface_27))
        out.append(self._to_str(self.view_factor_27))
        out.append(self._to_str(self.from_surface_28))
        out.append(self._to_str(self.to_surface_28))
        out.append(self._to_str(self.view_factor_28))
        out.append(self._to_str(self.from_surface_29))
        out.append(self._to_str(self.to_surface_29))
        out.append(self._to_str(self.view_factor_29))
        out.append(self._to_str(self.from_surface_30))
        out.append(self._to_str(self.to_surface_30))
        out.append(self._to_str(self.view_factor_30))
        out.append(self._to_str(self.from_surface_31))
        out.append(self._to_str(self.to_surface_31))
        out.append(self._to_str(self.view_factor_31))
        out.append(self._to_str(self.from_surface_32))
        out.append(self._to_str(self.to_surface_32))
        out.append(self._to_str(self.view_factor_32))
        out.append(self._to_str(self.from_surface_33))
        out.append(self._to_str(self.to_surface_33))
        out.append(self._to_str(self.view_factor_33))
        out.append(self._to_str(self.from_surface_34))
        out.append(self._to_str(self.to_surface_34))
        out.append(self._to_str(self.view_factor_34))
        out.append(self._to_str(self.from_surface_35))
        out.append(self._to_str(self.to_surface_35))
        out.append(self._to_str(self.view_factor_35))
        out.append(self._to_str(self.from_surface_36))
        out.append(self._to_str(self.to_surface_36))
        out.append(self._to_str(self.view_factor_36))
        out.append(self._to_str(self.from_surface_37))
        out.append(self._to_str(self.to_surface_37))
        out.append(self._to_str(self.view_factor_37))
        out.append(self._to_str(self.from_surface_38))
        out.append(self._to_str(self.to_surface_38))
        out.append(self._to_str(self.view_factor_38))
        out.append(self._to_str(self.from_surface_39))
        out.append(self._to_str(self.to_surface_39))
        out.append(self._to_str(self.view_factor_39))
        out.append(self._to_str(self.from_surface_40))
        out.append(self._to_str(self.to_surface_40))
        out.append(self._to_str(self.view_factor_40))
        out.append(self._to_str(self.from_surface_41))
        out.append(self._to_str(self.to_surface_41))
        out.append(self._to_str(self.view_factor_41))
        out.append(self._to_str(self.from_surface_42))
        out.append(self._to_str(self.to_surface_42))
        out.append(self._to_str(self.view_factor_42))
        out.append(self._to_str(self.from_surface_43))
        out.append(self._to_str(self.to_surface_43))
        out.append(self._to_str(self.view_factor_43))
        out.append(self._to_str(self.from_surface_44))
        out.append(self._to_str(self.to_surface_44))
        out.append(self._to_str(self.view_factor_44))
        out.append(self._to_str(self.from_surface_45))
        out.append(self._to_str(self.to_surface_45))
        out.append(self._to_str(self.view_factor_45))
        out.append(self._to_str(self.from_surface_46))
        out.append(self._to_str(self.to_surface_46))
        out.append(self._to_str(self.view_factor_46))
        out.append(self._to_str(self.from_surface_47))
        out.append(self._to_str(self.to_surface_47))
        out.append(self._to_str(self.view_factor_47))
        out.append(self._to_str(self.from_surface_48))
        out.append(self._to_str(self.to_surface_48))
        out.append(self._to_str(self.view_factor_48))
        out.append(self._to_str(self.from_surface_49))
        out.append(self._to_str(self.to_surface_49))
        out.append(self._to_str(self.view_factor_49))
        out.append(self._to_str(self.from_surface_50))
        out.append(self._to_str(self.to_surface_50))
        out.append(self._to_str(self.view_factor_50))
        out.append(self._to_str(self.from_surface_51))
        out.append(self._to_str(self.to_surface_51))
        out.append(self._to_str(self.view_factor_51))
        out.append(self._to_str(self.from_surface_52))
        out.append(self._to_str(self.to_surface_52))
        out.append(self._to_str(self.view_factor_52))
        out.append(self._to_str(self.from_surface_53))
        out.append(self._to_str(self.to_surface_53))
        out.append(self._to_str(self.view_factor_53))
        out.append(self._to_str(self.from_surface_54))
        out.append(self._to_str(self.to_surface_54))
        out.append(self._to_str(self.view_factor_54))
        out.append(self._to_str(self.from_surface_55))
        out.append(self._to_str(self.to_surface_55))
        out.append(self._to_str(self.view_factor_55))
        out.append(self._to_str(self.from_surface_56))
        out.append(self._to_str(self.to_surface_56))
        out.append(self._to_str(self.view_factor_56))
        out.append(self._to_str(self.from_surface_57))
        out.append(self._to_str(self.to_surface_57))
        out.append(self._to_str(self.view_factor_57))
        out.append(self._to_str(self.from_surface_58))
        out.append(self._to_str(self.to_surface_58))
        out.append(self._to_str(self.view_factor_58))
        out.append(self._to_str(self.from_surface_59))
        out.append(self._to_str(self.to_surface_59))
        out.append(self._to_str(self.view_factor_59))
        out.append(self._to_str(self.from_surface_60))
        out.append(self._to_str(self.to_surface_60))
        out.append(self._to_str(self.view_factor_60))
        out.append(self._to_str(self.from_surface_61))
        out.append(self._to_str(self.to_surface_61))
        out.append(self._to_str(self.view_factor_61))
        out.append(self._to_str(self.from_surface_62))
        out.append(self._to_str(self.to_surface_62))
        out.append(self._to_str(self.view_factor_62))
        out.append(self._to_str(self.from_surface_63))
        out.append(self._to_str(self.to_surface_63))
        out.append(self._to_str(self.view_factor_63))
        out.append(self._to_str(self.from_surface_64))
        out.append(self._to_str(self.to_surface_64))
        out.append(self._to_str(self.view_factor_64))
        out.append(self._to_str(self.from_surface_65))
        out.append(self._to_str(self.to_surface_65))
        out.append(self._to_str(self.view_factor_65))
        out.append(self._to_str(self.from_surface_66))
        out.append(self._to_str(self.to_surface_66))
        out.append(self._to_str(self.view_factor_66))
        out.append(self._to_str(self.from_surface_67))
        out.append(self._to_str(self.to_surface_67))
        out.append(self._to_str(self.view_factor_67))
        out.append(self._to_str(self.from_surface_68))
        out.append(self._to_str(self.to_surface_68))
        out.append(self._to_str(self.view_factor_68))
        out.append(self._to_str(self.from_surface_69))
        out.append(self._to_str(self.to_surface_69))
        out.append(self._to_str(self.view_factor_69))
        out.append(self._to_str(self.from_surface_70))
        out.append(self._to_str(self.to_surface_70))
        out.append(self._to_str(self.view_factor_70))
        out.append(self._to_str(self.from_surface_71))
        out.append(self._to_str(self.to_surface_71))
        out.append(self._to_str(self.view_factor_71))
        out.append(self._to_str(self.from_surface_72))
        out.append(self._to_str(self.to_surface_72))
        out.append(self._to_str(self.view_factor_72))
        out.append(self._to_str(self.from_surface_73))
        out.append(self._to_str(self.to_surface_73))
        out.append(self._to_str(self.view_factor_73))
        out.append(self._to_str(self.from_surface_74))
        out.append(self._to_str(self.to_surface_74))
        out.append(self._to_str(self.view_factor_74))
        out.append(self._to_str(self.from_surface_75))
        out.append(self._to_str(self.to_surface_75))
        out.append(self._to_str(self.view_factor_75))
        out.append(self._to_str(self.from_surface_76))
        out.append(self._to_str(self.to_surface_76))
        out.append(self._to_str(self.view_factor_76))
        out.append(self._to_str(self.from_surface_77))
        out.append(self._to_str(self.to_surface_77))
        out.append(self._to_str(self.view_factor_77))
        out.append(self._to_str(self.from_surface_78))
        out.append(self._to_str(self.to_surface_78))
        out.append(self._to_str(self.view_factor_78))
        out.append(self._to_str(self.from_surface_79))
        out.append(self._to_str(self.to_surface_79))
        out.append(self._to_str(self.view_factor_79))
        out.append(self._to_str(self.from_surface_80))
        out.append(self._to_str(self.to_surface_80))
        out.append(self._to_str(self.view_factor_80))
        out.append(self._to_str(self.from_surface_81))
        out.append(self._to_str(self.to_surface_81))
        out.append(self._to_str(self.view_factor_81))
        out.append(self._to_str(self.from_surface_82))
        out.append(self._to_str(self.to_surface_82))
        out.append(self._to_str(self.view_factor_82))
        out.append(self._to_str(self.from_surface_83))
        out.append(self._to_str(self.to_surface_83))
        out.append(self._to_str(self.view_factor_83))
        out.append(self._to_str(self.from_surface_84))
        out.append(self._to_str(self.to_surface_84))
        out.append(self._to_str(self.view_factor_84))
        out.append(self._to_str(self.from_surface_85))
        out.append(self._to_str(self.to_surface_85))
        out.append(self._to_str(self.view_factor_85))
        out.append(self._to_str(self.from_surface_86))
        out.append(self._to_str(self.to_surface_86))
        out.append(self._to_str(self.view_factor_86))
        out.append(self._to_str(self.from_surface_87))
        out.append(self._to_str(self.to_surface_87))
        out.append(self._to_str(self.view_factor_87))
        out.append(self._to_str(self.from_surface_88))
        out.append(self._to_str(self.to_surface_88))
        out.append(self._to_str(self.view_factor_88))
        out.append(self._to_str(self.from_surface_89))
        out.append(self._to_str(self.to_surface_89))
        out.append(self._to_str(self.view_factor_89))
        out.append(self._to_str(self.from_surface_90))
        out.append(self._to_str(self.to_surface_90))
        out.append(self._to_str(self.view_factor_90))
        out.append(self._to_str(self.from_surface_91))
        out.append(self._to_str(self.to_surface_91))
        out.append(self._to_str(self.view_factor_91))
        out.append(self._to_str(self.from_surface_92))
        out.append(self._to_str(self.to_surface_92))
        out.append(self._to_str(self.view_factor_92))
        out.append(self._to_str(self.from_surface_93))
        out.append(self._to_str(self.to_surface_93))
        out.append(self._to_str(self.view_factor_93))
        out.append(self._to_str(self.from_surface_94))
        out.append(self._to_str(self.to_surface_94))
        out.append(self._to_str(self.view_factor_94))
        out.append(self._to_str(self.from_surface_95))
        out.append(self._to_str(self.to_surface_95))
        out.append(self._to_str(self.view_factor_95))
        out.append(self._to_str(self.from_surface_96))
        out.append(self._to_str(self.to_surface_96))
        out.append(self._to_str(self.view_factor_96))
        out.append(self._to_str(self.from_surface_97))
        out.append(self._to_str(self.to_surface_97))
        out.append(self._to_str(self.view_factor_97))
        out.append(self._to_str(self.from_surface_98))
        out.append(self._to_str(self.to_surface_98))
        out.append(self._to_str(self.view_factor_98))
        out.append(self._to_str(self.from_surface_99))
        out.append(self._to_str(self.to_surface_99))
        out.append(self._to_str(self.view_factor_99))
        out.append(self._to_str(self.from_surface_100))
        out.append(self._to_str(self.to_surface_100))
        out.append(self._to_str(self.view_factor_100))
        out.append(self._to_str(self.from_surface_101))
        out.append(self._to_str(self.to_surface_101))
        out.append(self._to_str(self.view_factor_101))
        out.append(self._to_str(self.from_surface_102))
        out.append(self._to_str(self.to_surface_102))
        out.append(self._to_str(self.view_factor_102))
        out.append(self._to_str(self.from_surface_103))
        out.append(self._to_str(self.to_surface_103))
        out.append(self._to_str(self.view_factor_103))
        out.append(self._to_str(self.from_surface_104))
        out.append(self._to_str(self.to_surface_104))
        out.append(self._to_str(self.view_factor_104))
        out.append(self._to_str(self.from_surface_105))
        out.append(self._to_str(self.to_surface_105))
        out.append(self._to_str(self.view_factor_105))
        out.append(self._to_str(self.from_surface_106))
        out.append(self._to_str(self.to_surface_106))
        out.append(self._to_str(self.view_factor_106))
        out.append(self._to_str(self.from_surface_107))
        out.append(self._to_str(self.to_surface_107))
        out.append(self._to_str(self.view_factor_107))
        out.append(self._to_str(self.from_surface_108))
        out.append(self._to_str(self.to_surface_108))
        out.append(self._to_str(self.view_factor_108))
        out.append(self._to_str(self.from_surface_109))
        out.append(self._to_str(self.to_surface_109))
        out.append(self._to_str(self.view_factor_109))
        out.append(self._to_str(self.from_surface_110))
        out.append(self._to_str(self.to_surface_110))
        out.append(self._to_str(self.view_factor_110))
        out.append(self._to_str(self.from_surface_111))
        out.append(self._to_str(self.to_surface_111))
        out.append(self._to_str(self.view_factor_111))
        out.append(self._to_str(self.from_surface_112))
        out.append(self._to_str(self.to_surface_112))
        out.append(self._to_str(self.view_factor_112))
        out.append(self._to_str(self.from_surface_113))
        out.append(self._to_str(self.to_surface_113))
        out.append(self._to_str(self.view_factor_113))
        out.append(self._to_str(self.from_surface_114))
        out.append(self._to_str(self.to_surface_114))
        out.append(self._to_str(self.view_factor_114))
        out.append(self._to_str(self.from_surface_115))
        out.append(self._to_str(self.to_surface_115))
        out.append(self._to_str(self.view_factor_115))
        out.append(self._to_str(self.from_surface_116))
        out.append(self._to_str(self.to_surface_116))
        out.append(self._to_str(self.view_factor_116))
        out.append(self._to_str(self.from_surface_117))
        out.append(self._to_str(self.to_surface_117))
        out.append(self._to_str(self.view_factor_117))
        out.append(self._to_str(self.from_surface_118))
        out.append(self._to_str(self.to_surface_118))
        out.append(self._to_str(self.view_factor_118))
        out.append(self._to_str(self.from_surface_119))
        out.append(self._to_str(self.to_surface_119))
        out.append(self._to_str(self.view_factor_119))
        out.append(self._to_str(self.from_surface_120))
        out.append(self._to_str(self.to_surface_120))
        out.append(self._to_str(self.view_factor_120))
        out.append(self._to_str(self.from_surface_121))
        out.append(self._to_str(self.to_surface_121))
        out.append(self._to_str(self.view_factor_121))
        return ",".join(out)