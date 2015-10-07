""" Data objects in group "Output Reporting"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class OutputVariableDictionary(DataObject):

    """ Corresponds to IDD object `Output:VariableDictionary`
        Produces a list summarizing the output variables and meters that are available for
        reporting for the model being simulated (rdd output file). The list varies depending
        on the types of objects present in the idf file.  For example, variables related to
        lights will only appear if a Lights object is present. The IDF option generates
        complete Output:Variable objects to simplify adding the desired output to the idf file.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'key field',
                                       {'name': u'Key Field',
                                        'pyname': u'key_field',
                                        'default': u'regular',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'IDF',
                                                            u'regular'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'sort option',
                                       {'name': u'Sort Option',
                                        'pyname': u'sort_option',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Name',
                                                            u'Unsorted'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:VariableDictionary',
               'pyname': u'OutputVariableDictionary',
               'required-object': False,
               'unique-object': False}

    @property
    def key_field(self):
        """field `Key Field`

        |  Default value: regular

        Args:
            value (str): value for IDD Field `Key Field`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `key_field` or None if not set

        """
        return self["Key Field"]

    @key_field.setter
    def key_field(self, value="regular"):
        """Corresponds to IDD field `Key Field`"""
        self["Key Field"] = value

    @property
    def sort_option(self):
        """field `Sort Option`

        Args:
            value (str): value for IDD Field `Sort Option`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sort_option` or None if not set

        """
        return self["Sort Option"]

    @sort_option.setter
    def sort_option(self, value=None):
        """Corresponds to IDD field `Sort Option`"""
        self["Sort Option"] = value




class OutputSurfacesList(DataObject):

    """ Corresponds to IDD object `Output:Surfaces:List`
        Produces a report summarizing the details of surfaces in the eio output file.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'report type',
                                       {'name': u'Report Type',
                                        'pyname': u'report_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Details',
                                                            u'Vertices',
                                                            u'DetailsWithVertices',
                                                            u'ViewFactorInfo',
                                                            u'Lines',
                                                            u'CostInfo',
                                                            u'DecayCurvesfromZoneComponentLoads'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'report specifications',
                                       {'name': u'Report Specifications',
                                        'pyname': u'report_specifications',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'IDF'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Surfaces:List',
               'pyname': u'OutputSurfacesList',
               'required-object': False,
               'unique-object': False}

    @property
    def report_type(self):
        """field `Report Type`

        Args:
            value (str): value for IDD Field `Report Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `report_type` or None if not set

        """
        return self["Report Type"]

    @report_type.setter
    def report_type(self, value=None):
        """Corresponds to IDD field `Report Type`"""
        self["Report Type"] = value

    @property
    def report_specifications(self):
        """field `Report Specifications`

        |  (IDF, only for Output:Surfaces:List, Lines report --
        |  will print transformed coordinates in IDF style)

        Args:
            value (str): value for IDD Field `Report Specifications`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `report_specifications` or None if not set

        """
        return self["Report Specifications"]

    @report_specifications.setter
    def report_specifications(self, value=None):
        """Corresponds to IDD field `Report Specifications`"""
        self["Report Specifications"] = value




class OutputSurfacesDrawing(DataObject):

    """ Corresponds to IDD object `Output:Surfaces:Drawing`
        Produces reports/files that are capable of rendering graphically or
        being imported into other programs. Rendering does not alter the
        actual inputs/surfaces.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'report type',
                                       {'name': u'Report Type',
                                        'pyname': u'report_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'DXF',
                                                            u'DXF:WireFrame',
                                                            u'VRML'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'report specifications 1',
                                       {'name': u'Report Specifications 1',
                                        'pyname': u'report_specifications_1',
                                        'default': u'Triangulate3DFace',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Triangulate3DFace',
                                                            u'ThickPolyline',
                                                            u'RegularPolyline'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'report specifications 2',
                                       {'name': u'Report Specifications 2',
                                        'pyname': u'report_specifications_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Surfaces:Drawing',
               'pyname': u'OutputSurfacesDrawing',
               'required-object': False,
               'unique-object': False}

    @property
    def report_type(self):
        """field `Report Type`

        Args:
            value (str): value for IDD Field `Report Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `report_type` or None if not set

        """
        return self["Report Type"]

    @report_type.setter
    def report_type(self, value=None):
        """Corresponds to IDD field `Report Type`"""
        self["Report Type"] = value

    @property
    def report_specifications_1(self):
        """field `Report Specifications 1`

        |  Triangulate3DFace (default), ThickPolyline, RegularPolyline apply to DXF
        |  This field is ignored for DXF:WireFrame and VRML
        |  Default value: Triangulate3DFace

        Args:
            value (str): value for IDD Field `Report Specifications 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `report_specifications_1` or None if not set

        """
        return self["Report Specifications 1"]

    @report_specifications_1.setter
    def report_specifications_1(self, value="Triangulate3DFace"):
        """Corresponds to IDD field `Report Specifications 1`"""
        self["Report Specifications 1"] = value

    @property
    def report_specifications_2(self):
        """field `Report Specifications 2`

        |  Use ColorScheme Name for DXF reports

        Args:
            value (str): value for IDD Field `Report Specifications 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `report_specifications_2` or None if not set

        """
        return self["Report Specifications 2"]

    @report_specifications_2.setter
    def report_specifications_2(self, value=None):
        """Corresponds to IDD field `Report Specifications 2`"""
        self["Report Specifications 2"] = value




class OutputSchedules(DataObject):

    """ Corresponds to IDD object `Output:Schedules`
        Produces a condensed reporting that illustrates the full range of schedule values in
        the eio output file. In the style of input: DaySchedule,  WeekSchedule, and
        Annual Schedule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'key field',
                                       {'name': u'Key Field',
                                        'pyname': u'key_field',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Hourly',
                                                            u'Timestep'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Schedules',
               'pyname': u'OutputSchedules',
               'required-object': False,
               'unique-object': False}

    @property
    def key_field(self):
        """field `Key Field`

        Args:
            value (str): value for IDD Field `Key Field`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `key_field` or None if not set

        """
        return self["Key Field"]

    @key_field.setter
    def key_field(self, value=None):
        """Corresponds to IDD field `Key Field`"""
        self["Key Field"] = value




class OutputConstructions(DataObject):

    """ Corresponds to IDD object `Output:Constructions`
        Adds a report to the eio output file which shows details for each construction,
        including overall properties, a list of material layers, and calculated results
        related to conduction transfer functions.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'details type 1',
                                       {'name': u'Details Type 1',
                                        'pyname': u'details_type_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constructions',
                                                            u'Materials'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'details type 2',
                                       {'name': u'Details Type 2',
                                        'pyname': u'details_type_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constructions',
                                                            u'Materials'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Constructions',
               'pyname': u'OutputConstructions',
               'required-object': False,
               'unique-object': False}

    @property
    def details_type_1(self):
        """field `Details Type 1`

        Args:
            value (str): value for IDD Field `Details Type 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `details_type_1` or None if not set

        """
        return self["Details Type 1"]

    @details_type_1.setter
    def details_type_1(self, value=None):
        """Corresponds to IDD field `Details Type 1`"""
        self["Details Type 1"] = value

    @property
    def details_type_2(self):
        """field `Details Type 2`

        Args:
            value (str): value for IDD Field `Details Type 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `details_type_2` or None if not set

        """
        return self["Details Type 2"]

    @details_type_2.setter
    def details_type_2(self, value=None):
        """Corresponds to IDD field `Details Type 2`"""
        self["Details Type 2"] = value




class OutputEnergyManagementSystem(DataObject):

    """ Corresponds to IDD object `Output:EnergyManagementSystem`
        This object is used to control the output produced by the Energy Management System
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'actuator availability dictionary reporting',
                                       {'name': u'Actuator Availability Dictionary Reporting',
                                        'pyname': u'actuator_availability_dictionary_reporting',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'NotByUniqueKeyNames',
                                                            u'Verbose'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'internal variable availability dictionary reporting',
                                       {'name': u'Internal Variable Availability Dictionary Reporting',
                                        'pyname': u'internal_variable_availability_dictionary_reporting',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'NotByUniqueKeyNames',
                                                            u'Verbose'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ems runtime language debug output level',
                                       {'name': u'EMS Runtime Language Debug Output Level',
                                        'pyname': u'ems_runtime_language_debug_output_level',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'ErrorsOnly',
                                                            u'Verbose'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:EnergyManagementSystem',
               'pyname': u'OutputEnergyManagementSystem',
               'required-object': False,
               'unique-object': True}

    @property
    def actuator_availability_dictionary_reporting(self):
        """field `Actuator Availability Dictionary Reporting`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Actuator Availability Dictionary Reporting`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `actuator_availability_dictionary_reporting` or None if not set

        """
        return self["Actuator Availability Dictionary Reporting"]

    @actuator_availability_dictionary_reporting.setter
    def actuator_availability_dictionary_reporting(self, value="None"):
        """Corresponds to IDD field `Actuator Availability Dictionary
        Reporting`"""
        self["Actuator Availability Dictionary Reporting"] = value

    @property
    def internal_variable_availability_dictionary_reporting(self):
        """field `Internal Variable Availability Dictionary Reporting`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Internal Variable Availability Dictionary Reporting`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `internal_variable_availability_dictionary_reporting` or None if not set

        """
        return self["Internal Variable Availability Dictionary Reporting"]

    @internal_variable_availability_dictionary_reporting.setter
    def internal_variable_availability_dictionary_reporting(
            self,
            value="None"):
        """Corresponds to IDD field `Internal Variable Availability Dictionary
        Reporting`"""
        self["Internal Variable Availability Dictionary Reporting"] = value

    @property
    def ems_runtime_language_debug_output_level(self):
        """field `EMS Runtime Language Debug Output Level`

        |  Default value: None

        Args:
            value (str): value for IDD Field `EMS Runtime Language Debug Output Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ems_runtime_language_debug_output_level` or None if not set

        """
        return self["EMS Runtime Language Debug Output Level"]

    @ems_runtime_language_debug_output_level.setter
    def ems_runtime_language_debug_output_level(self, value="None"):
        """Corresponds to IDD field `EMS Runtime Language Debug Output
        Level`"""
        self["EMS Runtime Language Debug Output Level"] = value




class OutputControlSurfaceColorScheme(DataObject):

    """ Corresponds to IDD object `OutputControl:SurfaceColorScheme`
        This object is used to set colors for reporting on various building elements particularly for the
        DXF reports.  We know the user can enter 0 to 255 and the color map is available in DXF output.
        Therefore, we are limiting the colors in that range.  You can
        extend by editing the IDD but you do so on your own.  Colors not changed in any scheme will
        remain as the default scheme uses.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'drawing element 1 type',
                                       {'name': u'Drawing Element 1 Type',
                                        'pyname': u'drawing_element_1_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 1',
                                       {'name': u'Color for Drawing Element 1',
                                        'pyname': u'color_for_drawing_element_1',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 2 type',
                                       {'name': u'Drawing Element 2 Type',
                                        'pyname': u'drawing_element_2_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 2',
                                       {'name': u'Color for Drawing Element 2',
                                        'pyname': u'color_for_drawing_element_2',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 3 type',
                                       {'name': u'Drawing Element 3 Type',
                                        'pyname': u'drawing_element_3_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 3',
                                       {'name': u'Color for Drawing Element 3',
                                        'pyname': u'color_for_drawing_element_3',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 4 type',
                                       {'name': u'Drawing Element 4 Type',
                                        'pyname': u'drawing_element_4_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 4',
                                       {'name': u'Color for Drawing Element 4',
                                        'pyname': u'color_for_drawing_element_4',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 5 type',
                                       {'name': u'Drawing Element 5 Type',
                                        'pyname': u'drawing_element_5_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 5',
                                       {'name': u'Color for Drawing Element 5',
                                        'pyname': u'color_for_drawing_element_5',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 6 type',
                                       {'name': u'Drawing Element 6 Type',
                                        'pyname': u'drawing_element_6_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 6',
                                       {'name': u'Color for Drawing Element 6',
                                        'pyname': u'color_for_drawing_element_6',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 7 type',
                                       {'name': u'Drawing Element 7 Type',
                                        'pyname': u'drawing_element_7_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 7',
                                       {'name': u'Color for Drawing Element 7',
                                        'pyname': u'color_for_drawing_element_7',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 8 type',
                                       {'name': u'Drawing Element 8 Type',
                                        'pyname': u'drawing_element_8_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 8',
                                       {'name': u'Color for Drawing Element 8',
                                        'pyname': u'color_for_drawing_element_8',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 9 type',
                                       {'name': u'Drawing Element 9 Type',
                                        'pyname': u'drawing_element_9_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 9',
                                       {'name': u'Color for Drawing Element 9',
                                        'pyname': u'color_for_drawing_element_9',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 10 type',
                                       {'name': u'Drawing Element 10 Type',
                                        'pyname': u'drawing_element_10_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 10',
                                       {'name': u'Color for Drawing Element 10',
                                        'pyname': u'color_for_drawing_element_10',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 11 type',
                                       {'name': u'Drawing Element 11 Type',
                                        'pyname': u'drawing_element_11_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 11',
                                       {'name': u'Color for Drawing Element 11',
                                        'pyname': u'color_for_drawing_element_11',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 12 type',
                                       {'name': u'Drawing Element 12 Type',
                                        'pyname': u'drawing_element_12_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 12',
                                       {'name': u'Color for Drawing Element 12',
                                        'pyname': u'color_for_drawing_element_12',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 13 type',
                                       {'name': u'Drawing Element 13 Type',
                                        'pyname': u'drawing_element_13_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 13',
                                       {'name': u'Color for Drawing Element 13',
                                        'pyname': u'color_for_drawing_element_13',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 14 type',
                                       {'name': u'Drawing Element 14 Type',
                                        'pyname': u'drawing_element_14_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 14',
                                       {'name': u'Color for Drawing Element 14',
                                        'pyname': u'color_for_drawing_element_14',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'drawing element 15 type',
                                       {'name': u'Drawing Element 15 Type',
                                        'pyname': u'drawing_element_15_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Text',
                                                            u'Walls',
                                                            u'Windows',
                                                            u'GlassDoors',
                                                            u'Doors',
                                                            u'Roofs',
                                                            u'Floors',
                                                            u'DetachedBuildingShades',
                                                            u'DetachedFixedShades',
                                                            u'AttachedBuildingShades',
                                                            u'Photovoltaics',
                                                            u'TubularDaylightDomes',
                                                            u'TubularDaylightDiffusers',
                                                            u'DaylightReferencePoint1',
                                                            u'DaylightReferencePoint2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'color for drawing element 15',
                                       {'name': u'Color for Drawing Element 15',
                                        'pyname': u'color_for_drawing_element_15',
                                        'maximum': 255,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'OutputControl:SurfaceColorScheme',
               'pyname': u'OutputControlSurfaceColorScheme',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  choose a name or use one of the DataSets

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def drawing_element_1_type(self):
        """field `Drawing Element 1 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 1 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_1_type` or None if not set

        """
        return self["Drawing Element 1 Type"]

    @drawing_element_1_type.setter
    def drawing_element_1_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 1 Type`"""
        self["Drawing Element 1 Type"] = value

    @property
    def color_for_drawing_element_1(self):
        """field `Color for Drawing Element 1`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_1` or None if not set

        """
        return self["Color for Drawing Element 1"]

    @color_for_drawing_element_1.setter
    def color_for_drawing_element_1(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 1`"""
        self["Color for Drawing Element 1"] = value

    @property
    def drawing_element_2_type(self):
        """field `Drawing Element 2 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 2 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_2_type` or None if not set

        """
        return self["Drawing Element 2 Type"]

    @drawing_element_2_type.setter
    def drawing_element_2_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 2 Type`"""
        self["Drawing Element 2 Type"] = value

    @property
    def color_for_drawing_element_2(self):
        """field `Color for Drawing Element 2`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_2` or None if not set

        """
        return self["Color for Drawing Element 2"]

    @color_for_drawing_element_2.setter
    def color_for_drawing_element_2(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 2`"""
        self["Color for Drawing Element 2"] = value

    @property
    def drawing_element_3_type(self):
        """field `Drawing Element 3 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 3 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_3_type` or None if not set

        """
        return self["Drawing Element 3 Type"]

    @drawing_element_3_type.setter
    def drawing_element_3_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 3 Type`"""
        self["Drawing Element 3 Type"] = value

    @property
    def color_for_drawing_element_3(self):
        """field `Color for Drawing Element 3`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_3` or None if not set

        """
        return self["Color for Drawing Element 3"]

    @color_for_drawing_element_3.setter
    def color_for_drawing_element_3(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 3`"""
        self["Color for Drawing Element 3"] = value

    @property
    def drawing_element_4_type(self):
        """field `Drawing Element 4 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 4 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_4_type` or None if not set

        """
        return self["Drawing Element 4 Type"]

    @drawing_element_4_type.setter
    def drawing_element_4_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 4 Type`"""
        self["Drawing Element 4 Type"] = value

    @property
    def color_for_drawing_element_4(self):
        """field `Color for Drawing Element 4`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_4` or None if not set

        """
        return self["Color for Drawing Element 4"]

    @color_for_drawing_element_4.setter
    def color_for_drawing_element_4(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 4`"""
        self["Color for Drawing Element 4"] = value

    @property
    def drawing_element_5_type(self):
        """field `Drawing Element 5 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 5 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_5_type` or None if not set

        """
        return self["Drawing Element 5 Type"]

    @drawing_element_5_type.setter
    def drawing_element_5_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 5 Type`"""
        self["Drawing Element 5 Type"] = value

    @property
    def color_for_drawing_element_5(self):
        """field `Color for Drawing Element 5`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_5` or None if not set

        """
        return self["Color for Drawing Element 5"]

    @color_for_drawing_element_5.setter
    def color_for_drawing_element_5(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 5`"""
        self["Color for Drawing Element 5"] = value

    @property
    def drawing_element_6_type(self):
        """field `Drawing Element 6 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 6 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_6_type` or None if not set

        """
        return self["Drawing Element 6 Type"]

    @drawing_element_6_type.setter
    def drawing_element_6_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 6 Type`"""
        self["Drawing Element 6 Type"] = value

    @property
    def color_for_drawing_element_6(self):
        """field `Color for Drawing Element 6`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_6` or None if not set

        """
        return self["Color for Drawing Element 6"]

    @color_for_drawing_element_6.setter
    def color_for_drawing_element_6(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 6`"""
        self["Color for Drawing Element 6"] = value

    @property
    def drawing_element_7_type(self):
        """field `Drawing Element 7 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 7 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_7_type` or None if not set

        """
        return self["Drawing Element 7 Type"]

    @drawing_element_7_type.setter
    def drawing_element_7_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 7 Type`"""
        self["Drawing Element 7 Type"] = value

    @property
    def color_for_drawing_element_7(self):
        """field `Color for Drawing Element 7`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_7` or None if not set

        """
        return self["Color for Drawing Element 7"]

    @color_for_drawing_element_7.setter
    def color_for_drawing_element_7(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 7`"""
        self["Color for Drawing Element 7"] = value

    @property
    def drawing_element_8_type(self):
        """field `Drawing Element 8 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 8 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_8_type` or None if not set

        """
        return self["Drawing Element 8 Type"]

    @drawing_element_8_type.setter
    def drawing_element_8_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 8 Type`"""
        self["Drawing Element 8 Type"] = value

    @property
    def color_for_drawing_element_8(self):
        """field `Color for Drawing Element 8`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_8` or None if not set

        """
        return self["Color for Drawing Element 8"]

    @color_for_drawing_element_8.setter
    def color_for_drawing_element_8(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 8`"""
        self["Color for Drawing Element 8"] = value

    @property
    def drawing_element_9_type(self):
        """field `Drawing Element 9 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 9 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_9_type` or None if not set

        """
        return self["Drawing Element 9 Type"]

    @drawing_element_9_type.setter
    def drawing_element_9_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 9 Type`"""
        self["Drawing Element 9 Type"] = value

    @property
    def color_for_drawing_element_9(self):
        """field `Color for Drawing Element 9`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_9` or None if not set

        """
        return self["Color for Drawing Element 9"]

    @color_for_drawing_element_9.setter
    def color_for_drawing_element_9(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 9`"""
        self["Color for Drawing Element 9"] = value

    @property
    def drawing_element_10_type(self):
        """field `Drawing Element 10 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 10 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_10_type` or None if not set

        """
        return self["Drawing Element 10 Type"]

    @drawing_element_10_type.setter
    def drawing_element_10_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 10 Type`"""
        self["Drawing Element 10 Type"] = value

    @property
    def color_for_drawing_element_10(self):
        """field `Color for Drawing Element 10`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_10` or None if not set

        """
        return self["Color for Drawing Element 10"]

    @color_for_drawing_element_10.setter
    def color_for_drawing_element_10(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 10`"""
        self["Color for Drawing Element 10"] = value

    @property
    def drawing_element_11_type(self):
        """field `Drawing Element 11 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 11 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_11_type` or None if not set

        """
        return self["Drawing Element 11 Type"]

    @drawing_element_11_type.setter
    def drawing_element_11_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 11 Type`"""
        self["Drawing Element 11 Type"] = value

    @property
    def color_for_drawing_element_11(self):
        """field `Color for Drawing Element 11`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_11` or None if not set

        """
        return self["Color for Drawing Element 11"]

    @color_for_drawing_element_11.setter
    def color_for_drawing_element_11(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 11`"""
        self["Color for Drawing Element 11"] = value

    @property
    def drawing_element_12_type(self):
        """field `Drawing Element 12 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 12 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_12_type` or None if not set

        """
        return self["Drawing Element 12 Type"]

    @drawing_element_12_type.setter
    def drawing_element_12_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 12 Type`"""
        self["Drawing Element 12 Type"] = value

    @property
    def color_for_drawing_element_12(self):
        """field `Color for Drawing Element 12`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_12` or None if not set

        """
        return self["Color for Drawing Element 12"]

    @color_for_drawing_element_12.setter
    def color_for_drawing_element_12(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 12`"""
        self["Color for Drawing Element 12"] = value

    @property
    def drawing_element_13_type(self):
        """field `Drawing Element 13 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 13 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_13_type` or None if not set

        """
        return self["Drawing Element 13 Type"]

    @drawing_element_13_type.setter
    def drawing_element_13_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 13 Type`"""
        self["Drawing Element 13 Type"] = value

    @property
    def color_for_drawing_element_13(self):
        """field `Color for Drawing Element 13`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_13` or None if not set

        """
        return self["Color for Drawing Element 13"]

    @color_for_drawing_element_13.setter
    def color_for_drawing_element_13(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 13`"""
        self["Color for Drawing Element 13"] = value

    @property
    def drawing_element_14_type(self):
        """field `Drawing Element 14 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 14 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_14_type` or None if not set

        """
        return self["Drawing Element 14 Type"]

    @drawing_element_14_type.setter
    def drawing_element_14_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 14 Type`"""
        self["Drawing Element 14 Type"] = value

    @property
    def color_for_drawing_element_14(self):
        """field `Color for Drawing Element 14`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_14` or None if not set

        """
        return self["Color for Drawing Element 14"]

    @color_for_drawing_element_14.setter
    def color_for_drawing_element_14(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 14`"""
        self["Color for Drawing Element 14"] = value

    @property
    def drawing_element_15_type(self):
        """field `Drawing Element 15 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 15 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drawing_element_15_type` or None if not set

        """
        return self["Drawing Element 15 Type"]

    @drawing_element_15_type.setter
    def drawing_element_15_type(self, value=None):
        """Corresponds to IDD field `Drawing Element 15 Type`"""
        self["Drawing Element 15 Type"] = value

    @property
    def color_for_drawing_element_15(self):
        """field `Color for Drawing Element 15`

        |  use color number for output assignment (e.g. DXF)
        |  value <= 255

        Args:
            value (int): value for IDD Field `Color for Drawing Element 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `color_for_drawing_element_15` or None if not set

        """
        return self["Color for Drawing Element 15"]

    @color_for_drawing_element_15.setter
    def color_for_drawing_element_15(self, value=None):
        """Corresponds to IDD field `Color for Drawing Element 15`"""
        self["Color for Drawing Element 15"] = value




class OutputTableSummaryReports(DataObject):

    """ Corresponds to IDD object `Output:Table:SummaryReports`
        This object allows the user to call report types that are predefined and will appear with the
        other tabular reports.  These predefined reports are sensitive to the OutputControl:Table:Style object
        and appear in the same files as the tabular reports.  The entries for this object is a list
        of the predefined reports that should appear in the tabular report output file.
        There should be as many fields (A) in this object as there are keys in the following (minus
        AllSummary+AllMonthly+AllSummaryAndMonthly)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict(),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Table:SummaryReports',
               'pyname': u'OutputTableSummaryReports',
               'required-object': False,
               'unique-object': True}




class OutputTableTimeBins(DataObject):

    """ Corresponds to IDD object `Output:Table:TimeBins`
        Produces a bin report in the table output file which shows the amount of time in hours
        that occurs in different bins for a single specific output variable or meter.
        Two different types of binning are reported: by month and by hour of the day.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'key value',
                                       {'name': u'Key Value',
                                        'pyname': u'key_value',
                                        'default': u'*',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'variable name',
                                       {'name': u'Variable Name',
                                        'pyname': u'variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'interval start',
                                       {'name': u'Interval Start',
                                        'pyname': u'interval_start',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'interval size',
                                       {'name': u'Interval Size',
                                        'pyname': u'interval_size',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'interval count',
                                       {'name': u'Interval Count',
                                        'pyname': u'interval_count',
                                        'maximum': 20,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'variable type',
                                       {'name': u'Variable Type',
                                        'pyname': u'variable_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Energy',
                                                            u'Temperature',
                                                            u'VolumetricFlow',
                                                            u'Power'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 5,
               'name': u'Output:Table:TimeBins',
               'pyname': u'OutputTableTimeBins',
               'required-object': False,
               'unique-object': False}

    @property
    def key_value(self):
        """field `Key Value`

        |  use '*' (without quotes) to apply this variable to all keys
        |  Default value: *

        Args:
            value (str): value for IDD Field `Key Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `key_value` or None if not set

        """
        return self["Key Value"]

    @key_value.setter
    def key_value(self, value="*"):
        """Corresponds to IDD field `Key Value`"""
        self["Key Value"] = value

    @property
    def variable_name(self):
        """field `Variable Name`

        Args:
            value (str): value for IDD Field `Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `variable_name` or None if not set

        """
        return self["Variable Name"]

    @variable_name.setter
    def variable_name(self, value=None):
        """Corresponds to IDD field `Variable Name`"""
        self["Variable Name"] = value

    @property
    def interval_start(self):
        """field `Interval Start`

        |  The lowest value for the intervals being binned into.
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Interval Start`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `interval_start` or None if not set

        """
        return self["Interval Start"]

    @interval_start.setter
    def interval_start(self, value=None):
        """Corresponds to IDD field `Interval Start`"""
        self["Interval Start"] = value

    @property
    def interval_size(self):
        """field `Interval Size`

        |  The size of the bins starting with Interval start.
        |  Units are based on field `A4`

        Args:
            value (float): value for IDD Field `Interval Size`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `interval_size` or None if not set

        """
        return self["Interval Size"]

    @interval_size.setter
    def interval_size(self, value=None):
        """Corresponds to IDD field `Interval Size`"""
        self["Interval Size"] = value

    @property
    def interval_count(self):
        """field `Interval Count`

        |  The number of bins used. The number of hours below the start of the
        |  Lowest bin and above the value of the last bin are also shown.
        |  value >= 1
        |  value <= 20

        Args:
            value (int): value for IDD Field `Interval Count`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `interval_count` or None if not set

        """
        return self["Interval Count"]

    @interval_count.setter
    def interval_count(self, value=None):
        """Corresponds to IDD field `Interval Count`"""
        self["Interval Count"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Optional schedule name. Binning is performed for non-zero hours.
        |  Binning always performed if left blank.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def variable_type(self):
        """field `Variable Type`

        |  Optional input on the type of units for the variable used by other fields in the object.

        Args:
            value (str): value for IDD Field `Variable Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `variable_type` or None if not set

        """
        return self["Variable Type"]

    @variable_type.setter
    def variable_type(self, value=None):
        """Corresponds to IDD field `Variable Type`"""
        self["Variable Type"] = value




class OutputTableMonthly(DataObject):

    """ Corresponds to IDD object `Output:Table:Monthly`
        Provides a generic method of setting up tables of monthly results. The report
        has multiple columns that are each defined using a repeated group of fields for any
        number of columns. A single Output:Table:Monthly object often produces multiple
        tables in the output. A table is produced for every instance of a particular output
        variable. For example, a table defined with zone variables will be produced once for
        every zone.
    """
    _schema = {'extensible-fields': OrderedDict([(u'variable or meter 1 name',
                                                  {'name': u'Variable or Meter 1 Name',
                                                   'pyname': u'variable_or_meter_1_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'external-list'}),
                                                 (u'aggregation type for variable or meter 1',
                                                  {'name': u'Aggregation Type for Variable or Meter 1',
                                                   'pyname': u'aggregation_type_for_variable_or_meter_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'accepted-values': [u'SumOrAverage',
                                                                       u'Maximum',
                                                                       u'Minimum',
                                                                       u'ValueWhenMaximumOrMinimum',
                                                                       u'HoursNonZero',
                                                                       u'HoursZero',
                                                                       u'HoursPositive',
                                                                       u'HoursNonPositive',
                                                                       u'HoursNegative',
                                                                       u'HoursNonNegative',
                                                                       u'SumOrAverageDuringHoursShown',
                                                                       u'MaximumDuringHoursShown',
                                                                       u'MinimumDuringHoursShown'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'digits after decimal',
                                       {'name': u'Digits After Decimal',
                                        'pyname': u'digits_after_decimal',
                                        'default': 2,
                                        'maximum': 10,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Table:Monthly',
               'pyname': u'OutputTableMonthly',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def digits_after_decimal(self):
        """field `Digits After Decimal`

        |  Default value: 2
        |  value <= 10

        Args:
            value (int): value for IDD Field `Digits After Decimal`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `digits_after_decimal` or None if not set

        """
        return self["Digits After Decimal"]

    @digits_after_decimal.setter
    def digits_after_decimal(self, value=2):
        """Corresponds to IDD field `Digits After Decimal`"""
        self["Digits After Decimal"] = value

    def add_extensible(self,
                       variable_or_meter_1_name=None,
                       aggregation_type_for_variable_or_meter_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            variable_or_meter_1_name (str): value for IDD Field `Variable or Meter 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            aggregation_type_for_variable_or_meter_1 (str): value for IDD Field `Aggregation Type for Variable or Meter 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        variable_or_meter_1_name = self.check_value(
            "Variable or Meter 1 Name",
            variable_or_meter_1_name)
        vals.append(variable_or_meter_1_name)
        aggregation_type_for_variable_or_meter_1 = self.check_value(
            "Aggregation Type for Variable or Meter 1",
            aggregation_type_for_variable_or_meter_1)
        vals.append(aggregation_type_for_variable_or_meter_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class OutputTableAnnual(DataObject):

    """ Corresponds to IDD object `Output:Table:Annual`
        Provides a generic method of setting up tables of annual results with one row per object.
        The report has multiple columns that are each defined using a repeated group of fields
        for any number of columns. A single Output:Table:Annual produces a single table in the
        output.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'filter',
                                       {'name': u'Filter',
                                        'pyname': u'filter',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Table:Annual',
               'pyname': u'OutputTableAnnual',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def filter(self):
        """field `Filter`

        |  An optional text string that is compared to the names of the objects referenced by the
        |  variables and if they match are included in the table. A footnote will appear that indicates
        |  that the objects shown may not be all the objects that of that type that occur in the file.

        Args:
            value (str): value for IDD Field `Filter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `filter` or None if not set

        """
        return self["Filter"]

    @filter.setter
    def filter(self, value=None):
        """Corresponds to IDD field `Filter`"""
        self["Filter"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Optional schedule name. If left blank, aggregation is performed for all hours simulated. If
        |  a schedule is specified, aggregation is performed for non-zero hours in the schedule.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value




class OutputControlTableStyle(DataObject):

    """ Corresponds to IDD object `OutputControl:Table:Style`
        default style for the OutputControl:Table:Style is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing programs -- there tab may be a better choice.  fixed puts spaces between
        the "columns".  HTML produces tables in HTML. XML produces an XML file.
        note - if no OutputControl:Table:Style is included, the defaults are comma and None.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'column separator',
                                       {'name': u'Column Separator',
                                        'pyname': u'column_separator',
                                        'default': u'Comma',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Comma',
                                                            u'Tab',
                                                            u'Fixed',
                                                            u'HTML',
                                                            u'XML',
                                                            u'CommaAndHTML',
                                                            u'CommaAndXML',
                                                            u'TabAndHTML',
                                                            u'XMLandHTML',
                                                            u'All'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'unit conversion',
                                       {'name': u'Unit Conversion',
                                        'pyname': u'unit_conversion',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'JtoKWH',
                                                            u'JtoMJ',
                                                            u'JtoGJ',
                                                            u'InchPound'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'OutputControl:Table:Style',
               'pyname': u'OutputControlTableStyle',
               'required-object': False,
               'unique-object': True}

    @property
    def column_separator(self):
        """field `Column Separator`

        |  Default value: Comma

        Args:
            value (str): value for IDD Field `Column Separator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `column_separator` or None if not set

        """
        return self["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """Corresponds to IDD field `Column Separator`"""
        self["Column Separator"] = value

    @property
    def unit_conversion(self):
        """field `Unit Conversion`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Unit Conversion`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `unit_conversion` or None if not set

        """
        return self["Unit Conversion"]

    @unit_conversion.setter
    def unit_conversion(self, value="None"):
        """Corresponds to IDD field `Unit Conversion`"""
        self["Unit Conversion"] = value




class OutputControlReportingTolerances(DataObject):

    """ Corresponds to IDD object `OutputControl:ReportingTolerances`
        Calculations of the time that setpoints are not met use a tolerance of 0.2C.
        This object allows changing the tolerance used to determine when setpoints are being met.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'tolerance for time heating setpoint not met',
                                       {'name': u'Tolerance for Time Heating Setpoint Not Met',
                                        'pyname': u'tolerance_for_time_heating_setpoint_not_met',
                                        'default': 0.2,
                                        'maximum': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'tolerance for time cooling setpoint not met',
                                       {'name': u'Tolerance for Time Cooling Setpoint Not Met',
                                        'pyname': u'tolerance_for_time_cooling_setpoint_not_met',
                                        'default': 0.2,
                                        'maximum': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'OutputControl:ReportingTolerances',
               'pyname': u'OutputControlReportingTolerances',
               'required-object': False,
               'unique-object': True}

    @property
    def tolerance_for_time_heating_setpoint_not_met(self):
        """field `Tolerance for Time Heating Setpoint Not Met`

        |  If the zone temperature is below the heating setpoint by more than
        |  this value, the following output variables will increment as appropriate
        |  Zone Heating Setpoint Not Met Time
        |  Zone Heating Setpoint Not Met While Occupied Time
        |  This also impacts table report "Annual Building Utility Performance Summary"
        |  subtable "Comfort and Setpoint Not Met Summary"
        |  Units: deltaC
        |  Default value: 0.2
        |  value <= 10.0

        Args:
            value (float): value for IDD Field `Tolerance for Time Heating Setpoint Not Met`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tolerance_for_time_heating_setpoint_not_met` or None if not set

        """
        return self["Tolerance for Time Heating Setpoint Not Met"]

    @tolerance_for_time_heating_setpoint_not_met.setter
    def tolerance_for_time_heating_setpoint_not_met(self, value=0.2):
        """Corresponds to IDD field `Tolerance for Time Heating Setpoint Not
        Met`"""
        self["Tolerance for Time Heating Setpoint Not Met"] = value

    @property
    def tolerance_for_time_cooling_setpoint_not_met(self):
        """field `Tolerance for Time Cooling Setpoint Not Met`

        |  If the zone temperature is above the cooling setpoint by more than
        |  this value, the following output variables will increment as appropriate
        |  Zone Cooling Setpoint Not Met Time
        |  Zone Cooling Setpoint Not Met While Occupied Time
        |  This also impacts table report "Annual Building Utility Performance Summary"
        |  subtable "Comfort and Setpoint Not Met Summary"
        |  Units: deltaC
        |  Default value: 0.2
        |  value <= 10.0

        Args:
            value (float): value for IDD Field `Tolerance for Time Cooling Setpoint Not Met`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tolerance_for_time_cooling_setpoint_not_met` or None if not set

        """
        return self["Tolerance for Time Cooling Setpoint Not Met"]

    @tolerance_for_time_cooling_setpoint_not_met.setter
    def tolerance_for_time_cooling_setpoint_not_met(self, value=0.2):
        """Corresponds to IDD field `Tolerance for Time Cooling Setpoint Not
        Met`"""
        self["Tolerance for Time Cooling Setpoint Not Met"] = value




class OutputVariable(DataObject):

    """ Corresponds to IDD object `Output:Variable`
        each Output:Variable command picks variables to be put onto the standard output file (.eso)
        some variables may not be reported for every simulation.
        a list of variables that can be reported are available after a run on
        the report dictionary file (.rdd) if the Output:VariableDictionary has been requested.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'key value',
                                       {'name': u'Key Value',
                                        'pyname': u'key_value',
                                        'default': u'*',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'variable name',
                                       {'name': u'Variable Name',
                                        'pyname': u'variable_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'reporting frequency',
                                       {'name': u'Reporting Frequency',
                                        'pyname': u'reporting_frequency',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Detailed',
                                                            u'Timestep',
                                                            u'Hourly',
                                                            u'Daily',
                                                            u'Monthly',
                                                            u'RunPeriod',
                                                            u'Environment',
                                                            u'Annual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Variable',
               'pyname': u'OutputVariable',
               'required-object': False,
               'unique-object': False}

    @property
    def key_value(self):
        """field `Key Value`

        |  use '*' (without quotes) to apply this variable to all keys
        |  Default value: *

        Args:
            value (str): value for IDD Field `Key Value`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `key_value` or None if not set

        """
        return self["Key Value"]

    @key_value.setter
    def key_value(self, value="*"):
        """Corresponds to IDD field `Key Value`"""
        self["Key Value"] = value

    @property
    def variable_name(self):
        """field `Variable Name`

        Args:
            value (str): value for IDD Field `Variable Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `variable_name` or None if not set

        """
        return self["Variable Name"]

    @variable_name.setter
    def variable_name(self, value=None):
        """Corresponds to IDD field `Variable Name`"""
        self["Variable Name"] = value

    @property
    def reporting_frequency(self):
        """field `Reporting Frequency`

        |  Detailed lists every instance (i.e. HVAC variable timesteps)
        |  Timestep refers to the zone Timestep/Number of Timesteps in hour value
        |  RunPeriod, Environment, and Annual are the same
        |  RunPeriod, Environment, and Annual are synonymous
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Reporting Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reporting_frequency` or None if not set

        """
        return self["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """Corresponds to IDD field `Reporting Frequency`"""
        self["Reporting Frequency"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value




class OutputMeter(DataObject):

    """ Corresponds to IDD object `Output:Meter`
        Each Output:Meter command picks meters to be put onto the standard output file (.eso) and
        meter file (.mtr). Not all meters are reported in every simulation. A list of
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'reporting frequency',
                                       {'name': u'Reporting Frequency',
                                        'pyname': u'reporting_frequency',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timestep',
                                                            u'Hourly',
                                                            u'Daily',
                                                            u'Monthly',
                                                            u'RunPeriod',
                                                            u'Environment',
                                                            u'Annual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Meter',
               'pyname': u'OutputMeter',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        |  or EndUse:..., e.g. GeneralLights:* for all General Lights
        |  Output:Meter puts results on both the eplusout.mtr and eplusout.eso files

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def reporting_frequency(self):
        """field `Reporting Frequency`

        |  Timestep refers to the zone Timestep/Number of Timesteps in hour value
        |  RunPeriod, Environment, and Annual are the same
        |  RunPeriod, Environment, and Annual are synonymous
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Reporting Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reporting_frequency` or None if not set

        """
        return self["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """Corresponds to IDD field `Reporting Frequency`"""
        self["Reporting Frequency"] = value




class OutputMeterMeterFileOnly(DataObject):

    """ Corresponds to IDD object `Output:Meter:MeterFileOnly`
        Each Output:Meter:MeterFileOnly command picks meters to be put only onto meter file (.mtr).
        Not all meters are reported in every simulation. A list of meters that can be reported
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'reporting frequency',
                                       {'name': u'Reporting Frequency',
                                        'pyname': u'reporting_frequency',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timestep',
                                                            u'Hourly',
                                                            u'Daily',
                                                            u'Monthly',
                                                            u'RunPeriod',
                                                            u'Environment',
                                                            u'Annual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Meter:MeterFileOnly',
               'pyname': u'OutputMeterMeterFileOnly',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        |  or EndUse:..., e.g. GeneralLights:* for all General Lights
        |  Output:Meter:MeterFileOnly puts results on the eplusout.mtr file only

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def reporting_frequency(self):
        """field `Reporting Frequency`

        |  Timestep refers to the zone Timestep/Number of Timesteps in hour value
        |  RunPeriod, Environment, and Annual are the same
        |  RunPeriod, Environment, and Annual are synonymous
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Reporting Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reporting_frequency` or None if not set

        """
        return self["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """Corresponds to IDD field `Reporting Frequency`"""
        self["Reporting Frequency"] = value




class OutputMeterCumulative(DataObject):

    """ Corresponds to IDD object `Output:Meter:Cumulative`
        Each Output:Meter:Cumulative command picks meters to be reported cumulatively onto the
        standard output file (.eso) and meter file (.mtr). Not all meters are reported in every
        simulation.
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'reporting frequency',
                                       {'name': u'Reporting Frequency',
                                        'pyname': u'reporting_frequency',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timestep',
                                                            u'Hourly',
                                                            u'Daily',
                                                            u'Monthly',
                                                            u'RunPeriod',
                                                            u'Environment',
                                                            u'Annual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Meter:Cumulative',
               'pyname': u'OutputMeterCumulative',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        |  or EndUse:..., e.g. GeneralLights:* for all General Lights
        |  Output:Meter:Cumulative puts results on both the eplusout.mtr and eplusout.eso files

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def reporting_frequency(self):
        """field `Reporting Frequency`

        |  Timestep refers to the zone Timestep/Number of Timesteps in hour value
        |  RunPeriod, Environment, and Annual are the same
        |  RunPeriod, Environment, and Annual are synonymous
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Reporting Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reporting_frequency` or None if not set

        """
        return self["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """Corresponds to IDD field `Reporting Frequency`"""
        self["Reporting Frequency"] = value




class OutputMeterCumulativeMeterFileOnly(DataObject):

    """ Corresponds to IDD object `Output:Meter:Cumulative:MeterFileOnly`
        Each Output:Meter:Cumulative:MeterFileOnly command picks meters to be reported cumulatively
        onto the standard output file (.eso) and meter file (.mtr). Not all meters are reported in
        every simulation.
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'external-list'}),
                                      (u'reporting frequency',
                                       {'name': u'Reporting Frequency',
                                        'pyname': u'reporting_frequency',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timestep',
                                                            u'Hourly',
                                                            u'Daily',
                                                            u'Monthly',
                                                            u'RunPeriod',
                                                            u'Environment',
                                                            u'Annual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Meter:Cumulative:MeterFileOnly',
               'pyname': u'OutputMeterCumulativeMeterFileOnly',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        |  or EndUse:..., e.g. GeneralLights:* for all General Lights
        |  Output:Meter:Cumulative:MeterFileOnly puts results on the eplusout.mtr file only

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def reporting_frequency(self):
        """field `Reporting Frequency`

        |  Timestep refers to the zone Timestep/Number of Timesteps in hour value
        |  RunPeriod, Environment, and Annual are the same
        |  RunPeriod, Environment, and Annual are synonymous
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Reporting Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reporting_frequency` or None if not set

        """
        return self["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """Corresponds to IDD field `Reporting Frequency`"""
        self["Reporting Frequency"] = value




class MeterCustom(DataObject):

    """ Corresponds to IDD object `Meter:Custom`
        Used to allow users to combine specific variables and/or meters into
        "custom" meter configurations. To access these meters by name, one must
        first run a simulation to generate the RDD/MDD files and names.
    """
    _schema = {'extensible-fields': OrderedDict([(u'key name 1',
                                                  {'name': u'Key Name 1',
                                                   'pyname': u'key_name_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha'}),
                                                 (u'output variable or meter name 1',
                                                  {'name': u'Output Variable or Meter Name 1',
                                                   'pyname': u'output_variable_or_meter_name_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fuel type',
                                       {'name': u'Fuel Type',
                                        'pyname': u'fuel_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'Water',
                                                            u'Generic',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Meter:Custom',
               'pyname': u'MeterCustom',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def fuel_type(self):
        """field `Fuel Type`

        Args:
            value (str): value for IDD Field `Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fuel_type` or None if not set

        """
        return self["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """Corresponds to IDD field `Fuel Type`"""
        self["Fuel Type"] = value

    def add_extensible(self,
                       key_name_1=None,
                       output_variable_or_meter_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            key_name_1 (str): value for IDD Field `Key Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_variable_or_meter_name_1 (str): value for IDD Field `Output Variable or Meter Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        key_name_1 = self.check_value("Key Name 1", key_name_1)
        vals.append(key_name_1)
        output_variable_or_meter_name_1 = self.check_value(
            "Output Variable or Meter Name 1",
            output_variable_or_meter_name_1)
        vals.append(output_variable_or_meter_name_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class MeterCustomDecrement(DataObject):

    """ Corresponds to IDD object `Meter:CustomDecrement`
        Used to allow users to combine specific variables and/or meters into
        "custom" meter configurations. To access these meters by name, one must
        first run a simulation to generate the RDD/MDD files and names.
    """
    _schema = {'extensible-fields': OrderedDict([(u'key name 1',
                                                  {'name': u'Key Name 1',
                                                   'pyname': u'key_name_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha'}),
                                                 (u'output variable or meter name 1',
                                                  {'name': u'Output Variable or Meter Name 1',
                                                   'pyname': u'output_variable_or_meter_name_1',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fuel type',
                                       {'name': u'Fuel Type',
                                        'pyname': u'fuel_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'Water',
                                                            u'Generic',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'source meter name',
                                       {'name': u'Source Meter Name',
                                        'pyname': u'source_meter_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Meter:CustomDecrement',
               'pyname': u'MeterCustomDecrement',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def fuel_type(self):
        """field `Fuel Type`

        Args:
            value (str): value for IDD Field `Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fuel_type` or None if not set

        """
        return self["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """Corresponds to IDD field `Fuel Type`"""
        self["Fuel Type"] = value

    @property
    def source_meter_name(self):
        """field `Source Meter Name`

        Args:
            value (str): value for IDD Field `Source Meter Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_meter_name` or None if not set

        """
        return self["Source Meter Name"]

    @source_meter_name.setter
    def source_meter_name(self, value=None):
        """Corresponds to IDD field `Source Meter Name`"""
        self["Source Meter Name"] = value

    def add_extensible(self,
                       key_name_1=None,
                       output_variable_or_meter_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            key_name_1 (str): value for IDD Field `Key Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_variable_or_meter_name_1 (str): value for IDD Field `Output Variable or Meter Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        key_name_1 = self.check_value("Key Name 1", key_name_1)
        vals.append(key_name_1)
        output_variable_or_meter_name_1 = self.check_value(
            "Output Variable or Meter Name 1",
            output_variable_or_meter_name_1)
        vals.append(output_variable_or_meter_name_1)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class OutputSqlite(DataObject):

    """ Corresponds to IDD object `Output:SQLite`
        Output from EnergyPlus can be written to an SQLite format file.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'option type',
                                       {'name': u'Option Type',
                                        'pyname': u'option_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Simple',
                                                            u'SimpleAndTabular'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:SQLite',
               'pyname': u'OutputSqlite',
               'required-object': False,
               'unique-object': True}

    @property
    def option_type(self):
        """field `Option Type`

        Args:
            value (str): value for IDD Field `Option Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `option_type` or None if not set

        """
        return self["Option Type"]

    @option_type.setter
    def option_type(self, value=None):
        """Corresponds to IDD field `Option Type`"""
        self["Option Type"] = value




class OutputEnvironmentalImpactFactors(DataObject):

    """ Corresponds to IDD object `Output:EnvironmentalImpactFactors`
        This is used to Automatically report the facility meters and turn on the Environmental Impact Report calculations
        for all of the Environmental Factors.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'reporting frequency',
                                       {'name': u'Reporting Frequency',
                                        'pyname': u'reporting_frequency',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timestep',
                                                            u'Hourly',
                                                            u'Daily',
                                                            u'Monthly',
                                                            u'RunPeriod'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:EnvironmentalImpactFactors',
               'pyname': u'OutputEnvironmentalImpactFactors',
               'required-object': False,
               'unique-object': False}

    @property
    def reporting_frequency(self):
        """field `Reporting Frequency`

        Args:
            value (str): value for IDD Field `Reporting Frequency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reporting_frequency` or None if not set

        """
        return self["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value=None):
        """Corresponds to IDD field `Reporting Frequency`"""
        self["Reporting Frequency"] = value




class EnvironmentalImpactFactors(DataObject):

    """ Corresponds to IDD object `EnvironmentalImpactFactors`
        Used to help convert district and ideal energy use to a fuel type and provide total carbon equivalent with coefficients
        Also used in Source=>Site conversions.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'district heating efficiency',
                                       {'name': u'District Heating Efficiency',
                                        'pyname': u'district_heating_efficiency',
                                        'default': 0.3,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'district cooling cop',
                                       {'name': u'District Cooling COP',
                                        'pyname': u'district_cooling_cop',
                                        'default': 3.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W/W'}),
                                      (u'steam conversion efficiency',
                                       {'name': u'Steam Conversion Efficiency',
                                        'pyname': u'steam_conversion_efficiency',
                                        'default': 0.25,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'total carbon equivalent emission factor from n2o',
                                       {'name': u'Total Carbon Equivalent Emission Factor From N2O',
                                        'pyname': u'total_carbon_equivalent_emission_factor_from_n2o',
                                        'default': 80.7272,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/kg'}),
                                      (u'total carbon equivalent emission factor from ch4',
                                       {'name': u'Total Carbon Equivalent Emission Factor From CH4',
                                        'pyname': u'total_carbon_equivalent_emission_factor_from_ch4',
                                        'default': 6.2727,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/kg'}),
                                      (u'total carbon equivalent emission factor from co2',
                                       {'name': u'Total Carbon Equivalent Emission Factor From CO2',
                                        'pyname': u'total_carbon_equivalent_emission_factor_from_co2',
                                        'default': 0.2727,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'kg/kg'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'EnvironmentalImpactFactors',
               'pyname': u'EnvironmentalImpactFactors',
               'required-object': False,
               'unique-object': False}

    @property
    def district_heating_efficiency(self):
        """field `District Heating Efficiency`

        |  District heating efficiency used when converted to natural gas
        |  Default value: 0.3

        Args:
            value (float): value for IDD Field `District Heating Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `district_heating_efficiency` or None if not set

        """
        return self["District Heating Efficiency"]

    @district_heating_efficiency.setter
    def district_heating_efficiency(self, value=0.3):
        """Corresponds to IDD field `District Heating Efficiency`"""
        self["District Heating Efficiency"] = value

    @property
    def district_cooling_cop(self):
        """field `District Cooling COP`

        |  District cooling COP used when converted to electricity
        |  Units: W/W
        |  Default value: 3.0

        Args:
            value (float): value for IDD Field `District Cooling COP`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `district_cooling_cop` or None if not set

        """
        return self["District Cooling COP"]

    @district_cooling_cop.setter
    def district_cooling_cop(self, value=3.0):
        """Corresponds to IDD field `District Cooling COP`"""
        self["District Cooling COP"] = value

    @property
    def steam_conversion_efficiency(self):
        """field `Steam Conversion Efficiency`

        |  Steam conversion efficiency used to convert steam usage to natural gas
        |  Default value: 0.25

        Args:
            value (float): value for IDD Field `Steam Conversion Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `steam_conversion_efficiency` or None if not set

        """
        return self["Steam Conversion Efficiency"]

    @steam_conversion_efficiency.setter
    def steam_conversion_efficiency(self, value=0.25):
        """Corresponds to IDD field `Steam Conversion Efficiency`"""
        self["Steam Conversion Efficiency"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_n2o(self):
        """field `Total Carbon Equivalent Emission Factor From N2O`

        |  Units: kg/kg
        |  Default value: 80.7272

        Args:
            value (float): value for IDD Field `Total Carbon Equivalent Emission Factor From N2O`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_n2o` or None if not set

        """
        return self["Total Carbon Equivalent Emission Factor From N2O"]

    @total_carbon_equivalent_emission_factor_from_n2o.setter
    def total_carbon_equivalent_emission_factor_from_n2o(self, value=80.7272):
        """Corresponds to IDD field `Total Carbon Equivalent Emission Factor
        From N2O`"""
        self["Total Carbon Equivalent Emission Factor From N2O"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_ch4(self):
        """field `Total Carbon Equivalent Emission Factor From CH4`

        |  Units: kg/kg
        |  Default value: 6.2727

        Args:
            value (float): value for IDD Field `Total Carbon Equivalent Emission Factor From CH4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_ch4` or None if not set

        """
        return self["Total Carbon Equivalent Emission Factor From CH4"]

    @total_carbon_equivalent_emission_factor_from_ch4.setter
    def total_carbon_equivalent_emission_factor_from_ch4(self, value=6.2727):
        """Corresponds to IDD field `Total Carbon Equivalent Emission Factor
        From CH4`"""
        self["Total Carbon Equivalent Emission Factor From CH4"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_co2(self):
        """field `Total Carbon Equivalent Emission Factor From CO2`

        |  Units: kg/kg
        |  Default value: 0.2727

        Args:
            value (float): value for IDD Field `Total Carbon Equivalent Emission Factor From CO2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_co2` or None if not set

        """
        return self["Total Carbon Equivalent Emission Factor From CO2"]

    @total_carbon_equivalent_emission_factor_from_co2.setter
    def total_carbon_equivalent_emission_factor_from_co2(self, value=0.2727):
        """Corresponds to IDD field `Total Carbon Equivalent Emission Factor
        From CO2`"""
        self["Total Carbon Equivalent Emission Factor From CO2"] = value




class FuelFactors(DataObject):

    """ Corresponds to IDD object `FuelFactors`
        Provides Fuel Factors for Emissions as well as Source=>Site conversions.
        OtherFuel1, OtherFuel2 provide options for users who want to create and use
        fuels that may not be mainstream (biomass, wood, pellets).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'existing fuel resource name',
                                       {'name': u'Existing Fuel Resource Name',
                                        'pyname': u'existing_fuel_resource_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Gasoline',
                                                            u'Propane',
                                                            u'Diesel',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'units of measure',
                                       {'name': u'Units of Measure',
                                        'pyname': u'units_of_measure',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'energy per unit factor',
                                       {'name': u'Energy per Unit Factor',
                                        'pyname': u'energy_per_unit_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'source energy factor',
                                       {'name': u'Source Energy Factor',
                                        'pyname': u'source_energy_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'J/J'}),
                                      (u'source energy schedule name',
                                       {'name': u'Source Energy Schedule Name',
                                        'pyname': u'source_energy_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'co2 emission factor',
                                       {'name': u'CO2 Emission Factor',
                                        'pyname': u'co2_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'co2 emission factor schedule name',
                                       {'name': u'CO2 Emission Factor Schedule Name',
                                        'pyname': u'co2_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'co emission factor',
                                       {'name': u'CO Emission Factor',
                                        'pyname': u'co_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'co emission factor schedule name',
                                       {'name': u'CO Emission Factor Schedule Name',
                                        'pyname': u'co_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ch4 emission factor',
                                       {'name': u'CH4 Emission Factor',
                                        'pyname': u'ch4_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'ch4 emission factor schedule name',
                                       {'name': u'CH4 Emission Factor Schedule Name',
                                        'pyname': u'ch4_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nox emission factor',
                                       {'name': u'NOx Emission Factor',
                                        'pyname': u'nox_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'nox emission factor schedule name',
                                       {'name': u'NOx Emission Factor Schedule Name',
                                        'pyname': u'nox_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'n2o emission factor',
                                       {'name': u'N2O Emission Factor',
                                        'pyname': u'n2o_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'n2o emission factor schedule name',
                                       {'name': u'N2O Emission Factor Schedule Name',
                                        'pyname': u'n2o_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'so2 emission factor',
                                       {'name': u'SO2 Emission Factor',
                                        'pyname': u'so2_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'so2 emission factor schedule name',
                                       {'name': u'SO2 Emission Factor Schedule Name',
                                        'pyname': u'so2_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pm emission factor',
                                       {'name': u'PM Emission Factor',
                                        'pyname': u'pm_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'pm emission factor schedule name',
                                       {'name': u'PM Emission Factor Schedule Name',
                                        'pyname': u'pm_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pm10 emission factor',
                                       {'name': u'PM10 Emission Factor',
                                        'pyname': u'pm10_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'pm10 emission factor schedule name',
                                       {'name': u'PM10 Emission Factor Schedule Name',
                                        'pyname': u'pm10_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pm2.5 emission factor',
                                       {'name': u'PM2.5 Emission Factor',
                                        'pyname': u'pm2_5_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'pm2.5 emission factor schedule name',
                                       {'name': u'PM2.5 Emission Factor Schedule Name',
                                        'pyname': u'pm2_5_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nh3 emission factor',
                                       {'name': u'NH3 Emission Factor',
                                        'pyname': u'nh3_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'nh3 emission factor schedule name',
                                       {'name': u'NH3 Emission Factor Schedule Name',
                                        'pyname': u'nh3_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nmvoc emission factor',
                                       {'name': u'NMVOC Emission Factor',
                                        'pyname': u'nmvoc_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'nmvoc emission factor schedule name',
                                       {'name': u'NMVOC Emission Factor Schedule Name',
                                        'pyname': u'nmvoc_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'hg emission factor',
                                       {'name': u'Hg Emission Factor',
                                        'pyname': u'hg_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'hg emission factor schedule name',
                                       {'name': u'Hg Emission Factor Schedule Name',
                                        'pyname': u'hg_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'pb emission factor',
                                       {'name': u'Pb Emission Factor',
                                        'pyname': u'pb_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'pb emission factor schedule name',
                                       {'name': u'Pb Emission Factor Schedule Name',
                                        'pyname': u'pb_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'water emission factor',
                                       {'name': u'Water Emission Factor',
                                        'pyname': u'water_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'L/MJ'}),
                                      (u'water emission factor schedule name',
                                       {'name': u'Water Emission Factor Schedule Name',
                                        'pyname': u'water_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nuclear high level emission factor',
                                       {'name': u'Nuclear High Level Emission Factor',
                                        'pyname': u'nuclear_high_level_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'g/MJ'}),
                                      (u'nuclear high level emission factor schedule name',
                                       {'name': u'Nuclear High Level Emission Factor Schedule Name',
                                        'pyname': u'nuclear_high_level_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nuclear low level emission factor',
                                       {'name': u'Nuclear Low Level Emission Factor',
                                        'pyname': u'nuclear_low_level_emission_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/MJ'}),
                                      (u'nuclear low level emission factor schedule name',
                                       {'name': u'Nuclear Low Level Emission Factor Schedule Name',
                                        'pyname': u'nuclear_low_level_emission_factor_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'FuelFactors',
               'pyname': u'FuelFactors',
               'required-object': False,
               'unique-object': False}

    @property
    def existing_fuel_resource_name(self):
        """field `Existing Fuel Resource Name`

        Args:
            value (str): value for IDD Field `Existing Fuel Resource Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `existing_fuel_resource_name` or None if not set

        """
        return self["Existing Fuel Resource Name"]

    @existing_fuel_resource_name.setter
    def existing_fuel_resource_name(self, value=None):
        """Corresponds to IDD field `Existing Fuel Resource Name`"""
        self["Existing Fuel Resource Name"] = value

    @property
    def units_of_measure(self):
        """field `Units of Measure`

        Args:
            value (str): value for IDD Field `Units of Measure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `units_of_measure` or None if not set

        """
        return self["Units of Measure"]

    @units_of_measure.setter
    def units_of_measure(self, value=None):
        """Corresponds to IDD field `Units of Measure`"""
        self["Units of Measure"] = value

    @property
    def energy_per_unit_factor(self):
        """field `Energy per Unit Factor`

        Args:
            value (float): value for IDD Field `Energy per Unit Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `energy_per_unit_factor` or None if not set

        """
        return self["Energy per Unit Factor"]

    @energy_per_unit_factor.setter
    def energy_per_unit_factor(self, value=None):
        """Corresponds to IDD field `Energy per Unit Factor`"""
        self["Energy per Unit Factor"] = value

    @property
    def source_energy_factor(self):
        """field `Source Energy Factor`

        |  Units: J/J

        Args:
            value (float): value for IDD Field `Source Energy Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_energy_factor` or None if not set

        """
        return self["Source Energy Factor"]

    @source_energy_factor.setter
    def source_energy_factor(self, value=None):
        """Corresponds to IDD field `Source Energy Factor`"""
        self["Source Energy Factor"] = value

    @property
    def source_energy_schedule_name(self):
        """field `Source Energy Schedule Name`

        Args:
            value (str): value for IDD Field `Source Energy Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_energy_schedule_name` or None if not set

        """
        return self["Source Energy Schedule Name"]

    @source_energy_schedule_name.setter
    def source_energy_schedule_name(self, value=None):
        """Corresponds to IDD field `Source Energy Schedule Name`"""
        self["Source Energy Schedule Name"] = value

    @property
    def co2_emission_factor(self):
        """field `CO2 Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `CO2 Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `co2_emission_factor` or None if not set

        """
        return self["CO2 Emission Factor"]

    @co2_emission_factor.setter
    def co2_emission_factor(self, value=None):
        """Corresponds to IDD field `CO2 Emission Factor`"""
        self["CO2 Emission Factor"] = value

    @property
    def co2_emission_factor_schedule_name(self):
        """field `CO2 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `CO2 Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `co2_emission_factor_schedule_name` or None if not set

        """
        return self["CO2 Emission Factor Schedule Name"]

    @co2_emission_factor_schedule_name.setter
    def co2_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `CO2 Emission Factor Schedule Name`"""
        self["CO2 Emission Factor Schedule Name"] = value

    @property
    def co_emission_factor(self):
        """field `CO Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `CO Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `co_emission_factor` or None if not set

        """
        return self["CO Emission Factor"]

    @co_emission_factor.setter
    def co_emission_factor(self, value=None):
        """Corresponds to IDD field `CO Emission Factor`"""
        self["CO Emission Factor"] = value

    @property
    def co_emission_factor_schedule_name(self):
        """field `CO Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `CO Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `co_emission_factor_schedule_name` or None if not set

        """
        return self["CO Emission Factor Schedule Name"]

    @co_emission_factor_schedule_name.setter
    def co_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `CO Emission Factor Schedule Name`"""
        self["CO Emission Factor Schedule Name"] = value

    @property
    def ch4_emission_factor(self):
        """field `CH4 Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `CH4 Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ch4_emission_factor` or None if not set

        """
        return self["CH4 Emission Factor"]

    @ch4_emission_factor.setter
    def ch4_emission_factor(self, value=None):
        """Corresponds to IDD field `CH4 Emission Factor`"""
        self["CH4 Emission Factor"] = value

    @property
    def ch4_emission_factor_schedule_name(self):
        """field `CH4 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `CH4 Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ch4_emission_factor_schedule_name` or None if not set

        """
        return self["CH4 Emission Factor Schedule Name"]

    @ch4_emission_factor_schedule_name.setter
    def ch4_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `CH4 Emission Factor Schedule Name`"""
        self["CH4 Emission Factor Schedule Name"] = value

    @property
    def nox_emission_factor(self):
        """field `NOx Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `NOx Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nox_emission_factor` or None if not set

        """
        return self["NOx Emission Factor"]

    @nox_emission_factor.setter
    def nox_emission_factor(self, value=None):
        """Corresponds to IDD field `NOx Emission Factor`"""
        self["NOx Emission Factor"] = value

    @property
    def nox_emission_factor_schedule_name(self):
        """field `NOx Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `NOx Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `nox_emission_factor_schedule_name` or None if not set

        """
        return self["NOx Emission Factor Schedule Name"]

    @nox_emission_factor_schedule_name.setter
    def nox_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `NOx Emission Factor Schedule Name`"""
        self["NOx Emission Factor Schedule Name"] = value

    @property
    def n2o_emission_factor(self):
        """field `N2O Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `N2O Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `n2o_emission_factor` or None if not set

        """
        return self["N2O Emission Factor"]

    @n2o_emission_factor.setter
    def n2o_emission_factor(self, value=None):
        """Corresponds to IDD field `N2O Emission Factor`"""
        self["N2O Emission Factor"] = value

    @property
    def n2o_emission_factor_schedule_name(self):
        """field `N2O Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `N2O Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `n2o_emission_factor_schedule_name` or None if not set

        """
        return self["N2O Emission Factor Schedule Name"]

    @n2o_emission_factor_schedule_name.setter
    def n2o_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `N2O Emission Factor Schedule Name`"""
        self["N2O Emission Factor Schedule Name"] = value

    @property
    def so2_emission_factor(self):
        """field `SO2 Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `SO2 Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `so2_emission_factor` or None if not set

        """
        return self["SO2 Emission Factor"]

    @so2_emission_factor.setter
    def so2_emission_factor(self, value=None):
        """Corresponds to IDD field `SO2 Emission Factor`"""
        self["SO2 Emission Factor"] = value

    @property
    def so2_emission_factor_schedule_name(self):
        """field `SO2 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `SO2 Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `so2_emission_factor_schedule_name` or None if not set

        """
        return self["SO2 Emission Factor Schedule Name"]

    @so2_emission_factor_schedule_name.setter
    def so2_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `SO2 Emission Factor Schedule Name`"""
        self["SO2 Emission Factor Schedule Name"] = value

    @property
    def pm_emission_factor(self):
        """field `PM Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `PM Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pm_emission_factor` or None if not set

        """
        return self["PM Emission Factor"]

    @pm_emission_factor.setter
    def pm_emission_factor(self, value=None):
        """Corresponds to IDD field `PM Emission Factor`"""
        self["PM Emission Factor"] = value

    @property
    def pm_emission_factor_schedule_name(self):
        """field `PM Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `PM Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pm_emission_factor_schedule_name` or None if not set

        """
        return self["PM Emission Factor Schedule Name"]

    @pm_emission_factor_schedule_name.setter
    def pm_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `PM Emission Factor Schedule Name`"""
        self["PM Emission Factor Schedule Name"] = value

    @property
    def pm10_emission_factor(self):
        """field `PM10 Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `PM10 Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pm10_emission_factor` or None if not set

        """
        return self["PM10 Emission Factor"]

    @pm10_emission_factor.setter
    def pm10_emission_factor(self, value=None):
        """Corresponds to IDD field `PM10 Emission Factor`"""
        self["PM10 Emission Factor"] = value

    @property
    def pm10_emission_factor_schedule_name(self):
        """field `PM10 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `PM10 Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pm10_emission_factor_schedule_name` or None if not set

        """
        return self["PM10 Emission Factor Schedule Name"]

    @pm10_emission_factor_schedule_name.setter
    def pm10_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `PM10 Emission Factor Schedule Name`"""
        self["PM10 Emission Factor Schedule Name"] = value

    @property
    def pm2_5_emission_factor(self):
        """field `PM2.5 Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `PM2.5 Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pm2_5_emission_factor` or None if not set
        """
        return self["PM2.5 Emission Factor"]

    @pm2_5_emission_factor.setter
    def pm2_5_emission_factor(self, value=None):
        """  Corresponds to IDD field `PM2.5 Emission Factor`

        """
        self["PM2.5 Emission Factor"] = value

    @property
    def pm2_5_emission_factor_schedule_name(self):
        """field `PM2.5 Emission Factor Schedule Name`


        Args:
            value (str): value for IDD Field `PM2.5 Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pm2_5_emission_factor_schedule_name` or None if not set
        """
        return self["PM2.5 Emission Factor Schedule Name"]

    @pm2_5_emission_factor_schedule_name.setter
    def pm2_5_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD field `PM2.5 Emission Factor Schedule Name`

        """
        self["PM2.5 Emission Factor Schedule Name"] = value

    @property
    def nh3_emission_factor(self):
        """field `NH3 Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `NH3 Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nh3_emission_factor` or None if not set

        """
        return self["NH3 Emission Factor"]

    @nh3_emission_factor.setter
    def nh3_emission_factor(self, value=None):
        """Corresponds to IDD field `NH3 Emission Factor`"""
        self["NH3 Emission Factor"] = value

    @property
    def nh3_emission_factor_schedule_name(self):
        """field `NH3 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `NH3 Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `nh3_emission_factor_schedule_name` or None if not set

        """
        return self["NH3 Emission Factor Schedule Name"]

    @nh3_emission_factor_schedule_name.setter
    def nh3_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `NH3 Emission Factor Schedule Name`"""
        self["NH3 Emission Factor Schedule Name"] = value

    @property
    def nmvoc_emission_factor(self):
        """field `NMVOC Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `NMVOC Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nmvoc_emission_factor` or None if not set

        """
        return self["NMVOC Emission Factor"]

    @nmvoc_emission_factor.setter
    def nmvoc_emission_factor(self, value=None):
        """Corresponds to IDD field `NMVOC Emission Factor`"""
        self["NMVOC Emission Factor"] = value

    @property
    def nmvoc_emission_factor_schedule_name(self):
        """field `NMVOC Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `NMVOC Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `nmvoc_emission_factor_schedule_name` or None if not set

        """
        return self["NMVOC Emission Factor Schedule Name"]

    @nmvoc_emission_factor_schedule_name.setter
    def nmvoc_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `NMVOC Emission Factor Schedule Name`"""
        self["NMVOC Emission Factor Schedule Name"] = value

    @property
    def hg_emission_factor(self):
        """field `Hg Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `Hg Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `hg_emission_factor` or None if not set

        """
        return self["Hg Emission Factor"]

    @hg_emission_factor.setter
    def hg_emission_factor(self, value=None):
        """Corresponds to IDD field `Hg Emission Factor`"""
        self["Hg Emission Factor"] = value

    @property
    def hg_emission_factor_schedule_name(self):
        """field `Hg Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Hg Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hg_emission_factor_schedule_name` or None if not set

        """
        return self["Hg Emission Factor Schedule Name"]

    @hg_emission_factor_schedule_name.setter
    def hg_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Hg Emission Factor Schedule Name`"""
        self["Hg Emission Factor Schedule Name"] = value

    @property
    def pb_emission_factor(self):
        """field `Pb Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `Pb Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pb_emission_factor` or None if not set

        """
        return self["Pb Emission Factor"]

    @pb_emission_factor.setter
    def pb_emission_factor(self, value=None):
        """Corresponds to IDD field `Pb Emission Factor`"""
        self["Pb Emission Factor"] = value

    @property
    def pb_emission_factor_schedule_name(self):
        """field `Pb Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Pb Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pb_emission_factor_schedule_name` or None if not set

        """
        return self["Pb Emission Factor Schedule Name"]

    @pb_emission_factor_schedule_name.setter
    def pb_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Pb Emission Factor Schedule Name`"""
        self["Pb Emission Factor Schedule Name"] = value

    @property
    def water_emission_factor(self):
        """field `Water Emission Factor`

        |  Units: L/MJ

        Args:
            value (float): value for IDD Field `Water Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_emission_factor` or None if not set

        """
        return self["Water Emission Factor"]

    @water_emission_factor.setter
    def water_emission_factor(self, value=None):
        """Corresponds to IDD field `Water Emission Factor`"""
        self["Water Emission Factor"] = value

    @property
    def water_emission_factor_schedule_name(self):
        """field `Water Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Water Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_emission_factor_schedule_name` or None if not set

        """
        return self["Water Emission Factor Schedule Name"]

    @water_emission_factor_schedule_name.setter
    def water_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Water Emission Factor Schedule Name`"""
        self["Water Emission Factor Schedule Name"] = value

    @property
    def nuclear_high_level_emission_factor(self):
        """field `Nuclear High Level Emission Factor`

        |  Units: g/MJ

        Args:
            value (float): value for IDD Field `Nuclear High Level Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nuclear_high_level_emission_factor` or None if not set

        """
        return self["Nuclear High Level Emission Factor"]

    @nuclear_high_level_emission_factor.setter
    def nuclear_high_level_emission_factor(self, value=None):
        """Corresponds to IDD field `Nuclear High Level Emission Factor`"""
        self["Nuclear High Level Emission Factor"] = value

    @property
    def nuclear_high_level_emission_factor_schedule_name(self):
        """field `Nuclear High Level Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Nuclear High Level Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `nuclear_high_level_emission_factor_schedule_name` or None if not set

        """
        return self["Nuclear High Level Emission Factor Schedule Name"]

    @nuclear_high_level_emission_factor_schedule_name.setter
    def nuclear_high_level_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Nuclear High Level Emission Factor
        Schedule Name`"""
        self["Nuclear High Level Emission Factor Schedule Name"] = value

    @property
    def nuclear_low_level_emission_factor(self):
        """field `Nuclear Low Level Emission Factor`

        |  Units: m3/MJ

        Args:
            value (float): value for IDD Field `Nuclear Low Level Emission Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nuclear_low_level_emission_factor` or None if not set

        """
        return self["Nuclear Low Level Emission Factor"]

    @nuclear_low_level_emission_factor.setter
    def nuclear_low_level_emission_factor(self, value=None):
        """Corresponds to IDD field `Nuclear Low Level Emission Factor`"""
        self["Nuclear Low Level Emission Factor"] = value

    @property
    def nuclear_low_level_emission_factor_schedule_name(self):
        """field `Nuclear Low Level Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Nuclear Low Level Emission Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `nuclear_low_level_emission_factor_schedule_name` or None if not set

        """
        return self["Nuclear Low Level Emission Factor Schedule Name"]

    @nuclear_low_level_emission_factor_schedule_name.setter
    def nuclear_low_level_emission_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Nuclear Low Level Emission Factor Schedule
        Name`"""
        self["Nuclear Low Level Emission Factor Schedule Name"] = value




class OutputDiagnostics(DataObject):

    """ Corresponds to IDD object `Output:Diagnostics`
        Special keys to produce certain warning messages or effect certain simulation characteristics.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'key 1',
                                       {'name': u'Key 1',
                                        'pyname': u'key_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DisplayAllWarnings',
                                                            u'DisplayExtraWarnings',
                                                            u'DisplayUnusedSchedules',
                                                            u'DisplayUnusedObjects',
                                                            u'DisplayAdvancedReportVariables',
                                                            u'DisplayZoneAirHeatBalanceOffBalance',
                                                            u'DoNotMirrorDetachedShading',
                                                            u'DisplayWeatherMissingDataWarnings',
                                                            u'ReportDuringWarmup',
                                                            u'ReportDetailedWarmupConvergence',
                                                            u'ReportDuringHVACSizingSimulation'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'key 2',
                                       {'name': u'Key 2',
                                        'pyname': u'key_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DisplayAllWarnings',
                                                            u'DisplayExtraWarnings',
                                                            u'DisplayUnusedSchedules',
                                                            u'DisplayUnusedObjects',
                                                            u'DisplayAdvancedReportVariables',
                                                            u'DisplayZoneAirHeatBalanceOffBalance',
                                                            u'DoNotMirrorDetachedShading',
                                                            u'DisplayWeatherMissingDataWarnings',
                                                            u'ReportDuringWarmup',
                                                            u'ReportDetailedWarmupConvergence',
                                                            u'ReportDuringHVACSizingSimulation'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:Diagnostics',
               'pyname': u'OutputDiagnostics',
               'required-object': False,
               'unique-object': False}

    @property
    def key_1(self):
        """field `Key 1`

        Args:
            value (str): value for IDD Field `Key 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `key_1` or None if not set

        """
        return self["Key 1"]

    @key_1.setter
    def key_1(self, value=None):
        """Corresponds to IDD field `Key 1`"""
        self["Key 1"] = value

    @property
    def key_2(self):
        """field `Key 2`

        Args:
            value (str): value for IDD Field `Key 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `key_2` or None if not set

        """
        return self["Key 2"]

    @key_2.setter
    def key_2(self, value=None):
        """Corresponds to IDD field `Key 2`"""
        self["Key 2"] = value




class OutputDebuggingData(DataObject):

    """ Corresponds to IDD object `Output:DebuggingData`
        switch eplusout.dbg file on or off
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'report debugging data',
                                       {'name': u'Report Debugging Data',
                                        'pyname': u'report_debugging_data',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'report during warmup',
                                       {'name': u'Report During Warmup',
                                        'pyname': u'report_during_warmup',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': u'singleline',
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:DebuggingData',
               'pyname': u'OutputDebuggingData',
               'required-object': False,
               'unique-object': True}

    @property
    def report_debugging_data(self):
        """field `Report Debugging Data`

        |  value=1 then yes all others no

        Args:
            value (float): value for IDD Field `Report Debugging Data`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `report_debugging_data` or None if not set

        """
        return self["Report Debugging Data"]

    @report_debugging_data.setter
    def report_debugging_data(self, value=None):
        """Corresponds to IDD field `Report Debugging Data`"""
        self["Report Debugging Data"] = value

    @property
    def report_during_warmup(self):
        """field `Report During Warmup`

        |  value=1 then always even during warmup  all others no

        Args:
            value (float): value for IDD Field `Report During Warmup`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `report_during_warmup` or None if not set

        """
        return self["Report During Warmup"]

    @report_during_warmup.setter
    def report_during_warmup(self, value=None):
        """Corresponds to IDD field `Report During Warmup`"""
        self["Report During Warmup"] = value




class OutputPreprocessorMessage(DataObject):

    """ Corresponds to IDD object `Output:PreprocessorMessage`
        This object does not come from a user input.  This is generated by a pre-processor
        so that various conditions can be gracefully passed on by the InputProcessor.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'preprocessor name',
                                       {'name': u'Preprocessor Name',
                                        'pyname': u'preprocessor_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'error severity',
                                       {'name': u'Error Severity',
                                        'pyname': u'error_severity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Information',
                                                            u'Warning',
                                                            u'Severe',
                                                            u'Fatal'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 1',
                                       {'name': u'Message Line 1',
                                        'pyname': u'message_line_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 2',
                                       {'name': u'Message Line 2',
                                        'pyname': u'message_line_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 3',
                                       {'name': u'Message Line 3',
                                        'pyname': u'message_line_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 4',
                                       {'name': u'Message Line 4',
                                        'pyname': u'message_line_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 5',
                                       {'name': u'Message Line 5',
                                        'pyname': u'message_line_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 6',
                                       {'name': u'Message Line 6',
                                        'pyname': u'message_line_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 7',
                                       {'name': u'Message Line 7',
                                        'pyname': u'message_line_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 8',
                                       {'name': u'Message Line 8',
                                        'pyname': u'message_line_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 9',
                                       {'name': u'Message Line 9',
                                        'pyname': u'message_line_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'message line 10',
                                       {'name': u'Message Line 10',
                                        'pyname': u'message_line_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Output Reporting',
               'min-fields': 0,
               'name': u'Output:PreprocessorMessage',
               'pyname': u'OutputPreprocessorMessage',
               'required-object': False,
               'unique-object': False}

    @property
    def preprocessor_name(self):
        """field `Preprocessor Name`

        Args:
            value (str): value for IDD Field `Preprocessor Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `preprocessor_name` or None if not set

        """
        return self["Preprocessor Name"]

    @preprocessor_name.setter
    def preprocessor_name(self, value=None):
        """Corresponds to IDD field `Preprocessor Name`"""
        self["Preprocessor Name"] = value

    @property
    def error_severity(self):
        """field `Error Severity`

        |  Depending on type, InputProcessor may terminate the program.

        Args:
            value (str): value for IDD Field `Error Severity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `error_severity` or None if not set

        """
        return self["Error Severity"]

    @error_severity.setter
    def error_severity(self, value=None):
        """Corresponds to IDD field `Error Severity`"""
        self["Error Severity"] = value

    @property
    def message_line_1(self):
        """field `Message Line 1`

        Args:
            value (str): value for IDD Field `Message Line 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_1` or None if not set

        """
        return self["Message Line 1"]

    @message_line_1.setter
    def message_line_1(self, value=None):
        """Corresponds to IDD field `Message Line 1`"""
        self["Message Line 1"] = value

    @property
    def message_line_2(self):
        """field `Message Line 2`

        Args:
            value (str): value for IDD Field `Message Line 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_2` or None if not set

        """
        return self["Message Line 2"]

    @message_line_2.setter
    def message_line_2(self, value=None):
        """Corresponds to IDD field `Message Line 2`"""
        self["Message Line 2"] = value

    @property
    def message_line_3(self):
        """field `Message Line 3`

        Args:
            value (str): value for IDD Field `Message Line 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_3` or None if not set

        """
        return self["Message Line 3"]

    @message_line_3.setter
    def message_line_3(self, value=None):
        """Corresponds to IDD field `Message Line 3`"""
        self["Message Line 3"] = value

    @property
    def message_line_4(self):
        """field `Message Line 4`

        Args:
            value (str): value for IDD Field `Message Line 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_4` or None if not set

        """
        return self["Message Line 4"]

    @message_line_4.setter
    def message_line_4(self, value=None):
        """Corresponds to IDD field `Message Line 4`"""
        self["Message Line 4"] = value

    @property
    def message_line_5(self):
        """field `Message Line 5`

        Args:
            value (str): value for IDD Field `Message Line 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_5` or None if not set

        """
        return self["Message Line 5"]

    @message_line_5.setter
    def message_line_5(self, value=None):
        """Corresponds to IDD field `Message Line 5`"""
        self["Message Line 5"] = value

    @property
    def message_line_6(self):
        """field `Message Line 6`

        Args:
            value (str): value for IDD Field `Message Line 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_6` or None if not set

        """
        return self["Message Line 6"]

    @message_line_6.setter
    def message_line_6(self, value=None):
        """Corresponds to IDD field `Message Line 6`"""
        self["Message Line 6"] = value

    @property
    def message_line_7(self):
        """field `Message Line 7`

        Args:
            value (str): value for IDD Field `Message Line 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_7` or None if not set

        """
        return self["Message Line 7"]

    @message_line_7.setter
    def message_line_7(self, value=None):
        """Corresponds to IDD field `Message Line 7`"""
        self["Message Line 7"] = value

    @property
    def message_line_8(self):
        """field `Message Line 8`

        Args:
            value (str): value for IDD Field `Message Line 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_8` or None if not set

        """
        return self["Message Line 8"]

    @message_line_8.setter
    def message_line_8(self, value=None):
        """Corresponds to IDD field `Message Line 8`"""
        self["Message Line 8"] = value

    @property
    def message_line_9(self):
        """field `Message Line 9`

        Args:
            value (str): value for IDD Field `Message Line 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_9` or None if not set

        """
        return self["Message Line 9"]

    @message_line_9.setter
    def message_line_9(self, value=None):
        """Corresponds to IDD field `Message Line 9`"""
        self["Message Line 9"] = value

    @property
    def message_line_10(self):
        """field `Message Line 10`

        Args:
            value (str): value for IDD Field `Message Line 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `message_line_10` or None if not set

        """
        return self["Message Line 10"]

    @message_line_10.setter
    def message_line_10(self, value=None):
        """Corresponds to IDD field `Message Line 10`"""
        self["Message Line 10"] = value


