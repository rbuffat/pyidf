from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class OutputVariableDictionary(object):
    """ Corresponds to IDD object `Output:VariableDictionary`
        Produces a list summarizing the output variables and meters that are available for
        reporting for the model being simulated (rdd output file). The list varies depending
        on the types of objects present in the idf file.  For example, variables related to
        lights will only appear if a Lights object is present. The IDF option generates
        complete Output:Variable objects to simplify adding the desired output to the idf file.
    """
    internal_name = "Output:VariableDictionary"
    field_count = 2
    required_fields = ["Key Field"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:VariableDictionary`
        """
        self._data = OrderedDict()
        self._data["Key Field"] = None
        self._data["Sort Option"] = None
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
            self.key_field = None
        else:
            self.key_field = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sort_option = None
        else:
            self.sort_option = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def key_field(self):
        """Get key_field

        Returns:
            str: the value of `key_field` or None if not set
        """
        return self._data["Key Field"]

    @key_field.setter
    def key_field(self, value="regular"):
        """  Corresponds to IDD Field `Key Field`

        Args:
            value (str): value for IDD Field `Key Field`
                Accepted values are:
                      - IDF
                      - regular
                Default value: regular
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputVariableDictionary.key_field`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputVariableDictionary.key_field`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputVariableDictionary.key_field`')
            vals = {}
            vals["idf"] = "IDF"
            vals["regular"] = "regular"
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
                                     'field `OutputVariableDictionary.key_field`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputVariableDictionary.key_field`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Key Field"] = value

    @property
    def sort_option(self):
        """Get sort_option

        Returns:
            str: the value of `sort_option` or None if not set
        """
        return self._data["Sort Option"]

    @sort_option.setter
    def sort_option(self, value=None):
        """  Corresponds to IDD Field `Sort Option`

        Args:
            value (str): value for IDD Field `Sort Option`
                Accepted values are:
                      - Name
                      - Unsorted
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputVariableDictionary.sort_option`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputVariableDictionary.sort_option`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputVariableDictionary.sort_option`')
            vals = {}
            vals["name"] = "Name"
            vals["unsorted"] = "Unsorted"
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
                                     'field `OutputVariableDictionary.sort_option`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputVariableDictionary.sort_option`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Sort Option"] = value

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
                    raise ValueError("Required field OutputVariableDictionary:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputVariableDictionary:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputVariableDictionary: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputVariableDictionary: {} / {}".format(out_fields,
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

class OutputSurfacesList(object):
    """ Corresponds to IDD object `Output:Surfaces:List`
        Produces a report summarizing the details of surfaces in the eio output file.
    """
    internal_name = "Output:Surfaces:List"
    field_count = 2
    required_fields = ["Report Type"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Surfaces:List`
        """
        self._data = OrderedDict()
        self._data["Report Type"] = None
        self._data["Report Specifications"] = None
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
            self.report_type = None
        else:
            self.report_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.report_specifications = None
        else:
            self.report_specifications = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def report_type(self):
        """Get report_type

        Returns:
            str: the value of `report_type` or None if not set
        """
        return self._data["Report Type"]

    @report_type.setter
    def report_type(self, value=None):
        """  Corresponds to IDD Field `Report Type`

        Args:
            value (str): value for IDD Field `Report Type`
                Accepted values are:
                      - Details
                      - Vertices
                      - DetailsWithVertices
                      - ViewFactorInfo
                      - Lines
                      - CostInfo
                      - DecayCurvesfromZoneComponentLoads
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSurfacesList.report_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSurfacesList.report_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSurfacesList.report_type`')
            vals = {}
            vals["details"] = "Details"
            vals["vertices"] = "Vertices"
            vals["detailswithvertices"] = "DetailsWithVertices"
            vals["viewfactorinfo"] = "ViewFactorInfo"
            vals["lines"] = "Lines"
            vals["costinfo"] = "CostInfo"
            vals["decaycurvesfromzonecomponentloads"] = "DecayCurvesfromZoneComponentLoads"
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
                                     'field `OutputSurfacesList.report_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputSurfacesList.report_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Report Type"] = value

    @property
    def report_specifications(self):
        """Get report_specifications

        Returns:
            str: the value of `report_specifications` or None if not set
        """
        return self._data["Report Specifications"]

    @report_specifications.setter
    def report_specifications(self, value=None):
        """  Corresponds to IDD Field `Report Specifications`
        (IDF, only for Output:Surfaces:List, Lines report --
        will print transformed coordinates in IDF style)

        Args:
            value (str): value for IDD Field `Report Specifications`
                Accepted values are:
                      - IDF
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSurfacesList.report_specifications`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSurfacesList.report_specifications`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSurfacesList.report_specifications`')
            vals = {}
            vals["idf"] = "IDF"
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
                                     'field `OutputSurfacesList.report_specifications`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputSurfacesList.report_specifications`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Report Specifications"] = value

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
                    raise ValueError("Required field OutputSurfacesList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputSurfacesList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputSurfacesList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputSurfacesList: {} / {}".format(out_fields,
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

class OutputSurfacesDrawing(object):
    """ Corresponds to IDD object `Output:Surfaces:Drawing`
        Produces reports/files that are capable of rendering graphically or
        being imported into other programs. Rendering does not alter the
        actual inputs/surfaces.
    """
    internal_name = "Output:Surfaces:Drawing"
    field_count = 3
    required_fields = ["Report Type"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Surfaces:Drawing`
        """
        self._data = OrderedDict()
        self._data["Report Type"] = None
        self._data["Report Specifications 1"] = None
        self._data["Report Specifications 2"] = None
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
            self.report_type = None
        else:
            self.report_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.report_specifications_1 = None
        else:
            self.report_specifications_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.report_specifications_2 = None
        else:
            self.report_specifications_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def report_type(self):
        """Get report_type

        Returns:
            str: the value of `report_type` or None if not set
        """
        return self._data["Report Type"]

    @report_type.setter
    def report_type(self, value=None):
        """  Corresponds to IDD Field `Report Type`

        Args:
            value (str): value for IDD Field `Report Type`
                Accepted values are:
                      - DXF
                      - DXF:WireFrame
                      - VRML
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSurfacesDrawing.report_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSurfacesDrawing.report_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSurfacesDrawing.report_type`')
            vals = {}
            vals["dxf"] = "DXF"
            vals["dxf:wireframe"] = "DXF:WireFrame"
            vals["vrml"] = "VRML"
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
                                     'field `OutputSurfacesDrawing.report_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputSurfacesDrawing.report_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Report Type"] = value

    @property
    def report_specifications_1(self):
        """Get report_specifications_1

        Returns:
            str: the value of `report_specifications_1` or None if not set
        """
        return self._data["Report Specifications 1"]

    @report_specifications_1.setter
    def report_specifications_1(self, value="Triangulate3DFace"):
        """  Corresponds to IDD Field `Report Specifications 1`
        Triangulate3DFace (default), ThickPolyline, RegularPolyline apply to DXF
        This field is ignored for DXF:WireFrame and VRML

        Args:
            value (str): value for IDD Field `Report Specifications 1`
                Accepted values are:
                      - Triangulate3DFace
                      - ThickPolyline
                      - RegularPolyline
                Default value: Triangulate3DFace
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSurfacesDrawing.report_specifications_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSurfacesDrawing.report_specifications_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSurfacesDrawing.report_specifications_1`')
            vals = {}
            vals["triangulate3dface"] = "Triangulate3DFace"
            vals["thickpolyline"] = "ThickPolyline"
            vals["regularpolyline"] = "RegularPolyline"
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
                                     'field `OutputSurfacesDrawing.report_specifications_1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputSurfacesDrawing.report_specifications_1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Report Specifications 1"] = value

    @property
    def report_specifications_2(self):
        """Get report_specifications_2

        Returns:
            str: the value of `report_specifications_2` or None if not set
        """
        return self._data["Report Specifications 2"]

    @report_specifications_2.setter
    def report_specifications_2(self, value=None):
        """  Corresponds to IDD Field `Report Specifications 2`
        Use ColorScheme Name for DXF reports

        Args:
            value (str): value for IDD Field `Report Specifications 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSurfacesDrawing.report_specifications_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSurfacesDrawing.report_specifications_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSurfacesDrawing.report_specifications_2`')
        self._data["Report Specifications 2"] = value

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
                    raise ValueError("Required field OutputSurfacesDrawing:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputSurfacesDrawing:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputSurfacesDrawing: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputSurfacesDrawing: {} / {}".format(out_fields,
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

class OutputSchedules(object):
    """ Corresponds to IDD object `Output:Schedules`
        Produces a condensed reporting that illustrates the full range of schedule values in
        the eio output file. In the style of input: DaySchedule,  WeekSchedule, and
        Annual Schedule.
    """
    internal_name = "Output:Schedules"
    field_count = 1
    required_fields = ["Key Field"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Schedules`
        """
        self._data = OrderedDict()
        self._data["Key Field"] = None
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
            self.key_field = None
        else:
            self.key_field = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def key_field(self):
        """Get key_field

        Returns:
            str: the value of `key_field` or None if not set
        """
        return self._data["Key Field"]

    @key_field.setter
    def key_field(self, value=None):
        """  Corresponds to IDD Field `Key Field`

        Args:
            value (str): value for IDD Field `Key Field`
                Accepted values are:
                      - Hourly
                      - Timestep
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSchedules.key_field`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSchedules.key_field`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSchedules.key_field`')
            vals = {}
            vals["hourly"] = "Hourly"
            vals["timestep"] = "Timestep"
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
                                     'field `OutputSchedules.key_field`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputSchedules.key_field`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Key Field"] = value

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
                    raise ValueError("Required field OutputSchedules:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputSchedules:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputSchedules: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputSchedules: {} / {}".format(out_fields,
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

class OutputConstructions(object):
    """ Corresponds to IDD object `Output:Constructions`
        Adds a report to the eio output file which shows details for each construction,
        including overall properties, a list of material layers, and calculated results
        related to conduction transfer functions.
    """
    internal_name = "Output:Constructions"
    field_count = 2
    required_fields = []
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Constructions`
        """
        self._data = OrderedDict()
        self._data["Details Type 1"] = None
        self._data["Details Type 2"] = None
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
            self.details_type_1 = None
        else:
            self.details_type_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.details_type_2 = None
        else:
            self.details_type_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def details_type_1(self):
        """Get details_type_1

        Returns:
            str: the value of `details_type_1` or None if not set
        """
        return self._data["Details Type 1"]

    @details_type_1.setter
    def details_type_1(self, value=None):
        """  Corresponds to IDD Field `Details Type 1`

        Args:
            value (str): value for IDD Field `Details Type 1`
                Accepted values are:
                      - Constructions
                      - Materials
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputConstructions.details_type_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputConstructions.details_type_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputConstructions.details_type_1`')
            vals = {}
            vals["constructions"] = "Constructions"
            vals["materials"] = "Materials"
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
                                     'field `OutputConstructions.details_type_1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputConstructions.details_type_1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Details Type 1"] = value

    @property
    def details_type_2(self):
        """Get details_type_2

        Returns:
            str: the value of `details_type_2` or None if not set
        """
        return self._data["Details Type 2"]

    @details_type_2.setter
    def details_type_2(self, value=None):
        """  Corresponds to IDD Field `Details Type 2`

        Args:
            value (str): value for IDD Field `Details Type 2`
                Accepted values are:
                      - Constructions
                      - Materials
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputConstructions.details_type_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputConstructions.details_type_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputConstructions.details_type_2`')
            vals = {}
            vals["constructions"] = "Constructions"
            vals["materials"] = "Materials"
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
                                     'field `OutputConstructions.details_type_2`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputConstructions.details_type_2`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Details Type 2"] = value

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
                    raise ValueError("Required field OutputConstructions:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputConstructions:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputConstructions: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputConstructions: {} / {}".format(out_fields,
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

class OutputEnergyManagementSystem(object):
    """ Corresponds to IDD object `Output:EnergyManagementSystem`
        This object is used to control the output produced by the Energy Management System
    """
    internal_name = "Output:EnergyManagementSystem"
    field_count = 3
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:EnergyManagementSystem`
        """
        self._data = OrderedDict()
        self._data["Actuator Availability Dictionary Reporting"] = None
        self._data["Internal Variable Availability Dictionary Reporting"] = None
        self._data["EMS Runtime Language Debug Output Level"] = None
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
            self.actuator_availability_dictionary_reporting = None
        else:
            self.actuator_availability_dictionary_reporting = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.internal_variable_availability_dictionary_reporting = None
        else:
            self.internal_variable_availability_dictionary_reporting = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ems_runtime_language_debug_output_level = None
        else:
            self.ems_runtime_language_debug_output_level = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def actuator_availability_dictionary_reporting(self):
        """Get actuator_availability_dictionary_reporting

        Returns:
            str: the value of `actuator_availability_dictionary_reporting` or None if not set
        """
        return self._data["Actuator Availability Dictionary Reporting"]

    @actuator_availability_dictionary_reporting.setter
    def actuator_availability_dictionary_reporting(self, value="None"):
        """  Corresponds to IDD Field `Actuator Availability Dictionary Reporting`

        Args:
            value (str): value for IDD Field `Actuator Availability Dictionary Reporting`
                Accepted values are:
                      - None
                      - NotByUniqueKeyNames
                      - Verbose
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputEnergyManagementSystem.actuator_availability_dictionary_reporting`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputEnergyManagementSystem.actuator_availability_dictionary_reporting`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputEnergyManagementSystem.actuator_availability_dictionary_reporting`')
            vals = {}
            vals["none"] = "None"
            vals["notbyuniquekeynames"] = "NotByUniqueKeyNames"
            vals["verbose"] = "Verbose"
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
                                     'field `OutputEnergyManagementSystem.actuator_availability_dictionary_reporting`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputEnergyManagementSystem.actuator_availability_dictionary_reporting`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Actuator Availability Dictionary Reporting"] = value

    @property
    def internal_variable_availability_dictionary_reporting(self):
        """Get internal_variable_availability_dictionary_reporting

        Returns:
            str: the value of `internal_variable_availability_dictionary_reporting` or None if not set
        """
        return self._data["Internal Variable Availability Dictionary Reporting"]

    @internal_variable_availability_dictionary_reporting.setter
    def internal_variable_availability_dictionary_reporting(self, value="None"):
        """  Corresponds to IDD Field `Internal Variable Availability Dictionary Reporting`

        Args:
            value (str): value for IDD Field `Internal Variable Availability Dictionary Reporting`
                Accepted values are:
                      - None
                      - NotByUniqueKeyNames
                      - Verbose
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputEnergyManagementSystem.internal_variable_availability_dictionary_reporting`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputEnergyManagementSystem.internal_variable_availability_dictionary_reporting`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputEnergyManagementSystem.internal_variable_availability_dictionary_reporting`')
            vals = {}
            vals["none"] = "None"
            vals["notbyuniquekeynames"] = "NotByUniqueKeyNames"
            vals["verbose"] = "Verbose"
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
                                     'field `OutputEnergyManagementSystem.internal_variable_availability_dictionary_reporting`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputEnergyManagementSystem.internal_variable_availability_dictionary_reporting`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Internal Variable Availability Dictionary Reporting"] = value

    @property
    def ems_runtime_language_debug_output_level(self):
        """Get ems_runtime_language_debug_output_level

        Returns:
            str: the value of `ems_runtime_language_debug_output_level` or None if not set
        """
        return self._data["EMS Runtime Language Debug Output Level"]

    @ems_runtime_language_debug_output_level.setter
    def ems_runtime_language_debug_output_level(self, value="None"):
        """  Corresponds to IDD Field `EMS Runtime Language Debug Output Level`

        Args:
            value (str): value for IDD Field `EMS Runtime Language Debug Output Level`
                Accepted values are:
                      - None
                      - ErrorsOnly
                      - Verbose
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputEnergyManagementSystem.ems_runtime_language_debug_output_level`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputEnergyManagementSystem.ems_runtime_language_debug_output_level`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputEnergyManagementSystem.ems_runtime_language_debug_output_level`')
            vals = {}
            vals["none"] = "None"
            vals["errorsonly"] = "ErrorsOnly"
            vals["verbose"] = "Verbose"
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
                                     'field `OutputEnergyManagementSystem.ems_runtime_language_debug_output_level`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputEnergyManagementSystem.ems_runtime_language_debug_output_level`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["EMS Runtime Language Debug Output Level"] = value

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
                    raise ValueError("Required field OutputEnergyManagementSystem:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputEnergyManagementSystem:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputEnergyManagementSystem: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputEnergyManagementSystem: {} / {}".format(out_fields,
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
    required_fields = ["Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `OutputControl:SurfaceColorScheme`
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
            self.drawing_element_1_type = None
        else:
            self.drawing_element_1_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_1 = None
        else:
            self.color_for_drawing_element_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_2_type = None
        else:
            self.drawing_element_2_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_2 = None
        else:
            self.color_for_drawing_element_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_3_type = None
        else:
            self.drawing_element_3_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_3 = None
        else:
            self.color_for_drawing_element_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_4_type = None
        else:
            self.drawing_element_4_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_4 = None
        else:
            self.color_for_drawing_element_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_5_type = None
        else:
            self.drawing_element_5_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_5 = None
        else:
            self.color_for_drawing_element_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_6_type = None
        else:
            self.drawing_element_6_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_6 = None
        else:
            self.color_for_drawing_element_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_7_type = None
        else:
            self.drawing_element_7_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_7 = None
        else:
            self.color_for_drawing_element_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_8_type = None
        else:
            self.drawing_element_8_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_8 = None
        else:
            self.color_for_drawing_element_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_9_type = None
        else:
            self.drawing_element_9_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_9 = None
        else:
            self.color_for_drawing_element_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_10_type = None
        else:
            self.drawing_element_10_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_10 = None
        else:
            self.color_for_drawing_element_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_11_type = None
        else:
            self.drawing_element_11_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_11 = None
        else:
            self.color_for_drawing_element_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_12_type = None
        else:
            self.drawing_element_12_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_12 = None
        else:
            self.color_for_drawing_element_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_13_type = None
        else:
            self.drawing_element_13_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_13 = None
        else:
            self.color_for_drawing_element_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_14_type = None
        else:
            self.drawing_element_14_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_14 = None
        else:
            self.color_for_drawing_element_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.drawing_element_15_type = None
        else:
            self.drawing_element_15_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.color_for_drawing_element_15 = None
        else:
            self.color_for_drawing_element_15 = vals[i]
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
        choose a name or use one of the DataSets

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
                                 ' for field `OutputControlSurfaceColorScheme.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.name`')
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
        """  Corresponds to IDD Field `Drawing Element 1 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 1 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_1_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_1_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_1_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_1_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_1_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 1`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 1`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_1`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_1`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_1`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_1`')
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
        """  Corresponds to IDD Field `Drawing Element 2 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 2 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_2_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_2_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_2_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_2_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_2_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 2`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 2`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_2`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_2`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_2`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_2`')
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
        """  Corresponds to IDD Field `Drawing Element 3 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 3 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_3_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_3_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_3_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_3_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_3_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 3`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 3`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_3`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_3`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_3`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_3`')
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
        """  Corresponds to IDD Field `Drawing Element 4 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 4 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_4_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_4_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_4_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_4_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_4_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 4`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 4`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_4`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_4`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_4`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_4`')
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
        """  Corresponds to IDD Field `Drawing Element 5 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 5 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_5_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_5_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_5_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_5_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_5_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 5`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 5`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_5`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_5`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_5`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_5`')
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
        """  Corresponds to IDD Field `Drawing Element 6 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 6 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_6_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_6_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_6_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_6_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_6_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 6`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 6`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_6`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_6`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_6`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_6`')
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
        """  Corresponds to IDD Field `Drawing Element 7 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 7 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_7_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_7_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_7_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_7_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_7_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 7`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 7`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_7`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_7`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_7`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_7`')
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
        """  Corresponds to IDD Field `Drawing Element 8 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 8 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_8_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_8_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_8_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_8_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_8_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 8`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 8`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_8`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_8`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_8`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_8`')
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
        """  Corresponds to IDD Field `Drawing Element 9 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 9 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_9_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_9_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_9_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_9_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_9_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 9`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 9`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_9`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_9`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_9`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_9`')
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
        """  Corresponds to IDD Field `Drawing Element 10 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 10 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_10_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_10_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_10_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_10_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_10_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 10`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 10`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_10`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_10`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_10`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_10`')
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
        """  Corresponds to IDD Field `Drawing Element 11 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 11 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_11_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_11_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_11_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_11_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_11_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 11`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 11`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_11`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_11`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_11`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_11`')
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
        """  Corresponds to IDD Field `Drawing Element 12 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 12 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_12_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_12_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_12_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_12_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_12_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 12`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 12`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_12`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_12`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_12`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_12`')
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
        """  Corresponds to IDD Field `Drawing Element 13 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 13 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_13_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_13_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_13_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_13_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_13_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 13`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 13`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_13`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_13`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_13`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_13`')
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
        """  Corresponds to IDD Field `Drawing Element 14 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 14 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_14_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_14_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_14_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_14_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_14_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 14`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 14`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_14`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_14`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_14`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_14`')
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
        """  Corresponds to IDD Field `Drawing Element 15 Type`

        Args:
            value (str): value for IDD Field `Drawing Element 15 Type`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlSurfaceColorScheme.drawing_element_15_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_15_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlSurfaceColorScheme.drawing_element_15_type`')
            vals = {}
            vals["text"] = "Text"
            vals["walls"] = "Walls"
            vals["windows"] = "Windows"
            vals["glassdoors"] = "GlassDoors"
            vals["doors"] = "Doors"
            vals["roofs"] = "Roofs"
            vals["floors"] = "Floors"
            vals["detachedbuildingshades"] = "DetachedBuildingShades"
            vals["detachedfixedshades"] = "DetachedFixedShades"
            vals["attachedbuildingshades"] = "AttachedBuildingShades"
            vals["photovoltaics"] = "Photovoltaics"
            vals["tubulardaylightdomes"] = "TubularDaylightDomes"
            vals["tubulardaylightdiffusers"] = "TubularDaylightDiffusers"
            vals["daylightreferencepoint1"] = "DaylightReferencePoint1"
            vals["daylightreferencepoint2"] = "DaylightReferencePoint2"
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
                                     'field `OutputControlSurfaceColorScheme.drawing_element_15_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlSurfaceColorScheme.drawing_element_15_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Color for Drawing Element 15`
        use color number for output assignment (e.g. DXF)

        Args:
            value (int): value for IDD Field `Color for Drawing Element 15`
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
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_15`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_15`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_15`')
            if value > 255:
                raise ValueError('value need to be smaller 255 '
                                 'for field `OutputControlSurfaceColorScheme.color_for_drawing_element_15`')
        self._data["Color for Drawing Element 15"] = value

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
                    raise ValueError("Required field OutputControlSurfaceColorScheme:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputControlSurfaceColorScheme:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputControlSurfaceColorScheme: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputControlSurfaceColorScheme: {} / {}".format(out_fields,
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

class OutputTableSummaryReports(object):
    """ Corresponds to IDD object `Output:Table:SummaryReports`
        This object allows the user to call report types that are predefined and will appear with the
        other tabular reports.  These predefined reports are sensitive to the OutputControl:Table:Style object
        and appear in the same files as the tabular reports.  The entries for this object is a list
        of the predefined reports that should appear in the tabular report output file.
        There should be as many fields (A) in this object as there are keys in the following (minus
        AllSummary+AllMonthly+AllSummaryAndMonthly)
    """
    internal_name = "Output:Table:SummaryReports"
    field_count = 0
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Table:SummaryReports`
        """
        self._data = OrderedDict()
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
        self.strict = old_strict

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
                    raise ValueError("Required field OutputTableSummaryReports:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputTableSummaryReports:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputTableSummaryReports: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputTableSummaryReports: {} / {}".format(out_fields,
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

class OutputTableTimeBins(object):
    """ Corresponds to IDD object `Output:Table:TimeBins`
        Produces a bin report in the table output file which shows the amount of time in hours
        that occurs in different bins for a single specific output variable or meter.
        Two different types of binning are reported: by month and by hour of the day.
    """
    internal_name = "Output:Table:TimeBins"
    field_count = 7
    required_fields = ["Variable Name"]
    extensible_fields = 0
    format = None
    min_fields = 5
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Table:TimeBins`
        """
        self._data = OrderedDict()
        self._data["Key Value"] = None
        self._data["Variable Name"] = None
        self._data["Interval Start"] = None
        self._data["Interval Size"] = None
        self._data["Interval Count"] = None
        self._data["Schedule Name"] = None
        self._data["Variable Type"] = None
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
            self.key_value = None
        else:
            self.key_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.variable_name = None
        else:
            self.variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interval_start = None
        else:
            self.interval_start = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interval_size = None
        else:
            self.interval_size = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.interval_count = None
        else:
            self.interval_count = vals[i]
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
            self.variable_type = None
        else:
            self.variable_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def key_value(self):
        """Get key_value

        Returns:
            str: the value of `key_value` or None if not set
        """
        return self._data["Key Value"]

    @key_value.setter
    def key_value(self, value="*"):
        """  Corresponds to IDD Field `Key Value`
        use '*' (without quotes) to apply this variable to all keys

        Args:
            value (str): value for IDD Field `Key Value`
                Default value: *
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputTableTimeBins.key_value`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableTimeBins.key_value`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableTimeBins.key_value`')
        self._data["Key Value"] = value

    @property
    def variable_name(self):
        """Get variable_name

        Returns:
            str: the value of `variable_name` or None if not set
        """
        return self._data["Variable Name"]

    @variable_name.setter
    def variable_name(self, value=None):
        """  Corresponds to IDD Field `Variable Name`

        Args:
            value (str): value for IDD Field `Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputTableTimeBins.variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableTimeBins.variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableTimeBins.variable_name`')
        self._data["Variable Name"] = value

    @property
    def interval_start(self):
        """Get interval_start

        Returns:
            float: the value of `interval_start` or None if not set
        """
        return self._data["Interval Start"]

    @interval_start.setter
    def interval_start(self, value=None):
        """  Corresponds to IDD Field `Interval Start`
        The lowest value for the intervals being binned into.

        Args:
            value (float): value for IDD Field `Interval Start`
                Units are based on field `A4`
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
                                 ' for field `OutputTableTimeBins.interval_start`'.format(value))
        self._data["Interval Start"] = value

    @property
    def interval_size(self):
        """Get interval_size

        Returns:
            float: the value of `interval_size` or None if not set
        """
        return self._data["Interval Size"]

    @interval_size.setter
    def interval_size(self, value=None):
        """  Corresponds to IDD Field `Interval Size`
        The size of the bins starting with Interval start.

        Args:
            value (float): value for IDD Field `Interval Size`
                Units are based on field `A4`
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
                                 ' for field `OutputTableTimeBins.interval_size`'.format(value))
        self._data["Interval Size"] = value

    @property
    def interval_count(self):
        """Get interval_count

        Returns:
            int: the value of `interval_count` or None if not set
        """
        return self._data["Interval Count"]

    @interval_count.setter
    def interval_count(self, value=None):
        """  Corresponds to IDD Field `Interval Count`
        The number of bins used. The number of hours below the start of the
        Lowest bin and above the value of the last bin are also shown.

        Args:
            value (int): value for IDD Field `Interval Count`
                value >= 1
                value <= 20
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
                                     'for field `OutputTableTimeBins.interval_count`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputTableTimeBins.interval_count`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `OutputTableTimeBins.interval_count`')
            if value > 20:
                raise ValueError('value need to be smaller 20 '
                                 'for field `OutputTableTimeBins.interval_count`')
        self._data["Interval Count"] = value

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
        Optional schedule name. Binning is performed for non-zero hours.
        Binning always performed if left blank.

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
                                 ' for field `OutputTableTimeBins.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableTimeBins.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableTimeBins.schedule_name`')
        self._data["Schedule Name"] = value

    @property
    def variable_type(self):
        """Get variable_type

        Returns:
            str: the value of `variable_type` or None if not set
        """
        return self._data["Variable Type"]

    @variable_type.setter
    def variable_type(self, value=None):
        """  Corresponds to IDD Field `Variable Type`
        Optional input on the type of units for the variable used by other fields in the object.

        Args:
            value (str): value for IDD Field `Variable Type`
                Accepted values are:
                      - Energy
                      - Temperature
                      - VolumetricFlow
                      - Power
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputTableTimeBins.variable_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableTimeBins.variable_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableTimeBins.variable_type`')
            vals = {}
            vals["energy"] = "Energy"
            vals["temperature"] = "Temperature"
            vals["volumetricflow"] = "VolumetricFlow"
            vals["power"] = "Power"
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
                                     'field `OutputTableTimeBins.variable_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputTableTimeBins.variable_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Variable Type"] = value

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
                    raise ValueError("Required field OutputTableTimeBins:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputTableTimeBins:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputTableTimeBins: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputTableTimeBins: {} / {}".format(out_fields,
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

class OutputTableMonthly(object):
    """ Corresponds to IDD object `Output:Table:Monthly`
        Provides a generic method of setting up tables of monthly results. The report
        has multiple columns that are each defined using a repeated group of fields for any
        number of columns. A single Output:Table:Monthly object often produces multiple
        tables in the output. A table is produced for every instance of a particular output
        variable. For example, a table defined with zone variables will be produced once for
        every zone.
    """
    internal_name = "Output:Table:Monthly"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Variable or Meter 1 Name", "Aggregation Type for Variable or Meter 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Table:Monthly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Digits After Decimal"] = None
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
            self.digits_after_decimal = None
        else:
            self.digits_after_decimal = vals[i]
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
                                 ' for field `OutputTableMonthly.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableMonthly.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableMonthly.name`')
        self._data["Name"] = value

    @property
    def digits_after_decimal(self):
        """Get digits_after_decimal

        Returns:
            int: the value of `digits_after_decimal` or None if not set
        """
        return self._data["Digits After Decimal"]

    @digits_after_decimal.setter
    def digits_after_decimal(self, value=2):
        """  Corresponds to IDD Field `Digits After Decimal`

        Args:
            value (int): value for IDD Field `Digits After Decimal`
                Default value: 2
                value >= 0
                value <= 10
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
                                     'for field `OutputTableMonthly.digits_after_decimal`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputTableMonthly.digits_after_decimal`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `OutputTableMonthly.digits_after_decimal`')
            if value > 10:
                raise ValueError('value need to be smaller 10 '
                                 'for field `OutputTableMonthly.digits_after_decimal`')
        self._data["Digits After Decimal"] = value

    def add_extensible(self,
                       variable_or_meter_1_name=None,
                       aggregation_type_for_variable_or_meter_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            variable_or_meter_1_name (str): value for IDD Field `Variable or Meter 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            aggregation_type_for_variable_or_meter_1 (str): value for IDD Field `Aggregation Type for Variable or Meter 1`
                Accepted values are:
                      - SumOrAverage
                      - Maximum
                      - Minimum
                      - ValueWhenMaximumOrMinimum
                      - HoursNonZero
                      - HoursZero
                      - HoursPositive
                      - HoursNonPositive
                      - HoursNegative
                      - HoursNonNegative
                      - SumOrAverageDuringHoursShown
                      - MaximumDuringHoursShown
                      - MinimumDuringHoursShown
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_variable_or_meter_1_name(variable_or_meter_1_name))
        vals.append(self._check_aggregation_type_for_variable_or_meter_1(aggregation_type_for_variable_or_meter_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_variable_or_meter_1_name(self, value):
        """ Validates falue of field `Variable or Meter 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputTableMonthly.variable_or_meter_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableMonthly.variable_or_meter_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableMonthly.variable_or_meter_1_name`')
        return value

    def _check_aggregation_type_for_variable_or_meter_1(self, value):
        """ Validates falue of field `Aggregation Type for Variable or Meter 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputTableMonthly.aggregation_type_for_variable_or_meter_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputTableMonthly.aggregation_type_for_variable_or_meter_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputTableMonthly.aggregation_type_for_variable_or_meter_1`')
            vals = {}
            vals["sumoraverage"] = "SumOrAverage"
            vals["maximum"] = "Maximum"
            vals["minimum"] = "Minimum"
            vals["valuewhenmaximumorminimum"] = "ValueWhenMaximumOrMinimum"
            vals["hoursnonzero"] = "HoursNonZero"
            vals["hourszero"] = "HoursZero"
            vals["hourspositive"] = "HoursPositive"
            vals["hoursnonpositive"] = "HoursNonPositive"
            vals["hoursnegative"] = "HoursNegative"
            vals["hoursnonnegative"] = "HoursNonNegative"
            vals["sumoraverageduringhoursshown"] = "SumOrAverageDuringHoursShown"
            vals["maximumduringhoursshown"] = "MaximumDuringHoursShown"
            vals["minimumduringhoursshown"] = "MinimumDuringHoursShown"
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
                                     'field `OutputTableMonthly.aggregation_type_for_variable_or_meter_1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputTableMonthly.aggregation_type_for_variable_or_meter_1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
                    raise ValueError("Required field OutputTableMonthly:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputTableMonthly:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputTableMonthly: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputTableMonthly: {} / {}".format(out_fields,
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
    required_fields = ["Column Separator"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `OutputControl:Table:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None
        self._data["Unit Conversion"] = None
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
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.unit_conversion = None
        else:
            self.unit_conversion = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `Column Separator`

        Args:
            value (str): value for IDD Field `Column Separator`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlTableStyle.column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlTableStyle.column_separator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlTableStyle.column_separator`')
            vals = {}
            vals["comma"] = "Comma"
            vals["tab"] = "Tab"
            vals["fixed"] = "Fixed"
            vals["html"] = "HTML"
            vals["xml"] = "XML"
            vals["commaandhtml"] = "CommaAndHTML"
            vals["commaandxml"] = "CommaAndXML"
            vals["tabandhtml"] = "TabAndHTML"
            vals["xmlandhtml"] = "XMLandHTML"
            vals["all"] = "All"
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
                                     'field `OutputControlTableStyle.column_separator`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlTableStyle.column_separator`'.format(value, vals[value_lower]))
            value = vals[value_lower]
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
        """  Corresponds to IDD Field `Unit Conversion`

        Args:
            value (str): value for IDD Field `Unit Conversion`
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
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlTableStyle.unit_conversion`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlTableStyle.unit_conversion`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlTableStyle.unit_conversion`')
            vals = {}
            vals["none"] = "None"
            vals["jtokwh"] = "JtoKWH"
            vals["jtomj"] = "JtoMJ"
            vals["jtogj"] = "JtoGJ"
            vals["inchpound"] = "InchPound"
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
                                     'field `OutputControlTableStyle.unit_conversion`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlTableStyle.unit_conversion`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Unit Conversion"] = value

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
                    raise ValueError("Required field OutputControlTableStyle:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputControlTableStyle:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputControlTableStyle: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputControlTableStyle: {} / {}".format(out_fields,
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

class OutputControlReportingTolerances(object):
    """ Corresponds to IDD object `OutputControl:ReportingTolerances`
        Calculations of the time that setpoints are not met use a tolerance of 0.2C.
        This object allows changing the tolerance used to determine when setpoints are being met.
    """
    internal_name = "OutputControl:ReportingTolerances"
    field_count = 2
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `OutputControl:ReportingTolerances`
        """
        self._data = OrderedDict()
        self._data["Tolerance for Time Heating Setpoint Not Met"] = None
        self._data["Tolerance for Time Cooling Setpoint Not Met"] = None
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
            self.tolerance_for_time_heating_setpoint_not_met = None
        else:
            self.tolerance_for_time_heating_setpoint_not_met = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.tolerance_for_time_cooling_setpoint_not_met = None
        else:
            self.tolerance_for_time_cooling_setpoint_not_met = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def tolerance_for_time_heating_setpoint_not_met(self):
        """Get tolerance_for_time_heating_setpoint_not_met

        Returns:
            float: the value of `tolerance_for_time_heating_setpoint_not_met` or None if not set
        """
        return self._data["Tolerance for Time Heating Setpoint Not Met"]

    @tolerance_for_time_heating_setpoint_not_met.setter
    def tolerance_for_time_heating_setpoint_not_met(self, value=0.2):
        """  Corresponds to IDD Field `Tolerance for Time Heating Setpoint Not Met`
        If the zone temperature is below the heating setpoint by more than
        this value, the following output variables will increment as appropriate
        Zone Heating Setpoint Not Met Time
        Zone Heating Setpoint Not Met While Occupied Time
        This also impacts table report "Annual Building Utility Performance Summary"
        subtable "Comfort and Setpoint Not Met Summary"

        Args:
            value (float): value for IDD Field `Tolerance for Time Heating Setpoint Not Met`
                Units: deltaC
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputControlReportingTolerances.tolerance_for_time_heating_setpoint_not_met`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `OutputControlReportingTolerances.tolerance_for_time_heating_setpoint_not_met`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `OutputControlReportingTolerances.tolerance_for_time_heating_setpoint_not_met`')
        self._data["Tolerance for Time Heating Setpoint Not Met"] = value

    @property
    def tolerance_for_time_cooling_setpoint_not_met(self):
        """Get tolerance_for_time_cooling_setpoint_not_met

        Returns:
            float: the value of `tolerance_for_time_cooling_setpoint_not_met` or None if not set
        """
        return self._data["Tolerance for Time Cooling Setpoint Not Met"]

    @tolerance_for_time_cooling_setpoint_not_met.setter
    def tolerance_for_time_cooling_setpoint_not_met(self, value=0.2):
        """  Corresponds to IDD Field `Tolerance for Time Cooling Setpoint Not Met`
        If the zone temperature is above the cooling setpoint by more than
        this value, the following output variables will increment as appropriate
        Zone Cooling Setpoint Not Met Time
        Zone Cooling Setpoint Not Met While Occupied Time
        This also impacts table report "Annual Building Utility Performance Summary"
        subtable "Comfort and Setpoint Not Met Summary"

        Args:
            value (float): value for IDD Field `Tolerance for Time Cooling Setpoint Not Met`
                Units: deltaC
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
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputControlReportingTolerances.tolerance_for_time_cooling_setpoint_not_met`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `OutputControlReportingTolerances.tolerance_for_time_cooling_setpoint_not_met`')
            if value > 10.0:
                raise ValueError('value need to be smaller 10.0 '
                                 'for field `OutputControlReportingTolerances.tolerance_for_time_cooling_setpoint_not_met`')
        self._data["Tolerance for Time Cooling Setpoint Not Met"] = value

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
                    raise ValueError("Required field OutputControlReportingTolerances:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputControlReportingTolerances:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputControlReportingTolerances: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputControlReportingTolerances: {} / {}".format(out_fields,
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

class OutputVariable(object):
    """ Corresponds to IDD object `Output:Variable`
        each Output:Variable command picks variables to be put onto the standard output file (.eso)
        some variables may not be reported for every simulation.
        a list of variables that can be reported are available after a run on
        the report dictionary file (.rdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "Output:Variable"
    field_count = 4
    required_fields = ["Variable Name"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Variable`
        """
        self._data = OrderedDict()
        self._data["Key Value"] = None
        self._data["Variable Name"] = None
        self._data["Reporting Frequency"] = None
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
            self.key_value = None
        else:
            self.key_value = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.variable_name = None
        else:
            self.variable_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.reporting_frequency = None
        else:
            self.reporting_frequency = vals[i]
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
    def key_value(self):
        """Get key_value

        Returns:
            str: the value of `key_value` or None if not set
        """
        return self._data["Key Value"]

    @key_value.setter
    def key_value(self, value="*"):
        """  Corresponds to IDD Field `Key Value`
        use '*' (without quotes) to apply this variable to all keys

        Args:
            value (str): value for IDD Field `Key Value`
                Default value: *
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputVariable.key_value`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputVariable.key_value`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputVariable.key_value`')
        self._data["Key Value"] = value

    @property
    def variable_name(self):
        """Get variable_name

        Returns:
            str: the value of `variable_name` or None if not set
        """
        return self._data["Variable Name"]

    @variable_name.setter
    def variable_name(self, value=None):
        """  Corresponds to IDD Field `Variable Name`

        Args:
            value (str): value for IDD Field `Variable Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputVariable.variable_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputVariable.variable_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputVariable.variable_name`')
        self._data["Variable Name"] = value

    @property
    def reporting_frequency(self):
        """Get reporting_frequency

        Returns:
            str: the value of `reporting_frequency` or None if not set
        """
        return self._data["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """  Corresponds to IDD Field `Reporting Frequency`
        Detailed lists every instance (i.e. HVAC variable timesteps)
        Timestep refers to the zone Timestep/Number of Timesteps in hour value
        RunPeriod, Environment, and Annual are the same
        RunPeriod, Environment, and Annual are synonymous

        Args:
            value (str): value for IDD Field `Reporting Frequency`
                Accepted values are:
                      - Detailed
                      - Timestep
                      - Hourly
                      - Daily
                      - Monthly
                      - RunPeriod
                      - Environment
                      - Annual
                Default value: Hourly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputVariable.reporting_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputVariable.reporting_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputVariable.reporting_frequency`')
            vals = {}
            vals["detailed"] = "Detailed"
            vals["timestep"] = "Timestep"
            vals["hourly"] = "Hourly"
            vals["daily"] = "Daily"
            vals["monthly"] = "Monthly"
            vals["runperiod"] = "RunPeriod"
            vals["environment"] = "Environment"
            vals["annual"] = "Annual"
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
                                     'field `OutputVariable.reporting_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputVariable.reporting_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Frequency"] = value

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
                                 ' for field `OutputVariable.schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputVariable.schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputVariable.schedule_name`')
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
                    raise ValueError("Required field OutputVariable:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputVariable:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputVariable: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputVariable: {} / {}".format(out_fields,
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

class OutputMeter(object):
    """ Corresponds to IDD object `Output:Meter`
        Each Output:Meter command picks meters to be put onto the standard output file (.eso) and
        meter file (.mtr). Not all meters are reported in every simulation. A list of
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "Output:Meter"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Meter`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reporting Frequency"] = None
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
            self.reporting_frequency = None
        else:
            self.reporting_frequency = vals[i]
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
        Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        or EndUse:..., e.g. GeneralLights:* for all General Lights
        Output:Meter puts results on both the eplusout.mtr and eplusout.eso files

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
                                 ' for field `OutputMeter.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeter.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeter.name`')
        self._data["Name"] = value

    @property
    def reporting_frequency(self):
        """Get reporting_frequency

        Returns:
            str: the value of `reporting_frequency` or None if not set
        """
        return self._data["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """  Corresponds to IDD Field `Reporting Frequency`
        Timestep refers to the zone Timestep/Number of Timesteps in hour value
        RunPeriod, Environment, and Annual are the same
        RunPeriod, Environment, and Annual are synonymous

        Args:
            value (str): value for IDD Field `Reporting Frequency`
                Accepted values are:
                      - Timestep
                      - Hourly
                      - Daily
                      - Monthly
                      - RunPeriod
                      - Environment
                      - Annual
                Default value: Hourly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputMeter.reporting_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeter.reporting_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeter.reporting_frequency`')
            vals = {}
            vals["timestep"] = "Timestep"
            vals["hourly"] = "Hourly"
            vals["daily"] = "Daily"
            vals["monthly"] = "Monthly"
            vals["runperiod"] = "RunPeriod"
            vals["environment"] = "Environment"
            vals["annual"] = "Annual"
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
                                     'field `OutputMeter.reporting_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputMeter.reporting_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Frequency"] = value

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
                    raise ValueError("Required field OutputMeter:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputMeter:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputMeter: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputMeter: {} / {}".format(out_fields,
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

class OutputMeterMeterFileOnly(object):
    """ Corresponds to IDD object `Output:Meter:MeterFileOnly`
        Each Output:Meter:MeterFileOnly command picks meters to be put only onto meter file (.mtr).
        Not all meters are reported in every simulation. A list of meters that can be reported
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "Output:Meter:MeterFileOnly"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Meter:MeterFileOnly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reporting Frequency"] = None
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
            self.reporting_frequency = None
        else:
            self.reporting_frequency = vals[i]
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
        Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        or EndUse:..., e.g. GeneralLights:* for all General Lights
        Output:Meter:MeterFileOnly puts results on the eplusout.mtr file only

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
                                 ' for field `OutputMeterMeterFileOnly.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeterMeterFileOnly.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeterMeterFileOnly.name`')
        self._data["Name"] = value

    @property
    def reporting_frequency(self):
        """Get reporting_frequency

        Returns:
            str: the value of `reporting_frequency` or None if not set
        """
        return self._data["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """  Corresponds to IDD Field `Reporting Frequency`
        Timestep refers to the zone Timestep/Number of Timesteps in hour value
        RunPeriod, Environment, and Annual are the same
        RunPeriod, Environment, and Annual are synonymous

        Args:
            value (str): value for IDD Field `Reporting Frequency`
                Accepted values are:
                      - Timestep
                      - Hourly
                      - Daily
                      - Monthly
                      - RunPeriod
                      - Environment
                      - Annual
                Default value: Hourly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputMeterMeterFileOnly.reporting_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeterMeterFileOnly.reporting_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeterMeterFileOnly.reporting_frequency`')
            vals = {}
            vals["timestep"] = "Timestep"
            vals["hourly"] = "Hourly"
            vals["daily"] = "Daily"
            vals["monthly"] = "Monthly"
            vals["runperiod"] = "RunPeriod"
            vals["environment"] = "Environment"
            vals["annual"] = "Annual"
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
                                     'field `OutputMeterMeterFileOnly.reporting_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputMeterMeterFileOnly.reporting_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Frequency"] = value

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
                    raise ValueError("Required field OutputMeterMeterFileOnly:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputMeterMeterFileOnly:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputMeterMeterFileOnly: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputMeterMeterFileOnly: {} / {}".format(out_fields,
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

class OutputMeterCumulative(object):
    """ Corresponds to IDD object `Output:Meter:Cumulative`
        Each Output:Meter:Cumulative command picks meters to be reported cumulatively onto the
        standard output file (.eso) and meter file (.mtr). Not all meters are reported in every
        simulation.
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "Output:Meter:Cumulative"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Meter:Cumulative`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reporting Frequency"] = None
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
            self.reporting_frequency = None
        else:
            self.reporting_frequency = vals[i]
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
        Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        or EndUse:..., e.g. GeneralLights:* for all General Lights
        Output:Meter:Cumulative puts results on both the eplusout.mtr and eplusout.eso files

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
                                 ' for field `OutputMeterCumulative.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeterCumulative.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeterCumulative.name`')
        self._data["Name"] = value

    @property
    def reporting_frequency(self):
        """Get reporting_frequency

        Returns:
            str: the value of `reporting_frequency` or None if not set
        """
        return self._data["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """  Corresponds to IDD Field `Reporting Frequency`
        Timestep refers to the zone Timestep/Number of Timesteps in hour value
        RunPeriod, Environment, and Annual are the same
        RunPeriod, Environment, and Annual are synonymous

        Args:
            value (str): value for IDD Field `Reporting Frequency`
                Accepted values are:
                      - Timestep
                      - Hourly
                      - Daily
                      - Monthly
                      - RunPeriod
                      - Environment
                      - Annual
                Default value: Hourly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputMeterCumulative.reporting_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeterCumulative.reporting_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeterCumulative.reporting_frequency`')
            vals = {}
            vals["timestep"] = "Timestep"
            vals["hourly"] = "Hourly"
            vals["daily"] = "Daily"
            vals["monthly"] = "Monthly"
            vals["runperiod"] = "RunPeriod"
            vals["environment"] = "Environment"
            vals["annual"] = "Annual"
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
                                     'field `OutputMeterCumulative.reporting_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputMeterCumulative.reporting_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Frequency"] = value

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
                    raise ValueError("Required field OutputMeterCumulative:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputMeterCumulative:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputMeterCumulative: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputMeterCumulative: {} / {}".format(out_fields,
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

class OutputMeterCumulativeMeterFileOnly(object):
    """ Corresponds to IDD object `Output:Meter:Cumulative:MeterFileOnly`
        Each Output:Meter:Cumulative:MeterFileOnly command picks meters to be reported cumulatively
        onto the standard output file (.eso) and meter file (.mtr). Not all meters are reported in
        every simulation.
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "Output:Meter:Cumulative:MeterFileOnly"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Meter:Cumulative:MeterFileOnly`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Reporting Frequency"] = None
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
            self.reporting_frequency = None
        else:
            self.reporting_frequency = vals[i]
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
        Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters
        or EndUse:..., e.g. GeneralLights:* for all General Lights
        Output:Meter:Cumulative:MeterFileOnly puts results on the eplusout.mtr file only

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
                                 ' for field `OutputMeterCumulativeMeterFileOnly.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeterCumulativeMeterFileOnly.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeterCumulativeMeterFileOnly.name`')
        self._data["Name"] = value

    @property
    def reporting_frequency(self):
        """Get reporting_frequency

        Returns:
            str: the value of `reporting_frequency` or None if not set
        """
        return self._data["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value="Hourly"):
        """  Corresponds to IDD Field `Reporting Frequency`
        Timestep refers to the zone Timestep/Number of Timesteps in hour value
        RunPeriod, Environment, and Annual are the same
        RunPeriod, Environment, and Annual are synonymous

        Args:
            value (str): value for IDD Field `Reporting Frequency`
                Accepted values are:
                      - Timestep
                      - Hourly
                      - Daily
                      - Monthly
                      - RunPeriod
                      - Environment
                      - Annual
                Default value: Hourly
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputMeterCumulativeMeterFileOnly.reporting_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputMeterCumulativeMeterFileOnly.reporting_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputMeterCumulativeMeterFileOnly.reporting_frequency`')
            vals = {}
            vals["timestep"] = "Timestep"
            vals["hourly"] = "Hourly"
            vals["daily"] = "Daily"
            vals["monthly"] = "Monthly"
            vals["runperiod"] = "RunPeriod"
            vals["environment"] = "Environment"
            vals["annual"] = "Annual"
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
                                     'field `OutputMeterCumulativeMeterFileOnly.reporting_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputMeterCumulativeMeterFileOnly.reporting_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Frequency"] = value

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
                    raise ValueError("Required field OutputMeterCumulativeMeterFileOnly:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputMeterCumulativeMeterFileOnly:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputMeterCumulativeMeterFileOnly: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputMeterCumulativeMeterFileOnly: {} / {}".format(out_fields,
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

class MeterCustom(object):
    """ Corresponds to IDD object `Meter:Custom`
        Used to allow users to combine specific variables and/or meters into
        "custom" meter configurations. To access these meters by name, one must
        first run a simulation to generate the RDD/MDD files and names.
    """
    internal_name = "Meter:Custom"
    field_count = 2
    required_fields = ["Name"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Key Name 1", "Output Variable or Meter Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Meter:Custom`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fuel Type"] = None
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
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
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
                                 ' for field `MeterCustom.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustom.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustom.name`')
        self._data["Name"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """  Corresponds to IDD Field `Fuel Type`

        Args:
            value (str): value for IDD Field `Fuel Type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - Water
                      - Generic
                      - OtherFuel1
                      - OtherFuel2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustom.fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustom.fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustom.fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["water"] = "Water"
            vals["generic"] = "Generic"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
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
                                     'field `MeterCustom.fuel_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `MeterCustom.fuel_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fuel Type"] = value

    def add_extensible(self,
                       key_name_1=None,
                       output_variable_or_meter_name_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            key_name_1 (str): value for IDD Field `Key Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_variable_or_meter_name_1 (str): value for IDD Field `Output Variable or Meter Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_key_name_1(key_name_1))
        vals.append(self._check_output_variable_or_meter_name_1(output_variable_or_meter_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_key_name_1(self, value):
        """ Validates falue of field `Key Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustom.key_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustom.key_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustom.key_name_1`')
        return value

    def _check_output_variable_or_meter_name_1(self, value):
        """ Validates falue of field `Output Variable or Meter Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustom.output_variable_or_meter_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustom.output_variable_or_meter_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustom.output_variable_or_meter_name_1`')
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
                    raise ValueError("Required field MeterCustom:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field MeterCustom:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for MeterCustom: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for MeterCustom: {} / {}".format(out_fields,
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

class MeterCustomDecrement(object):
    """ Corresponds to IDD object `Meter:CustomDecrement`
        Used to allow users to combine specific variables and/or meters into
        "custom" meter configurations. To access these meters by name, one must
        first run a simulation to generate the RDD/MDD files and names.
    """
    internal_name = "Meter:CustomDecrement"
    field_count = 3
    required_fields = ["Name", "Source Meter Name"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Key Name 1", "Output Variable or Meter Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Meter:CustomDecrement`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fuel Type"] = None
        self._data["Source Meter Name"] = None
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
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_meter_name = None
        else:
            self.source_meter_name = vals[i]
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
                                 ' for field `MeterCustomDecrement.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustomDecrement.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustomDecrement.name`')
        self._data["Name"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value=None):
        """  Corresponds to IDD Field `Fuel Type`

        Args:
            value (str): value for IDD Field `Fuel Type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Diesel
                      - Gasoline
                      - Water
                      - Generic
                      - OtherFuel1
                      - OtherFuel2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustomDecrement.fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustomDecrement.fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustomDecrement.fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["water"] = "Water"
            vals["generic"] = "Generic"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
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
                                     'field `MeterCustomDecrement.fuel_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `MeterCustomDecrement.fuel_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Fuel Type"] = value

    @property
    def source_meter_name(self):
        """Get source_meter_name

        Returns:
            str: the value of `source_meter_name` or None if not set
        """
        return self._data["Source Meter Name"]

    @source_meter_name.setter
    def source_meter_name(self, value=None):
        """  Corresponds to IDD Field `Source Meter Name`

        Args:
            value (str): value for IDD Field `Source Meter Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustomDecrement.source_meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustomDecrement.source_meter_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustomDecrement.source_meter_name`')
        self._data["Source Meter Name"] = value

    def add_extensible(self,
                       key_name_1=None,
                       output_variable_or_meter_name_1=None,
                       ):
        """ Add values for extensible fields

        Args:

            key_name_1 (str): value for IDD Field `Key Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            output_variable_or_meter_name_1 (str): value for IDD Field `Output Variable or Meter Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_key_name_1(key_name_1))
        vals.append(self._check_output_variable_or_meter_name_1(output_variable_or_meter_name_1))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_key_name_1(self, value):
        """ Validates falue of field `Key Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustomDecrement.key_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustomDecrement.key_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustomDecrement.key_name_1`')
        return value

    def _check_output_variable_or_meter_name_1(self, value):
        """ Validates falue of field `Output Variable or Meter Name 1`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `MeterCustomDecrement.output_variable_or_meter_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `MeterCustomDecrement.output_variable_or_meter_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `MeterCustomDecrement.output_variable_or_meter_name_1`')
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
                    raise ValueError("Required field MeterCustomDecrement:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field MeterCustomDecrement:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for MeterCustomDecrement: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for MeterCustomDecrement: {} / {}".format(out_fields,
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

class OutputSqlite(object):
    """ Corresponds to IDD object `Output:SQLite`
        Output from EnergyPlus can be written to an SQLite format file.
    """
    internal_name = "Output:SQLite"
    field_count = 1
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:SQLite`
        """
        self._data = OrderedDict()
        self._data["Option Type"] = None
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
            self.option_type = None
        else:
            self.option_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def option_type(self):
        """Get option_type

        Returns:
            str: the value of `option_type` or None if not set
        """
        return self._data["Option Type"]

    @option_type.setter
    def option_type(self, value=None):
        """  Corresponds to IDD Field `Option Type`

        Args:
            value (str): value for IDD Field `Option Type`
                Accepted values are:
                      - Simple
                      - SimpleAndTabular
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputSqlite.option_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputSqlite.option_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputSqlite.option_type`')
            vals = {}
            vals["simple"] = "Simple"
            vals["simpleandtabular"] = "SimpleAndTabular"
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
                                     'field `OutputSqlite.option_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputSqlite.option_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Option Type"] = value

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
                    raise ValueError("Required field OutputSqlite:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputSqlite:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputSqlite: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputSqlite: {} / {}".format(out_fields,
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

class OutputEnvironmentalImpactFactors(object):
    """ Corresponds to IDD object `Output:EnvironmentalImpactFactors`
        This is used to Automatically report the facility meters and turn on the Environmental Impact Report calculations
        for all of the Environmental Factors.
    """
    internal_name = "Output:EnvironmentalImpactFactors"
    field_count = 1
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:EnvironmentalImpactFactors`
        """
        self._data = OrderedDict()
        self._data["Reporting Frequency"] = None
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
            self.reporting_frequency = None
        else:
            self.reporting_frequency = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def reporting_frequency(self):
        """Get reporting_frequency

        Returns:
            str: the value of `reporting_frequency` or None if not set
        """
        return self._data["Reporting Frequency"]

    @reporting_frequency.setter
    def reporting_frequency(self, value=None):
        """  Corresponds to IDD Field `Reporting Frequency`

        Args:
            value (str): value for IDD Field `Reporting Frequency`
                Accepted values are:
                      - Timestep
                      - Hourly
                      - Daily
                      - Monthly
                      - RunPeriod
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputEnvironmentalImpactFactors.reporting_frequency`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputEnvironmentalImpactFactors.reporting_frequency`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputEnvironmentalImpactFactors.reporting_frequency`')
            vals = {}
            vals["timestep"] = "Timestep"
            vals["hourly"] = "Hourly"
            vals["daily"] = "Daily"
            vals["monthly"] = "Monthly"
            vals["runperiod"] = "RunPeriod"
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
                                     'field `OutputEnvironmentalImpactFactors.reporting_frequency`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputEnvironmentalImpactFactors.reporting_frequency`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Frequency"] = value

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
                    raise ValueError("Required field OutputEnvironmentalImpactFactors:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputEnvironmentalImpactFactors:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputEnvironmentalImpactFactors: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputEnvironmentalImpactFactors: {} / {}".format(out_fields,
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

class EnvironmentalImpactFactors(object):
    """ Corresponds to IDD object `EnvironmentalImpactFactors`
        Used to help convert district and ideal energy use to a fuel type and provide total carbon equivalent with coefficients
        Also used in Source=>Site conversions.
    """
    internal_name = "EnvironmentalImpactFactors"
    field_count = 6
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `EnvironmentalImpactFactors`
        """
        self._data = OrderedDict()
        self._data["District Heating Efficiency"] = None
        self._data["District Cooling COP"] = None
        self._data["Steam Conversion Efficiency"] = None
        self._data["Total Carbon Equivalent Emission Factor From N2O"] = None
        self._data["Total Carbon Equivalent Emission Factor From CH4"] = None
        self._data["Total Carbon Equivalent Emission Factor From CO2"] = None
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
            self.district_heating_efficiency = None
        else:
            self.district_heating_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.district_cooling_cop = None
        else:
            self.district_cooling_cop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.steam_conversion_efficiency = None
        else:
            self.steam_conversion_efficiency = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_carbon_equivalent_emission_factor_from_n2o = None
        else:
            self.total_carbon_equivalent_emission_factor_from_n2o = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_carbon_equivalent_emission_factor_from_ch4 = None
        else:
            self.total_carbon_equivalent_emission_factor_from_ch4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_carbon_equivalent_emission_factor_from_co2 = None
        else:
            self.total_carbon_equivalent_emission_factor_from_co2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def district_heating_efficiency(self):
        """Get district_heating_efficiency

        Returns:
            float: the value of `district_heating_efficiency` or None if not set
        """
        return self._data["District Heating Efficiency"]

    @district_heating_efficiency.setter
    def district_heating_efficiency(self, value=0.3):
        """  Corresponds to IDD Field `District Heating Efficiency`
        District heating efficiency used when converted to natural gas

        Args:
            value (float): value for IDD Field `District Heating Efficiency`
                Default value: 0.3
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
                                 ' for field `EnvironmentalImpactFactors.district_heating_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `EnvironmentalImpactFactors.district_heating_efficiency`')
        self._data["District Heating Efficiency"] = value

    @property
    def district_cooling_cop(self):
        """Get district_cooling_cop

        Returns:
            float: the value of `district_cooling_cop` or None if not set
        """
        return self._data["District Cooling COP"]

    @district_cooling_cop.setter
    def district_cooling_cop(self, value=3.0):
        """  Corresponds to IDD Field `District Cooling COP`
        District cooling COP used when converted to electricity

        Args:
            value (float): value for IDD Field `District Cooling COP`
                Units: W/W
                Default value: 3.0
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
                                 ' for field `EnvironmentalImpactFactors.district_cooling_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `EnvironmentalImpactFactors.district_cooling_cop`')
        self._data["District Cooling COP"] = value

    @property
    def steam_conversion_efficiency(self):
        """Get steam_conversion_efficiency

        Returns:
            float: the value of `steam_conversion_efficiency` or None if not set
        """
        return self._data["Steam Conversion Efficiency"]

    @steam_conversion_efficiency.setter
    def steam_conversion_efficiency(self, value=0.25):
        """  Corresponds to IDD Field `Steam Conversion Efficiency`
        Steam conversion efficiency used to convert steam usage to natural gas

        Args:
            value (float): value for IDD Field `Steam Conversion Efficiency`
                Default value: 0.25
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
                                 ' for field `EnvironmentalImpactFactors.steam_conversion_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `EnvironmentalImpactFactors.steam_conversion_efficiency`')
        self._data["Steam Conversion Efficiency"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_n2o(self):
        """Get total_carbon_equivalent_emission_factor_from_n2o

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_n2o` or None if not set
        """
        return self._data["Total Carbon Equivalent Emission Factor From N2O"]

    @total_carbon_equivalent_emission_factor_from_n2o.setter
    def total_carbon_equivalent_emission_factor_from_n2o(self, value=80.7272):
        """  Corresponds to IDD Field `Total Carbon Equivalent Emission Factor From N2O`

        Args:
            value (float): value for IDD Field `Total Carbon Equivalent Emission Factor From N2O`
                Units: kg/kg
                Default value: 80.7272
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
                                 ' for field `EnvironmentalImpactFactors.total_carbon_equivalent_emission_factor_from_n2o`'.format(value))
        self._data["Total Carbon Equivalent Emission Factor From N2O"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_ch4(self):
        """Get total_carbon_equivalent_emission_factor_from_ch4

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_ch4` or None if not set
        """
        return self._data["Total Carbon Equivalent Emission Factor From CH4"]

    @total_carbon_equivalent_emission_factor_from_ch4.setter
    def total_carbon_equivalent_emission_factor_from_ch4(self, value=6.2727):
        """  Corresponds to IDD Field `Total Carbon Equivalent Emission Factor From CH4`

        Args:
            value (float): value for IDD Field `Total Carbon Equivalent Emission Factor From CH4`
                Units: kg/kg
                Default value: 6.2727
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
                                 ' for field `EnvironmentalImpactFactors.total_carbon_equivalent_emission_factor_from_ch4`'.format(value))
        self._data["Total Carbon Equivalent Emission Factor From CH4"] = value

    @property
    def total_carbon_equivalent_emission_factor_from_co2(self):
        """Get total_carbon_equivalent_emission_factor_from_co2

        Returns:
            float: the value of `total_carbon_equivalent_emission_factor_from_co2` or None if not set
        """
        return self._data["Total Carbon Equivalent Emission Factor From CO2"]

    @total_carbon_equivalent_emission_factor_from_co2.setter
    def total_carbon_equivalent_emission_factor_from_co2(self, value=0.2727):
        """  Corresponds to IDD Field `Total Carbon Equivalent Emission Factor From CO2`

        Args:
            value (float): value for IDD Field `Total Carbon Equivalent Emission Factor From CO2`
                Units: kg/kg
                Default value: 0.2727
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
                                 ' for field `EnvironmentalImpactFactors.total_carbon_equivalent_emission_factor_from_co2`'.format(value))
        self._data["Total Carbon Equivalent Emission Factor From CO2"] = value

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
                    raise ValueError("Required field EnvironmentalImpactFactors:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field EnvironmentalImpactFactors:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for EnvironmentalImpactFactors: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for EnvironmentalImpactFactors: {} / {}".format(out_fields,
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

class FuelFactors(object):
    """ Corresponds to IDD object `FuelFactors`
        Provides Fuel Factors for Emissions as well as Source=>Site conversions.
        OtherFuel1, OtherFuel2 provide options for users who want to create and use
        fuels that may not be mainstream (biomass, wood, pellets).
    """
    internal_name = "FuelFactors"
    field_count = 37
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `FuelFactors`
        """
        self._data = OrderedDict()
        self._data["Existing Fuel Resource Name"] = None
        self._data["Units of Measure"] = None
        self._data["Energy per Unit Factor"] = None
        self._data["Source Energy Factor"] = None
        self._data["Source Energy Schedule Name"] = None
        self._data["CO2 Emission Factor"] = None
        self._data["CO2 Emission Factor Schedule Name"] = None
        self._data["CO Emission Factor"] = None
        self._data["CO Emission Factor Schedule Name"] = None
        self._data["CH4 Emission Factor"] = None
        self._data["CH4 Emission Factor Schedule Name"] = None
        self._data["NOx Emission Factor"] = None
        self._data["NOx Emission Factor Schedule Name"] = None
        self._data["N2O Emission Factor"] = None
        self._data["N2O Emission Factor Schedule Name"] = None
        self._data["SO2 Emission Factor"] = None
        self._data["SO2 Emission Factor Schedule Name"] = None
        self._data["PM Emission Factor"] = None
        self._data["PM Emission Factor Schedule Name"] = None
        self._data["PM10 Emission Factor"] = None
        self._data["PM10 Emission Factor Schedule Name"] = None
        self._data["PM2.5 Emission Factor"] = None
        self._data["PM2.5 Emission Factor Schedule Name"] = None
        self._data["NH3 Emission Factor"] = None
        self._data["NH3 Emission Factor Schedule Name"] = None
        self._data["NMVOC Emission Factor"] = None
        self._data["NMVOC Emission Factor Schedule Name"] = None
        self._data["Hg Emission Factor"] = None
        self._data["Hg Emission Factor Schedule Name"] = None
        self._data["Pb Emission Factor"] = None
        self._data["Pb Emission Factor Schedule Name"] = None
        self._data["Water Emission Factor"] = None
        self._data["Water Emission Factor Schedule Name"] = None
        self._data["Nuclear High Level Emission Factor"] = None
        self._data["Nuclear High Level Emission Factor Schedule Name"] = None
        self._data["Nuclear Low Level Emission Factor"] = None
        self._data["Nuclear Low Level Emission Factor Schedule Name"] = None
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
            self.existing_fuel_resource_name = None
        else:
            self.existing_fuel_resource_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.units_of_measure = None
        else:
            self.units_of_measure = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.energy_per_unit_factor = None
        else:
            self.energy_per_unit_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_energy_factor = None
        else:
            self.source_energy_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.source_energy_schedule_name = None
        else:
            self.source_energy_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.co2_emission_factor = None
        else:
            self.co2_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.co2_emission_factor_schedule_name = None
        else:
            self.co2_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.co_emission_factor = None
        else:
            self.co_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.co_emission_factor_schedule_name = None
        else:
            self.co_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ch4_emission_factor = None
        else:
            self.ch4_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ch4_emission_factor_schedule_name = None
        else:
            self.ch4_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nox_emission_factor = None
        else:
            self.nox_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nox_emission_factor_schedule_name = None
        else:
            self.nox_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.n2o_emission_factor = None
        else:
            self.n2o_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.n2o_emission_factor_schedule_name = None
        else:
            self.n2o_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.so2_emission_factor = None
        else:
            self.so2_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.so2_emission_factor_schedule_name = None
        else:
            self.so2_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pm_emission_factor = None
        else:
            self.pm_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pm_emission_factor_schedule_name = None
        else:
            self.pm_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pm10_emission_factor = None
        else:
            self.pm10_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pm10_emission_factor_schedule_name = None
        else:
            self.pm10_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pm2_5_emission_factor = None
        else:
            self.pm2_5_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pm2_5_emission_factor_schedule_name = None
        else:
            self.pm2_5_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nh3_emission_factor = None
        else:
            self.nh3_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nh3_emission_factor_schedule_name = None
        else:
            self.nh3_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nmvoc_emission_factor = None
        else:
            self.nmvoc_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nmvoc_emission_factor_schedule_name = None
        else:
            self.nmvoc_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hg_emission_factor = None
        else:
            self.hg_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.hg_emission_factor_schedule_name = None
        else:
            self.hg_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pb_emission_factor = None
        else:
            self.pb_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pb_emission_factor_schedule_name = None
        else:
            self.pb_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_emission_factor = None
        else:
            self.water_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_emission_factor_schedule_name = None
        else:
            self.water_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nuclear_high_level_emission_factor = None
        else:
            self.nuclear_high_level_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nuclear_high_level_emission_factor_schedule_name = None
        else:
            self.nuclear_high_level_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nuclear_low_level_emission_factor = None
        else:
            self.nuclear_low_level_emission_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.nuclear_low_level_emission_factor_schedule_name = None
        else:
            self.nuclear_low_level_emission_factor_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def existing_fuel_resource_name(self):
        """Get existing_fuel_resource_name

        Returns:
            str: the value of `existing_fuel_resource_name` or None if not set
        """
        return self._data["Existing Fuel Resource Name"]

    @existing_fuel_resource_name.setter
    def existing_fuel_resource_name(self, value=None):
        """  Corresponds to IDD Field `Existing Fuel Resource Name`

        Args:
            value (str): value for IDD Field `Existing Fuel Resource Name`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - FuelOil#1
                      - FuelOil#2
                      - Coal
                      - Gasoline
                      - Propane
                      - Diesel
                      - OtherFuel1
                      - OtherFuel2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.existing_fuel_resource_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.existing_fuel_resource_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.existing_fuel_resource_name`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["coal"] = "Coal"
            vals["gasoline"] = "Gasoline"
            vals["propane"] = "Propane"
            vals["diesel"] = "Diesel"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
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
                                     'field `FuelFactors.existing_fuel_resource_name`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `FuelFactors.existing_fuel_resource_name`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Existing Fuel Resource Name"] = value

    @property
    def units_of_measure(self):
        """Get units_of_measure

        Returns:
            str: the value of `units_of_measure` or None if not set
        """
        return self._data["Units of Measure"]

    @units_of_measure.setter
    def units_of_measure(self, value=None):
        """  Corresponds to IDD Field `Units of Measure`

        Args:
            value (str): value for IDD Field `Units of Measure`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.units_of_measure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.units_of_measure`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.units_of_measure`')
        self._data["Units of Measure"] = value

    @property
    def energy_per_unit_factor(self):
        """Get energy_per_unit_factor

        Returns:
            float: the value of `energy_per_unit_factor` or None if not set
        """
        return self._data["Energy per Unit Factor"]

    @energy_per_unit_factor.setter
    def energy_per_unit_factor(self, value=None):
        """  Corresponds to IDD Field `Energy per Unit Factor`

        Args:
            value (float): value for IDD Field `Energy per Unit Factor`
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
                                 ' for field `FuelFactors.energy_per_unit_factor`'.format(value))
        self._data["Energy per Unit Factor"] = value

    @property
    def source_energy_factor(self):
        """Get source_energy_factor

        Returns:
            float: the value of `source_energy_factor` or None if not set
        """
        return self._data["Source Energy Factor"]

    @source_energy_factor.setter
    def source_energy_factor(self, value=None):
        """  Corresponds to IDD Field `Source Energy Factor`

        Args:
            value (float): value for IDD Field `Source Energy Factor`
                Units: J/J
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
                                 ' for field `FuelFactors.source_energy_factor`'.format(value))
        self._data["Source Energy Factor"] = value

    @property
    def source_energy_schedule_name(self):
        """Get source_energy_schedule_name

        Returns:
            str: the value of `source_energy_schedule_name` or None if not set
        """
        return self._data["Source Energy Schedule Name"]

    @source_energy_schedule_name.setter
    def source_energy_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Source Energy Schedule Name`

        Args:
            value (str): value for IDD Field `Source Energy Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.source_energy_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.source_energy_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.source_energy_schedule_name`')
        self._data["Source Energy Schedule Name"] = value

    @property
    def co2_emission_factor(self):
        """Get co2_emission_factor

        Returns:
            float: the value of `co2_emission_factor` or None if not set
        """
        return self._data["CO2 Emission Factor"]

    @co2_emission_factor.setter
    def co2_emission_factor(self, value=None):
        """  Corresponds to IDD Field `CO2 Emission Factor`

        Args:
            value (float): value for IDD Field `CO2 Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.co2_emission_factor`'.format(value))
        self._data["CO2 Emission Factor"] = value

    @property
    def co2_emission_factor_schedule_name(self):
        """Get co2_emission_factor_schedule_name

        Returns:
            str: the value of `co2_emission_factor_schedule_name` or None if not set
        """
        return self._data["CO2 Emission Factor Schedule Name"]

    @co2_emission_factor_schedule_name.setter
    def co2_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `CO2 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `CO2 Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.co2_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.co2_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.co2_emission_factor_schedule_name`')
        self._data["CO2 Emission Factor Schedule Name"] = value

    @property
    def co_emission_factor(self):
        """Get co_emission_factor

        Returns:
            float: the value of `co_emission_factor` or None if not set
        """
        return self._data["CO Emission Factor"]

    @co_emission_factor.setter
    def co_emission_factor(self, value=None):
        """  Corresponds to IDD Field `CO Emission Factor`

        Args:
            value (float): value for IDD Field `CO Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.co_emission_factor`'.format(value))
        self._data["CO Emission Factor"] = value

    @property
    def co_emission_factor_schedule_name(self):
        """Get co_emission_factor_schedule_name

        Returns:
            str: the value of `co_emission_factor_schedule_name` or None if not set
        """
        return self._data["CO Emission Factor Schedule Name"]

    @co_emission_factor_schedule_name.setter
    def co_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `CO Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `CO Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.co_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.co_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.co_emission_factor_schedule_name`')
        self._data["CO Emission Factor Schedule Name"] = value

    @property
    def ch4_emission_factor(self):
        """Get ch4_emission_factor

        Returns:
            float: the value of `ch4_emission_factor` or None if not set
        """
        return self._data["CH4 Emission Factor"]

    @ch4_emission_factor.setter
    def ch4_emission_factor(self, value=None):
        """  Corresponds to IDD Field `CH4 Emission Factor`

        Args:
            value (float): value for IDD Field `CH4 Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.ch4_emission_factor`'.format(value))
        self._data["CH4 Emission Factor"] = value

    @property
    def ch4_emission_factor_schedule_name(self):
        """Get ch4_emission_factor_schedule_name

        Returns:
            str: the value of `ch4_emission_factor_schedule_name` or None if not set
        """
        return self._data["CH4 Emission Factor Schedule Name"]

    @ch4_emission_factor_schedule_name.setter
    def ch4_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `CH4 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `CH4 Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.ch4_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.ch4_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.ch4_emission_factor_schedule_name`')
        self._data["CH4 Emission Factor Schedule Name"] = value

    @property
    def nox_emission_factor(self):
        """Get nox_emission_factor

        Returns:
            float: the value of `nox_emission_factor` or None if not set
        """
        return self._data["NOx Emission Factor"]

    @nox_emission_factor.setter
    def nox_emission_factor(self, value=None):
        """  Corresponds to IDD Field `NOx Emission Factor`

        Args:
            value (float): value for IDD Field `NOx Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.nox_emission_factor`'.format(value))
        self._data["NOx Emission Factor"] = value

    @property
    def nox_emission_factor_schedule_name(self):
        """Get nox_emission_factor_schedule_name

        Returns:
            str: the value of `nox_emission_factor_schedule_name` or None if not set
        """
        return self._data["NOx Emission Factor Schedule Name"]

    @nox_emission_factor_schedule_name.setter
    def nox_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `NOx Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `NOx Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.nox_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.nox_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.nox_emission_factor_schedule_name`')
        self._data["NOx Emission Factor Schedule Name"] = value

    @property
    def n2o_emission_factor(self):
        """Get n2o_emission_factor

        Returns:
            float: the value of `n2o_emission_factor` or None if not set
        """
        return self._data["N2O Emission Factor"]

    @n2o_emission_factor.setter
    def n2o_emission_factor(self, value=None):
        """  Corresponds to IDD Field `N2O Emission Factor`

        Args:
            value (float): value for IDD Field `N2O Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.n2o_emission_factor`'.format(value))
        self._data["N2O Emission Factor"] = value

    @property
    def n2o_emission_factor_schedule_name(self):
        """Get n2o_emission_factor_schedule_name

        Returns:
            str: the value of `n2o_emission_factor_schedule_name` or None if not set
        """
        return self._data["N2O Emission Factor Schedule Name"]

    @n2o_emission_factor_schedule_name.setter
    def n2o_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `N2O Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `N2O Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.n2o_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.n2o_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.n2o_emission_factor_schedule_name`')
        self._data["N2O Emission Factor Schedule Name"] = value

    @property
    def so2_emission_factor(self):
        """Get so2_emission_factor

        Returns:
            float: the value of `so2_emission_factor` or None if not set
        """
        return self._data["SO2 Emission Factor"]

    @so2_emission_factor.setter
    def so2_emission_factor(self, value=None):
        """  Corresponds to IDD Field `SO2 Emission Factor`

        Args:
            value (float): value for IDD Field `SO2 Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.so2_emission_factor`'.format(value))
        self._data["SO2 Emission Factor"] = value

    @property
    def so2_emission_factor_schedule_name(self):
        """Get so2_emission_factor_schedule_name

        Returns:
            str: the value of `so2_emission_factor_schedule_name` or None if not set
        """
        return self._data["SO2 Emission Factor Schedule Name"]

    @so2_emission_factor_schedule_name.setter
    def so2_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `SO2 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `SO2 Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.so2_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.so2_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.so2_emission_factor_schedule_name`')
        self._data["SO2 Emission Factor Schedule Name"] = value

    @property
    def pm_emission_factor(self):
        """Get pm_emission_factor

        Returns:
            float: the value of `pm_emission_factor` or None if not set
        """
        return self._data["PM Emission Factor"]

    @pm_emission_factor.setter
    def pm_emission_factor(self, value=None):
        """  Corresponds to IDD Field `PM Emission Factor`

        Args:
            value (float): value for IDD Field `PM Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.pm_emission_factor`'.format(value))
        self._data["PM Emission Factor"] = value

    @property
    def pm_emission_factor_schedule_name(self):
        """Get pm_emission_factor_schedule_name

        Returns:
            str: the value of `pm_emission_factor_schedule_name` or None if not set
        """
        return self._data["PM Emission Factor Schedule Name"]

    @pm_emission_factor_schedule_name.setter
    def pm_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `PM Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `PM Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.pm_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.pm_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.pm_emission_factor_schedule_name`')
        self._data["PM Emission Factor Schedule Name"] = value

    @property
    def pm10_emission_factor(self):
        """Get pm10_emission_factor

        Returns:
            float: the value of `pm10_emission_factor` or None if not set
        """
        return self._data["PM10 Emission Factor"]

    @pm10_emission_factor.setter
    def pm10_emission_factor(self, value=None):
        """  Corresponds to IDD Field `PM10 Emission Factor`

        Args:
            value (float): value for IDD Field `PM10 Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.pm10_emission_factor`'.format(value))
        self._data["PM10 Emission Factor"] = value

    @property
    def pm10_emission_factor_schedule_name(self):
        """Get pm10_emission_factor_schedule_name

        Returns:
            str: the value of `pm10_emission_factor_schedule_name` or None if not set
        """
        return self._data["PM10 Emission Factor Schedule Name"]

    @pm10_emission_factor_schedule_name.setter
    def pm10_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `PM10 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `PM10 Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.pm10_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.pm10_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.pm10_emission_factor_schedule_name`')
        self._data["PM10 Emission Factor Schedule Name"] = value

    @property
    def pm2_5_emission_factor(self):
        """Get pm2_5_emission_factor

        Returns:
            float: the value of `pm2_5_emission_factor` or None if not set
        """
        return self._data["PM2.5 Emission Factor"]

    @pm2_5_emission_factor.setter
    def pm2_5_emission_factor(self, value=None):
        """  Corresponds to IDD Field `PM2.5 Emission Factor`

        Args:
            value (float): value for IDD Field `PM2.5 Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.pm2_5_emission_factor`'.format(value))
        self._data["PM2.5 Emission Factor"] = value

    @property
    def pm2_5_emission_factor_schedule_name(self):
        """Get pm2_5_emission_factor_schedule_name

        Returns:
            str: the value of `pm2_5_emission_factor_schedule_name` or None if not set
        """
        return self._data["PM2.5 Emission Factor Schedule Name"]

    @pm2_5_emission_factor_schedule_name.setter
    def pm2_5_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `PM2.5 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `PM2.5 Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.pm2_5_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.pm2_5_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.pm2_5_emission_factor_schedule_name`')
        self._data["PM2.5 Emission Factor Schedule Name"] = value

    @property
    def nh3_emission_factor(self):
        """Get nh3_emission_factor

        Returns:
            float: the value of `nh3_emission_factor` or None if not set
        """
        return self._data["NH3 Emission Factor"]

    @nh3_emission_factor.setter
    def nh3_emission_factor(self, value=None):
        """  Corresponds to IDD Field `NH3 Emission Factor`

        Args:
            value (float): value for IDD Field `NH3 Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.nh3_emission_factor`'.format(value))
        self._data["NH3 Emission Factor"] = value

    @property
    def nh3_emission_factor_schedule_name(self):
        """Get nh3_emission_factor_schedule_name

        Returns:
            str: the value of `nh3_emission_factor_schedule_name` or None if not set
        """
        return self._data["NH3 Emission Factor Schedule Name"]

    @nh3_emission_factor_schedule_name.setter
    def nh3_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `NH3 Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `NH3 Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.nh3_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.nh3_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.nh3_emission_factor_schedule_name`')
        self._data["NH3 Emission Factor Schedule Name"] = value

    @property
    def nmvoc_emission_factor(self):
        """Get nmvoc_emission_factor

        Returns:
            float: the value of `nmvoc_emission_factor` or None if not set
        """
        return self._data["NMVOC Emission Factor"]

    @nmvoc_emission_factor.setter
    def nmvoc_emission_factor(self, value=None):
        """  Corresponds to IDD Field `NMVOC Emission Factor`

        Args:
            value (float): value for IDD Field `NMVOC Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.nmvoc_emission_factor`'.format(value))
        self._data["NMVOC Emission Factor"] = value

    @property
    def nmvoc_emission_factor_schedule_name(self):
        """Get nmvoc_emission_factor_schedule_name

        Returns:
            str: the value of `nmvoc_emission_factor_schedule_name` or None if not set
        """
        return self._data["NMVOC Emission Factor Schedule Name"]

    @nmvoc_emission_factor_schedule_name.setter
    def nmvoc_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `NMVOC Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `NMVOC Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.nmvoc_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.nmvoc_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.nmvoc_emission_factor_schedule_name`')
        self._data["NMVOC Emission Factor Schedule Name"] = value

    @property
    def hg_emission_factor(self):
        """Get hg_emission_factor

        Returns:
            float: the value of `hg_emission_factor` or None if not set
        """
        return self._data["Hg Emission Factor"]

    @hg_emission_factor.setter
    def hg_emission_factor(self, value=None):
        """  Corresponds to IDD Field `Hg Emission Factor`

        Args:
            value (float): value for IDD Field `Hg Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.hg_emission_factor`'.format(value))
        self._data["Hg Emission Factor"] = value

    @property
    def hg_emission_factor_schedule_name(self):
        """Get hg_emission_factor_schedule_name

        Returns:
            str: the value of `hg_emission_factor_schedule_name` or None if not set
        """
        return self._data["Hg Emission Factor Schedule Name"]

    @hg_emission_factor_schedule_name.setter
    def hg_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Hg Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Hg Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.hg_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.hg_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.hg_emission_factor_schedule_name`')
        self._data["Hg Emission Factor Schedule Name"] = value

    @property
    def pb_emission_factor(self):
        """Get pb_emission_factor

        Returns:
            float: the value of `pb_emission_factor` or None if not set
        """
        return self._data["Pb Emission Factor"]

    @pb_emission_factor.setter
    def pb_emission_factor(self, value=None):
        """  Corresponds to IDD Field `Pb Emission Factor`

        Args:
            value (float): value for IDD Field `Pb Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.pb_emission_factor`'.format(value))
        self._data["Pb Emission Factor"] = value

    @property
    def pb_emission_factor_schedule_name(self):
        """Get pb_emission_factor_schedule_name

        Returns:
            str: the value of `pb_emission_factor_schedule_name` or None if not set
        """
        return self._data["Pb Emission Factor Schedule Name"]

    @pb_emission_factor_schedule_name.setter
    def pb_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Pb Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Pb Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.pb_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.pb_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.pb_emission_factor_schedule_name`')
        self._data["Pb Emission Factor Schedule Name"] = value

    @property
    def water_emission_factor(self):
        """Get water_emission_factor

        Returns:
            float: the value of `water_emission_factor` or None if not set
        """
        return self._data["Water Emission Factor"]

    @water_emission_factor.setter
    def water_emission_factor(self, value=None):
        """  Corresponds to IDD Field `Water Emission Factor`

        Args:
            value (float): value for IDD Field `Water Emission Factor`
                Units: L/MJ
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
                                 ' for field `FuelFactors.water_emission_factor`'.format(value))
        self._data["Water Emission Factor"] = value

    @property
    def water_emission_factor_schedule_name(self):
        """Get water_emission_factor_schedule_name

        Returns:
            str: the value of `water_emission_factor_schedule_name` or None if not set
        """
        return self._data["Water Emission Factor Schedule Name"]

    @water_emission_factor_schedule_name.setter
    def water_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Water Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Water Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.water_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.water_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.water_emission_factor_schedule_name`')
        self._data["Water Emission Factor Schedule Name"] = value

    @property
    def nuclear_high_level_emission_factor(self):
        """Get nuclear_high_level_emission_factor

        Returns:
            float: the value of `nuclear_high_level_emission_factor` or None if not set
        """
        return self._data["Nuclear High Level Emission Factor"]

    @nuclear_high_level_emission_factor.setter
    def nuclear_high_level_emission_factor(self, value=None):
        """  Corresponds to IDD Field `Nuclear High Level Emission Factor`

        Args:
            value (float): value for IDD Field `Nuclear High Level Emission Factor`
                Units: g/MJ
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
                                 ' for field `FuelFactors.nuclear_high_level_emission_factor`'.format(value))
        self._data["Nuclear High Level Emission Factor"] = value

    @property
    def nuclear_high_level_emission_factor_schedule_name(self):
        """Get nuclear_high_level_emission_factor_schedule_name

        Returns:
            str: the value of `nuclear_high_level_emission_factor_schedule_name` or None if not set
        """
        return self._data["Nuclear High Level Emission Factor Schedule Name"]

    @nuclear_high_level_emission_factor_schedule_name.setter
    def nuclear_high_level_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Nuclear High Level Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Nuclear High Level Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.nuclear_high_level_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.nuclear_high_level_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.nuclear_high_level_emission_factor_schedule_name`')
        self._data["Nuclear High Level Emission Factor Schedule Name"] = value

    @property
    def nuclear_low_level_emission_factor(self):
        """Get nuclear_low_level_emission_factor

        Returns:
            float: the value of `nuclear_low_level_emission_factor` or None if not set
        """
        return self._data["Nuclear Low Level Emission Factor"]

    @nuclear_low_level_emission_factor.setter
    def nuclear_low_level_emission_factor(self, value=None):
        """  Corresponds to IDD Field `Nuclear Low Level Emission Factor`

        Args:
            value (float): value for IDD Field `Nuclear Low Level Emission Factor`
                Units: m3/MJ
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
                                 ' for field `FuelFactors.nuclear_low_level_emission_factor`'.format(value))
        self._data["Nuclear Low Level Emission Factor"] = value

    @property
    def nuclear_low_level_emission_factor_schedule_name(self):
        """Get nuclear_low_level_emission_factor_schedule_name

        Returns:
            str: the value of `nuclear_low_level_emission_factor_schedule_name` or None if not set
        """
        return self._data["Nuclear Low Level Emission Factor Schedule Name"]

    @nuclear_low_level_emission_factor_schedule_name.setter
    def nuclear_low_level_emission_factor_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Nuclear Low Level Emission Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Nuclear Low Level Emission Factor Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `FuelFactors.nuclear_low_level_emission_factor_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `FuelFactors.nuclear_low_level_emission_factor_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `FuelFactors.nuclear_low_level_emission_factor_schedule_name`')
        self._data["Nuclear Low Level Emission Factor Schedule Name"] = value

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
                    raise ValueError("Required field FuelFactors:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field FuelFactors:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for FuelFactors: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for FuelFactors: {} / {}".format(out_fields,
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

class OutputDiagnostics(object):
    """ Corresponds to IDD object `Output:Diagnostics`
        Special keys to produce certain warning messages or effect certain simulation characteristics.
    """
    internal_name = "Output:Diagnostics"
    field_count = 2
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:Diagnostics`
        """
        self._data = OrderedDict()
        self._data["Key 1"] = None
        self._data["Key 2"] = None
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
            self.key_1 = None
        else:
            self.key_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.key_2 = None
        else:
            self.key_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def key_1(self):
        """Get key_1

        Returns:
            str: the value of `key_1` or None if not set
        """
        return self._data["Key 1"]

    @key_1.setter
    def key_1(self, value=None):
        """  Corresponds to IDD Field `Key 1`

        Args:
            value (str): value for IDD Field `Key 1`
                Accepted values are:
                      - DisplayAllWarnings
                      - DisplayExtraWarnings
                      - DisplayUnusedSchedules
                      - DisplayUnusedObjects
                      - DisplayAdvancedReportVariables
                      - DisplayZoneAirHeatBalanceOffBalance
                      - DoNotMirrorDetachedShading
                      - DisplayWeatherMissingDataWarnings
                      - ReportDuringWarmup
                      - ReportDetailedWarmupConvergence
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputDiagnostics.key_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputDiagnostics.key_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputDiagnostics.key_1`')
            vals = {}
            vals["displayallwarnings"] = "DisplayAllWarnings"
            vals["displayextrawarnings"] = "DisplayExtraWarnings"
            vals["displayunusedschedules"] = "DisplayUnusedSchedules"
            vals["displayunusedobjects"] = "DisplayUnusedObjects"
            vals["displayadvancedreportvariables"] = "DisplayAdvancedReportVariables"
            vals["displayzoneairheatbalanceoffbalance"] = "DisplayZoneAirHeatBalanceOffBalance"
            vals["donotmirrordetachedshading"] = "DoNotMirrorDetachedShading"
            vals["displayweathermissingdatawarnings"] = "DisplayWeatherMissingDataWarnings"
            vals["reportduringwarmup"] = "ReportDuringWarmup"
            vals["reportdetailedwarmupconvergence"] = "ReportDetailedWarmupConvergence"
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
                                     'field `OutputDiagnostics.key_1`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputDiagnostics.key_1`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Key 1"] = value

    @property
    def key_2(self):
        """Get key_2

        Returns:
            str: the value of `key_2` or None if not set
        """
        return self._data["Key 2"]

    @key_2.setter
    def key_2(self, value=None):
        """  Corresponds to IDD Field `Key 2`

        Args:
            value (str): value for IDD Field `Key 2`
                Accepted values are:
                      - DisplayAllWarnings
                      - DisplayExtraWarnings
                      - DisplayUnusedSchedules
                      - DisplayUnusedObjects
                      - DisplayAdvancedReportVariables
                      - DisplayZoneAirHeatBalanceOffBalance
                      - DoNotMirrorDetachedShading
                      - DisplayWeatherMissingDataWarnings
                      - ReportDuringWarmup
                      - ReportDetailedWarmupConvergence
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputDiagnostics.key_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputDiagnostics.key_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputDiagnostics.key_2`')
            vals = {}
            vals["displayallwarnings"] = "DisplayAllWarnings"
            vals["displayextrawarnings"] = "DisplayExtraWarnings"
            vals["displayunusedschedules"] = "DisplayUnusedSchedules"
            vals["displayunusedobjects"] = "DisplayUnusedObjects"
            vals["displayadvancedreportvariables"] = "DisplayAdvancedReportVariables"
            vals["displayzoneairheatbalanceoffbalance"] = "DisplayZoneAirHeatBalanceOffBalance"
            vals["donotmirrordetachedshading"] = "DoNotMirrorDetachedShading"
            vals["displayweathermissingdatawarnings"] = "DisplayWeatherMissingDataWarnings"
            vals["reportduringwarmup"] = "ReportDuringWarmup"
            vals["reportdetailedwarmupconvergence"] = "ReportDetailedWarmupConvergence"
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
                                     'field `OutputDiagnostics.key_2`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputDiagnostics.key_2`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Key 2"] = value

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
                    raise ValueError("Required field OutputDiagnostics:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputDiagnostics:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputDiagnostics: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputDiagnostics: {} / {}".format(out_fields,
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

class OutputDebuggingData(object):
    """ Corresponds to IDD object `Output:DebuggingData`
        switch eplusout.dbg file on or off
    """
    internal_name = "Output:DebuggingData"
    field_count = 2
    required_fields = []
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:DebuggingData`
        """
        self._data = OrderedDict()
        self._data["Report Debugging Data"] = None
        self._data["Report During Warmup"] = None
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
            self.report_debugging_data = None
        else:
            self.report_debugging_data = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.report_during_warmup = None
        else:
            self.report_during_warmup = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def report_debugging_data(self):
        """Get report_debugging_data

        Returns:
            float: the value of `report_debugging_data` or None if not set
        """
        return self._data["Report Debugging Data"]

    @report_debugging_data.setter
    def report_debugging_data(self, value=None):
        """  Corresponds to IDD Field `Report Debugging Data`
        value=1 then yes all others no

        Args:
            value (float): value for IDD Field `Report Debugging Data`
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
                                 ' for field `OutputDebuggingData.report_debugging_data`'.format(value))
        self._data["Report Debugging Data"] = value

    @property
    def report_during_warmup(self):
        """Get report_during_warmup

        Returns:
            float: the value of `report_during_warmup` or None if not set
        """
        return self._data["Report During Warmup"]

    @report_during_warmup.setter
    def report_during_warmup(self, value=None):
        """  Corresponds to IDD Field `Report During Warmup`
        value=1 then always even during warmup  all others no

        Args:
            value (float): value for IDD Field `Report During Warmup`
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
                                 ' for field `OutputDebuggingData.report_during_warmup`'.format(value))
        self._data["Report During Warmup"] = value

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
                    raise ValueError("Required field OutputDebuggingData:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputDebuggingData:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputDebuggingData: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputDebuggingData: {} / {}".format(out_fields,
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

class OutputPreprocessorMessage(object):
    """ Corresponds to IDD object `Output:PreprocessorMessage`
        This object does not come from a user input.  This is generated by a pre-processor
        so that various conditions can be gracefully passed on by the InputProcessor.
    """
    internal_name = "Output:PreprocessorMessage"
    field_count = 12
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:PreprocessorMessage`
        """
        self._data = OrderedDict()
        self._data["Preprocessor Name"] = None
        self._data["Error Severity"] = None
        self._data["Message Line 1"] = None
        self._data["Message Line 2"] = None
        self._data["Message Line 3"] = None
        self._data["Message Line 4"] = None
        self._data["Message Line 5"] = None
        self._data["Message Line 6"] = None
        self._data["Message Line 7"] = None
        self._data["Message Line 8"] = None
        self._data["Message Line 9"] = None
        self._data["Message Line 10"] = None
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
            self.preprocessor_name = None
        else:
            self.preprocessor_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.error_severity = None
        else:
            self.error_severity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_1 = None
        else:
            self.message_line_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_2 = None
        else:
            self.message_line_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_3 = None
        else:
            self.message_line_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_4 = None
        else:
            self.message_line_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_5 = None
        else:
            self.message_line_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_6 = None
        else:
            self.message_line_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_7 = None
        else:
            self.message_line_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_8 = None
        else:
            self.message_line_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_9 = None
        else:
            self.message_line_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.message_line_10 = None
        else:
            self.message_line_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def preprocessor_name(self):
        """Get preprocessor_name

        Returns:
            str: the value of `preprocessor_name` or None if not set
        """
        return self._data["Preprocessor Name"]

    @preprocessor_name.setter
    def preprocessor_name(self, value=None):
        """  Corresponds to IDD Field `Preprocessor Name`

        Args:
            value (str): value for IDD Field `Preprocessor Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.preprocessor_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.preprocessor_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.preprocessor_name`')
        self._data["Preprocessor Name"] = value

    @property
    def error_severity(self):
        """Get error_severity

        Returns:
            str: the value of `error_severity` or None if not set
        """
        return self._data["Error Severity"]

    @error_severity.setter
    def error_severity(self, value=None):
        """  Corresponds to IDD Field `Error Severity`
        Depending on type, InputProcessor may terminate the program.

        Args:
            value (str): value for IDD Field `Error Severity`
                Accepted values are:
                      - Information
                      - Warning
                      - Severe
                      - Fatal
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.error_severity`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.error_severity`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.error_severity`')
            vals = {}
            vals["information"] = "Information"
            vals["warning"] = "Warning"
            vals["severe"] = "Severe"
            vals["fatal"] = "Fatal"
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
                                     'field `OutputPreprocessorMessage.error_severity`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputPreprocessorMessage.error_severity`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Error Severity"] = value

    @property
    def message_line_1(self):
        """Get message_line_1

        Returns:
            str: the value of `message_line_1` or None if not set
        """
        return self._data["Message Line 1"]

    @message_line_1.setter
    def message_line_1(self, value=None):
        """  Corresponds to IDD Field `Message Line 1`

        Args:
            value (str): value for IDD Field `Message Line 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_1`')
        self._data["Message Line 1"] = value

    @property
    def message_line_2(self):
        """Get message_line_2

        Returns:
            str: the value of `message_line_2` or None if not set
        """
        return self._data["Message Line 2"]

    @message_line_2.setter
    def message_line_2(self, value=None):
        """  Corresponds to IDD Field `Message Line 2`

        Args:
            value (str): value for IDD Field `Message Line 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_2`')
        self._data["Message Line 2"] = value

    @property
    def message_line_3(self):
        """Get message_line_3

        Returns:
            str: the value of `message_line_3` or None if not set
        """
        return self._data["Message Line 3"]

    @message_line_3.setter
    def message_line_3(self, value=None):
        """  Corresponds to IDD Field `Message Line 3`

        Args:
            value (str): value for IDD Field `Message Line 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_3`')
        self._data["Message Line 3"] = value

    @property
    def message_line_4(self):
        """Get message_line_4

        Returns:
            str: the value of `message_line_4` or None if not set
        """
        return self._data["Message Line 4"]

    @message_line_4.setter
    def message_line_4(self, value=None):
        """  Corresponds to IDD Field `Message Line 4`

        Args:
            value (str): value for IDD Field `Message Line 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_4`')
        self._data["Message Line 4"] = value

    @property
    def message_line_5(self):
        """Get message_line_5

        Returns:
            str: the value of `message_line_5` or None if not set
        """
        return self._data["Message Line 5"]

    @message_line_5.setter
    def message_line_5(self, value=None):
        """  Corresponds to IDD Field `Message Line 5`

        Args:
            value (str): value for IDD Field `Message Line 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_5`')
        self._data["Message Line 5"] = value

    @property
    def message_line_6(self):
        """Get message_line_6

        Returns:
            str: the value of `message_line_6` or None if not set
        """
        return self._data["Message Line 6"]

    @message_line_6.setter
    def message_line_6(self, value=None):
        """  Corresponds to IDD Field `Message Line 6`

        Args:
            value (str): value for IDD Field `Message Line 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_6`')
        self._data["Message Line 6"] = value

    @property
    def message_line_7(self):
        """Get message_line_7

        Returns:
            str: the value of `message_line_7` or None if not set
        """
        return self._data["Message Line 7"]

    @message_line_7.setter
    def message_line_7(self, value=None):
        """  Corresponds to IDD Field `Message Line 7`

        Args:
            value (str): value for IDD Field `Message Line 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_7`')
        self._data["Message Line 7"] = value

    @property
    def message_line_8(self):
        """Get message_line_8

        Returns:
            str: the value of `message_line_8` or None if not set
        """
        return self._data["Message Line 8"]

    @message_line_8.setter
    def message_line_8(self, value=None):
        """  Corresponds to IDD Field `Message Line 8`

        Args:
            value (str): value for IDD Field `Message Line 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_8`')
        self._data["Message Line 8"] = value

    @property
    def message_line_9(self):
        """Get message_line_9

        Returns:
            str: the value of `message_line_9` or None if not set
        """
        return self._data["Message Line 9"]

    @message_line_9.setter
    def message_line_9(self, value=None):
        """  Corresponds to IDD Field `Message Line 9`

        Args:
            value (str): value for IDD Field `Message Line 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_9`')
        self._data["Message Line 9"] = value

    @property
    def message_line_10(self):
        """Get message_line_10

        Returns:
            str: the value of `message_line_10` or None if not set
        """
        return self._data["Message Line 10"]

    @message_line_10.setter
    def message_line_10(self, value=None):
        """  Corresponds to IDD Field `Message Line 10`

        Args:
            value (str): value for IDD Field `Message Line 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputPreprocessorMessage.message_line_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputPreprocessorMessage.message_line_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputPreprocessorMessage.message_line_10`')
        self._data["Message Line 10"] = value

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
                    raise ValueError("Required field OutputPreprocessorMessage:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputPreprocessorMessage:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputPreprocessorMessage: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputPreprocessorMessage: {} / {}".format(out_fields,
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