from collections import OrderedDict

class WindowPropertyShadingControl(object):
    """ Corresponds to IDD object `WindowProperty:ShadingControl`
        Specifies the type, location, and controls for window shades, window blinds, and
        switchable glazing. Referenced by the surface objects for exterior windows and glass
        doors (ref: FenestrationSurface:Detailed, Window, and GlazedDoor).
    """
    internal_name = "WindowProperty:ShadingControl"
    field_count = 12

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowProperty:ShadingControl`
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
            self.shading_type = None
        else:
            self.shading_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_with_shading_name = None
        else:
            self.construction_with_shading_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shading_control_type = None
        else:
            self.shading_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint = None
        else:
            self.setpoint = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shading_control_is_scheduled = None
        else:
            self.shading_control_is_scheduled = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.glare_control_is_active = None
        else:
            self.glare_control_is_active = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.shading_device_material_name = None
        else:
            self.shading_device_material_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.type_of_slat_angle_control_for_blinds = None
        else:
            self.type_of_slat_angle_control_for_blinds = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.slat_angle_schedule_name = None
        else:
            self.slat_angle_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.setpoint_2 = None
        else:
            self.setpoint_2 = vals[i]
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
        Referenced by surfaces that are exterior windows
        Not used by interzone windows

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
    def shading_type(self):
        """Get shading_type

        Returns:
            str: the value of `shading_type` or None if not set
        """
        return self._data["Shading Type"]

    @shading_type.setter
    def shading_type(self, value=None):
        """  Corresponds to IDD Field `shading_type`

        Args:
            value (str): value for IDD Field `shading_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `shading_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shading_type`')
            vals = set()
            vals.add("InteriorShade")
            vals.add("ExteriorShade")
            vals.add("ExteriorScreen")
            vals.add("InteriorBlind")
            vals.add("ExteriorBlind")
            vals.add("BetweenGlassShade")
            vals.add("BetweenGlassBlind")
            vals.add("SwitchableGlazing")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `shading_type`'.format(value))

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
        """  Corresponds to IDD Field `construction_with_shading_name`
        Required if Shading Type = SwitchableGlazing
        Required if Shading Type = interior or exterior shade or blind, or exterior screen, and
        "Shading Device Material Name" is not specified.
        If both "Construction with Shading Name" and "Shading Device Material Name" are entered,
        the former takes precedence.

        Args:
            value (str): value for IDD Field `construction_with_shading_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_with_shading_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_with_shading_name`')

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
        """  Corresponds to IDD Field `shading_control_type`
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
            value (str): value for IDD Field `shading_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `shading_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shading_control_type`')
            vals = set()
            vals.add("AlwaysOn")
            vals.add("AlwaysOff")
            vals.add("OnIfScheduleAllows")
            vals.add("OnIfHighSolarOnWindow")
            vals.add("OnIfHighHorizontalSolar")
            vals.add("OnIfHighOutdoorAirTemperature")
            vals.add("OnIfHighZoneAirTemperature")
            vals.add("OnIfHighZoneCooling")
            vals.add("OnIfHighGlare")
            vals.add("MeetDaylightIlluminanceSetpoint")
            vals.add("OnNightIfLowOutdoorTempAndOffDay")
            vals.add("OnNightIfLowInsideTempAndOffDay")
            vals.add("OnNightIfHeatingAndOffDay")
            vals.add("OnNightIfLowOutdoorTempAndOnDayIfCooling")
            vals.add("OnNightIfHeatingAndOnDayIfCooling")
            vals.add("OffNightAndOnDayIfCoolingAndHighSolarOnWindow")
            vals.add("OnNightAndOnDayIfCoolingAndHighSolarOnWindow")
            vals.add("OnIfHighOutdoorAirTempAndHighSolarOnWindow")
            vals.add("OnIfHighOutdoorAirTempAndHighHorizontalSolar")
            vals.add("OnIfHighZoneAirTempAndHighSolarOnWindow")
            vals.add("OnIfHighZoneAirTempAndHighHorizontalSolar")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `shading_control_type`'.format(value))

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
        """  Corresponds to IDD Field `schedule_name`
        Required if Shading Control Is Scheduled = Yes.
        If schedule value = 1, shading control is active, i.e., shading can take place only
        if the control test passes. If schedule value = 0, shading is off whether or not
        the control test passes. Schedule Name is required if Shading Control Is Scheduled = Yes.
        If Schedule Name is not specified, shading control is assumed to be active at all times.

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

    @property
    def setpoint(self):
        """Get setpoint

        Returns:
            float: the value of `setpoint` or None if not set
        """
        return self._data["Setpoint"]

    @setpoint.setter
    def setpoint(self, value=None):
        """  Corresponds to IDD Field `setpoint`
        W/m2 for solar-based controls, W for cooling- or heating-based controls,
        deg C for temperature-based controls.
        Unused for Shading Control Type = AlwaysOn, AlwaysOff, OnIfScheduleAllows,
        OnIfHighGlare, Glare, and DaylightIlluminance

        Args:
            value (float): value for IDD Field `setpoint`
                Unit: W/m2, W or deg C
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
                                 'for field `setpoint`'.format(value))

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
        """  Corresponds to IDD Field `shading_control_is_scheduled`
        If Yes, Schedule Name is required; if No, Schedule Name is not used.
        Shading Control Is Scheduled = Yes is required if Shading Control Type = OnIfScheduleAllows.

        Args:
            value (str): value for IDD Field `shading_control_is_scheduled`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `shading_control_is_scheduled`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shading_control_is_scheduled`')
            vals = set()
            vals.add("No")
            vals.add("Yes")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `shading_control_is_scheduled`'.format(value))

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
        """  Corresponds to IDD Field `glare_control_is_active`
        If Yes and window is in a daylit zone, shading is on if zone's discomfort glare index exceeds
        the maximum discomfort glare index specified in the Daylighting object referenced by the zone.
        The glare test is OR'ed with the test specified by Shading Control Type.
        Glare Control Is Active = Yes is required if Shading Control Type = OnIfHighGlare.

        Args:
            value (str): value for IDD Field `glare_control_is_active`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `glare_control_is_active`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `glare_control_is_active`')
            vals = set()
            vals.add("No")
            vals.add("Yes")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `glare_control_is_active`'.format(value))

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
        """  Corresponds to IDD Field `shading_device_material_name`
        Enter the name of a WindowMaterial:Shade, WindowMaterial:Screen or WindowMaterial:Blind object.
        Required if "Construction with Shading Name" is not specified.
        Not used if Shading Control Type = SwitchableGlazing, BetweenGlassShade, or BetweenGlassBlind.
        If both "Construction with Shading Name" and "Shading Device Material Name" are entered,
        the former takes precedence.

        Args:
            value (str): value for IDD Field `shading_device_material_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `shading_device_material_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `shading_device_material_name`')

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
        """  Corresponds to IDD Field `type_of_slat_angle_control_for_blinds`
        Used only if Shading Type = InteriorBlind, ExteriorBlind or BetweenGlassBlind.
        If choice is ScheduledSlatAngle then Slat Angle Schedule Name is required.

        Args:
            value (str): value for IDD Field `type_of_slat_angle_control_for_blinds`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_slat_angle_control_for_blinds`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_slat_angle_control_for_blinds`')
            vals = set()
            vals.add("FixedSlatAngle")
            vals.add("ScheduledSlatAngle")
            vals.add("BlockBeamSolar")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `type_of_slat_angle_control_for_blinds`'.format(value))

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
        """  Corresponds to IDD Field `slat_angle_schedule_name`
        Used only if Shading Type = InteriorBlind, ExteriorBlind or BetweenGlassBlind.
        Required if Type of Slat Angle Control for Blinds = ScheduledSlatAngle
        Schedule values should be degrees (0 minimum, 180 maximum)

        Args:
            value (str): value for IDD Field `slat_angle_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `slat_angle_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `slat_angle_schedule_name`')

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
        """  Corresponds to IDD Field `setpoint_2`
        W/m2 for solar-based controls, deg C for temperature-based controls.
        Used only as the second setpoint for the following two-setpoint control types:
        OnIfHighOutdoorAirTempAndHighSolarOnWindow, OnIfHighOutdoorAirTempAndHighHorizontalSolar,
        OnIfHighZoneAirTempAndHighSolarOnWindow, and OnIfHighZoneAirTempAndHighHorizontalSolar

        Args:
            value (float): value for IDD Field `setpoint_2`
                Unit: W/m2 or deg C
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
                                 'for field `setpoint_2`'.format(value))

        self._data["Setpoint 2"] = value

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
        out.append(self._to_str(self.shading_type))
        out.append(self._to_str(self.construction_with_shading_name))
        out.append(self._to_str(self.shading_control_type))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.setpoint))
        out.append(self._to_str(self.shading_control_is_scheduled))
        out.append(self._to_str(self.glare_control_is_active))
        out.append(self._to_str(self.shading_device_material_name))
        out.append(self._to_str(self.type_of_slat_angle_control_for_blinds))
        out.append(self._to_str(self.slat_angle_schedule_name))
        out.append(self._to_str(self.setpoint_2))
        return ",".join(out)

class WindowPropertyFrameAndDivider(object):
    """ Corresponds to IDD object `WindowProperty:FrameAndDivider`
        Specifies the dimensions of a window frame, dividers, and inside reveal surfaces.
        Referenced by the surface objects for exterior windows and glass doors
        (ref: FenestrationSurface:Detailed, Window, and GlazedDoor).
    """
    internal_name = "WindowProperty:FrameAndDivider"
    field_count = 25

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowProperty:FrameAndDivider`
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
            self.frame_width = None
        else:
            self.frame_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_outside_projection = None
        else:
            self.frame_outside_projection = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_inside_projection = None
        else:
            self.frame_inside_projection = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_conductance = None
        else:
            self.frame_conductance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance = None
        else:
            self.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_solar_absorptance = None
        else:
            self.frame_solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_visible_absorptance = None
        else:
            self.frame_visible_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.frame_thermal_hemispherical_emissivity = None
        else:
            self.frame_thermal_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_type = None
        else:
            self.divider_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_width = None
        else:
            self.divider_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_horizontal_dividers = None
        else:
            self.number_of_horizontal_dividers = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_vertical_dividers = None
        else:
            self.number_of_vertical_dividers = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_outside_projection = None
        else:
            self.divider_outside_projection = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_inside_projection = None
        else:
            self.divider_inside_projection = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_conductance = None
        else:
            self.divider_conductance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance = None
        else:
            self.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_solar_absorptance = None
        else:
            self.divider_solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_visible_absorptance = None
        else:
            self.divider_visible_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.divider_thermal_hemispherical_emissivity = None
        else:
            self.divider_thermal_hemispherical_emissivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_reveal_solar_absorptance = None
        else:
            self.outside_reveal_solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_sill_depth = None
        else:
            self.inside_sill_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_sill_solar_absorptance = None
        else:
            self.inside_sill_solar_absorptance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_reveal_depth = None
        else:
            self.inside_reveal_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_reveal_solar_absorptance = None
        else:
            self.inside_reveal_solar_absorptance = vals[i]
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
        Referenced by surfaces that are exterior windows
        Not used by interzone windows

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
    def frame_width(self):
        """Get frame_width

        Returns:
            float: the value of `frame_width` or None if not set
        """
        return self._data["Frame Width"]

    @frame_width.setter
    def frame_width(self, value=0.0 ):
        """  Corresponds to IDD Field `frame_width`
        Width of frame in plane of window
        Frame width assumed the same on all sides of window

        Args:
            value (float): value for IDD Field `frame_width`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `frame_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `frame_width`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `frame_width`')

        self._data["Frame Width"] = value

    @property
    def frame_outside_projection(self):
        """Get frame_outside_projection

        Returns:
            float: the value of `frame_outside_projection` or None if not set
        """
        return self._data["Frame Outside Projection"]

    @frame_outside_projection.setter
    def frame_outside_projection(self, value=0.0 ):
        """  Corresponds to IDD Field `frame_outside_projection`
        Amount that frame projects outward from the outside face of the glazing

        Args:
            value (float): value for IDD Field `frame_outside_projection`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `frame_outside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `frame_outside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `frame_outside_projection`')

        self._data["Frame Outside Projection"] = value

    @property
    def frame_inside_projection(self):
        """Get frame_inside_projection

        Returns:
            float: the value of `frame_inside_projection` or None if not set
        """
        return self._data["Frame Inside Projection"]

    @frame_inside_projection.setter
    def frame_inside_projection(self, value=0.0 ):
        """  Corresponds to IDD Field `frame_inside_projection`
        Amount that frame projects inward from the inside face of the glazing

        Args:
            value (float): value for IDD Field `frame_inside_projection`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `frame_inside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `frame_inside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `frame_inside_projection`')

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
        """  Corresponds to IDD Field `frame_conductance`
        Effective conductance of frame
        Excludes air films
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `frame_conductance`
                Unit: W/m2-K
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
                                 'for field `frame_conductance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `frame_conductance`')

        self._data["Frame Conductance"] = value

    @property
    def ratio_of_frameedge_glass_conductance_to_centerofglass_conductance(self):
        """Get ratio_of_frameedge_glass_conductance_to_centerofglass_conductance

        Returns:
            float: the value of `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance` or None if not set
        """
        return self._data["Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance"]

    @ratio_of_frameedge_glass_conductance_to_centerofglass_conductance.setter
    def ratio_of_frameedge_glass_conductance_to_centerofglass_conductance(self, value=1.0 ):
        """  Corresponds to IDD Field `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`
        Excludes air films; applies only to multipane windows
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `ratio_of_frameedge_glass_conductance_to_centerofglass_conductance`')

        self._data["Ratio of Frame-Edge Glass Conductance to Center-Of-Glass Conductance"] = value

    @property
    def frame_solar_absorptance(self):
        """Get frame_solar_absorptance

        Returns:
            float: the value of `frame_solar_absorptance` or None if not set
        """
        return self._data["Frame Solar Absorptance"]

    @frame_solar_absorptance.setter
    def frame_solar_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `frame_solar_absorptance`
        Assumed same on outside and inside of frame

        Args:
            value (float): value for IDD Field `frame_solar_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `frame_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `frame_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `frame_solar_absorptance`')

        self._data["Frame Solar Absorptance"] = value

    @property
    def frame_visible_absorptance(self):
        """Get frame_visible_absorptance

        Returns:
            float: the value of `frame_visible_absorptance` or None if not set
        """
        return self._data["Frame Visible Absorptance"]

    @frame_visible_absorptance.setter
    def frame_visible_absorptance(self, value=0.7 ):
        """  Corresponds to IDD Field `frame_visible_absorptance`
        Assumed same on outside and inside of frame

        Args:
            value (float): value for IDD Field `frame_visible_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `frame_visible_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `frame_visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `frame_visible_absorptance`')

        self._data["Frame Visible Absorptance"] = value

    @property
    def frame_thermal_hemispherical_emissivity(self):
        """Get frame_thermal_hemispherical_emissivity

        Returns:
            float: the value of `frame_thermal_hemispherical_emissivity` or None if not set
        """
        return self._data["Frame Thermal Hemispherical Emissivity"]

    @frame_thermal_hemispherical_emissivity.setter
    def frame_thermal_hemispherical_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `frame_thermal_hemispherical_emissivity`
        Assumed same on outside and inside of frame

        Args:
            value (float): value for IDD Field `frame_thermal_hemispherical_emissivity`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `frame_thermal_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `frame_thermal_hemispherical_emissivity`')

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
        """  Corresponds to IDD Field `divider_type`

        Args:
            value (str): value for IDD Field `divider_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `divider_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `divider_type`')
            vals = set()
            vals.add("DividedLite")
            vals.add("Suspended")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `divider_type`'.format(value))

        self._data["Divider Type"] = value

    @property
    def divider_width(self):
        """Get divider_width

        Returns:
            float: the value of `divider_width` or None if not set
        """
        return self._data["Divider Width"]

    @divider_width.setter
    def divider_width(self, value=0.0 ):
        """  Corresponds to IDD Field `divider_width`
        Width of dividers in plane of window
        Width assumed the same for all dividers

        Args:
            value (float): value for IDD Field `divider_width`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `divider_width`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `divider_width`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `divider_width`')

        self._data["Divider Width"] = value

    @property
    def number_of_horizontal_dividers(self):
        """Get number_of_horizontal_dividers

        Returns:
            float: the value of `number_of_horizontal_dividers` or None if not set
        """
        return self._data["Number of Horizontal Dividers"]

    @number_of_horizontal_dividers.setter
    def number_of_horizontal_dividers(self, value=0.0 ):
        """  Corresponds to IDD Field `number_of_horizontal_dividers`
        "Horizontal" means parallel to local window X-axis

        Args:
            value (float): value for IDD Field `number_of_horizontal_dividers`
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
                                 'for field `number_of_horizontal_dividers`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `number_of_horizontal_dividers`')

        self._data["Number of Horizontal Dividers"] = value

    @property
    def number_of_vertical_dividers(self):
        """Get number_of_vertical_dividers

        Returns:
            float: the value of `number_of_vertical_dividers` or None if not set
        """
        return self._data["Number of Vertical Dividers"]

    @number_of_vertical_dividers.setter
    def number_of_vertical_dividers(self, value=0.0 ):
        """  Corresponds to IDD Field `number_of_vertical_dividers`
        "Vertical" means parallel to local window Y-axis

        Args:
            value (float): value for IDD Field `number_of_vertical_dividers`
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
                                 'for field `number_of_vertical_dividers`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `number_of_vertical_dividers`')

        self._data["Number of Vertical Dividers"] = value

    @property
    def divider_outside_projection(self):
        """Get divider_outside_projection

        Returns:
            float: the value of `divider_outside_projection` or None if not set
        """
        return self._data["Divider Outside Projection"]

    @divider_outside_projection.setter
    def divider_outside_projection(self, value=0.0 ):
        """  Corresponds to IDD Field `divider_outside_projection`
        Amount that divider projects outward from the outside face of the glazing
        Outside projection assumed the same for all divider elements

        Args:
            value (float): value for IDD Field `divider_outside_projection`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `divider_outside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `divider_outside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `divider_outside_projection`')

        self._data["Divider Outside Projection"] = value

    @property
    def divider_inside_projection(self):
        """Get divider_inside_projection

        Returns:
            float: the value of `divider_inside_projection` or None if not set
        """
        return self._data["Divider Inside Projection"]

    @divider_inside_projection.setter
    def divider_inside_projection(self, value=0.0 ):
        """  Corresponds to IDD Field `divider_inside_projection`
        Amount that divider projects inward from the inside face of the glazing
        Inside projection assumed the same for all divider elements

        Args:
            value (float): value for IDD Field `divider_inside_projection`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `divider_inside_projection`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `divider_inside_projection`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `divider_inside_projection`')

        self._data["Divider Inside Projection"] = value

    @property
    def divider_conductance(self):
        """Get divider_conductance

        Returns:
            float: the value of `divider_conductance` or None if not set
        """
        return self._data["Divider Conductance"]

    @divider_conductance.setter
    def divider_conductance(self, value=0.0 ):
        """  Corresponds to IDD Field `divider_conductance`
        Effective conductance of divider
        Excludes air films
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `divider_conductance`
                Unit: W/m2-K
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
                                 'for field `divider_conductance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `divider_conductance`')

        self._data["Divider Conductance"] = value

    @property
    def ratio_of_divideredge_glass_conductance_to_centerofglass_conductance(self):
        """Get ratio_of_divideredge_glass_conductance_to_centerofglass_conductance

        Returns:
            float: the value of `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance` or None if not set
        """
        return self._data["Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance"]

    @ratio_of_divideredge_glass_conductance_to_centerofglass_conductance.setter
    def ratio_of_divideredge_glass_conductance_to_centerofglass_conductance(self, value=1.0 ):
        """  Corresponds to IDD Field `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`
        Excludes air films
        Obtained from WINDOW 5 or other 2-D calculation

        Args:
            value (float): value for IDD Field `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `ratio_of_divideredge_glass_conductance_to_centerofglass_conductance`')

        self._data["Ratio of Divider-Edge Glass Conductance to Center-Of-Glass Conductance"] = value

    @property
    def divider_solar_absorptance(self):
        """Get divider_solar_absorptance

        Returns:
            float: the value of `divider_solar_absorptance` or None if not set
        """
        return self._data["Divider Solar Absorptance"]

    @divider_solar_absorptance.setter
    def divider_solar_absorptance(self, value=0.0 ):
        """  Corresponds to IDD Field `divider_solar_absorptance`
        Assumed same on outside and inside of divider

        Args:
            value (float): value for IDD Field `divider_solar_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `divider_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `divider_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `divider_solar_absorptance`')

        self._data["Divider Solar Absorptance"] = value

    @property
    def divider_visible_absorptance(self):
        """Get divider_visible_absorptance

        Returns:
            float: the value of `divider_visible_absorptance` or None if not set
        """
        return self._data["Divider Visible Absorptance"]

    @divider_visible_absorptance.setter
    def divider_visible_absorptance(self, value=0.0 ):
        """  Corresponds to IDD Field `divider_visible_absorptance`
        Assumed same on outside and inside of divider

        Args:
            value (float): value for IDD Field `divider_visible_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `divider_visible_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `divider_visible_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `divider_visible_absorptance`')

        self._data["Divider Visible Absorptance"] = value

    @property
    def divider_thermal_hemispherical_emissivity(self):
        """Get divider_thermal_hemispherical_emissivity

        Returns:
            float: the value of `divider_thermal_hemispherical_emissivity` or None if not set
        """
        return self._data["Divider Thermal Hemispherical Emissivity"]

    @divider_thermal_hemispherical_emissivity.setter
    def divider_thermal_hemispherical_emissivity(self, value=0.9 ):
        """  Corresponds to IDD Field `divider_thermal_hemispherical_emissivity`
        Assumed same on outside and inside of divider

        Args:
            value (float): value for IDD Field `divider_thermal_hemispherical_emissivity`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `divider_thermal_hemispherical_emissivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `divider_thermal_hemispherical_emissivity`')
            if value >= 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `divider_thermal_hemispherical_emissivity`')

        self._data["Divider Thermal Hemispherical Emissivity"] = value

    @property
    def outside_reveal_solar_absorptance(self):
        """Get outside_reveal_solar_absorptance

        Returns:
            float: the value of `outside_reveal_solar_absorptance` or None if not set
        """
        return self._data["Outside Reveal Solar Absorptance"]

    @outside_reveal_solar_absorptance.setter
    def outside_reveal_solar_absorptance(self, value=0.0 ):
        """  Corresponds to IDD Field `outside_reveal_solar_absorptance`

        Args:
            value (float): value for IDD Field `outside_reveal_solar_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `outside_reveal_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outside_reveal_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `outside_reveal_solar_absorptance`')

        self._data["Outside Reveal Solar Absorptance"] = value

    @property
    def inside_sill_depth(self):
        """Get inside_sill_depth

        Returns:
            float: the value of `inside_sill_depth` or None if not set
        """
        return self._data["Inside Sill Depth"]

    @inside_sill_depth.setter
    def inside_sill_depth(self, value=0.0 ):
        """  Corresponds to IDD Field `inside_sill_depth`

        Args:
            value (float): value for IDD Field `inside_sill_depth`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `inside_sill_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `inside_sill_depth`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `inside_sill_depth`')

        self._data["Inside Sill Depth"] = value

    @property
    def inside_sill_solar_absorptance(self):
        """Get inside_sill_solar_absorptance

        Returns:
            float: the value of `inside_sill_solar_absorptance` or None if not set
        """
        return self._data["Inside Sill Solar Absorptance"]

    @inside_sill_solar_absorptance.setter
    def inside_sill_solar_absorptance(self, value=0.0 ):
        """  Corresponds to IDD Field `inside_sill_solar_absorptance`

        Args:
            value (float): value for IDD Field `inside_sill_solar_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `inside_sill_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `inside_sill_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `inside_sill_solar_absorptance`')

        self._data["Inside Sill Solar Absorptance"] = value

    @property
    def inside_reveal_depth(self):
        """Get inside_reveal_depth

        Returns:
            float: the value of `inside_reveal_depth` or None if not set
        """
        return self._data["Inside Reveal Depth"]

    @inside_reveal_depth.setter
    def inside_reveal_depth(self, value=0.0 ):
        """  Corresponds to IDD Field `inside_reveal_depth`
        Distance from plane of inside surface of glazing
        to plane of inside surface of wall.
        Outside reveal depth is determined from the geometry
        of the window and the wall it is on; it is non-zero if the plane of
        the outside surface of the glazing is set back from the plane of the
        outside surface of the wall.

        Args:
            value (float): value for IDD Field `inside_reveal_depth`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `inside_reveal_depth`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `inside_reveal_depth`')
            if value > 2.0:
                raise ValueError('value need to be smaller 2.0 '
                                 'for field `inside_reveal_depth`')

        self._data["Inside Reveal Depth"] = value

    @property
    def inside_reveal_solar_absorptance(self):
        """Get inside_reveal_solar_absorptance

        Returns:
            float: the value of `inside_reveal_solar_absorptance` or None if not set
        """
        return self._data["Inside Reveal Solar Absorptance"]

    @inside_reveal_solar_absorptance.setter
    def inside_reveal_solar_absorptance(self, value=0.0 ):
        """  Corresponds to IDD Field `inside_reveal_solar_absorptance`

        Args:
            value (float): value for IDD Field `inside_reveal_solar_absorptance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `inside_reveal_solar_absorptance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `inside_reveal_solar_absorptance`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `inside_reveal_solar_absorptance`')

        self._data["Inside Reveal Solar Absorptance"] = value

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
        out.append(self._to_str(self.frame_width))
        out.append(self._to_str(self.frame_outside_projection))
        out.append(self._to_str(self.frame_inside_projection))
        out.append(self._to_str(self.frame_conductance))
        out.append(self._to_str(self.ratio_of_frameedge_glass_conductance_to_centerofglass_conductance))
        out.append(self._to_str(self.frame_solar_absorptance))
        out.append(self._to_str(self.frame_visible_absorptance))
        out.append(self._to_str(self.frame_thermal_hemispherical_emissivity))
        out.append(self._to_str(self.divider_type))
        out.append(self._to_str(self.divider_width))
        out.append(self._to_str(self.number_of_horizontal_dividers))
        out.append(self._to_str(self.number_of_vertical_dividers))
        out.append(self._to_str(self.divider_outside_projection))
        out.append(self._to_str(self.divider_inside_projection))
        out.append(self._to_str(self.divider_conductance))
        out.append(self._to_str(self.ratio_of_divideredge_glass_conductance_to_centerofglass_conductance))
        out.append(self._to_str(self.divider_solar_absorptance))
        out.append(self._to_str(self.divider_visible_absorptance))
        out.append(self._to_str(self.divider_thermal_hemispherical_emissivity))
        out.append(self._to_str(self.outside_reveal_solar_absorptance))
        out.append(self._to_str(self.inside_sill_depth))
        out.append(self._to_str(self.inside_sill_solar_absorptance))
        out.append(self._to_str(self.inside_reveal_depth))
        out.append(self._to_str(self.inside_reveal_solar_absorptance))
        return ",".join(out)

class WindowPropertyAirflowControl(object):
    """ Corresponds to IDD object `WindowProperty:AirflowControl`
        Used to control forced airflow through a gap between glass layers
    """
    internal_name = "WindowProperty:AirflowControl"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowProperty:AirflowControl`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Airflow Source"] = None
        self._data["Airflow Destination"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Airflow Control Type"] = None
        self._data["Airflow Is Scheduled"] = None
        self._data["Airflow Multiplier Schedule Name"] = None

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
            self.airflow_source = None
        else:
            self.airflow_source = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_destination = None
        else:
            self.airflow_destination = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_control_type = None
        else:
            self.airflow_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_is_scheduled = None
        else:
            self.airflow_is_scheduled = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.airflow_multiplier_schedule_name = None
        else:
            self.airflow_multiplier_schedule_name = vals[i]
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
        Name must be that of an exterior window with two or three glass layers.

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
    def airflow_source(self):
        """Get airflow_source

        Returns:
            str: the value of `airflow_source` or None if not set
        """
        return self._data["Airflow Source"]

    @airflow_source.setter
    def airflow_source(self, value="IndoorAir"):
        """  Corresponds to IDD Field `airflow_source`

        Args:
            value (str): value for IDD Field `airflow_source`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflow_source`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_source`')
            vals = set()
            vals.add("IndoorAir")
            vals.add("OutdoorAir")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `airflow_source`'.format(value))

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
        """  Corresponds to IDD Field `airflow_destination`

        Args:
            value (str): value for IDD Field `airflow_destination`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflow_destination`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_destination`')
            vals = set()
            vals.add("IndoorAir")
            vals.add("OutdoorAir")
            vals.add("ReturnAir")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `airflow_destination`'.format(value))

        self._data["Airflow Destination"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `maximum_flow_rate`
        Above is m3/s per m of glazing width

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
                Unit: m3/s-m
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
                                 'for field `maximum_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_flow_rate`')

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
        """  Corresponds to IDD Field `airflow_control_type`
        ScheduledOnly requires that Airflow Has Multiplier Schedule Name = Yes
        and that Airflow Multiplier Schedule Name is specified.

        Args:
            value (str): value for IDD Field `airflow_control_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflow_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_control_type`')
            vals = set()
            vals.add("AlwaysOnAtMaximumFlow")
            vals.add("AlwaysOff")
            vals.add("ScheduledOnly")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `airflow_control_type`'.format(value))

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
        """  Corresponds to IDD Field `airflow_is_scheduled`
        If Yes, then Airflow Multiplier Schedule Name must be specified

        Args:
            value (str): value for IDD Field `airflow_is_scheduled`
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
                                 'for field `airflow_is_scheduled`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_is_scheduled`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `airflow_is_scheduled`'.format(value))

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
        """  Corresponds to IDD Field `airflow_multiplier_schedule_name`
        Required if Airflow Is Scheduled = Yes.
        Schedule values are 0.0 or 1.0 and multiply Maximum Air Flow.

        Args:
            value (str): value for IDD Field `airflow_multiplier_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflow_multiplier_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_multiplier_schedule_name`')

        self._data["Airflow Multiplier Schedule Name"] = value

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
        out.append(self._to_str(self.airflow_source))
        out.append(self._to_str(self.airflow_destination))
        out.append(self._to_str(self.maximum_flow_rate))
        out.append(self._to_str(self.airflow_control_type))
        out.append(self._to_str(self.airflow_is_scheduled))
        out.append(self._to_str(self.airflow_multiplier_schedule_name))
        return ",".join(out)

class WindowPropertyStormWindow(object):
    """ Corresponds to IDD object `WindowProperty:StormWindow`
        This is a movable exterior glass layer that is usually applied in the winter
        and removed in the summer.
    """
    internal_name = "WindowProperty:StormWindow"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowProperty:StormWindow`
        """
        self._data = OrderedDict()
        self._data["Window Name"] = None
        self._data["Storm Glass Layer Name"] = None
        self._data["Distance Between Storm Glass Layer and Adjacent Glass"] = None
        self._data["Month that Storm Glass Layer is Put On"] = None
        self._data["Day of Month that Storm Glass Layer is Put On"] = None
        self._data["Month that Storm Glass Layer is Taken Off"] = None
        self._data["Day of Month that Storm Glass Layer is Taken Off"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.window_name = None
        else:
            self.window_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.storm_glass_layer_name = None
        else:
            self.storm_glass_layer_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_between_storm_glass_layer_and_adjacent_glass = None
        else:
            self.distance_between_storm_glass_layer_and_adjacent_glass = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.month_that_storm_glass_layer_is_put_on = None
        else:
            self.month_that_storm_glass_layer_is_put_on = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_of_month_that_storm_glass_layer_is_put_on = None
        else:
            self.day_of_month_that_storm_glass_layer_is_put_on = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.month_that_storm_glass_layer_is_taken_off = None
        else:
            self.month_that_storm_glass_layer_is_taken_off = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.day_of_month_that_storm_glass_layer_is_taken_off = None
        else:
            self.day_of_month_that_storm_glass_layer_is_taken_off = vals[i]
        i += 1

    @property
    def window_name(self):
        """Get window_name

        Returns:
            str: the value of `window_name` or None if not set
        """
        return self._data["Window Name"]

    @window_name.setter
    def window_name(self, value=None):
        """  Corresponds to IDD Field `window_name`
        Must be the name of a FenestrationSurface:Detailed object with Surface Type = WINDOW.
        The WindowProperty:StormWindow object can only be used with exterior windows.

        Args:
            value (str): value for IDD Field `window_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_name`')

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
        """  Corresponds to IDD Field `storm_glass_layer_name`
        Must be a WindowMaterial:Glazing or WindowMaterial:Glazing:RefractionExtinctionMethod
        Gap between storm glass layer and adjacent glass layer is assumed to be filled
        with Air

        Args:
            value (str): value for IDD Field `storm_glass_layer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `storm_glass_layer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `storm_glass_layer_name`')

        self._data["Storm Glass Layer Name"] = value

    @property
    def distance_between_storm_glass_layer_and_adjacent_glass(self):
        """Get distance_between_storm_glass_layer_and_adjacent_glass

        Returns:
            float: the value of `distance_between_storm_glass_layer_and_adjacent_glass` or None if not set
        """
        return self._data["Distance Between Storm Glass Layer and Adjacent Glass"]

    @distance_between_storm_glass_layer_and_adjacent_glass.setter
    def distance_between_storm_glass_layer_and_adjacent_glass(self, value=0.05 ):
        """  Corresponds to IDD Field `distance_between_storm_glass_layer_and_adjacent_glass`

        Args:
            value (float): value for IDD Field `distance_between_storm_glass_layer_and_adjacent_glass`
                Unit: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `distance_between_storm_glass_layer_and_adjacent_glass`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `distance_between_storm_glass_layer_and_adjacent_glass`')
            if value > 0.5:
                raise ValueError('value need to be smaller 0.5 '
                                 'for field `distance_between_storm_glass_layer_and_adjacent_glass`')

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
        """  Corresponds to IDD Field `month_that_storm_glass_layer_is_put_on`

        Args:
            value (int): value for IDD Field `month_that_storm_glass_layer_is_put_on`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `month_that_storm_glass_layer_is_put_on`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `month_that_storm_glass_layer_is_put_on`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `month_that_storm_glass_layer_is_put_on`')

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
        """  Corresponds to IDD Field `day_of_month_that_storm_glass_layer_is_put_on`

        Args:
            value (int): value for IDD Field `day_of_month_that_storm_glass_layer_is_put_on`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `day_of_month_that_storm_glass_layer_is_put_on`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `day_of_month_that_storm_glass_layer_is_put_on`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `day_of_month_that_storm_glass_layer_is_put_on`')

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
        """  Corresponds to IDD Field `month_that_storm_glass_layer_is_taken_off`

        Args:
            value (int): value for IDD Field `month_that_storm_glass_layer_is_taken_off`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `month_that_storm_glass_layer_is_taken_off`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `month_that_storm_glass_layer_is_taken_off`')
            if value > 12:
                raise ValueError('value need to be smaller 12 '
                                 'for field `month_that_storm_glass_layer_is_taken_off`')

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
        """  Corresponds to IDD Field `day_of_month_that_storm_glass_layer_is_taken_off`

        Args:
            value (int): value for IDD Field `day_of_month_that_storm_glass_layer_is_taken_off`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `day_of_month_that_storm_glass_layer_is_taken_off`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `day_of_month_that_storm_glass_layer_is_taken_off`')
            if value > 31:
                raise ValueError('value need to be smaller 31 '
                                 'for field `day_of_month_that_storm_glass_layer_is_taken_off`')

        self._data["Day of Month that Storm Glass Layer is Taken Off"] = value

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
        out.append(self._to_str(self.window_name))
        out.append(self._to_str(self.storm_glass_layer_name))
        out.append(self._to_str(self.distance_between_storm_glass_layer_and_adjacent_glass))
        out.append(self._to_str(self.month_that_storm_glass_layer_is_put_on))
        out.append(self._to_str(self.day_of_month_that_storm_glass_layer_is_put_on))
        out.append(self._to_str(self.month_that_storm_glass_layer_is_taken_off))
        out.append(self._to_str(self.day_of_month_that_storm_glass_layer_is_taken_off))
        return ",".join(out)