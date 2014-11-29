from collections import OrderedDict

class OutputControlIlluminanceMapStyle(object):
    """ Corresponds to IDD object `OutputControl:IlluminanceMap:Style`
        default style for the Daylighting Illuminance Map is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns"
    """
    internal_name = "OutputControl:IlluminanceMap:Style"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutputControl:IlluminanceMap:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `column_separator`

        Args:
            value (str): value for IDD Field `column_separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                Default value: Comma
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `column_separator`')
            vals = set()
            vals.add("Comma")
            vals.add("Tab")
            vals.add("Fixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `column_separator`'.format(value))

        self._data["Column Separator"] = value

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
        out.append(self._to_str(self.column_separator))
        return ",".join(out)

class OutputControlSizingStyle(object):
    """ Corresponds to IDD object `OutputControl:Sizing:Style`
        default style for the Sizing output files is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns"
    """
    internal_name = "OutputControl:Sizing:Style"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutputControl:Sizing:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value=None):
        """  Corresponds to IDD Field `column_separator`

        Args:
            value (str): value for IDD Field `column_separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `column_separator`')
            vals = set()
            vals.add("Comma")
            vals.add("Tab")
            vals.add("Fixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `column_separator`'.format(value))

        self._data["Column Separator"] = value

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
        out.append(self._to_str(self.column_separator))
        return ",".join(out)

class OutputControlSurfaceColorScheme(object):
    """ Corresponds to IDD object `OutputControl:SurfaceColorScheme`
        This object is used to set colors for reporting on various building elements particularly for the
        DXF reports.  We know the user can enter 0 to 255 and the color map is available in DXF output.
        Therefore, we are limiting the colors in that range.  You can
        extend by editing the IDD but you do so on your own.  Colors not changed in any scheme will
        remain as the default scheme uses.
    """
    internal_name = "OutputControl:SurfaceColorScheme"
    field_count = 31

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutputControl:SurfaceColorScheme`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Drawing Element 1 Type"] = None
        self._data["Color for Drawing Element 1"] = None
        self._data["Drawing Element 2 Type"] = None
        self._data["Color for Drawing Element 2"] = None
        self._data["Drawing Element 3 Type"] = None
        self._data["Color for Drawing Element 3"] = None
        self._data["Drawing Element 4 Type"] = None
        self._data["Color for Drawing Element 4"] = None
        self._data["Drawing Element 5 Type"] = None
        self._data["Color for Drawing Element 5"] = None
        self._data["Drawing Element 6 Type"] = None
        self._data["Color for Drawing Element 6"] = None
        self._data["Drawing Element 7 Type"] = None
        self._data["Color for Drawing Element 7"] = None
        self._data["Drawing Element 8 Type"] = None
        self._data["Color for Drawing Element 8"] = None
        self._data["Drawing Element 9 Type"] = None
        self._data["Color for Drawing Element 9"] = None
        self._data["Drawing Element 10 Type"] = None
        self._data["Color for Drawing Element 10"] = None
        self._data["Drawing Element 11 Type"] = None
        self._data["Color for Drawing Element 11"] = None
        self._data["Drawing Element 12 Type"] = None
        self._data["Color for Drawing Element 12"] = None
        self._data["Drawing Element 13 Type"] = None
        self._data["Color for Drawing Element 13"] = None
        self._data["Drawing Element 14 Type"] = None
        self._data["Color for Drawing Element 14"] = None
        self._data["Drawing Element 15 Type"] = None
        self._data["Color for Drawing Element 15"] = None

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
            self.drawing_element_1_type = None
        else:
            self.drawing_element_1_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_1 = None
        else:
            self.color_for_drawing_element_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_2_type = None
        else:
            self.drawing_element_2_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_2 = None
        else:
            self.color_for_drawing_element_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_3_type = None
        else:
            self.drawing_element_3_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_3 = None
        else:
            self.color_for_drawing_element_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_4_type = None
        else:
            self.drawing_element_4_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_4 = None
        else:
            self.color_for_drawing_element_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_5_type = None
        else:
            self.drawing_element_5_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_5 = None
        else:
            self.color_for_drawing_element_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_6_type = None
        else:
            self.drawing_element_6_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_6 = None
        else:
            self.color_for_drawing_element_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_7_type = None
        else:
            self.drawing_element_7_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_7 = None
        else:
            self.color_for_drawing_element_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_8_type = None
        else:
            self.drawing_element_8_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_8 = None
        else:
            self.color_for_drawing_element_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_9_type = None
        else:
            self.drawing_element_9_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_9 = None
        else:
            self.color_for_drawing_element_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_10_type = None
        else:
            self.drawing_element_10_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_10 = None
        else:
            self.color_for_drawing_element_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_11_type = None
        else:
            self.drawing_element_11_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_11 = None
        else:
            self.color_for_drawing_element_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_12_type = None
        else:
            self.drawing_element_12_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_12 = None
        else:
            self.color_for_drawing_element_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_13_type = None
        else:
            self.drawing_element_13_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_13 = None
        else:
            self.color_for_drawing_element_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_14_type = None
        else:
            self.drawing_element_14_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_14 = None
        else:
            self.color_for_drawing_element_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.drawing_element_15_type = None
        else:
            self.drawing_element_15_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.color_for_drawing_element_15 = None
        else:
            self.color_for_drawing_element_15 = vals[i]
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
        choose a name or use one of the DataSets

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
    def drawing_element_1_type(self):
        """Get drawing_element_1_type

        Returns:
            str: the value of `drawing_element_1_type` or None if not set
        """
        return self._data["Drawing Element 1 Type"]

    @drawing_element_1_type.setter
    def drawing_element_1_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_1_type`

        Args:
            value (str): value for IDD Field `drawing_element_1_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_1_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_1_type`'.format(value))

        self._data["Drawing Element 1 Type"] = value

    @property
    def color_for_drawing_element_1(self):
        """Get color_for_drawing_element_1

        Returns:
            int: the value of `color_for_drawing_element_1` or None if not set
        """
        return self._data["Color for Drawing Element 1"]

    @color_for_drawing_element_1.setter
    def color_for_drawing_element_1(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_1`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_1`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_1`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_1`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_1`')

        self._data["Color for Drawing Element 1"] = value

    @property
    def drawing_element_2_type(self):
        """Get drawing_element_2_type

        Returns:
            str: the value of `drawing_element_2_type` or None if not set
        """
        return self._data["Drawing Element 2 Type"]

    @drawing_element_2_type.setter
    def drawing_element_2_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_2_type`

        Args:
            value (str): value for IDD Field `drawing_element_2_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_2_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_2_type`'.format(value))

        self._data["Drawing Element 2 Type"] = value

    @property
    def color_for_drawing_element_2(self):
        """Get color_for_drawing_element_2

        Returns:
            int: the value of `color_for_drawing_element_2` or None if not set
        """
        return self._data["Color for Drawing Element 2"]

    @color_for_drawing_element_2.setter
    def color_for_drawing_element_2(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_2`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_2`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_2`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_2`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_2`')

        self._data["Color for Drawing Element 2"] = value

    @property
    def drawing_element_3_type(self):
        """Get drawing_element_3_type

        Returns:
            str: the value of `drawing_element_3_type` or None if not set
        """
        return self._data["Drawing Element 3 Type"]

    @drawing_element_3_type.setter
    def drawing_element_3_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_3_type`

        Args:
            value (str): value for IDD Field `drawing_element_3_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_3_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_3_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_3_type`'.format(value))

        self._data["Drawing Element 3 Type"] = value

    @property
    def color_for_drawing_element_3(self):
        """Get color_for_drawing_element_3

        Returns:
            int: the value of `color_for_drawing_element_3` or None if not set
        """
        return self._data["Color for Drawing Element 3"]

    @color_for_drawing_element_3.setter
    def color_for_drawing_element_3(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_3`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_3`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_3`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_3`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_3`')

        self._data["Color for Drawing Element 3"] = value

    @property
    def drawing_element_4_type(self):
        """Get drawing_element_4_type

        Returns:
            str: the value of `drawing_element_4_type` or None if not set
        """
        return self._data["Drawing Element 4 Type"]

    @drawing_element_4_type.setter
    def drawing_element_4_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_4_type`

        Args:
            value (str): value for IDD Field `drawing_element_4_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_4_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_4_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_4_type`'.format(value))

        self._data["Drawing Element 4 Type"] = value

    @property
    def color_for_drawing_element_4(self):
        """Get color_for_drawing_element_4

        Returns:
            int: the value of `color_for_drawing_element_4` or None if not set
        """
        return self._data["Color for Drawing Element 4"]

    @color_for_drawing_element_4.setter
    def color_for_drawing_element_4(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_4`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_4`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_4`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_4`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_4`')

        self._data["Color for Drawing Element 4"] = value

    @property
    def drawing_element_5_type(self):
        """Get drawing_element_5_type

        Returns:
            str: the value of `drawing_element_5_type` or None if not set
        """
        return self._data["Drawing Element 5 Type"]

    @drawing_element_5_type.setter
    def drawing_element_5_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_5_type`

        Args:
            value (str): value for IDD Field `drawing_element_5_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_5_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_5_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_5_type`'.format(value))

        self._data["Drawing Element 5 Type"] = value

    @property
    def color_for_drawing_element_5(self):
        """Get color_for_drawing_element_5

        Returns:
            int: the value of `color_for_drawing_element_5` or None if not set
        """
        return self._data["Color for Drawing Element 5"]

    @color_for_drawing_element_5.setter
    def color_for_drawing_element_5(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_5`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_5`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_5`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_5`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_5`')

        self._data["Color for Drawing Element 5"] = value

    @property
    def drawing_element_6_type(self):
        """Get drawing_element_6_type

        Returns:
            str: the value of `drawing_element_6_type` or None if not set
        """
        return self._data["Drawing Element 6 Type"]

    @drawing_element_6_type.setter
    def drawing_element_6_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_6_type`

        Args:
            value (str): value for IDD Field `drawing_element_6_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_6_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_6_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_6_type`'.format(value))

        self._data["Drawing Element 6 Type"] = value

    @property
    def color_for_drawing_element_6(self):
        """Get color_for_drawing_element_6

        Returns:
            int: the value of `color_for_drawing_element_6` or None if not set
        """
        return self._data["Color for Drawing Element 6"]

    @color_for_drawing_element_6.setter
    def color_for_drawing_element_6(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_6`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_6`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_6`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_6`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_6`')

        self._data["Color for Drawing Element 6"] = value

    @property
    def drawing_element_7_type(self):
        """Get drawing_element_7_type

        Returns:
            str: the value of `drawing_element_7_type` or None if not set
        """
        return self._data["Drawing Element 7 Type"]

    @drawing_element_7_type.setter
    def drawing_element_7_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_7_type`

        Args:
            value (str): value for IDD Field `drawing_element_7_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_7_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_7_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_7_type`'.format(value))

        self._data["Drawing Element 7 Type"] = value

    @property
    def color_for_drawing_element_7(self):
        """Get color_for_drawing_element_7

        Returns:
            int: the value of `color_for_drawing_element_7` or None if not set
        """
        return self._data["Color for Drawing Element 7"]

    @color_for_drawing_element_7.setter
    def color_for_drawing_element_7(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_7`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_7`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_7`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_7`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_7`')

        self._data["Color for Drawing Element 7"] = value

    @property
    def drawing_element_8_type(self):
        """Get drawing_element_8_type

        Returns:
            str: the value of `drawing_element_8_type` or None if not set
        """
        return self._data["Drawing Element 8 Type"]

    @drawing_element_8_type.setter
    def drawing_element_8_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_8_type`

        Args:
            value (str): value for IDD Field `drawing_element_8_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_8_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_8_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_8_type`'.format(value))

        self._data["Drawing Element 8 Type"] = value

    @property
    def color_for_drawing_element_8(self):
        """Get color_for_drawing_element_8

        Returns:
            int: the value of `color_for_drawing_element_8` or None if not set
        """
        return self._data["Color for Drawing Element 8"]

    @color_for_drawing_element_8.setter
    def color_for_drawing_element_8(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_8`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_8`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_8`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_8`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_8`')

        self._data["Color for Drawing Element 8"] = value

    @property
    def drawing_element_9_type(self):
        """Get drawing_element_9_type

        Returns:
            str: the value of `drawing_element_9_type` or None if not set
        """
        return self._data["Drawing Element 9 Type"]

    @drawing_element_9_type.setter
    def drawing_element_9_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_9_type`

        Args:
            value (str): value for IDD Field `drawing_element_9_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_9_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_9_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_9_type`'.format(value))

        self._data["Drawing Element 9 Type"] = value

    @property
    def color_for_drawing_element_9(self):
        """Get color_for_drawing_element_9

        Returns:
            int: the value of `color_for_drawing_element_9` or None if not set
        """
        return self._data["Color for Drawing Element 9"]

    @color_for_drawing_element_9.setter
    def color_for_drawing_element_9(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_9`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_9`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_9`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_9`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_9`')

        self._data["Color for Drawing Element 9"] = value

    @property
    def drawing_element_10_type(self):
        """Get drawing_element_10_type

        Returns:
            str: the value of `drawing_element_10_type` or None if not set
        """
        return self._data["Drawing Element 10 Type"]

    @drawing_element_10_type.setter
    def drawing_element_10_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_10_type`

        Args:
            value (str): value for IDD Field `drawing_element_10_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_10_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_10_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_10_type`'.format(value))

        self._data["Drawing Element 10 Type"] = value

    @property
    def color_for_drawing_element_10(self):
        """Get color_for_drawing_element_10

        Returns:
            int: the value of `color_for_drawing_element_10` or None if not set
        """
        return self._data["Color for Drawing Element 10"]

    @color_for_drawing_element_10.setter
    def color_for_drawing_element_10(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_10`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_10`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_10`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_10`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_10`')

        self._data["Color for Drawing Element 10"] = value

    @property
    def drawing_element_11_type(self):
        """Get drawing_element_11_type

        Returns:
            str: the value of `drawing_element_11_type` or None if not set
        """
        return self._data["Drawing Element 11 Type"]

    @drawing_element_11_type.setter
    def drawing_element_11_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_11_type`

        Args:
            value (str): value for IDD Field `drawing_element_11_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_11_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_11_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_11_type`'.format(value))

        self._data["Drawing Element 11 Type"] = value

    @property
    def color_for_drawing_element_11(self):
        """Get color_for_drawing_element_11

        Returns:
            int: the value of `color_for_drawing_element_11` or None if not set
        """
        return self._data["Color for Drawing Element 11"]

    @color_for_drawing_element_11.setter
    def color_for_drawing_element_11(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_11`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_11`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_11`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_11`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_11`')

        self._data["Color for Drawing Element 11"] = value

    @property
    def drawing_element_12_type(self):
        """Get drawing_element_12_type

        Returns:
            str: the value of `drawing_element_12_type` or None if not set
        """
        return self._data["Drawing Element 12 Type"]

    @drawing_element_12_type.setter
    def drawing_element_12_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_12_type`

        Args:
            value (str): value for IDD Field `drawing_element_12_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_12_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_12_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_12_type`'.format(value))

        self._data["Drawing Element 12 Type"] = value

    @property
    def color_for_drawing_element_12(self):
        """Get color_for_drawing_element_12

        Returns:
            int: the value of `color_for_drawing_element_12` or None if not set
        """
        return self._data["Color for Drawing Element 12"]

    @color_for_drawing_element_12.setter
    def color_for_drawing_element_12(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_12`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_12`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_12`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_12`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_12`')

        self._data["Color for Drawing Element 12"] = value

    @property
    def drawing_element_13_type(self):
        """Get drawing_element_13_type

        Returns:
            str: the value of `drawing_element_13_type` or None if not set
        """
        return self._data["Drawing Element 13 Type"]

    @drawing_element_13_type.setter
    def drawing_element_13_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_13_type`

        Args:
            value (str): value for IDD Field `drawing_element_13_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_13_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_13_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_13_type`'.format(value))

        self._data["Drawing Element 13 Type"] = value

    @property
    def color_for_drawing_element_13(self):
        """Get color_for_drawing_element_13

        Returns:
            int: the value of `color_for_drawing_element_13` or None if not set
        """
        return self._data["Color for Drawing Element 13"]

    @color_for_drawing_element_13.setter
    def color_for_drawing_element_13(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_13`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_13`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_13`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_13`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_13`')

        self._data["Color for Drawing Element 13"] = value

    @property
    def drawing_element_14_type(self):
        """Get drawing_element_14_type

        Returns:
            str: the value of `drawing_element_14_type` or None if not set
        """
        return self._data["Drawing Element 14 Type"]

    @drawing_element_14_type.setter
    def drawing_element_14_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_14_type`

        Args:
            value (str): value for IDD Field `drawing_element_14_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_14_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_14_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_14_type`'.format(value))

        self._data["Drawing Element 14 Type"] = value

    @property
    def color_for_drawing_element_14(self):
        """Get color_for_drawing_element_14

        Returns:
            int: the value of `color_for_drawing_element_14` or None if not set
        """
        return self._data["Color for Drawing Element 14"]

    @color_for_drawing_element_14.setter
    def color_for_drawing_element_14(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_14`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_14`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_14`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_14`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_14`')

        self._data["Color for Drawing Element 14"] = value

    @property
    def drawing_element_15_type(self):
        """Get drawing_element_15_type

        Returns:
            str: the value of `drawing_element_15_type` or None if not set
        """
        return self._data["Drawing Element 15 Type"]

    @drawing_element_15_type.setter
    def drawing_element_15_type(self, value=None):
        """  Corresponds to IDD Field `drawing_element_15_type`

        Args:
            value (str): value for IDD Field `drawing_element_15_type`
                Accepted values are:
                      - Text
                      - Walls
                      - Windows
                      - GlassDoors
                      - Doors
                      - Roofs
                      - Floors
                      - DetachedBuildingShades
                      - DetachedFixedShades
                      - AttachedBuildingShades
                      - Photovoltaics
                      - TubularDaylightDomes
                      - TubularDaylightDiffusers
                      - DaylightReferencePoint1
                      - DaylightReferencePoint2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `drawing_element_15_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `drawing_element_15_type`')
            vals = set()
            vals.add("Text")
            vals.add("Walls")
            vals.add("Windows")
            vals.add("GlassDoors")
            vals.add("Doors")
            vals.add("Roofs")
            vals.add("Floors")
            vals.add("DetachedBuildingShades")
            vals.add("DetachedFixedShades")
            vals.add("AttachedBuildingShades")
            vals.add("Photovoltaics")
            vals.add("TubularDaylightDomes")
            vals.add("TubularDaylightDiffusers")
            vals.add("DaylightReferencePoint1")
            vals.add("DaylightReferencePoint2")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `drawing_element_15_type`'.format(value))

        self._data["Drawing Element 15 Type"] = value

    @property
    def color_for_drawing_element_15(self):
        """Get color_for_drawing_element_15

        Returns:
            int: the value of `color_for_drawing_element_15` or None if not set
        """
        return self._data["Color for Drawing Element 15"]

    @color_for_drawing_element_15.setter
    def color_for_drawing_element_15(self, value=None):
        """  Corresponds to IDD Field `color_for_drawing_element_15`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `color_for_drawing_element_15`
                value >= 0
                value <= 255
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
                                 'for field `color_for_drawing_element_15`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `color_for_drawing_element_15`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `color_for_drawing_element_15`')

        self._data["Color for Drawing Element 15"] = value

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
        out.append(self._to_str(self.drawing_element_1_type))
        out.append(self._to_str(self.color_for_drawing_element_1))
        out.append(self._to_str(self.drawing_element_2_type))
        out.append(self._to_str(self.color_for_drawing_element_2))
        out.append(self._to_str(self.drawing_element_3_type))
        out.append(self._to_str(self.color_for_drawing_element_3))
        out.append(self._to_str(self.drawing_element_4_type))
        out.append(self._to_str(self.color_for_drawing_element_4))
        out.append(self._to_str(self.drawing_element_5_type))
        out.append(self._to_str(self.color_for_drawing_element_5))
        out.append(self._to_str(self.drawing_element_6_type))
        out.append(self._to_str(self.color_for_drawing_element_6))
        out.append(self._to_str(self.drawing_element_7_type))
        out.append(self._to_str(self.color_for_drawing_element_7))
        out.append(self._to_str(self.drawing_element_8_type))
        out.append(self._to_str(self.color_for_drawing_element_8))
        out.append(self._to_str(self.drawing_element_9_type))
        out.append(self._to_str(self.color_for_drawing_element_9))
        out.append(self._to_str(self.drawing_element_10_type))
        out.append(self._to_str(self.color_for_drawing_element_10))
        out.append(self._to_str(self.drawing_element_11_type))
        out.append(self._to_str(self.color_for_drawing_element_11))
        out.append(self._to_str(self.drawing_element_12_type))
        out.append(self._to_str(self.color_for_drawing_element_12))
        out.append(self._to_str(self.drawing_element_13_type))
        out.append(self._to_str(self.color_for_drawing_element_13))
        out.append(self._to_str(self.drawing_element_14_type))
        out.append(self._to_str(self.color_for_drawing_element_14))
        out.append(self._to_str(self.drawing_element_15_type))
        out.append(self._to_str(self.color_for_drawing_element_15))
        return ",".join(out)

class OutputControlTableStyle(object):
    """ Corresponds to IDD object `OutputControl:Table:Style`
        default style for the OutputControl:Table:Style is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns".  HTML produces tables in HTML. XML produces an XML file.
        note - if no OutputControl:Table:Style is included, the defaults are comma and None.
    """
    internal_name = "OutputControl:Table:Style"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutputControl:Table:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None
        self._data["Unit Conversion"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.unit_conversion = None
        else:
            self.unit_conversion = vals[i]
        i += 1

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `column_separator`

        Args:
            value (str): value for IDD Field `column_separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                      - HTML
                      - XML
                      - CommaAndHTML
                      - CommaAndXML
                      - TabAndHTML
                      - XMLandHTML
                      - All
                Default value: Comma
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `column_separator`')
            vals = set()
            vals.add("Comma")
            vals.add("Tab")
            vals.add("Fixed")
            vals.add("HTML")
            vals.add("XML")
            vals.add("CommaAndHTML")
            vals.add("CommaAndXML")
            vals.add("TabAndHTML")
            vals.add("XMLandHTML")
            vals.add("All")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `column_separator`'.format(value))

        self._data["Column Separator"] = value

    @property
    def unit_conversion(self):
        """Get unit_conversion

        Returns:
            str: the value of `unit_conversion` or None if not set
        """
        return self._data["Unit Conversion"]

    @unit_conversion.setter
    def unit_conversion(self, value="None"):
        """  Corresponds to IDD Field `unit_conversion`

        Args:
            value (str): value for IDD Field `unit_conversion`
                Accepted values are:
                      - None
                      - JtoKWH
                      - JtoMJ
                      - JtoGJ
                      - InchPound
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
                                 'for field `unit_conversion`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `unit_conversion`')
            vals = set()
            vals.add("None")
            vals.add("JtoKWH")
            vals.add("JtoMJ")
            vals.add("JtoGJ")
            vals.add("InchPound")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `unit_conversion`'.format(value))

        self._data["Unit Conversion"] = value

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
        out.append(self._to_str(self.column_separator))
        out.append(self._to_str(self.unit_conversion))
        return ",".join(out)

class OutputControlReportingTolerances(object):
    """ Corresponds to IDD object `OutputControl:ReportingTolerances`
        Calculations of the time that setpoints are not met use a tolerance of 0.2C.
        This object allows changing the tolerance used to determine when setpoints are being met.
    """
    internal_name = "OutputControl:ReportingTolerances"
    field_count = 2

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `OutputControl:ReportingTolerances`
        """
        self._data = OrderedDict()
        self._data["Tolerance for Time Heating Setpoint Not Met"] = None
        self._data["Tolerance for Time Cooling Setpoint Not Met"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.tolerance_for_time_heating_setpoint_not_met = None
        else:
            self.tolerance_for_time_heating_setpoint_not_met = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.tolerance_for_time_cooling_setpoint_not_met = None
        else:
            self.tolerance_for_time_cooling_setpoint_not_met = vals[i]
        i += 1

    @property
    def tolerance_for_time_heating_setpoint_not_met(self):
        """Get tolerance_for_time_heating_setpoint_not_met

        Returns:
            float: the value of `tolerance_for_time_heating_setpoint_not_met` or None if not set
        """
        return self._data["Tolerance for Time Heating Setpoint Not Met"]

    @tolerance_for_time_heating_setpoint_not_met.setter
    def tolerance_for_time_heating_setpoint_not_met(self, value=0.2 ):
        """  Corresponds to IDD Field `tolerance_for_time_heating_setpoint_not_met`
        If the zone temperature is below the heating setpoint by more than
        this value, the following output variables will increment as appropriate
        Zone Heating Setpoint Not Met Time
        Zone Heating Setpoint Not Met While Occupied Time
        This also impacts table report "Annual Building Utility Performance Summary"
        subtable "Comfort and Setpoint Not Met Summary"

        Args:
            value (float): value for IDD Field `tolerance_for_time_heating_setpoint_not_met`
                Unit: deltaC
                Default value: 0.2
                value >= 0.0
                value <= 10.0
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
                                 'for field `tolerance_for_time_heating_setpoint_not_met`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tolerance_for_time_heating_setpoint_not_met`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `tolerance_for_time_heating_setpoint_not_met`')

        self._data["Tolerance for Time Heating Setpoint Not Met"] = value

    @property
    def tolerance_for_time_cooling_setpoint_not_met(self):
        """Get tolerance_for_time_cooling_setpoint_not_met

        Returns:
            float: the value of `tolerance_for_time_cooling_setpoint_not_met` or None if not set
        """
        return self._data["Tolerance for Time Cooling Setpoint Not Met"]

    @tolerance_for_time_cooling_setpoint_not_met.setter
    def tolerance_for_time_cooling_setpoint_not_met(self, value=0.2 ):
        """  Corresponds to IDD Field `tolerance_for_time_cooling_setpoint_not_met`
        If the zone temperature is above the cooling setpoint by more than
        this value, the following output variables will increment as appropriate
        Zone Cooling Setpoint Not Met Time
        Zone Cooling Setpoint Not Met While Occupied Time
        This also impacts table report "Annual Building Utility Performance Summary"
        subtable "Comfort and Setpoint Not Met Summary"

        Args:
            value (float): value for IDD Field `tolerance_for_time_cooling_setpoint_not_met`
                Unit: deltaC
                Default value: 0.2
                value >= 0.0
                value <= 10.0
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
                                 'for field `tolerance_for_time_cooling_setpoint_not_met`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `tolerance_for_time_cooling_setpoint_not_met`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `tolerance_for_time_cooling_setpoint_not_met`')

        self._data["Tolerance for Time Cooling Setpoint Not Met"] = value

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
        out.append(self._to_str(self.tolerance_for_time_heating_setpoint_not_met))
        out.append(self._to_str(self.tolerance_for_time_cooling_setpoint_not_met))
        return ",".join(out)