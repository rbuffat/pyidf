import logging
import re


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class DataObject(object):

    def __setitem__(self, key, value):
        key_lower = key.lower()
        if key_lower in self.schema['fields']:
            value = self.check_value(key_lower, value)
            self._data[key_lower] = value
        # TODO extensibles
        else:
            raise ValueError("{} not found in {}".format(key,
                                                         self.schema['pyname']))

    def __getitem__(self, key):
        if isinstance(key, str):
            key_lower = key.lower()
            if key_lower in self.schema['fields']:
                return self._data[key_lower]
        # TODO extensible fields
        raise ValueError("{} not found in {}".format(key,
                                                     self.schema['pyname']))

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        for i, key in enumerate(self.schema['fields']):
            if i < len(vals) and len(vals[i]) == 0:
                self[key] = None
            elif i < len(vals):
                self[key] = vals[i]
        i = len(self.schema['fields'])
        if len(self.schema['extensible-fields']) > 0:
            while i < len(vals):
                ext_vals = [None] * len(self.schema['extensible-fields'])
                for j, val in enumerate(vals[i:i + len(self.schema['extensible-fields'])]):
                    if len(val) == 0:
                        val = None
                    ext_vals[j] = val
                self.add_extensible(*ext_vals)
                i += len(self.schema['extensible-fields'])

        self.strict = old_strict

    def check_value(self, name, value):
        schema = self.schema
        lower_name = name.lower()
        if lower_name in schema['fields']:
            field = schema['fields'][lower_name]
        elif lower_name in schema['extensible-fields']:
            field = schema['extensible-fields'][lower_name]
        else:
            raise ValueError('No field exists with name in data object`{}`'.format(schema['name']))

        if value is not None:
            if field['autocalculatable'] and not field['type'] == "alpha":
                try:
                    value_lower = str(value).lower()
                    if value_lower == "autocalculate":
                        return "Autocalculate"

                    if not self.strict and "auto" in value_lower:
                        logger.warn('Accept value {} as "Autocalculate" '
                                    'for field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                        return "Autocalculate"
                except ValueError:
                    # No string
                    pass

            if field['autosizable'] and not field['type'] == "alpha":
                try:
                    value_lower = str(value).lower()
                    if value_lower == "autosize":
                        return "Autosize"

                    if not self.strict and "auto" in value_lower:
                        logger.warn('Accept value {} as "Autosize" '
                                     'for field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                        return "Autosize"
                except ValueError:
                    pass

            try:
                if field['type'] == "alpha":
                    value = str(value)
                elif field['type'] == "integer":
                    value = int(value)
                elif field['type'] == "real":
                    value = float(value)
                else:
                    value = str(value)
            except ValueError:

                alt = ""
                if field['autosizable']:
                    alt = " or \"Autosize\""
                if field['autocalculatable']:
                    alt = " or \"Autocalculate\""

                if field['type'] == "real":
                    if not self.strict:
                        try:
                            conv_value = int(float(value))
                            logger.warn('Cast float {} to int {}, precision may be lost '
                                         'for field `{}.{}`'.format(value,
                                                                    conv_value,
                                                                    schema['pyname'],
                                                                    field['pyname']))
                            value = conv_value
                        except ValueError:
                            raise ValueError('value {} need to be of type {}{} '
                                             'for field `{}.{}`'.format(value,
                                                                         field['type'],
                                                                         alt,
                                                                         schema['pyname'],
                                                                         field['pyname']))
                else:
                            raise ValueError('value {} need to be of type {}{} '
                                             'for field `{}.{}`'.format(value,
                                                                         field['type'],
                                                                         alt,
                                                                         schema['pyname'],
                                                                         field['pyname']))

            if field['type'] == "alpha":
                if ',' in value:
                    raise ValueError('value should not contain a comma '
                                     'for field `{}.{}`'.format(schema['pyname'],
                                                                field['pyname']))
                if '!' in value:
                    raise ValueError('value should not contain a ! '
                                     'for field `{}.{}`'.format(schema['pyname'],
                                                                field['pyname']))
            else:

                if 'minimum' in field and value < field['minimum']:
                    raise ValueError('value {} need to be greater or equal {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['minimum'],
                                                                schema['pyname'],
                                                                field['pyname']))

                if 'minimum>' in field and value <= field['minimum>']:
                    raise ValueError('value {} need to be greater  {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['minimum>'],
                                                                schema['pyname'],
                                                                field['pyname']))

                if 'maximum' in field and value > field['maximum']:
                    raise ValueError('value {} need to be smaller or equal  {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['maximum'],
                                                                schema['pyname'],
                                                                field['pyname']))
                if 'maximum<' in field and value >= field['maximum<']:
                    raise ValueError('value {} need to be smaller  {} '
                                     'for field `{}.{}`'.format(value,
                                                                field['maximum<'],
                                                                schema['pyname'],
                                                                field['pyname']))

            if 'accepted-values' in field:
                vals = set(field['accepted-values'])

                if field['type'] == "alpha":
                    value_lower = value.lower()
                else:
                    value_lower = value

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
                                         'field `{}.{}`'.format(value,
                                                                schema['pyname'],
                                                                field['pyname']))
                    else:
                        logger.warn('change value {} to accepted value {} for '
                                    'field `{}.{}`'.format(value,
                                                           vals[value_lower],
                                                           schema['pyname'],
                                                           field['pyname']))
                value = value_lower

        # value is None
        else:
            if 'required-field' in field and 'default' in field:
                key = field['name'].lower()
                if key in self.schema['fields'] and self.schema['fields'].keys().index(key) < self.schema['min-fields']:
                    logger.warn('Replacing None value for required field `{}.{}` '
                                'with {}'.format(schema['pyname'],
                                                 field['pyname'],
                                                 field['default']))
                value = field['default']

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
        for key, field in self.schema['fields'].iteritems():
            if field['required-field'] and self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field {}.{} is None".format(key,
                                                                           self.schema['pyname'],
                                                                           self.field['pyname']))
                    break
                else:
                    logger.warn("Required field {}:{} is None".format(key,
                                                                     self.schema['pyname'],
                                                                     self.field['pyname']))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.schema['min-fields']
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for {}: {} / {}".format(self.schema['pyname'],
                                                                            out_fields,
                                                                            self.schema['min-fields']))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for {}: {} / {}".format(self.schema['pyname'],
                                                                       out_fields,
                                                                       self.schema['min-fields']))
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
            maxel = 0
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                if self._data[key] is not None:
                    maxel = i + 1
                    break

        maxel = max(maxel, self.schema['min-fields'])

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.schema['extensible-fields'].keys()[i], self._to_str(value)))
        return out

    def __str__(self):
        out = self.export()
        string = ",".join([self.schema['name']] + [o[1] for o in out])
        if len(string) > 77:
            string = string[:77] + "..."
        return string

    def __iter__(self):
        for val in self._data.values():
            yield val

class DONames:
    LeadInput = "Lead Input"
    SimulationData = "Simulation Data"
    Version = "Version"
    SimulationControl = "SimulationControl"
    Building = "Building"
    ShadowCalculation = "ShadowCalculation"
    SurfaceConvectionAlgorithmInside = "SurfaceConvectionAlgorithm:Inside"
    SurfaceConvectionAlgorithmOutside = "SurfaceConvectionAlgorithm:Outside"
    HeatBalanceAlgorithm = "HeatBalanceAlgorithm"
    HeatBalanceSettingsConductionFiniteDifference = "HeatBalanceSettings:ConductionFiniteDifference"
    ZoneAirHeatBalanceAlgorithm = "ZoneAirHeatBalanceAlgorithm"
    ZoneAirContaminantBalance = "ZoneAirContaminantBalance"
    ZoneAirMassFlowConservation = "ZoneAirMassFlowConservation"
    ZoneCapacitanceMultiplierResearchSpecial = "ZoneCapacitanceMultiplier:ResearchSpecial"
    Timestep = "Timestep"
    ConvergenceLimits = "ConvergenceLimits"
    ProgramControl = "ProgramControl"
    ComplianceBuilding = "Compliance:Building"
    SiteLocation = "Site:Location"
    SizingPeriodDesignDay = "SizingPeriod:DesignDay"
    SizingPeriodWeatherFileDays = "SizingPeriod:WeatherFileDays"
    SizingPeriodWeatherFileConditionType = "SizingPeriod:WeatherFileConditionType"
    RunPeriod = "RunPeriod"
    RunPeriodCustomRange = "RunPeriod:CustomRange"
    RunPeriodControlSpecialDays = "RunPeriodControl:SpecialDays"
    RunPeriodControlDaylightSavingTime = "RunPeriodControl:DaylightSavingTime"
    WeatherPropertySkyTemperature = "WeatherProperty:SkyTemperature"
    SiteWeatherStation = "Site:WeatherStation"
    SiteHeightVariation = "Site:HeightVariation"
    SiteGroundTemperatureBuildingSurface = "Site:GroundTemperature:BuildingSurface"
    SiteGroundTemperatureFcfactorMethod = "Site:GroundTemperature:FCfactorMethod"
    SiteGroundTemperatureShallow = "Site:GroundTemperature:Shallow"
    SiteGroundTemperatureDeep = "Site:GroundTemperature:Deep"
    SiteGroundDomain = "Site:GroundDomain"
    SiteGroundReflectance = "Site:GroundReflectance"
    SiteGroundReflectanceSnowModifier = "Site:GroundReflectance:SnowModifier"
    SiteWaterMainsTemperature = "Site:WaterMainsTemperature"
    SitePrecipitation = "Site:Precipitation"
    RoofIrrigation = "RoofIrrigation"
    SiteSolarAndVisibleSpectrum = "Site:SolarAndVisibleSpectrum"
    SiteSpectrumData = "Site:SpectrumData"
    ScheduleTypeLimits = "ScheduleTypeLimits"
    ScheduleDayHourly = "Schedule:Day:Hourly"
    ScheduleDayInterval = "Schedule:Day:Interval"
    ScheduleDayList = "Schedule:Day:List"
    ScheduleWeekDaily = "Schedule:Week:Daily"
    ScheduleWeekCompact = "Schedule:Week:Compact"
    ScheduleYear = "Schedule:Year"
    ScheduleCompact = "Schedule:Compact"
    ScheduleConstant = "Schedule:Constant"
    ScheduleFile = "Schedule:File"
    Material = "Material"
    MaterialNoMass = "Material:NoMass"
    MaterialInfraredTransparent = "Material:InfraredTransparent"
    MaterialAirGap = "Material:AirGap"
    MaterialRoofVegetation = "Material:RoofVegetation"
    WindowMaterialSimpleGlazingSystem = "WindowMaterial:SimpleGlazingSystem"
    WindowMaterialGlazing = "WindowMaterial:Glazing"
    WindowMaterialGlazingGroupThermochromic = "WindowMaterial:GlazingGroup:Thermochromic"
    WindowMaterialGlazingRefractionExtinctionMethod = "WindowMaterial:Glazing:RefractionExtinctionMethod"
    WindowMaterialGas = "WindowMaterial:Gas"
    WindowGapSupportPillar = "WindowGap:SupportPillar"
    WindowGapDeflectionState = "WindowGap:DeflectionState"
    WindowMaterialGasMixture = "WindowMaterial:GasMixture"
    WindowMaterialGap = "WindowMaterial:Gap"
    WindowMaterialShade = "WindowMaterial:Shade"
    WindowMaterialComplexShade = "WindowMaterial:ComplexShade"
    WindowMaterialBlind = "WindowMaterial:Blind"
    WindowMaterialScreen = "WindowMaterial:Screen"
    WindowMaterialShadeEquivalentLayer = "WindowMaterial:Shade:EquivalentLayer"
    WindowMaterialDrapeEquivalentLayer = "WindowMaterial:Drape:EquivalentLayer"
    WindowMaterialBlindEquivalentLayer = "WindowMaterial:Blind:EquivalentLayer"
    WindowMaterialScreenEquivalentLayer = "WindowMaterial:Screen:EquivalentLayer"
    WindowMaterialGlazingEquivalentLayer = "WindowMaterial:Glazing:EquivalentLayer"
    ConstructionWindowEquivalentLayer = "Construction:WindowEquivalentLayer"
    WindowMaterialGapEquivalentLayer = "WindowMaterial:Gap:EquivalentLayer"
    MaterialPropertyMoisturePenetrationDepthSettings = "MaterialProperty:MoisturePenetrationDepth:Settings"
    MaterialPropertyPhaseChange = "MaterialProperty:PhaseChange"
    MaterialPropertyVariableThermalConductivity = "MaterialProperty:VariableThermalConductivity"
    MaterialPropertyHeatAndMoistureTransferSettings = "MaterialProperty:HeatAndMoistureTransfer:Settings"
    MaterialPropertyHeatAndMoistureTransferSorptionIsotherm = "MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm"
    MaterialPropertyHeatAndMoistureTransferSuction = "MaterialProperty:HeatAndMoistureTransfer:Suction"
    MaterialPropertyHeatAndMoistureTransferRedistribution = "MaterialProperty:HeatAndMoistureTransfer:Redistribution"
    MaterialPropertyHeatAndMoistureTransferDiffusion = "MaterialProperty:HeatAndMoistureTransfer:Diffusion"
    MaterialPropertyHeatAndMoistureTransferThermalConductivity = "MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity"
    MaterialPropertyGlazingSpectralData = "MaterialProperty:GlazingSpectralData"
    Construction = "Construction"
    ConstructionCfactorUndergroundWall = "Construction:CfactorUndergroundWall"
    ConstructionFfactorGroundFloor = "Construction:FfactorGroundFloor"
    ConstructionInternalSource = "Construction:InternalSource"
    WindowThermalModelParams = "WindowThermalModel:Params"
    ConstructionComplexFenestrationState = "Construction:ComplexFenestrationState"
    ConstructionWindowDataFile = "Construction:WindowDataFile"
    GlobalGeometryRules = "GlobalGeometryRules"
    GeometryTransform = "GeometryTransform"
    Zone = "Zone"
    ZoneList = "ZoneList"
    ZoneGroup = "ZoneGroup"
    BuildingSurfaceDetailed = "BuildingSurface:Detailed"
    WallDetailed = "Wall:Detailed"
    RoofCeilingDetailed = "RoofCeiling:Detailed"
    FloorDetailed = "Floor:Detailed"
    WallExterior = "Wall:Exterior"
    WallAdiabatic = "Wall:Adiabatic"
    WallUnderground = "Wall:Underground"
    WallInterzone = "Wall:Interzone"
    Roof = "Roof"
    CeilingAdiabatic = "Ceiling:Adiabatic"
    CeilingInterzone = "Ceiling:Interzone"
    FloorGroundContact = "Floor:GroundContact"
    FloorAdiabatic = "Floor:Adiabatic"
    FloorInterzone = "Floor:Interzone"
    FenestrationSurfaceDetailed = "FenestrationSurface:Detailed"
    Window = "Window"
    Door = "Door"
    GlazedDoor = "GlazedDoor"
    WindowInterzone = "Window:Interzone"
    DoorInterzone = "Door:Interzone"
    GlazedDoorInterzone = "GlazedDoor:Interzone"
    WindowPropertyShadingControl = "WindowProperty:ShadingControl"
    WindowPropertyFrameAndDivider = "WindowProperty:FrameAndDivider"
    WindowPropertyAirflowControl = "WindowProperty:AirflowControl"
    WindowPropertyStormWindow = "WindowProperty:StormWindow"
    InternalMass = "InternalMass"
    ShadingSite = "Shading:Site"
    ShadingBuilding = "Shading:Building"
    ShadingSiteDetailed = "Shading:Site:Detailed"
    ShadingBuildingDetailed = "Shading:Building:Detailed"
    ShadingOverhang = "Shading:Overhang"
    ShadingOverhangProjection = "Shading:Overhang:Projection"
    ShadingFin = "Shading:Fin"
    ShadingFinProjection = "Shading:Fin:Projection"
    ShadingZoneDetailed = "Shading:Zone:Detailed"
    ShadingPropertyReflectance = "ShadingProperty:Reflectance"
    SurfacePropertyHeatTransferAlgorithm = "SurfaceProperty:HeatTransferAlgorithm"
    SurfacePropertyHeatTransferAlgorithmMultipleSurface = "SurfaceProperty:HeatTransferAlgorithm:MultipleSurface"
    SurfacePropertyHeatTransferAlgorithmSurfaceList = "SurfaceProperty:HeatTransferAlgorithm:SurfaceList"
    SurfacePropertyHeatTransferAlgorithmConstruction = "SurfaceProperty:HeatTransferAlgorithm:Construction"
    SurfaceControlMovableInsulation = "SurfaceControl:MovableInsulation"
    SurfacePropertyOtherSideCoefficients = "SurfaceProperty:OtherSideCoefficients"
    SurfacePropertyOtherSideConditionsModel = "SurfaceProperty:OtherSideConditionsModel"
    SurfaceConvectionAlgorithmInsideAdaptiveModelSelections = "SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections"
    SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections = "SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections"
    SurfaceConvectionAlgorithmInsideUserCurve = "SurfaceConvectionAlgorithm:Inside:UserCurve"
    SurfaceConvectionAlgorithmOutsideUserCurve = "SurfaceConvectionAlgorithm:Outside:UserCurve"
    SurfacePropertyConvectionCoefficients = "SurfaceProperty:ConvectionCoefficients"
    SurfacePropertyConvectionCoefficientsMultipleSurface = "SurfaceProperty:ConvectionCoefficients:MultipleSurface"
    SurfacePropertiesVaporCoefficients = "SurfaceProperties:VaporCoefficients"
    SurfacePropertyExteriorNaturalVentedCavity = "SurfaceProperty:ExteriorNaturalVentedCavity"
    SurfacePropertySolarIncidentInside = "SurfaceProperty:SolarIncidentInside"
    ComplexFenestrationPropertySolarAbsorbedLayers = "ComplexFenestrationProperty:SolarAbsorbedLayers"
    ZonePropertyUserViewFactorsBySurfaceName = "ZoneProperty:UserViewFactors:bySurfaceName"
    GroundHeatTransferControl = "GroundHeatTransfer:Control"
    GroundHeatTransferSlabMaterials = "GroundHeatTransfer:Slab:Materials"
    GroundHeatTransferSlabMatlProps = "GroundHeatTransfer:Slab:MatlProps"
    GroundHeatTransferSlabBoundConds = "GroundHeatTransfer:Slab:BoundConds"
    GroundHeatTransferSlabBldgProps = "GroundHeatTransfer:Slab:BldgProps"
    GroundHeatTransferSlabInsulation = "GroundHeatTransfer:Slab:Insulation"
    GroundHeatTransferSlabEquivalentSlab = "GroundHeatTransfer:Slab:EquivalentSlab"
    GroundHeatTransferSlabAutoGrid = "GroundHeatTransfer:Slab:AutoGrid"
    GroundHeatTransferSlabManualGrid = "GroundHeatTransfer:Slab:ManualGrid"
    GroundHeatTransferSlabXface = "GroundHeatTransfer:Slab:XFACE"
    GroundHeatTransferSlabYface = "GroundHeatTransfer:Slab:YFACE"
    GroundHeatTransferSlabZface = "GroundHeatTransfer:Slab:ZFACE"
    GroundHeatTransferBasementSimParameters = "GroundHeatTransfer:Basement:SimParameters"
    GroundHeatTransferBasementMatlProps = "GroundHeatTransfer:Basement:MatlProps"
    GroundHeatTransferBasementInsulation = "GroundHeatTransfer:Basement:Insulation"
    GroundHeatTransferBasementSurfaceProps = "GroundHeatTransfer:Basement:SurfaceProps"
    GroundHeatTransferBasementBldgData = "GroundHeatTransfer:Basement:BldgData"
    GroundHeatTransferBasementInterior = "GroundHeatTransfer:Basement:Interior"
    GroundHeatTransferBasementComBldg = "GroundHeatTransfer:Basement:ComBldg"
    GroundHeatTransferBasementEquivSlab = "GroundHeatTransfer:Basement:EquivSlab"
    GroundHeatTransferBasementEquivAutoGrid = "GroundHeatTransfer:Basement:EquivAutoGrid"
    GroundHeatTransferBasementAutoGrid = "GroundHeatTransfer:Basement:AutoGrid"
    GroundHeatTransferBasementManualGrid = "GroundHeatTransfer:Basement:ManualGrid"
    GroundHeatTransferBasementXface = "GroundHeatTransfer:Basement:XFACE"
    GroundHeatTransferBasementYface = "GroundHeatTransfer:Basement:YFACE"
    GroundHeatTransferBasementZface = "GroundHeatTransfer:Basement:ZFACE"
    RoomAirModelType = "RoomAirModelType"
    RoomAirTemperaturePatternUserDefined = "RoomAir:TemperaturePattern:UserDefined"
    RoomAirTemperaturePatternConstantGradient = "RoomAir:TemperaturePattern:ConstantGradient"
    RoomAirTemperaturePatternTwoGradient = "RoomAir:TemperaturePattern:TwoGradient"
    RoomAirTemperaturePatternNondimensionalHeight = "RoomAir:TemperaturePattern:NondimensionalHeight"
    RoomAirTemperaturePatternSurfaceMapping = "RoomAir:TemperaturePattern:SurfaceMapping"
    RoomAirNode = "RoomAir:Node"
    RoomAirSettingsOneNodeDisplacementVentilation = "RoomAirSettings:OneNodeDisplacementVentilation"
    RoomAirSettingsThreeNodeDisplacementVentilation = "RoomAirSettings:ThreeNodeDisplacementVentilation"
    RoomAirSettingsCrossVentilation = "RoomAirSettings:CrossVentilation"
    RoomAirSettingsUnderFloorAirDistributionInterior = "RoomAirSettings:UnderFloorAirDistributionInterior"
    RoomAirSettingsUnderFloorAirDistributionExterior = "RoomAirSettings:UnderFloorAirDistributionExterior"
    People = "People"
    ComfortViewFactorAngles = "ComfortViewFactorAngles"
    Lights = "Lights"
    ElectricEquipment = "ElectricEquipment"
    GasEquipment = "GasEquipment"
    HotWaterEquipment = "HotWaterEquipment"
    SteamEquipment = "SteamEquipment"
    OtherEquipment = "OtherEquipment"
    ZoneBaseboardOutdoorTemperatureControlled = "ZoneBaseboard:OutdoorTemperatureControlled"
    ZoneContaminantSourceAndSinkCarbonDioxide = "ZoneContaminantSourceAndSink:CarbonDioxide"
    ZoneContaminantSourceAndSinkGenericConstant = "ZoneContaminantSourceAndSink:Generic:Constant"
    SurfaceContaminantSourceAndSinkGenericPressureDriven = "SurfaceContaminantSourceAndSink:Generic:PressureDriven"
    ZoneContaminantSourceAndSinkGenericCutoffModel = "ZoneContaminantSourceAndSink:Generic:CutoffModel"
    ZoneContaminantSourceAndSinkGenericDecaySource = "ZoneContaminantSourceAndSink:Generic:DecaySource"
    SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion = "SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"
    SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink = "SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"
    ZoneContaminantSourceAndSinkGenericDepositionRateSink = "ZoneContaminantSourceAndSink:Generic:DepositionRateSink"
    DaylightingControls = "Daylighting:Controls"
    DaylightingDelightControls = "Daylighting:DELight:Controls"
    DaylightingDelightReferencePoint = "Daylighting:DELight:ReferencePoint"
    DaylightingDelightComplexFenestration = "Daylighting:DELight:ComplexFenestration"
    DaylightingDeviceTubular = "DaylightingDevice:Tubular"
    DaylightingDeviceShelf = "DaylightingDevice:Shelf"
    DaylightingDeviceLightWell = "DaylightingDevice:LightWell"
    OutputDaylightFactors = "Output:DaylightFactors"
    OutputIlluminanceMap = "Output:IlluminanceMap"
    OutputControlIlluminanceMapStyle = "OutputControl:IlluminanceMap:Style"
    ZoneInfiltrationDesignFlowRate = "ZoneInfiltration:DesignFlowRate"
    ZoneInfiltrationEffectiveLeakageArea = "ZoneInfiltration:EffectiveLeakageArea"
    ZoneInfiltrationFlowCoefficient = "ZoneInfiltration:FlowCoefficient"
    ZoneVentilationDesignFlowRate = "ZoneVentilation:DesignFlowRate"
    ZoneVentilationWindandStackOpenArea = "ZoneVentilation:WindandStackOpenArea"
    ZoneAirBalanceOutdoorAir = "ZoneAirBalance:OutdoorAir"
    ZoneMixing = "ZoneMixing"
    ZoneCrossMixing = "ZoneCrossMixing"
    ZoneRefrigerationDoorMixing = "ZoneRefrigerationDoorMixing"
    ZoneEarthtube = "ZoneEarthtube"
    ZoneCoolTowerShower = "ZoneCoolTower:Shower"
    ZoneThermalChimney = "ZoneThermalChimney"
    AirflowNetworkSimulationControl = "AirflowNetwork:SimulationControl"
    AirflowNetworkMultiZoneZone = "AirflowNetwork:MultiZone:Zone"
    AirflowNetworkMultiZoneSurface = "AirflowNetwork:MultiZone:Surface"
    AirflowNetworkMultiZoneReferenceCrackConditions = "AirflowNetwork:MultiZone:ReferenceCrackConditions"
    AirflowNetworkMultiZoneSurfaceCrack = "AirflowNetwork:MultiZone:Surface:Crack"
    AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea = "AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea"
    AirflowNetworkMultiZoneComponentDetailedOpening = "AirflowNetwork:MultiZone:Component:DetailedOpening"
    AirflowNetworkMultiZoneComponentSimpleOpening = "AirflowNetwork:MultiZone:Component:SimpleOpening"
    AirflowNetworkMultiZoneComponentHorizontalOpening = "AirflowNetwork:MultiZone:Component:HorizontalOpening"
    AirflowNetworkMultiZoneComponentZoneExhaustFan = "AirflowNetwork:MultiZone:Component:ZoneExhaustFan"
    AirflowNetworkMultiZoneExternalNode = "AirflowNetwork:MultiZone:ExternalNode"
    AirflowNetworkMultiZoneWindPressureCoefficientArray = "AirflowNetwork:MultiZone:WindPressureCoefficientArray"
    AirflowNetworkMultiZoneWindPressureCoefficientValues = "AirflowNetwork:MultiZone:WindPressureCoefficientValues"
    AirflowNetworkDistributionNode = "AirflowNetwork:Distribution:Node"
    AirflowNetworkDistributionComponentLeak = "AirflowNetwork:Distribution:Component:Leak"
    AirflowNetworkDistributionComponentLeakageRatio = "AirflowNetwork:Distribution:Component:LeakageRatio"
    AirflowNetworkDistributionComponentDuct = "AirflowNetwork:Distribution:Component:Duct"
    AirflowNetworkDistributionComponentFan = "AirflowNetwork:Distribution:Component:Fan"
    AirflowNetworkDistributionComponentCoil = "AirflowNetwork:Distribution:Component:Coil"
    AirflowNetworkDistributionComponentHeatExchanger = "AirflowNetwork:Distribution:Component:HeatExchanger"
    AirflowNetworkDistributionComponentTerminalUnit = "AirflowNetwork:Distribution:Component:TerminalUnit"
    AirflowNetworkDistributionComponentConstantPressureDrop = "AirflowNetwork:Distribution:Component:ConstantPressureDrop"
    AirflowNetworkDistributionLinkage = "AirflowNetwork:Distribution:Linkage"
    ExteriorLights = "Exterior:Lights"
    ExteriorFuelEquipment = "Exterior:FuelEquipment"
    ExteriorWaterEquipment = "Exterior:WaterEquipment"
    HvactemplateThermostat = "HVACTemplate:Thermostat"
    HvactemplateZoneIdealLoadsAirSystem = "HVACTemplate:Zone:IdealLoadsAirSystem"
    HvactemplateZoneBaseboardHeat = "HVACTemplate:Zone:BaseboardHeat"
    HvactemplateZoneFanCoil = "HVACTemplate:Zone:FanCoil"
    HvactemplateZonePtac = "HVACTemplate:Zone:PTAC"
    HvactemplateZonePthp = "HVACTemplate:Zone:PTHP"
    HvactemplateZoneWaterToAirHeatPump = "HVACTemplate:Zone:WaterToAirHeatPump"
    HvactemplateZoneVrf = "HVACTemplate:Zone:VRF"
    HvactemplateZoneUnitary = "HVACTemplate:Zone:Unitary"
    HvactemplateZoneVav = "HVACTemplate:Zone:VAV"
    HvactemplateZoneVavFanPowered = "HVACTemplate:Zone:VAV:FanPowered"
    HvactemplateZoneVavHeatAndCool = "HVACTemplate:Zone:VAV:HeatAndCool"
    HvactemplateZoneConstantVolume = "HVACTemplate:Zone:ConstantVolume"
    HvactemplateZoneDualDuct = "HVACTemplate:Zone:DualDuct"
    HvactemplateSystemVrf = "HVACTemplate:System:VRF"
    HvactemplateSystemUnitary = "HVACTemplate:System:Unitary"
    HvactemplateSystemUnitaryHeatPumpAirToAir = "HVACTemplate:System:UnitaryHeatPump:AirToAir"
    HvactemplateSystemUnitarySystem = "HVACTemplate:System:UnitarySystem"
    HvactemplateSystemVav = "HVACTemplate:System:VAV"
    HvactemplateSystemPackagedVav = "HVACTemplate:System:PackagedVAV"
    HvactemplateSystemConstantVolume = "HVACTemplate:System:ConstantVolume"
    HvactemplateSystemDualDuct = "HVACTemplate:System:DualDuct"
    HvactemplateSystemDedicatedOutdoorAir = "HVACTemplate:System:DedicatedOutdoorAir"
    HvactemplatePlantChilledWaterLoop = "HVACTemplate:Plant:ChilledWaterLoop"
    HvactemplatePlantChiller = "HVACTemplate:Plant:Chiller"
    HvactemplatePlantChillerObjectReference = "HVACTemplate:Plant:Chiller:ObjectReference"
    HvactemplatePlantTower = "HVACTemplate:Plant:Tower"
    HvactemplatePlantTowerObjectReference = "HVACTemplate:Plant:Tower:ObjectReference"
    HvactemplatePlantHotWaterLoop = "HVACTemplate:Plant:HotWaterLoop"
    HvactemplatePlantBoiler = "HVACTemplate:Plant:Boiler"
    HvactemplatePlantBoilerObjectReference = "HVACTemplate:Plant:Boiler:ObjectReference"
    HvactemplatePlantMixedWaterLoop = "HVACTemplate:Plant:MixedWaterLoop"
    DesignSpecificationOutdoorAir = "DesignSpecification:OutdoorAir"
    DesignSpecificationZoneAirDistribution = "DesignSpecification:ZoneAirDistribution"
    SizingParameters = "Sizing:Parameters"
    SizingZone = "Sizing:Zone"
    DesignSpecificationZoneHvacSizing = "DesignSpecification:ZoneHVAC:Sizing"
    SizingSystem = "Sizing:System"
    SizingPlant = "Sizing:Plant"
    OutputControlSizingStyle = "OutputControl:Sizing:Style"
    ZoneControlHumidistat = "ZoneControl:Humidistat"
    ZoneControlThermostat = "ZoneControl:Thermostat"
    ZoneControlThermostatOperativeTemperature = "ZoneControl:Thermostat:OperativeTemperature"
    ZoneControlThermostatThermalComfort = "ZoneControl:Thermostat:ThermalComfort"
    ZoneControlThermostatTemperatureAndHumidity = "ZoneControl:Thermostat:TemperatureAndHumidity"
    ThermostatSetpointSingleHeating = "ThermostatSetpoint:SingleHeating"
    ThermostatSetpointSingleCooling = "ThermostatSetpoint:SingleCooling"
    ThermostatSetpointSingleHeatingOrCooling = "ThermostatSetpoint:SingleHeatingOrCooling"
    ThermostatSetpointDualSetpoint = "ThermostatSetpoint:DualSetpoint"
    ThermostatSetpointThermalComfortFangerSingleHeating = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
    ThermostatSetpointThermalComfortFangerSingleCooling = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
    ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
    ThermostatSetpointThermalComfortFangerDualSetpoint = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
    ZoneControlThermostatStagedDualSetpoint = "ZoneControl:Thermostat:StagedDualSetpoint"
    ZoneControlContaminantController = "ZoneControl:ContaminantController"
    ZoneHvacIdealLoadsAirSystem = "ZoneHVAC:IdealLoadsAirSystem"
    ZoneHvacFourPipeFanCoil = "ZoneHVAC:FourPipeFanCoil"
    ZoneHvacWindowAirConditioner = "ZoneHVAC:WindowAirConditioner"
    ZoneHvacPackagedTerminalAirConditioner = "ZoneHVAC:PackagedTerminalAirConditioner"
    ZoneHvacPackagedTerminalHeatPump = "ZoneHVAC:PackagedTerminalHeatPump"
    ZoneHvacWaterToAirHeatPump = "ZoneHVAC:WaterToAirHeatPump"
    ZoneHvacDehumidifierDx = "ZoneHVAC:Dehumidifier:DX"
    ZoneHvacEnergyRecoveryVentilator = "ZoneHVAC:EnergyRecoveryVentilator"
    ZoneHvacEnergyRecoveryVentilatorController = "ZoneHVAC:EnergyRecoveryVentilator:Controller"
    ZoneHvacUnitVentilator = "ZoneHVAC:UnitVentilator"
    ZoneHvacUnitHeater = "ZoneHVAC:UnitHeater"
    ZoneHvacEvaporativeCoolerUnit = "ZoneHVAC:EvaporativeCoolerUnit"
    ZoneHvacOutdoorAirUnit = "ZoneHVAC:OutdoorAirUnit"
    ZoneHvacOutdoorAirUnitEquipmentList = "ZoneHVAC:OutdoorAirUnit:EquipmentList"
    ZoneHvacTerminalUnitVariableRefrigerantFlow = "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"
    ZoneHvacBaseboardRadiantConvectiveWater = "ZoneHVAC:Baseboard:RadiantConvective:Water"
    ZoneHvacBaseboardRadiantConvectiveSteam = "ZoneHVAC:Baseboard:RadiantConvective:Steam"
    ZoneHvacBaseboardRadiantConvectiveElectric = "ZoneHVAC:Baseboard:RadiantConvective:Electric"
    ZoneHvacBaseboardConvectiveWater = "ZoneHVAC:Baseboard:Convective:Water"
    ZoneHvacBaseboardConvectiveElectric = "ZoneHVAC:Baseboard:Convective:Electric"
    ZoneHvacLowTemperatureRadiantVariableFlow = "ZoneHVAC:LowTemperatureRadiant:VariableFlow"
    ZoneHvacLowTemperatureRadiantConstantFlow = "ZoneHVAC:LowTemperatureRadiant:ConstantFlow"
    ZoneHvacLowTemperatureRadiantElectric = "ZoneHVAC:LowTemperatureRadiant:Electric"
    ZoneHvacLowTemperatureRadiantSurfaceGroup = "ZoneHVAC:LowTemperatureRadiant:SurfaceGroup"
    ZoneHvacHighTemperatureRadiant = "ZoneHVAC:HighTemperatureRadiant"
    ZoneHvacVentilatedSlab = "ZoneHVAC:VentilatedSlab"
    ZoneHvacVentilatedSlabSlabGroup = "ZoneHVAC:VentilatedSlab:SlabGroup"
    AirTerminalSingleDuctUncontrolled = "AirTerminal:SingleDuct:Uncontrolled"
    AirTerminalSingleDuctConstantVolumeReheat = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
    AirTerminalSingleDuctVavNoReheat = "AirTerminal:SingleDuct:VAV:NoReheat"
    AirTerminalSingleDuctVavReheat = "AirTerminal:SingleDuct:VAV:Reheat"
    AirTerminalSingleDuctVavReheatVariableSpeedFan = "AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan"
    AirTerminalSingleDuctVavHeatAndCoolNoReheat = "AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"
    AirTerminalSingleDuctVavHeatAndCoolReheat = "AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"
    AirTerminalSingleDuctSeriesPiuReheat = "AirTerminal:SingleDuct:SeriesPIU:Reheat"
    AirTerminalSingleDuctParallelPiuReheat = "AirTerminal:SingleDuct:ParallelPIU:Reheat"
    AirTerminalSingleDuctConstantVolumeFourPipeInduction = "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"
    AirTerminalSingleDuctConstantVolumeCooledBeam = "AirTerminal:SingleDuct:ConstantVolume:CooledBeam"
    AirTerminalSingleDuctInletSideMixer = "AirTerminal:SingleDuct:InletSideMixer"
    AirTerminalSingleDuctSupplySideMixer = "AirTerminal:SingleDuct:SupplySideMixer"
    AirTerminalDualDuctConstantVolume = "AirTerminal:DualDuct:ConstantVolume"
    AirTerminalDualDuctVav = "AirTerminal:DualDuct:VAV"
    AirTerminalDualDuctVavOutdoorAir = "AirTerminal:DualDuct:VAV:OutdoorAir"
    ZoneHvacAirDistributionUnit = "ZoneHVAC:AirDistributionUnit"
    ZoneHvacEquipmentList = "ZoneHVAC:EquipmentList"
    ZoneHvacEquipmentConnections = "ZoneHVAC:EquipmentConnections"
    FanConstantVolume = "Fan:ConstantVolume"
    FanVariableVolume = "Fan:VariableVolume"
    FanOnOff = "Fan:OnOff"
    FanZoneExhaust = "Fan:ZoneExhaust"
    FanPerformanceNightVentilation = "FanPerformance:NightVentilation"
    FanComponentModel = "Fan:ComponentModel"
    CoilCoolingWater = "Coil:Cooling:Water"
    CoilCoolingWaterDetailedGeometry = "Coil:Cooling:Water:DetailedGeometry"
    CoilCoolingDxSingleSpeed = "Coil:Cooling:DX:SingleSpeed"
    CoilCoolingDxTwoSpeed = "Coil:Cooling:DX:TwoSpeed"
    CoilCoolingDxMultiSpeed = "Coil:Cooling:DX:MultiSpeed"
    CoilCoolingDxVariableSpeed = "Coil:Cooling:DX:VariableSpeed"
    CoilCoolingDxTwoStageWithHumidityControlMode = "Coil:Cooling:DX:TwoStageWithHumidityControlMode"
    CoilPerformanceDxCooling = "CoilPerformance:DX:Cooling"
    CoilCoolingDxVariableRefrigerantFlow = "Coil:Cooling:DX:VariableRefrigerantFlow"
    CoilHeatingDxVariableRefrigerantFlow = "Coil:Heating:DX:VariableRefrigerantFlow"
    CoilHeatingWater = "Coil:Heating:Water"
    CoilHeatingSteam = "Coil:Heating:Steam"
    CoilHeatingElectric = "Coil:Heating:Electric"
    CoilHeatingElectricMultiStage = "Coil:Heating:Electric:MultiStage"
    CoilHeatingGas = "Coil:Heating:Gas"
    CoilHeatingGasMultiStage = "Coil:Heating:Gas:MultiStage"
    CoilHeatingDesuperheater = "Coil:Heating:Desuperheater"
    CoilHeatingDxSingleSpeed = "Coil:Heating:DX:SingleSpeed"
    CoilHeatingDxMultiSpeed = "Coil:Heating:DX:MultiSpeed"
    CoilHeatingDxVariableSpeed = "Coil:Heating:DX:VariableSpeed"
    CoilCoolingWaterToAirHeatPumpParameterEstimation = "Coil:Cooling:WaterToAirHeatPump:ParameterEstimation"
    CoilHeatingWaterToAirHeatPumpParameterEstimation = "Coil:Heating:WaterToAirHeatPump:ParameterEstimation"
    CoilCoolingWaterToAirHeatPumpEquationFit = "Coil:Cooling:WaterToAirHeatPump:EquationFit"
    CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit = "Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit"
    CoilHeatingWaterToAirHeatPumpEquationFit = "Coil:Heating:WaterToAirHeatPump:EquationFit"
    CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit = "Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit"
    CoilWaterHeatingAirToWaterHeatPump = "Coil:WaterHeating:AirToWaterHeatPump"
    CoilWaterHeatingDesuperheater = "Coil:WaterHeating:Desuperheater"
    CoilSystemCoolingDx = "CoilSystem:Cooling:DX"
    CoilSystemHeatingDx = "CoilSystem:Heating:DX"
    CoilSystemCoolingWaterHeatExchangerAssisted = "CoilSystem:Cooling:Water:HeatExchangerAssisted"
    CoilSystemCoolingDxHeatExchangerAssisted = "CoilSystem:Cooling:DX:HeatExchangerAssisted"
    CoilCoolingDxSingleSpeedThermalStorage = "Coil:Cooling:DX:SingleSpeed:ThermalStorage"
    EvaporativeCoolerDirectCelDekPad = "EvaporativeCooler:Direct:CelDekPad"
    EvaporativeCoolerIndirectCelDekPad = "EvaporativeCooler:Indirect:CelDekPad"
    EvaporativeCoolerIndirectWetCoil = "EvaporativeCooler:Indirect:WetCoil"
    EvaporativeCoolerIndirectResearchSpecial = "EvaporativeCooler:Indirect:ResearchSpecial"
    EvaporativeCoolerDirectResearchSpecial = "EvaporativeCooler:Direct:ResearchSpecial"
    HumidifierSteamElectric = "Humidifier:Steam:Electric"
    DehumidifierDesiccantNoFans = "Dehumidifier:Desiccant:NoFans"
    DehumidifierDesiccantSystem = "Dehumidifier:Desiccant:System"
    HeatExchangerAirToAirFlatPlate = "HeatExchanger:AirToAir:FlatPlate"
    HeatExchangerAirToAirSensibleAndLatent = "HeatExchanger:AirToAir:SensibleAndLatent"
    HeatExchangerDesiccantBalancedFlow = "HeatExchanger:Desiccant:BalancedFlow"
    HeatExchangerDesiccantBalancedFlowPerformanceDataType1 = "HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"
    AirLoopHvacUnitarySystem = "AirLoopHVAC:UnitarySystem"
    UnitarySystemPerformanceHeatPumpMultispeed = "UnitarySystemPerformance:HeatPump:Multispeed"
    AirLoopHvacUnitaryFurnaceHeatOnly = "AirLoopHVAC:Unitary:Furnace:HeatOnly"
    AirLoopHvacUnitaryFurnaceHeatCool = "AirLoopHVAC:Unitary:Furnace:HeatCool"
    AirLoopHvacUnitaryHeatOnly = "AirLoopHVAC:UnitaryHeatOnly"
    AirLoopHvacUnitaryHeatCool = "AirLoopHVAC:UnitaryHeatCool"
    AirLoopHvacUnitaryHeatPumpAirToAir = "AirLoopHVAC:UnitaryHeatPump:AirToAir"
    AirLoopHvacUnitaryHeatPumpWaterToAir = "AirLoopHVAC:UnitaryHeatPump:WaterToAir"
    AirLoopHvacUnitaryHeatCoolVavchangeoverBypass = "AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass"
    AirLoopHvacUnitaryHeatPumpAirToAirMultiSpeed = "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed"
    AirConditionerVariableRefrigerantFlow = "AirConditioner:VariableRefrigerantFlow"
    ZoneTerminalUnitList = "ZoneTerminalUnitList"
    ControllerWaterCoil = "Controller:WaterCoil"
    ControllerOutdoorAir = "Controller:OutdoorAir"
    ControllerMechanicalVentilation = "Controller:MechanicalVentilation"
    AirLoopHvacControllerList = "AirLoopHVAC:ControllerList"
    AirLoopHvac = "AirLoopHVAC"
    AirLoopHvacOutdoorAirSystemEquipmentList = "AirLoopHVAC:OutdoorAirSystem:EquipmentList"
    AirLoopHvacOutdoorAirSystem = "AirLoopHVAC:OutdoorAirSystem"
    OutdoorAirMixer = "OutdoorAir:Mixer"
    AirLoopHvacZoneSplitter = "AirLoopHVAC:ZoneSplitter"
    AirLoopHvacSupplyPlenum = "AirLoopHVAC:SupplyPlenum"
    AirLoopHvacSupplyPath = "AirLoopHVAC:SupplyPath"
    AirLoopHvacZoneMixer = "AirLoopHVAC:ZoneMixer"
    AirLoopHvacReturnPlenum = "AirLoopHVAC:ReturnPlenum"
    AirLoopHvacReturnPath = "AirLoopHVAC:ReturnPath"
    Branch = "Branch"
    BranchList = "BranchList"
    ConnectorSplitter = "Connector:Splitter"
    ConnectorMixer = "Connector:Mixer"
    ConnectorList = "ConnectorList"
    NodeList = "NodeList"
    OutdoorAirNode = "OutdoorAir:Node"
    OutdoorAirNodeList = "OutdoorAir:NodeList"
    PipeAdiabatic = "Pipe:Adiabatic"
    PipeAdiabaticSteam = "Pipe:Adiabatic:Steam"
    PipeIndoor = "Pipe:Indoor"
    PipeOutdoor = "Pipe:Outdoor"
    PipeUnderground = "Pipe:Underground"
    PipingSystemUndergroundDomain = "PipingSystem:Underground:Domain"
    PipingSystemUndergroundPipeCircuit = "PipingSystem:Underground:PipeCircuit"
    PipingSystemUndergroundPipeSegment = "PipingSystem:Underground:PipeSegment"
    Duct = "Duct"
    PumpVariableSpeed = "Pump:VariableSpeed"
    PumpConstantSpeed = "Pump:ConstantSpeed"
    PumpVariableSpeedCondensate = "Pump:VariableSpeed:Condensate"
    HeaderedPumpsConstantSpeed = "HeaderedPumps:ConstantSpeed"
    HeaderedPumpsVariableSpeed = "HeaderedPumps:VariableSpeed"
    TemperingValve = "TemperingValve"
    LoadProfilePlant = "LoadProfile:Plant"
    SolarCollectorPerformanceFlatPlate = "SolarCollectorPerformance:FlatPlate"
    SolarCollectorFlatPlateWater = "SolarCollector:FlatPlate:Water"
    SolarCollectorFlatPlatePhotovoltaicThermal = "SolarCollector:FlatPlate:PhotovoltaicThermal"
    SolarCollectorPerformancePhotovoltaicThermalSimple = "SolarCollectorPerformance:PhotovoltaicThermal:Simple"
    SolarCollectorIntegralCollectorStorage = "SolarCollector:IntegralCollectorStorage"
    SolarCollectorPerformanceIntegralCollectorStorage = "SolarCollectorPerformance:IntegralCollectorStorage"
    SolarCollectorUnglazedTranspired = "SolarCollector:UnglazedTranspired"
    SolarCollectorUnglazedTranspiredMultisystem = "SolarCollector:UnglazedTranspired:Multisystem"
    BoilerHotWater = "Boiler:HotWater"
    BoilerSteam = "Boiler:Steam"
    ChillerElectricEir = "Chiller:Electric:EIR"
    ChillerElectricReformulatedEir = "Chiller:Electric:ReformulatedEIR"
    ChillerElectric = "Chiller:Electric"
    ChillerAbsorptionIndirect = "Chiller:Absorption:Indirect"
    ChillerAbsorption = "Chiller:Absorption"
    ChillerConstantCop = "Chiller:ConstantCOP"
    ChillerEngineDriven = "Chiller:EngineDriven"
    ChillerCombustionTurbine = "Chiller:CombustionTurbine"
    ChillerHeaterAbsorptionDirectFired = "ChillerHeater:Absorption:DirectFired"
    ChillerHeaterAbsorptionDoubleEffect = "ChillerHeater:Absorption:DoubleEffect"
    HeatPumpWaterToWaterEquationFitHeating = "HeatPump:WaterToWater:EquationFit:Heating"
    HeatPumpWaterToWaterEquationFitCooling = "HeatPump:WaterToWater:EquationFit:Cooling"
    HeatPumpWaterToWaterParameterEstimationCooling = "HeatPump:WaterToWater:ParameterEstimation:Cooling"
    HeatPumpWaterToWaterParameterEstimationHeating = "HeatPump:WaterToWater:ParameterEstimation:Heating"
    DistrictCooling = "DistrictCooling"
    DistrictHeating = "DistrictHeating"
    PlantComponentTemperatureSource = "PlantComponent:TemperatureSource"
    CentralHeatPumpSystem = "CentralHeatPumpSystem"
    ChillerHeaterPerformanceElectricEir = "ChillerHeaterPerformance:Electric:EIR"
    CoolingTowerSingleSpeed = "CoolingTower:SingleSpeed"
    CoolingTowerTwoSpeed = "CoolingTower:TwoSpeed"
    CoolingTowerVariableSpeedMerkel = "CoolingTower:VariableSpeed:Merkel"
    CoolingTowerVariableSpeed = "CoolingTower:VariableSpeed"
    CoolingTowerPerformanceCoolTools = "CoolingTowerPerformance:CoolTools"
    CoolingTowerPerformanceYorkCalc = "CoolingTowerPerformance:YorkCalc"
    EvaporativeFluidCoolerSingleSpeed = "EvaporativeFluidCooler:SingleSpeed"
    EvaporativeFluidCoolerTwoSpeed = "EvaporativeFluidCooler:TwoSpeed"
    FluidCoolerSingleSpeed = "FluidCooler:SingleSpeed"
    FluidCoolerTwoSpeed = "FluidCooler:TwoSpeed"
    GroundHeatExchangerVertical = "GroundHeatExchanger:Vertical"
    GroundHeatExchangerPond = "GroundHeatExchanger:Pond"
    GroundHeatExchangerSurface = "GroundHeatExchanger:Surface"
    GroundHeatExchangerHorizontalTrench = "GroundHeatExchanger:HorizontalTrench"
    HeatExchangerFluidToFluid = "HeatExchanger:FluidToFluid"
    WaterHeaterMixed = "WaterHeater:Mixed"
    WaterHeaterStratified = "WaterHeater:Stratified"
    WaterHeaterSizing = "WaterHeater:Sizing"
    WaterHeaterHeatPump = "WaterHeater:HeatPump"
    ThermalStorageIceSimple = "ThermalStorage:Ice:Simple"
    ThermalStorageIceDetailed = "ThermalStorage:Ice:Detailed"
    ThermalStorageChilledWaterMixed = "ThermalStorage:ChilledWater:Mixed"
    ThermalStorageChilledWaterStratified = "ThermalStorage:ChilledWater:Stratified"
    PlantLoop = "PlantLoop"
    CondenserLoop = "CondenserLoop"
    PlantEquipmentList = "PlantEquipmentList"
    CondenserEquipmentList = "CondenserEquipmentList"
    PlantEquipmentOperationUncontrolled = "PlantEquipmentOperation:Uncontrolled"
    PlantEquipmentOperationCoolingLoad = "PlantEquipmentOperation:CoolingLoad"
    PlantEquipmentOperationHeatingLoad = "PlantEquipmentOperation:HeatingLoad"
    PlantEquipmentOperationOutdoorDryBulb = "PlantEquipmentOperation:OutdoorDryBulb"
    PlantEquipmentOperationOutdoorWetBulb = "PlantEquipmentOperation:OutdoorWetBulb"
    PlantEquipmentOperationOutdoorRelativeHumidity = "PlantEquipmentOperation:OutdoorRelativeHumidity"
    PlantEquipmentOperationOutdoorDewpoint = "PlantEquipmentOperation:OutdoorDewpoint"
    PlantEquipmentOperationComponentSetpoint = "PlantEquipmentOperation:ComponentSetpoint"
    PlantEquipmentOperationOutdoorDryBulbDifference = "PlantEquipmentOperation:OutdoorDryBulbDifference"
    PlantEquipmentOperationOutdoorWetBulbDifference = "PlantEquipmentOperation:OutdoorWetBulbDifference"
    PlantEquipmentOperationOutdoorDewpointDifference = "PlantEquipmentOperation:OutdoorDewpointDifference"
    PlantEquipmentOperationSchemes = "PlantEquipmentOperationSchemes"
    CondenserEquipmentOperationSchemes = "CondenserEquipmentOperationSchemes"
    EnergyManagementSystemSensor = "EnergyManagementSystem:Sensor"
    EnergyManagementSystemActuator = "EnergyManagementSystem:Actuator"
    EnergyManagementSystemProgramCallingManager = "EnergyManagementSystem:ProgramCallingManager"
    EnergyManagementSystemProgram = "EnergyManagementSystem:Program"
    EnergyManagementSystemSubroutine = "EnergyManagementSystem:Subroutine"
    EnergyManagementSystemGlobalVariable = "EnergyManagementSystem:GlobalVariable"
    EnergyManagementSystemOutputVariable = "EnergyManagementSystem:OutputVariable"
    EnergyManagementSystemMeteredOutputVariable = "EnergyManagementSystem:MeteredOutputVariable"
    EnergyManagementSystemTrendVariable = "EnergyManagementSystem:TrendVariable"
    EnergyManagementSystemInternalVariable = "EnergyManagementSystem:InternalVariable"
    EnergyManagementSystemCurveOrTableIndexVariable = "EnergyManagementSystem:CurveOrTableIndexVariable"
    EnergyManagementSystemConstructionIndexVariable = "EnergyManagementSystem:ConstructionIndexVariable"
    ExternalInterface = "ExternalInterface"
    ExternalInterfaceSchedule = "ExternalInterface:Schedule"
    ExternalInterfaceVariable = "ExternalInterface:Variable"
    ExternalInterfaceActuator = "ExternalInterface:Actuator"
    ExternalInterfaceFunctionalMockupUnitImport = "ExternalInterface:FunctionalMockupUnitImport"
    ExternalInterfaceFunctionalMockupUnitImportFromVariable = "ExternalInterface:FunctionalMockupUnitImport:From:Variable"
    ExternalInterfaceFunctionalMockupUnitImportToSchedule = "ExternalInterface:FunctionalMockupUnitImport:To:Schedule"
    ExternalInterfaceFunctionalMockupUnitImportToActuator = "ExternalInterface:FunctionalMockupUnitImport:To:Actuator"
    ExternalInterfaceFunctionalMockupUnitImportToVariable = "ExternalInterface:FunctionalMockupUnitImport:To:Variable"
    ExternalInterfaceFunctionalMockupUnitExportFromVariable = "ExternalInterface:FunctionalMockupUnitExport:From:Variable"
    ExternalInterfaceFunctionalMockupUnitExportToSchedule = "ExternalInterface:FunctionalMockupUnitExport:To:Schedule"
    ExternalInterfaceFunctionalMockupUnitExportToActuator = "ExternalInterface:FunctionalMockupUnitExport:To:Actuator"
    ExternalInterfaceFunctionalMockupUnitExportToVariable = "ExternalInterface:FunctionalMockupUnitExport:To:Variable"
    ZoneHvacForcedAirUserDefined = "ZoneHVAC:ForcedAir:UserDefined"
    AirTerminalSingleDuctUserDefined = "AirTerminal:SingleDuct:UserDefined"
    CoilUserDefined = "Coil:UserDefined"
    PlantComponentUserDefined = "PlantComponent:UserDefined"
    PlantEquipmentOperationUserDefined = "PlantEquipmentOperation:UserDefined"
    AvailabilityManagerScheduled = "AvailabilityManager:Scheduled"
    AvailabilityManagerScheduledOn = "AvailabilityManager:ScheduledOn"
    AvailabilityManagerScheduledOff = "AvailabilityManager:ScheduledOff"
    AvailabilityManagerOptimumStart = "AvailabilityManager:OptimumStart"
    AvailabilityManagerNightCycle = "AvailabilityManager:NightCycle"
    AvailabilityManagerDifferentialThermostat = "AvailabilityManager:DifferentialThermostat"
    AvailabilityManagerHighTemperatureTurnOff = "AvailabilityManager:HighTemperatureTurnOff"
    AvailabilityManagerHighTemperatureTurnOn = "AvailabilityManager:HighTemperatureTurnOn"
    AvailabilityManagerLowTemperatureTurnOff = "AvailabilityManager:LowTemperatureTurnOff"
    AvailabilityManagerLowTemperatureTurnOn = "AvailabilityManager:LowTemperatureTurnOn"
    AvailabilityManagerNightVentilation = "AvailabilityManager:NightVentilation"
    AvailabilityManagerHybridVentilation = "AvailabilityManager:HybridVentilation"
    AvailabilityManagerAssignmentList = "AvailabilityManagerAssignmentList"
    SetpointManagerScheduled = "SetpointManager:Scheduled"
    SetpointManagerScheduledDualSetpoint = "SetpointManager:Scheduled:DualSetpoint"
    SetpointManagerOutdoorAirReset = "SetpointManager:OutdoorAirReset"
    SetpointManagerSingleZoneReheat = "SetpointManager:SingleZone:Reheat"
    SetpointManagerSingleZoneHeating = "SetpointManager:SingleZone:Heating"
    SetpointManagerSingleZoneCooling = "SetpointManager:SingleZone:Cooling"
    SetpointManagerSingleZoneHumidityMinimum = "SetpointManager:SingleZone:Humidity:Minimum"
    SetpointManagerSingleZoneHumidityMaximum = "SetpointManager:SingleZone:Humidity:Maximum"
    SetpointManagerMixedAir = "SetpointManager:MixedAir"
    SetpointManagerOutdoorAirPretreat = "SetpointManager:OutdoorAirPretreat"
    SetpointManagerWarmest = "SetpointManager:Warmest"
    SetpointManagerColdest = "SetpointManager:Coldest"
    SetpointManagerReturnAirBypassFlow = "SetpointManager:ReturnAirBypassFlow"
    SetpointManagerWarmestTemperatureFlow = "SetpointManager:WarmestTemperatureFlow"
    SetpointManagerMultiZoneHeatingAverage = "SetpointManager:MultiZone:Heating:Average"
    SetpointManagerMultiZoneCoolingAverage = "SetpointManager:MultiZone:Cooling:Average"
    SetpointManagerMultiZoneMinimumHumidityAverage = "SetpointManager:MultiZone:MinimumHumidity:Average"
    SetpointManagerMultiZoneMaximumHumidityAverage = "SetpointManager:MultiZone:MaximumHumidity:Average"
    SetpointManagerMultiZoneHumidityMinimum = "SetpointManager:MultiZone:Humidity:Minimum"
    SetpointManagerMultiZoneHumidityMaximum = "SetpointManager:MultiZone:Humidity:Maximum"
    SetpointManagerFollowOutdoorAirTemperature = "SetpointManager:FollowOutdoorAirTemperature"
    SetpointManagerFollowSystemNodeTemperature = "SetpointManager:FollowSystemNodeTemperature"
    SetpointManagerFollowGroundTemperature = "SetpointManager:FollowGroundTemperature"
    SetpointManagerCondenserEnteringReset = "SetpointManager:CondenserEnteringReset"
    SetpointManagerCondenserEnteringResetIdeal = "SetpointManager:CondenserEnteringReset:Ideal"
    SetpointManagerSingleZoneOneStageCooling = "SetpointManager:SingleZone:OneStageCooling"
    SetpointManagerSingleZoneOneStageHeating = "SetpointManager:SingleZone:OneStageHeating"
    RefrigerationCase = "Refrigeration:Case"
    RefrigerationCompressorRack = "Refrigeration:CompressorRack"
    RefrigerationCaseAndWalkInList = "Refrigeration:CaseAndWalkInList"
    RefrigerationCondenserAirCooled = "Refrigeration:Condenser:AirCooled"
    RefrigerationCondenserEvaporativeCooled = "Refrigeration:Condenser:EvaporativeCooled"
    RefrigerationCondenserWaterCooled = "Refrigeration:Condenser:WaterCooled"
    RefrigerationCondenserCascade = "Refrigeration:Condenser:Cascade"
    RefrigerationGasCoolerAirCooled = "Refrigeration:GasCooler:AirCooled"
    RefrigerationTransferLoadList = "Refrigeration:TransferLoadList"
    RefrigerationSubcooler = "Refrigeration:Subcooler"
    RefrigerationCompressor = "Refrigeration:Compressor"
    RefrigerationCompressorList = "Refrigeration:CompressorList"
    RefrigerationSystem = "Refrigeration:System"
    RefrigerationTranscriticalSystem = "Refrigeration:TranscriticalSystem"
    RefrigerationSecondarySystem = "Refrigeration:SecondarySystem"
    RefrigerationWalkIn = "Refrigeration:WalkIn"
    RefrigerationAirChiller = "Refrigeration:AirChiller"
    ZoneHvacRefrigerationChillerSet = "ZoneHVAC:RefrigerationChillerSet"
    DemandManagerAssignmentList = "DemandManagerAssignmentList"
    DemandManagerExteriorLights = "DemandManager:ExteriorLights"
    DemandManagerLights = "DemandManager:Lights"
    DemandManagerElectricEquipment = "DemandManager:ElectricEquipment"
    DemandManagerThermostats = "DemandManager:Thermostats"
    GeneratorInternalCombustionEngine = "Generator:InternalCombustionEngine"
    GeneratorCombustionTurbine = "Generator:CombustionTurbine"
    GeneratorMicroTurbine = "Generator:MicroTurbine"
    GeneratorPhotovoltaic = "Generator:Photovoltaic"
    PhotovoltaicPerformanceSimple = "PhotovoltaicPerformance:Simple"
    PhotovoltaicPerformanceEquivalentOneDiode = "PhotovoltaicPerformance:EquivalentOne-Diode"
    PhotovoltaicPerformanceSandia = "PhotovoltaicPerformance:Sandia"
    GeneratorFuelCell = "Generator:FuelCell"
    GeneratorFuelCellPowerModule = "Generator:FuelCell:PowerModule"
    GeneratorFuelCellAirSupply = "Generator:FuelCell:AirSupply"
    GeneratorFuelCellWaterSupply = "Generator:FuelCell:WaterSupply"
    GeneratorFuelCellAuxiliaryHeater = "Generator:FuelCell:AuxiliaryHeater"
    GeneratorFuelCellExhaustGasToWaterHeatExchanger = "Generator:FuelCell:ExhaustGasToWaterHeatExchanger"
    GeneratorFuelCellElectricalStorage = "Generator:FuelCell:ElectricalStorage"
    GeneratorFuelCellInverter = "Generator:FuelCell:Inverter"
    GeneratorFuelCellStackCooler = "Generator:FuelCell:StackCooler"
    GeneratorMicroChp = "Generator:MicroCHP"
    GeneratorMicroChpNonNormalizedParameters = "Generator:MicroCHP:NonNormalizedParameters"
    GeneratorFuelSupply = "Generator:FuelSupply"
    GeneratorWindTurbine = "Generator:WindTurbine"
    ElectricLoadCenterGenerators = "ElectricLoadCenter:Generators"
    ElectricLoadCenterInverterSimple = "ElectricLoadCenter:Inverter:Simple"
    ElectricLoadCenterInverterFunctionOfPower = "ElectricLoadCenter:Inverter:FunctionOfPower"
    ElectricLoadCenterInverterLookUpTable = "ElectricLoadCenter:Inverter:LookUpTable"
    ElectricLoadCenterStorageSimple = "ElectricLoadCenter:Storage:Simple"
    ElectricLoadCenterStorageBattery = "ElectricLoadCenter:Storage:Battery"
    ElectricLoadCenterTransformer = "ElectricLoadCenter:Transformer"
    ElectricLoadCenterDistribution = "ElectricLoadCenter:Distribution"
    WaterUseEquipment = "WaterUse:Equipment"
    WaterUseConnections = "WaterUse:Connections"
    WaterUseStorage = "WaterUse:Storage"
    WaterUseWell = "WaterUse:Well"
    WaterUseRainCollector = "WaterUse:RainCollector"
    FaultModelTemperatureSensorOffsetOutdoorAir = "FaultModel:TemperatureSensorOffset:OutdoorAir"
    FaultModelHumiditySensorOffsetOutdoorAir = "FaultModel:HumiditySensorOffset:OutdoorAir"
    FaultModelEnthalpySensorOffsetOutdoorAir = "FaultModel:EnthalpySensorOffset:OutdoorAir"
    FaultModelPressureSensorOffsetOutdoorAir = "FaultModel:PressureSensorOffset:OutdoorAir"
    FaultModelTemperatureSensorOffsetReturnAir = "FaultModel:TemperatureSensorOffset:ReturnAir"
    FaultModelEnthalpySensorOffsetReturnAir = "FaultModel:EnthalpySensorOffset:ReturnAir"
    FaultModelFoulingCoil = "FaultModel:Fouling:Coil"
    MatrixTwoDimension = "Matrix:TwoDimension"
    CurveLinear = "Curve:Linear"
    CurveQuadLinear = "Curve:QuadLinear"
    CurveQuadratic = "Curve:Quadratic"
    CurveCubic = "Curve:Cubic"
    CurveQuartic = "Curve:Quartic"
    CurveExponent = "Curve:Exponent"
    CurveBicubic = "Curve:Bicubic"
    CurveBiquadratic = "Curve:Biquadratic"
    CurveQuadraticLinear = "Curve:QuadraticLinear"
    CurveTriquadratic = "Curve:Triquadratic"
    CurveFunctionalPressureDrop = "Curve:Functional:PressureDrop"
    CurveFanPressureRise = "Curve:FanPressureRise"
    CurveExponentialSkewNormal = "Curve:ExponentialSkewNormal"
    CurveSigmoid = "Curve:Sigmoid"
    CurveRectangularHyperbola1 = "Curve:RectangularHyperbola1"
    CurveRectangularHyperbola2 = "Curve:RectangularHyperbola2"
    CurveExponentialDecay = "Curve:ExponentialDecay"
    CurveDoubleExponentialDecay = "Curve:DoubleExponentialDecay"
    TableOneIndependentVariable = "Table:OneIndependentVariable"
    TableTwoIndependentVariables = "Table:TwoIndependentVariables"
    TableMultiVariableLookup = "Table:MultiVariableLookup"
    FluidPropertiesName = "FluidProperties:Name"
    FluidPropertiesGlycolConcentration = "FluidProperties:GlycolConcentration"
    FluidPropertiesTemperatures = "FluidProperties:Temperatures"
    FluidPropertiesSaturated = "FluidProperties:Saturated"
    FluidPropertiesSuperheated = "FluidProperties:Superheated"
    FluidPropertiesConcentration = "FluidProperties:Concentration"
    CurrencyType = "CurrencyType"
    ComponentCostAdjustments = "ComponentCost:Adjustments"
    ComponentCostReference = "ComponentCost:Reference"
    ComponentCostLineItem = "ComponentCost:LineItem"
    UtilityCostTariff = "UtilityCost:Tariff"
    UtilityCostQualify = "UtilityCost:Qualify"
    UtilityCostChargeSimple = "UtilityCost:Charge:Simple"
    UtilityCostChargeBlock = "UtilityCost:Charge:Block"
    UtilityCostRatchet = "UtilityCost:Ratchet"
    UtilityCostVariable = "UtilityCost:Variable"
    UtilityCostComputation = "UtilityCost:Computation"
    LifeCycleCostParameters = "LifeCycleCost:Parameters"
    LifeCycleCostRecurringCosts = "LifeCycleCost:RecurringCosts"
    LifeCycleCostNonrecurringCost = "LifeCycleCost:NonrecurringCost"
    LifeCycleCostUsePriceEscalation = "LifeCycleCost:UsePriceEscalation"
    LifeCycleCostUseAdjustment = "LifeCycleCost:UseAdjustment"
    ParametricSetValueForRun = "Parametric:SetValueForRun"
    ParametricLogic = "Parametric:Logic"
    ParametricRunControl = "Parametric:RunControl"
    ParametricFileNameSuffix = "Parametric:FileNameSuffix"
    OutputVariableDictionary = "Output:VariableDictionary"
    OutputSurfacesList = "Output:Surfaces:List"
    OutputSurfacesDrawing = "Output:Surfaces:Drawing"
    OutputSchedules = "Output:Schedules"
    OutputConstructions = "Output:Constructions"
    OutputEnergyManagementSystem = "Output:EnergyManagementSystem"
    OutputControlSurfaceColorScheme = "OutputControl:SurfaceColorScheme"
    OutputTableSummaryReports = "Output:Table:SummaryReports"
    OutputTableTimeBins = "Output:Table:TimeBins"
    OutputTableMonthly = "Output:Table:Monthly"
    OutputControlTableStyle = "OutputControl:Table:Style"
    OutputControlReportingTolerances = "OutputControl:ReportingTolerances"
    OutputVariable = "Output:Variable"
    OutputMeter = "Output:Meter"
    OutputMeterMeterFileOnly = "Output:Meter:MeterFileOnly"
    OutputMeterCumulative = "Output:Meter:Cumulative"
    OutputMeterCumulativeMeterFileOnly = "Output:Meter:Cumulative:MeterFileOnly"
    MeterCustom = "Meter:Custom"
    MeterCustomDecrement = "Meter:CustomDecrement"
    OutputSqlite = "Output:SQLite"
    OutputEnvironmentalImpactFactors = "Output:EnvironmentalImpactFactors"
    EnvironmentalImpactFactors = "EnvironmentalImpactFactors"
    FuelFactors = "FuelFactors"
    OutputDiagnostics = "Output:Diagnostics"
    OutputDebuggingData = "Output:DebuggingData"
    OutputPreprocessorMessage = "Output:PreprocessorMessage"